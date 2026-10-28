import io
import unittest
from email.message import Message
from probe_kraken_archive import probe, MAX_BYTES

class Response:
    def __init__(self,status,content_range,data):
        self.status=status;self.headers=Message();self.headers["Content-Range"]=content_range;self.stream=io.BytesIO(data)
    def read(self,n): return self.stream.read(n)
    def __enter__(self): return self
    def __exit__(self,*args): pass

class ProbeTests(unittest.TestCase):
    def test_bounded_success_not_archive_verified(self):
        def open_url(req,timeout):
            self.assertEqual(timeout,12)
            self.assertEqual(req.get_header("Range"),f"bytes=0-{MAX_BYTES-1}")
            return Response(206,f"bytes 0-{MAX_BYTES-1}/2000000000",b"x"*MAX_BYTES)
        result=probe(0,open_url)
        self.assertEqual(result["bytes_read"],MAX_BYTES)
        self.assertFalse(result["sha256_verified"])
    def test_server_ignoring_range_fails_without_reading(self):
        with self.assertRaisesRegex(RuntimeError,"Range request not honored"):
            probe(0,lambda req,timeout:Response(200,"",b"x"*MAX_BYTES))
    def test_wrong_content_range_rejected(self):
        with self.assertRaisesRegex(RuntimeError,"Unexpected content range"):
            probe(1,lambda req,timeout:Response(206,"bytes 5-65540/2000000000",b"x"*MAX_BYTES))
    def test_truncated_data_rejected(self):
        with self.assertRaisesRegex(RuntimeError,"Truncated"):
            probe(2,lambda req,timeout:Response(206,f"bytes 0-{MAX_BYTES-1}/2000000000",b"x"*7))
    def test_part_bounds(self):
        for bad in (-1,5,"0"):
            with self.assertRaises(ValueError):probe(bad)

if __name__=="__main__":unittest.main()
