import unittest
from paper_pov.candidate_snapshot_contract import candidate_snapshot, compare_invocations

SHA = "a" * 40


class CandidateSnapshotContractTests(unittest.TestCase):
    def test_manual_and_scheduled_same_report_same_digest(self):
        report = {"observations": [{"pair": "XUSD", "price": 1.5, "quote_at": "2026-01-01T00:00:00Z"}],
                  "watch": [{"pair": "XUSD", "status": "PAPER_WATCH"}]}
        manual = candidate_snapshot(report, source_sha=SHA, invocation="manual")
        scheduled = candidate_snapshot(dict(reversed(list(report.items()))),
                                       source_sha=SHA, invocation="scheduled")
        self.assertEqual(manual["report_sha256"], scheduled["report_sha256"])
        self.assertTrue(compare_invocations(manual, scheduled)["equivalent"])

    def test_changed_candidates_detected_not_silenced(self):
        a = candidate_snapshot({"watch": [{"pair": "XUSD"}]}, source_sha=SHA, invocation="manual")
        b = candidate_snapshot({"watch": []}, source_sha=SHA, invocation="scheduled")
        self.assertFalse(compare_invocations(a, b)["equivalent"])

    def test_different_source_rejected(self):
        a = candidate_snapshot({}, source_sha=SHA, invocation="manual")
        b = candidate_snapshot({}, source_sha="b"*40, invocation="scheduled")
        with self.assertRaisesRegex(ValueError, "source"):
            compare_invocations(a, b)

    def test_nonfinite_report_rejected(self):
        with self.assertRaises(ValueError):
            candidate_snapshot({"price": float("nan")}, source_sha=SHA, invocation="manual")

    def test_no_writer_side_effects(self):
        report = {"watch": []}
        snapshot = candidate_snapshot(report, source_sha=SHA, invocation="manual")
        self.assertFalse(snapshot["production_applied"])
        self.assertEqual(report, snapshot["report"])


if __name__ == "__main__":
    unittest.main()
