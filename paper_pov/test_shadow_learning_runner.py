"""Functional acceptance for paper-only outcome, learning, and persistence."""
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from paper_pov.shadow_learning_runner import score_future_paper_predictions
from paper_pov.heldout_outcome_adapter import (
    build_shadow_learning_state, read_shadow_learning_state, save_shadow_learning_state,
)

class ShadowPipelineAcceptance(unittest.TestCase):
    def test_outcome_to_persisted_state(self):
        origin = datetime(2026, 7, 1, tzinfo=timezone.utc)
        def iso(t):
            return t.isoformat()
        entries = [origin, origin + timedelta(days=3), origin + timedelta(days=8)]
        predictions = [
            {"prediction_id": str(i), "pair": "TESTUSD", "entry_utc": iso(entry),
             "feature_asof_utc": iso(entry - timedelta(minutes=5)),
             "entry_price": 100, "features": {"momentum": float(i)},
             "liquidity_qualified": True}
            for i, entry in enumerate(entries)]
        candles = []
        for entry in entries:
            for step in range(1, 577):
                t = entry + timedelta(minutes=5 * step)
                high = 135 if entry == entries[0] else 101
                candles.append({"pair": "TESTUSD", "timestamp_utc": iso(t),
                                "close": 100, "high": high})
        state = build_shadow_learning_state(
            predictions, candles, {"2": True},
            training_end_utc=iso(origin + timedelta(days=6)),
            holdout_start_utc=iso(origin + timedelta(days=8)),
            evaluation_asof_utc=iso(origin + timedelta(days=11)),
            feature_names=["momentum"])
        self.assertEqual(state["hit_counts"]["48"], 1)
        self.assertEqual(state["comparison"]["status"], "SHADOW_EVALUATED")
        self.assertFalse(state["promotion_authorized"])
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "state.json"
            save_shadow_learning_state(path, state)
            loaded = read_shadow_learning_state(path)
            self.assertEqual(loaded["state_digest"], state["state_digest"])
            future = score_future_paper_predictions(path, [{"prediction_id": "future", "features": {"momentum": 4.0}}])
            self.assertEqual(len(future["scores"]), 1)
            self.assertFalse(future["scores"][0]["watch_authorized"])

if __name__ == "__main__":
    unittest.main()
