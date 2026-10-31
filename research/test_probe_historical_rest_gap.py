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
        market, start, records, following, digest = select_bracketed_gap(self.trades, self.ohlc)
        self.assertEqual((market, start, len(records), len(following), digest),
                         ("BCHJPY", 300, 1, 1, "digest"))

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

    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_second_bounded_gap_candidate_selected(self, ohlc):
        self.write_trades([301, 901, 1501])
        ohlc.return_value = ({300, 900, 1500}, "digest")
        market, start, before, after, digest = select_bracketed_gap(
            self.trades, self.ohlc, candidate_index=1)
        self.assertEqual((market, start, len(before), len(after), digest),
                         ("BCHJPY", 900, 1, 1, "digest"))
        ohlc.assert_called_once()

    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_ohlc_rejected_first_gap_does_not_mask_later_valid_gap(self, ohlc):
        self.write_trades([301, 901, 1501])
        ohlc.return_value = ({300, 600, 900, 1500}, "digest")
        selected = select_bracketed_gap(self.trades, self.ohlc)
        self.assertEqual(selected[1], 900)

    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_out_of_range_candidate_index_abstains_without_rest(self, ohlc):
        ohlc.return_value = ({300, 900}, "digest")
        self.assertIsNone(select_bracketed_gap(
            self.trades, self.ohlc, candidate_index=1))

    def test_invalid_candidate_index_fails_closed(self):
        for index in (-1, 4, True, 1.5, None, "1"):
            with self.subTest(index=index), self.assertRaises(ValueError):
                select_bracketed_gap(self.trades, self.ohlc,
                                     candidate_index=index)

    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_later_invalid_market_still_fails_with_alternate_index(self, ohlc):
        self.write_trades([301, 901, 1501])
        with zipfile.ZipFile(self.trades, "a") as archive:
            archive.writestr("trades/ZZZUSD.csv", "bad,header\\n1,2,3\\n")
        with self.assertRaises(ValueError):
            select_bracketed_gap(self.trades, self.ohlc, candidate_index=1)
        ohlc.assert_not_called()

    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_audit_alternate_missing_candidate_never_creates_label(self, ohlc):
        ohlc.return_value = ({300, 900}, "digest")
        result = audit_bracketed_gap(self.trades, self.ohlc,
                                     candidate_index=1)
        self.assertEqual(result["status"], "abstain_no_bracketed_retained_gap")
        self.assertEqual(result["candidate_index"], 1)
        self.assertEqual(result["no_trade_intervals_verified"], 0)
        self.assertEqual(result["real_labels"], 0)
        self.assertIsNone(result["held_out_lift"])

    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_bounded_candidate_index_three_is_allowed_but_abstains(self, ohlc):
        ohlc.return_value = ({300, 900}, "digest")
        self.assertIsNone(select_bracketed_gap(
            self.trades, self.ohlc, candidate_index=3))

    @patch("probe_historical_rest_gap.corroborate_retained_ohlc")
    @patch("probe_historical_rest_gap.compare_rest_bucket")
    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_three_way_candidate_never_claims_verified_no_trade(self, ohlc, rest, three):
        ohlc.return_value = ({300, 900}, "digest")
        rest.side_effect = [
            {"status": "independent_rest_gap_candidate_correlated_not_complete",
             "following_bucket_witness_near": True, "pages": 1,
             "bytes_transferred": 120, "rest_cursor_trace": [{"page_sha256": "sha"}]},
            {"status": "independent_rest_bucket_correlated", "after_end_witness": True,
             "pages": 1, "bytes_transferred": 100}]
        three.return_value = {"status": "independent_rest_trade_ohlc_correlated",
                              "three_way_candle_correspondence": True}
        result = audit_bracketed_gap(self.trades, self.ohlc)
        self.assertEqual(result["status"], "independent_rest_bracketed_gap_candidate_not_complete")
        self.assertEqual(result["candidate_empty_gap_buckets"], [600])
        self.assertEqual(result["no_trade_intervals_verified"], 0)
        self.assertEqual(result["independent_complete_historical_intervals"], 0)
        self.assertEqual(result["real_labels"], 0)
        self.assertIsNone(result["held_out_lift"])
        self.assertFalse(result["production_modified"])
        self.assertEqual(rest.call_args_list[0].kwargs["gap_buckets"], 1)
        self.assertEqual(rest.call_args_list[1].args[1], 900)
        self.assertTrue(result["following_observed_candle_correlated"])
        self.assertEqual(result["total_rest_bytes_transferred"], 220)

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
        rest.return_value = {"status": "independent_rest_gap_candidate_correlated_not_complete",
                             "following_bucket_witness_near": True}
        three.return_value = {"status": "abstain_rest_trade_ohlc_disagreement",
                              "three_way_candle_correspondence": False}
        result = audit_bracketed_gap(self.trades, self.ohlc)
        self.assertEqual(result["status"], "abstain_rest_trade_ohlc_disagreement")
        self.assertEqual(result["candidate_empty_gap_buckets"], [])
        self.assertEqual(result["no_trade_intervals_verified"], 0)


    @patch("probe_historical_rest_gap.corroborate_retained_ohlc")
    @patch("probe_historical_rest_gap.compare_rest_bucket")
    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_missing_near_following_witness_abstains_before_second_rest(self, ohlc, rest, three):
        ohlc.return_value = ({300, 900}, "digest")
        rest.return_value = {"status": "independent_rest_gap_candidate_correlated_not_complete"}
        r = audit_bracketed_gap(self.trades, self.ohlc)
        self.assertEqual(r["status"], "abstain_rest_missing_near_following_witness")
        self.assertEqual(rest.call_count, 1)
        self.assertEqual(r["real_labels"], 0)
        three.assert_not_called()

    @patch("probe_historical_rest_gap.corroborate_retained_ohlc")
    @patch("probe_historical_rest_gap.compare_rest_bucket")
    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_following_rest_disagreement_rejects_candidate(self, ohlc, rest, three):
        ohlc.return_value = ({300, 900}, "digest")
        rest.side_effect = [
            {"status": "independent_rest_gap_candidate_correlated_not_complete",
             "following_bucket_witness_near": True},
            {"status": "abstain_rest_archive_disagreement"}]
        three.return_value = {"status": "independent_rest_trade_ohlc_correlated",
                              "three_way_candle_correspondence": True}
        r = audit_bracketed_gap(self.trades, self.ohlc)
        self.assertEqual(r["status"], "abstain_following_rest_bucket_unverified")
        self.assertEqual(r["candidate_empty_gap_buckets"], [])
        self.assertEqual(three.call_count, 1)

    @patch("probe_historical_rest_gap.corroborate_retained_ohlc")
    @patch("probe_historical_rest_gap.compare_rest_bucket")
    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_following_rest_requires_after_end_witness(self, ohlc, rest, three):
        ohlc.return_value = ({300, 900}, "digest")
        rest.side_effect = [
            {"status": "independent_rest_gap_candidate_correlated_not_complete",
             "following_bucket_witness_near": True},
            {"status": "independent_rest_bucket_correlated", "after_end_witness": False}]
        three.return_value = {"status": "independent_rest_trade_ohlc_correlated",
                              "three_way_candle_correspondence": True}
        r = audit_bracketed_gap(self.trades, self.ohlc)
        self.assertEqual(r["status"], "abstain_following_rest_bucket_unverified")
        self.assertEqual(r["real_labels"], 0)

    @patch("probe_historical_rest_gap.corroborate_retained_ohlc")
    @patch("probe_historical_rest_gap.compare_rest_bucket")
    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_following_ohlc_mismatch_rejects_candidate(self, ohlc, rest, three):
        ohlc.return_value = ({300, 900}, "digest")
        rest.side_effect = [
            {"status": "independent_rest_gap_candidate_correlated_not_complete",
             "following_bucket_witness_near": True},
            {"status": "independent_rest_bucket_correlated", "after_end_witness": True}]
        three.side_effect = [
            {"status": "independent_rest_trade_ohlc_correlated",
             "three_way_candle_correspondence": True},
            {"status": "abstain_rest_trade_ohlc_disagreement",
             "three_way_candle_correspondence": False}]
        r = audit_bracketed_gap(self.trades, self.ohlc)
        self.assertEqual(r["status"], "abstain_following_rest_ohlc_disagreement")
        self.assertEqual(r["candidate_empty_gap_buckets"], [])
        self.assertEqual(r["real_labels"], 0)

    @patch("probe_historical_rest_gap.corroborate_retained_ohlc")
    @patch("probe_historical_rest_gap.compare_rest_bucket")
    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_following_rest_transport_error_abstains(self, ohlc, rest, three):
        ohlc.return_value = ({300, 900}, "digest")
        rest.side_effect = [
            {"status": "independent_rest_gap_candidate_correlated_not_complete",
             "following_bucket_witness_near": True},
            OSError("following page unavailable")]
        three.return_value = {"status": "independent_rest_trade_ohlc_correlated",
                              "three_way_candle_correspondence": True}
        r = audit_bracketed_gap(self.trades, self.ohlc)
        self.assertEqual(r["status"], "abstain_following_rest_transport_or_source_error")
        self.assertEqual(r["following_error_type"], "OSError")
        self.assertEqual(r["real_labels"], 0)

    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_oversized_following_trade_bucket_never_selected(self, ohlc):
        self.write_trades([301] + [901 + i * 0.001 for i in range(101)])
        self.assertIsNone(select_bracketed_gap(self.trades, self.ohlc))
        ohlc.assert_not_called()

    @patch("probe_historical_rest_gap.corroborate_retained_ohlc")
    @patch("probe_historical_rest_gap.compare_rest_bucket")
    @patch("probe_historical_rest_gap.load_ohlc_starts")
    def test_wrong_preceding_ohlc_status_cannot_pass_true_boolean(self, ohlc, rest, three):
        ohlc.return_value = ({300, 900}, "digest")
        rest.return_value = {"status": "independent_rest_gap_candidate_correlated_not_complete",
                             "following_bucket_witness_near": True}
        three.return_value = {"status": "abstain_ohlc_unverified",
                              "three_way_candle_correspondence": True}
        r = audit_bracketed_gap(self.trades, self.ohlc)
        self.assertEqual(r["status"], "abstain_ohlc_unverified")
        self.assertEqual(rest.call_count, 1)

if __name__ == "__main__":
    unittest.main()
