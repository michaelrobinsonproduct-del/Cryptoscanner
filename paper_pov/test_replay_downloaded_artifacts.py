"""D2 ZIP replay: end-to-end success, tamper, identity and safety failures."""
import hashlib
import contextlib
import io
from unittest.mock import patch
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from paper_pov.replay_downloaded_artifacts import replay, read_archive, replay_visible_result, LEDGER_FILES, main
from paper_pov.results_report import render
from paper_pov.failure_report import render_failure
from paper_pov.test_results_report import fixture, SHA, LEDGER

RUN = "41235442591"


def pack(path, files):
    with zipfile.ZipFile(path, "w") as archive:
        for name, data in files.items():
            archive.writestr(name, data)


def seal(files, names):
    files["SHA256SUMS"] = ("\n".join(
        hashlib.sha256(files[n]).hexdigest() + "  " + n for n in names) + "\n").encode()


class DownloadedArtifactReplayTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.ledger_path = Path(self.temp.name) / "ledger.zip"
        self.results_path = Path(self.temp.name) / "results.zip"
        scan, score = fixture()
        payload, markdown = render(scan, score, run_id=RUN, source_sha=SHA,
                                   ledger_commit=LEDGER, event="schedule",
                                   originating_cron="9 * * * *")
        self.ledger = {"latest.json": json.dumps(scan).encode(),
                       "scoreboard.json": json.dumps(score).encode(),
                       "ledger.json": json.dumps({"sha256": score["ledger_sha256"],
                                                  "generation": score["generation"]}).encode()}
        self.results = {"results.json": json.dumps(payload).encode(),
                        "results.md": (markdown + "\n").encode()}
        self.save()

    def save(self):
        seal(self.ledger, ["latest.json", "scoreboard.json", "ledger.json"] +
             (["slot_receipt.json"] if "slot_receipt.json" in self.ledger else []))
        seal(self.results, ["results.json", "results.md"])
        pack(self.ledger_path, self.ledger)
        pack(self.results_path, self.results)

    def verify(self):
        return replay(self.ledger_path, self.results_path, run_id=RUN,
                      source_sha=SHA, ledger_commit=LEDGER)

    def test_new_slot_receipt_is_verified_in_downloaded_ledger(self):
        slot = {"schema": 1, "slot_identity": "2026-11-03T23:09:00+00:00",
                "run_id": RUN, "source_sha": SHA,
                "historical_quotes_reconstructed": False}
        self.ledger["slot_receipt.json"] = json.dumps(slot).encode()
        self.save()
        result = self.verify()
        self.assertEqual(result["slot_identity"], slot["slot_identity"])
        slot["run_id"] = "999"
        self.ledger["slot_receipt.json"] = json.dumps(slot).encode()
        self.save()
        with self.assertRaisesRegex(ValueError, "Slot receipt identity"):
            self.verify()

    def test_failed_run_receipt_is_visible_but_never_certified(self):
        failed, markdown = render_failure(RUN, SHA)
        receipt = {"results.json": json.dumps(failed).encode(),
                   "results.md": (markdown + "\n").encode()}
        seal(receipt, ["results.json", "results.md"])
        pack(self.results_path, receipt)
        outcome = replay_visible_result(failure_zip=self.results_path,
                                        run_id=RUN, source_sha=SHA)
        self.assertEqual(outcome["status"], "FAILED_PAPER_ONLY")
        self.assertIsNone(outcome["ledger_persisted"])
        self.assertIsNone(outcome["watch_candidates"])
        with self.assertRaisesRegex(ValueError, "Mixed success"):
            replay_visible_result(ledger_zip=self.ledger_path,
                                  failure_zip=self.results_path,
                                  run_id=RUN, source_sha=SHA)
        with self.assertRaisesRegex(ValueError, "identity"):
            replay_visible_result(failure_zip=self.results_path,
                                  run_id="999", source_sha=SHA)

    def test_failed_run_cli_reports_nonzero_and_no_ledger(self):
        failed, markdown = render_failure(RUN, SHA)
        receipt = {"results.json": json.dumps(failed).encode(),
                   "results.md": (markdown + "\n").encode()}
        seal(receipt, ["results.json", "results.md"])
        pack(self.results_path, receipt)
        output = io.StringIO()
        args = ["replay", "--failure-zip", str(self.results_path),
                "--run-id", RUN, "--source-sha", SHA]
        with patch("sys.argv", args), contextlib.redirect_stdout(output):
            code = main()
        result = json.loads(output.getvalue())
        self.assertEqual(code, 2)
        self.assertEqual(result["status"], "FAILED_PAPER_ONLY")
        self.assertIsNone(result["ledger_persisted"])
        self.assertIsNone(result["watch_candidates"])

    def test_complete_downloaded_artifact_replay(self):
        result = self.verify()
        self.assertEqual(result["watch_candidates"], 2)
        self.assertEqual(result["observed_markets"], 2)
        self.assertFalse(result["exchange_event_freshness_verified"])

    def test_rechecksummed_forged_score_fails_against_retained_scan(self):
        payload = json.loads(self.results["results.json"])
        payload["candidates"][0]["challenger_score"] += 100
        self.results["results.json"] = json.dumps(payload).encode()
        self.save()
        with self.assertRaisesRegex(ValueError, "retained scan"):
            self.verify()

    def test_corrupt_zip_checksum_fails(self):
        self.ledger["latest.json"] += b" "
        pack(self.ledger_path, self.ledger)
        with self.assertRaisesRegex(ValueError, "checksum"):
            self.verify()

    def test_mismatched_ledger_generation_fails(self):
        score = json.loads(self.ledger["scoreboard.json"])
        score["generation"] += 1
        self.ledger["scoreboard.json"] = json.dumps(score).encode()
        self.save()
        with self.assertRaisesRegex(ValueError, "Ledger/scoreboard"):
            self.verify()

    def test_wrong_expected_run_fails(self):
        with self.assertRaisesRegex(ValueError, "identity"):
            replay(self.ledger_path, self.results_path, run_id="999",
                   source_sha=SHA, ledger_commit=LEDGER)

    def test_duplicate_or_traversal_zip_entry_fails(self):
        with zipfile.ZipFile(self.ledger_path, "a") as archive:
            archive.writestr("../latest.json", b"{}")
        with self.assertRaisesRegex(ValueError, "Unsafe|duplicate"):
            read_archive(self.ledger_path, LEDGER_FILES)

    def cli(self, run_id=RUN):
        output = io.StringIO()
        args = ["replay", "--ledger-zip", str(self.ledger_path),
                "--results-zip", str(self.results_path),
                "--run-id", run_id, "--source-sha", SHA,
                "--ledger-commit", LEDGER]
        with patch("sys.argv", args), contextlib.redirect_stdout(output):
            code = main()
        return code, json.loads(output.getvalue())

    def test_legacy_missing_quote_evidence_abstains_with_nonzero_exit(self):
        payload = json.loads(self.results["results.json"])
        payload.pop("quote_evidence")
        self.results["results.json"] = json.dumps(payload).encode()
        self.save()
        code, output = self.cli()
        self.assertEqual(code, 2)
        self.assertEqual(output["status"], "ABSTAIN_LEGACY_QUOTE_EVIDENCE")
        self.assertFalse(output["certified"])
        self.assertFalse(output["exchange_event_freshness_verified"])
        with self.assertRaisesRegex(ValueError, "Missing independent quote evidence"):
            self.verify()

    def test_complete_replay_cli_certifies(self):
        code, output = self.cli()
        self.assertEqual(code, 0)
        self.assertTrue(output["certified"])
        self.assertEqual(output["watch_candidates"], 2)

    def test_identity_failure_never_becomes_legacy_abstention(self):
        payload = json.loads(self.results["results.json"])
        payload.pop("quote_evidence")
        self.results["results.json"] = json.dumps(payload).encode()
        self.save()
        with self.assertRaisesRegex(ValueError, "identity"):
            self.cli(run_id="999")

    def test_legacy_wrong_source_identity_is_hard_failure(self):
        payload = json.loads(self.results["results.json"])
        payload.pop("quote_evidence")
        payload["source_sha"] = "f" * 40
        self.results["results.json"] = json.dumps(payload).encode()
        self.save()
        with self.assertRaisesRegex(ValueError, "identity"):
            self.cli()

    def test_legacy_wrong_ledger_identity_is_hard_failure(self):
        payload = json.loads(self.results["results.json"])
        payload.pop("quote_evidence")
        payload["ledger_commit"] = "f" * 40
        self.results["results.json"] = json.dumps(payload).encode()
        self.save()
        with self.assertRaisesRegex(ValueError, "identity"):
            self.cli()

    def test_rechecksummed_legacy_forged_candidate_is_hard_failure(self):
        payload = json.loads(self.results["results.json"])
        payload.pop("quote_evidence")
        payload["candidates"][0]["challenger_score"] += 500
        self.results["results.json"] = json.dumps(payload).encode()
        self.save()
        with self.assertRaisesRegex(ValueError, "Legacy publication differs"):
            self.cli()

    def test_rechecksummed_legacy_forged_markdown_is_hard_failure(self):
        payload = json.loads(self.results["results.json"])
        payload.pop("quote_evidence")
        self.results["results.json"] = json.dumps(payload).encode()
        self.results["results.md"] += b"FAKE WATCH BUY\\n"
        self.save()
        with self.assertRaisesRegex(ValueError, "Legacy publication differs"):
            self.cli()

    def test_rechecksummed_legacy_missing_watch_is_hard_failure(self):
        payload = json.loads(self.results["results.json"])
        payload.pop("quote_evidence")
        payload["candidates"].pop()
        self.results["results.json"] = json.dumps(payload).encode()
        self.save()
        with self.assertRaisesRegex(ValueError, "Legacy publication differs"):
            self.cli()

    def test_corrupt_legacy_manifest_is_hard_failure(self):
        payload = json.loads(self.results["results.json"])
        payload.pop("quote_evidence")
        self.results["results.json"] = json.dumps(payload).encode()
        self.save()
        self.results["results.json"] += b" "
        pack(self.results_path, self.results)
        with self.assertRaisesRegex(ValueError, "checksum"):
            self.cli()


if __name__ == "__main__":
    unittest.main()    # Check immutable identity before classifying missing evidence. A forged
    # run/source/ledger reference is an integrity failure, never an abstention.
    payload = json.loads(results["results.json"])
    if not isinstance(payload, dict) or any(
            payload.get(key) != expected for key, expected in (
                ("run_id", str(run_id)), ("source_sha", source_sha),
                ("ledger_commit", ledger_commit),
                ("ledger_generation", score["generation"]),
                ("ledger_sha256", score["ledger_sha256"]))):
        raise ValueError("Published artifact identity mismatch")

