"""Focused bounded repeated-capture tests without network or sleeping."""
import tempfile
import unittest
from pathlib import Path

from research.kraken_capture_rounds import capture_rounds
from research.test_prospective_outcome_adapter import fixture


class CaptureRoundsTests(unittest.TestCase):
    def test_two_rounds_are_indexed_with_truthful_incomplete_coverage(self):
        with tempfile.TemporaryDirectory() as tmp:
            now = [1000]
            calls = []

            def collector(pairs, directory):
                calls.append((tuple(pairs), str(directory)))
                Path(directory).mkdir()
                fixture(Path(directory))

            def sleep(seconds):
                now[0] += seconds

            result = capture_rounds(
                ["XBTUSD"], Path(tmp) / "run", rounds=2,
                collector=collector, clock=lambda: now[0], sleep=sleep)
            self.assertEqual(len(calls), 2)
            self.assertEqual(now[0], 1300)
            self.assertEqual(result["rounds_indexed"], 2)
            self.assertEqual(result["coverage"]["snapshots_verified"], 2)
            self.assertEqual(result["coverage"]["qualified_first_entry_episodes"], 0)

    def test_unbounded_or_too_fast_capture_rejected_before_io(self):
        with tempfile.TemporaryDirectory() as tmp:
            for options in ({"rounds": 13}, {"rounds": 0},
                            {"interval_seconds": 299}):
                with self.assertRaises(ValueError):
                    capture_rounds(["XBTUSD"], Path(tmp) / "not-created", **options)
            self.assertFalse((Path(tmp) / "not-created").exists())


if __name__ == "__main__":
    unittest.main()
