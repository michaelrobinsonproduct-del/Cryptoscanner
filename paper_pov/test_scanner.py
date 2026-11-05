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
        self.assertEqual(a["online_usd_pairs"], 25)
        self.assertEqual(a["excluded_stablecoin_pairs"], 0)
        self.assertEqual(a["excluded_other_pairs"], 0)
        self.assertEqual(len(a["watch"]), 12)
        self.assertEqual(len({x["prediction_id"] for x in a["watch"]}), 12)
        self.assertTrue(all(x["ohlc_age_seconds"] <= 600 for x in a["watch"]))
        self.assertTrue(all(x["quote_observed_at"] <= x["as_of"] for x in a["watch"]))

    def test_gap_fails_closed(self):
        report = run(gap=True)
        self.assertEqual(report["watch"], [])
        self.assertEqual(report["scan_status"], "ABSTAIN_NO_QUALIFIED_OHLC")
        self.assertEqual(report["abstention_counts"]["ohlc_gap_or_schema"], 24)

    def test_zero_volume_no_trade_abstains(self):
        report = run(zero_volume=True)
        self.assertEqual(report["watch"], [])
        self.assertEqual(report["scan_status"], "ABSTAIN_NO_QUALIFIED_OHLC")
        self.assertEqual(report["abstention_counts"]["ohlc_gap_or_schema"], 24)

    def test_stale_candle_fails_closed(self):
        report = run(stale=True)
        self.assertEqual(report["watch"], [])
        self.assertEqual(report["scan_status"], "ABSTAIN_NO_QUALIFIED_OHLC")
        self.assertEqual(report["abstention_counts"]["stale_or_future_ohlc"], 24)

    def test_partial_ticker_payload_abstains_without_discarding_observations(self):
        base = fixture()
        def api(path):
            result = base(path)
            if path == "Ticker":
                result = dict(result)
                result.pop("C0USD")
            return result
        report = scanner.scan(api=api, clock=lambda: NOW, sleep=lambda _: None)
        self.assertEqual(report["scan_status"], "ABSTAIN_INCOMPLETE_TICKER_COVERAGE")
        self.assertFalse(report["ticker_coverage_complete"])
        self.assertEqual(report["ticker_rejections"]["missing_or_invalid_payload"], 1)
        self.assertEqual(report["observed_markets"], 24)
        self.assertEqual(report["watch"], [])
        self.assertEqual(report["ohlc_screened"], 0)
        self.assertEqual(report["preselection_decisions"]["NOT_OHLC_SELECTED"],
                         report["screened_markets"])

    def test_invalid_ticker_price_fails_closed_without_losing_valid_inventory(self):
        base = fixture()
        def api(path):
            result = base(path)
            if path == "Ticker":
                result = {key: dict(value) for key, value in result.items()}
                result["C0USD"]["c"] = ["0"]
            return result
        report = scanner.scan(api=api, clock=lambda: NOW, sleep=lambda _: None)
        self.assertEqual(report["scan_status"], "ABSTAIN_INCOMPLETE_TICKER_COVERAGE")
        self.assertFalse(report["ticker_coverage_complete"])
        self.assertEqual(report["ticker_rejections"]["invalid_price_or_volume"], 1)
        self.assertEqual(report["observed_markets"], 24)
        self.assertEqual(report["watch"], [])
        self.assertEqual(report["ohlc_screened"], 0)

    def test_nonfinite_derived_ticker_metric_fails_closed(self):
        base = fixture()
        def api(path):
            result = base(path)
            if path == "Ticker":
                result = {key: dict(value) for key, value in result.items()}
                result["C0USD"]["v"] = ["1", "1e308"]
                result["C0USD"]["c"] = ["1e308"]
                result["C0USD"]["a"] = ["1e308"]
                result["C0USD"]["b"] = ["1e308"]
            return result
        report = scanner.scan(api=api, clock=lambda: NOW, sleep=lambda _: None)
        self.assertEqual(report["scan_status"], "ABSTAIN_INCOMPLETE_TICKER_COVERAGE")
        self.assertEqual(report["ticker_rejections"]["nonfinite_derived_metric"], 1)
        self.assertEqual(report["watch"], [])

    def test_ohlc_assetpairs_declared_altname_is_accepted(self):
        base = fixture()
        def api(path):
            result = base(path)
            if path == "AssetPairs":
                return {key: dict(meta, altname="ALT" + key) for key, meta in result.items()}
            if path.startswith("OHLC?"):
                key = path.split("pair=")[1].split("&")[0]
                return {"ALT" + key: result[key], "last": result["last"]}
            return result
        report = scanner.scan(api=api, clock=lambda: NOW, sleep=lambda _: None)
        self.assertEqual(report["scan_status"], "WATCH")
        self.assertEqual(len(report["watch"]), 12)
        self.assertEqual(report["ohlc_screened"], 24)

    def test_ohlc_duplicate_altname_cannot_cross_pair_boundary(self):
        base = fixture()
        def api(path):
            result = base(path)
            if path == "AssetPairs":
                return {key: dict(meta, altname="SHAREDUSD") for key, meta in result.items()}
            if path.startswith("OHLC?"):
                key = path.split("pair=")[1].split("&")[0]
                return {"SHAREDUSD": result[key], "last": result["last"]}
            return result
        report = scanner.scan(api=api, clock=lambda: NOW, sleep=lambda _: None)
        self.assertEqual(report["watch"], [])
        self.assertEqual(report["scan_status"], "ABSTAIN_NO_QUALIFIED_OHLC")
        self.assertEqual(report["abstention_counts"]["ohlc_gap_or_schema"], 24)

    def test_ohlc_altname_colliding_with_another_pair_key_abstains(self):
        base = fixture()
        def api(path):
            result = base(path)
            if path == "AssetPairs":
                return {key: dict(meta, altname=("C1USD" if key == "C0USD"
                                               else "ALT" + key))
                        for key, meta in result.items()}
            if path.startswith("OHLC?"):
                key = path.split("pair=")[1].split("&")[0]
                returned = "C1USD" if key == "C0USD" else "ALT" + key
                return {returned: result[key], "last": result["last"]}
            return result
        report = scanner.scan(api=api, clock=lambda: NOW, sleep=lambda _: None)
        self.assertNotIn("C0USD", {item["pair"] for item in report["watch"]})
        self.assertEqual(report["abstention_counts"]["ohlc_gap_or_schema"], 1)
        self.assertEqual(report["ohlc_screened"], 24)

    def test_ohlc_unrelated_alias_abstains_without_wrong_market_data(self):
        base = fixture()
        def api(path):
            result = base(path)
            if path.startswith("OHLC?"):
                key = path.split("pair=")[1].split("&")[0]
                return {"UNRELATED" + key: result[key], "last": result["last"]}
            return result
        report = scanner.scan(api=api, clock=lambda: NOW, sleep=lambda _: None)
        self.assertEqual(report["scan_status"], "ABSTAIN_NO_QUALIFIED_OHLC")
        self.assertEqual(report["watch"], [])
        self.assertEqual(report["abstention_counts"]["ohlc_gap_or_schema"], 24)

    def test_insufficient_universe_coverage_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError, "coverage"):
            run(coverage=True)

    def test_stablecoin_is_excluded(self):
        result = run(stable=True)
        self.assertEqual(result["eligible_pairs"], 25)
        self.assertEqual(result["online_usd_pairs"], 38)
        self.assertEqual(result["excluded_stablecoin_pairs"], 13)
        self.assertEqual(result["excluded_other_pairs"], 0)
        self.assertEqual(result["online_usd_pairs"], result["eligible_pairs"] +
                         result["excluded_stablecoin_pairs"] + result["excluded_other_pairs"])
        observed = {x["pair"] for x in result["observations"]}
        watched = {x["pair"] for x in result["watch"]}
        for base in ("USDT", "BRL1", "QCAD", "USDG", "USDQ", "USDS",
                     "USDR", "USD1", "EURQ", "EURR", "EUROP", "EURT", "TGBP"):
            with self.subTest(stablecoin=base):
                self.assertNotIn(base + "USD", observed)
                self.assertNotIn(base + "USD", watched)

    def test_suffix_exclusions_are_counted_separately_from_stablecoins(self):
        def api(path):
            data = fixture()(path)
            if path == "AssetPairs":
                data["STAKEDUSD"] = {"status": "online", "wsname": "XBT.S/USD"}
                data["MARGINUSD"] = {"status": "online", "wsname": "XBT.M/USD"}
                data["OFFLINEUSD"] = {"status": "cancel_only", "wsname": "USDT/USD"}
            return data
        report = scanner.scan(api=api, clock=lambda: NOW, sleep=lambda _: None)
        self.assertEqual(report["eligible_pairs"], 25)
        self.assertEqual(report["online_usd_pairs"], 27)
        self.assertEqual(report["excluded_stablecoin_pairs"], 0)
        self.assertEqual(report["excluded_other_pairs"], 2)

    def test_duplicate_kraken_display_market_is_not_sealed_twice(self):
        def api(path):
            result = fixture()(path)
            if path == "AssetPairs":
                result["ZZ_DUPLICATE"] = {"status": "online", "wsname": "C0/USD"}
            if path == "Ticker":
                result["ZZ_DUPLICATE"] = result["C0USD"]
            return result
        report = scanner.scan(api=api, clock=lambda: NOW, sleep=lambda _: None)
        self.assertEqual(report["online_usd_pairs"], 26)
        self.assertEqual(report["excluded_other_pairs"], 1)
        self.assertEqual(report["eligible_pairs"], 25)
        self.assertEqual(len({c["symbol"] for c in report["watch"]}), len(report["watch"]))
        self.assertNotIn("ZZ_DUPLICATE", {c["pair"] for c in report["watch"]})

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

    def test_ohlc_expiring_during_screening_abstains_before_sealing(self):
        # The candle closes at 14:55; it is 9m old during OHLC
        # requests, but 11m old when the final scan receipt is sealed.
        calls = 0
        def clock():
            nonlocal calls
            calls += 1
            return NOW + dt.timedelta(minutes=6 if calls > 26 else 4)
        report = scanner.scan(api=fixture(), clock=clock, sleep=lambda _: None)
        self.assertEqual(report["watch"], [])
        self.assertEqual(report["scan_status"], "ABSTAIN_NO_QUALIFIED_OHLC")
        self.assertEqual(report["abstention_counts"]["stale_or_future_ohlc"], 24)
        self.assertEqual(report["preselection_decisions"]["OHLC_ABSTAINED"], 24)
        self.assertEqual(report["preselection_decisions"]["NOT_OHLC_SELECTED"], 1)

    def test_tiny_positive_acceleration_abstains_before_snapshot_seal(self):
        # Raw OHLC volume acceleration is positive, but the persisted four
        # decimal representation would be zero and fail A2 readback.
        def api(path):
            result = fixture()(path)
            if path.startswith("OHLC?"):
                pair = next(k for k in result if k != "last")
                for row in result[pair][-7:-1]:
                    row[6] = "0.000001"
            return result
        report = scanner.scan(api=api, clock=lambda: NOW, sleep=lambda _: None)
        self.assertEqual(report["watch"], [])
        self.assertEqual(report["scan_status"], "ABSTAIN_NO_QUALIFIED_OHLC")
        self.assertEqual(report["abstention_counts"]["invalid_market_metrics"], 24)
        self.assertEqual(report["preselection_decisions"]["OHLC_ABSTAINED"], 24)

    def test_future_ohlc_rejected(self):
        def future_api(path):
            result = fixture()(path)
            if path.startswith("OHLC?"):
                key = next(k for k in result if k != "last")
                for row in result[key]:
                    row[0] += 900
            return result
        report = scanner.scan(api=future_api, clock=lambda: NOW, sleep=lambda _: None)
        self.assertEqual(report["watch"], [])
        self.assertEqual(report["abstention_counts"]["stale_or_future_ohlc"], 24)

if __name__ == "__main__":
    unittest.main()
