"""Focused fixture regressions for read-only multi-horizon evidence adapter."""
import unittest
from .heldout_outcome_adapter import build_heldout_evidence


def row(key, horizon, **changes):
    data = dict(prediction_id=key, horizon_hours=horizon,
                entry_utc="2026-08-04T00:00:00Z",
                feature_asof_utc="2026-08-03T23:55:00Z",
                label_mature_utc="2026-08-06T00:00:00Z",
                coverage_complete=True, source_authenticated=True,
                liquidity_qualified=True, source_sha256="a"*64, hit=True)
    data.update(changes)
    return data


class OutcomeAdapterTests(unittest.TestCase):
    def evaluate(self, rows, base=None, challenger=None):
        return build_heldout_evidence(
            rows, base if base is not None else {"p": True},
            challenger if challenger is not None else {"p": False},
            training_end_utc="2026-07-29T00:00:00Z",
            holdout_start_utc="2026-08-01T00:00:00Z",
            evaluation_asof_utc="2026-08-07T00:00:00Z",
            baseline_version="baseline-1", challenger_version="shadow-2")

    def test_four_horizons_join_and_no_promotion(self):
        result = self.evaluate([row("p", h) for h in (1, 6, 24, 48)])
        self.assertEqual(result["outcome_coverage"], {"1": 1, "6": 1, "24": 1, "48": 1})
        self.assertEqual(result["cohort_size"], 1)
        self.assertEqual(result["status"], "NO_QUALIFIED_RULE")
        self.assertFalse(result["source_authentication_verified_by_adapter"])

    def test_gap_abstains_without_inventing_label(self):
        result = self.evaluate([row("p", 48), row("gap", 6, coverage_complete=False)])
        self.assertEqual(result["abstention_counts"], {"INCOMPLETE_SOURCE_COVERAGE": 1})

    def test_immature_outcome_abstains(self):
        result = self.evaluate([row("p", 48), row("later", 24, label_mature_utc="2026-08-08T00:00:00Z")])
        self.assertEqual(result["abstention_counts"], {"OUT_OF_WINDOW_OR_IMMATURE": 1})

    def test_duplicate_horizon_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.evaluate([row("p", 48), row("p", 48)])

    def test_missing_baseline_decision_rejected(self):
        with self.assertRaisesRegex(ValueError, "identical"):
            self.evaluate([row("p", 48)], base={})

    def test_unverified_source_abstains(self):
        result = self.evaluate([row("p", 48), row("u", 6, source_authenticated=False)])
        self.assertEqual(result["abstention_counts"], {"UNQUALIFIED_SOURCE_OR_LIQUIDITY": 1})

    def test_48h_gap_requires_decision_exclusion(self):
        result = self.evaluate([row("p", 48), row("gap", 48, coverage_complete=False)])
        self.assertEqual(result["cohort_size"], 1)
        self.assertEqual(result["abstention_counts"], {"INCOMPLETE_SOURCE_COVERAGE": 1})


if __name__ == "__main__":
    unittest.main()
