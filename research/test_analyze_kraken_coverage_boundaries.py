import unittest
from analyze_kraken_coverage_boundaries import coverage


def candle(ts):
    return (ts, 100, 100, 100, 100, 2, 1)


def trade(ts):
    return (ts, 100, 2, 0)


class CoverageTests(unittest.TestCase):
    def test_period_partition_and_gap(self):
        r = coverage([candle(x) for x in (0, 300, 600, 900, 1200, 1500)],
                     [trade(600), trade(1200)])
        self.assertEqual(r["ohlc_before_trade_period"], 2)
        self.assertEqual(r["ohlc_after_trade_period"], 1)
        self.assertEqual(r["ohlc_within_trade_period_without_trade_bucket"], 1)
        self.assertEqual(r["ohlc_unmatched_reconciled"], 4)
        self.assertEqual(r["real_labels"], 0)

    def test_contiguous_candidate_run_is_not_verified(self):
        r = coverage([candle(x) for x in (300, 600, 900)],
                     [trade(300), trade(600), trade(900)])
        self.assertEqual(r["longest_contiguous_matching_5m_buckets"], 3)
        self.assertFalse(r["independent_completeness_verified"])
        self.assertEqual(r["candidate_horizon_window_counts"]["1"], 0)

    def test_missing_ohlc_trade_bucket(self):
        r = coverage([candle(300)], [trade(300), trade(600)])
        self.assertEqual(r["trade_buckets_without_ohlc"], 1)

    def test_duplicate_ohlc_fails(self):
        with self.assertRaises(ValueError):
            coverage([candle(300), candle(300)], [trade(300)])

    def test_unsorted_trades_fail(self):
        with self.assertRaises(ValueError):
            coverage([candle(300), candle(600)], [trade(600), trade(300)])

    def test_empty_source_abstains(self):
        self.assertEqual(coverage([], [trade(300)])["real_labels"], 0)


if __name__ == "__main__":
    unittest.main()
