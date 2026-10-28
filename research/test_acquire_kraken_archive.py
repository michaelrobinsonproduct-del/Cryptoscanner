import hashlib,io,unittest
from email.message import Message
from unittest.mock import patch
import acquire_kraken_archive as m
class Response:
    def __init__(self,data,status=200,length=None,encoding="identity"):
        self.status=status;self.headers=Message();self.headers["Content-Length"]=str(len(data) if length is None else length)
        self.headers["Content-Encoding"]=encoding;self.data=io.BytesIO(data)
    def read(self,n):return self.data.read(n)
    def __enter__(self):return self
    def __exit__(self,*a):return False
class Tests(unittest.TestCase):
    def call(self,opener=None,**kw):
        return m.verify(opener=opener,disk=m.DISK,mem=m.MEM,**kw)
    def test_five_parts_digest(self):
        parts=[b"a",b"bc",b"def",b"ghij",b"klmno"]
        with patch.object(m,"SIZES",tuple(map(len,parts))),patch.object(m,"SHA",hashlib.sha256(b"".join(parts)).hexdigest()):
            result=self.call(lambda req,timeout:Response(parts[int(req.full_url[-2:])]))
        self.assertTrue(result["full_archive_sha256_verified"]);self.assertEqual(result["total_bytes"],15)
        self.assertFalse(result["historical_data_validated"])
    def test_disk(self):
        with self.assertRaisesRegex(RuntimeError,"disk"):m.verify(disk=0,mem=m.MEM)
    def test_memory(self):
        with self.assertRaisesRegex(RuntimeError,"memory"):m.verify(disk=m.DISK,mem=0)
    def test_status(self):
        with self.assertRaisesRegex(RuntimeError,"HTTP"):self.call(lambda *a,**k:Response(b"",status=206))
    def test_length(self):
        with self.assertRaisesRegex(RuntimeError,"Content-Length"):self.call(lambda *a,**k:Response(b"",length=3))
    def test_encoding(self):
        with self.assertRaisesRegex(RuntimeError,"encoding"):self.call(lambda *a,**k:Response(b"",length=m.SIZES[0],encoding="gzip"))
    def test_truncated(self):
        with patch.object(m,"SIZES",(3,)):
            with self.assertRaisesRegex(RuntimeError,"Truncated"):self.call(lambda *a,**k:Response(b"ab",length=3))
    def test_extra_bytes(self):
        with patch.object(m,"SIZES",(2,)):
            with self.assertRaisesRegex(RuntimeError,"extra bytes"):self.call(lambda *a,**k:Response(b"abc",length=2))
    def test_sha_mismatch(self):
        with patch.object(m,"SIZES",(3,)):
            with self.assertRaisesRegex(RuntimeError,"SHA256 mismatch"):self.call(lambda *a,**k:Response(b"abc"))
    def test_deadline(self):
        ticks=iter([0,m.DEADLINE+1])
        with self.assertRaisesRegex(RuntimeError,"Deadline"):self.call(lambda *a,**k:None,clock=lambda:next(ticks))
if __name__=="__main__":unittest.main()
