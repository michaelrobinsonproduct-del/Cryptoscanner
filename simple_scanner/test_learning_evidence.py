import unittest
from simple_scanner.learning_evidence import assess_evidence

def complete():
    return {"coverage":"FULL_MARKET_FEATURES","split":"CHRONOLOGICAL_UNSEEN",
            "feature_timestamps_verified":True,"market_outcome_coverage_verified":True,
            "horizons":{h:{"cohorts":50,"breakout_recall_delta":0.02,"delta_pct":0.1}
                        for h in (1,3,6,24)}}

class EvidenceTests(unittest.TestCase):
    def test_complete_evidence(self):
        self.assertTrue(assess_evidence(complete())["sufficient"])
    def test_watch_only_fails(self):
        x=complete();x["coverage"]="WATCH_CANDIDATES_ONLY"
        self.assertFalse(assess_evidence(x)["sufficient"])
    def test_random_split_fails(self):
        x=complete();x["split"]="RANDOM"
        self.assertFalse(assess_evidence(x)["sufficient"])
    def test_unverified_timestamps_fail(self):
        x=complete();x["feature_timestamps_verified"]=False
        self.assertFalse(assess_evidence(x)["sufficient"])
    def test_missing_horizon_fails(self):
        x=complete();del x["horizons"][24]
        self.assertFalse(assess_evidence(x)["sufficient"])
    def test_nonfinite_fails(self):
        x=complete();x["horizons"][1]["breakout_recall_delta"]=float("inf")
        self.assertFalse(assess_evidence(x)["sufficient"])
    def test_none_fails(self):
        self.assertFalse(assess_evidence(None)["sufficient"])
