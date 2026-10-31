"""Git-only single-writer transaction acceptance; all market reports synthetic."""
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from paper_pov import ledger, segmented_live_writer as live
from paper_pov import segmented_repository as segments
from paper_pov.test_ledger import synthetic, SHA


class LiveWriterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.gitdir = self.root / "git"
        self.gitdir.mkdir()
        self.git("init")
        self.git("config", "user.email", "paper@example.invalid")
        self.git("config", "user.name", "Paper Test")
        (self.gitdir / "paper-ledger.json").write_bytes(ledger.canonical(ledger.empty()))
        self.git("add", "--", "paper-ledger.json")
        self.git("commit", "-m", "immutable legacy ledger")
        self.base = self.git("rev-parse", "HEAD")

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.gitdir), *args],
                              check=True, capture_output=True).stdout.decode().strip()

    def prepare(self, base=None, minute=0, name="stage"):
        base = self.base if base is None else base
        destination = self.root / name
        after, info = live.stage(self.gitdir, base, synthetic(minute), SHA, destination)
        return destination, after, info

    def commit(self, base, staged):
        paths = live.apply(self.gitdir, base, staged)
        self.git("commit", "-m", "atomic paper ledger transition")
        sha = self.git("rev-parse", "HEAD")
        self.git("update-ref", live.REMOTE_REF, sha)
        return sha, paths

    def test_real_git_legacy_migration_and_remote_exact_readback(self):
        staged, after, info = self.prepare()
        self.assertEqual(after["generation"], 1)
        self.assertEqual(info["generation"], 1)
        self.assertEqual(len(json.loads((staged / segments.MANIFEST).read_bytes())["segments"]), 1)
        sha, paths = self.commit(self.base, staged)
        self.assertEqual(paths, sorted([segments.CHECKPOINT, segments.SNAPSHOT,
                                        segments.MANIFEST, segments._segment_path(1)]))
        proof = live.verify_remote(self.gitdir, self.base, sha, staged)
        self.assertEqual(proof["generation"], 1)
        self.assertEqual(proof["ledger_sha256"], after["sha256"])
        self.assertEqual(self.git("show", self.base + ":paper-ledger.json").encode(),
                         self.git("show", sha + ":paper-ledger.json").encode())
        self.assertEqual(segments.read_git_state(self.gitdir, sha, True)[0], after)

    def test_second_append_preserves_checkpoint_and_old_segments(self):
        first, _, _ = self.prepare()
        first_commit, _ = self.commit(self.base, first)
        second, after, _ = self.prepare(first_commit, 30, "second")
        second_commit, paths = self.commit(first_commit, second)
        self.assertEqual(paths, sorted([segments.SNAPSHOT, segments.MANIFEST,
                                        segments._segment_path(2)]))
        self.assertEqual(live.verify_remote(self.gitdir, first_commit, second_commit, second)
                         ["generation"], 2)
        for path in (segments.CHECKPOINT, segments._segment_path(1)):
            self.assertEqual(self.git("show", first_commit + ":" + path),
                             self.git("show", second_commit + ":" + path))
        self.assertEqual(segments.read_git_state(self.gitdir, second_commit, True)[0], after)

    def test_wrong_base_or_dirty_checkout_refused(self):
        staged, _, _ = self.prepare()
        with self.assertRaises(ValueError):
            live.apply(self.gitdir, "f" * 40, staged)
        (self.gitdir / "unexpected.txt").write_text("do not commit")
        with self.assertRaisesRegex(ValueError, "not clean"):
            live.apply(self.gitdir, self.base, staged)

    def test_staged_corruption_and_missing_segment_fail_closed(self):
        for kind in ("corrupt", "missing"):
            with self.subTest(kind=kind):
                staged, _, _ = self.prepare(name=kind)
                path = staged / segments._segment_path(1)
                if kind == "corrupt":
                    path.write_bytes(path.read_bytes()[:-1])
                else:
                    path.unlink()
                with self.assertRaises(ValueError):
                    live.apply(self.gitdir, self.base, staged)
                self.assertEqual(self.git("status", "--porcelain"), "")

    def test_remote_branch_movement_and_unexpected_commit_files_refused(self):
        staged, _, _ = self.prepare()
        sha, _ = self.commit(self.base, staged)
        self.git("update-ref", live.REMOTE_REF, self.base)
        with self.assertRaisesRegex(ValueError, "Remote ledger ref"):
            live.verify_remote(self.gitdir, self.base, sha, staged)
        self.git("update-ref", live.REMOTE_REF, sha)
        (self.gitdir / "injected.txt").write_text("unrelated")
        self.git("add", "injected.txt")
        self.git("commit", "-m", "unexpected second writer")
        other = self.git("rev-parse", "HEAD")
        self.git("update-ref", live.REMOTE_REF, other)
        with self.assertRaises(ValueError):
            live.verify_remote(self.gitdir, self.base, other, staged)

    def test_duplicate_and_out_of_order_scan_rejected(self):
        staged, _, _ = self.prepare()
        sha, _ = self.commit(self.base, staged)
        with self.assertRaisesRegex(ValueError, "duplicate"):
            live.stage(self.gitdir, sha, synthetic(0), SHA, self.root / "dup")
        self.assertFalse((self.root / "dup").exists())

    def test_cli_stage_and_verified_outputs(self):
        report = self.root / "scan.json"
        report.write_bytes(ledger.canonical(synthetic(0)))
        dest = self.root / "cli"
        next_ledger = self.root / "next.json"
        scoreboard = self.root / "score.json"
        live.main(["stage", "--repository", str(self.gitdir),
                   "--base", self.base, "--staged", str(dest),
                   "--report", str(report), "--source-sha", SHA,
                   "--next-ledger", str(next_ledger), "--scoreboard", str(scoreboard)])
        self.assertEqual(json.loads(next_ledger.read_bytes())["generation"], 1)
        self.assertEqual(json.loads(scoreboard.read_bytes())["actual_scans"], 1)
        with self.assertRaises(FileExistsError):
            live.main(["stage", "--repository", str(self.gitdir),
                       "--base", self.base, "--staged", str(self.root / "other"),
                       "--report", str(report), "--source-sha", SHA,
                       "--next-ledger", str(next_ledger), "--scoreboard", str(scoreboard)])

    def test_incomplete_remote_migration_never_falls_back_to_legacy(self):
        staged, _, _ = self.prepare()
        sha, _ = self.commit(self.base, staged)
        (self.gitdir / segments.MANIFEST).unlink()
        self.git("add", "-A")
        self.git("commit", "-m", "partial transaction corruption")
        corrupt = self.git("rev-parse", "HEAD")
        with self.assertRaises(ValueError):
            live.stage(self.gitdir, corrupt, synthetic(30), SHA, self.root / "partial")
        self.assertEqual(segments.read_git_state(self.gitdir, sha)[1], "segmented")


if __name__ == "__main__":
    unittest.main()
