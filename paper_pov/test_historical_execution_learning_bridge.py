"""Contract checks for the real E1 reconstructed-outcome artifact handoff."""
import unittest
from .historical_execution_learning_bridge import project_historical_execution


def fixture():
    digest = "a" * 64
    labels = [
        {"horizon_hours": h, "status": "MATURED_OBSERVED",
         "observed_30pct_hit": h == 48, "qualified_for_learning": False}
        for h in (1, 6, 24, 48)
    ]
    record = {"prediction_id": "p", "pair": "XXBTZUSD",
              "entry_method": "next_5m_bar_open_proxy",
              "source_sha256": digest, "source_authenticated": False, "labels": labels}
    execution = {"schema": "historical_outcome_execution_v1",
                 "outcome_input_sha256": digest, "source_authenticated": False,
                 "qualified_for_learning": False, "promotion_authorized": False,
                 "outcomes": {"schema": "qualified_ohlc_outcome_batch_v1",
                              "source_sha256": digest, "source_authenticated": False,
                              "prediction_count": 1, "records": [record]}}
    return execution, [{"prediction_id": "p", "pair": "XXBTZUSD"},
                       {"prediction_id": "unlabeled", "pair": "ETHUSD"}]


class HistoricalBridgeTests(unittest.TestCase):
    def test_real_reconstruction_contract_remains_unqualified(self):
        execution, frozen = fixture()
        result = project_historical_execution(execution, frozen_predictions=frozen)
        self.assertEqual(result["reconstructed_prediction_count"], 1)
        self.assertEqual(result["missing_prediction_count"], 1)
        self.assertEqual(result["diagnostic_horizon_status_counts"]["48"]["MATURED_OBSERVED"], 1)
        self.assertEqual(result["status"], "NO_QUALIFIED_RULE")
        self.assertFalse(result["source_authenticated"])
        self.assertFalse(result["promotion_authorized"])

    def test_existing_b_learning_projection_contract(self):
        execution, frozen = fixture()
        handoff = project_historical_execution(execution, frozen_predictions=frozen)
        self.assertEqual(handoff["observed_prediction_count"], 2)
        self.assertEqual(handoff["complete_cohort_count"], 0)
        self.assertEqual(handoff["excluded_prediction_count"], 2)
        self.assertEqual(len(handoff["incomplete_prediction_horizons"]), 2)
        self.assertEqual(handoff["abstention_counts"], {"UNAUTHENTICATED_ARCHIVE_OR_PROXY_ENTRY": 1, "NO_RECONSTRUCTED_OUTCOME": 1})
        self.assertEqual(len(handoff["evidence_digest"]), 64)
        self.assertEqual(len(handoff["cohort_join_digest"]), 64)
        self.assertFalse(handoff["live_watch_authorized"])

    def test_gap_abstains_without_a_hit(self):
        execution, frozen = fixture()
        label = execution["outcomes"]["records"][0]["labels"][2]
        label.update(status="ABSTAIN_GAP", observed_30pct_hit=None)
        result = project_historical_execution(execution, frozen_predictions=frozen)
        self.assertEqual(result["diagnostic_horizon_status_counts"]["24"]["ABSTAIN_GAP"], 1)

    def test_outside_universe_and_false_authentication_rejected(self):
        execution, frozen = fixture()
        execution["outcomes"]["records"][0]["prediction_id"] = "invented"
        with self.assertRaisesRegex(ValueError, "frozen"):
            project_historical_execution(execution, frozen_predictions=frozen)
        execution, frozen = fixture()
        execution["source_authenticated"] = True
        with self.assertRaisesRegex(ValueError, "authentication"):
            project_historical_execution(execution, frozen_predictions=frozen)

    def test_missing_or_duplicate_horizon_rejected(self):
        execution, frozen = fixture()
        execution["outcomes"]["records"][0]["labels"][1]["horizon_hours"] = 1
        with self.assertRaisesRegex(ValueError, "duplicate"):
            project_historical_execution(execution, frozen_predictions=frozen)

    def test_reconstructed_asof_cannot_drift_from_frozen_a2(self):
        execution, frozen = fixture()
        execution["outcomes"]["records"][0]["as_of"] = "2026-01-02T00:00:00Z"
        times = {"p": "2026-01-01T00:00:00Z",
                 "unlabeled": "2026-01-01T00:00:00Z"}
        with self.assertRaisesRegex(ValueError, "differs from frozen"):
            project_historical_execution(
                execution, frozen_predictions=frozen, frozen_observation_times=times)
        execution["outcomes"]["records"][0]["as_of"] = "2025-12-31T19:00:00-05:00"
        result = project_historical_execution(
            execution, frozen_predictions=frozen, frozen_observation_times=times)
        self.assertEqual(result["status"], "NO_QUALIFIED_RULE")

    def test_nonhex_source_digest_rejected(self):
        execution, frozen = fixture()
        execution["outcome_input_sha256"] = "z" * 64
        execution["outcomes"]["source_sha256"] = "z" * 64
        execution["outcomes"]["records"][0]["source_sha256"] = "z" * 64
        with self.assertRaisesRegex(ValueError, "invalid input digest"):
            project_historical_execution(execution, frozen_predictions=frozen)

    def test_source_digest_disagreement_rejected(self):
        execution, frozen = fixture()
        execution["outcomes"]["source_sha256"] = "b" * 64
        with self.assertRaisesRegex(ValueError, "digest"):
            project_historical_execution(execution, frozen_predictions=frozen)


if __name__ == "__main__":
    unittest.main()
