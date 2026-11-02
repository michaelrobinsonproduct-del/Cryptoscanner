import unittest
from simple_scanner.shadow_learning import assess_challenger_promotion

class GateTests(unittest.TestCase):
    def test_empty(self):
        x = assess_challenger_promotion({"status": "INSUFFICIENT_MATURED_HISTORY"})
        self.assertFalse(x["promotion_eligible"])

    def test_historical_improvement_is_not_enough(self):
        metrics = {k: {"events": 30, "challenger_recall": 0.9, "baseline_recall": 0.5} for k in ("20pct_1h", "50pct_1h", "100pct_1h")}
        x = assess_challenger_promotion({"status": "HISTORICAL_HOLDOUT_EVALUATED", "metrics": metrics})
        self.assertFalse(x["promotion_eligible"])
        self.assertFalse(x["live_weights_modified"])

if __name__ == "__main__":
    unittest.main()
