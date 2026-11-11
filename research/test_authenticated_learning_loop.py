"""Connected E1-E3 acceptance: real verified source fixture and chronological score comparison."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from research.capture_acquisition_scores import capture_score
from research.prospective_round_store import append_round
from research.test_prospective_outcome_adapter import fixture
from research.authenticated_learning_loop import compare, evaluate_all, _extract, evaluate_cohorts


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

    def test_same_raw_kraken_sha_acquired_twice_never_backfills_wrong_outcome(self):
        sha = "f" * 64
        score = {"prediction_id": "a" * 64, "pair": "XBTUSD",
                 "source_sha256": sha, "source_first_observed_at": 2000,
                 "score_observed_at": 1999,
                 "baseline_score": 20.0, "challenger_score": 22.0}
        rows = [
            {"pair": "XBTUSD", "entry_source_sha256": sha,
             "entry_first_observed_at": at, "entry_liquidity_usd": 100,
             "status": "QUALIFIED_OBSERVED_PATH", "ge30pct": hit}
            for at, hit in ((1000, True), (2000, False))]
        from contextlib import ExitStack
        with ExitStack() as stack:
            stack.enter_context(patch("research.authenticated_learning_loop.load_captures",
                                      return_value=[score]))
            stack.enter_context(patch("research.authenticated_learning_loop.verified_associations",
                                      return_value=([score], [], {"source_abstentions": []})))
            stack.enter_context(patch("research.authenticated_learning_loop.evaluate_index",
                                      return_value={"outcomes": rows, "snapshots_verified": 2}))
            stack.enter_context(patch("research.authenticated_learning_loop.Path.is_dir",
                                      return_value=True))
            result = _extract("scores", "associations", "rounds", 1)
        self.assertEqual(len(result["qualified"]), 1)
        self.assertFalse(result["qualified"][0]["positive"])
        # Legacy captures without acquisition timestamps may not select an
        # arbitrary one of multiple otherwise identical source payloads.
        legacy = dict(score)
        legacy.pop("source_first_observed_at")
        with ExitStack() as stack:
            stack.enter_context(patch("research.authenticated_learning_loop.load_captures",
                                      return_value=[legacy]))
            stack.enter_context(patch("research.authenticated_learning_loop.verified_associations",
                                      return_value=([legacy], [], {"source_abstentions": []})))
            stack.enter_context(patch("research.authenticated_learning_loop.evaluate_index",
                                      return_value={"outcomes": rows, "snapshots_verified": 2}))
            stack.enter_context(patch("research.authenticated_learning_loop.Path.is_dir",
                                      return_value=True))
            denied = _extract("scores", "associations", "rounds", 1)
        self.assertEqual(denied["qualified"], [])
        self.assertEqual(denied["abstentions"][0]["reason"],
                         "AMBIGUOUS_SOURCE_OUTCOME")

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


    def test_ten_independently_verified_cohorts_one_held_out_split(self):
        from contextlib import ExitStack
        with tempfile.TemporaryDirectory() as tmp:
            roots = [Path(tmp) / ("cohort-%02d" % k) for k in range(10)]
            for root in roots:
                (root / "entry" / "associations").mkdir(parents=True)
            captures, outcomes = {}, {}
            for k, root in enumerate(roots):
                key = str(root / "entry")
                captures[key] = []
                outcomes[key] = []
                for j in range(20):
                    i = 20 * k + j
                    pid, sha = format(i, "064x"), format(1000 + i, "064x")
                    observed = 1700000000 + i * 3600
                    captures[key].append({
                        "prediction_id": pid, "pair": "XBTUSD",
                        "source_sha256": sha, "score_observed_at": observed - 2,
                        "baseline_score": float(i),
                        "challenger_score": float(200-i)})
                    outcomes[key].append({
                        "pair": "XBTUSD", "entry_source_sha256": sha,
                        "entry_first_observed_at": observed,
                        "entry_liquidity_usd": 100.0,
                        "status": "QUALIFIED_OBSERVED_PATH", "ge30pct": i % 5 == 0})
            def key_for(path):
                return str(Path(path).parent)
            with ExitStack() as stack:
                stack.enter_context(patch(
                    "research.authenticated_learning_loop.load_captures",
                    side_effect=lambda path: captures[key_for(path)]))
                stack.enter_context(patch(
                    "research.authenticated_learning_loop.verified_associations",
                    side_effect=lambda scores, associations, index:
                        (captures[key_for(scores)], [], {"source_abstentions": []})))
                stack.enter_context(patch(
                    "research.authenticated_learning_loop.evaluate_index",
                    side_effect=lambda index, hours:
                        {"outcomes": outcomes[key_for(index)], "snapshots_verified": 20}))
                result = evaluate_cohorts(roots, ledger_path=Path(tmp) / "shadow.jsonl")
            comparison = result["horizons"]["48"]["comparison"]
            self.assertEqual(result["cohorts"], 10)
            self.assertEqual(set(result["horizons"]), {"1", "6", "24", "48"})
            self.assertEqual(comparison["qualified_n"], 200)
            self.assertEqual(comparison["held_out_n"], 60)
            self.assertEqual(comparison["train_n"], 92)
            self.assertEqual(comparison["baseline"]["top_decile_n"], 6)
            self.assertEqual(comparison["challenger"]["top_decile_n"], 6)
            self.assertEqual(comparison["rule"], "QUALIFIED_COMPARISON")
            self.assertEqual(result["shadow_decision"]["decision"], "SHADOW_ELIGIBLE_REVIEW")
            self.assertFalse(result["production_applied"])
            self.assertEqual(len((Path(tmp) / "shadow.jsonl").read_text().splitlines()), 1)

    def test_repeated_cohort_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "cohort"
            root.mkdir()
            with self.assertRaisesRegex(ValueError, "distinct"):
                evaluate_cohorts([root, root])


if __name__ == "__main__":
    unittest.main()
