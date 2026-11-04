"""Deterministic fail-closed tests for isolated shadow evidence gate."""
import unittest
from .shadow_learning_evidence import evaluate_shadow_release


def cohort(n=40):
    rows = []
    for i in range(n):
        rows.append(dict(prediction_id=str(i), partition="held_out", horizon_hours=48,
                         source_authenticated=True, liquidity_qualified=True,
                         source_sha256="a"*64, hit=i % 2 == 0, watch=True,
                         entry_utc="2026-08-04T00:00:00Z", feature_asof_utc="2026-08-03T23:55:00Z",
                         label_mature_utc="2026-08-06T00:00:00Z", holdout_start_utc="2026-08-01T00:00:00Z"))
    return rows


class ShadowEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.a = dict(version="baseline-v1", observations=cohort())
        self.b = dict(version="challenger-v2", observations=cohort())

    def test_no_improvement_never_promotes(self):
        result = evaluate_shadow_release(self.a, self.b)
        self.assertEqual(result["status"], "NO_QUALIFIED_RULE")
        self.assertFalse(result["promotion_authorized"])
        self.assertEqual(result["cohort_size"], 40)

    def test_rejects_unmatched_universe(self):
        self.b["observations"].pop()
        with self.assertRaises(ValueError):
            evaluate_shadow_release(self.a, self.b)

    def test_rejects_unverified_source(self):
        self.b["observations"][0]["source_authenticated"] = False
        with self.assertRaises(ValueError):
            evaluate_shadow_release(self.a, self.b)

    def test_rejects_duplicate_identity(self):
        self.a["observations"][1]["prediction_id"] = "0"
        with self.assertRaises(ValueError):
            evaluate_shadow_release(self.a, self.b)

    def test_rejects_in_sample(self):
        self.a["observations"][0]["partition"] = "train"
        with self.assertRaises(ValueError):
            evaluate_shadow_release(self.a, self.b)

    def test_rejects_outcome_mismatch(self):
        self.b["observations"][0]["hit"] = False
        with self.assertRaises(ValueError):
            evaluate_shadow_release(self.a, self.b)

    def test_rejects_lookahead_feature(self):
        self.a["observations"][0]["feature_asof_utc"] = "2026-08-04T00:01:00Z"
        with self.assertRaises(ValueError):
            evaluate_shadow_release(self.a, self.b)

    def test_rejects_immature_48h_outcome(self):
        self.a["observations"][0]["label_mature_utc"] = "2026-08-05T23:59:00Z"
        with self.assertRaises(ValueError):
            evaluate_shadow_release(self.a, self.b)

    def test_rejects_provenance_mismatch(self):
        self.b["observations"][0]["entry_utc"] = "2026-08-04T00:05:00Z"
        with self.assertRaises(ValueError):
            evaluate_shadow_release(self.a, self.b)

    def test_rejects_non_utc_timestamps(self):
        self.a["observations"][0]["entry_utc"] = "2026-08-04T00:00:00"
        with self.assertRaises(ValueError):
            evaluate_shadow_release(self.a, self.b)

    def test_rejects_invalid_source_digest(self):
        self.a["observations"][0]["source_sha256"] = "z" * 64
        with self.assertRaises(ValueError):
            evaluate_shadow_release(self.a, self.b)

    def test_weak_sample_abstains(self):
        self.a["observations"] = cohort(10)
        self.b["observations"] = cohort(10)
        self.assertEqual(evaluate_shadow_release(self.a, self.b)["status"], "NO_QUALIFIED_RULE")


if __name__ == "__main__":
    unittest.main()
