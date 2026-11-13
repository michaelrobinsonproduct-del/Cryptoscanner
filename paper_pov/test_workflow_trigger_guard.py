"""Guard the one-writer stage-1 paper scan event and main-only execution contract."""
import re
import unittest
from pathlib import Path

PIPELINE = Path(__file__).resolve().parents[1] / ".github/workflows/paper-pipeline.yml"


class MainOnlyPaperTriggerTests(unittest.TestCase):
    def test_schedule_dispatch_and_authenticated_request_trigger_same_writer(self):
        text = PIPELINE.read_text()
        events = text.split("\npermissions:", 1)[0]
        self.assertIn("\n  workflow_dispatch:", events)
        self.assertIn("\n  schedule:", events)
        self.assertIn("\n  push:", events)
        self.assertIn("branches: [main]", events)
        self.assertIn("\'.github/paper-scan-request.txt\'", events)
        self.assertNotIn("\n  issue_comment:", events)
        self.assertNotIn("types: [created]", events)
        for forbidden in ("pull_request:", "repository_dispatch:"):
            self.assertNotIn(forbidden, events)

    def test_job_runs_only_from_default_main_ref(self):
        text = PIPELINE.read_text()
        self.assertIn(
            "if: github.ref == 'refs/heads/main' && "
            "(github.event_name == 'schedule' || github.event_name == 'workflow_dispatch' || github.event_name == 'push')",
            text,
        )
        self.assertEqual(text.count("if: github.ref == 'refs/heads/main'"), 1)

    def test_path_scoped_push_is_verified_before_any_ledger_mutation(self):
        text = PIPELINE.read_text()
        self.assertIn("fetch-depth: 2", text)
        self.assertIn("CHANGED=", text)
        self.assertIn("git diff-tree --no-commit-id --name-only -r", text)
        self.assertIn("PAPER_PUSH_REQUEST_UNAUTHORIZED_FILES", text)
        self.assertIn("PAPER_PUSH_REQUEST_VERIFIED", text)
        self.assertIn("PAPER_PUSH_REQUEST_EMPTY", text)
        self.assertLess(text.index("PAPER_PUSH_REQUEST_VERIFIED"),
                        text.index("Restore checksum-sealed existing ledger"))

    def test_twice_hourly_schedule_and_single_writer_unchanged(self):
        text = PIPELINE.read_text()
        self.assertEqual(re.findall(r"(?m)^\s*-\s*cron:\s*['\"]([^'\"]+)['\"]", text), ["20,50 * * * *"])
        self.assertIn("group: public-paper-proof-ledger-single-writer", text)
        self.assertIn("cancel-in-progress: false", text)
        self.assertEqual(text.count("git push origin HEAD:refs/heads/paper-proof-ledger"), 1)
        self.assertIn("PAPER_CANONICAL_RESULTS_REMOTE_READBACK_VERIFIED", text)
        self.assertIn("LEDGER_CONCURRENT_UPDATE_ABORT", text)
        self.assertIn("--publication-dir /tmp/paper-output/results", text)
        self.assertIn("--atomic-publication", text)
        self.assertIn("PAPER_LEDGER_REMOTE_READBACK_VERIFIED", text)
        self.assertIn("Render sealed results BEFORE the single atomic publication", text)

    def test_dispatch_is_paper_only_and_has_no_second_writer(self):
        text = PIPELINE.read_text()
        self.assertIn("python -m paper_pov.scanner", text)
        self.assertIn("PAPER_RESULTS_VERIFIED", (PIPELINE.parents[2] / "paper_pov/results_report.py").read_text())
        self.assertNotIn("git push --force", text)
        self.assertNotIn("railway", text.lower())


    def test_exact_writer_dispatches_existing_read_only_learning_after_publication(self):
        text = PIPELINE.read_text()
        learning = (PIPELINE.parent / "paper-ledger-learning.yml").read_text()
        dispatch = "actions/workflows/paper-ledger-learning.yml/dispatches"
        self.assertEqual(text.count(dispatch), 1)
        self.assertIn("  actions: write", text)
        self.assertLess(text.index("PAPER_CANONICAL_RESULTS_REMOTE_READBACK_VERIFIED"),
                        text.index(dispatch))
        self.assertNotIn('-X POST "repos/${GITHUB_REPOSITORY}/issues/34/comments"', text)
        self.assertIn('inputs[paper_run_id]=${GITHUB_RUN_ID}', text)
        self.assertIn("PAPER_READ_ONLY_LEARNING_DISPATCH_FAILED", text)
        self.assertNotIn("  workflow_run:", learning)
        self.assertIn("  workflow_dispatch:", learning)
        self.assertIn("  contents: read", learning)
        self.assertNotIn("  contents: write", learning)
        self.assertNotIn("git push", learning)
        legacy = (PIPELINE.parent / "paper-legacy-shadow.yml").read_text()
        legacy_dispatch = "actions/workflows/paper-legacy-shadow.yml/dispatches"
        self.assertEqual(text.count(legacy_dispatch), 1)
        self.assertLess(text.index("PAPER_CANONICAL_RESULTS_REMOTE_READBACK_VERIFIED"),
                        text.index(legacy_dispatch))
        self.assertIn('inputs[paper_run_id]=${GITHUB_RUN_ID}', text)
        self.assertIn("PAPER_READ_ONLY_LEGACY_DISPATCH_FAILED", text)
        self.assertNotIn("  workflow_run:", legacy)
        self.assertIn("  workflow_dispatch:", legacy)
        self.assertIn("  contents: read", legacy)
        self.assertNotIn("  contents: write", legacy)
        self.assertNotIn("git push", legacy)


if __name__ == "__main__":
    unittest.main()
