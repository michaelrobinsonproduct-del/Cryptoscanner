import unittest
from audit_trade_candidate_windows import audit_candidate_windows


def candle(t, *, close=100, high=100, low=100):
    return (t, 100, high, low, close, 2, 1)


class CandidateAuditTests(unittest.TestCase):
    def test_full_hour_30_percent_peak_is_descriptive_only(self):
        rows = [candle(i*300, high=135 if i == 12 else 100) for i in range(13)]
        r = audit_candidate_windows(rows, {i*300 for i in range(13)})
        h = r["horizons"]["1"]
        self.assertEqual(h["candidate_full_future_windows"], 1)
        self.assertEqual(h["descriptive_peak_30"], 1)
        self.assertEqual(h["excluded_beyond_retained_end"], 12)
        self.assertEqual(r["real_labels"], 0)
        self.assertFalse(r["executable_fill_verified"])

    def test_entry_high_is_not_future_return(self):
        rows = [candle(i*300, high=140 if i == 0 else 100) for i in range(13)]
        h = audit_candidate_windows(rows, {i*300 for i in range(13)})["horizons"]["1"]
        self.assertEqual(h["descriptive_peak_30"], 0)

    def test_future_high_uses_entry_close(self):
        rows = [candle(i*300, close=90 if i == 0 else 100,
                       high=120 if i == 12 else 100,
                       low=80 if i == 0 else 100) for i in range(13)]
        h = audit_candidate_windows(rows, {i*300 for i in range(13)})["horizons"]["1"]
        self.assertEqual(h["descriptive_peak_30"], 1)

    def test_missing_exact_candle_is_gap_not_negative(self):
        rows = [candle(i*300) for i in range(13)]
        exact = {i*300 for i in range(13)} - {600}
        h = audit_candidate_windows(rows, exact)["horizons"]["1"]
        self.assertEqual(h["candidate_full_future_windows"], 0)
        self.assertEqual(h["excluded_missing_exact_future"], 1)
        self.assertEqual(h["descriptive_peak_30"], 0)

    def test_missing_source_candle_is_gap(self):
        rows = [candle(i*300) for i in range(13) if i != 2]
        h = audit_candidate_windows(rows, {r[0] for r in rows})["horizons"]["1"]
        self.assertEqual(h["excluded_missing_exact_future"], 1)

    def test_beyond_retained_end_is_unknown_not_negative(self):
        rows = [candle(i*300) for i in range(12)]
        h = audit_candidate_windows(rows, {r[0] for r in rows})["horizons"]["1"]
        self.assertEqual(h["excluded_beyond_retained_end"], 12)
        self.assertEqual(h["candidate_full_future_windows"], 0)

    def test_duplicate_and_out_of_order_source_abstain(self):
        row = candle(0)
        for rows in ([row, row], [candle(300), row]):
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                audit_candidate_windows(rows, {0})

    def test_nonfinite_and_bad_alignment_abstain(self):
        for bad in (float("nan"), float("inf"), 301, -300, True):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                audit_candidate_windows([(bad, 100, 100, 100, 100, 1, 1)], set())

    def test_unmatched_timestamp_abstains(self):
        with self.assertRaises(ValueError):
            audit_candidate_windows([candle(0)], {300})

    def test_empty_exact_cannot_create_labels(self):
        r = audit_candidate_windows([candle(0)], set())
        self.assertEqual(r["horizons"]["1"]["candidate_entries"], 0)
        self.assertEqual(r["real_labels"], 0)

    def test_48h_end_boundary_included(self):
        rows = [candle(i*300, high=135 if i == 576 else 100) for i in range(577)]
        h = audit_candidate_windows(rows, {r[0] for r in rows})["horizons"]["48"]
        self.assertEqual(h["candidate_full_future_windows"], 1)
        self.assertEqual(h["descriptive_peak_30"], 1)

    def test_invalid_ohlc_price_or_count_abstains(self):
        for row in [(0, 100, 99, 100, 100, 1, 1),
                    (0, 100, 100, 100, 100, -1, 1),
                    (0, 100, 100, 100, 100, 1, 1.5)]:
            with self.subTest(row=row), self.assertRaises(ValueError):
                audit_candidate_windows([row], {0})


    def test_officially_documented_interior_no_trade_gaps_are_counted(self):
        rows = [candle(0), candle(900), candle(1200)]
        r = audit_candidate_windows(rows, {0, 900, 1200})
        self.assertEqual(r["ohlc_interior_gap_events"], 1)
        self.assertEqual(r["ohlc_interior_missing_intervals"], 2)
        self.assertIn("support.kraken.com/articles/360047124832", r["ohlc_gap_documentation_url"])
        self.assertFalse(r["ohlc_gap_semantics_authorize_labels"])
        self.assertEqual(r["real_labels"], 0)

    def test_consecutive_ohlc_has_no_interior_missing_intervals(self):
        r = audit_candidate_windows([candle(i * 300) for i in range(5)], {0})
        self.assertEqual(r["ohlc_interior_gap_events"], 0)
        self.assertEqual(r["ohlc_interior_missing_intervals"], 0)

    def test_retained_edges_remain_unknown(self):
        r = audit_candidate_windows([candle(3000), candle(3300)], {3000})
        self.assertEqual(r["ohlc_interior_missing_intervals"], 0)
        self.assertEqual(r["outside_retained_slice_semantics"], "unknown")

    def test_no_trade_source_gaps_never_override_missing_trade_evidence(self):
        rows = [candle(i * 300) for i in range(13) if i != 2]
        r = audit_candidate_windows(rows, {t[0] for t in rows})
        self.assertEqual(r["ohlc_interior_missing_intervals"], 1)
        self.assertEqual(r["horizons"]["1"]["candidate_full_future_windows"], 0)
        self.assertGreater(r["horizons"]["1"]["excluded_missing_exact_future"], 0)
        self.assertFalse(r["ohlc_gap_semantics_authorize_labels"])

    def test_multiple_gaps_count_intervals_not_only_events(self):
        rows = [candle(0), candle(900), candle(2100), candle(2400)]
        r = audit_candidate_windows(rows, {0, 900, 2100, 2400})
        self.assertEqual(r["ohlc_interior_gap_events"], 2)
        self.assertEqual(r["ohlc_interior_missing_intervals"], 5)

    def test_single_retained_row_cannot_infer_outside_history(self):
        r = audit_candidate_windows([candle(3600)], {3600})
        self.assertEqual(r["ohlc_interior_gap_events"], 0)
        self.assertEqual(r["ohlc_interior_missing_intervals"], 0)
        self.assertEqual(r["horizons"]["48"]["excluded_beyond_retained_end"], 1)


    def test_zero_trade_or_zero_volume_candle_cannot_be_a_candidate(self):
        for row in ((0, 100, 100, 100, 100, 0, 1),
                    (0, 100, 100, 100, 100, 1, 0)):
            with self.subTest(row=row), self.assertRaisesRegex(ValueError, "values"):
                audit_candidate_windows([row], {0})

if __name__ == "__main__":
    unittest.main()
