"""Lossless archived-segment rollover: synthetic market data, real local Git proof."""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from paper_pov import ledger, segmented_live_writer as live
from paper_pov import segmented_repository as repo
from paper_pov.test_ledger import synthetic, SHA


class RolloverTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.gitdir = self.root / "ledger"
        self.gitdir.mkdir()
        self.git("init")
        self.git("config", "user.email", "paper@example.invalid")
        self.git("config", "user.name", "Paper Test")
        (self.gitdir / "paper-ledger.json").write_bytes(ledger.canonical(ledger.empty()))
        self.git("add", "paper-ledger.json")
        self.git("commit", "-m", "legacy genesis")
        self.base = self.git("rev-parse", "HEAD")
        self.index = 0

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.gitdir), *args],
                              capture_output=True, check=True).stdout.decode().strip()

    def next_scan(self, base, minute):
        self.index += 1
        staged = self.root / ("scan-" + str(self.index))
        after, _ = live.stage(self.gitdir, base, synthetic(minute), SHA, staged)
        paths = live.apply(self.gitdir, base, staged)
        self.git("commit", "-m", "atomic paper scan")
        new = self.git("rev-parse", "HEAD")
        self.git("update-ref", live.REMOTE_REF, new)
        self.assertEqual(live.verify_remote(self.gitdir, base, new, staged)
                         ["generation"], after["generation"])
        return new, staged, paths

    def build_history(self, count=5):
        base = self.base
        for i in range(count):
            base, _, _ = self.next_scan(base, 30 * i)
        return base

    def test_git_anchored_rollover_replays_and_archives_without_loss(self):
        base = self.build_history(5)
        prior, mode = repo.read_git_state(self.gitdir, base, full_replay=True)
        self.assertEqual(mode, "segmented")
        archived = self.root / "archived"
        initial = self.root / "previous"
        initial.mkdir()
        manifest = json.loads(self.git("show", base + ":" + repo.MANIFEST))
        for path in [repo.CHECKPOINT, repo.SNAPSHOT, repo.MANIFEST] + [
                repo._segment_path(e["generation"]) for e in manifest["segments"]]:
            repo._write(initial / path, subprocess.run(
                ["git", "-C", str(self.gitdir), "show", base + ":" + path],
                check=True, capture_output=True).stdout)
        repo.stage_rollover(initial, base, archived)
        restored, new_manifest = repo.read_state(archived, full_replay=True)
        self.assertEqual(restored, prior)
        self.assertEqual(new_manifest["segments"], [])
        self.assertEqual(new_manifest["checkpoint"]["git_commit"], base)
        self.assertEqual(new_manifest["checkpoint"]["generation"], 5)
        self.assertEqual((archived / repo.CHECKPOINT).read_bytes(), ledger.canonical(prior))
        final = self.root / "final"
        repo.stage_append(archived, synthetic(150), SHA, final)
        paths = live.changed_paths(self.gitdir, base, final)
        for generation in range(1, 6):
            self.assertIn(repo._segment_path(generation), paths)
        self.assertIn(repo.CHECKPOINT, paths)
        self.assertIn(repo._segment_path(6), paths)
        live.apply(self.gitdir, base, final)
        self.git("commit", "-m", "atomic archival rollover and scan")
        new = self.git("rev-parse", "HEAD")
        self.git("update-ref", live.REMOTE_REF, new)
        self.assertEqual(live.verify_remote(self.gitdir, base, new, final)
                         ["generation"], 6)
        for generation in range(1, 6):
            path = repo._segment_path(generation)
            self.assertTrue(self.git("show", base + ":" + path))
            self.assertFalse(repo._git_has(self.gitdir, new, path))
        state, mode = repo.read_git_state(self.gitdir, new, full_replay=True)
        self.assertEqual(mode, "segmented")
        self.assertEqual(state, ledger.advance(prior, synthetic(150), SHA,
                                               32_000_000))
        self.assertEqual(state["predictions"][:len(prior["predictions"])],
                         prior["predictions"])
        self.assertEqual(state["observations"][:len(prior["observations"])],
                         prior["observations"])

    def test_automatic_rollover_at_aggregate_budget_without_data_loss(self):
        base = self.build_history(6)
        prior, _ = repo.read_git_state(self.gitdir, base, full_replay=True)
        manifest = json.loads(self.git("show", base + ":" + repo.MANIFEST))
        initial = self.root / "initial"
        initial.mkdir()
        for path in [repo.CHECKPOINT, repo.SNAPSHOT, repo.MANIFEST] + [
                repo._segment_path(e["generation"]) for e in manifest["segments"]]:
            repo._write(initial / path, subprocess.run(
                ["git", "-C", str(self.gitdir), "show", base + ":" + path],
                check=True, capture_output=True).stdout)
        normal = self.root / "normal"
        repo.stage_append(initial, synthetic(180), SHA, normal)
        rolled = self.root / "rolled"
        repo.stage_rollover(initial, base, rolled)
        compact = self.root / "compact"
        repo.stage_append(rolled, synthetic(180), SHA, compact)
        normal_size = repo.active_storage_bytes(normal)
        compact_size = repo.active_storage_bytes(compact)
        self.assertLess(compact_size, normal_size)
        budget = (normal_size + compact_size) // 2
        with patch.object(repo, "MAX_ACTIVE_TREE_BYTES", budget):
            staged = self.root / "automatic"
            state, info = live.stage(self.gitdir, base, synthetic(180), SHA, staged)
            self.assertLessEqual(info["active_storage_bytes"], budget)
            self.assertEqual(state["generation"], prior["generation"] + 1)
            self.assertEqual(state["predictions"][:len(prior["predictions"])],
                             prior["predictions"])
            self.assertEqual(len(repo.read_state(staged, True)[1]["segments"]), 1)
            paths = live.changed_paths(self.gitdir, base, staged)
            self.assertIn(repo.CHECKPOINT, paths)
            self.assertIn(repo._segment_path(1), paths)
            self.assertIn(repo._segment_path(7), paths)

    def test_corrupt_archive_and_false_origin_fail_closed(self):
        base = self.build_history(2)
        manifest = json.loads(self.git("show", base + ":" + repo.MANIFEST))
        initial = self.root / "initial"
        initial.mkdir()
        for path in [repo.CHECKPOINT, repo.SNAPSHOT, repo.MANIFEST] + [
                repo._segment_path(e["generation"]) for e in manifest["segments"]]:
            repo._write(initial / path, subprocess.run(
                ["git", "-C", str(self.gitdir), "show", base + ":" + path],
                check=True, capture_output=True).stdout)
        bad = self.root / "bad"
        shutil.copytree(initial, bad)
        segment = bad / repo._segment_path(1)
        segment.write_bytes(segment.read_bytes()[:-1])
        with self.assertRaises(ValueError):
            repo.stage_rollover(bad, base, self.root / "corrupt-out")
        self.assertFalse((self.root / "corrupt-out").exists())
        forged = self.root / "forged"
        repo.stage_rollover(initial, "f" * 40, forged)
        appended = self.root / "forged-append"
        repo.stage_append(forged, synthetic(60), SHA, appended)
        with self.assertRaisesRegex(ValueError, "Unverified archived checkpoint"):
            live.changed_paths(self.gitdir, base, appended)
        self.assertEqual(self.git("rev-parse", "HEAD"), base)


if __name__ == "__main__":
    unittest.main()
