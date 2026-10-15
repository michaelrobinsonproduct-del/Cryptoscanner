"""Promotion safety tests: no change to live scanner."""
import unittest
from simple_scanner.promotion_gate import decide_promotion

def good():
    return {h: {"cohorts": 50, "delta_pct": 0.2, "breakout_recall_delta": 0.01}
            for h in (1,3,6,24)}

class PromotionGateTests(unittest.TestCase):
    def test_eligible_but_never_mutates(self):
        r=decide_promotion(good(),history_integrity="ok",dex_errors=0)
        self.assertTrue(r["eligible"])
        self.assertFalse(r["live_weights_modified"])
        self.assertFalse(r["buy_approved"])
    def test_missing_horizon_rejected(self):
        x=good(); del x[24]
        self.assertFalse(decide_promotion(x,history_integrity="ok",dex_errors=0)["eligible"])
    def test_holdout_regression_rejected(self):
        x=good(); x[3]["delta_pct"]=-0.01
        self.assertFalse(decide_promotion(x,history_integrity="ok",dex_errors=0)["eligible"])
    def test_breakout_recall_regression_rejected(self):
        x=good(); x[6]["breakout_recall_delta"]=-0.01
        self.assertFalse(decide_promotion(x,history_integrity="ok",dex_errors=0)["eligible"])
    def test_data_or_dex_failure_rejected(self):
        self.assertFalse(decide_promotion(good(),history_integrity="bad",dex_errors=0)["eligible"])
        self.assertFalse(decide_promotion(good(),history_integrity="ok",dex_errors=1)["eligible"])
    def test_nonfinite_and_small_samples_rejected(self):
        x=good(); x[1]["delta_pct"]=float("nan"); x[24]["cohorts"]=3
        self.assertFalse(decide_promotion(x,history_integrity="ok",dex_errors=0)["eligible"])
    def test_duplicate_pending_promotion_rejected(self):
        self.assertFalse(decide_promotion(good(),history_integrity="ok",dex_errors=0,prior_approved=True)["eligible"])
