import unittest
from simple_scanner.replay_comparison import compare_replay

class ReplayComparisonTests(unittest.TestCase):
    def test_equal_budget_and_no_promotion(self):
        rows=[]
        for i in range(50):
            t=f"2026-10-{1+i//24:02d}T{i%24:02d}:00:00+00:00"
            rows.extend([
                {"run_at":t,"pair":"A","prior_momentum_pct":1,
                 "future_gain_pct":0,"baseline_selected":True,"breakout":False},
                {"run_at":t,"pair":"B","prior_momentum_pct":3,
                 "future_gain_pct":8,"baseline_selected":False,"breakout":True}
            ])
        r=compare_replay(rows)
        self.assertEqual(r["baseline_hits"],0)
        self.assertGreater(r["challenger_hits"],0)
        self.assertEqual(r["challenger_recall"],1)
        self.assertFalse(r["promotion_eligible"])
        self.assertFalse(r["live_weights_modified"])
    def test_no_budget_no_picks(self):
        rows=[{"run_at":"t","pair":"B","prior_momentum_pct":3,
               "future_gain_pct":8,"baseline_selected":False,"breakout":True}]
        self.assertEqual(compare_replay(rows)["challenger_hits"],0)
    def test_empty_holdout(self):
        r=compare_replay([])
        self.assertIsNone(r["challenger_recall"])
        self.assertFalse(r["promotion_eligible"])
