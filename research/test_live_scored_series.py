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
            (root / "round-index.jsonl").write_text('{"entry":true}\\n')
            return {"mode": "RESEARCH_ONLY_PROSPECTIVE_SCORE_DEPTH",
                    "production_applied": False}
        def collector(pairs, directory):
            events.append(("depth", clock(), tuple(pairs)))
            directory.mkdir()
        def indexer(index, directory):
            self.assertTrue(directory.is_dir())
            with Path(index).open("a") as handle:
                handle.write(json.dumps({"batch": str(directory)}) + "\\n")
            events.append(("index", directory.name))
        def evaluate(index, hours):
            self.assertEqual(len(Path(index).read_text().splitlines()), 3)
            return {"horizon_hours": hours, "qualified": 0,
                    "status": "ABSTAIN_INCOMPLETE"}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "series"
            with patch("research.live_scored_series.load_captures",
                       return_value=[{"pair": "TAOUSD"}]):
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
