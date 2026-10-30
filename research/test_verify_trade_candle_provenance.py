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


if __name__ == "__main__":
    unittest.main()
