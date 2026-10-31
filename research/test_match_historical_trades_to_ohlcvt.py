import tempfile
import unittest
import zipfile
from pathlib import Path
from match_historical_trades_to_ohlcvt import parse_member, aggregate, compare


class TradeMatchingTests(unittest.TestCase):
    def test_schema_not_verified_abstains(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"trades.zip"
            with zipfile.ZipFile(p, "w") as z: z.writestr("XBTUSD.csv", "timestamp,price,volume,type,order_type,misc,trade_id\n300,100,2,b,l,,id1\n")
            with zipfile.ZipFile(p) as z:
                with self.assertRaises(RuntimeError): parse_member(z, "XBTUSD.csv")

    def test_parse_three_column_fixture_only(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"trades.zip"
            with zipfile.ZipFile(p, "w") as z: z.writestr("XBTUSD.csv", "timestamp,price,volume,type,order_type,misc,trade_id\n300,100,2,b,l,,id1\n301,101,3,s,m,,id2\n")
            with zipfile.ZipFile(p) as z:
                rows = parse_member(z, "XBTUSD.csv", schema_verified=True)
            self.assertEqual(len(rows), 2)

    def test_parse_wrong_shape_fails(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"trades.zip"
            with zipfile.ZipFile(p, "w") as z: z.writestr("XBTUSD.csv", "timestamp,price,volume,type,order_type,misc,trade_id\n300,100,2,extra\n")
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

    def test_empty_ohlc_cannot_be_verified_even_with_completeness_claim(self):
        r = compare([], [(300,100,2,0)], independently_complete=True)
        self.assertEqual(r, {"status": "missing_ohlc_evidence", "verified_intervals": 0})

    def test_duplicate_ohlc_cannot_be_verified(self):
        row = (300,100,101,100,101,5,2)
        r = compare([row, row], [(300,100,2,0),(301,101,3,1)],
                    independently_complete=True)
        self.assertEqual(r["status"], "duplicate_ohlc_timestamp")
        self.assertEqual(r["verified_intervals"], 0)

    def test_unaligned_and_nonfinite_ohlc_timestamps_fail_closed(self):
        for bad in (301, float("nan"), float("inf"), -300, True, 300.5):
            with self.subTest(timestamp=bad):
                r = compare([(bad,100,101,100,101,5,2)],
                            [(300,100,2,0),(301,101,3,1)],
                            independently_complete=True)
                self.assertEqual(r["status"], "invalid_ohlc_timestamp")
                self.assertEqual(r["verified_intervals"], 0)

    def test_invalid_shape_fails_closed(self):
        r = compare([(300,100,101)], [(300,100,2,0)], independently_complete=True)
        self.assertEqual(r["status"], "invalid_ohlc_shape")

    def test_comparison_resource_cap(self):
        with self.assertRaises(ValueError):
            compare([(300,100,100,100,100,1,1)]*250001, [(300,100,1,0)],
                    independently_complete=True)

    def test_fixture_missing_trade_interval_fails(self):
        r = compare([(600,100,100,100,100,1,1)], [(300,100,1,0)], independently_complete=True)
        self.assertEqual(r["status"], "missing_trade_interval")


    def test_comparison_rejects_duplicate_trade_order_even_if_prices_match(self):
        candle = (300, 100, 101, 100, 101, 5, 2)
        trades = [(300, 100, 2, 0), (301, 101, 3, 0)]
        r = compare([candle], trades, independently_complete=True)
        self.assertEqual(r["status"], "invalid_evidence")
        self.assertEqual(r["verified_intervals"], 0)


    def test_micro_price_mismatch_is_not_exact_even_with_completeness_claim(self):
        candle = (300, 1e-8, 1e-8, 1e-8, 1e-8, 1e-12, 1)
        trade = [(301, 1.9e-8, 1e-12, 0)]
        r = compare([candle], trade, independently_complete=True)
        self.assertEqual(r["status"], "aggregation_mismatch")
        self.assertEqual(r["verified_intervals"], 0)

if __name__ == "__main__":
    unittest.main()
