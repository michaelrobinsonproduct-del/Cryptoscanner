import json
import tempfile
import unittest
from pathlib import Path
import zipfile
import csv
import io
import hashlib

from analyze_reusable_ohlc_candidates import audit, _peak_windows
from build_reusable_ohlc_evidence import build


class DescriptiveAuditTests(unittest.TestCase):
    def test_future_peak_not_entry_high(self):
        seg = [(i*300, 100 if i != 1 else 131, 100) for i in range(14)]
        self.assertEqual(_peak_windows(seg, 12), (2, 1))

    def test_window_requires_full_future_coverage(self):
        self.assertEqual(_peak_windows([(i*300, 131, 100) for i in range(12)], 12), (0, 0))

    def test_real_archive_fixture_descriptive_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            rows = [[str(i*300), "100", "131" if i == 1 else "100",
                     "100", "100", "10", "2"] for i in range(578)]
            stream = io.StringIO()
            csv.writer(stream, lineterminator="\n").writerows(rows)
            archive = p/"source.zip"
            with zipfile.ZipFile(archive, "w") as z:
                z.writestr("TESTUSD_5.csv", stream.getvalue())
            digest = hashlib.sha256(archive.read_bytes()).hexdigest()
            cohort = {"archive_sha256": digest, "real_labels": 0,
                      "selection": "test", "selected": [{"member": "TESTUSD_5.csv"}]}
            evidence = p/"evidence.zip"
            build(archive, cohort, evidence, expected_archive_sha256=digest)
            report = audit(evidence, expected_archive_sha256=digest)
            self.assertEqual(report["real_labels"], 0)
            self.assertEqual(report["held_out_evaluation"], "not_authorized")
            self.assertEqual(report["per_market"]["TESTUSD_5.csv"]["1"]["unverified_peak_30_windows"], 1)
            self.assertEqual(report["per_market"]["TESTUSD_5.csv"]["48"]["complete_ohlc_windows"], 2)

    def test_source_mismatch_abstains(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(Exception):
                audit(Path(tmp)/"absent.zip", expected_archive_sha256="0"*64)


if __name__ == "__main__":
    unittest.main()
