"""Paper-only Kraken ticker time-reference and numeric-overflow regression tests.

All inputs are synthetic. No real market claims, ledger writes, or orders.
"""
import json
import unittest

from paper_pov import scanner
from paper_pov.test_scanner import NOW, fixture


def modified(*, ticker=None, ohlc=None):
    def api(path):
        response = fixture()(path)
        if path == "Ticker" and ticker is not None:
            ticker(response["C0USD"])
        if path.startswith("OHLC?pair=C0USD&") and ohlc is not None:
            ohlc(response["C0USD"])
        return response
    report = scanner.scan(api=api, clock=lambda: NOW, sleep=lambda _: None)
    # Derived arithmetic must never inject NaN/Infinity into a durable report.
    json.dumps(report, allow_nan=False)
    return report


def observed(report, pair="C0USD"):
    return {o["pair"] for o in report["observations"]}.__contains__(pair)


def watched(report, pair="C0USD"):
    return {p["pair"] for p in report["watch"]}.__contains__(pair)


class KrakenTickerSemanticsTests(unittest.TestCase):
    def test_today_open_not_mislabeled_rolling_24h(self):
        report = modified()
        self.assertEqual(report["ticker_move_reference"], "kraken_ticker_today_open_utc")
        self.assertTrue(watched(report))
        item = next(p for p in report["watch"] if p["pair"] == "C0USD")
        self.assertEqual(item["move_since_utc_open_pct"], 1.0)
        self.assertEqual(item["move_reference"], "kraken_ticker_today_open_utc")
        self.assertNotIn("move24_pct", item)
        self.assertIsNone(report["held_out_lift"])
        self.assertIs(report["production_applied"], False)

    def test_rolling_24h_vwap_does_not_redefine_today_open(self):
        def change(t):
            t["p"] = ["0.5", "0.25"]  # Kraken today/rolling-24h VWAP
        report = modified(ticker=change)
        item = next(p for p in report["watch"] if p["pair"] == "C0USD")
        self.assertEqual(item["move_since_utc_open_pct"], 1.0)

    def test_today_open_threshold_applied_without_fake_24h_move(self):
        def change(t):
            t["o"] = "1.009"  # ~0.1% since UTC day open: below paper gate
            t["p"] = ["0.5", "0.25"]
        report = modified(ticker=change)
        self.assertTrue(observed(report))
        self.assertFalse(watched(report))

    def test_zero_today_open_skips_bad_market_not_entire_scan(self):
        report = modified(ticker=lambda t: t.__setitem__("o", "0"))
        self.assertFalse(observed(report))
        self.assertFalse(watched(report))
        self.assertGreaterEqual(len(report["watch"]), 1)


class DerivedArithmeticSafetyTests(unittest.TestCase):
    def test_finite_inputs_with_overflowing_notional_abstain(self):
        def change(t):
            for key in ("c", "b", "a"):
                t[key][0] = "1e308"
            t["o"] = "1e308"
            t["v"][1] = "1e308"
        report = modified(ticker=change)
        self.assertFalse(observed(report))
        self.assertFalse(watched(report))

    def test_finite_inputs_with_overflowing_move_abstain(self):
        def change(t):
            for key in ("c", "b", "a"):
                t[key][0] = "1e308"
            t["o"] = "1e-308"
            t["v"][1] = "1"
        report = modified(ticker=change)
        self.assertFalse(observed(report))
        self.assertFalse(watched(report))

    def test_finite_inputs_with_overflowing_spread_abstain(self):
        def change(t):
            t["b"][0] = "1e-308"
            t["a"][0] = "1e308"
        report = modified(ticker=change)
        self.assertFalse(observed(report))
        self.assertFalse(watched(report))

    def test_overflowing_ohlc_volume_acceleration_abstains(self):
        def change(rows):
            for row in rows:
                row[6] = "1e308"
        report = modified(ohlc=change)
        self.assertTrue(observed(report))
        self.assertFalse(watched(report))
        self.assertTrue(any(a["pair"] == "C0USD" and
                            "nonfinite OHLC derived" in a["reason"]
                            for a in report["abstentions"]))

    def test_overflowing_ohlc_momentum_abstains(self):
        def change(rows):
            rows[9][3] = "1e-308"  # low
            rows[9][4] = "1e-308"  # close four bars ago
            rows[12][2] = "1e308"  # high
            rows[12][4] = "1e308"  # most recent completed close
        report = modified(ohlc=change)
        self.assertTrue(observed(report))
        self.assertFalse(watched(report))
        self.assertTrue(any(a["pair"] == "C0USD" and
                            "nonfinite OHLC derived" in a["reason"]
                            for a in report["abstentions"]))

    def test_normal_finite_ohlc_still_generates_paper_watch(self):
        report = modified()
        self.assertTrue(observed(report))
        self.assertTrue(watched(report))
        self.assertEqual(report["forward_labels"], 0)


if __name__ == "__main__":
    unittest.main()
