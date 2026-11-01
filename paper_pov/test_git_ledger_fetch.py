"""Bounded ledger fetch never downloads all repository history."""
import unittest
from unittest.mock import patch
import subprocess
import tempfile
from pathlib import Path

from paper_pov import git_ledger_fetch as f

HEAD = "a" * 40
CHECKPOINT = "b" * 40


class BoundedFetchTests(unittest.TestCase):
    @patch.object(f, "_git")
    @patch.object(f.subprocess, "run")
    def test_legacy_uses_bounded_depth512_without_checkpoint(self, run, git):
        git.side_effect = [b"", (HEAD + "\n").encode(), b"legacy"]
        run.side_effect = [subprocess.CompletedProcess([], 1, b"", b"missing"),
                           subprocess.CompletedProcess([], 1, b"", b"missing")]
        self.assertEqual(f.fetch_bounded(), HEAD)
        self.assertIn("--depth=512", git.call_args_list[0].args)
        self.assertNotIn("--unshallow", str(git.call_args_list))

    @patch.object(f, "_checkpoint_needs_fetch", return_value=False)
    @patch.object(f, "_git")
    @patch.object(f.subprocess, "run")
    def test_segmented_preserves_already_fetched_legacy_ancestry(self, run, git, needs):
        git.side_effect = [b"", (HEAD + "\n").encode(), b"checkpoint"]
        manifest = ('{"checkpoint":{"git_commit":"' + CHECKPOINT + '"}}').encode()
        run.return_value = subprocess.CompletedProcess([], 0, manifest, b"")
        self.assertEqual(f.fetch_bounded(), HEAD)
        self.assertEqual(needs.call_args.args, (CHECKPOINT,))
        self.assertEqual(len(git.call_args_list), 3)
        self.assertFalse(any("--depth=1" in str(c.args) for c in git.call_args_list))

    @patch.object(f, "_checkpoint_needs_fetch", return_value=True)
    @patch.object(f, "_git")
    @patch.object(f.subprocess, "run")
    def test_missing_or_shallow_checkpoint_refetched_with_bounded_ancestry(self, run, git, needs):
        git.side_effect = [b"", (HEAD + "\n").encode(), b"", b"checkpoint"]
        manifest = ('{"checkpoint":{"git_commit":"' + CHECKPOINT + '"}}').encode()
        run.return_value = subprocess.CompletedProcess([], 0, manifest, b"")
        self.assertEqual(f.fetch_bounded(), HEAD)
        self.assertIn(("fetch", "--no-tags", "--depth=512", "origin", CHECKPOINT),
                      [c.args for c in git.call_args_list])
        self.assertNotIn(("fetch", "--no-tags", "--depth=1", "origin", CHECKPOINT),
                         [c.args for c in git.call_args_list])

    @patch.object(f, "_git")
    @patch.object(f.subprocess, "run")
    def test_checkpoint_boundary_detection_fails_closed_or_deepens(self, run, git):
        with tempfile.TemporaryDirectory() as directory:
            shallow = Path(directory) / "shallow"
            git.return_value = str(shallow).encode() + b"\n"
            run.return_value = subprocess.CompletedProcess([], 1, b"", b"")
            self.assertTrue(f._checkpoint_needs_fetch(CHECKPOINT))
            git.assert_not_called()  # Missing commit needs fetching without Git-path lookup.
            run.return_value = subprocess.CompletedProcess([], 0, b"", b"")
            self.assertFalse(f._checkpoint_needs_fetch(CHECKPOINT))
            shallow.write_text(CHECKPOINT + "\n")
            self.assertTrue(f._checkpoint_needs_fetch(CHECKPOINT))
            shallow.write_text(HEAD + "\n")
            self.assertFalse(f._checkpoint_needs_fetch(CHECKPOINT))

    @patch.object(f, "_git")
    @patch.object(f.subprocess, "run")
    def test_malformed_segmented_checkpoint_fails_closed(self, run, git):
        git.side_effect = [b"", (HEAD + "\n").encode()]
        run.return_value = subprocess.CompletedProcess(
            [], 0, b'{"checkpoint":{"git_commit":"not-a-sha"}}', b"")
        with self.assertRaises(ValueError):
            f.fetch_bounded()
        self.assertEqual(len(git.call_args_list), 2)


if __name__ == "__main__":
    unittest.main()
