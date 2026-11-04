"""Bounded scored-entry to prospective depth-series acceptance (no network/sleep)."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from research.live_scored_series import capture_scored_series


class ScoredSeriesTests(unittest.TestCase):
    def test_one_scored_entry_and_two_real_followups_keep_original_receipt(self):
        events = []
        elapsed = [1000.]
        def clock():
            return elapsed[0]
        def sleep(seconds):
            self.assertGreater(seconds, 0)
            elapsed[0] += seconds
        def entry(root):
            events.append(("score_then_depth", clock()))
            (root / "scores").mkdir(parents=True)
            (root / "scores" / ("a" * 64 + ".json")).write_text('{"proof":"sealed"}')
            (root / "round-index.jsonl").write_text('{"entry":true}\n')
            return {"mode": "RESEARCH_ONLY_PROSPECTIVE_SCORE_DEPTH",
                    "production_applied": False}
        def collector(pairs, directory):
            events.append(("depth", clock(), tuple(pairs)))
            directory.mkdir()
        def indexer(index, directory):
            self.assertTrue(directory.is_dir())
            with Path(index).open("a") as handle:
                handle.write(json.dumps({"batch": str(directory)}) + "\n")
            events.append(("index", directory.name))
        def evaluate(index, hours):
            self.assertEqual(len(Path(index).read_text().splitlines()), 3)
            return {"horizon_hours": hours, "qualified": 0,
                    "status": "ABSTAIN_INCOMPLETE"}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "series"
            with patch("research.live_scored_series.load_captures",
                       return_value=[{"pair": "TAOUSD"}]), patch(
                           "research.live_scored_series.evaluate_all",
                           return_value={"mode": "RESEARCH_ONLY_AUTHENTICATED_HELD_OUT",
                                         "production_applied": False}):
                result = capture_scored_series(
                    root, rounds=3, clock=clock, sleep=sleep,
                    entry_capture=entry, collector=collector,
                    indexer=indexer, evaluate=evaluate)
            self.assertEqual(json.loads((root / "series-report.json").read_text()), result)
            self.assertEqual((root / "entry" / "scores" / ("a" * 64 + ".json")).read_text(),
                             '{"proof":"sealed"}')
            self.assertEqual(result["rounds_indexed"], 3)
            self.assertFalse(result["production_applied"])
            self.assertFalse(result["trading_approved"])
            self.assertEqual(set(result["coverage"]), {"1", "6", "24", "48"})
        self.assertEqual(events, [
            ("score_then_depth", 1000.0),
            ("depth", 1300.0, ("TAOUSD",)), ("index", "depth-001"),
            ("depth", 1600.0, ("TAOUSD",)), ("index", "depth-002")])

    def test_slow_scanner_does_not_shift_first_real_depth_slot_early(self):
        elapsed = [1000.0]
        followups = []
        def entry(root):
            (root / "scores").mkdir(parents=True)
            (root / "round-index.jsonl").write_text("entry\\n")
            elapsed[0] += 160
            return {"mode": "RESEARCH_ONLY_PROSPECTIVE_SCORE_DEPTH",
                    "production_applied": False}
        def collector(pairs, directory):
            followups.append(elapsed[0])
            directory.mkdir()
        def append(index, directory):
            with Path(index).open("a") as handle:
                handle.write("next\\n")
        with tempfile.TemporaryDirectory() as tmp:
            with patch("research.live_scored_series.load_captures",
                       return_value=[{"pair": "TAOUSD"}]), patch(
                           "research.live_scored_series.evaluate_all",
                           return_value={"mode": "RESEARCH_ONLY_AUTHENTICATED_HELD_OUT",
                                         "production_applied": False}):
                capture_scored_series(Path(tmp) / "series", rounds=2,
                                      clock=lambda: elapsed[0],
                                      sleep=lambda n: elapsed.__setitem__(0, elapsed[0] + n),
                                      entry_capture=entry, collector=collector,
                                      indexer=append,
                                      evaluate=lambda *_: {"qualified_first_entry_episodes": 0})
        self.assertEqual(followups, [1460.0])

    def test_entry_failure_does_not_claim_rounds(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "series"
            with self.assertRaisesRegex(ValueError, "not a research-only"):
                capture_scored_series(root, rounds=2,
                    entry_capture=lambda _: {"mode": "LIVE", "production_applied": True})
            self.assertFalse((root / "series-report.json").exists())

    def test_missing_entry_index_rejected_without_followup(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "series"
            def entry(folder):
                (folder / "scores").mkdir(parents=True)
                return {"mode": "RESEARCH_ONLY_PROSPECTIVE_SCORE_DEPTH",
                        "production_applied": False}
            with patch("research.live_scored_series.load_captures",
                       return_value=[{"pair": "TAOUSD"}]):
                with self.assertRaisesRegex(ValueError, "entry depth round"):
                    capture_scored_series(root, rounds=2, entry_capture=entry)
            self.assertFalse((root / "depth-001").exists())

    def test_interrupted_followup_never_claims_complete_evidence(self):
        elapsed = [500.0]
        def entry(folder):
            (folder / "scores").mkdir(parents=True)
            (folder / "round-index.jsonl").write_text('{"entry":true}\n')
            return {"mode": "RESEARCH_ONLY_PROSPECTIVE_SCORE_DEPTH",
                    "production_applied": False}
        def fail_second_source(pairs, directory):
            if directory.name == "depth-002":
                raise OSError("Kraken network failure")
            directory.mkdir()
        def append(index, directory):
            with Path(index).open("a") as out:
                out.write(json.dumps({"batch": str(directory)}) + "\n")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "series"
            with patch("research.live_scored_series.load_captures",
                       return_value=[{"pair": "TAOUSD"}]):
                with self.assertRaisesRegex(OSError, "network failure"):
                    capture_scored_series(root, rounds=3, clock=lambda: elapsed[0],
                                          sleep=lambda seconds: elapsed.__setitem__(0, elapsed[0] + seconds),
                                          entry_capture=entry, collector=fail_second_source,
                                          indexer=append)
            self.assertEqual(len((root / "entry" / "round-index.jsonl").read_text().splitlines()), 2)
            self.assertFalse((root / "series-report.json").exists())

    def test_bounds_and_existing_series_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            for n in (0, 1, 14, True, 2.0):
                with self.subTest(rounds=n), self.assertRaises(ValueError):
                    capture_scored_series(Path(tmp) / "x", rounds=n)
            with self.assertRaisesRegex(ValueError, "interval"):
                capture_scored_series(Path(tmp) / "y", rounds=2, interval_seconds=299)
            existing = Path(tmp) / "existing"
            existing.mkdir()
            with self.assertRaises(FileExistsError):
                capture_scored_series(existing, rounds=2)


if __name__ == "__main__":
    unittest.main()
