"""D2 ZIP replay: end-to-end success, tamper, identity and safety failures."""
import hashlib
import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from paper_pov.replay_downloaded_artifacts import replay, read_archive, LEDGER_FILES
from paper_pov.results_report import render
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
        seal(self.ledger, ["latest.json", "scoreboard.json", "ledger.json"])
        seal(self.results, ["results.json", "results.md"])
        pack(self.ledger_path, self.ledger)
        pack(self.results_path, self.results)

    def verify(self):
        return replay(self.ledger_path, self.results_path, run_id=RUN,
                      source_sha=SHA, ledger_commit=LEDGER)

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


if __name__ == "__main__":
    unittest.main()
