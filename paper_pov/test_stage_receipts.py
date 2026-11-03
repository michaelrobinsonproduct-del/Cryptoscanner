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
        original = writer._exclusive_receipt
        def broken(path, data):
            if Path(path) == b:
                raise OSError("disk full")
            return original(path, data)
        with patch.object(writer, "_exclusive_receipt", side_effect=broken):
            with self.assertRaises(OSError):
                self.publish()
        self.assertFalse(a.exists())
        self.assertFalse(b.exists())

    def test_corrupt_first_write_fails_readback_and_cleans(self):
        a, b = self.paths()
        with patch.object(writer, "_exclusive_receipt",
                          side_effect=lambda path, data: (Path(path).write_bytes(b"corrupt"), (Path(path).stat().st_dev, Path(path).stat().st_ino))[1]):
            with self.assertRaises(ValueError):
                self.publish()
        self.assertFalse(a.exists())
        self.assertFalse(b.exists())

    def test_racing_second_destination_is_not_deleted(self):
        a, b = self.paths()
        original = writer._exclusive_receipt
        def competing(path, data):
            if Path(path) == b:
                b.write_bytes(b"another writer")
                raise FileExistsError("competing publication")
            return original(path, data)
        with patch.object(writer, "_exclusive_receipt", side_effect=competing):
            with self.assertRaises(FileExistsError):
                self.publish()
        self.assertFalse(a.exists())
        self.assertEqual(b.read_bytes(), b"another writer")

    def test_competing_replacement_during_readback_is_preserved(self):
        a, b = self.paths()
        original = writer._exclusive_receipt
        def replace_after_creation(path, data):
            identity = original(path, data)
            if Path(path) == a:
                path = Path(path)
                path.unlink()
                path.write_bytes(b"competitor")
            return identity
        with patch.object(writer, "_exclusive_receipt", side_effect=replace_after_creation):
            with self.assertRaises(ValueError):
                self.publish()
        self.assertEqual(a.read_bytes(), b"competitor")
        self.assertFalse(b.exists())

    def test_same_bytes_replacement_is_detected_by_inode(self):
        a, b = self.paths()
        original = writer._exclusive_receipt
        def swapped(path, data):
            identity = original(path, data)
            if Path(path) == a:
                Path(path).unlink()
                Path(path).write_bytes(data)
            return identity
        with patch.object(writer, "_exclusive_receipt", side_effect=swapped):
            with self.assertRaisesRegex(ValueError, "replaced before readback"):
                self.publish()
        self.assertEqual(a.read_bytes(), ledger.canonical(self.state))
        self.assertFalse(b.exists())

    def test_competing_replacement_after_failed_write_is_preserved(self):
        a, _ = self.paths()
        real_fdopen = writer.os.fdopen
        class FailingStream:
            def __init__(self, stream):
                self.stream = stream
            def __enter__(self):
                self.stream.__enter__()
                return self
            def __exit__(self, *args):
                return self.stream.__exit__(*args)
            def write(self, data):
                self.stream.write(data)
                a.unlink()
                a.write_bytes(b"competitor")
                raise OSError("interrupted")
        def failed_fdopen(fd, mode):
            return FailingStream(real_fdopen(fd, mode))
        with patch.object(writer.os, "fdopen", side_effect=failed_fdopen):
            with self.assertRaises(OSError):
                writer._exclusive_receipt(a, b"ours")
        self.assertEqual(a.read_bytes(), b"competitor")

    def test_symlinked_parent_is_rejected(self):
        outside = self.root / "outside"
        outside.mkdir()
        redirected = self.root / "redirected"
        redirected.symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Unsafe receipt"):
            writer.publish_stage_outputs(redirected / "ledger.json", self.state,
                                         self.root / "score.json", self.score)
        self.assertFalse((outside / "ledger.json").exists())

    def test_exclusive_open_refuses_existing_file(self):
        a, _ = self.paths()
        a.write_text("other writer")
        with self.assertRaises(FileExistsError):
            writer._exclusive_receipt(a, b"ours")
        self.assertEqual(a.read_text(), "other writer")

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
