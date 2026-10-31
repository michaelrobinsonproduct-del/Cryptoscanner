"""Fail-closed Git storage transaction tests. All observations are synthetic."""
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from paper_pov import ledger, segmented_repository as repo, segmented_storage as storage
from paper_pov.test_ledger import synthetic, SHA


class GitRepositoryStorageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.sha = "b" * 40

    def migrate(self, state=None, raw=None, target="migrated"):
        state = ledger.empty() if state is None else state
        raw = ledger.canonical(state) if raw is None else raw
        directory = self.root / target
        repo.stage_migration(raw, self.sha, directory)
        return directory

    def append(self, previous, minutes, target):
        directory = self.root / target
        info = repo.stage_append(previous, synthetic(minutes), SHA, directory)
        return directory, info

    def test_exact_legacy_checkpoint_preserved_and_full_replay(self):
        first = ledger.advance(ledger.empty(), synthetic(0), SHA)
        raw = json.dumps(first, indent=2, sort_keys=True).encode()
        root = self.migrate(first, raw)
        self.assertEqual((root / repo.CHECKPOINT).read_bytes(), raw)
        restored, manifest = repo.read_state(root, full_replay=True)
        self.assertEqual(restored, first)
        self.assertEqual(manifest["checkpoint"]["file_sha256"],
                         hashlib.sha256(raw).hexdigest())
        self.assertEqual(manifest["checkpoint"]["git_commit"], self.sha)
        self.assertEqual(manifest["segments"], [])

    def test_immutable_append_and_recovery(self):
        root = self.migrate()
        root2, info1 = self.append(root, 0, "scan1")
        root3, info2 = self.append(root2, 30, "scan2")
        self.assertEqual(info1["generation"], 1)
        self.assertEqual(info2["generation"], 2)
        state, manifest = repo.read_state(root3, full_replay=True)
        self.assertEqual(state["generation"], 2)
        self.assertEqual(len(manifest["segments"]), 2)
        self.assertEqual(state, ledger.advance(
            ledger.advance(ledger.empty(), synthetic(0), SHA), synthetic(30), SHA))
        self.assertEqual((root / repo.CHECKPOINT).read_bytes(),
                         (root3 / repo.CHECKPOINT).read_bytes())
        self.assertEqual((root2 / repo._segment_path(1)).read_bytes(),
                         (root3 / repo._segment_path(1)).read_bytes())
        self.assertEqual(repo.read_state(root)[0]["generation"], 0)
        self.assertEqual(repo.read_state(root2)[0]["generation"], 1)

    def test_archived_50_hour_outcomes_recover_from_segments(self):
        root = self.migrate()
        root2, _ = self.append(root, 0, "first")
        root3, _ = self.append(root2, 51 * 60, "late")
        state, manifest = repo.read_state(root3, full_replay=True)
        self.assertEqual(state["archived"]["scans"], 1)
        self.assertEqual(state["archived"]["gap_abstentions"], 48)
        first_report = storage.read_segment(
            (root3 / repo._segment_path(1)).read_bytes())["report"]
        self.assertEqual(first_report["observations"], synthetic(0)["observations"])
        self.assertEqual(len(manifest["segments"]), 2)

    def test_partial_transaction_and_preexisting_destination_fail(self):
        root = self.migrate()
        with self.assertRaises(FileExistsError):
            repo.stage_migration(ledger.canonical(ledger.empty()), self.sha, root)
        with self.assertRaises(FileExistsError):
            repo.stage_append(root, synthetic(0), SHA, root)
        partial = self.root / "partial"
        partial.mkdir()
        (partial / repo.MANIFEST).write_bytes((root / repo.MANIFEST).read_bytes())
        with self.assertRaises(ValueError):
            repo.read_state(partial)

    def test_corruption_or_missing_segment_fails_closed(self):
        root = self.migrate()
        root2, _ = self.append(root, 0, "first")
        root3, _ = self.append(root2, 30, "second")
        path = root3 / repo._segment_path(1)
        data = path.read_bytes()
        path.write_bytes(data[:-1])
        with self.assertRaises(ValueError):
            repo.read_state(root3)
        path.write_bytes(data)
        path.unlink()
        with self.assertRaises(ValueError):
            repo.read_state(root3)

    def test_snapshot_checkpoint_and_manifest_tamper_fail(self):
        for which in (repo.SNAPSHOT, repo.CHECKPOINT, repo.MANIFEST):
            with self.subTest(which=which):
                root = self.migrate(target="migrate-" + which)
                path = root / which
                path.write_bytes(path.read_bytes() + b" ")
                with self.assertRaises(ValueError):
                    repo.read_state(root)

    def test_missing_duplicate_out_of_order_inventory_fail(self):
        root = self.migrate()
        root2, _ = self.append(root, 0, "first")
        root3, _ = self.append(root2, 30, "second")
        manifest_path = root3 / repo.MANIFEST
        original = manifest_path.read_bytes()
        for mutate in (
                lambda m: m["segments"].pop(),
                lambda m: m["segments"].append(copy.deepcopy(m["segments"][-1])),
                lambda m: m["segments"].reverse(),
                lambda m: m["segments"][1].update(before_sha256="f" * 64),
                lambda m: m["head"].update(generation=99)):
            manifest = json.loads(original)
            mutate(manifest)
            manifest_path.write_bytes(ledger.canonical(manifest))
            with self.assertRaises(ValueError):
                repo.read_state(root3)
        manifest_path.write_bytes(original)
        self.assertEqual(repo.read_state(root3, full_replay=True)[0]["generation"], 2)

    def test_extra_file_and_symlink_fail(self):
        root = self.migrate()
        (root / "unexpected.txt").write_text("oops")
        with self.assertRaises(ValueError):
            repo.read_state(root)
        (root / "unexpected.txt").unlink()
        (root / "link").symlink_to(root / repo.CHECKPOINT)
        with self.assertRaises(ValueError):
            repo.read_state(root)

    def test_duplicate_or_out_of_order_scan_rejected_without_mutation(self):
        root = self.migrate()
        root2, _ = self.append(root, 30, "first")
        prior = (root2 / repo.MANIFEST).read_bytes()
        with self.assertRaises(ValueError):
            repo.stage_append(root2, synthetic(30), SHA, self.root / "dup")
        with self.assertRaises(ValueError):
            repo.stage_append(root2, synthetic(0), SHA, self.root / "old")
        self.assertEqual((root2 / repo.MANIFEST).read_bytes(), prior)
        self.assertFalse((self.root / "dup").exists())

    def test_wrong_provenance_and_missing_checkpoint_fail(self):
        with self.assertRaises(ValueError):
            repo.stage_migration(ledger.canonical(ledger.empty()), "not-a-sha",
                                 self.root / "invalid")
        root = self.migrate()
        (root / repo.CHECKPOINT).unlink()
        with self.assertRaises(ValueError):
            repo.read_state(root)

    def test_bad_report_aborts_without_staging(self):
        root = self.migrate()
        report = synthetic(0)
        report["buy_approved"] = True
        with self.assertRaises(ValueError):
            repo.stage_append(root, report, SHA, self.root / "unsafe")
        self.assertFalse((self.root / "unsafe").exists())

    def test_cli_migrate_verify_and_append(self):
        legacy = self.root / "legacy.json"
        legacy.write_bytes(ledger.canonical(ledger.empty()))
        repo.main(["migrate", "--legacy-file", str(legacy),
                   "--checkpoint-commit", self.sha, "--destination",
                   str(self.root / "first")])
        report = self.root / "report.json"
        report.write_bytes(ledger.canonical(synthetic(0)))
        repo.main(["append", "--previous", str(self.root / "first"),
                   "--report-file", str(report), "--source-sha", SHA,
                   "--destination", str(self.root / "second")])
        repo.main(["verify", "--directory", str(self.root / "second"),
                   "--full-replay"])
        self.assertEqual(repo.read_state(self.root / "second")[0]["generation"], 1)


if __name__ == "__main__":
    unittest.main()
