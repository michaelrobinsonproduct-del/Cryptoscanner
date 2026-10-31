import unittest

from audit_point_in_time_candidates import audit_point_in_time_candidates


def candle(t, *, close=100, high=None, low=None, volume=2):
    return (t, 100, max(100, close) if high is None else high,
            min(100, close) if low is None else low, close, volume, 1)


def series(n=16, *, future_high=135, entry_close=100):
    rows = [candle(i * 300) for i in range(n)]
    if n > 3:
        rows[3] = candle(900, close=entry_close)
    if n > 15:
        rows[15] = candle(4500, high=future_high)
    return rows


class PointInTimeCandidateTests(unittest.TestCase):
    def test_closed_features_and_future_30_peak_separated(self):
        rows = series()
        r = audit_point_in_time_candidates(rows, {x[0] for x in rows})
        h = r["horizons"]["1"]
        self.assertEqual(h["descriptive_complete_future_windows"], 1)
        self.assertEqual(h["descriptive_peak_30"], 1)
        self.assertEqual(h["descriptive_peak_30_with_prior_return_below_10pct"], 1)
        e = h["examples"][0]
        self.assertEqual(e["entry_open_utc"], 900)
        self.assertEqual(e["decision_as_of_utc"], 1200)
        self.assertEqual(e["prior_15m_return"], 0)
        self.assertEqual(e["prior_15m_quote_volume_proxy"], 600)
        self.assertEqual(e["prior_15m_high_low_range"], 0)
        self.assertEqual(r["real_labels"], 0)
        self.assertFalse(r["features_use_future_candles"])
        self.assertFalse(r["executable_fill_verified"])

    def test_future_high_cannot_modify_prior_features(self):
        a = audit_point_in_time_candidates(series(future_high=135),
                                           {i * 300 for i in range(16)})
        b = audit_point_in_time_candidates(series(future_high=180),
                                           {i * 300 for i in range(16)})
        x, y = a["horizons"]["1"]["examples"][0], b["horizons"]["1"]["examples"][0]
        for key in ("prior_15m_return", "prior_15m_quote_volume_proxy",
                    "prior_15m_high_low_range", "decision_as_of_utc"):
            self.assertEqual(x[key], y[key])
        self.assertNotEqual(x["future_descriptive_peak_return"],
                            y["future_descriptive_peak_return"])

    def test_prior_surge_excluded_from_early_30_count(self):
        rows = series(future_high=160, entry_close=120)
        h = audit_point_in_time_candidates(rows, {x[0] for x in rows})["horizons"]["1"]
        self.assertEqual(h["descriptive_peak_30"], 1)
        self.assertEqual(h["descriptive_peak_30_with_prior_return_below_10pct"], 0)

    def test_missing_prior_exact_abstains_from_feature(self):
        rows = series()
        exact = {x[0] for x in rows} - {0}
        r = audit_point_in_time_candidates(rows, exact)
        self.assertEqual(r["excluded_missing_exact_15m_history"], 3)
        self.assertEqual(r["horizons"]["1"]["descriptive_complete_future_windows"], 0)

    def test_missing_future_exact_is_not_negative(self):
        rows = series()
        exact = {x[0] for x in rows} - {3000}
        h = audit_point_in_time_candidates(rows, exact)["horizons"]["1"]
        self.assertEqual(h["descriptive_complete_future_windows"], 0)
        self.assertGreater(h["excluded_missing_exact_future"], 0)
        self.assertEqual(h["descriptive_peak_30"], 0)

    def test_retained_end_unknown_not_negative(self):
        rows = series(4)
        h = audit_point_in_time_candidates(rows, {x[0] for x in rows})["horizons"]["1"]
        self.assertEqual(h["feature_ready_entries"], 1)
        self.assertEqual(h["excluded_outside_retained_end"], 1)
        self.assertEqual(h["descriptive_complete_future_windows"], 0)

    def test_no_exact_entries_no_features_no_labels(self):
        r = audit_point_in_time_candidates(series(), set())
        self.assertEqual(r["feature_ready_entries"], 0)
        self.assertEqual(r["horizons"]["48"]["descriptive_complete_future_windows"], 0)
        self.assertEqual(r["real_labels"], 0)
        self.assertEqual(r["held_out_evaluation"], "not_authorized")

    def test_invalid_source_row_rejected(self):
        for rows in ([candle(0), candle(0)],
                     [candle(300), candle(0)],
                     [candle(0, volume=-1)],
                     [(0, 100, float("nan"), 100, 100, 2, 1)]):
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                audit_point_in_time_candidates(rows, set())

    def test_48h_boundary_with_prior_history(self):
        rows = [candle(i * 300) for i in range(580)]
        rows[-1] = candle(579 * 300, high=135)
        h = audit_point_in_time_candidates(rows, {x[0] for x in rows})["horizons"]["48"]
        self.assertEqual(h["descriptive_complete_future_windows"], 1)
        self.assertEqual(h["descriptive_peak_30"], 1)
        self.assertEqual(h["examples"][0]["decision_as_of_utc"], 1200)
        self.assertEqual(h["real_labels"], 0)

    def test_report_bounded_and_never_authorizes_model(self):
        rows = [candle(i * 300) for i in range(1000)]
        r = audit_point_in_time_candidates(rows, {x[0] for x in rows})
        self.assertTrue(all(len(x["examples"]) <= 3 for x in r["horizons"].values()))
        self.assertTrue(all(x["real_labels"] == 0 for x in r["horizons"].values()))
        self.assertTrue(r["quote_volume_is_proxy_not_executed_notional"])
        self.assertEqual(r["held_out_evaluation"], "not_authorized")
        self.assertFalse(r["production_modified"])


if __name__ == "__main__":
    unittest.main()
