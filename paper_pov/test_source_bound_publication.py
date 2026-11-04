"""D2: independent publication-to-retained-source integration acceptance."""
import hashlib
import json
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path
from paper_pov.results_report import render, verify_published, main
from paper_pov.test_results_report import fixture, SHA, LEDGER

RUN = "41235442591"

class SourceBoundPublicationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.directory = Path(self.tmp.name)
        self.scan, self.score = fixture()
        self.publish()

    def publish(self, mutate=None):
        payload, md = render(self.scan, self.score, run_id=RUN,
                             source_sha=SHA, ledger_commit=LEDGER,
                             event="schedule", originating_cron="9 * * * *")
        if mutate:
            mutate(payload)
        (self.directory / "results.json").write_text(json.dumps(payload))
        (self.directory / "results.md").write_text(md + "\n")
        lines = [hashlib.sha256((self.directory / n).read_bytes()).hexdigest() + "  " + n
                 for n in ("results.json", "results.md")]
        (self.directory / "SHA256SUMS").write_text("\n".join(lines) + "\n")

    def verify(self):
        return verify_published(self.directory, run_id=RUN, source_sha=SHA,
                                ledger_commit=LEDGER,
                                ledger_sha256=self.score["ledger_sha256"],
                                scan=self.scan, scoreboard=self.score)

    def test_actual_cli_publish_then_verify_against_retained_inputs(self):
        source = self.directory / "retained-scan.json"
        board = self.directory / "retained-scoreboard.json"
        output = self.directory / "published"
        source.write_text(json.dumps(self.scan))
        board.write_text(json.dumps(self.score))
        args = ["results", "--scan", str(source), "--scoreboard", str(board),
                "--run-id", RUN, "--source-sha", SHA, "--ledger-commit", LEDGER,
                "--event", "schedule", "--originating-cron", "9 * * * *",
                "--output-dir", str(output)]
        with patch("sys.argv", args):
            main()
        verify_args = ["results", "--verify-only", "--scan", str(source),
                       "--scoreboard", str(board), "--run-id", RUN,
                       "--source-sha", SHA, "--ledger-commit", LEDGER,
                       "--ledger-sha256", self.score["ledger_sha256"],
                       "--output-dir", str(output)]
        with patch("sys.argv", verify_args):
            main()
        self.assertEqual(len(verify_published(
            output, run_id=RUN, source_sha=SHA, ledger_commit=LEDGER,
            ledger_sha256=self.score["ledger_sha256"],
            scan=self.scan, scoreboard=self.score)["candidates"]), 2)

    def test_valid_source_bound_publication(self):
        self.assertEqual(len(self.verify()["candidates"]), 2)

    def test_rechecksummed_omitted_watch_fails(self):
        self.publish(lambda p: p["candidates"].pop())
        with self.assertRaisesRegex(ValueError, "retained scan"):
            self.verify()

    def test_rechecksummed_changed_score_fails(self):
        self.publish(lambda p: p["candidates"][0].update(challenger_score=999))
        with self.assertRaisesRegex(ValueError, "retained scan"):
            self.verify()

    def test_rechecksummed_markdown_spoof_fails(self):
        (self.directory / "results.md").write_text("Fabricated WATCH success\n")
        lines = [hashlib.sha256((self.directory / n).read_bytes()).hexdigest() + "  " + n
                 for n in ("results.json", "results.md")]
        (self.directory / "SHA256SUMS").write_text("\n".join(lines) + "\n")
        with self.assertRaisesRegex(ValueError, "markdown differs"):
            self.verify()

    def verify_without_retained_sources(self):
        return verify_published(self.directory, run_id=RUN, source_sha=SHA,
                                ledger_commit=LEDGER,
                                ledger_sha256=self.score["ledger_sha256"])

    def test_independent_replay_rejects_duplicate_prediction_identity(self):
        self.publish(lambda p: p["candidates"][1].update(
            prediction_id=p["candidates"][0]["prediction_id"]))
        with self.assertRaisesRegex(ValueError, "published WATCH identity"):
            self.verify_without_retained_sources()

    def test_independent_replay_rejects_reordered_rank(self):
        self.publish(lambda p: p["candidates"][0].update(rank=2))
        with self.assertRaisesRegex(ValueError, "published WATCH identity"):
            self.verify_without_retained_sources()

    def test_independent_replay_rejects_forged_watch_status(self):
        self.publish(lambda p: p["candidates"][0].update(status="BUY"))
        with self.assertRaisesRegex(ValueError, "published WATCH identity"):
            self.verify_without_retained_sources()

    def test_independent_replay_accepts_valid_published_candidates(self):
        self.assertEqual(len(self.verify_without_retained_sources()["candidates"]), 2)

    def test_wrong_retained_source_fails(self):
        self.scan["watch"][0]["challenger_score"] += 1
        with self.assertRaisesRegex(ValueError, "retained scan"):
            self.verify()

    def test_missing_one_retained_input_fails(self):
        with self.assertRaisesRegex(ValueError, "together"):
            verify_published(self.directory, run_id=RUN, source_sha=SHA,
                             ledger_commit=LEDGER,
                             ledger_sha256=self.score["ledger_sha256"],
                             scan=self.scan)

if __name__ == "__main__":
    unittest.main()
