import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from research.capture_acquisition_scores import capture_score
from research.acquisition_receipt_pipeline import evaluate, load_captures, write_new

PID = "a" * 64


class AcquisitionPipelineTests(unittest.TestCase):
    def test_real_capture_to_authenticated_binding_and_immutable_report(self):
        with tempfile.TemporaryDirectory() as root:
            captures = Path(root) / "captures"
            capture_score(captures, prediction_id=PID, pair="XBTUSD",
                          baseline_score=1.0, challenger_score=2.0,
                          observed_at=1000)
            ledger = {"predictions": [{"prediction_id": PID, "pair": "XBTUSD",
                                      "baseline_score": 1.0, "challenger_score": 2.0}]}
            source = [{"pair": "XBTUSD", "source_sha256": "b" * 64,
                       "first_observed_at": 1001, "entry_liquidity_usd": 25}]
            # This focused integration fixture replaces only external depth
            # verification and ledger signature, not binding logic.
            with patch("research.bind_acquisition_receipts.verify"), patch(
                "research.bind_acquisition_receipts.verified_rows",
                return_value=(source, [])):
                report = evaluate(ledger, root, captures)
            self.assertEqual(report["accepted_count"], 0)
            self.assertEqual(report["excluded"][0]["reason"],
                             "NO_VERIFIED_DEPTH_SOURCE")
            self.assertFalse(report["production_applied"])
            path = Path(root) / "result.json"
            self.assertEqual(len(write_new(path, report)), 64)
            with self.assertRaises(FileExistsError):
                write_new(path, report)

    def test_capture_filename_identity_and_mode_fail_closed(self):
        with tempfile.TemporaryDirectory() as root:
            capture_score(root, prediction_id=PID, pair="XBTUSD",
                          baseline_score=1, challenger_score=2, observed_at=1)
            self.assertEqual(len(load_captures(root)), 1)
            path = Path(root) / (PID + ".json")
            data = json.loads(path.read_text())
            data["mode"] = "PRODUCTION"
            path.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, "invalid"):
                load_captures(root)

    def test_no_captures_truthful_zero_coverage(self):
        with tempfile.TemporaryDirectory() as root:
            with patch("research.bind_acquisition_receipts.verify"), patch(
                "research.bind_acquisition_receipts.verified_rows",
                return_value=([], [{"reason": "NO_SOURCE"}])):
                report = evaluate({"predictions": []}, root, root)
            self.assertEqual(report["capture_count"], 0)
            self.assertEqual(report["accepted_count"], 0)
            self.assertEqual(len(report["source_abstentions"]), 1)


if __name__ == "__main__":
    unittest.main()
