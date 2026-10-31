import io
import json
import unittest
import zipfile

from probe_bounded_trade_members import (RangeZipReader, collect,
                                         write_evidence, MAX_REQUEST)


def archive_bytes():
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("ABUSD.csv", "timestamp,price,volume\n1710000000,1,2\n1710000001,2,3\n")
        z.writestr("CDUSD.csv", "timestamp,price,volume\n1710000002,3,4\n")
    # Fake remote ZIP length must exceed minimum to enforce realistic range semantics.
    return out.getvalue()


class Response:
    def __init__(self, data, start, end, total, status=206, override=None):
        self.status = status
        self.headers = {"Content-Range": override or f"bytes {start}-{end}/{total}",
                        "Content-Encoding": "identity"}
        self.data = data[start:end+1]
        self.pos = 0

    def read(self, size=-1):
        chunk = self.data[self.pos:] if size < 0 else self.data[self.pos:self.pos+size]
        self.pos += len(chunk)
        return chunk

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


def opener(data, *, status=206, override=None):
    def open_request(request, timeout=None):
        raw = request.get_header("Range")
        assert raw and raw.startswith("bytes="), "unbounded download attempted"
        start, end = (int(x) for x in raw[6:].split("-"))
        return Response(data, start, end, len(data), status=status, override=override)
    return open_request


def selected(*names):
    return {"selected": [{"member": x + "_5.csv"} for x in names]}


