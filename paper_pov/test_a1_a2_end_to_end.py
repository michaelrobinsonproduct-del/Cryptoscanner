"""A1→A2 complete fixture-backed scan, durable receipt and read-only consumption."""
import datetime as dt
import tempfile
import unittest
from pathlib import Path

from paper_pov.scanner import UTC, scan, persist_report
from paper_pov.candidate_snapshot import read_snapshot


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
            self.assertEqual(persist_report(latest, report), receipt)
            return result

    def test_live_shape_watch_stablecoin_timeout_and_durable_readback(self):
        report = scan(api=self.api, clock=lambda: self.now, sleep=lambda _: None, max_ohlc=4)
        result = self.round_trip(report)
        self.assertEqual(report["excluded_stablecoin_pairs"], 1)
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
