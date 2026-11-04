import unittest
from paper_pov.compare_scan_reports import compare_reports

SHA = "a"*40


class CompareScanReportsTests(unittest.TestCase):
    def test_equal_reports(self):
        report = {"watch": [{"pair": "XUSD", "status": "PAPER_WATCH"}]}
        result = compare_reports(report, report, manual_sha=SHA, scheduled_sha=SHA)
        self.assertTrue(result["equivalent"])
        self.assertEqual(result["reason"], "IDENTICAL_REPORT_BYTES")

    def test_different_report_is_not_parity(self):
        result = compare_reports({"watch": ["XUSD"]}, {"watch": []},
                                 manual_sha=SHA, scheduled_sha=SHA)
        self.assertFalse(result["equivalent"])
        self.assertEqual(result["reason"], "REPORT_CONTENT_DIFFERS")

    def test_different_code_is_not_parity(self):
        result = compare_reports({}, {}, manual_sha=SHA, scheduled_sha="b"*40)
        self.assertFalse(result["equivalent"])
        self.assertEqual(result["reason"], "SOURCE_SHA_MISMATCH")


if __name__ == "__main__":
    unittest.main()
