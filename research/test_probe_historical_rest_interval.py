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


def make_page(rows, cursor="9999999999999", *, error=None):
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
        cursor = ["9999999999999", "10000000000000", "10000000000001", "10000000000002"]
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
            rows = [["0.00001", "2", 300.1], ["0.000011", "3", 301.5], ["0.000011", "1", 601]]
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


if __name__ == "__main__":
    unittest.main()
