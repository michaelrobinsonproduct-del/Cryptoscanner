import datetime as dt
import unittest
from paper_pov.qualified_ohlc_outcomes import reconstruct, reconstruct_batch

UTC = dt.timezone.utc
START = dt.datetime(2026, 1, 1, tzinfo=UTC)


def bars(count=578, gap=None):
    return [
        {"open_at": (START + dt.timedelta(minutes=5 * i)).isoformat(),
         "open": 100.0, "high": 135.0 if i == 6 else 101.0,
         "low": 99.0, "close": 100.0}
        for i in range(count) if i != gap
    ]


def run(data, until=None):
    return reconstruct(
        {"prediction_id": "p", "pair": "XUSD",
         "status": "PAPER_WATCH", "as_of": (START + dt.timedelta(seconds=10)).isoformat()},
        data, observed_until=(until or START + dt.timedelta(hours=49)).isoformat(),
        source_sha256="a" * 64)


class OutcomeTests(unittest.TestCase):
    def test_four_closed_horizons_and_intrahorizon_peak(self):
        result = run(bars())
        self.assertEqual([x["status"] for x in result["labels"]],
                         ["MATURED_OBSERVED"] * 4)
        self.assertTrue(all(x["observed_30pct_hit"] for x in result["labels"]))
        self.assertEqual(result["labels"][0]["return_pct"], 0)
        self.assertFalse(result["source_authenticated"])
        self.assertFalse(result["labels"][0]["qualified_for_learning"])

    def test_missing_bar_abstains_affected_horizons(self):
        result = run(bars(gap=4))
        self.assertEqual([x["status"] for x in result["labels"]], ["ABSTAIN_GAP"] * 4)

    def test_immature_horizons_abstain(self):
        result = run(bars(), START + dt.timedelta(hours=2))
        self.assertEqual([x["status"] for x in result["labels"]],
                         ["MATURED_OBSERVED", "ABSTAIN_IMMATURE",
                          "ABSTAIN_IMMATURE", "ABSTAIN_IMMATURE"])

    def test_missing_entry_abstains(self):
        result = run(bars(gap=1))
        self.assertTrue(all(x["status"] == "ABSTAIN_ENTRY" for x in result["labels"]))

    def test_unordered_and_duplicate_bars_fail(self):
        data = bars(3)
        with self.assertRaises(ValueError):
            run(data + [data[-1]])
        with self.assertRaises(ValueError):
            run(data[::-1])

    def test_invalid_ohlc_rejected(self):
        data = bars(3)
        data[0]["high"] = 90
        with self.assertRaises(ValueError):
            run(data)


    def test_batch_keeps_missing_market_abstentions(self):
        predictions = [
            {'prediction_id': str(i), 'pair': pair, 'status': 'PAPER_WATCH',
             'as_of': (START + dt.timedelta(seconds=10)).isoformat()}
            for i, pair in enumerate(('XUSD', 'YUSD'))
        ]
        result = reconstruct_batch(predictions, {'XUSD': bars()},
                                   observed_until=(START + dt.timedelta(hours=49)).isoformat(),
                                   source_sha256='a' * 64)
        self.assertEqual(result['prediction_count'], 2)
        self.assertEqual(result['status_counts']['48h:MATURED_OBSERVED'], 1)
        self.assertEqual(result['status_counts']['48h:ABSTAIN_ENTRY'], 1)
        self.assertEqual(result['learning_qualified_count'], 0)
        with self.assertRaises(ValueError):
            reconstruct_batch(predictions + [predictions[0]], {'XUSD': bars()},
                              observed_until=(START + dt.timedelta(hours=49)).isoformat(),
                              source_sha256='a' * 64)

if __name__ == "__main__":
    unittest.main()
