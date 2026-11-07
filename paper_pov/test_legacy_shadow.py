"""Offline adversarial tests for independent legacy-inspired read-only strategy."""
import datetime as dt
import unittest

from paper_pov import legacy_shadow

UTC = dt.timezone.utc
NOW = dt.datetime(2026, 11, 1, 17, 30, tzinfo=UTC)
SOURCE = "a" * 40


def candle_rows(*, gap=False, future=False, empty=False):
    base = int(NOW.timestamp()) - 13 * 300 + (300 if future else 0)
    rows = []
    for i in range(13):
        start = base + i * 300 + (300 if gap and i >= 8 else 0)
        close = 1.9 + i * .006
        volume = 2 if i >= 7 else 1
        if empty and i == 8:
            volume = 0
        rows.append([start, close - .002, close + .003, close - .003,
                     close, close, volume, 0 if empty and i == 8 else 1])
    rows.append([rows[-1][0] + 300, 2, 2.1, 1.9, 2, 2, 1, 1])
    return rows


class FakeKraken:
    def __init__(self):
        self.pairs = {"P%02d" % i: {"status": "online", "wsname": "C%02d/USD" % i}
                      for i in range(25)}
        self.pairs["USDTUSD"] = {"status": "online", "wsname": "USDT/USD"}
        self.tickers = {key: {"c": ["2"], "b": ["1.999"], "a": ["2.001"],
                              "o": "1.9", "v": ["50000", "100000"], "t": ["500", "10000"]}
                        for key in self.pairs}
        self.rows = candle_rows()
        self.bad_ohlc = False
        self.calls = []

    def __call__(self, path):
        self.calls.append(path)
        if path == "AssetPairs":
            return self.pairs
        if path == "Ticker":
            return self.tickers
        if path.startswith("OHLC?pair="):
            pair = path.split("pair=")[1].split("&")[0]
            return {"WRONG" if self.bad_ohlc else pair: self.rows, "last": 1}
        raise AssertionError("Unexpected public endpoint")


def run(api=None, clock=None, **kwargs):
    return legacy_shadow.scan(api=api or FakeKraken(), clock=clock or (lambda: NOW),
                              sleep=lambda _: None, run_id="12345", source_sha=SOURCE,
                              trigger_paper_run_id="67890", **kwargs)


