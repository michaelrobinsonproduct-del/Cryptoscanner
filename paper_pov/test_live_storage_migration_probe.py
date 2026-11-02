"""Read-only real-ledger migration contracts; synthetic fixtures are NOT hits."""
import json
import unittest
from pathlib import Path

from paper_pov import ledger, segmented_storage as storage
from paper_pov.live_storage_migration_probe import probe
from paper_pov.test_ledger import synthetic

SHA = "a" * 40
WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/paper-live-storage-migration-probe.yml"


def fixture():
    return ledger.canonical(ledger.advance(ledger.empty(), synthetic(0), SHA))


class LiveMigrationProbeTests(unittest.TestCase):
    def test_roundtrip_preserves_exact_state_and_scoreboard(self):
        raw = fixture()
        report, packed = probe(raw, SHA)
        self.assertEqual(report["status"], "READ_ONLY_REAL_LEDGER_PACK_ROUNDTRIP_VERIFIED")
        self.assertEqual(report["ledger_generation"], 1)
        self.assertEqual(report["actual_scans"], 1)
        self.assertEqual(report["raw_bytes"], len(raw))
        self.assertEqual(ledger.canonical(storage.unpack_snapshot(packed)), raw)
        self.assertEqual(report["held_out_lift"], None)
        self.assertFalse(report["writer_migrated"])
        self.assertFalse(report["cadence_expanded"])
        self.assertFalse(report["production_applied"])

    def test_reject_corruption_and_reformatted_source(self):
        raw = fixture()
        with self.assertRaises(ValueError):
            probe(raw.replace(b'"sha256":"', b'"sha256":"0', 1), SHA)
        with self.assertRaises(ValueError):
            probe(json.dumps(json.loads(raw), indent=2).encode(), SHA)

    def test_reject_missing_bad_commit_or_oversized(self):
        for raw, sha in ((b"", SHA), (fixture(), "unknown"),
                         (b"X" * (ledger.MAX_BYTES + 1), SHA)):
            with self.subTest(length=len(raw)):
                with self.assertRaises(ValueError):
                    probe(raw, sha)

    def test_reject_empty_generation_even_if_validly_sealed(self):
        with self.assertRaisesRegex(ValueError, "No genuine"):
            probe(ledger.canonical(ledger.empty()), SHA)

    def test_probe_workflow_is_read_only_and_cannot_scan(self):
        text = WORKFLOW.read_text()
        self.assertIn("contents: read", text)
        self.assertIn("git show FETCH_HEAD:paper-ledger.json", text)
        self.assertIn("git ls-remote --heads", text)
        self.assertIn("PAPER_LEDGER_BRANCH_MOVED_ABORT", text)
        for forbidden in ("git push ", "workflow_dispatch:", "schedule:",
                          "python -m paper_pov.scanner", "contents: write",
                          "issues: write", "railway"):
            self.assertNotIn(forbidden, text.lower())


if __name__ == "__main__":
    unittest.main()
