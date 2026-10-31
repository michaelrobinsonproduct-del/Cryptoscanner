"""Synthetic-only tests for read-only report provenance and abstention."""
import copy
import hashlib
import unittest

from paper_eval.report import report
from paper_eval.test_audit import scenario
from paper_pov import ledger

SHA = "b" * 40


class ReportTests(unittest.TestCase):
    def test_four_horizons_checksum_and_no_false_claims(self):
        state = scenario()
        result = report(state, SHA)
        self.assertEqual(set(result["horizons"]), {"1", "6", "24", "48"})
        self.assertEqual(result["ledger_sha256"], state["sha256"])
        self.assertEqual(result["ledger_commit"], SHA)
        self.assertEqual(result["horizons"]["1"]["comparable_runs"], 1)
        for h in ("6", "24", "48"):
            self.assertEqual(result["horizons"][h]["comparable_runs"], 0)
        self.assertIsNone(result["independent_held_out_lift"])
        self.assertFalse(result["production_applied"])
        digest = result.pop("report_sha256")
        self.assertEqual(digest, hashlib.sha256(ledger.canonical(result)).hexdigest())

    def test_exact_commit_provenance_required(self):
        state = scenario(offsets=(0,))
        for invalid in ("main", "A" * 40, "z" * 40, "a" * 39, "", None):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                report(state, invalid)

    def test_invalid_ledger_checksum_aborts(self):
        state = scenario(offsets=(0,))
        state["observations"][0]["price"] = 100
        with self.assertRaisesRegex(ValueError, "checksum"):
            report(state, SHA)

    def test_resealed_fabricated_matured_outcome_aborts(self):
        state = scenario()
        altered = copy.deepcopy(state)
        altered["outcomes"][0]["return_pct"] = 999
        ledger.seal(altered)
        with self.assertRaisesRegex(ValueError, "return disagrees"):
            report(altered, SHA)

    def test_gap_only_is_not_misreported_as_failure(self):
        state = scenario(offsets=(0, 120))
        result = report(state, SHA)
        self.assertEqual(result["horizons"]["1"]["comparable_runs"], 0)
        self.assertEqual(result["horizons"]["1"]["excluded_incomplete_or_gap"], 1)
        self.assertIsNone(result["horizons"]["1"]["baseline_observed_hit_rate"])


if __name__ == "__main__":
    unittest.main()
