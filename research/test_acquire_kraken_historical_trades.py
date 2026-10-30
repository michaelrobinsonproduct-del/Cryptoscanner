import io
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch
from acquire_kraken_historical_trades import download, inspect, run, EXPECTED_BYTES


class Response:
    status = 200
    headers = {"Content-Encoding": "identity", "Content-Length": str(EXPECTED_BYTES)}
    def __enter__(self): return self
    def __exit__(self, *args): return False
    def read(self, n): return b""


class AcquisitionTests(unittest.TestCase):
    def test_truncated_download_fails_closed_and_cleans(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"archive.zip"
            with self.assertRaises(RuntimeError):
                download(p, opener=lambda *a, **kw: Response())
            self.assertFalse(p.exists())

    def test_existing_file_refused(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"archive.zip"
            p.write_text("keep")
            with self.assertRaises(FileExistsError):
                download(p, opener=lambda *a, **kw: Response())
            self.assertEqual(p.read_text(), "keep")

    def test_safe_zip_metadata_only(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"test.zip"
            with zipfile.ZipFile(p, "w") as z:
                z.writestr("XBTUSD.csv", "trade,price\n")
            r = inspect(p)
            self.assertEqual(r["members"], 1)
            self.assertFalse(r["member_csv_semantics_verified"])

    def test_zip_traversal_refused(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"bad.zip"
            with zipfile.ZipFile(p, "w") as z:
                z.writestr("../escape.csv", "bad")
            with self.assertRaises(RuntimeError):
                inspect(p)

    def test_report_no_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"evidence.json"
            p.write_text("keep")
            with self.assertRaises(FileExistsError):
                run(p)
            self.assertEqual(p.read_text(), "keep")


if __name__ == "__main__":
    unittest.main()
