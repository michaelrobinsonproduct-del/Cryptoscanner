import unittest
from diagnose_real_trade_candle_overlap import diagnose


class DiagnosticTests(unittest.TestCase):
    def test_exact_candidate_is_not_completeness(self):
        r = diagnose([(300, 100, 101, 100, 101, 5, 2)],
                     [(300, 100, 2, 0), (301, 101, 3, 1)])
        self.assertEqual(r["exact_candidate_matches"], 1)
        self.assertEqual(r["verified_complete_intervals"], 0)
        self.assertEqual(r["real_labels"], 0)

    def test_missing_source_bucket_is_counted(self):
        r = diagnose([(300, 100, 100, 100, 100, 2, 1)],
                     [(600, 100, 2, 0)])
        self.assertEqual(r["mismatch_counts"]["trade_bucket_missing_from_ohlc"], 1)
        self.assertEqual(r["ohlc_intervals_without_trade_bucket"], 1)

    def test_volume_mismatch_is_not_accepted(self):
        r = diagnose([(300, 100, 100, 100, 100, 3, 1)],
                     [(300, 100, 2, 0)])
        self.assertEqual(r["mismatch_counts"]["aggregation_mismatch"], 1)
        self.assertEqual(r["exact_candidate_matches"], 0)

    def test_duplicate_ohlc_timestamp_fails(self):
        with self.assertRaises(ValueError):
            diagnose([(300, 100, 100, 100, 100, 2, 1)] * 2,
                     [(300, 100, 2, 0)])

    def test_empty_input_never_produces_labels(self):
        self.assertEqual(diagnose([], [])["real_labels"], 0)


if __name__ == "__main__":
    unittest.main()
