#!/usr/bin/env python3
"""Validate declared owners, modes and dependencies; never execute fixture prompts."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURES_PATH = ROOT / 'scripts/fixtures/skill-routing-fixtures.json'

def contained_file(base, reference):
    path = (base / reference).resolve()
    return base.resolve() in path.parents and path.is_file()

def validate_contracts(root=ROOT):
    contracts = json.loads((root / 'routing-contracts.json').read_text())
    packages = {p.name for p in root.iterdir() if (p / 'SKILL.md').is_file()}
    owners = contracts['skills']
    errors = []
    if set(owners) != packages:
        errors.append('Contract owners do not exactly match active packages.')
    for name, contract in owners.items():
        for mode, reference in contract['modes'].items():
            if not mode or (reference and not contained_file(root / name, reference)):
                errors.append(f'{name}/{mode}: missing mode reference')
        for dependency in contract['dependencies']:
            if dependency not in owners:
                errors.append(f'{name}: missing local dependency {dependency}')
    migration_path = root / 'migration-map.json'
    if migration_path.exists():
        migration = json.loads(migration_path.read_text())
        entries = migration['entries']
        if len(entries) != migration['original_count'] or len({e['old_name'] for e in entries}) != len(entries):
            errors.append('Migration does not account for every original capability exactly once.')
        if len(packages) != migration['active_count'] or {e['replacement'] for e in entries} != packages:
            errors.append('Migration destinations do not match active packages.')
        for entry in entries:
            owner = entry['replacement']
            if owner not in owners or entry['mode'] not in owners[owner]['modes'] or not contained_file(root, entry['reference_destination']):
                errors.append(f'Invalid migration destination: {entry["old_name"]}')
    fixtures = json.loads((root / 'scripts/fixtures/skill-routing-fixtures.json').read_text())
    for cluster in fixtures['clusters']:
        for skill in cluster['skills']:
            if skill['id'] not in owners:
                errors.append(f"Unknown fixture skill: {skill['id']}")
            for dependency in skill.get('dependencies', []):
                if dependency not in owners.get(skill['id'], {}).get('dependencies', []):
                    errors.append(f'Undeclared fixture dependency: {dependency}')
            for fixture in skill['fixtures']:
                owner = fixture['expected_owner']
                if owner not in owners or fixture['mode'] not in owners[owner]['modes']:
                    errors.append(f'Invalid fixture owner/mode: {owner}/{fixture["mode"]}')
    return errors, fixtures

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verbose', action='store_true')
    args = parser.parse_args()
    try:
        errors, fixtures = validate_contracts()
    except (ValueError, KeyError, OSError) as exc:
        print(f'Static routing check failed: {exc}')
        return 1
    for error in errors:
        print(error)
    if args.verbose:
        print(json.dumps(fixtures, indent=2))
    print(f'Static owner/mode/dependency checks: {len(errors)} errors. No model evaluation performed.')
    return bool(errors)

if __name__ == '__main__':
    raise SystemExit(main())
