"""No-network failure injection for the read-only GitHub cadence collector."""
import io
import unittest
from unittest.mock import patch

from paper_pov.cadence_collect import collect, github_reader, delivery_log_claim, SafeLogRedirect
from urllib.request import Request

SHA = "a" * 40
NOW = "2026-11-02T03:20:00Z"


def row(rid, event):
    return {"id": rid, "event": event, "created_at": "2026-11-02T03:10:01Z",
            "run_attempt": 1, "status": "completed", "conclusion": "success",
            "path": ".github/workflows/paper-pipeline.yml",
            "head_branch": "main", "head_sha": SHA}


def job(rid):
    return {"id": rid + 100, "run_id": rid, "name": "public-paper",
            "status": "completed", "conclusion": "success",
            "started_at": "2026-11-02T03:10:04Z",
            "completed_at": "2026-11-02T03:11:00Z"}


def log(event, cron):
    return ("2026-11-02T03:10:06Z PAPER_VERIFIED_GITHUB_EVENT=" + event + "\n"
            "2026-11-02T03:10:06Z PAPER_VERIFIED_ORIGINATING_CRON=" + cron + "\n"
            "2026-11-02T03:10:06Z PAPER_PIPELINE_SOURCE_SHA=" + SHA + "\n")


def fixture(native=None, dispatched=None, jobs=True):
    native = [row(1, "schedule")] if native is None else native
    dispatched = [row(2, "workflow_dispatch")] if dispatched is None else dispatched
    calls = []
    def get(path, text=False):
        calls.append((path, text))
        if "workflows/paper-pipeline.yml/runs?" in path:
            rows = native if "event=schedule" in path else dispatched
            return {"workflow_runs": rows, "total_count": len(rows)}
        if "/runs/" in path and "/jobs?" in path:
            rid = int(path.split("/runs/")[1].split("/")[0])
            rows = [job(rid)] if jobs else []
            return {"jobs": rows, "total_count": len(rows)}
        if "/jobs/" in path and "/logs" in path and text:
            jid = int(path.split("/jobs/")[1].split("/")[0])
            return log("schedule", "9 * * * *") if jid == 101 else log(
                "workflow_dispatch", "MANUAL_DISPATCH")
        raise AssertionError("unexpected API request: " + path)
    return get, calls


