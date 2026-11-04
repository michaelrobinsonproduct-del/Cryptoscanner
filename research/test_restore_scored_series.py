"""Actual portable score/depth series relocation and next-round acceptance."""
import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from research.capture_acquisition_scores import capture_score
from research.prospective_round_store import append_round, evaluate_index
from research.test_prospective_outcome_adapter import fixture
from research.restore_scored_series import restore_and_capture

PID = "a" * 64


def seed(root):
    entry = root / "entry"
    entry.mkdir(parents=True)
    capture_score(entry / "scores", prediction_id=PID, pair="XBTUSD",
                  baseline_score=45, challenger_score=47, observed_at=1700000001)
    depth = entry / "depth"
    depth.mkdir()
    fixture(depth)
    append_round(entry / "round-index.jsonl", depth)
    return entry


class RestoreScoredSeriesTests(unittest.TestCase):
    def test_restore_real_bytes_append_and_evaluate_across_runs(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "original"
            score = seed(source)
            original_receipt = (score / "scores" / (PID + ".json")).read_bytes()
            original_index = (score / "round-index.jsonl").read_bytes()
            # Downloaded artifacts retain old absolute GitHub runner paths.
            # Prove a different job can restore source solely from the local
            # checksummed archive, never opening the obsolete absolute path.
            import json
            original_record = json.loads(original_index)
            original_record["batch"] = "/home/runner/work/expired/entry/depth"
            (score / "round-index.jsonl").write_text(json.dumps(original_record) + "\n")
            original_index = (score / "round-index.jsonl").read_bytes()
            def collector(pairs, directory):
                self.assertEqual(pairs, ["XBTUSD"])
                directory.mkdir()
                fixture(directory)
            new = root / "restored"
            result = restore_and_capture(source, new, collector=collector)
            self.assertEqual(result["rounds_verified"], 2)
            self.assertEqual(result["original_index_sha256"],
                             hashlib.sha256(original_index).hexdigest())
            self.assertEqual((source / "entry" / "round-index.jsonl").read_bytes(),
                             original_index)
            self.assertEqual((new / "entry" / "original-index.jsonl").read_bytes(),
                             original_index)
            self.assertEqual((new / "entry" / "scores" / (PID + ".json")).read_bytes(),
                             original_receipt)
            self.assertEqual(evaluate_index(new / "entry" / "round-index.jsonl")["rounds_verified"], 2)
            self.assertFalse(result["production_applied"])
            # Another independent job restores the new artifact without
            # rewriting original evidence or synthesizing elapsed 5m slots.
            latest = root / "third-job"
            resumed = restore_and_capture(new, latest, collector=collector)
            self.assertEqual(resumed["rounds_verified"], 3)
            self.assertEqual(evaluate_index(latest / "entry" / "round-index.jsonl")["rounds_verified"], 3)

    def test_modified_manifest_fails_before_copy_or_collection(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "original"
            seed(source)
            with (source / "entry" / "depth" / "manifest.json").open("a") as handle:
                handle.write("tampered")
            target = Path(temp) / "new"
            with self.assertRaisesRegex(ValueError, "source manifest digest"):
                restore_and_capture(source, target, collector=lambda *_: self.fail("collected"))
            self.assertFalse(target.exists())

    def test_external_or_duplicate_index_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "original"
            seed(source)
            index = source / "entry" / "round-index.jsonl"
            original = index.read_text()
            index.write_text(original + original)
            with self.assertRaisesRegex(ValueError, "duplicate"):
                restore_and_capture(source, Path(temp) / "new")
            index.write_text(original)
            import json
            line = json.loads(original)
            line["batch"] = "/untrusted/external/depth-999"
            index.write_text(json.dumps(line) + "\n")
            with self.assertRaises(ValueError):
                restore_and_capture(source, Path(temp) / "new")

    def test_changed_pair_unacceptable_even_if_manifest_digest_updated(self):
        import json
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "original"
            seed(source)
            manifest_path = source / "entry" / "depth" / "manifest.json"
            manifest = json.loads(manifest_path.read_text())
            manifest["entries"][0]["pair"] = "ETHUSD"
            manifest_path.write_text(json.dumps(manifest))
            index_path = source / "entry" / "round-index.jsonl"
            index_row = json.loads(index_path.read_text())
            index_row["manifest_sha256"] = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
            index_path.write_text(json.dumps(index_row) + "\n")
            with self.assertRaisesRegex(ValueError, "scored cohort"):
                restore_and_capture(source, Path(tmp) / "new",
                                    collector=lambda *_: self.fail("collected"))
            self.assertFalse((Path(tmp) / "new").exists())

    def test_newly_collected_pair_substitution_is_never_indexed(self):
        import json
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "original"
            seed(source)
            def substituted_collector(pairs, directory):
                self.assertEqual(pairs, ["XBTUSD"])
                directory.mkdir()
                fixture(directory)
                manifest_path = directory / "manifest.json"
                manifest = json.loads(manifest_path.read_text())
                manifest["entries"][0]["pair"] = "ETHUSD"
                manifest_path.write_text(json.dumps(manifest))
            target = Path(tmp) / "new"
            with self.assertRaisesRegex(ValueError, "new depth round differs"):
                restore_and_capture(source, target, collector=substituted_collector)
            self.assertEqual(len((target / "entry" / "round-index.jsonl").read_text().splitlines()), 1)

    def test_missing_receipt_and_existing_destination_fail_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "original"
            seed(source)
            (source / "entry" / "scores" / (PID + ".json")).unlink()
            with self.assertRaises(ValueError):
                restore_and_capture(source, Path(temp) / "new")
            capture_score(source / "entry" / "scores", prediction_id=PID,
                          pair="XBTUSD", baseline_score=45,
                          challenger_score=47, observed_at=1700000001)
            target = Path(temp) / "existing"
            target.mkdir()
            with self.assertRaises(FileExistsError):
                restore_and_capture(source, target)


if __name__ == "__main__":
    unittest.main()
