"""Batch 2: isolated regression checks for shadow research ranking and promotion."""
import math
import unittest
from simple_scanner.shadow_learning import (
    score, compare, early_accumulation_rank, assess_challenger_promotion
)

class Batch2ResearchSafetyTests(unittest.TestCase):
    def test_score_caps_extreme_momentum_and_volume(self):
        row = ("run", "PAIR", 1e9, 1e9, 60.0, 0.0)
        self.assertEqual(score(row, 8, 15), 100.0)

    def test_compare_keeps_equal_cohort_budget(self):
        rows = [
            ("t1", "A", 0, 1, 90, -5),
            ("t1", "B", 3, 2, 80, 8),
            ("t2", "A", 0, 1, 90, -4),
            ("t2", "B", 3, 2, 80, 7),
        ]
        result = compare(rows, 8, 15)
        self.assertEqual(result["cohorts"], 2)
        self.assertEqual(result["base_avg_pct"], -4.5)
        self.assertEqual(result["challenger_avg_pct"], 7.5)
        self.assertEqual(result["delta_pct"], 12.0)

    def test_early_rank_rejects_invalid_and_illiquid_rows(self):
        rows = [
            ("GOOD", 1.5, 20, 200000, 1.0, 1.02),
            ("NAN", float("nan"), 20, 200000, 1.0, 1.02),
            ("ZERO", 1.5, 20, 200000, 0, 1.02),
            ("ILLIQUID", 1.5, 20, 24999, 1.0, 1.02),
            ("SPREAD", 1.5, 126, 200000, 1.0, 1.02),
            ("EXTENDED", 13, 20, 200000, 1.0, 1.02),
            ("CHASE", 1.5, 20, 200000, 1.0, 1.06),
        ]
        result = early_accumulation_rank(rows)
        self.assertEqual([x["pair"] for x in result], ["GOOD"])

    def test_promotion_blocked_without_forward_evidence(self):
        metrics = {k: {"events": 100, "baseline_recall": 0.1, "challenger_recall": 0.9}
                   for k in ("20pct_1h", "50pct_1h", "100pct_1h")}
        result = assess_challenger_promotion({
            "status": "HISTORICAL_HOLDOUT_EVALUATED", "metrics": metrics
        })
        self.assertFalse(result["promotion_eligible"])
        self.assertFalse(result["live_weights_modified"])
        self.assertIn("prospective_validation_pending", result["reasons"])
        self.assertIn("equal_budget_comparison_pending", result["reasons"])

    def test_promotion_blocked_for_missing_history(self):
        result = assess_challenger_promotion({"status": "INSUFFICIENT_MATURED_HISTORY"})
        self.assertEqual(result["status"], "BLOCKED_INSUFFICIENT_EVIDENCE")
        self.assertFalse(result["promotion_eligible"])

if __name__ == "__main__":
    unittest.main()