class CadenceCollectorTests(unittest.TestCase):
    def test_readonly_collects_native_dispatch_and_sha_bound_log_index(self):
        get, calls = fixture()
        result = collect(get, "owner/repo", NOW)
        self.assertEqual(result["report"]["verified_native_count"], 1)
        self.assertEqual(result["report"]["verified_dispatch_count"], 1)
        self.assertEqual(len(result["evidence"]), 2)
        self.assertEqual(len(result["evidence"][0]["decoded_log_sha256"]), 64)
        self.assertFalse(result["evidence"][0]["raw_log_sha256_verified"])
        self.assertTrue(result["read_only"])
        self.assertFalse(result["raw_log_content_persisted"])
        self.assertTrue(all(path.startswith("/repos/") for path, _ in calls))
        workflow_queries = [path for path, _ in calls if "/workflows/" in path]
        self.assertEqual(len(workflow_queries), 2)
        self.assertTrue(all("created=%3E%3D2026-11-01T03%3A20%3A00Z" in path
                            for path in workflow_queries))
        self.assertEqual(sum("jobs/" in path and "/logs" in path for path, _ in calls), 2)

    def test_delivery_log_claim_requires_matching_run_and_job_time(self):
        base = log("schedule", "9 * * * *")
        readback = ("2026-11-02T03:10:30Z PAPER_LEDGER_REMOTE_READBACK_VERIFIED " + SHA + "\n")
        result = ("2026-11-02T03:10:40Z PAPER_RESULTS_VERIFIED 1 51 11\n")
        def get(path, text=False):
            upstream, _ = fixture(native=[row(1, "schedule")], dispatched=[])
            value = upstream(path, text)
            return base + readback + result if "/logs" in path else value
        evidence = collect(get, "owner/repo", NOW)["evidence"][0]
        self.assertEqual(evidence["delivery_log_claim_status"],
                         "MATCHED_LOG_MARKERS_NOT_REMOTE_BYTES")
        self.assertEqual((evidence["claimed_generation"], evidence["claimed_watch_count"]), (51, 11))
        self.assertFalse(evidence["remote_ledger_bytes_verified"])
        self.assertFalse(evidence["results_delivery_verified"])

    def test_delivery_log_claim_rejects_wrong_run_duplicate_and_reversed_order(self):
        start = __import__("datetime").datetime.fromisoformat("2026-11-02T03:10:04+00:00")
        end = __import__("datetime").datetime.fromisoformat("2026-11-02T03:11:00+00:00")
        readback = "2026-11-02T03:10:30Z PAPER_LEDGER_REMOTE_READBACK_VERIFIED " + SHA + "\n"
        good = "2026-11-02T03:10:40Z PAPER_RESULTS_VERIFIED 1 51 11\n"
        for payload in (readback + good.replace(" 1 51", " 2 51"),
                        readback + good + good,
                        readback + good + readback,
                        good.replace("03:10:40", "03:10:20") + readback,
                        "echo PAPER_LEDGER_REMOTE_READBACK_VERIFIED " + SHA + "\n" + good):
            with self.subTest(payload=payload):
                self.assertEqual(delivery_log_claim(payload, 1, start, end)
                                 ["delivery_log_claim_status"], "UNVERIFIED")

    def test_no_writer_job_abstains_not_fabricates_native_success(self):
        get, _ = fixture(jobs=False)
        result = collect(get, "owner/repo", NOW)
        self.assertEqual(result["report"]["verified_native_count"], 0)
        self.assertEqual(result["report"]["unverified_or_ambiguous_count"], 2)

    def test_green_workflow_with_failed_or_skipped_writer_abstains(self):
        for conclusion in ("failure", "skipped", "cancelled", None):
            with self.subTest(conclusion=conclusion):
                get, calls = fixture()
                def changed(path, text=False):
                    response = get(path, text)
                    if "/runs/" in path and "/jobs?" in path:
                        response["jobs"][0]["conclusion"] = conclusion
                    return response
                result = collect(changed, "owner/repo", NOW)
                self.assertEqual(result["report"]["verified_native_count"], 0)
                self.assertEqual(result["report"]["verified_dispatch_count"], 0)
                self.assertFalse(any("/logs" in path for path, _ in calls))

    def test_missing_or_incoherent_writer_job_times_abstain(self):
        for field, value in (("completed_at", None),
                             ("completed_at", "2026-11-02T03:09:00Z"),
                             ("started_at", "2026-11-02T03:12:00Z")):
            with self.subTest(field=field, value=value):
                get, calls = fixture()
                def changed(path, text=False):
                    response = get(path, text)
                    if "/runs/" in path and "/jobs?" in path:
                        response["jobs"][0][field] = value
                    return response
                result = collect(changed, "owner/repo", NOW)
                self.assertEqual(result["report"]["verified_native_count"], 0)
                self.assertFalse(any("/logs" in path for path, _ in calls))

    def test_event_query_mismatch_abstains_before_cadence_metrics(self):
        get, _ = fixture()
        def changed(path, text=False):
            response = get(path, text)
            if "event=schedule" in path:
                response["workflow_runs"][0]["event"] = "workflow_dispatch"
            return response
        with self.assertRaisesRegex(ValueError, "event query mismatch"):
            collect(changed, "owner/repo", NOW)

    def test_duplicate_event_run_ids_fail_closed(self):
        get, _ = fixture(dispatched=[row(1, "workflow_dispatch")])
        with self.assertRaisesRegex(ValueError, "duplicate"):
            collect(get, "owner/repo", NOW)

    def test_run_budget_fails_before_partial_results(self):
        get, _ = fixture()
        with self.assertRaisesRegex(ValueError, "budget"):
            collect(get, "owner/repo", NOW, max_runs=1)

    def test_full_page_fails_instead_of_silent_pagination_loss(self):
        get, _ = fixture(native=[row(i, "schedule") for i in range(1, 101)])
        with self.assertRaisesRegex(ValueError, "truncated"):
            collect(get, "owner/repo", NOW)

    def test_server_reported_extra_run_page_abstains_instead_of_undercount(self):
        get, _ = fixture()
        def altered(path, text=False):
            response = get(path, text)
            if "/workflows/" in path:
                response["total_count"] += 1
            return response
        with self.assertRaisesRegex(ValueError, "truncated"):
            collect(altered, "owner/repo", NOW)

    def test_server_reported_extra_job_page_abstains_instead_of_certifying(self):
        get, _ = fixture()
        def altered(path, text=False):
            response = get(path, text)
            if "/runs/" in path and "/jobs?" in path:
                response["total_count"] += 1
            return response
        with self.assertRaisesRegex(ValueError, "truncated"):
            collect(altered, "owner/repo", NOW)

    def test_lossy_non_utf8_job_log_is_rejected_before_provenance(self):
        with patch("paper_pov.cadence_collect.build_opener") as opener:
            opener.return_value.open.return_value.__enter__.return_value = io.BytesIO(
                b"bad-utf8-" + bytes([255]))
            get = github_reader("test-readonly-token")
            with self.assertRaises(UnicodeDecodeError):
                get("/repos/owner/repo/actions/jobs/123/logs", text=True)

    def test_log_redirect_strips_bearer_and_rejects_untrusted_storage(self):
        req = Request("https://api.github.com/repos/owner/repo/actions/jobs/123/logs",
                      headers={"Authorization": "Bearer private-token"})
        safe = SafeLogRedirect().redirect_request(
            req, None, 302, "Found", {},
            "https://pipelines.actions.githubusercontent.com/logs?sig=abc")
        self.assertEqual(safe.get_method(), "GET")
        self.assertIsNone(safe.get_header("Authorization"))
        for target in ("http://pipelines.actions.githubusercontent.com/logs",
                       "https://evil.example.com/logs",
                       "https://githubusercontent.com.evil.example.com/logs"):
            with self.subTest(target=target), self.assertRaises(ValueError):
                SafeLogRedirect().redirect_request(req, None, 302, "Found", {}, target)

    def test_live_rehearsal_workflow_is_get_only_and_has_no_writer(self):
        from pathlib import Path
        workflow = (Path(__file__).resolve().parents[1] / ".github" /
                    "workflows" / "paper-cadence-provenance-ci.yml").read_text()
        self.assertIn("actions: read", workflow)
        self.assertIn("authenticated-get-only-rehearsal:", workflow)
        self.assertIn("python -m paper_pov.cadence_collect", workflow)
        self.assertIn("--lookback-hours 6 --max-runs 40", workflow)
        self.assertNotIn("gh workflow run", workflow)
        self.assertNotIn("paper-proof-ledger-single-writer", workflow)

    def test_reader_uses_only_get_for_authenticated_evidence(self):
        def fake_open(request, timeout):
            self.assertEqual(request.get_method(), "GET")
            self.assertEqual(timeout, 20)
            return io.BytesIO(b'{"total_count":0,"workflow_runs":[]}')
        with patch("paper_pov.cadence_collect.urlopen", side_effect=fake_open):
            result = github_reader("test-readonly-token")(
                "/repos/owner/repo/actions/workflows/paper-pipeline.yml/runs")
        self.assertEqual(result["total_count"], 0)

    def test_invalid_repo_or_unbounded_parameters_fail_before_network(self):
        get, calls = fixture()
        for repo in ("owner", "owner/repo/other", "owner/repo?x=1",
                     "../repo", "owner/..", "./repo"):
            with self.subTest(repo=repo), self.assertRaises(ValueError):
                collect(get, repo, NOW)
        with self.assertRaises(ValueError):
            collect(get, "owner/repo", NOW, lookback_hours=169)
        self.assertEqual(calls, [])


if __name__ == "__main__":
    unittest.main()
