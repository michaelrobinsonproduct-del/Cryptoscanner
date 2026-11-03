"""Focused end-to-end score bytes -> immutable association -> verified depth -> binder."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from research.capture_acquisition_scores import capture_score
from research.depth_acquisition_associations import write_association, verified_associations
from research.acquisition_receipt_pipeline import evaluate, write_new


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

    def test_exclusive_create(self):
        self.associate()
        with self.assertRaises(FileExistsError):
            self.associate()


if __name__ == "__main__":
    unittest.main()
