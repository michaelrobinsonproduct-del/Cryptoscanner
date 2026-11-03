"""Focused end-to-end score bytes -> immutable association -> verified depth -> binder."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from research.capture_acquisition_scores import capture_score
from research.depth_acquisition_associations import write_association, verified_associations
from research.acquisition_receipt_pipeline import evaluate, evaluate_learning, evaluate_horizons, evaluate_learning_horizons, source_only_coverage, write_new, main


class DepthAssociationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.pid = "a" * 64
        self.source = "b" * 64
        self.capture = capture_score(self.root / "scores", prediction_id=self.pid,
                                     pair="XBTUSD", baseline_score=0.2,
                                     challenger_score=0.3, observed_at=100)
        self.row = {"pair": "XBTUSD", "source_sha256": self.source,
                    "first_observed_at": 101, "entry_liquidity_usd": 25}

    def associate(self, **changes):
        args = {"prediction_id": self.pid, "pair": "XBTUSD",
                "source_sha256": self.source,
                "score_receipt_sha256": self.capture["sha256"]}
        args.update(changes)
        return write_association(self.root / "depth-links", **args)

    @patch("research.depth_acquisition_associations.verified_rows")
    def test_connect_score_to_verified_depth(self, rows):
        from research.depth_acquisition_associations import associate_captured_scores
        rows.return_value = ([self.row], [])
        result = associate_captured_scores(self.root / "scores", self.root / "raw",
                                           self.root / "depth-links")
        self.assertEqual(result["associated"], [self.pid])
        self.assertEqual(result["excluded"], [])
        bound, exclusions, _ = verified_associations(
            self.root / "scores", self.root / "depth-links", self.root / "raw")
        self.assertEqual((len(bound), exclusions), (1, []))
        self.assertEqual(bound[0]["source_sha256"], self.source)

    @patch("research.depth_acquisition_associations.verified_rows")
    def test_connector_cli_persists_association_report(self, rows):
        from research.depth_acquisition_associations import main as association_main
        rows.return_value = ([self.row], [])
        output = self.root / "association-report.json"
        with patch.object(sys, "argv", ["associate",
                "--captures-directory", str(self.root / "scores"),
                "--depth-directory", str(self.root / "raw"),
                "--associations-directory", str(self.root / "depth-links"),
                "--report", str(output)]):
            association_main()
        report = json.loads(output.read_text())
        self.assertEqual(report["associated"], [self.pid])
        self.assertFalse(report["production_applied"])

    def test_auto_association_invalid_arguments_do_not_write(self):
        with patch.object(sys, "argv", ["pipeline",
                "--captures-directory", str(self.root / "scores"),
                "--depth-directory", str(self.root / "raw"),
                "--associations-directory", str(self.root / "depth-links"),
                "--associate-verified-depth", "--output", str(self.root / "report.json")]):
            with self.assertRaises(SystemExit):
                main()
        self.assertFalse((self.root / "depth-links").exists())

    @patch("research.depth_acquisition_associations.verified_rows")
    @patch("research.acquisition_receipt_pipeline.bind")
    def test_pipeline_auto_associates_before_evaluation(self, binder, rows):
        rows.return_value = ([self.row], [])
        binder.return_value = {"accepted": [], "excluded_count": 0,
                               "source_abstentions": [], "verified_depth_rows": 1}
        ledger = self.root / "paper.json"
        ledger.write_text("{}")
        output = self.root / "auto-evaluation.json"
        with patch.object(sys, "argv", ["pipeline", "--paper-ledger", str(ledger),
                "--captures-directory", str(self.root / "scores"),
                "--depth-directory", str(self.root / "raw"),
                "--associations-directory", str(self.root / "depth-links"),
                "--associate-verified-depth", "--output", str(output)]):
            main()
        self.assertTrue((self.root / "depth-links" / (self.pid + ".json")).exists())
        self.assertEqual(json.loads(output.read_text())["capture_count"], 1)

    @patch("research.depth_acquisition_associations.verified_rows")
    def test_indexed_round_association(self, rows):
        from research.depth_acquisition_associations import associate_indexed_captures
        rows.return_value = ([self.row], [])
        batch = self.root / "round"
        batch.mkdir()
        (batch / "manifest.json").write_text("{}")
        index = self.root / "rounds.jsonl"
        index.write_text(json.dumps({
            "batch": str(batch),
            "manifest_sha256": hashlib.sha256(b"{}").hexdigest(),
            "snapshots_verified": 1, "abstentions": 0}) + "\n")
        result = associate_indexed_captures(self.root / "scores", index,
                                            self.root / "depth-links")
        self.assertEqual(result["associated"], [self.pid])
        self.assertEqual(result["rounds_verified"], 1)
        self.assertFalse(result["production_applied"])

    @patch("research.depth_acquisition_associations.verified_rows")
    def test_connector_abstains_on_missing_depth(self, rows):
        from research.depth_acquisition_associations import associate_captured_scores
        rows.return_value = ([], [])
        result = associate_captured_scores(self.root / "scores", self.root / "raw",
                                           self.root / "depth-links")
        self.assertEqual(result["associated"], [])
        self.assertEqual(result["excluded"][0]["reason"], "NO_UNIQUE_TIMELY_DEPTH")

    @patch("research.depth_acquisition_associations.verified_rows")
    def test_real_score_bytes_to_verified_depth_and_report(self, rows):
        rows.return_value = ([self.row], [])
        self.associate()
        captures, excluded, coverage = verified_associations(
            self.root / "scores", self.root / "depth-links", self.root / "raw")
        self.assertEqual((len(captures), excluded, coverage["verified_depth_rows"]), (1, [], 1))
        self.assertEqual(captures[0]["source_sha256"], self.source)
        with patch("research.acquisition_receipt_pipeline.bind") as binder:
            binder.return_value = {"accepted_count": 1, "excluded_count": 0,
                                   "source_abstentions": [], "accepted": captures}
            report = evaluate({}, self.root / "raw", self.root / "scores",
                              self.root / "depth-links")
            self.assertEqual(report["capture_count"], 1)
            self.assertEqual(report["reconciliation_receipt_count"], 1)
            self.assertEqual(report["reconciliation_receipts"][0]["source_sha256"], self.source)
            self.assertEqual(report["association_excluded_count"], 0)
            self.assertFalse(report["production_applied"])
            self.assertEqual(binder.call_args.args[2][0]["source_sha256"], self.source)
            path = self.root / "result.json"
            write_new(path, report)
            with self.assertRaises(FileExistsError):
                write_new(path, report)

    @patch("research.depth_acquisition_associations.verified_rows")
    def test_missing_and_unverified_source_abstain(self, rows):
        rows.return_value = ([self.row], [])
        (self.root / "depth-links").mkdir()
        captures, exclusions, _ = verified_associations(
            self.root / "scores", self.root / "depth-links", self.root / "raw")
        self.assertEqual(captures, [])
        self.assertEqual(exclusions[0]["reason"], "MISSING_DEPTH_ASSOCIATION")
        self.associate(source_sha256="c" * 64)
        captures, exclusions, _ = verified_associations(
            self.root / "scores", self.root / "depth-links", self.root / "raw")
        self.assertEqual(captures, [])
        self.assertEqual(exclusions[0]["reason"], "UNVERIFIED_DEPTH_ASSOCIATION")

    @patch("research.depth_acquisition_associations.verified_rows")
    def test_score_tampering_and_late_score_fail_closed(self, rows):
        rows.return_value = ([self.row], [])
        self.associate()
        path = Path(self.capture["path"])
        doc = json.loads(path.read_text())
        doc["baseline_score"] = 0.99
        path.write_text(json.dumps(doc))
        captures, excluded, _ = verified_associations(
            self.root / "scores", self.root / "depth-links", self.root / "raw")
        self.assertEqual(captures, [])
        self.assertEqual(excluded[0]["reason"], "SCORE_ASSOCIATION_MISMATCH")
        path.write_text(json.dumps(self.capture["receipt"], sort_keys=True, separators=(",", ":")) + "\n")
        rows.return_value = ([{**self.row, "first_observed_at": 99}], [])
        captures, excluded, _ = verified_associations(
            self.root / "scores", self.root / "depth-links", self.root / "raw")
        self.assertEqual(excluded[0]["reason"], "SCORE_NOT_PRE_ENTRY")

    def test_no_association_directory_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "authenticated depth associations required"):
            evaluate({}, self.root / "raw", self.root / "scores")

    @patch("research.depth_acquisition_associations.verified_rows")
    def test_unverified_association_never_exported_to_reconciliation(self, rows):
        rows.return_value = ([self.row], [])
        self.associate(source_sha256="c" * 64)
        with patch("research.acquisition_receipt_pipeline.bind") as binder:
            binder.return_value = {"accepted": [], "accepted_count": 0,
                                   "excluded_count": 0, "source_abstentions": []}
            report = evaluate({}, self.root / "raw", self.root / "scores",
                              self.root / "depth-links")
            self.assertEqual(report["capture_count"], 1)
            self.assertEqual(report["reconciliation_receipts"], [])
            self.assertEqual(report["association_excluded_count"], 1)
            self.assertEqual(binder.call_args.args[2], [])

    @patch("research.prospective_round_store.evaluate_index")
    def test_all_horizons_keep_censored_paths_out_of_hit_denominator(self, evaluate_index):
        def fixture(_, hours):
            return {"rounds_verified": 13, "snapshots_verified": 52,
                    "outcomes": ([{"status": "QUALIFIED_OBSERVED_PATH", "ge30pct": False}]
                                 if hours == 1 else []) + [{"status": "INCOMPLETE_FUTURE_PATH"}] * (48 if hours == 1 else 52),
                    "abstentions": []}
        evaluate_index.side_effect = fixture
        result = evaluate_horizons("fixture-index")
        self.assertEqual(list(result), ["1", "6", "24", "48"])
        self.assertEqual(result["1"]["qualified"], 1)
        self.assertEqual(result["1"]["observed_ge30pct"], 0)
        self.assertEqual(result["1"]["incomplete_or_unqualified"], 48)
        self.assertEqual(result["48"]["qualified"], 0)
        self.assertEqual(result["48"]["incomplete_or_unqualified"], 52)
        self.assertTrue(all(not v["production_applied"] for v in result.values()))
        self.assertEqual(evaluate_index.call_count, 4)

    def test_unsupported_horizon_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "unsupported evaluation horizon"):
            evaluate_horizons("unused", (72,))

    @patch("research.acquisition_receipt_pipeline.evaluate_horizons")
    @patch("research.acquisition_receipt_pipeline.evaluate")
    def test_coverage_only_cli_persists_readable_report(self, evaluate, horizons):
        ledger = self.root / "ledger.json"
        ledger.write_text("{}")
        index = self.root / "round-index.jsonl"
        index.write_text("")
        output = self.root / "coverage.json"
        evaluate.return_value = {"capture_count": 0, "reconciliation_receipt_count": 0}
        horizons.return_value = {"1": {"qualified": 0, "incomplete_or_unqualified": 1,
                                       "source_abstentions": 0, "production_applied": False}}
        args = ["pipeline", "--paper-ledger", str(ledger), "--depth-directory", str(self.root),
                "--captures-directory", str(self.root), "--associations-directory", str(self.root),
                "--round-index", str(index), "--all-horizon-coverage", "--output", str(output)]
        with patch.object(sys, "argv", args):
            main()
        result = json.loads(output.read_text())
        self.assertEqual(result["horizon_coverage"]["1"]["qualified"], 0)
        self.assertEqual(result["horizon_coverage"]["1"]["incomplete_or_unqualified"], 1)
        horizons.assert_called_once_with(str(index))
        with patch.object(sys, "argv", args), self.assertRaises(FileExistsError):
            main()

    @patch("research.acquisition_receipt_pipeline.evaluate_horizons")
    def test_source_only_report(self, horizons):
        horizons.return_value = {"1": {"qualified": 0}}
        path = self.root / "source-only.json"
        index = self.root / "source-index.jsonl"
        index.write_text("fixture")
        digest = source_only_coverage(str(index), path)
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), digest)
        self.assertFalse(json.loads(path.read_text())["production_applied"])
        with self.assertRaises(FileExistsError):
            source_only_coverage(str(index), path)

    @patch("research.acquisition_receipt_pipeline.evaluate_horizons")
    def test_source_cli(self, horizons):
        horizons.return_value = {"1": {"qualified": 0}}
        output = self.root / "source-cli.json"
        (self.root / "index").write_text("fixture")
        with patch.object(sys, "argv", ["pipeline", "--round-index", str(self.root / "index"),
                                       "--all-horizon-coverage", "--output", str(output)]):
            main()
        self.assertEqual(json.loads(output.read_text())["horizon_coverage"]["1"]["qualified"], 0)

    @patch("research.reconcile_paper_scores.reconcile")
    @patch("research.prospective_round_store.evaluate_index")
    @patch("research.acquisition_receipt_pipeline.evaluate")
    def test_four_horizon_learning_reuses_authenticated_receipts(self, binding, index, reconcile):
        binding.return_value = {"capture_count": 1, "reconciliation_receipt_count": 1,
                                "association_excluded_count": 0, "excluded_count": 0,
                                "reconciliation_receipts": [{"prediction_id": self.pid}]}
        index.side_effect = lambda path, hours: {"horizon": hours}
        reconcile.side_effect = lambda ledger, evidence, **kw: {
            "comparison": {"held_out_n": 0, "rule": "NO QUALIFIED RULE"},
            "shadow_decision": {"decision": "KEEP_BASELINE"},
            "horizon": evidence["horizon"]}
        report = evaluate_learning_horizons({}, "depth", "scores", "links", "index",
                    split_at=1000, baseline_version="b", challenger_version="c",
                    evidence_sha256="f" * 64)
        self.assertEqual(list(report["horizon_comparisons"]), ["1", "6", "24", "48"])
        self.assertEqual([x["horizon"] for x in report["horizon_comparisons"].values()],
                         [1, 6, 24, 48])
        self.assertEqual(binding.call_count, 1)
        self.assertEqual(reconcile.call_count, 4)
        self.assertTrue(all(call.kwargs["score_receipts"][0]["prediction_id"] == self.pid
                            for call in reconcile.call_args_list))
        self.assertFalse(report["production_applied"])

    def test_exclusive_create(self):
        self.associate()
        with self.assertRaises(FileExistsError):
            self.associate()


    @patch("research.reconcile_paper_scores.verify")
    @patch("research.bind_acquisition_receipts.verify")
    @patch("research.bind_acquisition_receipts.verified_rows")
    @patch("research.depth_acquisition_associations.verified_rows")
    def test_authenticated_capture_to_held_out_shadow_no_qualified_rule(
            self, association_rows, binder_rows, binder_verify, ledger_verify):
        """One real fixture score/depth/outcome flows through E2/E3; no fake lift."""
        association_rows.return_value = ([self.row], [])
        binder_rows.return_value = ([self.row], [])
        self.associate()
        ledger = {"predictions": [{"prediction_id": self.pid, "pair": "XBTUSD",
                                  "baseline_score": 0.2, "challenger_score": 0.3}]}
        evidence = {"production_applied": False,
                    "outcomes": [{"pair": "XBTUSD", "entry_first_observed_at": 101,
                                  "entry_source_sha256": self.source,
                                  "entry_liquidity_usd": 25,
                                  "status": "QUALIFIED_OBSERVED_PATH",
                                  "ge30pct": False}],
                    "rounds_verified": 1, "snapshots_verified": 1,
                    "qualified_first_entry_episodes": 1, "abstentions": []}
        report = evaluate_learning(
            ledger, self.root / "raw", self.root / "scores",
            self.root / "depth-links", evidence, split_at=101,
            baseline_version="base-v1", challenger_version="challenger-v2",
            evidence_sha256="f" * 64)
        self.assertEqual(report["acquisition_coverage"]["authenticated_receipts"], 1)
        self.assertEqual(report["comparison"]["held_out_n"], 1)
        self.assertEqual(report["comparison"]["rule"], "NO QUALIFIED RULE")
        self.assertEqual(report["shadow_decision"]["decision"], "KEEP_BASELINE")
        self.assertFalse(report["production_applied"])

    @patch("research.reconcile_paper_scores.verify")
    @patch("research.bind_acquisition_receipts.verify")
    @patch("research.bind_acquisition_receipts.verified_rows")
    @patch("research.depth_acquisition_associations.verified_rows")
    def test_unverified_source_cannot_enter_held_out(
            self, association_rows, binder_rows, binder_verify, ledger_verify):
        association_rows.return_value = ([self.row], [])
        binder_rows.return_value = ([self.row], [])
        self.associate(source_sha256="c" * 64)
        ledger = {"predictions": [{"prediction_id": self.pid, "pair": "XBTUSD",
                                  "baseline_score": 0.2, "challenger_score": 0.3}]}
        evidence = {"production_applied": False, "outcomes": [],
                    "rounds_verified": 1, "snapshots_verified": 1,
                    "qualified_first_entry_episodes": 0, "abstentions": []}
        report = evaluate_learning(
            ledger, self.root / "raw", self.root / "scores",
            self.root / "depth-links", evidence, split_at=101,
            baseline_version="base-v1", challenger_version="challenger-v2",
            evidence_sha256="f" * 64)
        self.assertEqual(report["acquisition_coverage"]["authenticated_receipts"], 0)
        self.assertEqual(report["acquisition_coverage"]["association_exclusions"], 1)
        self.assertEqual(report["comparison"]["held_out_n"], 0)
        self.assertEqual(report["shadow_decision"]["decision"], "KEEP_BASELINE")


if __name__ == "__main__":
    unittest.main()
