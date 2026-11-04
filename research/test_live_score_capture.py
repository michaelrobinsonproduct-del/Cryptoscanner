"""Fixture-backed research live scoring capture, never historical replay."""
import datetime as dt
import tempfile
import unittest
from pathlib import Path

from research.live_score_capture import capture_live_scan
from research.acquisition_receipt_pipeline import load_captures

UTC = dt.timezone.utc


class LiveCaptureTests(unittest.TestCase):
    def test_scoring_to_immutable_receipt(self):
        with tempfile.TemporaryDirectory() as root:
            now = dt.datetime(2026, 11, 3, tzinfo=UTC)
            report = {"mode": "PAPER_ONLY", "production_applied": False,
                      "as_of": now.isoformat(), "watch": [{
                          "prediction_id": "a"*64, "pair": "XBTUSD",
                          "status": "PAPER_WATCH", "as_of": now.isoformat(),
                          "baseline_score": 10, "challenger_score": 12}]}
            result = capture_live_scan(Path(root), scanner=lambda: report, clock=lambda: now)
            self.assertEqual(result["captures"], 1)
            self.assertEqual(load_captures(root)[0]["score_observed_at"], now.timestamp())
            with self.assertRaises(FileExistsError):
                capture_live_scan(root, scanner=lambda: report, clock=lambda: now)

    def test_historical_replay_abstains(self):
        with tempfile.TemporaryDirectory() as root:
            now = dt.datetime(2026, 11, 3, tzinfo=UTC)
            old = now-dt.timedelta(hours=1)
            report = {"mode": "PAPER_ONLY", "production_applied": False,
                      "as_of": old.isoformat(), "watch": [{"status": "PAPER_WATCH"}]}
            with self.assertRaisesRegex(ValueError, "synchronous"):
                capture_live_scan(root, scanner=lambda: report, clock=lambda: now)
            self.assertEqual(list(Path(root).glob("*.json")), [])


if __name__ == "__main__":
    unittest.main()
