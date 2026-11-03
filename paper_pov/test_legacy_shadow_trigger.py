"""Adversarial offline owner fallback tests; no GitHub calls or ledger writes."""
import copy
import datetime as dt
import json
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch

from paper_pov import legacy_shadow_trigger as gate

NOW = dt.datetime(2026, 11, 1, 19, 35, tzinfo=dt.timezone.utc)
SHA = "a" * 40
WRITER_ID = 41300000000
CURRENT_ID = 41300001000


def iso(minutes):
    return (NOW + dt.timedelta(minutes=minutes)).isoformat().replace("+00:00", "Z")


def fixture():
    event = {"action": "created", "repository": {"full_name": gate.REPO,
             "default_branch": "main"}, "issue": {"number": 34},
             "comment": {"body": gate.COMMAND, "created_at": iso(-1),
                         "user": {"login": gate.OWNER, "id": gate.OWNER_ID},
                         "author_association": "OWNER"},
             "sender": {"login": gate.OWNER, "id": gate.OWNER_ID}}
    writer = {"id": WRITER_ID, "name": gate.PAPER, "path": gate.PAPER_PATH,
              "repository": {"full_name": gate.REPO}, "head_branch": "main",
              "head_sha": SHA, "run_attempt": 1, "event": "workflow_dispatch",
              "status": "completed", "conclusion": "success",
              "created_at": iso(-7), "updated_at": iso(-3)}
    state = {"generation": 35, "sha256": "b" * 64, "runs": [{"source_sha": SHA}]}
    manifest = {"head": {"generation": 35, "ledger_sha256": "b" * 64}}
    return dict(event=event, paper_runs={"workflow_runs": [writer]},
                shadow_runs={"workflow_runs": []}, state=state, manifest=manifest,
                ledger_message=f"paper: atomic packed scan {WRITER_ID} source {SHA}",
                repository=gate.REPO, current_run_id=CURRENT_ID,
                checkout_sha=SHA, now=NOW)


def decide(**changes):
    f = fixture()
    f.update(changes)
    with patch.object(gate.ledger, "verify") as verified:
        result = gate.decide(**f)
        if result["action"] == "RUN_SHADOW":
            verified.assert_called_once()
        return result


