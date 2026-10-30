import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from batch9_verify_archive import run
from inventory_kraken_archive import EXPECTED_SHA256


class Batch9ArchiveGateTests(unittest.TestCase):
    def test_verified_archive_still_abstains_without_independent_trades(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "evidence.json"
            def fake_download(path, resources):
                path.write_bytes(b"synthetic-not-a-real-archive")
                return {"sha256": EXPECTED_SHA256, "bytes": 25,
                        "integrity_verified": True}
            with patch("batch9_verify_archive.resource_gate", return_value={}), patch(
                    "batch9_verify_archive.download_verified", side_effect=fake_download):
                result = run(output)
            self.assertFalse(result["timestamp_open_verified"])
            self.assertEqual(result["real_historical_labels"], 0)
            self.assertEqual(result["horizons"], {})
            self.assertTrue(output.exists())

    def test_wrong_identity_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch("batch9_verify_archive.resource_gate", return_value={}), patch(
                    "batch9_verify_archive.download_verified",
                    return_value={"sha256": "0"*64, "integrity_verified": True, "bytes": 1}):
                with self.assertRaises(RuntimeError):
                    run(Path(folder) / "evidence.json")

    def test_overwrite_refused_before_network(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / "evidence.json"
            p.write_text("existing")
            with self.assertRaises(FileExistsError):
                run(p)
            self.assertEqual(p.read_text(), "existing")


if __name__ == "__main__":
    unittest.main()
