import unittest
from verify_trade_candle_provenance import verify_open_boundary


class TradeBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.candle = (300, 100, 120, 90, 110, 5, 3)
        self.trades = [(301, 100, 1, 0), (450, 120, 2, 1), (599, 110, 2, 2)]

    def test_requires_independent_source(self):
        self.assertEqual(verify_open_boundary(self.candle, self.trades)["status"],
                         "unverified_independent_trade_source")

    def test_valid_exact_trades_verify_open_boundary(self):
        candle = (300, 100, 120, 100, 110, 5, 3)
        result = verify_open_boundary(candle, self.trades, independent_trade_source=True)
        self.assertEqual(result["status"], "verified_open_boundary")
        self.assertEqual(result["candle_close_as_of"], 600)

    def test_last_boundary_trade_excluded(self):
        trades = self.trades[:-1] + [(600, 110, 2, 2)]
        self.assertEqual(verify_open_boundary(self.candle, trades, independent_trade_source=True)["status"],
                         "timestamp_boundary_mismatch")

    def test_incomplete_trade_sample_abstains(self):
        self.assertEqual(verify_open_boundary(self.candle, self.trades[:2], independent_trade_source=True)["status"],
                         "incomplete_evidence")

    def test_incorrect_volume_abstains(self):
        candle = (300, 100, 120, 100, 110, 50, 3)
        self.assertEqual(verify_open_boundary(candle, self.trades, independent_trade_source=True)["status"],
                         "aggregation_mismatch")

    def test_open_high_low_close_mismatch_abstains(self):
        self.assertEqual(verify_open_boundary(self.candle, self.trades, independent_trade_source=True)["status"],
                         "aggregation_mismatch")

    def test_unaligned_timestamp_abstains(self):
        candle = (301, 100, 120, 100, 110, 5, 3)
        self.assertEqual(verify_open_boundary(candle, self.trades, independent_trade_source=True)["status"],
                         "incomplete_evidence")


    def test_bool_candle_fields_rejected(self):
        for i in (0, 1, 2, 3, 4, 5, 6):
            candle = list((300, 100, 120, 100, 110, 5, 3))
            candle[i] = True
            with self.subTest(field=i):
                self.assertNotEqual(verify_open_boundary(candle, self.trades,
                    independent_trade_source=True)["status"], "verified_open_boundary")

    def test_negative_or_fractional_candle_open_rejected(self):
        for timestamp in (-300, 300.5, 301):
            candle = (timestamp, 100, 120, 100, 110, 5, 3)
            with self.subTest(timestamp=timestamp):
                self.assertNotEqual(verify_open_boundary(candle, self.trades,
                    independent_trade_source=True)["status"], "verified_open_boundary")

    def test_noninteger_count_rejected(self):
        for count in (3.5, True, float("inf")):
            candle = (300, 100, 120, 100, 110, 5, count)
            with self.subTest(count=count):
                self.assertNotEqual(verify_open_boundary(candle, self.trades,
                    independent_trade_source=True)["status"], "verified_open_boundary")

    def test_inconsistent_ohlc_bounds_rejected(self):
        for candle in ((300, 100, 99, 100, 110, 5, 3),
                       (300, 100, 120, 111, 110, 5, 3),
                       (300, 0, 120, 0, 110, 5, 3)):
            with self.subTest(candle=candle):
                self.assertNotEqual(verify_open_boundary(candle, self.trades,
                    independent_trade_source=True)["status"], "verified_open_boundary")

    def test_duplicate_trade_stable_order_rejected(self):
        trades = [(301, 100, 1, 0), (450, 120, 2, 0), (599, 110, 2, 2)]
        self.assertEqual(verify_open_boundary((300, 100, 120, 100, 110, 5, 3),
            trades, independent_trade_source=True)["status"], "invalid_evidence")

    def test_fractional_or_negative_trade_order_rejected(self):
        for order in (1.5, -1, float("nan"), True):
            trades = [(301, 100, 1, 0), (450, 120, 2, order), (599, 110, 2, 2)]
            with self.subTest(order=order):
                self.assertEqual(verify_open_boundary((300, 100, 120, 100, 110, 5, 3),
                    trades, independent_trade_source=True)["status"], "invalid_evidence")

    def test_bool_or_nonfinite_trade_fields_rejected(self):
        for field, value in ((0, True), (1, float("nan")), (2, True), (3, float("inf"))):
            trades = list(self.trades)
            bad = list(trades[1])
            bad[field] = value
            trades[1] = tuple(bad)
            with self.subTest(field=field):
                self.assertEqual(verify_open_boundary((300, 100, 120, 100, 110, 5, 3),
                    trades, independent_trade_source=True)["status"], "invalid_evidence")

    def test_integer_valued_csv_floats_still_match(self):
        candle = (300.0, 100.0, 120.0, 100.0, 110.0, 5.0, 3.0)
        trades = [(301.0, 100.0, 1.0, 0.0),
                  (450.0, 120.0, 2.0, 1.0),
                  (599.0, 110.0, 2.0, 2.0)]
        self.assertEqual(verify_open_boundary(candle, trades,
            independent_trade_source=True)["status"], "verified_open_boundary")


if __name__ == "__main__":
    unittest.main()
