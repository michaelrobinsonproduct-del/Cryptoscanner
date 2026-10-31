"""Bounded ledger fetch never downloads all repository history."""
import unittest
from unittest.mock import patch
import subprocess

from paper_pov import git_ledger_fetch as f

HEAD = "a" * 40
CHECKPOINT = "b" * 40


class BoundedFetchTests(unittest.TestCase):
    @patch.object(f, "_git")
    @patch.object(f.subprocess, "run")
    def test_legacy_uses_depth64_without_checkpoint(self, run, git):
        git.side_effect = [b"", (HEAD + "\n").encode(), b"legacy"]
        run.side_effect = [subprocess.CompletedProcess([], 1, b"", b"missing"),
                           subprocess.CompletedProcess([], 1, b"", b"missing")]
        self.assertEqual(f.fetch_bounded(), HEAD)
        self.assertIn("--depth=64", git.call_args_list[0].args)
        self.assertNotIn("--unshallow", str(git.call_args_list))

    @patch.object(f, "_git")
    @patch.object(f.subprocess, "run")
    def test_segmented_fetches_exact_checkpoint_by_sha(self, run, git):
        git.side_effect = [b"", (HEAD + "\n").encode(), b"", b"checkpoint"]
        manifest = ('{"checkpoint":{"git_commit":"' + CHECKPOINT + '"}}').encode()
        run.return_value = subprocess.CompletedProcess([], 0, manifest, b"")
        self.assertEqual(f.fetch_bounded(), HEAD)
        self.assertIn(("fetch", "--no-tags", "--depth=1", "origin", CHECKPOINT),
                      [c.args for c in git.call_args_list])

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
