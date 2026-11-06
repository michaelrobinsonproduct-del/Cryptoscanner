"""Focused learned paper overlay acceptance: frozen E state, same-scan rejection."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from paper_pov.learned_score_overlay import score_future_paper_predictions, candidate_features


def sealed_state():
    challenger = {"version": "frozen-1", "status": "SHADOW_ONLY",
                  "feature_names": ["baseline_score", "momentum_15m", "volume_acceleration"],
                  "feature_centers": {"baseline_score": 50, "momentum_15m": 0, "volume_acceleration": 1},
                  "feature_scales": {"baseline_score": 10, "momentum_15m": 0.01, "volume_acceleration": 1},
                  "feature_weights": {"baseline_score": 1, "momentum_15m": 1, "volume_acceleration": 1}}
    state = {"schema": "paper_learning_state_v1", "challenger": challenger,
             "evaluation_asof_utc": "2026-11-01T00:00:00+00:00",
             "promotion_authorized": False, "production_applied": False}
    state["state_digest"] = hashlib.sha256(json.dumps(state, sort_keys=True,
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    return state


class LearnedOverlayTest(unittest.TestCase):
    def test_scoring_uses_e_feature_units_and_frozen_state(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "state.json"
            path.write_text(json.dumps(sealed_state()))
            published = {"candidates": [{"prediction_id": "p1", "baseline_score": 60,
                                         "move15_pct": 2, "volume_accel": 2}]}
            result = score_future_paper_predictions(path, candidate_features(published),
                        scan_asof="2026-11-02T00:00:00+00:00")
            self.assertEqual(result["status"], "SHADOW_ONLY")
            self.assertAlmostEqual(result["scores"][0]["shadow_score"], 4)
            self.assertFalse(result["production_applied"])

    def test_same_scan_and_tampered_state_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "state.json"
            state = sealed_state()
            path.write_text(json.dumps(state))
            with self.assertRaises(ValueError):
                score_future_paper_predictions(path, [], scan_asof=state["evaluation_asof_utc"])
            state["challenger"]["feature_weights"]["baseline_score"] = 99
            path.write_text(json.dumps(state))
            with self.assertRaises(ValueError):
                score_future_paper_predictions(path, [], scan_asof="2026-11-02T00:00:00+00:00")


if __name__ == "__main__":
    unittest.main()
