import unittest
from reconstruct_forward_outcomes import Candle, reconstruct, reconstruct_as_of

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

    def test_exact_horizon_end_excludes_next_candle_all_horizons(self):
        for h in (1, 6, 24, 48):
            rows = series(578)
            after = h * 12 + 1
            rows[after] = Candle(after * 300, 190, 100, 10)
            result = reconstruct(rows, 0)
            self.assertFalse(result["horizons"][str(h)]["hit_10"])

    def test_missing_intermediate_candle_abstains_all_horizons(self):
        for h in (1, 6, 24, 48):
            missing = h * 12 - 1
            rows = [c for c in series(577) if c.timestamp != missing * 300]
            result = reconstruct(rows, 0)
            self.assertEqual(result["horizons"][str(h)]["status"], "gap")

    def test_no_trade_gap_is_not_assumed_flat(self):
        rows = [c for c in series(577) if c.timestamp != 300]
        result = reconstruct(rows, 0)
        self.assertEqual(result["horizons"]["1"]["status"], "gap")
        self.assertNotIn("hit_10", result["horizons"]["1"])

    def test_future_high_only_after_entry_not_entry_high(self):
        rows = series(577)
        rows[0] = Candle(0, 200, 100, 10)
        result = reconstruct(rows, 0)
        self.assertFalse(result["horizons"]["48"]["hit_10"])

    def test_exact_threshold_at_all_horizons(self):
        for h in (1, 6, 24, 48):
            rows = series(577)
            rows[h * 12] = Candle(h * 3600, 130, 100, 10)
            result = reconstruct(rows, 0)
            self.assertTrue(result["horizons"][str(h)]["hit_30"])

    def test_liquidity_at_entry_only_not_future(self):
        rows = series(577)
        rows[0] = Candle(0, 100, 100, 1)
        rows[1] = Candle(300, 100, 100, 1000)
        result = reconstruct(rows, 0, min_quote_volume=101)
        self.assertEqual(result["status"], "insufficient_entry_liquidity")

    def test_source_open_timestamp_requires_explicit_observation_provenance(self):
        # Kraken OHLCVT timestamps label the candle opening; the candle's close
        # and full volume are unavailable at the opening instant. The legacy
        # reconstruct() API has no observation-as-of or candle-close provenance
        # parameter, so do not treat its fixture success as live PIT validation.
        from inspect import signature
        self.assertNotIn("as_of_timestamp", signature(reconstruct).parameters)

    def test_as_of_requires_source_timestamp_semantics(self):
        self.assertEqual(reconstruct_as_of(series(578), 300)["status"], "unverified_source_timestamp_semantics")
        self.assertEqual(reconstruct_as_of(series(578), 300, source_timestamp_semantics="candle_close_utc")["status"], "unverified_source_timestamp_semantics")

    def test_as_of_closed_entry_and_all_four_horizons(self):
        rows = series(578)
        rows[0] = Candle(0, 200, 100, 10)
        rows[12] = Candle(3600, 130, 100, 10)
        result = reconstruct_as_of(rows, 300, source_timestamp_semantics="candle_open_utc")
        self.assertEqual(result["entry_source_open"], 0)
        self.assertEqual(result["observation_as_of"], 300)
        for h in ("1", "6", "24", "48"):
            self.assertEqual(result["horizons"][h]["status"], "mature")
            self.assertTrue(result["horizons"][h]["hit_30"])

    def test_as_of_excludes_first_candle_after_one_hour(self):
        rows = series(578)
        rows[13] = Candle(3900, 190, 100, 10)
        result = reconstruct_as_of(rows, 300, source_timestamp_semantics="candle_open_utc")
        self.assertFalse(result["horizons"]["1"]["hit_10"])
        self.assertTrue(result["horizons"]["6"]["hit_30"])

    def test_as_of_missing_no_trade_interval_abstains(self):
        rows = [c for c in series(578) if c.timestamp != 600]
        result = reconstruct_as_of(rows, 300, source_timestamp_semantics="candle_open_utc")
        for h in ("1", "6", "24", "48"):
            self.assertEqual(result["horizons"][h]["status"], "gap")

    def test_as_of_liquidity_uses_only_closed_entry(self):
        rows = series(578)
        rows[0] = Candle(0, 100, 100, 0)
        rows[1] = Candle(300, 100, 100, 1000)
        result = reconstruct_as_of(rows, 300, min_quote_volume=1, source_timestamp_semantics="candle_open_utc")
        self.assertEqual(result["status"], "insufficient_entry_liquidity")

    def test_as_of_requires_completed_48h_end(self):
        result = reconstruct_as_of(series(576), 300, source_timestamp_semantics="candle_open_utc")
        self.assertEqual(result["horizons"]["48"]["status"], "immature")

if __name__ == "__main__":
    unittest.main()
