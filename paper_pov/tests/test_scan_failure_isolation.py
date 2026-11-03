"""A1/A2 integrated fixture: one Kraken OHLC outage must not erase valid WATCH."""
import datetime as dt
import unittest
from paper_pov.scanner import UTC, scan

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
        ticker = {k: {"c": ["102"], "b": ["101.9"], "a": ["102.1"],
                      "o": "100", "v": ["1", "10000"]} for k in pairs}
        def api(path):
            if path == "AssetPairs":
                return pairs
            if path == "Ticker":
                return ticker
            if path.startswith("OHLC?pair=X00USD"):
                raise OSError("transient Kraken timeout")
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
        self.assertEqual(report["excluded_stablecoin_pairs"], 0)

if __name__ == "__main__":
    unittest.main()
