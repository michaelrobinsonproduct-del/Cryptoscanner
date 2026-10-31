import unittest
from assess_trade_interval_coverage import assess


def candles(*opens):
    return [(t, 100, 101, 99, 100, 1, 1) for t in opens]


def buckets(*opens):
    return {t: [(t + 1, 100, 1, 0)] for t in opens}


class CoverageCensusTests(unittest.TestCase):
    def test_exact_contiguous_hour_still_not_predictive(self):
        ts = [300 + 300*i for i in range(14)]
        r = assess(candles(*ts), buckets(*ts), set(ts))
        self.assertEqual(r['overlap']['exact_candidate_intervals'], 14)
        self.assertEqual(r['horizons']['1']['complete_descriptive_windows'], 2)
        self.assertEqual(r['horizons']['1']['excluded_beyond_ohlc_tail'], 12)
        self.assertEqual(r['verified_predictive_labels'], 0)
        self.assertFalse(r['independent_trade_source_completeness_verified'])

    def test_gap_in_both_sources_is_unknown_not_no_trade(self):
        r = assess(candles(300, 900), buckets(300, 900), {300, 900})
        self.assertEqual(r['overlap']['neither_source_observed_intervals'], 1)
        self.assertEqual(r['no_trade_inference'], 'not_authorized_for_unobserved_intervals')

    def test_partition_ohlc_only_trade_only_and_mismatch(self):
        r = assess(candles(300, 600, 900, 1200), buckets(300, 600, 1200, 1500), {300, 1200})
        self.assertEqual(r['overlap'], {
            'intervals_in_shared_observed_span': 4,
            'exact_candidate_intervals': 2,
            'both_present_but_nonmatching': 1,
            'ohlc_only_intervals': 1,
            'trade_only_intervals': 0,
            'neither_source_observed_intervals': 0})

    def test_trade_only_interval_in_overlap(self):
        r = assess(candles(300, 900), buckets(300, 600, 900), {300, 900})
        self.assertEqual(r['overlap']['trade_only_intervals'], 1)

    def test_nonoverlapping_period_is_not_false_no_trade(self):
        r = assess(candles(300, 600), buckets(900, 1200), set())
        self.assertEqual(r['overlap']['intervals_in_shared_observed_span'], 0)
        self.assertEqual(r['horizons']['48']['candidate_entries'], 0)

    def test_ohlc_tail_priority(self):
        r = assess(candles(300, 600), buckets(300, 600, 900), {300})
        self.assertEqual(r['horizons']['1']['excluded_beyond_ohlc_tail'], 1)

    def test_trade_tail_exclusion_is_separate(self):
        ts = [300 + 300*i for i in range(14)]
        r = assess(candles(*ts), buckets(*ts[:2]), {300, 600})
        self.assertEqual(r['horizons']['1']['excluded_beyond_trade_tail'], 2)

    def test_missing_ohlc_future_not_counted_negative(self):
        ts = [300 + 300*i for i in range(14)]
        r = assess(candles(*sorted(set(ts)-{900})), buckets(*ts), {300, 600})
        self.assertEqual(r['horizons']['1']['excluded_missing_ohlc_future'], 2)

    def test_missing_trade_future_not_counted_negative(self):
        ts = [300 + 300*i for i in range(14)]
        r = assess(candles(*ts), buckets(*sorted(set(ts)-{900})), {300, 600})
        self.assertEqual(r['horizons']['1']['excluded_missing_trade_future'], 2)

    def test_nonmatching_future_not_counted_negative(self):
        ts = [300 + 300*i for i in range(14)]
        r = assess(candles(*ts), buckets(*ts), set(ts)-{900})
        self.assertEqual(r['horizons']['1']['excluded_nonmatching_future'], 2)

    def test_exact_not_in_both_sources_rejected(self):
        with self.assertRaisesRegex(ValueError, 'without both sources'):
            assess(candles(300), buckets(600), {300})

    def test_duplicate_or_reverse_ohlc_rejected(self):
        for ts in ((300,300), (600,300)):
            with self.subTest(ts=ts), self.assertRaisesRegex(ValueError, 'chronology'):
                assess(candles(*ts), buckets(300), set())

    def test_bad_trade_bucket_rejected(self):
        for bad in ({300: []}, {301: [(301, 1, 1, 0)]}, {True: [(1,1,1,0)]}):
            with self.subTest(bad=bad), self.assertRaisesRegex(ValueError, 'trade bucket'):
                assess(candles(300), bad, set())

    def test_nonfinite_and_fractional_timestamp_rejected(self):
        for ts in (float('nan'), float('inf'), 300.5, True, -300):
            with self.subTest(ts=ts), self.assertRaisesRegex(ValueError, 'chronology'):
                assess(candles(ts), buckets(300), set())

    def test_no_trade_evidence_never_authorizes_labels(self):
        r = assess(candles(300), buckets(300), {300})
        for horizon in r['horizons'].values():
            self.assertEqual(horizon['verified_predictive_labels'], 0)
        self.assertEqual(r['held_out_evaluation'], 'not_authorized')
        self.assertFalse(r['production_modified'])


if __name__ == '__main__':
    unittest.main()
