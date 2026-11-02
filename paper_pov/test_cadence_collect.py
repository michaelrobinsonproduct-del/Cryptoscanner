"""No-network failure injection for the read-only GitHub cadence collector."""
import io
import unittest
from unittest.mock import patch

from paper_pov.cadence_collect import collect, github_reader, delivery_log_claim, artifact_metadata_claim, SafeLogRedirect, RejectApiRedirect
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
        if "/runs/" in path and "/artifacts?" in path:
            rid = int(path.split("/runs/")[1].split("/")[0])
            source = {"id": rid, "head_sha": SHA, "head_branch": "main"}
            artifacts = [
                {"id": rid * 10 + i, "name": name + str(rid), "expired": False,
                 "size_in_bytes": 1234, "workflow_run": source,
                 "digest": "sha256:" + ("a" if i == 1 else "b") * 64}
                for i, name in enumerate(("public-paper-ledger-", "public-paper-results-"), 1)]
            return {"artifacts": artifacts, "total_count": len(artifacts)}
        if path.endswith("/git/ref/heads/paper-proof-ledger"):
            return {"ref": "refs/heads/paper-proof-ledger",
                    "object": {"sha": SHA, "type": "commit"}}
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

    def test_original_artifact_zip_byte_verifier_accepts_only_sealed_identity(self):
        import hashlib
        import json
        import zipfile
        from paper_pov import ledger
        from paper_pov.artifact_bytes_verify import verify_pair, main
        from contextlib import redirect_stdout
        from pathlib import Path
        import tempfile

        as_of = "2026-11-02T03:10:00+00:00"
        pair = "X/USD"
        prediction_id = hashlib.sha256(("paper-v1|" + as_of + "|" + pair).encode()).hexdigest()
        ledger_run_id = "d" * 64
        state = ledger.seal({
            "schema": 1, "generation": 1,
            "runs": [{"id": ledger_run_id, "as_of": as_of, "source_sha": SHA,
                      "report_sha256": "c" * 64, "watch_count": 1,
                      "observation_count": 1}],
            "predictions": [{"prediction_id": prediction_id, "run_id": ledger_run_id,
                             "as_of": as_of, "pair": pair, "price": 1.0,
                             "baseline_score": 1, "challenger_score": 2, "rank": 1}],
            "observations": [{"run_id": ledger_run_id, "at": as_of,
                              "pair": pair, "price": 1.0}],
            "outcomes": []})
        ledger.verify(state)
        score = {"generation": 1, "ledger_sha256": state["sha256"]}
        latest = {"mode": "PAPER_ONLY", "buy_approved": False, "as_of": as_of}
        result = {"run_id": "1", "source_sha": SHA, "ledger_commit": "b" * 40,
                  "ledger_generation": 1, "ledger_sha256": state["sha256"],
                  "status": "SUCCESS_PAPER_ONLY", "remote_readback_verified": True,
                  "buy_approved": False, "exchange_event_freshness_verified": False,
                  "as_of": as_of, "observed_markets": 1,
                  "candidates": [{"rank": 1, "prediction_id": prediction_id,
                                  "price_usd": 1.0, "baseline_score": 1,
                                  "challenger_score": 2}],
                  "max_client_quote_age_seconds": 7.61}

        def archive(members):
            payload = {name: (json.dumps(value).encode() if not isinstance(value, bytes)
                              else value) for name, value in members.items()}
            sums = "".join(hashlib.sha256(value).hexdigest() + "  " + name + "\n"
                           for name, value in payload.items())
            payload["SHA256SUMS"] = sums.encode()
            buffer = io.BytesIO()
            with zipfile.ZipFile(buffer, "w") as z:
                for name, value in payload.items():
                    z.writestr(name, value)
            raw = buffer.getvalue()
            return raw, "sha256:" + hashlib.sha256(raw).hexdigest()

        lzip, ldigest = archive({"latest.json": latest, "scoreboard.json": score,
                                 "ledger.json": state})
        rzip, rdigest = archive({"results.md": b"PAPER", "results.json": result})
        def check(a=lzip, b=ldigest, c=rzip, d=rdigest):
            return verify_pair(a, b, c, d, run_id=1, source_sha=SHA,
                               ledger_commit="b" * 40)
        proof = check()
        self.assertTrue(proof["artifact_zip_bytes_independently_verified"])
        self.assertEqual(proof["supplied_github_run_origin_status"],
                         "UNVERIFIED_NO_INDEPENDENT_RUN_METADATA")
        self.assertFalse(proof["owner_manual_origin_verified"])
        self.assertEqual(proof["internal_sha256_verified"], 5)
        self.assertFalse(proof["remote_ledger_readback_independently_verified"])
        self.assertFalse(proof["results_delivery_verified"])
        # Optional GitHub run metadata must be separately authenticated by
        # the caller. Even matching dispatch metadata is NOT owner-manual proof.
        authentic = {"id": 1, "head_sha": SHA, "head_branch": "main",
                     "path": ".github/workflows/paper-pipeline.yml",
                     "run_attempt": 1, "status": "completed",
                     "conclusion": "success", "event": "workflow_dispatch"}
        def with_run(metadata):
            return verify_pair(lzip, ldigest, rzip, rdigest, run_id=1,
                               source_sha=SHA, ledger_commit="b" * 40,
                               github_run_metadata=metadata)
        dispatched = with_run(authentic)
        self.assertEqual(dispatched["supplied_github_run_origin_status"],
                         "SUPPLIED_DISPATCH_METADATA_OWNER_ORIGIN_UNKNOWN")
        self.assertFalse(dispatched["owner_manual_origin_verified"])
        scheduled = with_run({**authentic, "event": "schedule"})
        self.assertEqual(scheduled["supplied_github_run_origin_status"],
                         "SUPPLIED_SCHEDULE_METADATA_NOT_CRON_SLOT_ATTESTED")
        self.assertFalse(scheduled["originating_cron_slot_verified"])
        for change in ({"id": True}, {"id": 2},
                       {"head_sha": "f" * 40}, {"head_branch": "research"},
                       {"path": ".github/workflows/other.yml"},
                       {"run_attempt": 2}, {"run_attempt": True},
                       {"status": "in_progress"}, {"conclusion": "failure"},
                       {"event": "push"}):
            with self.subTest(change=change):
                with self.assertRaisesRegex(ValueError, "run provenance mismatch"):
                    with_run({**authentic, **change})
        with self.assertRaisesRegex(ValueError, "run provenance mismatch"):
            with_run("untrusted string")

        with tempfile.TemporaryDirectory() as folder:
            lpath = Path(folder) / "ledger.zip"
            rpath = Path(folder) / "results.zip"
            lpath.write_bytes(lzip)
            rpath.write_bytes(rzip)
            argv = ["artifact_bytes_verify", "--ledger-zip", str(lpath),
                    "--ledger-digest", ldigest, "--results-zip", str(rpath),
                    "--results-digest", rdigest, "--run-id", "1",
                    "--source-sha", SHA, "--ledger-commit", "b" * 40]
            output = io.StringIO()
            with patch("sys.argv", argv), redirect_stdout(output):
                main()
            self.assertIn("PAPER_ARTIFACT_BYTES_READONLY", output.getvalue())
            self.assertIn('"artifact_zip_bytes_independently_verified": true',
                          output.getvalue())
        with self.assertRaisesRegex(ValueError, "ZIP SHA256"):
            check(a=lzip + b"tamper")
        with self.assertRaisesRegex(ValueError, "identity"):
            check(c=archive({"results.md": b"PAPER", "results.json":
                             {**result, "source_sha": "c" * 40}})[0],
                  d=archive({"results.md": b"PAPER", "results.json":
                             {**result, "source_sha": "c" * 40}})[1])
        with self.assertRaisesRegex(ValueError, "missing, extra or duplicate"):
            wrong, digest = archive({"results.md": b"PAPER", "results.json": result,
                                     "extra.txt": b"unexpected"})
            check(c=wrong, d=digest)
        with self.assertRaisesRegex(ValueError, "stale"):
            wrong, digest = archive({"results.md": b"PAPER", "results.json":
                                     {**result, "max_client_quote_age_seconds": 601}})
            check(c=wrong, d=digest)

        # An empty sealed ledger cannot authenticate a successful scan.
        empty = ledger.empty()
        l0, d0 = archive({"latest.json": latest,
                          "scoreboard.json": {"generation": 0, "ledger_sha256": empty["sha256"]},
                          "ledger.json": empty})
        r0, rd0 = archive({"results.md": b"PAPER", "results.json":
                            {**result, "ledger_generation": 0, "ledger_sha256": empty["sha256"]}})
        with self.assertRaisesRegex(ValueError, "identity"):
            check(a=l0, b=d0, c=r0, d=rd0)

        # A prior ledger cannot authenticate a different scan timestamp.
        shifted = "2026-11-02T03:12:00+00:00"
        lwrong, ldwrong = archive({"latest.json": {**latest, "as_of": shifted},
                                   "scoreboard.json": score, "ledger.json": state})
        rwrong, rdwrong = archive({"results.md": b"PAPER", "results.json":
                                   {**result, "as_of": shifted}})
        with self.assertRaisesRegex(ValueError, "identity"):
            check(a=lwrong, b=ldwrong, c=rwrong, d=rdwrong)

        # Sealed results cannot invent a different market observation count.
        rwrong, rdwrong = archive({"results.md": b"PAPER", "results.json":
                                   {**result, "observed_markets": 2}})
        with self.assertRaisesRegex(ValueError, "identity"):
            check(c=rwrong, d=rdwrong)

        # Every reported WATCH must be the latest immutable ledger decision.
        for field, replacement in (("prediction_id", "e" * 64),
                                   ("rank", 2), ("price_usd", 9.0),
                                   ("baseline_score", 99.0),
                                   ("challenger_score", 99.0)):
            with self.subTest(field=field):
                altered = [{**result["candidates"][0], field: replacement}]
                rwrong, rdwrong = archive({"results.md": b"PAPER", "results.json":
                                           {**result, "candidates": altered}})
                with self.assertRaisesRegex(ValueError, "candidate/ledger"):
                    check(c=rwrong, d=rdwrong)
        rwrong, rdwrong = archive({"results.md": b"PAPER", "results.json":
                                   {**result, "candidates": []}})
        with self.assertRaisesRegex(ValueError, "candidate/ledger"):
            check(c=rwrong, d=rdwrong)

    def test_readonly_collects_native_dispatch_and_sha_bound_log_index(self):
        get, calls = fixture()
        result = collect(get, "owner/repo", NOW)
        self.assertEqual(result["report"]["verified_native_count"], 1)
        self.assertEqual(result["report"]["verified_dispatch_count"], 1)
        self.assertEqual(len(result["evidence"]), 2)
        self.assertEqual(len(result["evidence"][0]["decoded_log_sha256"]), 64)
        self.assertFalse(result["evidence"][0]["raw_log_sha256_verified"])
        self.assertEqual(result["evidence"][0]["artifact_metadata_status"],
                         "GITHUB_METADATA_MATCHED_NOT_BYTES")
        self.assertFalse(result["evidence"][0]["artifact_zip_bytes_independently_verified"])
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
        collected = collect(get, "owner/repo", NOW)
        evidence = collected["evidence"][0]
        self.assertEqual(collected["current_remote_ref_evidence"]["status"],
                         "MATCHED_CURRENT_REF_SHA_NOT_LEDGER_BYTES")
        self.assertFalse(collected["current_remote_ref_evidence"]["remote_ledger_bytes_verified"])
        self.assertEqual(evidence["delivery_log_claim_status"],
                         "MATCHED_LOG_MARKERS_NOT_REMOTE_BYTES")
        self.assertEqual((evidence["claimed_generation"], evidence["claimed_watch_count"]), (51, 11))
        self.assertFalse(evidence["remote_ledger_bytes_verified"])
        self.assertFalse(evidence["results_delivery_verified"])

    def test_remote_ref_mismatch_and_unavailable_never_prove_remote_bytes(self):
        base = log("schedule", "9 * * * *")
        marker = ("2026-11-02T03:10:30Z PAPER_LEDGER_REMOTE_READBACK_VERIFIED " +
                  SHA + "\n2026-11-02T03:10:40Z PAPER_RESULTS_VERIFIED 1 51 11\n")
        for mode in ("advanced", "invalid", "unavailable"):
            with self.subTest(mode=mode):
                upstream, calls = fixture(native=[row(1, "schedule")], dispatched=[])
                def altered(path, text=False):
                    if "/logs" in path:
                        return base + marker
                    if path.endswith("/git/ref/heads/paper-proof-ledger"):
                        if mode == "unavailable":
                            raise OSError("read-only endpoint unavailable")
                        if mode == "invalid":
                            return {"ref": "refs/heads/other",
                                    "object": {"sha": SHA, "type": "commit"}}
                        return {"ref": "refs/heads/paper-proof-ledger",
                                "object": {"sha": "b" * 40, "type": "commit"}}
                    return upstream(path, text)
                proof = collect(altered, "owner/repo", NOW)["current_remote_ref_evidence"]
                self.assertEqual(proof["status"],
                                 "UNVERIFIED_REF_DIFFERENT_OR_ADVANCED"
                                 if mode == "advanced" else
                                 "UNVERIFIED_REMOTE_REF_UNAVAILABLE")
                self.assertFalse(proof.get("remote_ledger_bytes_verified", False))

    def test_remote_ref_requires_source_authenticated_writer_not_just_log_claim(self):
        marker = ("2026-11-02T03:10:30Z PAPER_LEDGER_REMOTE_READBACK_VERIFIED " +
                  SHA + "\n2026-11-02T03:10:40Z PAPER_RESULTS_VERIFIED 1 52 5\n")
        for tamper in ("source", "event"):
            with self.subTest(tamper=tamper):
                upstream, calls = fixture(native=[row(1, "schedule")], dispatched=[])
                def altered(path, text=False):
                    value = upstream(path, text)
                    if "/logs" in path:
                        provenance = log("schedule", "9 * * * *")
                        if tamper == "source":
                            provenance = provenance.replace(
                                "PAPER_PIPELINE_SOURCE_SHA=" + SHA,
                                "PAPER_PIPELINE_SOURCE_SHA=" + "b" * 40)
                        else:
                            provenance = provenance.replace(
                                "PAPER_VERIFIED_GITHUB_EVENT=schedule",
                                "PAPER_VERIFIED_GITHUB_EVENT=workflow_dispatch")
                        return provenance + marker
                    return value
                proof = collect(altered, "owner/repo", NOW)
                self.assertEqual(proof["report"]["verified_native_count"], 0)
                self.assertEqual(proof["evidence"][0]["delivery_log_claim_status"],
                                 "MATCHED_LOG_MARKERS_NOT_REMOTE_BYTES")
                self.assertEqual(proof["current_remote_ref_evidence"]["status"],
                                 "UNVERIFIED_NO_SOURCE_AUTHENTICATED_LOG_CLAIM")
                self.assertFalse(any("/git/ref/" in path for path, _ in calls))

    def test_remote_ref_uses_latest_authenticated_not_latest_unverified_claim(self):
        upstream, _ = fixture()
        def altered(path, text=False):
            value = upstream(path, text)
            if "/jobs/101/logs" in path:
                return value + (
                    "2026-11-02T03:10:30Z PAPER_LEDGER_REMOTE_READBACK_VERIFIED " +
                    SHA + "\n2026-11-02T03:10:40Z PAPER_RESULTS_VERIFIED 1 52 5\n")
            if "/jobs/102/logs" in path:
                return value.replace("PAPER_PIPELINE_SOURCE_SHA=" + SHA,
                                     "PAPER_PIPELINE_SOURCE_SHA=" + "b" * 40) + (
                    "2026-11-02T03:10:30Z PAPER_LEDGER_REMOTE_READBACK_VERIFIED " +
                    "b" * 40 + "\n2026-11-02T03:10:40Z PAPER_RESULTS_VERIFIED 2 52 5\n")
            return value
        proof = collect(altered, "owner/repo", NOW)
        self.assertEqual(proof["report"]["verified_native_count"], 1)
        self.assertEqual(proof["report"]["verified_dispatch_count"], 0)
        self.assertEqual(proof["current_remote_ref_evidence"]["claimed_run_id"], 1)
        self.assertEqual(proof["current_remote_ref_evidence"]["status"],
                         "MATCHED_CURRENT_REF_SHA_NOT_LEDGER_BYTES")

    def test_delivery_claim_rejects_reordered_lines_despite_plausible_timestamps(self):
        from datetime import datetime, timezone
        start = datetime(2026, 11, 2, 3, 10, 4, tzinfo=timezone.utc)
        end = datetime(2026, 11, 2, 3, 11, 0, tzinfo=timezone.utc)
        readback = "2026-11-02T03:10:30Z PAPER_LEDGER_REMOTE_READBACK_VERIFIED " + SHA
        result = "2026-11-02T03:10:40Z PAPER_RESULTS_VERIFIED 1 51 11"
        self.assertEqual(
            delivery_log_claim(result + "\n" + readback + "\n", 1, start, end)
            ["delivery_log_claim_status"], "UNVERIFIED")
        self.assertEqual(
            delivery_log_claim(readback + "\n" + result + "\n", 1, start, end)
            ["delivery_log_claim_status"], "MATCHED_LOG_MARKERS_NOT_REMOTE_BYTES")

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

    def test_second_canonical_writer_with_wrong_run_id_blocks_collection(self):
        get, calls = fixture()
        def altered(path, text=False):
            response = get(path, text)
            if "/runs/1/jobs?" in path:
                response["jobs"].append(dict(job(1), id=999, run_id=999))
                response["total_count"] = len(response["jobs"])
            return response
        result = collect(altered, "owner/repo", NOW)
        self.assertEqual(result["report"]["verified_native_count"], 0)
        self.assertEqual(result["report"]["runs"][0]["classification"],
                         "AMBIGUOUS_WRITER_JOB_METADATA")
        self.assertFalse(any("/jobs/101/logs" in path for path, _ in calls))

    def test_authenticated_cross_run_writer_overlap_is_a_bounded_failure(self):
        get, _ = fixture()
        result = collect(get, "owner/repo", NOW)
        proof = result["writer_overlap_evidence"]
        self.assertEqual(proof["status"], "FAILED_OVERLAPPING_CANONICAL_WRITER_JOBS")
        self.assertEqual(proof["authenticated_writer_job_count"], 2)
        self.assertEqual(proof["overlap_pair_count"], 1)
        self.assertEqual(proof["overlaps"][0]["overlap_seconds"], 56)
        self.assertFalse(proof["global_exclusivity_verified"])

    def test_nonoverlap_is_not_global_writer_exclusivity_proof(self):
        get, _ = fixture()
        def changed(path, text=False):
            response = get(path, text)
            if "/runs/2/jobs?" in path:
                response["jobs"][0]["started_at"] = "2026-11-02T03:11:01Z"
                response["jobs"][0]["completed_at"] = "2026-11-02T03:12:00Z"
            if "/jobs/102/logs" in path:
                return response.replace("03:10:06Z", "03:11:06Z")
            return response
        result = collect(changed, "owner/repo", NOW)
        proof = result["writer_overlap_evidence"]
        self.assertEqual(result["report"]["verified_dispatch_count"], 1)
        self.assertEqual(proof["status"], "NO_OVERLAP_OBSERVED_BOUNDED_SAMPLE")
        self.assertEqual(proof["overlap_pair_count"], 0)
        self.assertFalse(proof["global_exclusivity_verified"])

    def test_insufficient_writer_sample_cannot_certify_global_exclusivity(self):
        get, _ = fixture(dispatched=[])
        proof = collect(get, "owner/repo", NOW)["writer_overlap_evidence"]
        self.assertEqual(proof["status"], "UNVERIFIED_INSUFFICIENT_AUTHENTICATED_JOBS")
        self.assertEqual(proof["authenticated_writer_job_count"], 1)
        self.assertFalse(proof["global_exclusivity_verified"])

    def test_incomplete_adjacent_writer_run_blocks_clean_no_overlap_claim(self):
        get, _ = fixture()
        def altered(path, text=False):
            response = get(path, text)
            if "/runs/2/jobs?" in path:
                response["jobs"][0]["conclusion"] = "failure"
            return response
        proof = collect(altered, "owner/repo", NOW)["writer_overlap_evidence"]
        self.assertEqual(proof["status"], "UNVERIFIED_INCOMPLETE_WRITER_COVERAGE")
        self.assertEqual(proof["authenticated_writer_job_count"], 1)
        self.assertEqual(proof["incomplete_writer_run_ids"], [2])
        self.assertFalse(proof["global_exclusivity_verified"])

    def test_reused_canonical_job_id_never_authenticates_distinct_runs(self):
        from paper_pov.cadence_collect import canonical_writer_overlap_evidence
        report = {"runs": [
            {"run_id": 1, "classification": "VERIFIED_NATIVE_SCHEDULE",
             "created_at": "2026-11-02T03:10:01Z"},
            {"run_id": 2, "classification": "VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE",
             "created_at": "2026-11-02T03:10:01Z"}]}
        second = dict(job(2), id=job(1)["id"],
                      started_at="2026-11-02T03:11:01Z",
                      completed_at="2026-11-02T03:12:00Z")
        proof = canonical_writer_overlap_evidence(report, {"1": [job(1)], "2": [second]})
        self.assertEqual(proof["status"], "UNVERIFIED_REUSED_WRITER_JOB_ID")
        self.assertFalse(proof["global_exclusivity_verified"])

    def test_incoherent_writer_job_interval_cannot_claim_no_overlap(self):
        from paper_pov.cadence_collect import canonical_writer_overlap_evidence
        report = {"runs": [{"run_id": 1, "classification": "VERIFIED_NATIVE_SCHEDULE",
                            "created_at": "2026-11-02T03:10:01Z"}]}
        invalid = dict(job(1), started_at="2026-11-02T03:09:00Z")
        proof = canonical_writer_overlap_evidence(report, {"1": [invalid]})
        self.assertEqual(proof["status"], "UNVERIFIED_INVALID_WRITER_INTERVAL")

    def test_malformed_unverified_run_cannot_disappear_from_overlap_coverage(self):
        from paper_pov.cadence_collect import canonical_writer_overlap_evidence
        report = {"runs": [
            {"run_id": 1, "classification": "VERIFIED_NATIVE_SCHEDULE",
             "created_at": "2026-11-02T03:10:01Z"},
            {"run_id": 2, "classification": "VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE",
             "created_at": "2026-11-02T03:10:01Z"},
            {"run_id": None, "classification": "INVALID_RUN_METADATA"}]}
        second = dict(job(2), started_at="2026-11-02T03:11:01Z",
                      completed_at="2026-11-02T03:12:00Z")
        proof = canonical_writer_overlap_evidence(report, {"1": [job(1)], "2": [second]})
        self.assertEqual(proof["status"], "UNVERIFIED_INCOMPLETE_WRITER_COVERAGE")
        self.assertEqual(proof["incomplete_writer_run_count"], 1)
        self.assertEqual(proof["incomplete_writer_run_ids"], [])

    def test_foreign_second_canonical_writer_job_abstains_even_with_matching_first(self):
        from paper_pov.cadence_collect import canonical_writer_overlap_evidence
        report = {"runs": [{"run_id": 1, "classification": "VERIFIED_NATIVE_SCHEDULE",
                            "created_at": "2026-11-02T03:10:01Z"}]}
        forged = dict(job(1), id=999, run_id=999)
        proof = canonical_writer_overlap_evidence(report, {"1": [job(1), forged]})
        self.assertEqual(proof["status"], "UNVERIFIED_INCONSISTENT_WRITER_JOB")
        self.assertFalse(proof["global_exclusivity_verified"])

    def test_failed_canonical_job_overlap_is_detected_without_claiming_duplicate_writes(self):
        upstream, _ = fixture()
        def altered(path, text=False):
            response = upstream(path, text)
            if "/runs/2/jobs?" in path:
                response["jobs"][0]["conclusion"] = "failure"
            return response
        result = collect(altered, "owner/repo", NOW)
        self.assertEqual(result["report"]["verified_dispatch_count"], 0)
        evidence = result["writer_attempt_interval_evidence"]
        self.assertEqual(evidence["status"],
                         "FAILED_OVERLAPPING_GITHUB_CANONICAL_JOB_INTERVALS")
        self.assertEqual(evidence["overlap_pair_count"], 1)
        self.assertEqual(evidence["overlaps"][0]["overlap_seconds"], 56)
        self.assertFalse(evidence["actual_ledger_write_overlap_verified"])

    def test_nonoverlapping_failed_job_does_not_establish_clean_source_provenance(self):
        upstream, _ = fixture()
        def altered(path, text=False):
            response = upstream(path, text)
            if "/runs/2/jobs?" in path:
                response["jobs"][0].update({
                    "conclusion": "failure",
                    "started_at": "2026-11-02T03:11:01Z",
                    "completed_at": "2026-11-02T03:12:00Z"})
            return response
        evidence = collect(altered, "owner/repo", NOW)["writer_attempt_interval_evidence"]
        self.assertEqual(evidence["status"],
                         "UNVERIFIED_SOURCE_PROVENANCE_FOR_JOB_INTERVALS")
        self.assertEqual(evidence["unverified_source_run_ids"], [2])
        self.assertEqual(evidence["overlap_pair_count"], 0)
        self.assertFalse(evidence["global_exclusivity_verified"])

    def test_running_canonical_job_is_read_but_cannot_prove_no_overlap(self):
        upstream, calls = fixture()
        def altered(path, text=False):
            response = upstream(path, text)
            if "event=workflow_dispatch" in path:
                response["workflow_runs"][0]["status"] = "in_progress"
                response["workflow_runs"][0]["conclusion"] = None
            if "/runs/2/jobs?" in path:
                response["jobs"][0].update({
                    "status": "in_progress", "conclusion": None,
                    "completed_at": None})
            return response
        result = collect(altered, "owner/repo", NOW)
        self.assertTrue(any("/runs/2/jobs?" in p for p, _ in calls))
        self.assertFalse(any("/jobs/102/logs" in p for p, _ in calls))
        self.assertEqual(result["writer_attempt_interval_evidence"]["status"],
                         "UNVERIFIED_INCOMPLETE_JOB_INTERVALS")
        self.assertEqual(result["writer_attempt_interval_evidence"]
                         ["unknown_interval_run_ids"], [2])

    def test_attempt_overlap_reused_job_id_is_not_independent_writer_evidence(self):
        from paper_pov.cadence_collect import canonical_writer_attempt_intervals
        report = {"checked_at": NOW, "runs": [
            {"run_id": 1, "classification": "VERIFIED_NATIVE_SCHEDULE",
             "created_at": "2026-11-02T03:10:01Z"},
            {"run_id": 2, "classification": "VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE",
             "created_at": "2026-11-02T03:10:01Z"}]}
        second = dict(job(2), id=job(1)["id"])
        proof = canonical_writer_attempt_intervals(
            report, {"1": [job(1)], "2": [second]})
        self.assertEqual(proof["status"], "UNVERIFIED_INCOMPLETE_JOB_INTERVALS")
        self.assertEqual(proof["unknown_interval_run_ids"], [2])
        self.assertEqual(proof["overlap_pair_count"], 0)

    def test_attempt_overlap_future_completed_job_abstains(self):
        from paper_pov.cadence_collect import canonical_writer_attempt_intervals
        report = {"checked_at": NOW, "runs": [
            {"run_id": 1, "classification": "VERIFIED_NATIVE_SCHEDULE",
             "created_at": "2026-11-02T03:10:01Z"},
            {"run_id": 2, "classification": "VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE",
             "created_at": "2026-11-02T03:10:01Z"}]}
        future = dict(job(2), completed_at="2026-11-02T03:21:00Z")
        proof = canonical_writer_attempt_intervals(
            report, {"1": [job(1)], "2": [future]})
        self.assertEqual(proof["status"], "UNVERIFIED_INCOMPLETE_JOB_INTERVALS")
        self.assertEqual(proof["unknown_interval_run_ids"], [2])
        self.assertFalse(proof["global_exclusivity_verified"])

    def test_ledger_claim_continuity_monotonic_is_not_remote_byte_proof(self):
        from paper_pov.cadence_collect import authenticated_ledger_claim_continuity
        report = {"runs": [
            {"run_id": 1, "classification": "VERIFIED_NATIVE_SCHEDULE",
             "created_at": "2026-11-02T03:00:00Z"},
            {"run_id": 2, "classification": "VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE",
             "created_at": "2026-11-02T03:10:00Z"}]}
        evidence = [
            {"run_id": rid, "claimed_generation": generation,
             "claimed_ledger_commit": SHA,
             "delivery_log_claim_status": "MATCHED_LOG_MARKERS_NOT_REMOTE_BYTES"}
            for rid, generation in ((1, 52), (2, 53))]
        proof = authenticated_ledger_claim_continuity(report, evidence)
        self.assertEqual(proof["status"],
                         "MONOTONIC_AUTHENTICATED_LOG_CLAIMS_NOT_REMOTE_BYTES")
        self.assertEqual(proof["authenticated_claim_count"], 2)
        self.assertFalse(proof["remote_ledger_bytes_verified"])

    def test_ledger_claim_continuity_detects_regression_and_conflicting_same_generation(self):
        from paper_pov.cadence_collect import authenticated_ledger_claim_continuity
        report = {"runs": [
            {"run_id": 1, "classification": "VERIFIED_NATIVE_SCHEDULE",
             "created_at": "2026-11-02T03:00:00Z"},
            {"run_id": 2, "classification": "VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE",
             "created_at": "2026-11-02T03:10:00Z"}]}
        for gen, commit in ((51, SHA), (52, "b" * 40)):
            evidence = [
                {"run_id": 1, "claimed_generation": 52, "claimed_ledger_commit": SHA,
                 "delivery_log_claim_status": "MATCHED_LOG_MARKERS_NOT_REMOTE_BYTES"},
                {"run_id": 2, "claimed_generation": gen, "claimed_ledger_commit": commit,
                 "delivery_log_claim_status": "MATCHED_LOG_MARKERS_NOT_REMOTE_BYTES"}]
            proof = authenticated_ledger_claim_continuity(report, evidence)
            self.assertEqual(proof["status"],
                             "FAILED_CONFLICTING_AUTHENTICATED_LEDGER_CLAIMS")
            self.assertEqual((proof["first_run_id"], proof["second_run_id"]), (1, 2))

    def test_repeated_generation_and_missing_claims_abstain(self):
        from paper_pov.cadence_collect import authenticated_ledger_claim_continuity
        report = {"runs": [
            {"run_id": 1, "classification": "VERIFIED_NATIVE_SCHEDULE",
             "created_at": "2026-11-02T03:00:00Z"},
            {"run_id": 2, "classification": "VERIFIED_WORKFLOW_DISPATCH_NOT_NATIVE",
             "created_at": "2026-11-02T03:10:00Z"}]}
        def entry(rid, gen):
            return {"run_id": rid, "claimed_generation": gen,
                    "claimed_ledger_commit": SHA,
                    "delivery_log_claim_status": "MATCHED_LOG_MARKERS_NOT_REMOTE_BYTES"}
        self.assertEqual(authenticated_ledger_claim_continuity(
            report, [entry(1, 52), entry(2, 52)])["status"],
            "UNVERIFIED_REPEATED_LEDGER_GENERATION")
        self.assertEqual(authenticated_ledger_claim_continuity(
            report, [entry(1, 52), entry(2, 55)])["status"],
            "UNVERIFIED_GENERATION_GAPS")
        self.assertEqual(authenticated_ledger_claim_continuity(
            report, [entry(1, 52)])["status"],
            "UNVERIFIED_INCOMPLETE_AUTHENTICATED_CLAIMS")

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

    def test_artifact_metadata_wrong_identity_and_duplicate_abstain(self):
        get, _ = fixture()
        for change in ("wrong_source", "duplicate", "missing", "wrong_digest", "expired"):
            with self.subTest(change=change):
                def altered(path, text=False):
                    response = get(path, text)
                    if "/artifacts?" in path:
                        rows = response["artifacts"]
                        if change == "wrong_source":
                            rows[0]["workflow_run"]["head_sha"] = "f" * 40
                        elif change == "duplicate":
                            rows[1]["name"] = rows[0]["name"]
                        elif change == "missing":
                            rows.pop()
                            response["total_count"] = len(rows)
                        elif change == "wrong_digest":
                            rows[0]["digest"] = "sha256:not-a-digest"
                        else:
                            rows[0]["expired"] = True
                    return response
                evidence = collect(altered, "owner/repo", NOW)["evidence"]
                self.assertEqual(len(evidence), 2)
                self.assertTrue(all(x["artifact_metadata_status"] == "UNVERIFIED"
                                    for x in evidence if x["run_id"] == 1))

    def test_artifact_metadata_duplicate_id_and_boolean_source_run_id_abstain(self):
        get, _ = fixture()
        for kind in ("duplicate_id", "boolean_source_run_id", "unhashable_artifact_id"):
            with self.subTest(kind=kind):
                def altered(path, text=False):
                    response = get(path, text)
                    if "/artifacts?" in path:
                        if kind == "duplicate_id":
                            response["artifacts"][1]["id"] = response["artifacts"][0]["id"]
                        elif kind == "boolean_source_run_id":
                            response["artifacts"][0]["workflow_run"]["id"] = True
                        else:
                            response["artifacts"][0]["id"] = ["malformed"]
                    return response
                evidence = collect(altered, "owner/repo", NOW)["evidence"]
                self.assertEqual(evidence[0]["artifact_metadata_status"], "UNVERIFIED")
                self.assertFalse(evidence[0].get("artifact_zip_bytes_independently_verified", False))

    def test_artifact_metadata_truncation_abstains(self):
        get, _ = fixture()
        def altered(path, text=False):
            response = get(path, text)
            if "/artifacts?" in path:
                response["total_count"] += 1
            return response
        with self.assertRaisesRegex(ValueError, "artifact metadata page"):
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

    def test_cli_exposes_attempt_and_ledger_claim_failures_without_network_writes(self):
        from paper_pov.cadence_collect import main
        result = {"report": {"runs": [], "verified_native_count": 0},
                  "writer_attempt_interval_evidence": {
                      "status": "FAILED_OVERLAPPING_GITHUB_CANONICAL_JOB_INTERVALS"},
                  "ledger_log_claim_continuity": {
                      "status": "FAILED_CONFLICTING_AUTHENTICATED_LEDGER_CLAIMS"},
                  "writer_overlap_evidence": {"status": "UNVERIFIED"},
                  "current_remote_ref_evidence": {"status": "UNVERIFIED"}}
        args = ["cadence_collect", "--repo", "owner/repo",
                "--checked-at", NOW, "--output", "/tmp/readonly.json"]
        with patch("sys.argv", args), patch(
                "paper_pov.cadence_collect.github_reader", return_value=lambda *a: None), patch(
                "paper_pov.cadence_collect.collect", return_value=result), patch(
                "pathlib.Path.write_text") as write, patch("builtins.print") as output:
            main()
        self.assertEqual(write.call_count, 1)
        messages = [call.args[0] for call in output.call_args_list]
        self.assertEqual(len(messages), 2)
        self.assertTrue(messages[1].startswith("PAPER_RELIABILITY_READONLY "))
        self.assertIn("FAILED_OVERLAPPING_GITHUB_CANONICAL_JOB_INTERVALS", messages[1])
        self.assertIn("FAILED_CONFLICTING_AUTHENTICATED_LEDGER_CLAIMS", messages[1])

    def test_live_rehearsal_workflow_is_get_only_and_has_no_writer(self):
        from pathlib import Path
        workflow = (Path(__file__).resolve().parents[1] / ".github" /
                    "workflows" / "paper-cadence-provenance-ci.yml").read_text()
        self.assertIn("actions: read", workflow)
        self.assertIn("authenticated-get-only-rehearsal:", workflow)
        self.assertIn("'paper_pov/artifact_bytes_verify.py'", workflow)
        self.assertIn("python -m paper_pov.cadence_collect", workflow)
        self.assertIn("--lookback-hours 6 --max-runs 40", workflow)
        self.assertNotIn("gh workflow run", workflow)
        self.assertNotIn("paper-proof-ledger-single-writer", workflow)

    def test_reader_uses_only_get_for_authenticated_evidence(self):
        def fake_open(request, timeout):
            self.assertEqual(request.get_method(), "GET")
            self.assertEqual(timeout, 20)
            return io.BytesIO(b'{"total_count":0,"workflow_runs":[]}')
        with patch("paper_pov.cadence_collect.build_opener") as opener:
            opener.return_value.open.side_effect = fake_open
            result = github_reader("test-readonly-token")(
                "/repos/owner/repo/actions/workflows/paper-pipeline.yml/runs")
            self.assertIsInstance(opener.call_args.args[0], RejectApiRedirect)
        self.assertEqual(result["total_count"], 0)

    def test_authenticated_json_api_redirect_fails_closed_without_token_forwarding(self):
        req = Request("https://api.github.com/repos/owner/repo/actions/runs",
                      headers={"Authorization": "Bearer private-token"})
        for target in ("https://evil.example.com/collect",
                       "https://pipelines.actions.githubusercontent.com/logs?sig=abc",
                       "https://api.github.com/repos/owner/repo/other"):
            with self.subTest(target=target), self.assertRaisesRegex(
                    ValueError, "JSON API redirect"):
                RejectApiRedirect().redirect_request(
                    req, None, 302, "Found", {}, target)

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
