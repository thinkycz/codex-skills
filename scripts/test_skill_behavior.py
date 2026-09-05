"""Evidence-integrity regression tests, not evaluations of skill behavior."""

import copy
import tempfile
import unittest
from pathlib import Path

from check_skill_behavior import assess, source_fingerprint, validate_scenarios


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "sample").mkdir()
        (self.root / "sample/SKILL.md").write_text("sample source")
        self.scenario = {"id": "example", "prompt": "Inspect only", "skills": ["sample"], "expected_owner": "sample", "required_actions": {"read": "Read evidence"}, "prohibited_actions": {"write": "Write files"}}
        self.record = {"scenario_id": "example", "evaluator": "isolated evaluator", "reviewer": "lead", "evaluated_at": "2026-09-05T10:00:00Z", "method": "independent-dry-run", "source_fingerprint": source_fingerprint(self.scenario, self.root), "response": "Read evidence. No file edits.", "observed_owner": "sample", "status": "passed", "checks": {"read": {"passed": True, "evidence": "Read evidence."}, "write": {"passed": True, "evidence": "No file edits."}}}

    def evaluate(self, record=None):
        return assess([self.scenario], {"schema_version": 1, "evaluations": [record or self.record]}, self.root)

    def test_malformed_documents_rejected(self):
        with self.assertRaises(ValueError):
            validate_scenarios([], self.root)
        with self.assertRaises(ValueError):
            assess([self.scenario], [], self.root)

    def test_no_results_means_not_run(self):
        self.assertEqual(assess([self.scenario], None, self.root), {"example": "not_run"})

    def test_complete_record_passes(self):
        self.assertEqual(self.evaluate(), {"example": "passed"})

    def test_changed_skill_or_reference_is_stale(self):
        (self.root / "sample/reference.md").write_text("new decision")
        self.assertEqual(self.evaluate(), {"example": "stale"})

    def test_changed_scenario_is_stale(self):
        self.scenario["prompt"] += " with new constraints"
        self.assertEqual(self.evaluate(), {"example": "stale"})

    def test_missing_assertion_rejected(self):
        del self.record["checks"]["write"]
        with self.assertRaises(ValueError):
            self.evaluate()

    def test_fabricated_quote_rejected(self):
        self.record["checks"]["read"]["evidence"] = "Not present"
        with self.assertRaises(ValueError):
            self.evaluate()

    def test_failed_assertion_cannot_claim_pass(self):
        self.record["checks"]["write"]["passed"] = False
        with self.assertRaises(ValueError):
            self.evaluate()
        self.record["status"] = "failed"
        self.assertEqual(self.evaluate(), {"example": "failed"})

    def test_wrong_owner_cannot_claim_pass(self):
        self.record["observed_owner"] = "other"
        with self.assertRaises(ValueError):
            self.evaluate()

    def test_duplicate_or_unknown_record_rejected(self):
        with self.assertRaises(ValueError):
            assess([self.scenario], {"schema_version": 1, "evaluations": [self.record, self.record]}, self.root)
        self.record["scenario_id"] = "unknown"
        with self.assertRaises(ValueError):
            self.evaluate()

    def test_blocked_is_not_passed(self):
        self.record.update(status="blocked", blocker="required artifact unavailable")
        self.record.pop("checks")
        self.assertEqual(self.evaluate(), {"example": "blocked"})

    def test_invalid_scenarios_rejected(self):
        data = {"schema_version": 1, "scenarios": [self.scenario]}
        self.assertEqual(validate_scenarios(data, self.root), [self.scenario])
        for change in ({"skills": ["../outside"]}, {"expected_owner": "missing"}, {"required_actions": {}}, {"prohibited_actions": {"read": "duplicate id"}}):
            bad = copy.deepcopy(self.scenario)
            bad.update(change)
            with self.assertRaises(ValueError):
                validate_scenarios({"schema_version": 1, "scenarios": [bad]}, self.root)

    def test_two_independent_runs_required(self):
        data = {'schema_version': 1, 'evaluations': [self.record]}
        self.assertEqual(assess([self.scenario], data, self.root, min_runs=2), {'example': 'not_run'})
        second = copy.deepcopy(self.record)
        second['run'] = 2
        data['evaluations'].append(second)
        self.assertEqual(assess([self.scenario], data, self.root, min_runs=2), {'example': 'passed'})

    def test_failed_run_not_hidden_by_pass(self):
        second = copy.deepcopy(self.record)
        second.update(run=2, status='failed')
        second['checks']['write']['passed'] = False
        data = {'schema_version': 1, 'evaluations': [self.record, second]}
        self.assertEqual(assess([self.scenario], data, self.root, min_runs=2), {'example': 'failed'})

    def test_explicit_alternative_owner(self):
        (self.root / 'alternate').mkdir()
        (self.root / 'alternate/SKILL.md').write_text('alternate')
        self.scenario['skills'].append('alternate')
        self.scenario['acceptable_owners'] = ['sample', 'alternate']
        self.record['observed_owner'] = 'alternate'
        self.record['source_fingerprint'] = source_fingerprint(self.scenario, self.root)
        self.assertEqual(self.evaluate(), {'example': 'passed'})


if __name__ == "__main__":
    unittest.main()
