import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from consolidated_historical_learning import assess, read_member, run
from inventory_kraken_archive import EXPECTED_SHA256


class ConsolidatedTests(unittest.TestCase):
    def setUp(self):
        self.rows = [(300., 100., 120., 100., 110., 5., 3.)]
        self.trades = [(301, 100, 1, 0), (450, 120, 2, 1), (599, 110, 2, 2)]

    def test_missing_independent_source_abstains(self):
        r = assess(self.rows)
        self.assertEqual(r["real_labels"], 0)
        self.assertFalse(r["timestamp_open_verified"])

    def test_complete_trade_match_only_enables_provenance(self):
        r = assess(self.rows, independent_trades=self.trades,
                   independent_trade_source=True, source_complete=True)
        self.assertTrue(r["timestamp_open_verified"])
        self.assertEqual(r["real_labels"], 0)
        self.assertEqual(r["horizons"]["1"]["status"], "immature")

    def test_partial_trade_sample_abstains(self):
        r = assess(self.rows, independent_trades=self.trades[:2],
                   independent_trade_source=True, source_complete=True)
        self.assertFalse(r["timestamp_open_verified"])

    def test_no_source_completeness_abstains(self):
        r = assess(self.rows, independent_trades=self.trades,
                   independent_trade_source=True, source_complete=False)
        self.assertEqual(r["real_labels"], 0)

    def test_no_overwrite_before_download(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "report.json"
            p.write_text("original")
            with self.assertRaises(FileExistsError):
                run(p)
            self.assertEqual(p.read_text(), "original")

    def test_wrong_digest_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            with patch("consolidated_historical_learning.resource_gate", return_value={}), patch(
                "consolidated_historical_learning.download_verified",
                return_value={"sha256": "0"*64, "integrity_verified": True, "bytes": 1}):
                with self.assertRaises(RuntimeError):
                    run(Path(d) / "report.json")


if __name__ == "__main__":
    unittest.main()
