import json
import tempfile
import unittest
from pathlib import Path

from research.capture_acquisition_scores import capture_score, attach_verified_depth

PID = "a" * 64


class CaptureTests(unittest.TestCase):
    def test_capture_then_bind_depth_without_rewriting_original(self):
        with tempfile.TemporaryDirectory() as d:
            captured = capture_score(d, prediction_id=PID, pair="XBTUSD",
                                     baseline_score=1.5, challenger_score=2.0,
                                     observed_at=999)
            before = Path(captured["path"]).read_bytes()
            bound = attach_verified_depth(captured, {
                "pair": "XBTUSD", "source_sha256": "b" * 64,
                "first_observed_at": 1000})
            self.assertEqual(bound["score_observed_at"], 999)
            self.assertEqual(bound["source_sha256"], "b" * 64)
            self.assertEqual(before, Path(captured["path"]).read_bytes())
            self.assertEqual(json.loads(before)["mode"], "RESEARCH_ONLY")

    def test_exclusive_creation_blocks_retroactive_rewrite(self):
        with tempfile.TemporaryDirectory() as d:
            capture_score(d, prediction_id=PID, pair="XBTUSD",
                          baseline_score=1, challenger_score=2, observed_at=999)
            with self.assertRaises(FileExistsError):
                capture_score(d, prediction_id=PID, pair="XBTUSD",
                              baseline_score=999, challenger_score=2, observed_at=998)

    def test_fail_closed_late_score_and_pair(self):
        with tempfile.TemporaryDirectory() as d:
            captured = capture_score(d, prediction_id=PID, pair="XBTUSD",
                                     baseline_score=1, challenger_score=2,
                                     observed_at=1001)
            with self.assertRaisesRegex(ValueError, "after depth"):
                attach_verified_depth(captured, {
                    "pair": "XBTUSD", "source_sha256": "b" * 64,
                    "first_observed_at": 1000})
            with self.assertRaisesRegex(ValueError, "pair mismatch"):
                attach_verified_depth(captured, {
                    "pair": "ETHUSD", "source_sha256": "b" * 64,
                    "first_observed_at": 2000})

    def test_invalid_scores_rejected_without_file(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaisesRegex(ValueError, "nonfinite"):
                capture_score(d, prediction_id=PID, pair="XBTUSD",
                              baseline_score=float("nan"), challenger_score=2)
            self.assertEqual(list(Path(d).iterdir()), [])


if __name__ == "__main__":
    unittest.main()
