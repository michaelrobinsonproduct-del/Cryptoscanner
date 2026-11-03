"""A1/A2 integrated fixture: one Kraken OHLC outage must not erase valid WATCH."""
import datetime as dt
import unittest
import tempfile
import json
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
                 for i in range(20)}
        pairs["USDTUSD"] = {"status": "online", "wsname": "USDT/USD"}
        ticker = {k: {"c": ["102"], "b": ["101.9"], "a": ["102.1"],
                      "o": "100", "v": ["1", "10000"]} for k in pairs}
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
        self.assertEqual(report["abstention_counts"]["request_failure"], 4)
        self.assertEqual(len(report["abstentions"]), 4)
        self.assertFalse(report["buy_approved"])
        with tempfile.TemporaryDirectory() as root:
            latest = Path(root) / "latest.json"
            receipt = persist_report(latest, report)
            self.assertEqual(json.loads(receipt.read_text()), json.loads(latest.read_text()))
            self.assertEqual(json.loads(latest.read_text())["scan_status"],
                             "ABSTAIN_NO_QUALIFIED_OHLC")

if __name__ == "__main__":
    unittest.main()
