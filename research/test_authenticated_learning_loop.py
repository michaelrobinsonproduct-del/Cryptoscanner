"""Connected E1-E3 acceptance: real verified source fixture and chronological score comparison."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from research.capture_acquisition_scores import capture_score
from research.prospective_round_store import append_round
from research.test_prospective_outcome_adapter import fixture
from research.authenticated_learning_loop import compare, evaluate_all


class AuthenticatedLearningTests(unittest.TestCase):
    def test_real_source_bytes_without_contiguous_path_keep_baseline(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            capture_score(root / "scores", prediction_id="a" * 64, pair="XBTUSD",
                          baseline_score=40, challenger_score=41, observed_at=1700000001)
            depth = root / "depth"
            depth.mkdir()
            fixture(depth)
            index = root / "rounds.jsonl"
            append_round(index, depth)
            report = evaluate_all(root / "scores", root / "missing-associations", index,
                                  ledger_path=root / "shadow.jsonl")
            self.assertEqual(set(report["horizons"]), {"1", "6", "24", "48"})
            for horizon in report["horizons"].values():
                self.assertEqual(horizon["comparison"]["qualified_n"], 0)
                self.assertEqual(horizon["comparison"]["held_out_n"], 0)
                self.assertEqual(horizon["shadow_decision"]["decision"], "KEEP_BASELINE")
            self.assertEqual(len((root / "shadow.jsonl").read_text().splitlines()), 1)

    def test_identical_held_out_cohort_with_48h_purge(self):
        rows = []
        outcomes = []
        for i in range(100):
            pid = format(i, "064x")
            sha = format(i + 1000, "064x")
            observed = 1700000000 + i * 3600
            rows.append({"prediction_id": pid, "pair": "XBTUSD",
                         "source_sha256": sha, "score_observed_at": observed - 2,
                         "baseline_score": float(i), "challenger_score": float(100-i)})
            outcomes.append({"pair": "XBTUSD", "entry_source_sha256": sha,
                             "entry_first_observed_at": observed,
                             "entry_liquidity_usd": 100.0,
                             "status": "QUALIFIED_OBSERVED_PATH",
                             "ge30pct": i % 5 == 0})
        from contextlib import ExitStack
        with ExitStack() as stack:
            stack.enter_context(patch("research.authenticated_learning_loop.load_captures", return_value=rows))
            stack.enter_context(patch("research.authenticated_learning_loop.verified_associations",
                                      return_value=(rows, [], {"source_abstentions": []})))
            stack.enter_context(patch("research.authenticated_learning_loop.evaluate_index",
                                      return_value={"outcomes": outcomes, "snapshots_verified": 100}))
            stack.enter_context(patch("research.authenticated_learning_loop.Path.is_dir", return_value=True))
            report = compare("scores", "associations", "rounds")
        result = report["comparison"]
        self.assertEqual(result["qualified_n"], 100)
        self.assertEqual(result["held_out_n"], 30)
        self.assertEqual(result["train_n"], 22)
        self.assertEqual(result["baseline"]["top_decile_n"], 3)
        self.assertEqual(result["challenger"]["top_decile_n"], 3)
        self.assertEqual(report["shadow_decision"]["decision"], "KEEP_BASELINE")


if __name__ == "__main__":
    unittest.main()
