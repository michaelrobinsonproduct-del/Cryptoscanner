import io
import json
import unittest
from probe_historical_rest_interval import compare_rest_bucket


class Response:
    status = 200
    headers = {}
    def __init__(self, payload):
        self.data = io.BytesIO(json.dumps(payload).encode())
    def __enter__(self): return self
    def __exit__(self, *args): return False
    def read(self, n): return self.data.read(n)


def make_page(rows, cursor="1900000000000000000", *, error=None):
    return {"error": error or [], "result": {"DENTEUR": rows, "last": cursor}}


class HistoricalRestProbeTests(unittest.TestCase):
    def setUp(self):
        self.expected = [(300.1, 0.00001, 2, 0), (301.5, 0.000011, 3, 1)]
        self.rows = [["0.00001", "2", 300.1, "b", "l", ""],
                     ["0.000011", "3", 301.5, "s", "m", ""],
                     ["0.000011", "1", 601, "b", "m", ""]]

    def test_realistic_bounded_correspondence_still_not_labels(self):
        r = compare_rest_bucket("DENTEUR", 300, self.expected,
                                opener=lambda *a, **kw: Response(make_page(self.rows)))
        self.assertEqual(r["status"], "independent_rest_bucket_correlated")
        self.assertEqual(r["rest_trades"], 2)
        self.assertEqual(r["real_labels"], 0)
        self.assertFalse(r["independent_quarterly_completeness_verified"])

    def test_missing_trade_abstains(self):
        r = compare_rest_bucket("DENTEUR", 300, self.expected,
                                opener=lambda *a, **kw: Response(make_page(self.rows[1:])))
        self.assertEqual(r["status"], "abstain_rest_archive_disagreement")

    def test_microprice_mismatch_abstains(self):
        rows = [list(x) for x in self.rows]
        rows[0][0] = "0.000019"
        r = compare_rest_bucket("DENTEUR", 300, self.expected,
                                opener=lambda *a, **kw: Response(make_page(rows)))
        self.assertEqual(r["status"], "abstain_rest_archive_disagreement")

    def test_stale_api_history_is_not_a_source_mismatch(self):
        rows = [["1", "1", 1800000000, "b", "l", ""]]
        r = compare_rest_bucket("DENTEUR", 300, self.expected,
                                opener=lambda *a, **kw: Response(make_page(rows)))
        self.assertEqual(r["status"], "abstain_historical_range_unavailable")

    def test_nonadvancing_cursor_aborts(self):
        with self.assertRaisesRegex(RuntimeError, "nonadvancing"):
            compare_rest_bucket("DENTEUR", 300, self.expected,
                opener=lambda *a, **kw: Response(make_page(self.rows, "1")))

    def test_error_aborts(self):
        with self.assertRaisesRegex(RuntimeError, "REST error"):
            compare_rest_bucket("DENTEUR", 300, self.expected,
                opener=lambda *a, **kw: Response(make_page(self.rows, error=["EGeneral:fail"])))

    def test_unwitnessed_tail_abstains(self):
        cursor = ["301500000000", "303500000000", "305500000000", "307500000000"]
        i = iter(range(4))
        def page(*a, **kw):
            j = next(i)
            rows = [["0.00001", "2", 300.1+j*2, "b", "l", ""],
                    ["0.000011", "3", 301.5+j*2, "s", "m", ""]]
            return Response(make_page(rows, cursor[j]))
        r = compare_rest_bucket("DENTEUR", 300, self.expected, opener=page)
        self.assertEqual(r["status"], "abstain_rest_pagination_or_history_limit")
        self.assertEqual(r["real_labels"], 0)

    def test_malformed_rows_fail_closed(self):
        for rows in ([['NaN','1',300], self.rows[-1]],
                     [["1", "-2", 300], self.rows[-1]],
                     [["1", "1", 310], ["1", "1", 301], self.rows[-1]]):
            with self.subTest(rows=rows), self.assertRaises(RuntimeError):
                compare_rest_bucket("DENTEUR", 300, self.expected,
                    opener=lambda *a, **kw: Response(make_page(rows)))

    def test_bad_request_never_fetches(self):
        for pair, start, expected in (("../", 300, self.expected),
                                      ("DENTEUR", 301, self.expected),
                                      ("DENTEUR", 300, [])):
            with self.subTest(pair=pair,start=start), self.assertRaises(ValueError):
                compare_rest_bucket(pair, start, expected, opener=lambda *a, **kw: self.fail("network"))

    def test_bounded_page_size_aborts(self):
        class Huge(Response):
            def read(self, n): return b"x" * (n+1)
        with self.assertRaisesRegex(RuntimeError, "budget"):
            compare_rest_bucket("DENTEUR", 300, self.expected,
                opener=lambda *a, **kw: Huge(make_page(self.rows)))


    def test_rest_cursor_trace_has_verifiable_request_and_response(self):
        r = compare_rest_bucket("DENTEUR", 300, self.expected,
                                opener=lambda *a, **kw: Response(make_page(self.rows)))
        trace = r["rest_cursor_trace"]
        self.assertEqual(len(trace), 1)
        self.assertEqual(trace[0]["requested_since"], "299999999999")
        self.assertEqual(trace[0]["returned_last"], "1900000000000000000")
        self.assertEqual(trace[0]["rows"], 3)
        self.assertTrue(trace[0]["after_end_witness"])
        self.assertEqual(trace[0]["page_sha256"], r["rest_page_sha256"][0])

    def test_rest_cursor_behind_observed_trades_rejected(self):
        with self.assertRaisesRegex(RuntimeError, "cursor predates"):
            compare_rest_bucket("DENTEUR", 300, self.expected,
                opener=lambda *a, **kw: Response(make_page(self.rows, "300000000000")))

    def test_duplicate_rest_trade_ids_rejected(self):
        rows = [self.rows[0] + [42], self.rows[1] + [42], self.rows[2] + [43]]
        with self.assertRaisesRegex(RuntimeError, "duplicate or invalid REST trade id"):
            compare_rest_bucket("DENTEUR", 300, self.expected,
                opener=lambda *a, **kw: Response(make_page(rows)))

    def test_unique_rest_trade_ids_preserve_correspondence(self):
        rows = [row + [i + 1] for i, row in enumerate(self.rows)]
        r = compare_rest_bucket("DENTEUR", 300, self.expected,
            opener=lambda *a, **kw: Response(make_page(rows)))
        self.assertEqual(r["status"], "independent_rest_bucket_correlated")
        self.assertEqual(r["real_labels"], 0)

    def test_invalid_rest_side_or_order_type_rejected(self):
        for index, value in ((3, "x"), (4, "z")):
            rows = [list(row) for row in self.rows]
            rows[0][index] = value
            with self.subTest(index=index), self.assertRaisesRegex(RuntimeError, "schema"):
                compare_rest_bucket("DENTEUR", 300, self.expected,
                    opener=lambda *a, **kw: Response(make_page(rows)))

    def test_missing_rest_fields_rejected(self):
        for row in (self.rows[0][:3], self.rows[0] + ["id", "extra"]):
            with self.subTest(row=row), self.assertRaisesRegex(RuntimeError, "schema"):
                compare_rest_bucket("DENTEUR", 300, self.expected,
                    opener=lambda *a, **kw: Response(make_page([row, self.rows[-1]])))

    def test_empty_or_boolean_rest_trade_id_rejected(self):
        for trade_id in ("", True):
            rows = [self.rows[0] + [trade_id], self.rows[-1] + [10]]
            with self.subTest(trade_id=trade_id), self.assertRaisesRegex(RuntimeError, "trade id"):
                compare_rest_bucket("DENTEUR", 300, self.expected,
                    opener=lambda *a, **kw: Response(make_page(rows)))

    def test_malformed_after_end_trade_cannot_hide_in_successful_page(self):
        rows = [list(x) for x in self.rows]
        rows.append(["1", "1", 602, "bad", "l", ""])
        with self.assertRaisesRegex(RuntimeError, "schema"):
            compare_rest_bucket("DENTEUR", 300, self.expected,
                opener=lambda *a, **kw: Response(make_page(rows)))

    def test_duplicate_trade_id_after_end_rejected(self):
        rows = [self.rows[0] + [10], self.rows[1] + [11],
                self.rows[2] + [12], ["1", "1", 602, "b", "l", "", 12]]
        with self.assertRaisesRegex(RuntimeError, "trade id"):
            compare_rest_bucket("DENTEUR", 300, self.expected,
                opener=lambda *a, **kw: Response(make_page(rows)))

    def test_source_schema_failure_does_not_claim_complete_interval(self):
        rows = [self.rows[0][:3], self.rows[-1]]
        with self.assertRaises(RuntimeError):
            compare_rest_bucket("DENTEUR", 300, self.expected,
                opener=lambda *a, **kw: Response(make_page(rows)))


    def test_duplicate_rest_last_json_key_rejected(self):
        raw = ('{"error":[],"result":{"DENTEUR":' +
               json.dumps(self.rows) +
               ',"last":"1900000000000000000","last":"1900000000000000001"}}')
        class Raw(Response):
            def __init__(self): self.data = io.BytesIO(raw.encode())
        with self.assertRaisesRegex(RuntimeError, "duplicate Kraken REST JSON key"):
            compare_rest_bucket("DENTEUR", 300, self.expected, opener=lambda *a, **kw: Raw())

    def test_duplicate_rest_market_json_key_rejected(self):
        raw = ('{"error":[],"result":{"DENTEUR":' +
               json.dumps(self.rows) + ',"DENTEUR":' +
               json.dumps(self.rows) + ',"last":"1900000000000000000"}}')
        class Raw(Response):
            def __init__(self): self.data = io.BytesIO(raw.encode())
        with self.assertRaisesRegex(RuntimeError, "duplicate Kraken REST JSON key"):
            compare_rest_bucket("DENTEUR", 300, self.expected, opener=lambda *a, **kw: Raw())

    def test_duplicate_rest_error_json_key_rejected(self):
        raw = ('{"error":[],"error":[],"result":{"DENTEUR":' +
               json.dumps(self.rows) + ',"last":"1900000000000000000"}}')
        class Raw(Response):
            def __init__(self): self.data = io.BytesIO(raw.encode())
        with self.assertRaisesRegex(RuntimeError, "duplicate Kraken REST JSON key"):
            compare_rest_bucket("DENTEUR", 300, self.expected, opener=lambda *a, **kw: Raw())

    def test_rest_trade_before_requested_cursor_rejected(self):
        rows = [["0.00001", "1", 299, "b", "l", ""]] + self.rows
        with self.assertRaisesRegex(RuntimeError, "predates requested cursor"):
            compare_rest_bucket("DENTEUR", 300, self.expected,
                                opener=lambda *a, **kw: Response(make_page(rows)))

    def test_boolean_rest_numeric_fields_rejected(self):
        for field in (0, 1, 2):
            rows = [list(row) for row in self.rows]
            rows[0][field] = True
            with self.subTest(field=field), self.assertRaisesRegex(RuntimeError, "boolean"):
                compare_rest_bucket("DENTEUR", 300, self.expected,
                                    opener=lambda *a, **kw: Response(make_page(rows)))

    def test_overlong_rest_cursor_rejected(self):
        with self.assertRaisesRegex(RuntimeError, "nonadvancing"):
            compare_rest_bucket("DENTEUR", 300, self.expected,
                                opener=lambda *a, **kw: Response(make_page(self.rows, "9" * 30)))

    def test_zero_prefixed_rest_cursor_rejected(self):
        with self.assertRaisesRegex(RuntimeError, "nonadvancing"):
            compare_rest_bucket("DENTEUR", 300, self.expected,
                                opener=lambda *a, **kw: Response(make_page(self.rows, "0" + "1900000000000000000")))

    def test_rest_trade_at_exact_bucket_open_is_valid_correspondence(self):
        expected = [(300.0, 0.00001, 2, 0), (301.5, 0.000011, 3, 1)]
        rows = [list(row) for row in self.rows]
        rows[0][2] = 300.0
        r = compare_rest_bucket("DENTEUR", 300, expected,
                                opener=lambda *a, **kw: Response(make_page(rows)))
        self.assertEqual(r["status"], "independent_rest_bucket_correlated")
        self.assertEqual(r["real_labels"], 0)



    def test_two_page_cursor_contiguous_correspondence_not_completeness(self):
        pages = iter([
            make_page(self.rows[:2], "301500000001"),
            make_page(self.rows[2:], "601000000001"),
        ])
        r = compare_rest_bucket("DENTEUR", 300, self.expected,
                                opener=lambda *a, **kw: Response(next(pages)))
        self.assertEqual(r["status"], "independent_rest_bucket_correlated")
        self.assertEqual(r["pages"], 2)
        self.assertEqual(r["independent_complete_historical_intervals"], 0)
        self.assertEqual(r["real_labels"], 0)

    def test_two_page_cursor_leap_cannot_hide_unobserved_trades(self):
        pages = iter([
            make_page(self.rows[:2], "500000000000"),
            make_page(self.rows[2:], "601000000001"),
        ])
        with self.assertRaisesRegex(RuntimeError, "skips unobserved historical range"):
            compare_rest_bucket("DENTEUR", 300, self.expected,
                                opener=lambda *a, **kw: Response(next(pages)))

    def test_partial_bucket_cursor_leap_rejected_before_false_correspondence(self):
        pages = iter([
            make_page(self.rows[:1], "400000000000"),
            make_page(self.rows[1:], "601000000001"),
        ])
        with self.assertRaisesRegex(RuntimeError, "skips unobserved historical range"):
            compare_rest_bucket("DENTEUR", 300, self.expected,
                                opener=lambda *a, **kw: Response(next(pages)))

    def test_two_page_gap_cursor_contiguous_remains_candidate_only(self):
        after = ["0.000012", "1", 900, "b", "l", ""]
        pages = iter([
            make_page(self.rows[:2], "301500000001"),
            make_page([after], "900000000001"),
        ])
        r = compare_rest_bucket("DENTEUR", 300, self.expected,
                                opener=lambda *a, **kw: Response(next(pages)),
                                gap_buckets=1)
        self.assertEqual(r["status"], "independent_rest_gap_candidate_correlated_not_complete")
        self.assertEqual(r["candidate_empty_gap_buckets"], [600])
        self.assertEqual(r["no_trade_intervals_verified"], 0)
        self.assertEqual(r["real_labels"], 0)

    def test_two_page_gap_cursor_leap_cannot_certify_missing_interval(self):
        after = ["0.000012", "1", 900, "b", "l", ""]
        pages = iter([
            make_page(self.rows[:2], "800000000000"),
            make_page([after], "900000000001"),
        ])
        with self.assertRaisesRegex(RuntimeError, "skips unobserved historical range"):
            compare_rest_bucket("DENTEUR", 300, self.expected,
                                opener=lambda *a, **kw: Response(next(pages)),
                                gap_buckets=1)


