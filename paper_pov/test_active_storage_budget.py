"""Aggregate active packed-ledger capacity: no silent overflow or history loss."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from paper_pov import ledger, segmented_repository as repo
from paper_pov.test_ledger import synthetic, SHA


class AggregateBudgetTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.checkpoint_sha = "b" * 40

    def migrate(self, name="migrated"):
        path = self.root / name
        repo.stage_migration(ledger.canonical(ledger.empty()),
                             self.checkpoint_sha, path)
        return path

    def test_active_size_includes_checkpoint_snapshot_manifest_and_all_segments(self):
        first = self.migrate()
        second = self.root / "next"
        info = repo.stage_append(first, synthetic(0), SHA, second)
        files = [p for p in second.rglob("*") if p.is_file()]
        self.assertEqual(len(files), 4)
        actual = sum(p.stat().st_size for p in files)
        self.assertEqual(repo.active_storage_bytes(second), actual)
        self.assertEqual(info["active_storage_bytes"], actual)
        self.assertEqual(info["active_storage_budget_bytes"], 10_000_000)
        self.assertLess(actual, info["active_storage_budget_bytes"])
        self.assertEqual(repo.read_state(second, full_replay=True)[0]["generation"], 1)

    def test_migration_aborts_before_publish_when_total_budget_exceeded(self):
        target = self.root / "too-small-migration"
        with patch.object(repo, "MAX_ACTIVE_TREE_BYTES", 1):
            with self.assertRaisesRegex(ValueError, "Aggregate active"):
                repo.stage_migration(ledger.canonical(ledger.empty()),
                                     self.checkpoint_sha, target)
        self.assertFalse(target.exists())

    def test_append_aborts_without_mutating_prior_ledger_or_publishing(self):
        before = self.migrate()
        original = {str(p.relative_to(before)): p.read_bytes()
                    for p in before.rglob("*") if p.is_file()}
        target = self.root / "blocked"
        with patch.object(repo, "MAX_ACTIVE_TREE_BYTES",
                          repo.active_storage_bytes(before)):
            with self.assertRaisesRegex(ValueError, "archive rollover required"):
                repo.stage_append(before, synthetic(0), SHA, target)
        self.assertFalse(target.exists())
        self.assertEqual(original, {str(p.relative_to(before)): p.read_bytes()
                                   for p in before.rglob("*") if p.is_file()})
        self.assertEqual(repo.read_state(before, full_replay=True)[0]["generation"], 0)

    def test_multiple_immutable_segments_remain_replayable_with_headroom(self):
        previous = self.migrate()
        for i in range(6):
            target = self.root / ("scan-" + str(i))
            info = repo.stage_append(previous, synthetic(30 * i), SHA, target)
            self.assertLess(info["active_storage_bytes"],
                            info["active_storage_budget_bytes"])
            self.assertEqual(repo.read_state(target, full_replay=True)[0]["generation"],
                             i + 1)
            previous = target
        self.assertEqual(len(list((previous / repo.SEGMENTS).glob("*.json"))), 6)
        self.assertLess(repo.active_storage_bytes(previous), repo.MAX_ACTIVE_TREE_BYTES)


if __name__ == "__main__":
    unittest.main()
