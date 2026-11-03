"""Focused end-to-end score bytes -> immutable association -> verified depth -> binder."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from research.capture_acquisition_scores import capture_score
from research.depth_acquisition_associations import write_association, verified_associations
from research.acquisition_receipt_pipeline import evaluate, evaluate_learning, evaluate_horizons, write_new


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
