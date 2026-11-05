"""A1→A2 complete fixture-backed scan, durable receipt and read-only consumption."""
import datetime as dt
import hashlib
import tempfile
import unittest
from pathlib import Path

from paper_pov.scanner import UTC, scan, persist_report
from paper_pov.candidate_snapshot import read_snapshot
from paper_pov.preselection_universe import export_universe, export_receipt_history


class EndToEndCandidateTests(unittest.TestCase):
    def setUp(self):
        self.now = dt.datetime(2026, 11, 3, 5, 7, tzinfo=UTC)
        self.pairs = {f"X{i:02d}USD": {"status": "online", "wsname": f"X{i:02d}/USD"} for i in range(25)}
        self.pairs["USDTUSD"] = {"status": "online", "wsname": "USDT/USD"}
        self.ticker = {k: {"c": ["102"], "b": ["101.9"], "a": ["102.1"],
                           "o": "100", "v": ["1", "10000"]} for k in self.pairs}
        start = int(self.now.timestamp() // 300) * 300 - 13 * 300
        self.candles = [[start + i * 300, "101", "103", "100", "102",
                         "102", "100", "3"] for i in range(14)]

    def api(self, path):
        if path == "AssetPairs":
            return self.pairs
        if path == "Ticker":
            return self.ticker
        if path.startswith("OHLC?pair="):
            pair = path.split("pair=", 1)[1].split("&", 1)[0]
            if pair == "X00USD":
                raise OSError("Kraken timeout")
            return {pair: self.candles, "last": self.candles[-1][0]}
        raise AssertionError(path)

    def round_trip(self, report):
        with tempfile.TemporaryDirectory() as folder:
            latest = Path(folder) / "latest.json"
            receipt = persist_report(latest, report)
            result = read_snapshot(latest, now=self.now + dt.timedelta(seconds=30))
            self.assertEqual(result["receipt_sha256"], __import__("hashlib").sha256(receipt.read_bytes()).hexdigest())
            self.assertEqual(result["watch"], report["watch"])
            self.assertEqual(result["observed_markets"], report["observed_markets"])
            self.assertEqual(result["abstention_counts"], report["abstention_counts"])
            universe = export_universe(latest, now=self.now + dt.timedelta(seconds=30))
            self.assertEqual(universe["receipt_sha256"], result["receipt_sha256"])
            self.assertEqual(len(universe["markets"]), report["observed_markets"])
            self.assertFalse(universe["qualified_for_learning"])
            self.assertEqual(len({x["observation_id"] for x in universe["markets"]}), report["observed_markets"])
            for x in universe["markets"]:
                expected = hashlib.sha256(("paper-preselection-v1|" +
                    universe["receipt_sha256"] + "|" + x["pair"]).encode()).hexdigest()
                self.assertEqual(x["observation_id"], expected)
            ranked = {x["pair"]: x["rank"] for x in result["watch"]}
            self.assertEqual({x["pair"]: x["watch_rank"] for x in universe["markets"]
                              if x["selection_status"] == "WATCH"}, ranked)
            self.assertEqual(sum(universe["selection_decisions"].values()), report["observed_markets"])
            self.assertEqual(universe["selection_decisions"]["WATCH"], len(report["watch"]))
            self.assertEqual(universe["selection_decisions"]["OHLC_ABSTAINED"], len(report["abstentions"]))
            self.assertEqual(universe["selection_decisions"]["SCREEN_REJECTED"], report["preselection_coverage"]["screen_rejected"])
            self.assertEqual(universe["selection_decisions"]["NOT_OHLC_SELECTED"] +
                             universe["selection_decisions"].get("SOURCE_COVERAGE_ABSTAINED", 0) +
                             universe["selection_decisions"].get("NOT_RANKED_WATCH", 0) +
                             universe["selection_decisions"]["WATCH"] +
                             universe["selection_decisions"]["OHLC_ABSTAINED"],
                             report["preselection_coverage"]["screen_passed"])
            self.assertTrue(all((x["baseline_score"] is not None) == x["screen_passed"] for x in universe["markets"]))
            self.assertEqual(persist_report(latest, report), receipt)
            return result

    def test_sparse_ticker_universe_preserves_source_abstention_through_receipt(self):
        # A quote-complete candidate selection is impossible with a partial
        # Kraken Ticker response, even if the surviving markets look liquid.
        self.ticker = {key: value for key, value in self.ticker.items()
                       if key in {f"X{i:02d}USD" for i in range(12)}}
        report = scan(api=self.api, clock=lambda: self.now, sleep=lambda _: None)
        self.assertEqual(report["scan_status"], "ABSTAIN_INCOMPLETE_TICKER_COVERAGE")
        self.assertEqual(report["watch"], [])
        self.assertEqual(report["preselection_decisions"]["SOURCE_COVERAGE_ABSTAINED"], 12)
        self.assertEqual(report["preselection_decisions"]["NOT_OHLC_SELECTED"], 0)
        result = self.round_trip(report)
        self.assertEqual(result["observed_markets"], 12)

    def test_live_shape_watch_stablecoin_timeout_and_durable_readback(self):
        report = scan(api=self.api, clock=lambda: self.now, sleep=lambda _: None, max_ohlc=4)
        result = self.round_trip(report)
        self.assertEqual(report["excluded_stablecoin_pairs"], 1)
        self.assertEqual(report["preselection_coverage"], {"valid_tickers": 25, "screen_passed": 25, "screen_rejected": 0})
        self.assertEqual(report["abstention_counts"]["request_failure"], 1)
        self.assertEqual(len(result["watch"]), 3)
        self.assertTrue(all(x["status"] == "PAPER_WATCH" and x["buy_approved"] is False for x in result["watch"]))
        self.assertEqual(set(result["quote_age_seconds"]), {x["pair"] for x in result["watch"]})
        self.assertTrue(all(x["pair"] != "USDTUSD" for x in result["watch"]))

    def test_zero_watch_is_readable_abstention_not_buy(self):
        for ticker in self.ticker.values():
            ticker["o"] = ticker["c"][0]
        report = scan(api=self.api, clock=lambda: self.now, sleep=lambda _: None)
        result = self.round_trip(report)
        self.assertEqual(result["scan_status"], "ABSTAIN_NO_LIQUID_CANDIDATES")
        self.assertEqual(result["watch"], [])
        self.assertEqual(result["quote_age_seconds"], {})
        self.assertEqual(report["preselection_coverage"], {"valid_tickers": 25, "screen_passed": 0, "screen_rejected": 25})
        self.assertTrue(all(x["screen_rejections"] == ["below_early_move"] for x in report["preselection_universe"]))

    def test_nonwatch_ticker_provenance_cannot_poison_historical_learning(self):
        # An unranked ticker is still an E historical observation; a forged
        # source timestamp must not survive a freshly resealed receipt.
        report = scan(api=self.api, clock=lambda: self.now, sleep=lambda _: None, max_ohlc=4)
        nonwatch = next(row for row in report["observations"]
                        if row["pair"] not in {w["pair"] for w in report["watch"]})
        from copy import deepcopy
        for field, bad in (("observed_at", (self.now + dt.timedelta(minutes=1)).isoformat()),
                           ("observed_at", (self.now - dt.timedelta(minutes=11)).isoformat()),
                           ("source", "unverified_exchange_timestamp"),
                           ("price", float("nan"))):
            with self.subTest(field=field, bad=str(bad)):
                forged = deepcopy(report)
                next(row for row in forged["observations"] if row["pair"] == nonwatch["pair"])[field] = bad
                with tempfile.TemporaryDirectory() as folder:
                    latest = Path(folder) / "latest.json"
                    if field == "price":
                        # Nonfinite JSON is rejected at immutable receipt serialization.
                        with self.assertRaisesRegex(ValueError, "Out of range float"):
                            persist_report(latest, forged)
                    else:
                        persist_report(latest, forged)
                        with self.assertRaisesRegex(ValueError, "source observation"):
                            read_snapshot(latest, now=self.now)

    def test_preselection_export_rejects_relabelled_screen_failure(self):
        # A sealed zero-WATCH receipt can still carry internally contradictory
        # research decisions; reject false historical miss labels at export.
        for ticker in self.ticker.values():
            ticker["o"] = ticker["c"][0]
        report = scan(api=self.api, clock=lambda: self.now, sleep=lambda _: None)
        row = report["preselection_universe"][0]
        self.assertFalse(row["screen_passed"])
        row["selection_status"] = "NOT_OHLC_SELECTED"
        report["preselection_decisions"]["SCREEN_REJECTED"] -= 1
        report["preselection_decisions"]["NOT_OHLC_SELECTED"] += 1
        with tempfile.TemporaryDirectory() as folder:
            latest = Path(folder) / "latest.json"
            persist_report(latest, report)
            # A2 validates WATCH evidence; the preselection exporter owns
            # the stricter historical selection semantics.
            self.assertEqual(read_snapshot(latest, now=self.now)["watch"], [])
            with self.assertRaisesRegex(ValueError, "screen and selection decision mismatch"):
                export_universe(latest, now=self.now)

    def test_historical_universe_research_survives_live_expiry_without_live_watch(self):
        report = scan(api=self.api, clock=lambda: self.now, sleep=lambda _: None, max_ohlc=4)
        with tempfile.TemporaryDirectory() as folder:
            latest = Path(folder) / "latest.json"
            receipt = persist_report(latest, report)
            old = self.now + dt.timedelta(days=14)
            with self.assertRaisesRegex(ValueError, "stale or future paper snapshot"):
                export_universe(latest, now=old)
            research = export_universe(latest, now=old, historical=True)
            self.assertEqual(research["snapshot_use"], "HISTORICAL_RESEARCH_ONLY")
            self.assertFalse(research["live_watch_eligible"])
            self.assertFalse(research["qualified_for_learning"])
            self.assertEqual(research["receipt_sha256"], hashlib.sha256(receipt.read_bytes()).hexdigest())
            self.assertEqual(len(research["markets"]), 25)
            self.assertEqual(research["selection_decisions"]["WATCH"], 3)
            # Research mode still requires the original immutable receipt.
            receipt.unlink()
            with self.assertRaisesRegex(ValueError, "immutable receipt"):
                export_universe(latest, historical=True)

    def test_historical_zero_watch_remains_research_only(self):
        for ticker in self.ticker.values():
            ticker["o"] = ticker["c"][0]
        report = scan(api=self.api, clock=lambda: self.now, sleep=lambda _: None)
        with tempfile.TemporaryDirectory() as folder:
            latest = Path(folder) / "latest.json"
            persist_report(latest, report)
            research = export_universe(latest, historical=True)
            self.assertEqual(research["selection_decisions"]["WATCH"], 0)
            self.assertEqual(research["selection_decisions"]["SCREEN_REJECTED"], 25)
            self.assertFalse(research["live_watch_eligible"])

    def test_receipt_history_exports_longitudinal_complete_universe(self):
        with tempfile.TemporaryDirectory() as folder:
            latest = Path(folder) / "latest.json"
            first = scan(api=self.api, clock=lambda: self.now, sleep=lambda _: None, max_ohlc=4)
            persist_report(latest, first)
            later = self.now + dt.timedelta(minutes=5)
            second = scan(api=self.api, clock=lambda: later, sleep=lambda _: None, max_ohlc=4)
            persist_report(latest, second)
            feed = export_receipt_history(latest.parent / "receipts")
            self.assertEqual(feed["receipt_count"], 2)
            self.assertEqual(feed["market_observation_count"], 50)
            self.assertFalse(feed["live_watch_eligible"])
            self.assertFalse(feed["future_outcomes_authenticated"])
            self.assertEqual(len({r["observation_id"] for snap in feed["snapshots"]
                                  for r in snap["markets"]}), 50)
            self.assertEqual([s["as_of"] for s in feed["snapshots"]],
                             sorted(s["as_of"] for s in feed["snapshots"]))

    def test_reader_rejects_aged_quote_without_rewriting_receipt(self):
        report = scan(api=self.api, clock=lambda: self.now, sleep=lambda _: None, max_ohlc=4)
        with tempfile.TemporaryDirectory() as folder:
            latest = Path(folder) / "latest.json"
            receipt = persist_report(latest, report)
            original = receipt.read_bytes()
            with self.assertRaisesRegex(ValueError, "stale or future paper snapshot"):
                read_snapshot(latest, now=self.now + dt.timedelta(minutes=11))
            self.assertEqual(receipt.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
