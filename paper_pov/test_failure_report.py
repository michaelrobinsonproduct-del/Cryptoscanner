"""Deterministic failure-only public paper report contracts; no network."""
import datetime as dt
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from failure_report import render_failure, write_failure

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/paper-pipeline.yml"
SHA = "a" * 40


class FailureReportTests(unittest.TestCase):
    def test_fail_closed_and_never_invent_success_or_prices(self):
        data, md = render_failure("41254358695", SHA,
            dt.datetime(2026, 10, 31, 23, 58, tzinfo=dt.timezone.utc))
        self.assertEqual(data["status"], "FAILED_PAPER_ONLY")
        self.assertEqual(data["candidates"], [])
        self.assertIsNone(data["ledger_generation"])
        self.assertIsNone(data["ledger_remote_readback_verified"])
        self.assertTrue(data["ledger_may_have_been_committed"])
        self.assertIsNone(data["market_freshness_seconds"])
        self.assertIsNone(data["eligible_pairs"])
        self.assertIsNone(data["held_out_lift"])
        self.assertFalse(data["buy_approved"])
        self.assertFalse(data["production_applied"])
        self.assertEqual(set(data["horizons"]), {"1", "6", "24", "48"})
        self.assertTrue(all(v["status"] == "NOT_VERIFIED" for v in data["horizons"].values()))
        self.assertIn("FAILED run", md)
        self.assertIn("inspect the remote ledger before any retry", md)

    def test_durable_checksums_and_utc(self):
        with tempfile.TemporaryDirectory() as tmp:
            data = write_failure(tmp, "1", SHA,
                dt.datetime(2026, 10, 31, 19, 58,
                            tzinfo=dt.timezone(dt.timedelta(hours=-4))))
            self.assertEqual(data["as_of"], "2026-10-31T23:58:00+00:00")
            files = Path(tmp)
            for line in (files / "SHA256SUMS").read_text().splitlines():
                digest, name = line.split("  ")
                self.assertEqual(hashlib.sha256((files / name).read_bytes()).hexdigest(), digest)
            self.assertEqual(json.loads((files / "results.json").read_text())["run_id"], "1")

    def test_rejects_untrusted_ids_and_naive_time(self):
        for run_id, sha in [("0", SHA), ("1; echo bad", SHA), ("1", "A" * 40),
                            ("1", "bad"), ("-1", SHA)]:
            with self.assertRaises(ValueError):
                render_failure(run_id, sha)
        with self.assertRaises(ValueError):
            render_failure("1", SHA, dt.datetime(2026, 10, 31))

    def test_workflow_failure_reporting_does_not_create_second_writer(self):
        text = WORKFLOW.read_text()
        self.assertIn("Publish explicit failed-run paper results", text)
        self.assertIn("public-paper-failure-", text)
        self.assertIn("paper_pov/failure_report.py", text)
        self.assertIn("sha256sum -c SHA256SUMS", text)
        self.assertIn("PAPER_FAILURE_ISSUE_READBACK_VERIFIED", text)
        self.assertEqual(text.count("git push origin HEAD:refs/heads/paper-proof-ledger"), 1)
        self.assertIn("group: public-paper-proof-ledger-single-writer", text)
        self.assertIn("cron: '9 * * * *'", text)
        self.assertNotIn("git push --force", text)


if __name__ == "__main__":
    unittest.main()
