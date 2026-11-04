import datetime as dt
import hashlib
import tempfile
import unittest
from pathlib import Path
from paper_pov.historical_outcome_execution import run_historical_outcomes

START = dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc)
SCHEMA = {"format": "kraken_trade_csv_explicit_v1", "timestamp_unit": "seconds",
          "columns": {"timestamp": 0, "price": 1, "volume": 2},
          "header": False, "column_count": 3}


class HistoricalOutcomeExecutionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.raw = b"".join(
            f"{int((START + dt.timedelta(minutes=5*i)).timestamp())},{100+i*0.01:.2f},1\n".encode()
            for i in range(577))
        (self.root / "XUSD.csv").write_bytes(self.raw)
        self.manifest = {"schema": "kraken_archive_manifest_v1", "source": "Kraken",
                         "partitions": [{"file": "XUSD.csv", "size_bytes": len(self.raw),
                                         "sha256": hashlib.sha256(self.raw).hexdigest()}]}
        self.predictions = [
            {"prediction_id": "p1", "pair": "XUSD", "status": "PAPER_WATCH",
             "as_of": START.isoformat()},
            {"prediction_id": "p2", "pair": "YUSD", "status": "PAPER_WATCH",
             "as_of": START.isoformat()}]
        self.until = (START + dt.timedelta(hours=49)).isoformat()

    def test_real_file_through_all_four_horizons_and_missing_market(self):
        result = run_historical_outcomes(self.manifest, self.root, SCHEMA,
                                         {"XUSD": "XUSD.csv"}, self.predictions, self.until)
        self.assertEqual(result["prediction_count"], 2)
        for h in (1, 6, 24, 48):
            self.assertEqual(result["status_counts"][f"{h}h:MATURED_OBSERVED"], 1)
            self.assertEqual(result["status_counts"][f"{h}h:ABSTAIN_ENTRY"], 1)
        self.assertEqual(result["learning_qualified_count"], 0)
        self.assertEqual(result["qualified_cohorts"], [])
        self.assertIsNone(result["held_out_lift"])
        self.assertFalse(result["source_authenticated"])

    def test_tampered_archive_fails_before_label_generation(self):
        (self.root / "XUSD.csv").write_bytes(self.raw.replace(b"100.00", b"101.00", 1))
        with self.assertRaisesRegex(ValueError, "checksum"):
            run_historical_outcomes(self.manifest, self.root, SCHEMA,
                                    {"XUSD": "XUSD.csv"}, self.predictions, self.until)

    def test_missing_5m_trade_bucket_abstains(self):
        lines = self.raw.splitlines(keepends=True)
        raw = b"".join(lines[:20] + lines[21:])
        (self.root / "XUSD.csv").write_bytes(raw)
        self.manifest["partitions"][0]["size_bytes"] = len(raw)
        self.manifest["partitions"][0]["sha256"] = hashlib.sha256(raw).hexdigest()
        result = run_historical_outcomes(self.manifest, self.root, SCHEMA,
                                         {"XUSD": "XUSD.csv"}, self.predictions, self.until)
        self.assertEqual(result["status_counts"]["48h:ABSTAIN_GAP"], 1)
        self.assertEqual(result["learning_qualified_count"], 0)


if __name__ == "__main__":
    unittest.main()