class HistoricalGapCandidateTests(unittest.TestCase):
    """Synthetic source-page checks: a candidate empty gap is NOT source proof."""

    def setUp(self):
        self.expected = [(300.1, 0.00001, 2, 0), (301.5, 0.000011, 3, 1)]
        self.before = [["0.00001", "2", 300.1, "b", "l", ""],
                       ["0.000011", "3", 301.5, "s", "m", ""]]
        self.after = ["0.000012", "1", 900, "b", "l", ""]

    def audit(self, rows, *, gap_buckets=1):
        return compare_rest_bucket(
            "DENTEUR", 300, self.expected,
            opener=lambda *a, **kw: Response(make_page(rows)),
            gap_buckets=gap_buckets)

    def test_one_empty_gap_is_only_a_candidate(self):
        result = self.audit(self.before + [self.after])
        self.assertEqual(result["status"], "independent_rest_gap_candidate_correlated_not_complete")
        self.assertEqual(result["candidate_empty_gap_buckets"], [600])
        self.assertEqual(result["witness_end"], 900)
        self.assertEqual(result["no_trade_intervals_verified"], 0)
        self.assertEqual(result["independent_complete_historical_intervals"], 0)
        self.assertEqual(result["real_labels"], 0)
        self.assertFalse(result["independent_quarterly_completeness_verified"])

    def test_gap_trade_at_exact_open_abstains(self):
        rows = self.before + [["0.000012", "1", 600, "s", "l", ""], self.after]
        result = self.audit(rows)
        self.assertEqual(result["status"], "abstain_rest_gap_contains_trades")
        self.assertEqual(result["candidate_empty_gap_buckets"], [])
        self.assertEqual(result["no_trade_intervals_verified"], 0)

    def test_gap_trade_at_last_instant_abstains(self):
        rows = self.before + [["0.000012", "1", 899.999, "s", "l", ""], self.after]
        self.assertEqual(self.audit(rows)["status"], "abstain_rest_gap_contains_trades")

    def test_exact_after_gap_boundary_is_not_gap_trade(self):
        rows = self.before + [["0.000012", "1", 900, "s", "l", ""]]
        self.assertEqual(self.audit(rows)["candidate_empty_gap_buckets"], [600])

    def test_mismatch_in_observed_bucket_rejects_gap_candidate(self):
        rows = [["0.999", "2", 300.1, "b", "l", ""], self.before[1], self.after]
        result = self.audit(rows)
        self.assertEqual(result["status"], "abstain_rest_archive_disagreement")
        self.assertEqual(result["candidate_empty_gap_buckets"], [])

    def test_missing_historical_start_does_not_certify_empty_gap(self):
        result = self.audit([self.after])
        self.assertEqual(result["status"], "abstain_historical_range_unavailable")
        self.assertEqual(result["real_labels"], 0)

    def test_gap_count_strictly_bounded_and_not_boolean(self):
        for n in (-1, 2, 10, True, 0.5, None):
            with self.subTest(n=n), self.assertRaises(ValueError):
                self.audit(self.before + [self.after], gap_buckets=n)

    def test_default_mode_does_not_audit_gap(self):
        result = self.audit(self.before + [self.after], gap_buckets=0)
        self.assertEqual(result["status"], "independent_rest_bucket_correlated")
        self.assertEqual(result["candidate_empty_gap_buckets"], [])
        self.assertEqual(result["witness_end"], 600)

    def test_malformed_after_gap_witness_is_rejected(self):
        rows = self.before + [["0.000012", "1", 900, "bad", "l", ""]]
        with self.assertRaisesRegex(RuntimeError, "schema"):
            self.audit(rows)


    def test_distant_october_like_witness_is_not_a_may_gap_certificate(self):
        rows = self.before + [["0.000012", "1", 1791795122.2037888, "b", "l", ""]]
        r = self.audit(rows)
        self.assertEqual(r["status"], "abstain_rest_gap_following_witness_distant")
        self.assertEqual(r["candidate_empty_gap_buckets"], [])
        self.assertFalse(r["following_bucket_witness_near"])
        self.assertEqual(r["first_after_end_trade_timestamp"], 1791795122.2037888)
        self.assertEqual(r["real_labels"], 0)

    def test_following_bucket_end_boundary_is_too_distant(self):
        r = self.audit(self.before + [["0.000012", "1", 1200, "b", "l", ""]])
        self.assertEqual(r["status"], "abstain_rest_gap_following_witness_distant")
        self.assertEqual(r["candidate_empty_gap_buckets"], [])

    def test_last_instant_of_following_bucket_is_near_but_not_certified(self):
        r = self.audit(self.before + [["0.000012", "1", 1199.999, "b", "l", ""]])
        self.assertEqual(r["status"], "independent_rest_gap_candidate_correlated_not_complete")
        self.assertTrue(r["following_bucket_witness_near"])
        self.assertEqual(r["no_trade_intervals_verified"], 0)

    def test_first_after_end_timestamp_is_retained_in_cursor_trace(self):
        r = self.audit(self.before + [self.after])
        self.assertEqual(r["first_after_end_trade_timestamp"], 900)
        self.assertEqual(r["rest_cursor_trace"][0]["first_after_end_trade_timestamp"], 900)
        self.assertTrue(r["following_bucket_witness_near"])

    def test_near_witness_then_distant_trade_remains_near(self):
        rows = self.before + [self.after, ["0.000012", "1", 1791795122, "b", "l", ""]]
        r = self.audit(rows)
        self.assertEqual(r["status"], "independent_rest_gap_candidate_correlated_not_complete")
        self.assertEqual(r["first_after_end_trade_timestamp"], 900)
        self.assertEqual(r["real_labels"], 0)

    def test_gap_trade_takes_precedence_over_distant_after_end_witness(self):
        rows = self.before + [["0.000012", "1", 650, "s", "l", ""],
                              ["0.000012", "1", 1200, "b", "l", ""]]
        r = self.audit(rows)
        self.assertEqual(r["status"], "abstain_rest_gap_contains_trades")
        self.assertEqual(r["candidate_empty_gap_buckets"], [])

    def test_default_observed_bucket_mode_does_not_require_near_gap_witness(self):
        rows = self.before + [["0.000012", "1", 1791795122, "b", "l", ""]]
        r = self.audit(rows, gap_buckets=0)
        self.assertEqual(r["status"], "independent_rest_bucket_correlated")
        self.assertEqual(r["real_labels"], 0)

    def test_nonadvancing_cursor_rejected_even_if_gap_looks_empty(self):
        with self.assertRaisesRegex(RuntimeError, "nonadvancing"):
            compare_rest_bucket(
                "DENTEUR", 300, self.expected, gap_buckets=1,
                opener=lambda *a, **kw: Response(make_page(self.before + [self.after], "1")))

