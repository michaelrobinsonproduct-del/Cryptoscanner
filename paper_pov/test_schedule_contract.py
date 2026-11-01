"""Fail-closed paper scanner cron provenance and single-writer contract.

These static contracts run before any live ledger write; they deliberately do
not claim GitHub will deliver every scheduled event.
"""
import re
import unittest
from pathlib import Path

WORKFLOW = (Path(__file__).resolve().parents[1] /
            ".github/workflows/paper-pipeline.yml")


class PaperCronAttributionContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = WORKFLOW.read_text()

    def test_exact_two_slots_on_same_workflow(self):
        cron = re.findall(r"^\s+- cron: '([^']+)'\s*$", self.text, re.M)
        self.assertEqual(cron, ["9 * * * *", "39 * * * *"])
        self.assertEqual(self.text.count("  schedule:\n"), 1)
        self.assertEqual(self.text.count("  workflow_dispatch:\n"), 1)

    def test_single_non_cancelling_writer_lock(self):
        self.assertEqual(
            self.text.count("group: public-paper-proof-ledger-single-writer"), 1)
        self.assertIn("cancel-in-progress: false", self.text)
        self.assertIn("github.ref == 'refs/heads/main'", self.text)
        self.assertIn("github.event_name == 'schedule'", self.text)
        self.assertIn("github.event_name == 'workflow_dispatch'", self.text)

    def test_originating_cron_is_checked_before_tests_and_mutation(self):
        marker = "name: Fail-closed originating schedule provenance"
        self.assertEqual(self.text.count(marker), 1)
        self.assertLess(self.text.index(marker),
                        self.text.index("name: Exact commit tests before any ledger mutation"))
        self.assertLess(self.text.index(marker),
                        self.text.index("name: Non-force, single-writer ledger push"))
        self.assertIn("PAPER_GITHUB_EVENT: ${{ github.event_name }}", self.text)
        self.assertIn("PAPER_CRON_EXPRESSION: ${{ github.event.schedule }}", self.text)
        self.assertIn("'9 * * * *'|'39 * * * *'", self.text)
        self.assertIn("PAPER_UNRECOGNIZED_ORIGINATING_CRON", self.text)
        self.assertIn("PAPER_UNRECOGNIZED_GITHUB_EVENT", self.text)
        self.assertIn("PAPER_MANUAL_WITH_SCHEDULE_PAYLOAD", self.text)

    def test_immutable_ledger_and_results_steps_still_present(self):
        for marker in (
            "Restore checksum-sealed existing ledger",
            "Real bounded public Kraken scan (paper only)",
            "Cross-run nonregression and provenance acceptance",
            "Non-force, single-writer ledger push and remote readback",
            "Preserve public human-readable paper results",
            "Publish explicit failed-run paper results",
        ):
            self.assertIn(marker, self.text)


if __name__ == "__main__":
    unittest.main()
