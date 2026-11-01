"""Adversarial no-writer provenance tests for completed PAPER learning trigger."""
import copy
import hashlib
import json
import unittest

from paper_pov import ledger
from paper_pov.learning_trigger import verify_run, select_commit, verify_export, REPO, NAME, PATH
from paper_pov.test_learning_outcomes import fixture


class LearningTriggerTests(unittest.TestCase):
    def setUp(self):
        self.api = {"id": 41337237141, "run_attempt": 1,
                    "head_sha": "a" * 40, "head_branch": "main",
                    "event": "workflow_dispatch", "name": NAME, "path": PATH,
                    "status": "completed", "conclusion": "success",
                    "repository": {"full_name": REPO},
                    "head_repository": {"full_name": REPO}}
        self.event = {"action": "completed", "repository": {"full_name": REPO},
                      "workflow_run": copy.deepcopy(self.api)}

    def valid(self, event=None, api=None, repo=REPO):
        return verify_run(event or self.event, api or self.api, repo, "b" * 40)

    def test_successful_dispatch_and_schedule_are_accepted(self):
        p = self.valid()
        self.assertEqual(p["writer_run_id"], 41337237141)
        self.assertNotEqual(p["learning_source_sha"], p["writer_source_sha"])
        self.api["event"] = self.event["workflow_run"]["event"] = "schedule"
        self.assertEqual(self.valid()["writer_event"], "schedule")

    def test_untrusted_events_and_api_mismatches_fail_closed(self):
        cases = [
            ("event", "action", "requested"), ("api", "conclusion", "failure"),
            ("api", "status", "in_progress"), ("api", "head_branch", "feature"),
            ("api", "event", "pull_request"), ("api", "path", "other.yml"),
            ("api", "name", "Other writer"), ("api", "head_sha", "bad"),
            ("api", "run_attempt", 0), ("api", "id", 0)]
        for obj, field, value in cases:
            with self.subTest(obj=obj, field=field):
                e, a = copy.deepcopy(self.event), copy.deepcopy(self.api)
                (e if obj == "event" else a)[field] = value
                with self.assertRaises(ValueError):
                    verify_run(e, a, REPO, "b" * 40)
        for field in ("repository", "head_repository"):
            a = copy.deepcopy(self.api)
            a[field]["full_name"] = "attacker/fork"
            with self.assertRaises(ValueError):
                verify_run(self.event, a, REPO, "b" * 40)
        with self.assertRaises(ValueError):
            self.valid(repo="attacker/fork")
        with self.assertRaises(ValueError):
            verify_run(self.event, self.api, REPO, "not-a-sha")

    def test_exact_immutable_ledger_commit_selection(self):
        p = self.valid()
        subject = "paper: atomic packed scan 41337237141 source " + "a" * 40
        lines = "c" * 40 + " " + subject + "\n" + "d" * 40 + " unrelated"
        self.assertEqual(select_commit(lines, p), "c" * 40)
        with self.assertRaises(ValueError):
            select_commit(lines + "\n" + "e" * 40 + " " + subject, p)
        with self.assertRaises(ValueError):
            select_commit("c" * 40 + " paper: atomic packed scan 1 source " + "a" * 40, p)

    def test_export_requires_seal_generation_and_exact_source(self):
        state = fixture(list(range(0, 21 * 30, 30)))
        p = self.valid()
        m = {"head": {"generation": state["generation"],
                      "ledger_sha256": state["sha256"]}}
        self.assertEqual(verify_export(state, m, p)["generation"], 21)
        bad = copy.deepcopy(state)
        bad["runs"][-1]["source_sha"] = "f" * 40
        ledger.seal(bad)
        with self.assertRaises(ValueError):
            verify_export(bad, m, p)
        with self.assertRaises(ValueError):
            verify_export(state, {"head": {"generation": 20, "ledger_sha256": state["sha256"]}}, p)
        with self.assertRaises(ValueError):
            verify_export(state, {"head": {"generation": 21, "ledger_sha256": "0" * 64}}, p)
        bad = copy.deepcopy(state)
        bad["sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            verify_export(bad, m, p)


if __name__ == "__main__":
    unittest.main()
