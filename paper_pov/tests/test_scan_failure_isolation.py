"""A1/A2 integrated fixture: one Kraken OHLC outage must not erase valid WATCH."""
import datetime as dt
import unittest
import tempfile
import json
import io
from contextlib import redirect_stdout
from unittest.mock import patch
from paper_pov import scanner
from pathlib import Path
from paper_pov.scanner import UTC, scan, persist_report

class ScanFailureIsolationTests(unittest.TestCase):
    def test_failed_market_abstains_but_valid_market_persists(self):
        now = dt.datetime(2026, 11, 3, 5, 7, tzinfo=UTC)
        start = int(now.timestamp() // 300) * 300 - 13 * 300
        candles = []
        for i in range(14):
            price = 101 + i * 0.1
            candles.append([start + i * 300, str(price), str(price + 0.2),
                            str(price - 0.2), str(price), str(price),
                            "100", "3"])
        pairs = {f"X{i:02d}USD": {"status": "online", "wsname": f"X{i:02d}/USD"}
                 for i in range(25)}
        pairs["USDTUSD"] = {"status": "online", "wsname": "USDT/USD"}
        ticker = {k: {"c": ["102"], "b": ["101.9"], "a": ["102.1"],
                      "o": "100", "v": ["1", "10000"]} for k in pairs}
        ticker["X23USD"]["a"] = ["100"]  # crossed bid/ask
        ticker["X24USD"]["c"] = ["not-a-number"]  # malformed ticker
        def api(path):
            if path == "AssetPairs":
                return pairs
            if path == "Ticker":
                return ticker
            if path.startswith("OHLC?pair=X00USD"):
                raise OSError("transient Kraken timeout")
            if path.startswith("OHLC?pair=X01USD"):
                old = [list(c) for c in candles]
                for c in old:
                    c[0] -= 3600
                return {"X01USD": old, "last": start + 13 * 300 - 3600}
            if path.startswith("OHLC?pair="):
                key = path.split("pair=", 1)[1].split("&", 1)[0]
                return {key: candles, "last": start + 13 * 300}
            raise AssertionError(path)
        report = scan(api=api, clock=lambda: now, sleep=lambda _: None, max_ohlc=4)
        self.assertEqual(report["mode"], "PAPER_ONLY")
        self.assertTrue(report["watch"])
        self.assertTrue(any(x["pair"] == "X00USD" and "timeout" in x["reason"]
                            for x in report["abstentions"]))
        self.assertTrue(all(x["status"] == "PAPER_WATCH" and not x["buy_approved"]
                            for x in report["watch"]))
        self.assertEqual(report["excluded_stablecoin_pairs"], 1)
        self.assertEqual(report["observed_markets"], 23)
        self.assertEqual(report["ticker_rejections"]["invalid_price_or_volume"], 1)
        self.assertEqual(report["ticker_rejections"]["missing_or_invalid_payload"], 1)
        self.assertEqual(report["observed_markets"] + sum(report["ticker_rejections"].values()), report["eligible_pairs"])
        self.assertEqual(report["abstention_counts"]["request_failure"], 1)
        self.assertEqual(report["abstention_counts"]["stale_or_future_ohlc"], 1)
        self.assertEqual(sum(report["abstention_counts"].values()), len(report["abstentions"]))
        self.assertEqual({x["category"] for x in report["abstentions"]},
                         {"request_failure", "stale_or_future_ohlc"})
        self.assertTrue(any(x["pair"] == "X01USD" and "stale" in x["reason"] for x in report["abstentions"]))
        self.assertTrue(all(x["pair"] != "USDTUSD" for x in report["watch"]))
        with tempfile.TemporaryDirectory() as root:
            latest = Path(root) / "latest.json"
            receipt = persist_report(latest, report)
            restored = json.loads(receipt.read_text())
            self.assertEqual(restored, json.loads(latest.read_text()))
            self.assertEqual(restored["watch"], report["watch"])
            self.assertEqual(restored["abstentions"], report["abstentions"])
            self.assertEqual(len(restored["watch"]), 2)
            self.assertEqual(len(restored["abstentions"]), 2)
            self.assertEqual(restored["forward_labels"], 0)
            self.assertFalse(restored["production_applied"])

    def test_no_liquid_candidates_persist_distinct_coverage_abstention(self):
        now = dt.datetime(2026, 11, 3, 5, 7, tzinfo=UTC)
        pairs = {f"X{i:02d}USD": {"status": "online", "wsname": f"X{i:02d}/USD"}
                 for i in range(20)}
        ticker = {k: {"c": ["100"], "b": ["99.9"], "a": ["100.1"],
                      "o": "100", "v": ["1", "10000"]} for k in pairs}
        calls = []
        def api(path):
            calls.append(path)
            if path == "AssetPairs":
                return pairs
            if path == "Ticker":
                return ticker
            raise AssertionError("OHLC should not be requested without candidates")
        report = scan(api=api, clock=lambda: now, sleep=lambda _: None)
        self.assertEqual(calls, ["AssetPairs", "Ticker"])
        self.assertEqual(report["scan_status"], "ABSTAIN_NO_LIQUID_CANDIDATES")
        self.assertEqual(report["observed_markets"], 20)
        self.assertEqual(report["ohlc_screened"], 0)
        self.assertEqual(report["screened_markets"], 0)
        self.assertEqual(report["screening_rejections"]["below_early_move"], 20)
        self.assertEqual(report["screening_rejections"]["wide_spread"], 0)
        self.assertEqual(report["screening_rejections"]["low_notional"], 0)
        self.assertEqual(report["watch"], [])
        self.assertEqual(report["abstentions"], [])
        self.assertFalse(report["buy_approved"])
        with tempfile.TemporaryDirectory() as root:
            latest = Path(root) / "latest.json"
            receipt = persist_report(latest, report)
            self.assertEqual(json.loads(receipt.read_text()), json.loads(latest.read_text()))

    def test_all_ohlc_failures_persist_truthful_zero_watch(self):
        now = dt.datetime(2026, 11, 3, 5, 7, tzinfo=UTC)
        pairs = {f"X{i:02d}USD": {"status": "online", "wsname": f"X{i:02d}/USD"}
                 for i in range(20)}
        ticker = {k: {"c": ["102"], "b": ["101.9"], "a": ["102.1"],
                      "o": "100", "v": ["1", "10000"]} for k in pairs}
        def api(path):
            if path == "AssetPairs":
                return pairs
            if path == "Ticker":
                return ticker
            if path.startswith("OHLC?pair="):
                raise OSError("Kraken OHLC unavailable")
            raise AssertionError(path)
        report = scan(api=api, clock=lambda: now, sleep=lambda _: None, max_ohlc=4)
        self.assertEqual(report["scan_status"], "ABSTAIN_NO_QUALIFIED_OHLC")
        self.assertEqual(report["watch"], [])
        self.assertEqual(report["ohlc_screened"], 4)
        self.assertEqual(report["screened_markets"], 20)
        self.assertEqual(sum(report["screening_rejections"].values()), 0)
        self.assertEqual(report["abstention_counts"]["request_failure"], 4)
        self.assertEqual(len(report["abstentions"]), 4)
        self.assertFalse(report["buy_approved"])
        with tempfile.TemporaryDirectory() as root:
            latest = Path(root) / "latest.json"
            receipt = persist_report(latest, report)
            self.assertEqual(json.loads(receipt.read_text()), json.loads(latest.read_text()))
            self.assertEqual(json.loads(latest.read_text())["scan_status"],
                             "ABSTAIN_NO_QUALIFIED_OHLC")


    def test_cli_persists_and_prints_complete_ranked_watch_evidence(self):
        now = dt.datetime(2026, 11, 3, 5, 7, tzinfo=UTC)
        # Use the same contract as the real CLI, without network or a second writer.
        watch = {
            "symbol": "X00/USD", "rank": 1, "prediction_id": "fixture-prediction",
            "baseline_score": 45.5, "challenger_score": 52.5, "price": 102.0,
            "quote_observed_at": now.isoformat(),
            "quote_timestamp_semantics": "client_observed_not_exchange_event_time",
            "ohlc_last_closed_at": now.isoformat(), "move15_pct": 1.2,
            "volume_accel": 1.8, "spread_bps": 4.0, "notional_24h_usd": 250000,
            "status": "PAPER_WATCH", "risk": "ELEVATED", "buy_approved": False
        }
        report = {
            "as_of": now.isoformat(), "scan_status": "WATCH", "mode": "PAPER_ONLY",
            "online_usd_pairs": 21, "excluded_stablecoin_pairs": 1,
            "excluded_other_pairs": 0, "eligible_pairs": 20, "matched_tickers": 20,
            "observed_markets": 20, "ticker_rejections": {
                "missing_or_invalid_payload": 0, "invalid_price_or_volume": 0,
                "nonfinite_derived_metric": 0},
            "ohlc_screened": 1, "abstention_counts": {}, "forward_labels": 0,
            "production_applied": False, "watch": [watch]
        }
        with tempfile.TemporaryDirectory() as root:
            latest = Path(root) / "latest.json"
            output = io.StringIO()
            with patch.object(scanner, "scan", return_value=report), patch.dict(
                    "os.environ", {"PAPER_REPORT_PATH": str(latest)}), redirect_stdout(output):
                scanner.main()
            lines = output.getvalue().splitlines()
            printed_status = json.loads(next(x[len("PAPER_SCAN "):] for x in lines
                                             if x.startswith("PAPER_SCAN ")))
            printed_watch = json.loads(next(x[len("PAPER_WATCH "):] for x in lines
                                            if x.startswith("PAPER_WATCH ")))
            self.assertEqual(printed_status["scan_status"], "WATCH")
            self.assertEqual(printed_watch, [watch])
            self.assertEqual(json.loads(latest.read_text()), report)
            self.assertEqual(len(list((latest.parent / "receipts").glob("*.json"))), 1)

if __name__ == "__main__":
    unittest.main()
