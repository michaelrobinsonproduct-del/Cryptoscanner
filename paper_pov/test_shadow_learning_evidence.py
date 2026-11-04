"""Deterministic fail-closed tests for isolated shadow evidence gate."""
import unittest
from .shadow_learning_evidence import evaluate_shadow_release


def cohort(n=40):
    rows = []
    for i in range(n):
        rows.append(dict(prediction_id=str(i), partition="held_out", horizon_hours=48,
                         source_authenticated=True, liquidity_qualified=True,
                         source_sha256="a"*64, hit=i % 2 == 0, watch=True))
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

    def test_weak_sample_abstains(self):
        self.a["observations"] = cohort(10)
        self.b["observations"] = cohort(10)
        self.assertEqual(evaluate_shadow_release(self.a, self.b)["status"], "NO_QUALIFIED_RULE")


if __name__ == "__main__":
    unittest.main()
