"""Adversarial native scheduling deficit and recovery distinction contracts."""
import unittest
from paper_pov.native_gap_diagnostic import diagnose, recovery_candidates

NOW = "2026-11-02T17:21:00Z"
SHA = "e3fb5ec272d74a72f19e306c1825aae1b7960576"


def run(rid, created, event="schedule", **changes):
    row = {"id": rid, "created_at": created, "event": event,
           "path": ".github/workflows/paper-pipeline.yml",
           "head_branch": "main", "head_sha": SHA, "run_attempt": 1}
    row.update(changes)
    return row


class NativeGapDiagnosticTests(unittest.TestCase):
    def test_real_shape_matured_deficit_dispatch_not_native(self):
        runs = [run(41438473450, "2026-11-02T11:38:58Z"),
                run(41473947157, "2026-11-02T15:40:44Z"),
                run(41484528561, "2026-11-02T16:45:08Z", "workflow_dispatch")]
        d = diagnose(runs, NOW, listing_complete=True)
        self.assertEqual(d["matured_nominal_slot_count"], 11)
        self.assertEqual(d["minimum_unrepresented_native_creations_as_of"], 9)
        self.assertEqual(d["status"], "FAILED_NATIVE_CREATION_DEFICIT_AS_OF")
        self.assertFalse(d["permanent_miss_verified"])
        self.assertFalse(d["per_slot_origin_verified"])
        self.assertEqual(d["dispatch_api_run_ids"], [41484528561])

    def test_incomplete_listing_abstains(self):
        self.assertEqual(diagnose([], NOW)["status"], "UNVERIFIED_INCOMPLETE_API_COVERAGE")

    def test_duplicate_ids_abstain(self):
        r = run(1, "2026-11-02T16:45:08Z")
        self.assertIn("UNVERIFIED", diagnose([r, r], NOW, listing_complete=True)["status"])

    def test_foreign_workflow_and_branch_abstain(self):
        for field, value in (("path", ".github/workflows/other.yml"), ("head_branch", "feature")):
            with self.subTest(field=field):
                self.assertIn("UNVERIFIED", diagnose(
                    [run(1, "2026-11-02T16:45:08Z", **{field: value})],
                    NOW, listing_complete=True)["status"])

    def test_future_timestamp_abstains(self):
        self.assertIn("UNVERIFIED", diagnose(
            [run(1, "2026-11-02T17:22:00Z")], NOW, listing_complete=True)["status"])

    def test_rerun_is_one_origin_not_two(self):
        r = run(1, "2026-11-02T16:45:08Z", run_attempt=2)
        d = diagnose([r], NOW, listing_complete=True)
        self.assertEqual(d["native_api_run_count"], 1)

    def test_missing_attempt_abstains(self):
        self.assertIn("UNVERIFIED", diagnose(
            [run(1, "2026-11-02T16:45:08Z", run_attempt=None)],
            NOW, listing_complete=True)["status"])

    def test_invalid_source_abstains(self):
        self.assertIn("UNVERIFIED", diagnose(
            [run(1, "2026-11-02T16:45:08Z", head_sha="not-a-sha")],
            NOW, listing_complete=True)["status"])

    def test_delayed_schedule_not_assigned_hour(self):
        d = diagnose([run(1, "2026-11-02T15:40:44Z")], NOW, listing_complete=True)
        self.assertFalse(d["per_slot_origin_verified"])
        self.assertEqual(d["native_api_run_count"], 1)

    def test_empty_complete_window_reports_deficit_not_permanent_drop(self):
        d = diagnose([], NOW, listing_complete=True)
        self.assertEqual(d["minimum_unrepresented_native_creations_as_of"], 11)
        self.assertFalse(d["permanent_miss_verified"])

    def test_recovery_temporal_candidate_not_owner_manual(self):
        dispatch = run(41484528561, "2026-11-02T16:45:08Z", "workflow_dispatch")
        attempt = {"controller_run_id": 41484427220,
                   "accepted_at": "2026-11-02T16:45:09Z",
                   "marker_readback_verified": True,
                   "dispatch_http_accepted": True}
        d = recovery_candidates([dispatch], [attempt])
        self.assertEqual(d["dispatches"][0]["classification"], "RECOVERY_TIMING_CANDIDATE_NOT_CAUSAL")
        self.assertFalse(d["dispatches"][0]["owner_manual_verified"])
        self.assertFalse(d["dispatches"][0]["controller_causality_verified"])

    def test_ambiguous_controller_candidate_fails_closed(self):
        dispatch = run(1, "2026-11-02T16:45:08Z", "workflow_dispatch")
        attempts = [{"controller_run_id": i, "accepted_at": "2026-11-02T16:45:09Z",
                     "marker_readback_verified": True, "dispatch_http_accepted": True}
                    for i in (2, 3)]
        d = recovery_candidates([dispatch], attempts)
        self.assertEqual(d["dispatches"][0]["classification"], "AMBIGUOUS_RECOVERY_CORRELATION")

    def test_unverified_controller_marker_not_attributed(self):
        dispatch = run(1, "2026-11-02T16:45:08Z", "workflow_dispatch")
        d = recovery_candidates([dispatch], [{
            "controller_run_id": 2, "accepted_at": "2026-11-02T16:45:09Z",
            "marker_readback_verified": False, "dispatch_http_accepted": True}])
        self.assertEqual(d["dispatches"][0]["classification"], "UNVERIFIED_DISPATCH_ORIGIN")

    def test_recovery_foreign_or_rerun_dispatch_abstains(self):
        for changes in ({"path": ".github/workflows/other.yml"},
                        {"head_branch": "other"}, {"run_attempt": 2},
                        {"head_sha": "bad"}, {"id": True}):
            with self.subTest(changes=changes):
                d = recovery_candidates(
                    [run(1, "2026-11-02T16:45:08Z", "workflow_dispatch", **changes)], [])
                self.assertEqual(d["status"], "UNVERIFIED_INVALID_CORRELATION_INPUT")

    def test_recovery_duplicate_dispatch_identity_abstains(self):
        r = run(1, "2026-11-02T16:45:08Z", "workflow_dispatch")
        self.assertEqual(recovery_candidates([r, r], [])["status"],
                         "UNVERIFIED_INVALID_CORRELATION_INPUT")

    def test_recovery_duplicate_authenticated_controller_id_abstains(self):
        a = {"controller_run_id": 2, "accepted_at": "2026-11-02T16:45:09Z",
             "marker_readback_verified": True, "dispatch_http_accepted": True}
        r = run(1, "2026-11-02T16:45:08Z", "workflow_dispatch")
        self.assertEqual(recovery_candidates([r], [a, dict(a)])["status"],
                         "UNVERIFIED_INVALID_CORRELATION_INPUT")

    def test_recovery_before_controller_acceptance_beyond_clock_skew_not_attributed(self):
        a = {"controller_run_id": 2, "accepted_at": "2026-11-02T16:45:30Z",
             "marker_readback_verified": True, "dispatch_http_accepted": True}
        r = run(1, "2026-11-02T16:45:08Z", "workflow_dispatch")
        d = recovery_candidates([r], [a])
        self.assertEqual(d["dispatches"][0]["classification"], "UNVERIFIED_DISPATCH_ORIGIN")

    def test_recovery_outside_bounded_lag_not_attributed(self):
        a = {"controller_run_id": 2, "accepted_at": "2026-11-02T16:40:00Z",
             "marker_readback_verified": True, "dispatch_http_accepted": True}
        r = run(1, "2026-11-02T16:45:08Z", "workflow_dispatch")
        d = recovery_candidates([r], [a])
        self.assertEqual(d["dispatches"][0]["classification"], "UNVERIFIED_DISPATCH_ORIGIN")

    def test_recovery_one_controller_matching_two_dispatches_is_ambiguous(self):
        a = {"controller_run_id": 2, "accepted_at": "2026-11-02T16:45:09Z",
             "marker_readback_verified": True, "dispatch_http_accepted": True}
        runs = [run(1, "2026-11-02T16:45:08Z", "workflow_dispatch"),
                run(3, "2026-11-02T16:45:10Z", "workflow_dispatch")]
        d = recovery_candidates(runs, [a])
        self.assertEqual(len(d["dispatches"]), 2)
        self.assertTrue(all(x["classification"] == "AMBIGUOUS_RECOVERY_CORRELATION"
                            for x in d["dispatches"]))

    def test_recovery_optional_source_mismatch_never_attributed(self):
        a = {"controller_run_id": 2, "accepted_at": "2026-11-02T16:45:09Z",
             "marker_readback_verified": True, "dispatch_http_accepted": True,
             "source_sha": "a" * 40}
        r = run(1, "2026-11-02T16:45:08Z", "workflow_dispatch")
        d = recovery_candidates([r], [a])
        self.assertEqual(d["dispatches"][0]["classification"], "UNVERIFIED_DISPATCH_ORIGIN")

    def test_recovery_bad_authenticated_controller_time_abstains(self):
        a = {"controller_run_id": 2, "accepted_at": "not-a-timestamp",
             "marker_readback_verified": True, "dispatch_http_accepted": True}
        r = run(1, "2026-11-02T16:45:08Z", "workflow_dispatch")
        self.assertEqual(recovery_candidates([r], [a])["status"],
                         "UNVERIFIED_INVALID_CORRELATION_INPUT")


if __name__ == "__main__":
    unittest.main()
