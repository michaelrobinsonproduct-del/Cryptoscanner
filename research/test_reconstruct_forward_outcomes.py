import unittest
from reconstruct_forward_outcomes import Candle, reconstruct

def series(n, high=100, volume=10):
    return [Candle(i * 300, high, 100, volume) for i in range(n)]

class Tests(unittest.TestCase):
    def test_full_48h_and_thresholds(self):
        rows = series(577)
        rows[10] = Candle(3000, 131, 100, 10)
        result = reconstruct(rows, 0)
        for h in ("1", "6", "24", "48"):
            self.assertEqual(result["horizons"][h]["status"], "mature")
            self.assertTrue(result["horizons"][h]["hit_30"])
    def test_no_future_leakage_at_boundary(self):
        rows = series(577)
        rows[13] = Candle(3900, 150, 100, 10)
        result = reconstruct(rows, 0)
        self.assertFalse(result["horizons"]["1"]["hit_10"])
        self.assertTrue(result["horizons"]["6"]["hit_30"])
    def test_missing_interval_abstains(self):
        rows = [c for c in series(577) if c.timestamp != 600]
        self.assertEqual(reconstruct(rows, 0)["horizons"]["1"]["status"], "gap")
        self.assertEqual(reconstruct(rows, 0)["horizons"]["6"]["status"], "gap")
    def test_immature(self):
        self.assertEqual(reconstruct(series(12), 0)["horizons"]["1"]["status"], "immature")
    def test_missing_end_abstains(self):
        rows = [c for c in series(577) if c.timestamp != 3600]
        self.assertEqual(reconstruct(rows, 0)["horizons"]["1"]["status"], "gap")
    def test_liquidity_gate(self):
        self.assertEqual(reconstruct(series(577, volume=0), 0, min_quote_volume=100)["status"], "insufficient_entry_liquidity")
    def test_duplicates_rejected(self):
        with self.assertRaises(ValueError):
            reconstruct(series(2) + [series(2)[0]], 0)
    def test_invalid_price_rejected(self):
        with self.assertRaises(ValueError):
            reconstruct([Candle(0, 1, 2, 10)], 0)
    def test_missing_entry(self):
        self.assertEqual(reconstruct(series(577)[1:], 0)["status"], "missing_entry")
    def test_timestamp_alignment(self):
        with self.assertRaises(ValueError):
            reconstruct(series(577), 1)

if __name__ == "__main__":
    unittest.main()
