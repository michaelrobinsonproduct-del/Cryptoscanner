"""Offline fixtures for bounded 12-candle historical REST/retained-source audit."""
import io
import json
import tempfile
import unittest
import urllib.parse
import zipfile
from pathlib import Path
from unittest.mock import patch

from probe_historical_rest_window import (
    corroborate_observed_window, select_observed_window, WINDOW_CANDLES,
)


class Response:
    status = 200
    headers = {}
    def __init__(self, rows, last):
        self.data = io.BytesIO(json.dumps({"error": [], "result": {
            "BCHJPY": rows, "last": str(last)}}).encode())
    def __enter__(self): return self
    def __exit__(self, *args): return False
    def read(self, n): return self.data.read(n)


class HistoricalWindowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "trades.zip"
        self.starts = [300 + i * 300 for i in range(WINDOW_CANDLES)]
        self.write_trades(self.starts)

    def write_trades(self, starts):
        rows = ["timestamp,price,volume,type,order_type,misc,trade_id"]
        rows += [f"{start+1},{100+i},1,b,l,,trade-{i}" for i, start in enumerate(starts)]
        with zipfile.ZipFile(self.path, "w") as z:
            z.writestr("trades/BCHJPY.csv", "\n".join(rows) + "\n")

    def opener(self, request, timeout):
        args = urllib.parse.parse_qs(urllib.parse.urlparse(request.full_url).query)
        start = (int(args["since"][0]) + 1) // 1_000_000_000
        i = (start - 300) // 300
        return Response([[str(100+i), "1", start+1, "b", "l", ""],
                         [str(101+i), "1", start+301, "b", "l", ""]],
                        int(args["since"][0]) + 1000000000)

    @patch("probe_historical_rest_window.corroborate_retained_ohlc")
    def test_twelve_realistic_independent_rest_pages_correlate_but_not_labels(self, three):
        three.return_value = {"status": "independent_rest_trade_ohlc_correlated",
                              "three_way_candle_correspondence": True}
        r = corroborate_observed_window(self.path, "unused", opener=self.opener)
        self.assertEqual(r["status"], "independent_rest_observed_window_correlated_not_complete")
        self.assertEqual(r["observed_buckets_correlated"], 12)
        self.assertEqual(r["rest_pages"], 12)
        self.assertEqual(len(r["rest_page_sha256"]), 12)
        self.assertEqual(r["real_labels"], 0)
        self.assertEqual(r["independent_complete_historical_intervals"], 0)
        self.assertFalse(r["independent_quarterly_completeness_verified"])
        self.assertEqual(three.call_count, 12)

    def test_gap_never_filled_as_no_trade(self):
        self.write_trades(self.starts[:5] + self.starts[6:])
        self.assertIsNone(select_observed_window(self.path))
        r = corroborate_observed_window(self.path, "unused")
        self.assertEqual(r["status"], "abstain_no_contiguous_observed_window")
        self.assertEqual(r["no_trade_intervals_verified"], 0)

    def test_duplicate_source_trade_id_rejected(self):
        rows = ["timestamp,price,volume,type,order_type,misc,trade_id",
                "301,100,1,b,l,,duplicate", "601,101,1,b,l,,duplicate"]
        with zipfile.ZipFile(self.path, "w") as z:
            z.writestr("trades/BCHJPY.csv", "\n".join(rows) + "\n")
        with self.assertRaises(ValueError):
            select_observed_window(self.path)

    def test_window_size_restricted(self):
        for n in (0, 1, 13, True, 3.5):
            with self.subTest(n=n), self.assertRaises(ValueError):
                select_observed_window(self.path, candles=n)

    @patch("probe_historical_rest_window.corroborate_retained_ohlc")
    def test_first_three_way_mismatch_stops_without_labels(self, three):
        three.return_value = {"status": "abstain_rest_trade_ohlc_disagreement",
                              "three_way_candle_correspondence": False}
        r = corroborate_observed_window(self.path, "unused", opener=self.opener)
        self.assertEqual(r["observed_buckets_correlated"], 0)
        self.assertEqual(r["first_unverified_bucket"], 300)
        self.assertEqual(r["real_labels"], 0)
        self.assertEqual(three.call_count, 1)

    @patch("probe_historical_rest_window.corroborate_retained_ohlc")
    def test_rest_price_mismatch_stops_without_labels(self, three):
        def wrong(request, timeout):
            args = urllib.parse.parse_qs(urllib.parse.urlparse(request.full_url).query)
            start = (int(args["since"][0]) + 1) // 1_000_000_000
            return Response([["999", "1", start+1, "b", "l", ""],
                             ["999", "1", start+301, "b", "l", ""]],
                            int(args["since"][0]) + 1000000000)
        r = corroborate_observed_window(self.path, "unused", opener=wrong)
        self.assertEqual(r["observed_buckets_correlated"], 0)
        self.assertEqual(r["status"], "abstain_rest_archive_disagreement")
        three.assert_not_called()

    def test_unsafe_member_path_rejected(self):
        with zipfile.ZipFile(self.path, "w") as z:
            z.writestr("trades/../../BCHJPY.csv", "invalid")
        self.assertIsNone(select_observed_window(self.path))

    def test_duplicate_member_rejected(self):
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            with zipfile.ZipFile(self.path, "w") as z:
                z.writestr("trades/BCHJPY.csv", "invalid")
                z.writestr("trades/BCHJPY.csv", "invalid")
        with self.assertRaises(ValueError):
            select_observed_window(self.path)

    def test_invalid_delay_rejected(self):
        for delay in (-1, 3, float("nan")):
            with self.subTest(delay=delay), self.assertRaises(ValueError):
                corroborate_observed_window(self.path, "unused", delay_seconds=delay)

    @patch("probe_historical_rest_window.corroborate_retained_ohlc")
    def test_transport_failure_abstains_without_labels(self, three):
        def fail(request, timeout):
            raise OSError("offline")
        r = corroborate_observed_window(self.path, "unused", opener=fail)
        self.assertEqual(r["status"], "abstain_rest_transport_or_source_error")
        self.assertEqual(r["real_labels"], 0)
        three.assert_not_called()


if __name__ == "__main__":
    unittest.main()
