"""Focused real-paper E1/E2/E3 bridge acceptance."""
import copy
import unittest
from unittest.mock import patch

from research.public_paper_learning_bridge import evaluate


class PaperBridgeTests(unittest.TestCase):
    def setUp(self):
        self.ledger = {
            "sha256": "a" * 64,
            "predictions": [{"prediction_id": "b" * 64, "baseline_score": 0.2,
                             "challenger_score": 0.3}],
            "observations": [{"pair": "XBTUSD"}],
            "outcomes": [
                {"prediction_id": "b" * 64, "horizon_hours": 1,
                 "status": "MATURED_OBSERVED"},
                {"prediction_id": "b" * 64, "horizon_hours": 6,
                 "status": "ABSTAIN_GAP"}],
        }

    @patch("research.public_paper_learning_bridge.verify")
    def test_real_paper_is_not_falsely_promoted(self, verify):
        result = evaluate(self.ledger)
        verify.assert_called_once()
        self.assertEqual(result["horizons"]["1"]["paper_status_counts"], {"MATURED_OBSERVED": 1})
        self.assertEqual(result["horizons"]["6"]["paper_status_counts"], {"ABSTAIN_GAP": 1})
        self.assertEqual(result["horizons"]["24"]["authenticated_entry_labels"], 0)
        self.assertEqual(result["shadow_decision"]["decision"], "KEEP_BASELINE")
        self.assertEqual(result["shadow_decision"]["held_out_lift"], None)
        self.assertFalse(result["production_applied"])

    @patch("research.public_paper_learning_bridge.verify")
    def test_source_claims_and_orphan_outcomes_fail_closed(self, verify):
        modified = copy.deepcopy(self.ledger)
        modified["predictions"][0].update(
            {"source_sha256": "c" * 64, "score_observed_at": 1,
             "entry_first_observed_at": 2})
        with self.assertRaisesRegex(ValueError, "verified depth binder"):
            evaluate(modified)
        modified = copy.deepcopy(self.ledger)
        modified["outcomes"][0]["prediction_id"] = "d" * 64
        with self.assertRaisesRegex(ValueError, "orphan"):
            evaluate(modified)


if __name__ == "__main__":
    unittest.main()