class OwnerFallbackTests(unittest.TestCase):
    def test_cli_atomic_decision_and_stale_authorization_removal(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            f = fixture()
            names = {
                "event": "event.json", "paper_runs": "paper.json",
                "shadow_runs": "shadow.json", "state": "ledger.json",
                "manifest": "manifest.json",
            }
            for key, filename in names.items():
                (root / filename).write_text(json.dumps(f[key]))
            (root / "message.txt").write_text(f["ledger_message"])
            output = root / "decision.json"
            argv = []
            for flag, filename in (
                ("event", names["event"]), ("paper-runs", names["paper_runs"]),
                ("shadow-runs", names["shadow_runs"]), ("ledger", names["state"]),
                ("manifest", names["manifest"]), ("ledger-message", "message.txt"),
            ):
                argv.extend(["--" + flag, str(root / filename)])
            argv.extend(["--repository", gate.REPO, "--current-run-id", str(CURRENT_ID),
                         "--checkout-sha", SHA, "--output", str(output)])
            with patch.object(gate.ledger, "verify"):
                gate.main(argv, now=NOW)
            self.assertEqual(json.loads(output.read_text())["action"], "RUN_SHADOW")
            # A failed second invocation must remove stale authorization.
            (root / names["event"]).write_text("{broken json")
            with self.assertRaises(json.JSONDecodeError):
                gate.main(argv)
            self.assertFalse(output.exists())
            # An ambiguous run history must publish a complete ABSTAIN decision.
            (root / names["event"]).write_text(json.dumps(f["event"]))
            shadow = {"workflow_runs": [{"id": []}]}
            (root / names["shadow_runs"]).write_text(json.dumps(shadow))
            with patch.object(gate.ledger, "verify"):
                gate.main(argv, now=NOW)
            self.assertEqual(json.loads(output.read_text())["action"], "ABSTAIN")

    def test_valid_completed_sealed_dispatch_and_native(self):
        self.assertEqual(decide()["action"], "RUN_SHADOW")
        f = fixture()
        f["paper_runs"]["workflow_runs"][0]["event"] = "schedule"
        self.assertEqual(decide(**f)["action"], "RUN_SHADOW")

    def test_owner_command_must_be_exact_and_authenticated(self):
        for key, value in [("body", "/paper-cadence-heartbeat"),
                           ("author_association", "COLLABORATOR")]:
            f = fixture()
            f["event"]["comment"][key] = value
            with self.assertRaisesRegex(ValueError, "Unauthenticated"):
                decide(**f)
        f = fixture()
        f["event"]["sender"]["id"] = 1
        with self.assertRaisesRegex(ValueError, "Unauthenticated"):
            decide(**f)

    def test_shared_owner_identity_rejects_boolean_and_string_ids(self):
        # Python bool compares equal to 1; GitHub identity must be an exact integer.
        for role in ("sender", "comment"):
            for bad in (True, str(gate.OWNER_ID), None):
                f = fixture()
                identity = f["event"]["sender"] if role == "sender" else f["event"]["comment"]["user"]
                identity["id"] = bad
                with self.assertRaisesRegex(ValueError, "Unauthenticated"):
                    decide(**f)

    def test_wrong_issue_repository_and_pr_abstain(self):
        for change in ("number", "repository", "pull_request"):
            f = fixture()
            if change == "number":
                f["event"]["issue"]["number"] = 35
            elif change == "repository":
                f["event"]["repository"]["full_name"] = "attacker/fork"
            else:
                f["event"]["issue"]["pull_request"] = {"url": "x"}
            with self.assertRaises(ValueError):
                decide(**f)

    def test_stale_or_future_command(self):
        for m in (-12, 1):
            f = fixture()
            f["event"]["comment"]["created_at"] = iso(m)
            self.assertEqual(decide(**f)["action"], "ABSTAIN")

    def test_latest_writer_must_be_successful_and_finished(self):
        for status, conclusion in [("queued", None), ("in_progress", None),
                                   ("completed", "failure")]:
            f = fixture()
            f["paper_runs"]["workflow_runs"][0].update(
                status=status, conclusion=conclusion)
            self.assertEqual(decide(**f)["action"], "ABSTAIN")

    def test_newer_active_writer_blocks(self):
        f = fixture()
        newer = copy.deepcopy(f["paper_runs"]["workflow_runs"][0])
        newer.update(id=WRITER_ID + 1, created_at=iso(-2),
                     status="in_progress", conclusion=None)
        # GitHub returns newest-first; the active writer must be first.
        f["paper_runs"]["workflow_runs"].insert(0, newer)
        self.assertEqual(decide(**f)["reason"], "ACTIVE_OR_AMBIGUOUS_WRITER")

    def test_writer_source_and_id_must_match_latest_commit(self):
        for bad in ["paper: atomic packed scan 123 source " + SHA,
                    f"paper: atomic packed scan {WRITER_ID} source " + "c" * 40]:
            f = fixture()
            f["ledger_message"] = bad
            self.assertEqual(decide(**f)["reason"],
                             "LATEST_LEDGER_WRITER_IDENTITY_MISMATCH")

    def test_seal_and_source_mismatch_block(self):
        for what in ("source", "sha", "generation"):
            f = fixture()
            if what == "source":
                f["state"]["runs"][-1]["source_sha"] = "c" * 40
            elif what == "sha":
                f["manifest"]["head"]["ledger_sha256"] = "0" * 64
            else:
                f["manifest"]["head"]["generation"] = 34
            self.assertEqual(decide(**f)["reason"],
                             "SEALED_LEDGER_SOURCE_OR_SHA_MISMATCH")

    def test_shadow_native_or_fallback_already_started_blocks(self):
        for event in ("workflow_run", "issue_comment"):
            f = fixture()
            f["shadow_runs"]["workflow_runs"] = [{
                "id": CURRENT_ID + 1, "name": gate.SHADOW,
                "path": gate.SHADOW_PATH, "repository": {"full_name": gate.REPO},
                "created_at": iso(-5), "event": event,
                "status": "completed", "conclusion": "success"}]
            self.assertEqual(decide(**f)["reason"],
                             "SHADOW_ALREADY_TRIGGERED_OR_IN_PROGRESS")

    def test_skipped_unrelated_issue_comment_does_not_suppress_fallback(self):
        f = fixture()
        f["shadow_runs"]["workflow_runs"] = [{
            "id": CURRENT_ID + 1, "name": gate.SHADOW,
            "path": gate.SHADOW_PATH, "repository": {"full_name": gate.REPO},
            "created_at": iso(-2), "event": "issue_comment",
            "status": "completed", "conclusion": "skipped"}]
        self.assertEqual(decide(**f)["action"], "RUN_SHADOW")
        # Skipped unrelated comments may be interleaved with older native runs.
        f["shadow_runs"]["workflow_runs"].append({
            "id": CURRENT_ID + 2, "name": gate.SHADOW,
            "path": gate.SHADOW_PATH, "repository": {"full_name": gate.REPO},
            "created_at": iso(-8), "event": "workflow_run",
            "status": "completed", "conclusion": "success"})
        self.assertEqual(decide(**f)["action"], "RUN_SHADOW")

    def test_live_or_actual_comment_fallback_still_blocks(self):
        for status, conclusion in [
            ("queued", None), ("in_progress", None),
            ("completed", "success"), ("completed", "failure"),
            ("completed", "cancelled")]:
            f = fixture()
            f["shadow_runs"]["workflow_runs"] = [{
                "id": CURRENT_ID + 1, "name": gate.SHADOW,
                "path": gate.SHADOW_PATH, "repository": {"full_name": gate.REPO},
                "created_at": iso(-2), "event": "issue_comment",
                "status": status, "conclusion": conclusion}]
            self.assertEqual(decide(**f)["reason"],
                             "SHADOW_ALREADY_TRIGGERED_OR_IN_PROGRESS")

    def test_native_shadow_even_if_skipped_still_blocks(self):
        f = fixture()
        f["shadow_runs"]["workflow_runs"] = [{
            "id": CURRENT_ID + 1, "name": gate.SHADOW,
            "path": gate.SHADOW_PATH, "repository": {"full_name": gate.REPO},
            "created_at": iso(-2), "event": "workflow_run",
            "status": "completed", "conclusion": "skipped"}]
        self.assertEqual(decide(**f)["reason"],
                         "SHADOW_ALREADY_TRIGGERED_OR_IN_PROGRESS")

    def test_partial_shadow_page_duplicate_or_unsorted_fails_closed(self):
        f = fixture()
        row = {"id": CURRENT_ID + 1, "name": gate.SHADOW,
               "path": gate.SHADOW_PATH,
               "repository": {"full_name": gate.REPO},
               "created_at": iso(-2), "event": "issue_comment",
               "status": "completed", "conclusion": "skipped"}
        f["shadow_runs"]["workflow_runs"] = [copy.deepcopy(row), copy.deepcopy(row)]
        self.assertEqual(decide(**f)["reason"], "DUPLICATE_OR_INVALID_SHADOW_RUN_ID")
        f["shadow_runs"]["workflow_runs"][1]["id"] += 1
        f["shadow_runs"]["workflow_runs"][1]["created_at"] = iso(-1)
        self.assertEqual(decide(**f)["reason"], "UNSORTED_SHADOW_HISTORY")
        f["shadow_runs"]["workflow_runs"][1]["created_at"] = iso(-3)
        self.assertEqual(decide(**f)["action"], "RUN_SHADOW")

    def test_unknown_shadow_event_fails_closed(self):
        f = fixture()
        f["shadow_runs"]["workflow_runs"] = [{
            "id": CURRENT_ID + 1, "name": gate.SHADOW,
            "path": gate.SHADOW_PATH, "repository": {"full_name": gate.REPO},
            "created_at": iso(-2), "event": "workflow_dispatch",
            "status": "completed", "conclusion": "success"}]
        self.assertEqual(decide(**f)["reason"], "UNEXPECTED_SHADOW_EVENT")

    def test_owner_comment_workflow_concurrency_is_unique(self):
        from pathlib import Path
        workflow = Path(".github/workflows/paper-legacy-shadow.yml").read_text()
        self.assertIn("github.event.comment.id", workflow)
        self.assertIn("github.event.workflow_run.id", workflow)
        self.assertIn("cancel-in-progress: false", workflow)

    def test_current_fallback_excluded_from_shadow_history(self):
        f = fixture()
        f["shadow_runs"]["workflow_runs"] = [{
            "id": CURRENT_ID, "name": gate.SHADOW,
            "path": gate.SHADOW_PATH, "repository": {"full_name": gate.REPO},
            "created_at": iso(0), "status": "in_progress"}]
        self.assertEqual(decide(**f)["action"], "RUN_SHADOW")

    def test_old_writer_cannot_be_replayed(self):
        f = fixture()
        f["paper_runs"]["workflow_runs"][0]["updated_at"] = iso(-27)
        self.assertEqual(decide(**f)["action"], "ABSTAIN")

    def test_pagination_ambiguity_blocks(self):
        f = fixture()
        f["shadow_runs"]["workflow_runs"] = [{
            "id": CURRENT_ID, "created_at": iso(0)}] * 100
        self.assertEqual(decide(**f)["reason"], "DUPLICATE_OR_INVALID_SHADOW_RUN_ID")
        f = fixture()
        f["paper_runs"]["workflow_runs"] *= 100
        self.assertEqual(decide(**f)["reason"], "DUPLICATE_OR_INVALID_WRITER_RUN_ID")

    def test_completed_premerge_feature_branch_writer_is_not_a_live_writer(self):
        f = fixture()
        old = copy.deepcopy(f["paper_runs"]["workflow_runs"][0])
        old.update(id=WRITER_ID - 1, head_branch="proof-of-value-paper-20261031",
                   event="push", created_at=iso(-20), updated_at=iso(-19))
        f["paper_runs"]["workflow_runs"].append(old)
        self.assertEqual(decide(**f)["action"], "RUN_SHADOW")
        # A historical branch run cannot be allowed to hide an active writer.
        old.update(status="in_progress", conclusion=None)
        self.assertEqual(decide(**f)["reason"], "ACTIVE_OR_AMBIGUOUS_WRITER")

    def test_latest_writer_must_still_be_on_main(self):
        f = fixture()
        f["paper_runs"]["workflow_runs"][0]["head_branch"] = "proof-of-value-paper-20261031"
        self.assertEqual(decide(**f)["reason"], "UNTRUSTED_WRITER_RUN_HISTORY")

    def test_historical_writer_repository_and_workflow_identity_still_strict(self):
        for field, value in (("name", "Other Workflow"),
                             ("path", ".github/workflows/other.yml"),
                             ("repository", {"full_name": "attacker/fork"})):
            f = fixture()
            old = copy.deepcopy(f["paper_runs"]["workflow_runs"][0])
            old.update(id=WRITER_ID - 1, head_branch="old-feature",
                       event="push", created_at=iso(-20), updated_at=iso(-19))
            old[field] = value
            f["paper_runs"]["workflow_runs"].append(old)
            self.assertEqual(decide(**f)["reason"], "UNTRUSTED_WRITER_RUN_HISTORY")

    def test_full_writer_page_with_completed_feature_branch_tail(self):
        f = fixture()
        latest = f["paper_runs"]["workflow_runs"][0]
        for n in range(1, 100):
            old = copy.deepcopy(latest)
            old.update(id=WRITER_ID - n, created_at=iso(-7 - n),
                       updated_at=iso(-3 - n))
            if n >= 40:
                old.update(head_branch="proof-of-value-paper-20261031", event="push")
            f["paper_runs"]["workflow_runs"].append(old)
        self.assertEqual(decide(**f)["action"], "RUN_SHADOW")
        # A non-main historical run is safe only if it has truly finished.
        f["paper_runs"]["workflow_runs"][-1]["status"] = "queued"
        self.assertEqual(decide(**f)["reason"], "ACTIVE_OR_AMBIGUOUS_WRITER")

    def test_full_writer_page_with_unique_ordered_history_is_usable(self):
        f = fixture()
        latest = f["paper_runs"]["workflow_runs"][0]
        older = []
        for n in range(1, 100):
            run = copy.deepcopy(latest)
            run["id"] = WRITER_ID - n
            run["created_at"] = iso(-7 - n)
            run["updated_at"] = iso(-3 - n)
            older.append(run)
        f["paper_runs"]["workflow_runs"].extend(older)
        self.assertEqual(decide(**f)["action"], "RUN_SHADOW")
        f["paper_runs"]["workflow_runs"][1], f["paper_runs"]["workflow_runs"][2] = (
            f["paper_runs"]["workflow_runs"][2], f["paper_runs"]["workflow_runs"][1])
        self.assertEqual(decide(**f)["reason"], "UNSORTED_WRITER_HISTORY")

    def test_full_shadow_page_must_cover_entire_writer_window(self):
        f = fixture()
        latest_skipped = {
            "id": CURRENT_ID + 1, "name": gate.SHADOW,
            "path": gate.SHADOW_PATH, "repository": {"full_name": gate.REPO},
            "created_at": iso(-2), "event": "issue_comment",
            "status": "completed", "conclusion": "skipped"}
        history = [latest_skipped]
        for n in range(99):
            old = copy.deepcopy(latest_skipped)
            old["id"] = CURRENT_ID - 1 - n
            old["created_at"] = iso(-8 - n)
            history.append(old)
        f["shadow_runs"]["workflow_runs"] = history
        self.assertEqual(decide(**f)["action"], "RUN_SHADOW")
        for old in history[1:]:
            old["created_at"] = iso(-2)
        self.assertEqual(decide(**f)["reason"], "SHADOW_PAGINATION_AMBIGUITY")
        history[1]["created_at"] = iso(-1)
        self.assertEqual(decide(**f)["reason"], "UNSORTED_SHADOW_HISTORY")

    def test_invalid_clock_and_utc_timestamp_rejected(self):
        f = fixture()
        f["event"]["comment"]["created_at"] = "2026-11-01T19:34:00"
        with self.assertRaisesRegex(ValueError, "UTC"):
            decide(**f)
        f = fixture()
        f["now"] = dt.datetime(2026, 11, 1, 19, 35)
        with self.assertRaisesRegex(ValueError, "clock"):
            decide(**f)

    def test_corrupted_ledger_is_never_accepted(self):
        f = fixture()
        with patch.object(gate.ledger, "verify", side_effect=ValueError("bad seal")):
            with self.assertRaisesRegex(ValueError, "bad seal"):
                gate.decide(**f)



    def test_malformed_history_abstains_instead_of_crashing(self):
        for kind in ("paper_runs", "shadow_runs"):
            for malformed in ({"id": []}, {"id": True}, {"id": 0},
                              {"id": 999, "created_at": "invalid"}, None):
                f = fixture()
                f[kind]["workflow_runs"].append(malformed)
                result = decide(**f)
                self.assertEqual(result["action"], "ABSTAIN")
                self.assertIn(result["reason"], (
                    "DUPLICATE_OR_INVALID_WRITER_RUN_ID",
                    "DUPLICATE_OR_INVALID_SHADOW_RUN_ID",
                    "UNSORTED_WRITER_HISTORY", "UNSORTED_SHADOW_HISTORY"))

    def test_partial_history_valid_skipped_shadow_still_allows_fallback(self):
        f = fixture()
        f["shadow_runs"]["workflow_runs"] = [
            {"id": CURRENT_ID + 3, "name": gate.SHADOW,
             "path": gate.SHADOW_PATH, "repository": {"full_name": gate.REPO},
             "created_at": iso(-2), "event": "issue_comment",
             "status": "completed", "conclusion": "skipped"},
            {"id": CURRENT_ID + 2, "name": gate.SHADOW,
             "path": gate.SHADOW_PATH, "repository": {"full_name": gate.REPO},
             "created_at": iso(-8), "event": "workflow_run",
             "status": "completed", "conclusion": "success"}]
        self.assertEqual(decide(**f)["action"], "RUN_SHADOW")

if __name__ == "__main__":
    unittest.main()
