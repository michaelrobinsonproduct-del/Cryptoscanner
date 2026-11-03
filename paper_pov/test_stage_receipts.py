"""Focused D1 receipt publication regression tests (no Git or network)."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from paper_pov import ledger, segmented_live_writer as writer


class StageReceiptTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.state = ledger.empty()
        self.score = ledger.scoreboard(self.state)

    def paths(self):
        return self.root / "next.json", self.root / "score.json"

    def publish(self):
        a, b = self.paths()
        writer.publish_stage_outputs(a, self.state, b, self.score)
        return a, b

    def test_success_reads_both_receipts(self):
        a, b = self.publish()
        self.assertEqual(json.loads(a.read_text()), self.state)
        self.assertEqual(json.loads(b.read_text()), self.score)

    def test_existing_second_destination_never_writes_first(self):
        a, b = self.paths()
        b.write_text("existing")
        with self.assertRaises(FileExistsError):
            self.publish()
        self.assertFalse(a.exists())
        self.assertEqual(b.read_text(), "existing")

    def test_same_destination_fails_without_write(self):
        a, _ = self.paths()
        with self.assertRaises(ValueError):
            writer.publish_stage_outputs(a, self.state, a, self.score)
        self.assertFalse(a.exists())

    def test_second_write_failure_cleans_first_and_partial_second(self):
        a, b = self.paths()
        original = writer.segments._write
        def broken(path, data):
            if Path(path) == b:
                Path(path).write_bytes(b"partial")
                raise OSError("disk full")
            return original(path, data)
        with patch.object(writer.segments, "_write", side_effect=broken):
            with self.assertRaises(OSError):
                self.publish()
        self.assertFalse(a.exists())
        self.assertFalse(b.exists())

    def test_corrupt_first_write_fails_readback_and_cleans(self):
        a, b = self.paths()
        with patch.object(writer.segments, "_write",
                          side_effect=lambda path, data: Path(path).write_bytes(b"corrupt")):
            with self.assertRaises(ValueError):
                self.publish()
        self.assertFalse(a.exists())
        self.assertFalse(b.exists())

    def test_existing_symlink_destination_is_never_overwritten(self):
        a, b = self.paths()
        victim = self.root / "victim"
        victim.write_text("keep")
        b.symlink_to(victim)
        with self.assertRaises(FileExistsError):
            self.publish()
        self.assertFalse(a.exists())
        self.assertEqual(victim.read_text(), "keep")


if __name__ == "__main__":
    unittest.main()