class LegacyShadowTests(unittest.TestCase):
    def test_independent_signal_schema_canonical_rank_and_no_score_relabel(self):
        api = FakeKraken()
        out = run(api)
        self.assertEqual(out["mode"], "LEGACY_INSPIRED_SHADOW")
        self.assertTrue(out["independent_execution"])
        self.assertEqual(out["status"], "WATCH_PAPER_ONLY")
        self.assertEqual(out["run_id"], "12345")
        self.assertEqual(out["trigger_paper_run_id"], "67890")
        self.assertEqual(out["eligible_usd_pairs"], 25)
        self.assertEqual(len(out["candidates"]), 12)
        self.assertEqual([x["rank"] for x in out["candidates"]], list(range(1, 13)))
        self.assertTrue(all(x["legacy_score"] > 0 for x in out["candidates"]))
        self.assertTrue(all(x["move1h_pct"] > x["move15_pct"] > 0 for x in out["candidates"]))
        self.assertEqual(out["momentum_1h_reference"], "last_closed_5m_close_over_close_12_intervals_earlier")
        self.assertEqual(out["volume_acceleration_reference"], "last_6_completed_5m_volume_over_previous_6_completed_5m_volume")
        self.assertEqual(out["volume_window_minutes"], 30)
        self.assertEqual(out["volume_units"], "Kraken OHLC base-asset units (not USD notional)")
        self.assertTrue(all(x["volume_current_30m"] == 12 for x in out["candidates"]))
        self.assertTrue(all(x["volume_baseline_previous_30m"] == 6 for x in out["candidates"]))
        self.assertTrue(all(x["trades_24h"] == 10000 for x in out["candidates"]))
        self.assertNotIn("USDT/USD", str(out["candidates"]))
        self.assertFalse(out["production_applied"])
        self.assertFalse(out["buy_approved"])
        self.assertFalse(out["trade_executed"])
        self.assertIsNone(out["held_out_lift"])
        self.assertNotIn("baseline_score", str(out))
        self.assertNotIn("challenger_score", str(out))
        self.assertEqual(len([x for x in api.calls if x.startswith("OHLC?")]), 16)

    def test_distinct_github_provenance_required(self):
        with self.assertRaisesRegex(ValueError, "distinct"):
            legacy_shadow.scan(api=FakeKraken(), clock=lambda: NOW, sleep=lambda _: None,
                               run_id="123", source_sha=SOURCE, trigger_paper_run_id="123")
        with self.assertRaisesRegex(ValueError, "distinct"):
            legacy_shadow.scan(api=FakeKraken(), clock=lambda: NOW, sleep=lambda _: None,
                               run_id="123", source_sha="bad", trigger_paper_run_id="456")

    def test_incomplete_ticker_coverage_abstains(self):
        api = FakeKraken()
        api.tickers = dict(list(api.tickers.items())[:3])
        with self.assertRaisesRegex(ValueError, "Incomplete"):
            run(api)

    def test_mismatched_ohlc_pair_never_generates_watch(self):
        api = FakeKraken()
        api.bad_ohlc = True
        report = run(api)
        self.assertEqual(report["candidates"], [])
        self.assertEqual(report["status"], "DATA_UNAVAILABLE")
        self.assertEqual(report["ohlc_rejection_reasons"]["OHLC pair identity mismatch"], 16)

    def test_advertised_kraken_altname_accepted(self):
        api = FakeKraken()
        for key, meta in api.pairs.items():
            meta["altname"] = "ALT" + key
        original = api.__call__
        def aliased(path):
            response = original(path)
            if path.startswith("OHLC?pair="):
                pair = path.split("pair=")[1].split("&")[0]
                return {"ALT" + pair: response[pair], "last": 1}
            return response
        report = run(api=aliased)
        self.assertEqual(report["status"], "WATCH_PAPER_ONLY")
        self.assertEqual(len(report["candidates"]), 12)

    def test_closed_candle_accumulation_preserves_real_momentum_and_volume(self):
        # Regression: escaped newlines in a comment previously swallowed
        # starts.append(), leaving OHLC rejected instead of evaluated.
        api = FakeKraken()
        move15, move60, accel, closed_at, current_volume, baseline_volume = legacy_shadow._closed_features(
            {"P00": api.rows, "last": 1}, "P00", NOW)
        self.assertAlmostEqual(move15, 100 * (api.rows[12][4] / api.rows[9][4] - 1))
        self.assertAlmostEqual(move60, 100 * (api.rows[12][4] / api.rows[0][4] - 1))
        self.assertAlmostEqual(accel, 12 / 6)
        self.assertEqual(closed_at, NOW)
        self.assertEqual(current_volume, 12)
        self.assertEqual(baseline_volume, 6)

    def test_gapped_ohlc_abstains(self):
        api = FakeKraken()
        api.rows = candle_rows(gap=True)
        self.assertEqual(run(api)["candidates"], [])

    def test_future_ohlc_abstains(self):
        api = FakeKraken()
        api.rows = candle_rows(future=True)
        self.assertEqual(run(api)["candidates"], [])

    def test_genuine_zero_trade_candle_is_accepted_without_inventing_volume(self):
        api = FakeKraken()
        api.rows = candle_rows(empty=True)
        report = run(api)
        self.assertEqual(report["status"], "WATCH_PAPER_ONLY")
        self.assertEqual(len(report["candidates"]), 12)

    def test_zero_trade_zero_vwap_kraken_bucket_is_accepted(self):
        api = FakeKraken()
        api.rows = candle_rows(empty=True)
        api.rows[8][5] = 0
        report = run(api)
        self.assertEqual(report["status"], "WATCH_PAPER_ONLY")
        self.assertEqual(len(report["candidates"]), 12)

    def test_positive_trade_zero_vwap_is_rejected(self):
        api = FakeKraken()
        api.rows = candle_rows()
        api.rows[8][5] = 0
        report = run(api)
        self.assertEqual(report["status"], "DATA_UNAVAILABLE")
        self.assertEqual(report["ohlc_rejection_reasons"]["Invalid or empty completed candle"], 16)

    def test_inconsistent_zero_trade_volume_abstains(self):
        api = FakeKraken()
        api.rows = candle_rows(empty=True)
        api.rows[8][7] = 1
        report = run(api)
        self.assertEqual(report["status"], "DATA_UNAVAILABLE")
        self.assertEqual(report["ohlc_rejection_reasons"]["Invalid or empty completed candle"], 16)

    def test_expired_ticker_fails_closed(self):
        calls = [0]
        def clock():
            calls[0] += 1
            return NOW if calls[0] <= 2 else NOW + dt.timedelta(minutes=12)
        with self.assertRaisesRegex(ValueError, "expired"):
            run(clock=clock)

    def test_duplicate_canonical_identity_fails_closed(self):
        api = FakeKraken()
        api.pairs["DUP"] = {"status": "online", "wsname": "C00/USD"}
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            run(api)

    def test_bounded_ohlc_requests(self):
        with self.assertRaisesRegex(ValueError, "Unbounded"):
            run(max_ohlc=1000)

    def test_nonfinite_or_negative_ticker_values_rejected(self):
        api = FakeKraken()
        api.tickers["P00"]["c"] = ["nan"]
        api.tickers["P01"]["v"] = ["0", "-1"]
        out = run(api)
        self.assertNotIn("C00/USD", [x["symbol"] for x in out["candidates"]])
        self.assertNotIn("C01/USD", [x["symbol"] for x in out["candidates"]])

    def test_invalid_trade_count_excluded(self):
        api = FakeKraken()
        api.tickers["P00"]["t"] = ["0", "-1"]
        out = run(api)
        self.assertNotIn("C00/USD", [x["symbol"] for x in out["candidates"]])

    def test_naive_clock_rejected(self):
        with self.assertRaisesRegex(ValueError, "clock"):
            run(clock=lambda: NOW.replace(tzinfo=None))


if __name__ == "__main__":
    unittest.main()
