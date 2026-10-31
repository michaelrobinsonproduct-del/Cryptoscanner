"""Offline, deterministic, fail-closed paper scanner tests; never place orders."""
import datetime as dt
import json
from pathlib import Path
import tempfile
import unittest
from paper_pov import scanner

NOW = dt.datetime(2026, 10, 31, 15, 0, tzinfo=dt.timezone.utc)

def fixture(*, gap=False, zero_volume=False, stale=False, coverage=False, stable=False):
    pairs = {f"C{i}USD": {"status": "online", "wsname": f"C{i}/USD"} for i in range(25)}
    if stable:
        # Explicit source-backed fixtures: NEVER derive fixtures from scanner.STABLE.
        # Kraken also lists fiat-pegged BRL1, QCAD, USDG, EURQ, etc.
        for base in ("USDT", "BRL1", "QCAD", "USDG", "USDQ", "USDS",
                     "USDR", "USD1", "EURQ", "EURR", "EUROP", "EURT", "TGBP"):
            pairs[base + "USD"] = {"status": "online", "wsname": base + "/USD"}
    tickers = {key: {"c": ["1.01"], "b": ["1.009"], "a": ["1.011"],
                      "o": "1", "v": ["200000", "200000"]} for key in pairs}
    if coverage:
        tickers = dict(list(tickers.items())[:12])
    def api(path):
        if path == "AssetPairs":
            return pairs
        if path == "Ticker":
            return tickers
        if path.startswith("OHLC?"):
            pair = path.split("pair=")[1].split("&")[0]
            start = int(NOW.timestamp()) - (14 * 300) - (3600 if stale else 0)
            bars = [[start + i * 300, "1", "1.02", "1", "1.01", "1.01",
                     "0" if zero_volume else "100", "10"] for i in range(14)]
            if gap:
                bars[5][0] += 300
            return {pair: bars, "last": start + 14 * 300}
        raise AssertionError(path)
    return api

def run(**kwargs):
    return scanner.scan(api=fixture(**kwargs), clock=lambda: NOW, sleep=lambda _: None)

class PaperScanTests(unittest.TestCase):
    def test_real_as_of_contract_and_immutable_ids(self):
        a, b = run(), run()
        self.assertEqual(a, b)
        self.assertEqual(a["mode"], "PAPER_ONLY")
        self.assertIs(a["buy_approved"], False)
        self.assertIs(a["production_applied"], False)
        self.assertEqual(a["forward_labels"], 0)
        self.assertIsNone(a["held_out_lift"])
        self.assertEqual(a["observed_markets"], 25)
        self.assertEqual(len(a["watch"]), 12)
        self.assertEqual(len({x["prediction_id"] for x in a["watch"]}), 12)
        self.assertTrue(all(x["ohlc_age_seconds"] <= 600 for x in a["watch"]))
        self.assertTrue(all(x["quote_observed_at"] <= x["as_of"] for x in a["watch"]))

    def test_gap_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError, "No fresh"):
            run(gap=True)

    def test_zero_volume_no_trade_abstains(self):
        with self.assertRaisesRegex(RuntimeError, "No fresh"):
            run(zero_volume=True)

    def test_stale_candle_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError, "No fresh"):
            run(stale=True)

    def test_insufficient_universe_coverage_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError, "coverage"):
            run(coverage=True)

    def test_stablecoin_is_excluded(self):
        result = run(stable=True)
        self.assertEqual(result["eligible_pairs"], 25)
        observed = {x["pair"] for x in result["observations"]}
        watched = {x["pair"] for x in result["watch"]}
        for base in ("USDT", "BRL1", "QCAD", "USDG", "USDQ", "USDS",
                     "USDR", "USD1", "EURQ", "EURR", "EUROP", "EURT", "TGBP"):
            with self.subTest(stablecoin=base):
                self.assertNotIn(base + "USD", observed)
                self.assertNotIn(base + "USD", watched)

    def test_documented_fiat_pegs_are_explicitly_excluded(self):
        # The source-backed fixture catches omissions even if ranking changes.
        official = {"BRL1", "QCAD", "USDG", "USDQ", "USDS", "USDR",
                    "EURQ", "EURR", "EUROP", "EURT", "TGBP"}
        self.assertTrue(official.issubset(scanner.STABLE))
        self.assertIn("USD1", scanner.STABLE)

    def test_client_observed_ticker_not_exchange_time(self):
        result = run()
        self.assertIn("client-observed", result["source"])
        self.assertTrue(all(x["source"].endswith("client_observed") for x in result["observations"]))

    def test_atomic_report(self):
        result = run()
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "nested" / "report.json"
            scanner.atomic_json(path, result)
            self.assertEqual(json.loads(path.read_text()), result)
            self.assertEqual(list(path.parent.glob("*.tmp")), [])

    def test_nonfinite_quote_abstains_not_predictions(self):
        def bad_api(path):
            result = fixture()(path)
            if path == "Ticker":
                result["C0USD"]["c"] = ["nan"]
            return result
        report = scanner.scan(api=bad_api, clock=lambda: NOW, sleep=lambda _: None)
        self.assertNotIn("C0USD", {x["pair"] for x in report["watch"]})

    def test_future_ohlc_rejected(self):
        def future_api(path):
            result = fixture()(path)
            if path.startswith("OHLC?"):
                key = next(k for k in result if k != "last")
                for row in result[key]:
                    row[0] += 900
            return result
        with self.assertRaisesRegex(RuntimeError, "No fresh"):
            scanner.scan(api=future_api, clock=lambda: NOW, sleep=lambda _: None)

if __name__ == "__main__":
    unittest.main()
