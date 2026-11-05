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
        self.a = dict(version="baseline-v1", training_end_utc="2026-07-29T00:00:00Z", evaluation_asof_utc="2026-08-07T00:00:00Z", observations=cohort())
        self.b = dict(version="challenger-v2", training_end_utc="2026-07-29T00:00:00Z", evaluation_asof_utc="2026-08-07T00:00:00Z", observations=cohort())

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

    def test_self_attested_rows_cannot_qualify(self):
        # A favorable fixture must not be interpreted as authenticated lift.
        for i, row in enumerate(self.b["observations"]):
            row["watch"] = (i % 2 == 0)
        result = evaluate_shadow_release(self.a, self.b, minimum_holdout=10)
        self.assertEqual(result["status"], "NO_QUALIFIED_RULE")
        self.assertFalse(result["source_receipt_qualified"])

    def test_forged_matching_receipt_never_qualifies_favorable_shadow(self):
        receipt = dict(verification="independently_authenticated",
                       artifact_sha256="a" * 64, verifier_commit="b" * 40)
        self.a["source_receipt"] = receipt
        self.b["source_receipt"] = dict(receipt)
        for i, row in enumerate(self.b["observations"]):
            row["watch"] = i % 2 == 0
        result = evaluate_shadow_release(self.a, self.b, minimum_holdout=10)
        self.assertGreater(result["precision_delta"], 0)
        self.assertFalse(result["source_receipt_qualified"])
        self.assertEqual(result["status"], "NO_QUALIFIED_RULE")
        self.assertFalse(result["promotion_authorized"])

    def test_receipt_must_match_both_versions(self):
        receipt = dict(verification="independently_authenticated", artifact_sha256="a"*64,
                       verifier_commit="b"*40)
        self.a["source_receipt"] = receipt
        self.b["source_receipt"] = dict(receipt, artifact_sha256="c"*64)
        result = evaluate_shadow_release(self.a, self.b, minimum_holdout=10)
        self.assertFalse(result["source_receipt_qualified"])

    def test_training_purge_rejects_overlap(self):
        self.a["training_end_utc"] = "2026-07-31T00:01:00Z"
        self.b["training_end_utc"] = "2026-07-31T00:01:00Z"
        with self.assertRaisesRegex(ValueError, "purge"):
            evaluate_shadow_release(self.a, self.b)

    def test_training_boundary_must_match(self):
        self.b["training_end_utc"] = "2026-07-28T00:00:00Z"
        with self.assertRaisesRegex(ValueError, "boundary"):
            evaluate_shadow_release(self.a, self.b)

    def test_missed_mover_and_false_positive_accounting(self):
        for i, row in enumerate(self.b["observations"]):
            row["watch"] = i % 2 == 0
        result = evaluate_shadow_release(self.a, self.b, minimum_holdout=10)
        self.assertEqual(result["baseline"]["false_positives"], 20)
        self.assertEqual(result["challenger"]["false_positives"], 0)
        self.assertEqual(result["challenger"]["recall"], 1.0)
        self.assertEqual(result["challenger"]["coverage"], 0.5)
        self.assertEqual(result["status"], "NO_QUALIFIED_RULE")

    def test_rejects_future_outcome_not_mature_at_evaluation(self):
        self.a["evaluation_asof_utc"] = "2026-08-05T00:00:00Z"
        self.b["evaluation_asof_utc"] = "2026-08-05T00:00:00Z"
        with self.assertRaisesRegex(ValueError, "immature"):
            evaluate_shadow_release(self.a, self.b)

    def test_rejects_different_evaluation_cutoffs(self):
        self.b["evaluation_asof_utc"] = "2026-08-08T00:00:00Z"
        with self.assertRaisesRegex(ValueError, "cutoff mismatch"):
            evaluate_shadow_release(self.a, self.b)

    def test_rejects_mixed_holdout_boundaries(self):
        self.a["observations"][0]["holdout_start_utc"] = "2026-08-02T00:00:00Z"
        with self.assertRaisesRegex(ValueError, "Mixed held-out"):
            evaluate_shadow_release(self.a, self.b)

    def test_rejects_missing_evaluation_cutoff(self):
        self.a.pop("evaluation_asof_utc")
        self.b.pop("evaluation_asof_utc")
        with self.assertRaises(ValueError):
            evaluate_shadow_release(self.a, self.b)

    def test_weak_sample_abstains(self):
        self.a["observations"] = cohort(10)
        self.b["observations"] = cohort(10)
        self.assertEqual(evaluate_shadow_release(self.a, self.b)["status"], "NO_QUALIFIED_RULE")


if __name__ == "__main__":
    unittest.main()
