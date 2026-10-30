import io
import tempfile
import unittest
from pathlib import Path
from probe_kraken_historical_trade_archive import probe, run


class FakeResponse:
    def __init__(self, status=206, start=0, size=1000000, data=None):
        self.status = status
        self.headers = {"Content-Range": f"bytes {start}-65535/{size}"}
        self.data = io.BytesIO(data if data is not None else bytes((80,75,3,4)) + bytes(65532))
    def __enter__(self): return self
    def __exit__(self, *args): return False
    def read(self, size): return self.data.read(size)


class OfficialTradeArchiveTests(unittest.TestCase):
    def test_bounded_real_archive_source_candidate(self):
        r = probe(opener=lambda *a, **k: FakeResponse())
        self.assertEqual(r["bytes_sampled"], 65536)
        self.assertFalse(r["complete_trade_interval_verified"])
        self.assertEqual(r["historical_labels"], 0)

    def test_refuses_full_response(self):
        with self.assertRaises(RuntimeError):
            probe(opener=lambda *a, **k: FakeResponse(status=200))

    def test_refuses_bad_range(self):
        with self.assertRaises(RuntimeError):
            probe(opener=lambda *a, **k: FakeResponse(start=1))

    def test_refuses_non_zip(self):
        with self.assertRaises(RuntimeError):
            probe(opener=lambda *a, **k: FakeResponse(data=b"bad!" + bytes(65532)))

    def test_refuses_short_response(self):
        with self.assertRaises(RuntimeError):
            probe(opener=lambda *a, **k: FakeResponse(data=bytes((80,75,3,4))))

    def test_no_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "evidence.json"
            p.write_text("original")
            with self.assertRaises(FileExistsError):
                run(p)
            self.assertEqual(p.read_text(), "original")


if __name__ == "__main__":
    unittest.main()