class RetainedHistoricalIntegrationTests(unittest.TestCase):
    def test_selects_bounded_bucket_from_retained_zip(self):
        import tempfile
        import zipfile
        from pathlib import Path
        from unittest.mock import patch
        from probe_historical_rest_interval import probe_retained
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / 'trades.zip'
            with zipfile.ZipFile(path, 'w') as z:
                z.writestr('trades/DENTEUR.csv', 'fixture')
            expected = [(300.1, 0.00001, 2, 0), (301.5, 0.000011, 3, 1)]
            rows = [["0.00001", "2", 300.1, "b", "l", ""], ["0.000011", "3", 301.5, "s", "m", ""], ["0.000011", "1", 601, "b", "m", ""]]
            with patch('probe_historical_rest_interval.parse_member', return_value=expected), \
                 patch('probe_historical_rest_interval.aggregate', return_value=({}, {300: expected})):
                r = probe_retained(path, opener=lambda *a, **kw: Response(make_page(rows)))
            self.assertEqual(r['status'], 'independent_rest_bucket_correlated')
            self.assertEqual(r['market'], 'DENTEUR')
            self.assertEqual(r['real_labels'], 0)

    def test_source_error_is_abstention_not_false_match(self):
        import tempfile
        import zipfile
        from pathlib import Path
        from unittest.mock import patch
        from probe_historical_rest_interval import probe_retained
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / 'trades.zip'
            with zipfile.ZipFile(path, 'w') as z:
                z.writestr('trades/DENTEUR.csv', 'fixture')
            expected = [(300.1, 0.00001, 2, 0)]
            with patch('probe_historical_rest_interval.parse_member', return_value=expected), \
                 patch('probe_historical_rest_interval.aggregate', return_value=({}, {300: expected})):
                def fail(*a, **kw): raise OSError('network unavailable')
                r = probe_retained(path, opener=fail)
            self.assertEqual(r['status'], 'abstain_rest_transport_or_source_error')
            self.assertEqual(r['real_labels'], 0)



