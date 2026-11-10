"""Actual candle continuity, never synthetic forward-label coverage."""
import copy
import unittest

from paper_pov.rolling_kraken_candles import merge_observed_history


def item(pair, start, end):
    from datetime import datetime, timedelta, timezone
    origin = datetime(2026, 11, 1, tzinfo=timezone.utc)
    return {
        "pair": pair, "kraken_pair_key": pair, "source": "kraken_public_ohlc_rest",
        "response_sha256": "a" * 64,
        "candles": [
            {"pair": pair, "timestamp_utc": (origin + timedelta(minutes=i * 5)).isoformat(),
             "close": 2.0, "high": 2.1, "volume": 3.0}
            for i in range(start, end)
        ]
    }


def source(*items):
    return {"schema": "kraken_ohlc_observations_v1", "results": list(items),
            "source_authenticated": False}


class RollingKrakenCandlesTests(unittest.TestCase):
    def test_actual_overlap_joins_and_keeps_older_matured_candles(self):
        old = source(item("AAAUSD", 0, 5))
        fresh = source(item("AAAUSD", 3, 7), item("BBBUSD", 5, 7))
        combined = merge_observed_history(old, fresh)
        self.assertEqual(combined["retained_candles"], 9)
        self.assertEqual(combined["retained_pairs"], 2)
        self.assertEqual([r["timestamp_utc"] for r in combined["results"][0]["candles"]],
                         [r["timestamp_utc"] for r in item("AAAUSD", 0, 7)["candles"]])
        self.assertFalse(combined["source_authenticated"])
        self.assertFalse(combined["results"][0]["source_authenticated"])

    def test_no_backfill_or_gap_interpolation(self):
        result = merge_observed_history(source(item("AAAUSD", 0, 2)),
                                         source(item("AAAUSD", 7, 9)))
        self.assertEqual([r["timestamp_utc"] for r in result["results"][0]["candles"]],
                         [r["timestamp_utc"] for r in item("AAAUSD", 0, 2)["candles"] +
                          item("AAAUSD", 7, 9)["candles"]])

    def test_changed_historical_bar_fails_closed(self):
        old = source(item("AAAUSD", 0, 4))
        fresh = source(item("AAAUSD", 3, 7))
        fresh["results"][0]["candles"][0]["close"] = 1.99
        with self.assertRaisesRegex(ValueError, "overlap rewritten"):
            merge_observed_history(old, fresh)

    def test_no_previous_first_run(self):
        result = merge_observed_history(None, source(item("AAAUSD", 0, 4)))
        self.assertEqual(result["retained_candles"], 4)

    def test_reject_future_claims_and_malformed_sources(self):
        old = source(item("AAAUSD", 0, 4))
        old["results"][0]["candles"][0]["pair"] = "OTHER"
        with self.assertRaisesRegex(ValueError, "Cross-pair"):
            merge_observed_history(old, source(item("AAAUSD", 3, 7)))
        with self.assertRaisesRegex(ValueError, "Invalid retained"):
            merge_observed_history({"results": []}, source(item("AAAUSD", 3, 7)))


if __name__ == "__main__":
    unittest.main()
