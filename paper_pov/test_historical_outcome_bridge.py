import datetime as dt
import hashlib
import tempfile
import unittest
from pathlib import Path
from paper_pov.historical_outcome_bridge import prepare_outcome_input

SCHEMA = {"format": "kraken_trade_csv_explicit_v1", "timestamp_unit": "seconds",
          "columns": {"timestamp": 0, "price": 1, "volume": 2},
          "header": False, "column_count": 3}
RAW = b"1767225600,100,1\n1767225660,105,2\n1767226200,99,3\n"


class OutcomeBridgeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "XUSD.csv").write_bytes(RAW)
        self.manifest = {"schema": "kraken_archive_manifest_v1", "source": "Kraken",
                         "partitions": [{"file": "XUSD.csv", "size_bytes": len(RAW),
                                         "sha256": hashlib.sha256(RAW).hexdigest()}]}
        self.predictions = [{"prediction_id": "p1", "pair": "XUSD",
                             "status": "PAPER_WATCH",
                             "as_of": "2026-01-01T00:00:00+00:00"},
                            {"prediction_id": "p2", "pair": "YUSD",
                             "status": "PAPER_WATCH",
                             "as_of": "2026-01-01T00:00:00+00:00"}]
        self.until = "2026-01-03T01:00:00+00:00"

    def test_verified_partition_and_missing_market_are_both_preserved(self):
        result = prepare_outcome_input(self.manifest, self.root, SCHEMA,
                                       {"XUSD": "XUSD.csv"}, self.predictions, self.until)
        self.assertEqual(len(result["outcome_input"]["predictions"]), 2)
        self.assertEqual(len(result["outcome_input"]["bars_by_pair"]["XUSD"]), 2)
        self.assertEqual(result["outcome_input"]["bars_by_pair"]["YUSD"], [])
        self.assertEqual(result["partition_provenance"]["YUSD"]["status"],
                         "ABSTAIN_NO_PINNED_PARTITION")
        self.assertFalse(result["qualified_for_learning"])

    def test_tamper_rejected(self):
        (self.root / "XUSD.csv").write_bytes(RAW.replace(b"105", b"106"))
        with self.assertRaisesRegex(ValueError, "checksum"):
            prepare_outcome_input(self.manifest, self.root, SCHEMA,
                                  {"XUSD": "XUSD.csv"}, self.predictions, self.until)

    def test_future_prediction_rejected(self):
        with self.assertRaisesRegex(ValueError, "cutoff"):
            prepare_outcome_input(self.manifest, self.root, SCHEMA, {},
                                  [{**self.predictions[0], "as_of": "2027-01-01T00:00:00+00:00"}],
                                  self.until)


if __name__ == "__main__":
    unittest.main()