class ThreeWayHistoricalCorroborationTests(unittest.TestCase):
    def setUp(self):
        import hashlib
        import tempfile
        import zipfile
        from pathlib import Path
        from inventory_kraken_archive import EXPECTED_SHA256
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.trade_path = Path(self.temp.name) / "trades.zip"
        self.ohlc_path = Path(self.temp.name) / "ohlc.zip"
        with zipfile.ZipFile(self.trade_path, "w") as z:
            z.writestr("trades/DENTEUR.csv", "fixture")
        self.candle = "300,0.00001,0.000011,0.00001,0.000011,5,2\n"
        self.meta = {
            "source_rows": 1, "retained_rows": 1,
            "retained_first_open": 300, "retained_last_open": 300,
            "source_gap_events": 0, "source_missing_intervals": 0,
            "source_longest_contiguous": 1,
        }
        self.source_sha = EXPECTED_SHA256
        self.write_ohlc()

    def write_ohlc(self):
        import hashlib
        import zipfile
        meta = dict(self.meta, retained_sha256=hashlib.sha256(self.candle.encode()).hexdigest())
        manifest = {"schema": 1, "source_archive_sha256": self.source_sha,
                    "independent_trade_completeness": False, "real_labels": 0,
                    "markets": {"DENTEUR_5.csv": meta}}
        with zipfile.ZipFile(self.ohlc_path, "w") as z:
            z.writestr("candles/DENTEUR_5.csv", self.candle)
            z.writestr("manifest.json", json.dumps(manifest))

    def run_probe(self, rows=None):
        from unittest.mock import patch
        from probe_historical_rest_interval import probe_retained
        expected = [(300.1, 0.00001, 2, 0), (301.5, 0.000011, 3, 1)]
        if rows is None:
            rows = [["0.00001", "2", 300.1, "b", "l", ""], ["0.000011", "3", 301.5, "s", "m", ""],
                    ["0.000011", "1", 601, "b", "m", ""]]
        with patch("probe_historical_rest_interval.parse_member", return_value=expected), \
             patch("probe_historical_rest_interval.aggregate", return_value=({}, {300: expected})):
            return probe_retained(self.trade_path, ohlc_artifact=self.ohlc_path,
                                  opener=lambda *a, **kw: Response(make_page(rows)))

    def test_real_three_way_correspondence_still_zero_labels(self):
        r = self.run_probe()
        self.assertEqual(r["status"], "independent_rest_trade_ohlc_correlated")
        self.assertTrue(r["three_way_candle_correspondence"])
        self.assertEqual(r["independent_complete_historical_intervals"], 0)
        self.assertEqual(r["real_labels"], 0)
        self.assertFalse(r["independent_quarterly_completeness_verified"])
        self.assertEqual(r["timestamp_semantics"], "observed_open_boundary_for_this_bucket_only")

    def test_ohlc_price_mismatch_abstains(self):
        self.candle = "300,0.00001,0.000019,0.00001,0.000019,5,2\n"
        self.write_ohlc()
        r = self.run_probe()
        self.assertEqual(r["status"], "abstain_rest_trade_ohlc_disagreement")
        self.assertFalse(r["three_way_candle_correspondence"])

    def test_ohlc_volume_mismatch_abstains(self):
        self.candle = "300,0.00001,0.000011,0.00001,0.000011,50,2\n"
        self.write_ohlc()
        self.assertEqual(self.run_probe()["status"], "abstain_rest_trade_ohlc_disagreement")

    def test_ohlc_bucket_missing_abstains(self):
        self.candle = "600,0.00001,0.000011,0.00001,0.000011,5,2\n"
        self.meta.update(retained_first_open=600, retained_last_open=600)
        self.write_ohlc()
        self.assertEqual(self.run_probe()["status"], "abstain_ohlc_bucket_missing")

    def test_manifest_source_sha_mismatch_rejected(self):
        self.source_sha = "0" * 64
        self.write_ohlc()
        with self.assertRaisesRegex(ValueError, "untrusted OHLC"):
            self.run_probe()

    def test_tampered_ohlc_member_sha_rejected(self):
        import zipfile
        self.write_ohlc()
        with zipfile.ZipFile(self.ohlc_path, "r") as z:
            m = json.loads(z.read("manifest.json"))
        m["markets"]["DENTEUR_5.csv"]["retained_sha256"] = "0" * 64
        with zipfile.ZipFile(self.ohlc_path, "w") as z:
            z.writestr("candles/DENTEUR_5.csv", self.candle)
            z.writestr("manifest.json", json.dumps(m))
        with self.assertRaisesRegex(ValueError, "SHA256 mismatch"):
            self.run_probe()

    def test_rest_trade_disagreement_never_promotes_to_three_way(self):
        rows = [["0.00002", "2", 300.1, "b", "l", ""], ["0.000011", "3", 301.5, "s", "m", ""],
                ["0.000011", "1", 601, "b", "m", ""]]
        r = self.run_probe(rows)
        self.assertEqual(r["status"], "abstain_rest_archive_disagreement")
        self.assertFalse(r["three_way_candle_correspondence"])

    def test_untrusted_rest_pair_identity_rejected(self):
        expected = [(300.1, 0.00001, 2, 0)]
        with self.assertRaisesRegex(RuntimeError, "invalid historical REST page"):
            compare_rest_bucket("DENTEUR", 300, expected,
                opener=lambda *a, **kw: Response(
                    {"error": [], "result": {"OTHERPAIR": [["0.00001", "2", 300.1],
                       ["0.00001", "1", 601]], "last": "9999999999999"}}))


if __name__ == "__main__":
    unittest.main()
