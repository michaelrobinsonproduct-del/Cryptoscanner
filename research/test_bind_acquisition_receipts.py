import unittest
from unittest.mock import patch

from research.bind_acquisition_receipts import bind

SHA = "a" * 64
ROW = {"pair": "XBTUSD", "source_sha256": SHA,
       "first_observed_at": 1000, "entry_liquidity_usd": 25}
PRED = {"prediction_id": "b" * 64, "pair": "XBTUSD",
        "baseline_score": 10.0, "challenger_score": 12.0}
RECEIPT = {**PRED, "source_sha256": SHA, "score_observed_at": 999}


class AcquisitionBindingTests(unittest.TestCase):
    def run_binding(self, receipts, row=ROW):
        with patch("research.bind_acquisition_receipts.verify"), patch(
            "research.bind_acquisition_receipts.verified_rows",
            return_value=([row], [])):
            return bind({"predictions": [PRED]}, "unused", receipts)

    def test_end_to_end_independent_source_binding(self):
        result = self.run_binding([RECEIPT])
        self.assertEqual(result["accepted_count"], 1)
        self.assertEqual(result["excluded_count"], 0)
        self.assertEqual(result["accepted"][0]["entry_first_observed_at"], 1000)
        self.assertFalse(result["production_applied"])

    def test_missing_or_mismatched_source_abstains(self):
        result = self.run_binding([{**RECEIPT, "source_sha256": "c" * 64}])
        self.assertEqual(result["accepted_count"], 0)
        self.assertEqual(result["excluded"][0]["reason"], "NO_VERIFIED_DEPTH_SOURCE")

    def test_late_score_and_unverified_liquidity_abstain(self):
        self.assertEqual(self.run_binding([{**RECEIPT, "score_observed_at": 1001}])
                         ["excluded"][0]["reason"], "SCORE_NOT_PRE_ENTRY")
        self.assertEqual(self.run_binding([RECEIPT], {**ROW, "entry_liquidity_usd": 1})
                         ["excluded"][0]["reason"], "INSUFFICIENT_VERIFIED_LIQUIDITY")

    def test_score_mutation_and_duplicate_fail_closed(self):
        self.assertEqual(self.run_binding([{**RECEIPT, "challenger_score": 999}])
                         ["excluded"][0]["reason"], "SCORE_IDENTITY_MISMATCH")
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.run_binding([RECEIPT, RECEIPT])


if __name__ == "__main__":
    unittest.main()
