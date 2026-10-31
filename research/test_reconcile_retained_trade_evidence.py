import hashlib
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from reconcile_retained_trade_evidence import reconcile, _candidate_windows, _validate_retained_ohlc
from inventory_kraken_archive import EXPECTED_SHA256


class RetainedReconciliationTests(unittest.TestCase):
    def fixture(self, root, *, bad_volume=False, duplicate_id=False, missing_trade=False, bad_tail=False, bad_gap=False, bad_source_rows=False):
        candle = ('300,100,101,100,101,7,2\n' if bad_volume
                  else '300,100,101,100,101,5,2\n').encode()
        trade = ('timestamp,price,volume,type,order_type,misc,trade_id\n'
                 '300,100,2,b,l,,id1\n')
        if not missing_trade:
            trade += '301,101,3,s,m,,id2\n'
        if duplicate_id:
            trade += '302,101,1,b,l,,id1\n'
        trade = trade.encode()
        om = {"schema": 1, "source_archive_sha256": EXPECTED_SHA256,
              "independent_trade_completeness": False,
              "markets": {"ABUSD_5.csv": {
                  "retained_sha256": hashlib.sha256(candle).hexdigest(),
                  "retained_rows": 1,
                  "source_rows": 0 if bad_source_rows else 1,
                  "retained_first_open": 600 if bad_tail else 300,
                  "retained_last_open": 300,
                  "source_gap_events": 1 if bad_gap else 0,
                  "source_missing_intervals": 0,
                  "source_longest_contiguous": 1}}}
        tm = {"schema_version": 1, "source_archive_full_sha256_verified": False,
              "real_labels": 0, "markets": {"ABUSD.csv": {
                  "member_sha256": hashlib.sha256(trade).hexdigest(),
                  "member_bytes": len(trade), "member_crc_verified": True}}}
        def nested(path, name, entries):
            buf = io.BytesIO()
            with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as z:
                for entry, data in entries.items():
                    z.writestr(entry, data)
            with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as z:
                z.writestr(name, buf.getvalue())
        o, t = Path(root)/"o.zip", Path(root)/"t.zip"
        nested(o, "reusable_ohlc_evidence.zip",
               {"manifest.json": json.dumps(om), "candles/ABUSD_5.csv": candle})
        nested(t, "bounded_independent_trade_members.zip",
               {"manifest.json": json.dumps(tm), "trades/ABUSD.csv": trade})
        return o, t

    def test_realistic_exact_match_is_not_a_real_label(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root)
            r = reconcile(o, t,
                          expected_ohlc_digest=hashlib.sha256(o.read_bytes()).hexdigest(),
                          expected_trade_digest=hashlib.sha256(t.read_bytes()).hexdigest())
            m = r["markets"]["ABUSD.csv"]
            self.assertEqual(m["exact_trade_ohlc_candidate_intervals"], 1)
            self.assertEqual(m["verified_complete_intervals"], 0)
            self.assertEqual(r["real_labels"], 0)
            self.assertFalse(r["source_trade_archive_sha256_verified"])
            audit = m["candidate_outcome_audit"]
            self.assertEqual(audit["real_labels"], 0)
            self.assertEqual(audit["held_out_evaluation"], "not_authorized")
            self.assertEqual(audit["horizons"]["1"]["candidate_entries"], 1)
            self.assertEqual(audit["horizons"]["1"]["excluded_beyond_retained_end"], 1)

    def test_volume_mismatch_not_accepted(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root, bad_volume=True)
            m = reconcile(o, t)["markets"]["ABUSD.csv"]
            self.assertEqual(m["exact_trade_ohlc_candidate_intervals"], 0)
            self.assertEqual(m["mismatch_counts"]["aggregation_mismatch"], 1)

    def test_missing_trade_not_assumed_no_trade(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root, missing_trade=True)
            m = reconcile(o, t)["markets"]["ABUSD.csv"]
            self.assertEqual(m["exact_trade_ohlc_candidate_intervals"], 0)
            self.assertEqual(m["no_trade_or_source_gap_semantics"], "unknown")

    def test_duplicate_trade_id_fails_closed(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root, duplicate_id=True)
            with self.assertRaises(ValueError):
                reconcile(o, t)

    def test_artifact_digest_mismatch_fails_closed(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root)
            with self.assertRaises(ValueError):
                reconcile(o, t, expected_trade_digest="0"*64)

    def test_unpacked_actions_inner_zip_reuse(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root)
            oi, ti = Path(root)/"inner_o.zip", Path(root)/"inner_t.zip"
            with zipfile.ZipFile(o) as z:
                oi.write_bytes(z.read("reusable_ohlc_evidence.zip"))
            with zipfile.ZipFile(t) as z:
                ti.write_bytes(z.read("bounded_independent_trade_members.zip"))
            r = reconcile(oi, ti)
            self.assertEqual(r["markets"]["ABUSD.csv"]["exact_trade_ohlc_candidate_intervals"], 1)
            self.assertEqual(r["real_labels"], 0)

    def test_missing_future_candles_cannot_create_candidate_windows(self):
        timestamps = {300 + i*300 for i in range(13)}
        self.assertEqual(_candidate_windows(timestamps)["1"], 1)
        self.assertEqual(_candidate_windows(timestamps)["48"], 0)
        self.assertEqual(_candidate_windows(timestamps - {900})["1"], 0)

    def test_oversized_artifact_rejected_before_reading(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root)
            with o.open("r+b") as stream:
                stream.truncate(80 * 1024 * 1024 + 1)
            with self.assertRaisesRegex(ValueError, "oversized input artifact"):
                reconcile(o, t)

    def test_report_never_converts_exact_match_to_predictive_label(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root)
            report = reconcile(o, t)
            self.assertEqual(report["real_labels"], 0)
            self.assertEqual(report["held_out_evaluation"], "not_authorized")
            m = report["markets"]["ABUSD.csv"]
            self.assertEqual(m["candidate_outcome_audit"]["horizons"]["48"]["candidate_full_future_windows"], 0)
            self.assertEqual(m["verified_complete_intervals"], 0)
            self.assertEqual(m["no_trade_or_source_gap_semantics"], "unknown")


    def test_retained_source_tail_timestamp_mismatch_abstains(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root, bad_tail=True)
            with self.assertRaisesRegex(ValueError, "source-tail provenance"):
                reconcile(o, t)

    def test_full_retention_gap_metadata_mismatch_abstains(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root, bad_gap=True)
            with self.assertRaisesRegex(ValueError, "gap metadata mismatch"):
                reconcile(o, t)

    def test_source_row_count_cannot_be_less_than_retained(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root, bad_source_rows=True)
            with self.assertRaisesRegex(ValueError, "source-tail provenance"):
                reconcile(o, t)

    def test_report_documented_ohlc_gaps_do_not_unlock_trade_labels(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root)
            r = reconcile(o, t)
            m = r["markets"]["ABUSD.csv"]
            self.assertTrue(m["retained_source_tail_contract_verified"])
            self.assertEqual(m["ohlc_retained_interior_gap_events"], 0)
            self.assertEqual(m["ohlc_retained_missing_no_trade_candidate_intervals"], 0)
            self.assertIn("support.kraken.com", m["ohlc_documented_no_trade_semantics_reference"])
            self.assertFalse(m["ohlc_gap_semantics_authorize_labels"])
            self.assertEqual(r["real_labels"], 0)


    def _meta(self, *, rows=1, source_rows=None, gaps=0, missing=0,
              longest=1, first=300, last=300):
        return {"retained_rows": rows, "source_rows": rows if source_rows is None else source_rows,
                "retained_first_open": first, "retained_last_open": last,
                "source_gap_events": gaps, "source_missing_intervals": missing,
                "source_longest_contiguous": longest}

    def test_retained_ohlc_gap_and_contiguity_are_recomputed(self):
        raw = b"300,100,101,100,101,5,2\n900,100,101,100,101,5,2\n"
        rows, gaps = _validate_retained_ohlc(
            raw, self._meta(rows=2, gaps=1, missing=1, last=900))
        self.assertEqual(len(rows), 2)
        self.assertEqual(gaps, {"gap_events": 1, "missing_intervals": 1,
                                "longest_contiguous": 1})

    def test_retained_ohlc_duplicate_timestamp_abstains(self):
        raw = b"300,100,101,100,101,5,2\n300,100,101,100,101,5,2\n"
        with self.assertRaisesRegex(ValueError, "timestamp order"):
            _validate_retained_ohlc(raw, self._meta(rows=2))

    def test_retained_ohlc_reverse_timestamp_abstains(self):
        raw = b"600,100,101,100,101,5,2\n300,100,101,100,101,5,2\n"
        with self.assertRaisesRegex(ValueError, "timestamp order"):
            _validate_retained_ohlc(raw, self._meta(rows=2))

    def test_retained_ohlc_fractional_or_unaligned_timestamp_abstains(self):
        for timestamp in ("300.5", "301", "-300"):
            with self.subTest(timestamp=timestamp):
                raw = (timestamp + ",100,101,100,101,5,2\n").encode()
                with self.assertRaisesRegex(ValueError, "timestamp order"):
                    _validate_retained_ohlc(raw, self._meta())

    def test_retained_ohlc_nonfinite_values_abstain(self):
        for value in ("nan", "inf", "-inf"):
            with self.subTest(value=value):
                raw = ("300,100," + value + ",100,101,5,2\n").encode()
                with self.assertRaisesRegex(ValueError, "nonfinite"):
                    _validate_retained_ohlc(raw, self._meta())

    def test_retained_ohlc_invalid_bounds_and_negative_volume_abstain(self):
        for raw in (b"300,100,99,100,101,5,2\n",
                    b"300,100,101,100,101,-1,2\n",
                    b"300,100,101,100,101,5,2.5\n"):
            with self.subTest(raw=raw):
                with self.assertRaisesRegex(ValueError, "candle values"):
                    _validate_retained_ohlc(raw, self._meta())

    def test_retained_ohlc_wrong_column_count_abstains(self):
        with self.assertRaisesRegex(ValueError, "column count"):
            _validate_retained_ohlc(b"300,100,101,100,101,5\n", self._meta())

    def test_partial_source_tail_cannot_underreport_observed_gaps(self):
        raw = b"300,100,101,100,101,5,2\n900,100,101,100,101,5,2\n"
        with self.assertRaisesRegex(ValueError, "gap floor"):
            _validate_retained_ohlc(
                raw, self._meta(rows=2, source_rows=3, gaps=0, missing=0, last=900))

    def test_source_longest_contiguous_cannot_underreport_retained_tail(self):
        raw = b"300,100,101,100,101,5,2\n600,100,101,100,101,5,2\n"
        with self.assertRaisesRegex(ValueError, "source-tail provenance"):
            _validate_retained_ohlc(
                raw, self._meta(rows=2, source_rows=3, longest=1, last=600))

    def test_source_metadata_bool_or_fractional_counts_abstain(self):
        for key, value in (("source_rows", True), ("source_gap_events", 1.5),
                           ("source_longest_contiguous", False)):
            with self.subTest(key=key):
                meta = self._meta()
                meta[key] = value
                with self.assertRaisesRegex(ValueError, "metadata"):
                    _validate_retained_ohlc(b"300,100,101,100,101,5,2\n", meta)

    def test_full_source_gap_and_longest_metadata_must_match(self):
        raw = b"300,100,101,100,101,5,2\n600,100,101,100,101,5,2\n"
        with self.assertRaisesRegex(ValueError, "gap metadata mismatch"):
            _validate_retained_ohlc(
                raw, self._meta(rows=2, gaps=1, missing=1, longest=2, last=600))

    def test_reconciliation_reports_validation_without_authorizing_labels(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root)
            result = reconcile(o, t)
            market = result["markets"]["ABUSD.csv"]
            self.assertTrue(market["retained_ohlc_structure_validated"])
            self.assertTrue(market["retained_ohlc_gap_floor_verified"])
            self.assertEqual(market["retained_ohlc_longest_contiguous"], 1)
            self.assertEqual(result["real_labels"], 0)
            self.assertEqual(result["held_out_evaluation"], "not_authorized")


    def test_reconciled_coverage_census_has_conserved_exact_intervals(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root)
            m = reconcile(o, t)["markets"]["ABUSD.csv"]
            census = m["trade_ohlc_coverage_census"]
            self.assertEqual(census["overlap"]["exact_candidate_intervals"], 1)
            self.assertEqual(census["overlap"]["intervals_in_shared_observed_span"], 1)
            self.assertEqual(census["horizons"]["1"]["complete_descriptive_windows"], 0)
            self.assertEqual(census["horizons"]["1"]["excluded_beyond_ohlc_tail"], 1)
            self.assertFalse(census["independent_trade_source_completeness_verified"])
            self.assertEqual(census["verified_predictive_labels"], 0)

    def test_aggregation_mismatch_is_reported_as_unverified_overlap(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root, bad_volume=True)
            m = reconcile(o, t)["markets"]["ABUSD.csv"]
            census = m["trade_ohlc_coverage_census"]
            self.assertEqual(census["overlap"]["exact_candidate_intervals"], 0)
            self.assertEqual(census["overlap"]["both_present_but_nonmatching"], 1)
            self.assertEqual(census["horizons"]["48"]["candidate_entries"], 0)
            self.assertEqual(m["real_labels"], 0)

    def test_missing_trade_cannot_be_inferred_as_no_trade_from_ohlc(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root, missing_trade=True)
            m = reconcile(o, t)["markets"]["ABUSD.csv"]
            census = m["trade_ohlc_coverage_census"]
            self.assertEqual(census["overlap"]["both_present_but_nonmatching"], 1)
            self.assertEqual(census["no_trade_inference"],
                             "not_authorized_for_unobserved_intervals")
            self.assertFalse(census["retained_edges_complete"])
            self.assertEqual(m["verified_complete_intervals"], 0)


if __name__ == "__main__":
    unittest.main()