class BoundedTradeTests(unittest.TestCase):
    def test_range_reader_rejects_unbounded_read(self):
        data = archive_bytes()
        r = RangeZipReader("https://assets.kraken.com/test.zip",
                           expected_bytes=MAX_REQUEST+65537, opener=opener(data))
        with self.assertRaises(ValueError):
            r.read()

    def test_remote_zip_collects_full_crc_checked_members_without_labels(self):
        data = archive_bytes()
        # Tests need ZIP length >65536; pad a harmless stored member.
        out = io.BytesIO()
        with zipfile.ZipFile(out, "w") as z:
            z.writestr("ABUSD.csv", "timestamp,price,volume\n1710000000,1,2\n1710000001,2,3\n")
            z.writestr("padding.bin", b"x"*66000, compress_type=zipfile.ZIP_STORED)
        data = out.getvalue()
        manifest, files = collect(selected("ABUSD"), url="https://assets.kraken.com/test.zip",
                                  expected_bytes=len(data), opener=opener(data))
        self.assertEqual(manifest["retained_markets"], 1)
        self.assertEqual(manifest["real_labels"], 0)
        self.assertFalse(manifest["source_archive_full_sha256_verified"])
        self.assertTrue(manifest["markets"]["ABUSD.csv"]["member_crc_verified"])
        self.assertIn(b"1710000000", files["ABUSD.csv"])
        self.assertLess(manifest["range_bytes_transferred"], 24 * 1024 * 1024)

    def test_rejects_server_ignoring_range(self):
        data = b"x"*70000
        r = RangeZipReader("https://assets.kraken.com/test.zip",
                           expected_bytes=len(data), opener=opener(data, status=200))
        with self.assertRaises(RuntimeError):
            r.read(8)

    def test_rejects_wrong_content_range(self):
        data = b"x"*70000
        r = RangeZipReader("https://assets.kraken.com/test.zip",
                           expected_bytes=len(data), opener=opener(data, override="bytes 0-1/70000"))
        with self.assertRaises(RuntimeError):
            r.read(8)

    def test_transfer_budget_and_request_cap(self):
        data = b"x"*70000
        r = RangeZipReader("https://assets.kraken.com/test.zip",
                           expected_bytes=len(data), opener=opener(data), budget=4)
        with self.assertRaises(ValueError):
            r.read(5)
        self.assertEqual(r.transferred, 0)
        with self.assertRaises(ValueError):
            r.read(MAX_REQUEST+1)

    def test_untrusted_market_name_fails(self):
        with self.assertRaises(ValueError):
            collect(selected("../secret"), opener=opener(b"x"*70000),
                    expected_bytes=70000)

    def test_duplicate_market_fails(self):
        with self.assertRaises(ValueError):
            collect(selected("ABUSD", "ABUSD"), opener=opener(b"x"*70000),
                    expected_bytes=70000)

    def test_no_evidence_does_not_claim_labels(self):
        out = io.BytesIO()
        with zipfile.ZipFile(out, "w") as z:
            z.writestr("OTHER.csv", "timestamp,price,volume\n1710000000,1,2\n")
            z.writestr("padding.bin", b"x"*66000, compress_type=zipfile.ZIP_STORED)
        data = out.getvalue()
        result, files = collect(selected("ABUSD"), url="https://assets.kraken.com/test.zip",
                                expected_bytes=len(data), opener=opener(data))
        self.assertEqual(result["status"], "no_eligible_bounded_trade_members")
        self.assertEqual(result["real_labels"], 0)
        self.assertEqual(files, {})


    def test_strong_etag_pins_multiple_ranges_and_uses_if_range(self):
        data = b"x"*70000
        observed = []
        def opener(request, timeout=None):
            raw = request.get_header("Range")
            start, end = (int(x) for x in raw[6:].split("-"))
            observed.append(request.get_header("If-range"))
            response = Response(data, start, end, len(data))
            response.headers["ETag"] = '"kraken-v1"'
            response.headers["Content-Length"] = str(end-start+1)
            return response
        reader = RangeZipReader("https://assets.kraken.com/test.zip",
                                expected_bytes=len(data), opener=opener)
        self.assertEqual(reader.read(10), b"x"*10)
        self.assertEqual(reader.read(10), b"x"*10)
        self.assertEqual(observed, [None, '"kraken-v1"'])
        self.assertTrue(reader.source_validator["revision_pinned"])

    def test_etag_drift_rejected_without_advancing_position(self):
        data = b"x"*70000
        calls = [0]
        def opener(request, timeout=None):
            start, end = (int(x) for x in request.get_header("Range")[6:].split("-"))
            response = Response(data, start, end, len(data))
            response.headers["ETag"] = '"v1"' if calls[0] == 0 else '"v2"'
            calls[0] += 1
            return response
        reader = RangeZipReader("https://assets.kraken.com/test.zip",
                                expected_bytes=len(data), opener=opener)
        reader.read(5)
        with self.assertRaisesRegex(RuntimeError, "ETag changed"):
            reader.read(5)
        self.assertEqual(reader.tell(), 5)
        self.assertEqual(reader.transferred, 5)

    def test_etag_disappearing_is_rejected(self):
        data = b"x"*70000
        calls = [0]
        def opener(request, timeout=None):
            start, end = (int(x) for x in request.get_header("Range")[6:].split("-"))
            response = Response(data, start, end, len(data))
            if calls[0] == 0:
                response.headers["ETag"] = '"v1"'
            calls[0] += 1
            return response
        reader = RangeZipReader("https://assets.kraken.com/test.zip",
                                expected_bytes=len(data), opener=opener)
        reader.read(5)
        with self.assertRaisesRegex(RuntimeError, "ETag changed"):
            reader.read(5)

    def test_last_modified_pins_when_no_strong_etag(self):
        data = b"x"*70000
        seen = []
        def opener(request, timeout=None):
            start, end = (int(x) for x in request.get_header("Range")[6:].split("-"))
            seen.append(request.get_header("If-range"))
            response = Response(data, start, end, len(data))
            response.headers["Last-Modified"] = "Thu, 01 Oct 2026 00:00:00 GMT"
            return response
        reader = RangeZipReader("https://assets.kraken.com/test.zip",
                                expected_bytes=len(data), opener=opener)
        reader.read(3)
        reader.read(4)
        self.assertEqual(seen, [None, "Thu, 01 Oct 2026 00:00:00 GMT"])
        self.assertTrue(reader.source_validator["revision_pinned"])

    def test_weak_etag_is_not_claimed_as_revision_pinning(self):
        data = b"x"*70000
        def opener(request, timeout=None):
            start, end = (int(x) for x in request.get_header("Range")[6:].split("-"))
            response = Response(data, start, end, len(data))
            response.headers["ETag"] = 'W/"weak"'
            return response
        reader = RangeZipReader("https://assets.kraken.com/test.zip",
                                expected_bytes=len(data), opener=opener)
        reader.read(3)
        reader.read(4)
        self.assertFalse(reader.source_validator["revision_pinned"])

    def test_content_length_mismatch_rejected(self):
        data = b"x"*70000
        def opener(request, timeout=None):
            start, end = (int(x) for x in request.get_header("Range")[6:].split("-"))
            response = Response(data, start, end, len(data))
            response.headers["Content-Length"] = "999"
            return response
        reader = RangeZipReader("https://assets.kraken.com/test.zip",
                                expected_bytes=len(data), opener=opener)
        with self.assertRaisesRegex(RuntimeError, "response length"):
            reader.read(3)



if __name__ == "__main__":
    unittest.main()
