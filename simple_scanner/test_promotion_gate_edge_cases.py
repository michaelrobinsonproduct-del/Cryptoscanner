"""Additional isolated promotion gate safety tests."""
import unittest
from simple_scanner.promotion_gate import decide_promotion

class EdgeCases(unittest.TestCase):
    def setUp(self):
        self.rows={h:{"cohorts":60,"delta_pct":0.2,"breakout_recall_delta":0.01} for h in (1,3,6,24)}
    def decision(self, **kwargs):
        return decide_promotion(self.rows,history_integrity="ok",dex_errors=0,**kwargs)
    def test_no_missing_recall(self):
        self.rows[24].pop("breakout_recall_delta")
        self.assertFalse(self.decision()["eligible"])
    def test_no_negative_recall(self):
        self.rows[1]["breakout_recall_delta"]=-0.0001
        self.assertFalse(self.decision()["eligible"])
    def test_no_small_return_improvement(self):
        self.rows[6]["delta_pct"]=0.099
        self.assertFalse(self.decision()["eligible"])
    def test_no_invalid_cohorts(self):
        self.rows[3]["cohorts"]=True
        self.assertFalse(self.decision()["eligible"])
    def test_never_approves_buys(self):
        r=self.decision()
        self.assertFalse(r["buy_approved"])
        self.assertFalse(r["live_weights_modified"])
