import unittest
from simple_scanner.replay_quality import validate_replay

class ReplayQualityTests(unittest.TestCase):
    def setUp(self):
        self.replay={"scope":"FULL_MARKET_PRICES_ONLY","feature_parity_verified":False}
        self.comparison={"scope":"PRICE_ONLY_NOT_FEATURE_PARITY","holdout_cohorts":50,
                         "breakouts":30,"baseline_recall":0.2,"challenger_recall":0.3}
    def test_price_only_never_promotes(self):
        r=validate_replay(self.replay,self.comparison)
        self.assertFalse(r["valid"])
        self.assertFalse(r["promotion_eligible"])
    def test_insufficient_holdout(self):
        self.comparison["holdout_cohorts"]=3
        self.assertIn("insufficient_holdout_cohorts",validate_replay(self.replay,self.comparison)["reasons"])
    def test_invalid_recall(self):
        self.comparison["challenger_recall"]=float("nan")
        self.assertIn("invalid_challenger_recall",validate_replay(self.replay,self.comparison)["reasons"])
    def test_missing_inputs(self):
        self.assertFalse(validate_replay(None,None)["valid"])
    def test_never_promotes_even_if_feature_parity_claimed(self):
        self.replay["feature_parity_verified"]=True
        r=validate_replay(self.replay,self.comparison)
        self.assertTrue(r["valid"])
        self.assertFalse(r["promotion_eligible"])
