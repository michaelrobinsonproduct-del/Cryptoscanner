"""Actual portable score/depth series relocation and next-round acceptance."""
import hashlib
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from research.capture_acquisition_scores import capture_score
from research.acquisition_receipt_pipeline import load_captures
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
            with patch("research.restore_scored_series.evaluate_all", return_value={"mode": "RESEARCH_ONLY_AUTHENTICATED_HELD_OUT", "production_applied": False}):
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
            with patch("research.restore_scored_series.evaluate_all", return_value={"mode": "RESEARCH_ONLY_AUTHENTICATED_HELD_OUT", "production_applied": False}):
                resumed = restore_and_capture(new, latest, collector=collector)
            self.assertEqual(resumed["rounds_verified"], 3)
            self.assertEqual(evaluate_index(latest / "entry" / "round-index.jsonl")["rounds_verified"], 3)
            self.assertEqual(
                (latest / "continuation-history" / "through-002-rounds.json").read_bytes(),
                (new / "continuation-report.json").read_bytes())

    def test_twelve_actual_continuation_rounds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            seed(root / "original")
            times = [1000.0]
            def clock():
                return times[0]
            def sleep(seconds):
                times[0] += seconds
            observations = []
            def collector(pairs, target):
                self.assertEqual(pairs, ["XBTUSD"])
                observations.append((target.name, clock()))
                target.mkdir()
                fixture(target)
            with patch("research.restore_scored_series.evaluate_all",
                       return_value={"production_applied": False}):
                result = restore_and_capture(
                    root / "original", root / "extended", collector=collector,
                    followup_rounds=12, clock=clock, sleep=sleep)
            self.assertEqual(result["rounds_verified"], 13)
            self.assertEqual(result["followup_rounds_acquired"], 12)
            self.assertEqual(len(result["coverage"]), 4)
            self.assertEqual(len((root / "extended" / "entry" / "round-index.jsonl").read_text().splitlines()), 13)
            self.assertEqual(observations, [
                ("depth-%03d" % i, 1000.0 + 300 * (i - 1)) for i in range(1, 13)])
            self.assertFalse(result["production_applied"])


    def test_real_source_archive_continues_in_timed_batch(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "original"
            seed(source)
            elapsed = [1000.0]
            collected = []
            def clock():
                return elapsed[0]
            def sleep(seconds):
                self.assertGreater(seconds, 0)
                elapsed[0] += seconds
            def collector(pairs, directory):
                self.assertEqual(pairs, ["XBTUSD"])
                collected.append((directory.name, clock()))
                directory.mkdir()
                fixture(directory)
            target = root / "continued"
            with patch("research.restore_scored_series.evaluate_all",
                       return_value={"mode": "RESEARCH_ONLY_AUTHENTICATED_HELD_OUT",
                                     "production_applied": False}):
                report = restore_and_capture(
                    source, target, collector=collector, followup_rounds=3,
                    clock=clock, sleep=sleep)
            self.assertEqual(collected, [
                ("depth-001", 1000.0), ("depth-002", 1300.0),
                ("depth-003", 1600.0)])
            self.assertEqual(report["rounds_verified"], 4)
            self.assertEqual(report["followup_rounds_acquired"], 3)
            self.assertEqual(len((target/"entry"/"round-index.jsonl").read_text().splitlines()), 4)
            import json
            self.assertEqual(json.loads((target/"continuation-report.json").read_text()),
                             report)
            self.assertFalse(report["production_applied"])

    def test_hourly_rescore_appends_new_predictions_before_verified_depth(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "original"
            entry = seed(source)
            original = (entry / "scores" / (PID + ".json")).read_bytes()
            events = []
            elapsed = [1000.0]
            def score(directory, *, allowed_pairs, allow_empty):
                events.append("score")
                self.assertEqual(allowed_pairs, ["XBTUSD"])
                self.assertTrue(allow_empty)
                capture_score(directory, prediction_id="b" * 64, pair="XBTUSD",
                              baseline_score=51, challenger_score=52,
                              observed_at=1700000001.5)
                return {"captures": 1}
            def collect(pairs, directory):
                events.append("depth")
                directory.mkdir()
                fixture(directory)
            def bind(scores, index, associations):
                events.append("associate")
                self.assertEqual(len(list(Path(scores).glob("*.json"))), 1)
                self.assertEqual(len(Path(index).read_text().splitlines()), 2)
                self.assertTrue((Path(scores) / ("b" * 64 + ".json")).exists())
                return {"associated": ["b" * 64], "excluded": []}
            with patch("research.restore_scored_series.associate_indexed_captures",
                       side_effect=bind), patch(
                           "research.restore_scored_series.evaluate_all",
                           return_value={"mode": "RESEARCH_ONLY_AUTHENTICATED_HELD_OUT",
                                         "production_applied": False}):
                report = restore_and_capture(
                    source, root / "continued", collector=collect,
                    rescore=True, scorer=score, followup_rounds=2,
                    clock=lambda: elapsed[0],
                    sleep=lambda n: elapsed.__setitem__(0, elapsed[0] + n))
            self.assertEqual(events, ["score", "depth", "associate", "depth"])
            self.assertEqual(report["new_scored_candidates"], 1)
            self.assertEqual(report["new_source_associations"], 1)
            self.assertIsNone(report["rescore_failure_class"])
            self.assertEqual(len(load_captures(root / "continued" / "entry" / "scores")), 2)
            self.assertEqual((source / "entry" / "scores" / (PID + ".json")).read_bytes(),
                             original)
            self.assertEqual((root / "continued" / "entry" / "scores" /
                              (PID + ".json")).read_bytes(), original)

    def test_scoring_unavailable_preserves_source_continuation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            seed(root / "original")
            def unavailable(*args, **kwargs):
                raise ConnectionError("Kraken temporarily unavailable")
            def collect(pairs, directory):
                directory.mkdir()
                fixture(directory)
            with patch("research.restore_scored_series.evaluate_all",
                       return_value={"production_applied": False}):
                report = restore_and_capture(root / "original", root / "continued",
                                             collector=collect, rescore=True,
                                             scorer=unavailable, followup_rounds=1)
            self.assertEqual(report["rescore_failure_class"], "ConnectionError")
            self.assertEqual(report["new_scored_candidates"], 0)
            self.assertEqual(report["rounds_verified"], 2)
            self.assertEqual(len((root / "continued" / "entry" /
                                  "round-index.jsonl").read_text().splitlines()), 2)

    def test_continuation_waits_for_next_real_receipt_slot(self):
        from research.prospective_outcome_adapter import verified_rows
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "original"
            entry = seed(source)
            verified, _ = verified_rows(entry / "depth")
            last_observed = max(float(row["first_observed_at"]) for row in verified)
            elapsed = [1000.0]
            arrivals = []
            def collect(pairs, directory):
                arrivals.append(elapsed[0])
                directory.mkdir()
                fixture(directory)
            with patch("research.restore_scored_series.evaluate_all",
                       return_value={"mode": "RESEARCH_ONLY_AUTHENTICATED_HELD_OUT",
                                     "production_applied": False}):
                report = restore_and_capture(
                    source, root / "continued", collector=collect,
                    followup_rounds=1, clock=lambda: elapsed[0],
                    epoch_clock=lambda: last_observed + 180,
                    sleep=lambda n: elapsed.__setitem__(0, elapsed[0] + n))
            self.assertEqual(arrivals, [1120.0])
            self.assertEqual(report["resume_wait_seconds"], 120)
            self.assertEqual(report["rounds_verified"], 2)

    def test_mature_48h_archive_remains_extendable_for_later_scored_cohorts(self):
        # Exactly 577 real indexed rounds mature the original 48-hour entry,
        # but newly scored hourly entrants need another 48 hours of evidence.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "original"
            entry = seed(source)
            index = entry / "round-index.jsonl"
            import json
            index_rows = [json.loads(index.read_text())]
            for i in range(1, 577):
                directory = source / ("depth-%03d" % i)
                directory.mkdir()
                fixture(directory)
                index_rows.append({
                    "batch": str(directory.resolve()),
                    "manifest_sha256": hashlib.sha256(
                        (directory / "manifest.json").read_bytes()).hexdigest(),
                    "snapshots_verified": 1, "abstentions": 0})
            # The archive represents independently captured immutable rounds;
            # write its index once instead of 576 redundant fsync/lock cycles.
            index.write_text("".join(json.dumps(row, sort_keys=True) + "\\n"
                                     for row in index_rows))
            self.assertEqual(len(index.read_text().splitlines()), 577)
            def collect(pairs, directory):
                self.assertEqual(pairs, ["XBTUSD"])
                directory.mkdir()
                fixture(directory)
            with patch("research.restore_scored_series.evaluate_all",
                       return_value={"mode": "RESEARCH_ONLY_AUTHENTICATED_HELD_OUT",
                                     "production_applied": False}):
                result = restore_and_capture(
                    source, root / "extended", collector=collect,
                    followup_rounds=2)
            self.assertEqual(result["rounds_verified"], 579)
            self.assertEqual(result["followup_rounds_acquired"], 2)
            self.assertTrue((root / "extended" / "depth-578" / "manifest.json").exists())
            self.assertFalse(result["production_applied"])

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
