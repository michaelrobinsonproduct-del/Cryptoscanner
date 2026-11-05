"""Focused fixture regressions for read-only multi-horizon evidence adapter."""
import json
import tempfile
import unittest
from pathlib import Path
from .heldout_outcome_adapter import build_heldout_evidence, main, project_learning_handoff


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
        # Existing fixture p has a complete four-horizon source history.
        seen = {(r["prediction_id"], r["horizon_hours"]) for r in rows}
        if ("p", 48) in seen:
            rows = rows + [row("p", h) for h in (1, 6, 24) if ("p", h) not in seen]
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

    def test_cross_horizon_source_conflict_rejected(self):
        with self.assertRaisesRegex(ValueError, "Cross-horizon"):
            self.evaluate([row("p", 48), row("p", 6, source_sha256="b"*64)])

    def test_abstaining_horizon_cannot_omit_source_identity(self):
        incomplete = row("p", 6, coverage_complete=False)
        del incomplete["source_sha256"]
        with self.assertRaisesRegex(ValueError, "Missing cross-horizon"):
            self.evaluate([row("p", 48), incomplete])

    def test_read_only_b_handoff(self):
        payload = dict(outcomes=[row("p", h) for h in (1, 6, 24, 48)], baseline_decisions={"p": True},
                       challenger_decisions={"p": False},
                       training_end_utc="2026-07-29T00:00:00Z",
                       holdout_start_utc="2026-08-01T00:00:00Z",
                       evaluation_asof_utc="2026-08-07T00:00:00Z",
                       baseline_version="baseline-1", challenger_version="shadow-2")
        with tempfile.TemporaryDirectory() as folder:
            source, output = Path(folder)/"input.json", Path(folder)/"evidence.json"
            source.write_text(json.dumps(payload), encoding="utf-8")
            main([str(source), "--output", str(output)])
            result = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(result["status"], "NO_QUALIFIED_RULE")
            self.assertFalse(result["promotion_authorized"])
            self.assertFalse(result["source_authentication_verified_by_adapter"])

    def test_incomplete_horizon_abstains_from_comparison(self):
        result = self.evaluate([row("p", h) for h in (1, 6, 24, 48)] + [row("q", 48)], base={"p": True}, challenger={"p": False})
        self.assertEqual(result["incomplete_prediction_horizons"], {"q": [1, 6, 24]})
        self.assertEqual(result["four_horizon_complete_predictions"], 1)
        self.assertEqual(result["cohort_size"], 1)

    def test_abstaining_horizon_cannot_redefine_source_identity(self):
        with self.assertRaisesRegex(ValueError, "Cross-horizon"):
            self.evaluate([row("p", 48), row("p", 6, coverage_complete=False,
                                            source_sha256="b"*64)])

    def test_horizon_counts_are_descriptive_not_authenticated(self):
        result = self.evaluate([row("p", h, hit=(h != 1)) for h in (1, 6, 24, 48)])
        self.assertEqual(result["eligible_horizon_counts"]["1"], {"hits": 0, "misses": 1})
        self.assertEqual(result["eligible_horizon_counts"]["48"], {"hits": 1, "misses": 0})
        self.assertEqual(result["source_qualified_prediction_count"], 1)
        self.assertFalse(result["counts_independently_authenticated"])
        self.assertFalse(result["promotion_authorized"])

    def test_comparable_horizon_rates_exclude_partial_predictions(self):
        rows = [row("p", h, hit=(h == 48)) for h in (1, 6, 24, 48)]
        rows += [row("q", 1, hit=True), row("q", 6, hit=True)]
        result = self.evaluate(rows)
        self.assertEqual(result["eligible_horizon_counts"]["1"], {"hits": 1, "misses": 1})
        self.assertEqual(result["complete_cohort_horizon_counts"]["1"], {"hits": 0, "misses": 1})
        self.assertEqual(result["complete_cohort_horizon_counts"]["48"], {"hits": 1, "misses": 0})
        self.assertEqual(result["complete_cohort_horizon_rates"]["1"], 0.0)
        self.assertEqual(result["complete_cohort_horizon_rates"]["48"], 1.0)
        self.assertEqual(result["incomplete_prediction_horizons"], {"q": [24, 48]})
        handoff = project_learning_handoff(result)
        self.assertEqual(handoff["complete_cohort_horizon_counts"], result["complete_cohort_horizon_counts"])
        self.assertFalse(handoff["measured_lift_verified"])

    def test_missing_48h_is_reported_not_silently_dropped(self):
        result = self.evaluate([row("p", h) for h in (1, 6, 24, 48)] +
                               [row("q", h) for h in (1, 6, 24)])
        self.assertEqual(result["incomplete_prediction_horizons"], {"q": [48]})
        self.assertEqual(result["observed_prediction_count"], 2)
        self.assertEqual(result["excluded_prediction_count"], 1)
        self.assertEqual(result["four_horizon_complete_predictions"], 1)

    def test_read_only_learning_handoff_separates_unverified_counts(self):
        result = self.evaluate([row("p", h) for h in (1, 6, 24, 48)])
        handoff = project_learning_handoff(result)
        self.assertEqual(handoff["schema"], "paper_learning_handoff_v1")
        self.assertEqual(handoff["complete_cohort_count"], 1)
        self.assertFalse(handoff["source_authenticated"])
        self.assertFalse(handoff["measured_lift_verified"])
        self.assertFalse(handoff["promotion_authorized"])
        with self.assertRaisesRegex(ValueError, "Unsafe"):
            project_learning_handoff(dict(result, promotion_authorized=True))

    def test_cli_writes_separate_b_handoff_and_refuses_overwrite(self):
        payload = dict(outcomes=[row("p", h) for h in (1, 6, 24, 48)],
                       baseline_decisions={"p": True}, challenger_decisions={"p": False},
                       training_end_utc="2026-07-29T00:00:00Z",
                       holdout_start_utc="2026-08-01T00:00:00Z",
                       evaluation_asof_utc="2026-08-07T00:00:00Z",
                       baseline_version="baseline-1", challenger_version="shadow-2")
        with tempfile.TemporaryDirectory() as folder:
            source, full, handoff = (Path(folder)/name for name in ("input.json", "full.json", "b.json"))
            source.write_text(json.dumps(payload), encoding="utf-8")
            main([str(source), "--output", str(full), "--delivery-output", str(handoff)])
            self.assertEqual(json.loads(handoff.read_text())["status"], "NO_QUALIFIED_RULE")
            with self.assertRaises(FileExistsError):
                main([str(source), "--output", str(full), "--delivery-output", str(handoff)])

    def test_cli_rolls_back_if_b_handoff_publication_fails(self):
        from unittest.mock import patch
        from . import heldout_outcome_adapter as adapter
        payload = dict(outcomes=[row("p", h) for h in (1, 6, 24, 48)],
                       baseline_decisions={"p": True}, challenger_decisions={"p": False},
                       training_end_utc="2026-07-29T00:00:00Z",
                       holdout_start_utc="2026-08-01T00:00:00Z",
                       evaluation_asof_utc="2026-08-07T00:00:00Z",
                       baseline_version="baseline-1", challenger_version="shadow-2")
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source, full, handoff = (root / name for name in ("input.json", "full.json", "b.json"))
            source.write_text(json.dumps(payload), encoding="utf-8")
            real_link = adapter.os.link
            def fail_b(source_path, destination):
                if Path(destination) == handoff:
                    raise OSError("injected B publication failure")
                return real_link(source_path, destination)
            with patch.object(adapter.os, "link", side_effect=fail_b):
                with self.assertRaisesRegex(OSError, "injected B"):
                    main([str(source), "--output", str(full),
                          "--delivery-output", str(handoff)])
            self.assertFalse(full.exists())
            self.assertFalse(handoff.exists())
            self.assertEqual(list(root.glob(".heldout-*")), [])

    def test_48h_gap_requires_decision_exclusion(self):
        result = self.evaluate([row("p", 48), row("gap", 48, coverage_complete=False)])
        self.assertEqual(result["cohort_size"], 1)
        self.assertEqual(result["abstention_counts"], {"INCOMPLETE_SOURCE_COVERAGE": 1})


if __name__ == "__main__":
    unittest.main()
