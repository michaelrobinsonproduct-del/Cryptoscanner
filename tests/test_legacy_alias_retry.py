"""Focused independent Kraken OHLC alias-acquisition regression."""
import datetime as dt
import unittest

from paper_pov.legacy_shadow import scan

UTC = dt.timezone.utc
NOW = dt.datetime(2026, 11, 7, 15, 0, tzinfo=UTC)


class AliasRetryTests(unittest.TestCase):
    def test_unique_advertised_altname_recovers_rejected_rest_pair(self):
        pairs = {
            f"REST{i}": {"status": "online", "wsname": f"COIN{i}/USD",
                        "altname": f"ALT{i}"} for i in range(20)
        }
        ticker = {
            f"REST{i}": {"c": ["2"], "b": ["1.99"], "a": ["2.01"],
                         "o": ["1.95"], "v": ["100000", "100000"],
                         "t": ["1000", "1000"]} for i in range(20)
        }
        # 13 completed 5-minute buckets and one uncommitted tail.
        end = int(NOW.timestamp())
        candles = [[end - (13 - i) * 300, "2", "2.1", "1.9",
                    str(1.95 + i * .005), "2", "100", 10]
                   for i in range(13)]
        candles.append([end, "2", "2.1", "1.9", "2", "2", "0", 0])
        requested = []

        def api(path):
            if path == "AssetPairs":
                return pairs
            if path == "Ticker":
                return ticker
            requested.append(path)
            if "REST" in path:
                raise ValueError("Kraken response error or invalid schema")
            return {"ALT0": candles, "last": end}

        result = scan(api=api, clock=lambda: NOW, sleep=lambda _: None,
                      max_ohlc=1, run_id="101", source_sha="a" * 40,
                      trigger_paper_run_id="100")
        self.assertEqual(result["ohlc_evaluated"], 1)
        self.assertEqual(len(result["candidates"]), 1)
        self.assertEqual(result["status"], "WATCH_PAPER_ONLY")
        self.assertTrue(any("REST0" in p for p in requested))
        self.assertTrue(any("ALT0" in p for p in requested))


if __name__ == "__main__":
    unittest.main()
