import unittest
from simple_scanner.ticker_feature_capture import extract_features

STAMP="2026-10-15T12:00:00+00:00"
def ticker(last="102",bid="101",ask="102",opening="100",volume="2000"):
    return {"c":[last],"b":[bid],"a":[ask],"o":opening,"v":["0",volume]}

class CaptureTests(unittest.TestCase):
    def test_valid_universe(self):
        eligible={"A":{},"B":{}}
        data={"A":ticker(),"B":ticker(last="110")}
        before=str(data)
        result=extract_features(eligible,data,observed_at=STAMP)
        self.assertEqual(len(result["records"]),2)
        self.assertEqual(result["coverage_pct"],100)
        self.assertEqual(str(data),before)
        self.assertFalse(result["production_modified"])
        self.assertFalse(result["buy_approved"])
    def test_rejects_missing_and_crossed(self):
        result=extract_features({"A":{},"B":{}},{"A":ticker(bid="110",ask="100")},observed_at=STAMP)
        self.assertEqual(len(result["records"]),0)
        self.assertEqual(set(result["rejected"]),{"A","B"})
    def test_rejects_nonfinite(self):
        result=extract_features({"A":{}},{"A":ticker(last="nan")},observed_at=STAMP)
        self.assertEqual(len(result["records"]),0)
    def test_empty(self):
        self.assertEqual(extract_features({}, {},observed_at=STAMP)["coverage_pct"],0)
