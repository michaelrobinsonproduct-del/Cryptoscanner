"""Offline failure-injection for bracketed historical REST gap candidates."""
import tempfile
import unittest
import warnings
import zipfile
from pathlib import Path
from unittest.mock import patch

from probe_historical_rest_gap import audit_bracketed_gap, select_bracketed_gap


class BracketedGapTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.trades = Path(self.temp.name) / "trades.zip"
        self.ohlc = Path(self.temp.name) / "ohlc.zip"
        self.ohlc.write_bytes(b"fixture-not-source-authenticated")
        self.write_trades([301, 901])

    def write_trades(self, stamps):
        rows = ["timestamp,price,volume,type,order_type,misc,trade_id"]
        rows.extend(f"{t},{100+i},1,b,l,,trade-{i}" for i, t in enumerate(stamps))
        with zipfile.ZipFile(self.trades, "w") as archive:
            archive.writestr("trades/BCHJPY.csv", "\n".join(rows) + "\n")

    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_selects_single_gap_only_if_retained_ohlc_agrees(self, ohlc):
        ohlc.return_value = ({300, 900}, "digest")
        market, start, records, digest = select_bracketed_gap(self.trades, self.ohlc)
        self.assertEqual((market, start, len(records), digest),
                         ("BCHJPY", 300, 1, "digest"))

    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_ohlc_candle_in_gap_disqualifies_candidate(self, ohlc):
        ohlc.return_value = ({300, 600, 900}, "digest")
        self.assertIsNone(select_bracketed_gap(self.trades, self.ohlc))

    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_missing_following_ohlc_candle_disqualifies(self, ohlc):
        ohlc.return_value = ({300}, "digest")
        self.assertIsNone(select_bracketed_gap(self.trades, self.ohlc))

    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_no_trade_gap_candidate_when_retained_trades_contiguous(self, ohlc):
        self.write_trades([301, 601, 901])
        self.assertIsNone(select_bracketed_gap(self.trades, self.ohlc))
        ohlc.assert_not_called()

    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_later_malformed_market_cannot_hide(self, ohlc):
        with zipfile.ZipFile(self.trades, "a") as archive:
            archive.writestr("trades/ZZZUSD.csv", "invalid,header\n1,2,3\n")
        with self.assertRaises(ValueError):
            select_bracketed_gap(self.trades, self.ohlc)
        ohlc.assert_not_called()

    def test_duplicate_member_names_rejected(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            with zipfile.ZipFile(self.trades, "a") as archive:
                archive.writestr("trades/BCHJPY.csv", "bad")
        with self.assertRaises(ValueError):
            select_bracketed_gap(self.trades, self.ohlc)

    def test_unsafe_market_name_rejected(self):
        with zipfile.ZipFile(self.trades, "a") as archive:
            archive.writestr("trades/ZZZ-USD.csv", "bad")
        with self.assertRaises(ValueError):
            select_bracketed_gap(self.trades, self.ohlc)

    @patch("probe_historical_rest_gap.corroborate_retained_ohlc")
    @patch("probe_historical_rest_gap.compare_rest_bucket")
    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_three_way_candidate_never_claims_verified_no_trade(self, ohlc, rest, three):
        ohlc.return_value = ({300, 900}, "digest")
        rest.return_value = {
            "status": "independent_rest_gap_candidate_correlated_not_complete",
            "pages": 1, "bytes_transferred": 120, "rest_cursor_trace": [{"page_sha256": "sha"}]}
        three.return_value = {"three_way_candle_correspondence": True}
        result = audit_bracketed_gap(self.trades, self.ohlc)
        self.assertEqual(result["status"], "independent_rest_bracketed_gap_candidate_not_complete")
        self.assertEqual(result["candidate_empty_gap_buckets"], [600])
        self.assertEqual(result["no_trade_intervals_verified"], 0)
        self.assertEqual(result["independent_complete_historical_intervals"], 0)
        self.assertEqual(result["real_labels"], 0)
        self.assertIsNone(result["held_out_lift"])
        self.assertFalse(result["production_modified"])
        self.assertEqual(rest.call_args.kwargs["gap_buckets"], 1)

    @patch("probe_historical_rest_gap.corroborate_retained_ohlc")
    @patch("probe_historical_rest_gap.compare_rest_bucket")
    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_rest_gap_trade_rejects_candidate(self, ohlc, rest, three):
        ohlc.return_value = ({300, 900}, "digest")
        rest.return_value = {"status": "abstain_rest_gap_contains_trades"}
        result = audit_bracketed_gap(self.trades, self.ohlc)
        self.assertEqual(result["status"], "abstain_rest_gap_contains_trades")
        self.assertEqual(result["candidate_empty_gap_buckets"], [])
        three.assert_not_called()

    @patch("probe_historical_rest_gap.compare_rest_bucket")
    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_rest_transport_error_abstains(self, ohlc, rest):
        ohlc.return_value = ({300, 900}, "digest")
        rest.side_effect = OSError("source unavailable")
        result = audit_bracketed_gap(self.trades, self.ohlc)
        self.assertEqual(result["status"], "abstain_rest_transport_or_source_error")
        self.assertEqual(result["error_type"], "OSError")
        self.assertEqual(result["real_labels"], 0)

    @patch("probe_historical_rest_gap.corroborate_retained_ohlc")
    @patch("probe_historical_rest_gap.compare_rest_bucket")
    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_three_way_disagreement_rejects_gap_candidate(self, ohlc, rest, three):
        ohlc.return_value = ({300, 900}, "digest")
        rest.return_value = {"status": "independent_rest_gap_candidate_correlated_not_complete"}
        three.return_value = {"status": "abstain_rest_trade_ohlc_disagreement",
                              "three_way_candle_correspondence": False}
        result = audit_bracketed_gap(self.trades, self.ohlc)
        self.assertEqual(result["status"], "abstain_rest_trade_ohlc_disagreement")
        self.assertEqual(result["candidate_empty_gap_buckets"], [])
        self.assertEqual(result["no_trade_intervals_verified"], 0)


if __name__ == "__main__":
    unittest.main()
