import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile
from email.message import Message
import inventory_kraken_archive as m

class Response:
    def __init__(self, data, status=200, length=None, encoding="identity"):
        self.status = status
        self.headers = Message()
        self.headers["Content-Length"] = str(len(data) if length is None else length)
        self.headers["Content-Encoding"] = encoding
        self.stream = io.BytesIO(data)
    def read(self, size):
        return self.stream.read(size)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return False

class InventoryTests(unittest.TestCase):
    def test_valid_archive_inventory_real_csv(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)/"tiny.zip"
            with zipfile.ZipFile(p,"w",compression=zipfile.ZIP_DEFLATED) as z:
                z.writestr("OHLC/TESTUSD_5.csv", "300,10,12,9,11,5,2\n600,11,13,10,12,6,3\n1200,12,14,11,13,7,4\n")
            inv = m.inspect_archive(p)
            self.assertEqual(inv["five_minute_members"],1)
            r = inv["five_minute_csv_inventory"][0]
            self.assertEqual((r["rows"],r["gap_intervals"],r["invalid_rows"]),(3,1,0))
            self.assertTrue(r["crc_checked"])
            self.assertFalse(inv["future_outcomes_validated"])
    def test_invalid_and_duplicate_rows_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/"tiny.zip"
            with zipfile.ZipFile(p,"w") as z:
                z.writestr("TESTUSD_5.csv","300,10,12,9,11,5,2\n300,10,12,9,11,5,2\n600,0,12,9,11,5,2\n")
            r=m.inspect_archive(p)["five_minute_csv_inventory"][0]
            self.assertEqual((r["adjacent_duplicates"],r["invalid_rows"]),(1,1))
    def test_zip_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/"bad.zip"
            with zipfile.ZipFile(p,"w") as z:z.writestr("../TESTUSD_5.csv","300,10,12,9,11,5,2\n")
            with self.assertRaisesRegex(RuntimeError,"unsafe"):m.inspect_archive(p)
    def test_zip_duplicate_member_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/"duplicate.zip"
            with zipfile.ZipFile(p,"w") as z:
                for _ in range(2):z.writestr("TESTUSD_5.csv","300,10,12,9,11,5,2\n")
            with self.assertRaisesRegex(RuntimeError,"duplicate"):m.inspect_archive(p)
    def test_disk_gate_before_network(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(m.shutil,"disk_usage") as disk:
            disk.return_value=type("Usage",(),{"free":0})()
            with self.assertRaisesRegex(RuntimeError,"disk"):m.resource_gate(tmp,m.MIN_MEMORY)
    def test_memory_gate(self):
        with tempfile.TemporaryDirectory() as tmp,patch.object(m.shutil,"disk_usage") as disk:
            disk.return_value=type("Usage",(),{"free":m.MIN_DISK+sum(m.SIZES)})()
            with self.assertRaisesRegex(RuntimeError,"memory"):m.resource_gate(tmp,0)
    def test_verified_stream_and_failure_cleanup(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/"archive.zip"
            parts=[b"abc",b"def"]
            with patch.object(m,"SIZES",(3,3)),patch.object(m,"EXPECTED_SHA256",hashlib.sha256(b"abcdef").hexdigest()):
                result=m.download_verified(path,opener=lambda req,timeout:Response(parts[int(req.full_url[-2:])]),resources={})
                self.assertTrue(result["integrity_verified"])
                self.assertEqual(path.read_bytes(),b"abcdef")
            path.unlink()
            with patch.object(m,"SIZES",(3,)),patch.object(m,"EXPECTED_SHA256","0"*64):
                with self.assertRaisesRegex(RuntimeError,"SHA256 mismatch"):
                    m.download_verified(path,opener=lambda req,timeout:Response(b"abc"),resources={})
                self.assertFalse(path.exists())
    def test_http_and_length_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp,patch.object(m,"SIZES",(3,)):
            p=Path(tmp)/"archive.zip"
            with self.assertRaisesRegex(RuntimeError,"HTTP"):
                m.download_verified(p,opener=lambda req,timeout:Response(b"abc",status=206),resources={})
            self.assertFalse(p.exists())
            with self.assertRaisesRegex(RuntimeError,"Content-Length"):
                m.download_verified(p,opener=lambda req,timeout:Response(b"abc",length=2),resources={})
            self.assertFalse(p.exists())
    def test_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/"exists.json";p.write_text("protected")
            with self.assertRaises(FileExistsError):m.run(p)
            self.assertEqual(p.read_text(),"protected")
    def test_member_size_cap(self):
        info=zipfile.ZipInfo("TESTUSD_5.csv");info.file_size=m.MAX_MEMBER_BYTES+1
        with self.assertRaisesRegex(RuntimeError,"size cap"):m.safe_member(info)

if __name__=="__main__":unittest.main()
