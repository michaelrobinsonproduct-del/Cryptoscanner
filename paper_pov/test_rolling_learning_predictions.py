import copy
import datetime as dt
import unittest
from paper_pov.rolling_learning_predictions import merge

NOW = dt.datetime(2026, 11, 17, tzinfo=dt.timezone.utc)

def ledger(at, gen, rows):
    return {"generation": gen, "sha256": "a"*64, "runs": [{"as_of": at.isoformat()}],
            "predictions": rows}

def pred(at, key):
    return {"as_of": at.isoformat(), "prediction_id": key, "pair": "ABCUSD",
            "price": 1, "baseline_score": 60, "run_id": key}

class RollingLearningPredictionsTests(unittest.TestCase):
    def test_preserve_predictions_beyond_live_50h(self):
        old = pred(NOW-dt.timedelta(days=6), "old")
        recent = pred(NOW-dt.timedelta(hours=1), "recent")
        prior = merge(ledger(NOW-dt.timedelta(hours=1), 1, [old, recent]))
        result = merge(ledger(NOW, 2, [recent]), prior)
        self.assertEqual([p["prediction_id"] for p in result["predictions"]], ["old", "recent"])
        self.assertFalse(result["production_applied"])

    def test_reject_changed_immutable_prediction(self):
        row = pred(NOW-dt.timedelta(hours=1), "p")
        old = merge(ledger(NOW, 1, [row]))
        changed = dict(row, price=2)
        with self.assertRaisesRegex(ValueError, "Immutable"):
            merge(ledger(NOW, 2, [changed]), old)

    def test_prior_checksum_and_rollback(self):
        old = merge(ledger(NOW, 2, [pred(NOW, "p")]))
        tampered = copy.deepcopy(old)
        tampered["predictions"][0]["price"] = 5
        with self.assertRaisesRegex(ValueError, "checksum"):
            merge(ledger(NOW, 3, []), tampered)
        with self.assertRaisesRegex(ValueError, "generation rollback"):
            merge(ledger(NOW, 1, []), old)

    def test_retention_deliberately_bounded(self):
        old = pred(NOW-dt.timedelta(days=15), "past")
        self.assertEqual(merge(ledger(NOW, 1, [old]))["predictions"], [])

if __name__ == "__main__":
    unittest.main()
