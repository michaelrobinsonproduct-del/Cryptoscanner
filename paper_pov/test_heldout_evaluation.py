import datetime as dt
import hashlib
import unittest

from paper_pov import ledger
from paper_pov.heldout_evaluation import evaluate


def fixture(n=6, missing=False):
    state = ledger.empty()
    base = dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc)
    for i in range(n):
        at = (base + dt.timedelta(hours=72 * i)).isoformat()
        run_id = hashlib.sha256(("run" + str(i)).encode()).hexdigest()
        state["runs"].append({
            "id": run_id, "as_of": at, "source_sha": "a" * 40,
            "report_sha256": "b" * 64, "watch_count": 3,
            "observation_count": 3,
        })
        for j in range(3):
            pair = "PAIR" + str(j)
            pid = hashlib.sha256(("paper-v1|" + at + "|" + pair).encode()).hexdigest()
            state["predictions"].append({
                "prediction_id": pid, "run_id": run_id, "as_of": at,
                "pair": pair, "price": 1.0, "rank": j + 1,
                "baseline_score": float(3 - j),
                "challenger_score": float(j + 1),
            })
            state["observations"].append({
                "run_id": run_id, "at": at, "pair": pair, "price": 1.0,
            })
            if not (missing and i == n - 1 and j == 2):
                state["outcomes"].append({
                    "prediction_id": pid, "horizon_hours": 48,
                    "status": "MATURED_OBSERVED",
                    "target_at": (dt.datetime.fromisoformat(at) +
                                  dt.timedelta(hours=48)).isoformat(),
                    "observed_at": (dt.datetime.fromisoformat(at) +
                                    dt.timedelta(hours=48)).isoformat(),
                    "return_pct": 0.0, "observed_peak_pct": 31.0 if j == 2 else 0.0,
                    "observed_30pct_hit": j == 2,
                })
    state["generation"] = n
    return ledger.seal(state)


class HeldoutEvaluationTests(unittest.TestCase):
    def test_identical_cohort_and_purged_holdout(self):
        report = evaluate(fixture(), top_k=1, min_train=2, min_test=2)
        self.assertEqual(report["train_runs"], 4)
        self.assertEqual(report["test_runs"], 2)
        self.assertEqual(report["baseline_hits"], 0)
        self.assertEqual(report["challenger_hits"], 2)
        self.assertEqual(report["held_out_lift"], 1.0)
        self.assertEqual(report["status"], "NO_QUALIFIED_RULE")
        self.assertFalse(report["promotion_authorized"])

    def test_incomplete_scan_abstains_whole_cohort(self):
        report = evaluate(fixture(missing=True), top_k=1, min_train=2, min_test=2)
        self.assertEqual(report["eligible_complete_runs"], 5)
        self.assertGreater(report["abstained_or_incomplete_predictions"], 0)

    def test_insufficient_data_does_not_invent_lift(self):
        report = evaluate(fixture(2), top_k=1, min_train=2, min_test=2)
        self.assertIsNone(report["held_out_lift"])
        self.assertEqual(report["status"], "NO_QUALIFIED_RULE")

    def test_bad_checksum_rejected(self):
        state = fixture()
        state["predictions"][0]["baseline_score"] = 999
        with self.assertRaises(ValueError):
            evaluate(state, top_k=1, min_train=2, min_test=2)

    def test_bad_horizon_rejected(self):
        with self.assertRaises(ValueError):
            evaluate(fixture(), horizon=24)


if __name__ == "__main__":
    unittest.main()
