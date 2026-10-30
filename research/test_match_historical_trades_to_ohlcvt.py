import tempfile
import unittest
import zipfile
from pathlib import Path
from match_historical_trades_to_ohlcvt import parse_member, aggregate, compare


class TradeMatchingTests(unittest.TestCase):
    def test_schema_not_verified_abstains(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"trades.zip"
            with zipfile.ZipFile(p, "w") as z: z.writestr("XBTUSD.csv", "300,100,2\n")
            with zipfile.ZipFile(p) as z:
                with self.assertRaises(RuntimeError): parse_member(z, "XBTUSD.csv")

    def test_parse_three_column_fixture_only(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"trades.zip"
            with zipfile.ZipFile(p, "w") as z: z.writestr("XBTUSD.csv", "300,100,2\n301,101,3\n")
            with zipfile.ZipFile(p) as z:
                rows = parse_member(z, "XBTUSD.csv", schema_verified=True)
            self.assertEqual(len(rows), 2)

    def test_parse_wrong_shape_fails(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"trades.zip"
            with zipfile.ZipFile(p, "w") as z: z.writestr("XBTUSD.csv", "300,100,2,extra\n")
            with zipfile.ZipFile(p) as z:
                with self.assertRaises(ValueError): parse_member(z, "XBTUSD.csv", schema_verified=True)

    def test_aggregate_correct_fixture(self):
        a, _ = aggregate([(300,100,2,0),(301,101,3,1)])
        self.assertEqual(a[300], (300,100,101,100,101,5,2))

    def test_unverified_completeness_abstains(self):
        r = compare([(300,100,101,100,101,5,2)], [(300,100,2,0),(301,101,3,1)])
        self.assertEqual(r["verified_intervals"], 0)

    def test_fixture_exact_match(self):
        r = compare([(300,100,101,100,101,5,2)], [(300,100,2,0),(301,101,3,1)],
                    independently_complete=True)
        self.assertEqual(r["status"], "exact_trade_candle_match")

    def test_fixture_missing_trade_interval_fails(self):
        r = compare([(600,100,100,100,100,1,1)], [(300,100,1,0)], independently_complete=True)
        self.assertEqual(r["status"], "missing_trade_interval")


if __name__ == "__main__":
    unittest.main()
