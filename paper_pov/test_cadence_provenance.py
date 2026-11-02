"""Offline, adversarial contracts for read-only PAPER cadence provenance."""
import unittest
import json
import tempfile
import io
from pathlib import Path
from contextlib import redirect_stdout
from unittest.mock import patch
from paper_pov.cadence_provenance import audit, provenance, main

SHA = "a" * 40

def run(rid=1, when="2026-11-01T19:10:01Z", event="schedule", sha=SHA):
    return {"id": rid, "created_at": when, "event": event, "head_sha": sha,
            "path": ".github/workflows/paper-pipeline.yml", "head_branch": "main",
            "status": "completed", "conclusion": "success"}

def log(event="schedule", cron="39 * * * *", sha=SHA):
    return ("2026-11-01T19:10:06Z PAPER_VERIFIED_GITHUB_EVENT=" + event + "\n"
            "2026-11-01T19:10:06Z PAPER_VERIFIED_ORIGINATING_CRON=" + cron + "\n"
            "2026-11-01T19:10:06Z PAPER_PIPELINE_SOURCE_SHA=" + sha + "\n")

NOW = "2026-11-02T03:20:00Z"

class CadenceProvenanceTests(unittest.TestCase):
    def check(self, rows=None, logs=None, jobs=None):
        return audit(rows if rows is not None else [run()], logs if logs is not None else {"1": log()}, NOW, jobs=jobs)

    def test_actual_late_39_slot_is_not_misattributed_to_09_slot(self):
        result = self.check()
        self.assertEqual(result["verified_native_count"], 1)
        self.assertEqual(result["runs"][0]["latest_possible_nominal_slot"], "2026-11-01T18:39:00+00:00")
        self.assertEqual(result["runs"][0]["minimum_lateness_seconds"], 1861)
        self.assertFalse(result["runs"][0]["originating_hour_verified"])

    def test_late_09_slot_53_minutes(self):
        result = self.check([run(2, "2026-11-01T15:02:07Z")], {"2": log(cron="9 * * * *")})
        self.assertEqual(result["runs"][0]["latest_possible_nominal_slot"], "2026-11-01T14:09:00+00:00")
        self.assertEqual(result["runs"][0]["minimum_lateness_seconds"], 3187)

    def test_manual_dispatch_is_not_native_and_no_recovery_inference(self):
        result = self.check([run(event="workflow_dispatch")], {"1": log(event="workflow_dispatch", cron="MANUAL_DISPATCH")})
        self.assertEqual((result["verified_native_count"], result["verified_dispatch_count"]), (0, 1))
        self.assertEqual(result["runs"][0]["classification"], "VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE")

    def test_missing_or_shell_echoed_log_cannot_verify(self):
        for payload in ({}, {"1": 'echo "PAPER_VERIFIED_GITHUB_EVENT=schedule"'}):
            with self.subTest(payload=payload):
                self.assertEqual(self.check(logs=payload)["unverified_or_ambiguous_count"], 1)

    def test_duplicate_or_conflicting_provenance_abstains(self):
        self.assertIsNone(provenance(log() + log(event="workflow_dispatch")))
        self.assertEqual(self.check(logs={"1": log() + log()})["verified_native_count"], 0)

    def test_wrong_source_or_event_never_verified(self):
        for payload in ({"1": log(sha="b"*40)}, {"1": log(event="workflow_dispatch", cron="MANUAL_DISPATCH")}):
            with self.subTest(payload=payload):
                self.assertEqual(self.check(logs=payload)["verified_native_count"], 0)

    def test_missing_cron_or_wrong_cron_abstains(self):
        self.assertEqual(self.check(logs={"1": log(cron="MANUAL_DISPATCH")})["verified_native_count"], 0)

    def test_invalid_and_duplicate_run_ids_never_count_as_proven(self):
        result = self.check([run(), run()], {"1": log()})
        self.assertEqual(result["verified_native_count"], 0)
        self.assertEqual(result["unverified_or_ambiguous_count"], 2)
        self.assertTrue(all(r["classification"] == "INVALID_RUN_METADATA" for r in result["runs"]))

    def test_duplicate_conflicting_run_cannot_leave_first_verified(self):
        rows = [run(), {**run(), "event": "workflow_dispatch"}]
        result = self.check(rows, {"1": log()})
        self.assertEqual(result["verified_native_count"], 0)
        self.assertEqual(result["verified_dispatch_count"], 0)
        self.assertEqual(result["unverified_or_ambiguous_count"], 2)

    def test_future_run_within_two_minutes_is_invalid_not_silently_skipped(self):
        result = self.check([run(1, "2026-11-02T03:20:30Z")])
        self.assertEqual(result["runs"][0]["classification"], "INVALID_RUN_METADATA")

    def test_older_than_lookback_not_counted(self):
        self.assertEqual(self.check([run(1, "2026-10-31T00:00:00Z")])["runs"], [])

    def test_future_run_not_counted(self):
        self.assertEqual(self.check([run(1, "2026-11-03T00:00:00Z")])["runs"][0]["classification"], "INVALID_RUN_METADATA")


    def test_foreign_workflow_markers_cannot_spoof_paper_writer(self):
        for changed in ({"path": ".github/workflows/other.yml"},
                        {"head_branch": "research-branch"},
                        {"path": None}, {"head_branch": None}):
            with self.subTest(changed=changed):
                candidate = {**run(), **changed}
                result = self.check([candidate])
                self.assertEqual(result["verified_native_count"], 0)
                self.assertEqual(result["runs"][0]["classification"], "WRONG_WORKFLOW_OR_REF")

    def test_failed_native_is_attempt_not_successful_scan(self):
        candidate = {**run(), "conclusion": "failure"}
        result = self.check([candidate])
        self.assertEqual(result["verified_native_count"], 0)
        self.assertEqual(result["verified_native_unsuccessful_count"], 1)
        self.assertEqual(result["runs"][0]["classification"], "VERIFIED_NATIVE_SCHEDULE_UNSUCCESSFUL")
        self.assertEqual(result["runs"][0]["minimum_lateness_seconds"], 1861)
        self.assertFalse(result["runs"][0]["durable_ledger_verified"])

    def test_failed_dispatch_is_attempt_not_successful_scan(self):
        candidate = {**run(event="workflow_dispatch"), "conclusion": "cancelled"}
        result = self.check([candidate], {"1": log(event="workflow_dispatch", cron="MANUAL_DISPATCH")})
        self.assertEqual(result["verified_dispatch_count"], 0)
        self.assertEqual(result["verified_dispatch_unsuccessful_count"], 1)
        self.assertEqual(result["runs"][0]["classification"], "VERIFIED_WORKFLOW_DISPATCH_UNSUCCESSFUL")

    def test_incomplete_or_unknown_outcome_never_claimed_successful(self):
        for changed, expected in (({"status": "in_progress", "conclusion": None}, "INCOMPLETE_WORKFLOW"),
                                  ({"status": "completed", "conclusion": None}, "UNKNOWN_WORKFLOW_CONCLUSION"),
                                  ({"status": "completed", "conclusion": "skipped"}, "UNKNOWN_WORKFLOW_CONCLUSION")):
            with self.subTest(changed=changed):
                result = self.check([{**run(), **changed}])
                self.assertEqual(result["verified_native_count"], 0)
                self.assertEqual(result["runs"][0]["classification"], expected)

    def test_same_source_dispatch_and_schedule_does_not_prove_manual_parity(self):
        rows = [run(), run(2, "2026-11-01T19:40:01Z", event="workflow_dispatch")]
        logs = {"1": log(), "2": log(event="workflow_dispatch", cron="MANUAL_DISPATCH")}
        result = self.check(rows, logs)
        self.assertEqual((result["verified_native_count"], result["verified_dispatch_count"]), (1, 1))
        self.assertNotIn("manual_parity_verified", result)
        self.assertNotIn("ledger_verified", result)

    def test_successful_writer_creation_gap_is_quantified_not_called_ledger_gap(self):
        rows = [run(1, "2026-11-02T01:10:01Z"),
                run(2, "2026-11-02T02:10:01Z", event="workflow_dispatch")]
        logs = {"1": log(), "2": log(event="workflow_dispatch", cron="MANUAL_DISPATCH")}
        result = self.check(rows, logs)
        self.assertEqual(result["verified_successful_writer_run_creation_count"], 2)
        self.assertEqual(result["max_verified_successful_run_creation_gap_seconds"], 3600)
        self.assertEqual(result["seconds_since_last_verified_successful_run_creation"], 4199)
        self.assertTrue(result["over_45m_since_verified_successful_run_creation"])
        self.assertNotIn("missed_slots_verified", result)

    def test_failed_run_does_not_reset_last_successful_creation(self):
        rows = [run(1, "2026-11-02T01:10:01Z"),
                {**run(2, "2026-11-02T03:10:01Z"), "conclusion": "failure"}]
        result = self.check(rows, {"1": log(), "2": log()})
        self.assertEqual(result["verified_native_unsuccessful_count"], 1)
        self.assertEqual(result["last_verified_successful_run_created_at"], "2026-11-02T01:10:01+00:00")
        self.assertTrue(result["over_45m_since_verified_successful_run_creation"])

    def test_no_authenticated_run_abstains_on_staleness_instead_of_zero(self):
        result = self.check(rows=[], logs={})
        self.assertIsNone(result["over_45m_since_verified_successful_run_creation"])
        self.assertIsNone(result["max_verified_successful_run_creation_gap_seconds"])
        self.assertIsNone(result["seconds_since_last_verified_successful_run_creation"])

    def test_authenticated_writer_job_queue_separates_from_cron_lateness(self):
        jobs = {"1": [{"run_id": 1, "name": "public-paper",
                        "started_at": "2026-11-01T19:10:04Z"}]}
        result = self.check(jobs=jobs)
        self.assertEqual(result["writer_job_queue_sample_count"], 1)
        self.assertEqual(result["max_verified_writer_job_queue_seconds"], 3)
        self.assertEqual(result["runs"][0]["minimum_lateness_seconds"], 1861)
        self.assertEqual(result["runs"][0]["writer_job_queue_seconds"], 3)

    def test_untrusted_or_ambiguous_job_timing_abstains(self):
        for candidates in (None, [], [{"run_id": 999, "name": "public-paper",
                                        "started_at": "2026-11-01T19:10:04Z"}],
                           [{"run_id": 1, "name": "other",
                             "started_at": "2026-11-01T19:10:04Z"}],
                           [{"run_id": 1, "name": "public-paper",
                             "started_at": "2026-11-01T19:09:59Z"}],
                           [{"run_id": 1, "name": "public-paper",
                             "started_at": "2026-11-01T19:10:04Z"}] * 2):
            with self.subTest(candidates=candidates):
                result = self.check(jobs={"1": candidates})
                self.assertEqual(result["writer_job_queue_sample_count"], 0)
                self.assertIsNone(result["max_verified_writer_job_queue_seconds"])
                self.assertNotIn("writer_job_queue_seconds", result["runs"][0])

    def test_cli_optional_jobs_metadata_produces_read_only_queue_metric(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "runs.json").write_text(json.dumps({"workflow_runs": [run()]}))
            (root / "logs.json").write_text(json.dumps({"1": log()}))
            (root / "jobs.json").write_text(json.dumps({
                "1": [{"run_id": 1, "name": "public-paper",
                       "started_at": "2026-11-01T19:10:04Z"}]}))
            argv = ["cadence_provenance", "--runs", str(root / "runs.json"),
                    "--logs", str(root / "logs.json"), "--jobs", str(root / "jobs.json"),
                    "--checked-at", NOW, "--output", str(root / "report.json")]
            with patch("sys.argv", argv), redirect_stdout(io.StringIO()):
                main()
            report = json.loads((root / "report.json").read_text())
            self.assertEqual(report["writer_job_queue_sample_count"], 1)
            self.assertEqual(report["max_verified_writer_job_queue_seconds"], 3)
            self.assertFalse(report["runs"][0]["durable_ledger_verified"])

    def test_no_false_ledger_or_trade_claims(self):
        result = self.check()
        self.assertNotIn("ledger_verified", result)
        self.assertNotIn("BUY", str(result))

if __name__ == "__main__":
    unittest.main()
