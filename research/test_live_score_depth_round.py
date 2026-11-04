import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from research.live_score_depth_round import run


class LiveScoreDepthRoundTests(unittest.TestCase):
    def test_scores_are_sealed_before_same_market_depth_and_binding(self):
        events = []
        def capture(path):
            events.append("score")
            Path(path).mkdir(parents=True)
            return {"captures": 2}
        def load(path):
            return [{"pair": "XBTUSD"}, {"pair": "ETHUSD"}]
        def collect(pairs, path):
            events.append("depth")
            self.assertEqual(pairs, ["XBTUSD", "ETHUSD"])
            Path(path).mkdir()
            return {"pairs_requested": 2, "pairs_eligible": 2}
        def append(index, depth):\n            events.append("index")\n            Path(index).write_text("indexed\\n")\n            return {"snapshots_verified": 2}\n        def associate(scores, index, associations):
            events.append("associate")
            self.assertTrue((Path(scores)).is_dir())
            self.assertTrue(Path(index).is_file())
            Path(associations).mkdir()
            return {"associated": ["a"], "excluded": []}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "round"
            with patch("research.live_score_depth_round.capture_live_scan", side_effect=capture), \
                 patch("research.live_score_depth_round.load_captures", side_effect=load), \
                 patch("research.live_score_depth_round.collect", side_effect=collect), \
                 patch("research.live_score_depth_round.associate_captured_scores", side_effect=associate):
                result = run(root)
        self.assertEqual(events, ["score", "depth", "index", "associate"])
        self.assertEqual(result["associated"], 1)
        self.assertFalse(result["production_applied"])

    def test_existing_round_directory_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "existing"
            root.mkdir()
            with self.assertRaises(FileExistsError):
                run(root)


if __name__ == "__main__":
    unittest.main()
