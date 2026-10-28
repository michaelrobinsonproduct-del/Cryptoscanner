import io
import unittest
from email.message import Message
from preflight_kraken_archive import (
    acquire, preflight, RANGE_BYTES, TOTAL_CAP, MIN_FREE_DISK, MIN_AVAILABLE_MEMORY
)

class Response:
    def __init__(self, status, header, body):
        self.status = status
        self.headers = Message()
        self.headers["Content-Range"] = header
        self.body = io.BytesIO(body)
    def read(self, size):
        return self.body.read(size)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        pass

def fake(status=206, header="bytes 0-65535/2097152000", body=None):
    return lambda request, timeout: Response(status, header, b"a"*RANGE_BYTES if body is None else body)

class PreflightTests(unittest.TestCase):
    def test_five_bounded_ranges_and_unverified_archive(self):
        seen = []
        def opener(req, timeout):
            seen.append((req.full_url, req.get_header("Range"), timeout))
            return fake()(req, timeout)
        r = acquire(opener=opener, disk_free=MIN_FREE_DISK, mem_free=MIN_AVAILABLE_MEMORY)
        self.assertEqual(len(seen), 5)
        self.assertEqual(r["total_sample_bytes"], TOTAL_CAP)
        self.assertFalse(r["archive_sha256_verified"])
        self.assertTrue(all(row[1] == "bytes=0-65535" for row in seen))
        self.assertTrue(all(row[2] == 12 for row in seen))
    def test_disk_fail_closed_before_network(self):
        with self.assertRaisesRegex(RuntimeError, "disk"):
            acquire(opener=lambda *a, **kw: self.fail("network called"),
                    disk_free=MIN_FREE_DISK-1, mem_free=MIN_AVAILABLE_MEMORY)
    def test_memory_fail_closed_before_network(self):
        with self.assertRaisesRegex(RuntimeError, "memory"):
            acquire(opener=lambda *a, **kw: self.fail("network called"),
                    disk_free=MIN_FREE_DISK, mem_free=MIN_AVAILABLE_MEMORY-1)
    def test_range_ignored(self):
        with self.assertRaisesRegex(RuntimeError, "range ignored"):
            acquire(opener=fake(status=200), disk_free=MIN_FREE_DISK, mem_free=MIN_AVAILABLE_MEMORY)
    def test_invalid_header(self):
        with self.assertRaisesRegex(RuntimeError, "Content-Range"):
            acquire(opener=fake(header="bytes 1-65536/2097152000"),
                    disk_free=MIN_FREE_DISK, mem_free=MIN_AVAILABLE_MEMORY)
    def test_truncated(self):
        with self.assertRaisesRegex(RuntimeError, "truncated"):
            acquire(opener=fake(body=b"short"), disk_free=MIN_FREE_DISK, mem_free=MIN_AVAILABLE_MEMORY)
    def test_oversized(self):
        with self.assertRaisesRegex(RuntimeError, "truncated or oversized"):
            acquire(opener=fake(body=b"x"*(RANGE_BYTES+1)),
                    disk_free=MIN_FREE_DISK, mem_free=MIN_AVAILABLE_MEMORY)
    def test_deadline(self):
        times = iter([0, 91])
        with self.assertRaisesRegex(RuntimeError, "deadline"):
            acquire(clock=lambda: next(times), opener=lambda *a, **kw: self.fail("network called"),
                    disk_free=MIN_FREE_DISK, mem_free=MIN_AVAILABLE_MEMORY)

if __name__ == "__main__": unittest.main()
