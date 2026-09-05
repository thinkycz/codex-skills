"""Behavioral regressions for library tooling, using disposable fixtures only."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from export_universal_skills import export_skills, validate_destination, flatten_skill_content
from generated_artifacts import check_generated, semantic
from library_paths import source_files
from validate_skills import validate_references
from check_skill_routing import validate_contracts
from report_performance import record_metrics

class LibraryToolsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.root = self.base / 'source'
        self.root.mkdir()
        self.package = self.root / 'example'
        self.put('example/SKILL.md', '# Example\n\n[Detail](references/detail.md)\n')
        self.put('example/references/detail.md', '# Detail\n')
        self.put('example/agents/openai.yaml', 'interface:\n  default_prompt: "Use $example"\n')
        self.put('routing-contracts.json', json.dumps({'skills': {'example': {'modes': {'work': 'references/detail.md'}, 'dependencies': []}}, 'optional_external': []}))
        self.put('scripts/fixtures/skill-routing-fixtures.json', json.dumps({'clusters': [{'name': 'example', 'skills': [{'id': 'example', 'fixtures': [{'expected_owner': 'example', 'mode': 'work'}]}]}]}))

    def put(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def test_nested_missing_reference(self):
        self.put('example/references/detail.md', '[Missing](nested/missing.md)')
        self.assertTrue(any('missing local link' in e for e in validate_references(self.package)))

    def test_cross_package_reference(self):
        self.put('other/SKILL.md', '# Other')
        self.put('example/references/detail.md', '[Other](../../other/SKILL.md)')
        self.assertEqual(validate_references(self.package), [])

    def test_missing_named_dependency(self):
        self.put('routing-contracts.json', json.dumps({'skills': {'example': {'dependencies': ['absent']}}, 'optional_external': []}))
        self.assertIn('missing declared local dependency: absent', validate_references(self.package))

    def test_optional_external_dependency(self):
        self.put('example/references/detail.md', 'Use $external-skill if available.')
        self.assertTrue(validate_references(self.package))
        self.put('routing-contracts.json', json.dumps({'skills': {}, 'optional_external': ['external-skill']}))
        self.assertEqual(validate_references(self.package), [])

    def test_retired_agent_prompt(self):
        self.put('migration-map.json', json.dumps({'entries': [{'old_name': 'old-skill', 'replacement': 'example'}]}))
        self.put('example/agents/openai.yaml', 'default_prompt: "Use $old-skill"')
        self.assertTrue(any('retired skill name' in e for e in validate_references(self.package)))

    def test_contract_modes(self):
        self.assertEqual(validate_contracts(self.root)[0], [])
        (self.package / 'references/detail.md').unlink()
        self.assertTrue(validate_contracts(self.root)[0])

    def test_semantic_manifest_tampering(self):
        expected = {'skills.manifest.json': {'generated_at': 'new', 'included_skill_ids': ['example']}}
        self.put('skills.manifest.json', json.dumps({'generated_at': 'old', 'included_skill_ids': ['wrong']}))
        self.assertEqual(check_generated(self.root, expected), ['stale or tampered: skills.manifest.json'])

    def test_timestamp_only_is_not_stale(self):
        expected = {'skills.manifest.json': {'generated_at': 'new', 'included_skill_ids': ['example']}}
        self.put('skills.manifest.json', json.dumps({'generated_at': 'old', 'included_skill_ids': ['example']}))
        self.assertEqual(check_generated(self.root, expected), [])

    def test_missing_generated_file(self):
        self.assertEqual(check_generated(self.root, {'stocktake.report.md': 'expected'}), ['missing: stocktake.report.md'])

    def test_read_only_generated_check(self):
        self.put('skills.catalog.json', '{}')
        before = (self.root / 'skills.catalog.json').read_bytes()
        with patch.object(Path, 'write_text', side_effect=AssertionError('unexpected write')):
            self.assertTrue(check_generated(self.root, {'skills.catalog.json': {'skill_count': 1}}))
        self.assertEqual((self.root / 'skills.catalog.json').read_bytes(), before)

    def test_reject_overlap(self):
        for dest in (self.root, self.root / 'out', self.base):
            with self.subTest(dest=dest), self.assertRaises(ValueError):
                validate_destination(self.root, dest)

    def test_reject_symlink_overlap(self):
        alias = self.base / 'alias'
        alias.symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(ValueError):
            validate_destination(self.root, alias / 'out')

    def test_refuse_existing_destination_preserves_data(self):
        destination = self.base / 'out'
        destination.mkdir()
        marker = destination / 'user-data'
        marker.write_text('preserve')
        with self.assertRaises(ValueError):
            export_skills(destination, source_root=self.root)
        self.assertEqual(marker.read_text(), 'preserve')

    def test_complete_folder_export(self):
        self.put('example/scripts/helper.py', 'print("test")')
        asset = self.package / 'assets/icon.bin'
        asset.parent.mkdir()
        asset.write_bytes(b'\xff\x00')
        self.put('templates/shared.md', '# Shared')
        self.put('.system/vendor/SKILL.md', '# Vendor')
        destination = self.base / 'out'
        self.assertEqual(len(export_skills(destination, source_root=self.root)), 1)
        for path in source_files(self.package):
            self.assertEqual(path.read_bytes(), (destination / path.relative_to(self.root)).read_bytes())
        self.assertTrue((destination / 'templates/shared.md').is_file())
        self.assertFalse((destination / '.system').exists())

    def test_flatten_transitive_links_deduplicate(self):
        self.put('other/SKILL.md', '# Other\n[Detail](references/shared.md)')
        self.put('other/references/shared.md', '# UNIQUE-CONTENT')
        self.put('example/references/detail.md', '[Other](../../other/SKILL.md)\n[Again](../../other/SKILL.md)')
        text = flatten_skill_content(self.package, self.root)
        self.assertEqual(text.count('UNIQUE-CONTENT'), 1)
        self.assertNotIn('](../../other/', text)
        self.assertIn('](#file-', text)

    def test_cache_files_excluded(self):
        self.put('example/__pycache__/cache.pyc', 'noise')
        self.put('example/.DS_Store', 'noise')
        self.assertFalse(any(p.name in {'cache.pyc', '.DS_Store'} for p in source_files(self.package)))

    def test_flatten_named_dependencies(self):
        self.put('other/SKILL.md', '# Named dependency')
        self.put('routing-contracts.json', json.dumps({'skills': {'example': {'dependencies': ['other']}, 'other': {'dependencies': []}}}))
        self.put('example/references/detail.md', 'Use `other` when needed.')
        text = flatten_skill_content(self.package, self.root)
        self.assertIn('# Named dependency', text)
        self.assertIn('[other](#file-', text)

    def test_directory_symlinks_not_silently_omitted(self):
        directory = self.root / 'shared'
        directory.mkdir()
        (self.package / 'linked-assets').symlink_to(directory, target_is_directory=True)
        with self.assertRaises(ValueError):
            export_skills(self.base / 'out', source_root=self.root)

    def test_absolute_local_link_rejected(self):
        self.put('example/SKILL.md', '[Missing](/nonexistent/required.md)')
        self.assertTrue(any('nonportable local link' in e for e in validate_references(self.package)))
        with self.assertRaises(ValueError):
            flatten_skill_content(self.package, self.root)

    def test_unquoted_yaml_icon_checked(self):
        self.put('example/agents/openai.yaml', 'interface:\n  icon_small: ./assets/missing.png\n')
        self.assertTrue(any('missing local link' in e for e in validate_references(self.package)))

    def test_angle_bracket_link_rewritten(self):
        self.put('example/SKILL.md', '[Detail](<references/detail.md>)')
        text = flatten_skill_content(self.package, self.root)
        self.assertIn('[Detail](#file-', text)
        self.assertNotIn('](<references/', text)

    def test_flatten_directory_link_explicitly_refused(self):
        self.put('example/SKILL.md', '[Directory](references/)')
        with self.assertRaisesRegex(ValueError, 'Directory link unsupported'):
            flatten_skill_content(self.package, self.root)

    def test_mode_path_cannot_escape(self):
        outside = self.base / 'outside.md'
        outside.write_text('# outside')
        self.put('routing-contracts.json', json.dumps({'skills': {'example': {'modes': {'work': '../../outside.md'}, 'dependencies': []}}}))
        self.assertTrue(validate_contracts(self.root)[0])

    def test_load_aliases_cannot_inflate_measurement(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate resolved'):
            record_metrics(self.root, {'loaded_files': ['example/SKILL.md', 'example/../example/SKILL.md']})

    def test_export_escaping_symlink_refused(self):
        secret = self.base / 'outside'
        secret.write_text('private')
        (self.package / 'escape').symlink_to(secret)
        with self.assertRaises(ValueError):
            export_skills(self.base / 'out', source_root=self.root)
        self.assertFalse((self.base / 'out').exists())

if __name__ == '__main__':
    unittest.main()
