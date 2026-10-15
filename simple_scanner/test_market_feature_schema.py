import unittest
from simple_scanner.market_feature_schema import validate_record

NOW="2026-10-15T12:00:00+00:00"
def good():
    return {"pair":"ABCUSD","observed_at":NOW,"price":2.5,
            "spread_bps":12.0,"notional_24h_usd":200000,
            "move_24h_pct":1.4}

class FeatureSchemaTests(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(validate_record(good(),observed_at=NOW)["valid"])
    def test_stale(self):
        x=good();x["observed_at"]="2026-10-15T11:50:00+00:00"
        self.assertFalse(validate_record(x,observed_at=NOW)["valid"])
    def test_future(self):
        x=good();x["observed_at"]="2026-10-15T12:01:00+00:00"
        self.assertFalse(validate_record(x,observed_at=NOW)["valid"])
    def test_nan(self):
        x=good();x["price"]=float("nan")
        self.assertFalse(validate_record(x,observed_at=NOW)["valid"])
    def test_missing(self):
        x=good();del x["pair"]
        self.assertFalse(validate_record(x,observed_at=NOW)["valid"])
    def test_naive(self):
        x=good();x["observed_at"]="2026-10-15T12:00:00"
        self.assertFalse(validate_record(x,observed_at=NOW)["valid"])
