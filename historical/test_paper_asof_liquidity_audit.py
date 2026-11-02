"""Adversarial unit tests for read-only PAPER liquidity replay."""
import datetime as dt
import hashlib
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

import paper_asof_liquidity_audit as audit


class LiquidityReplayTests(unittest.TestCase):
    def test_verifies_original_bytes(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "fixture.zip"
            payload = b'{"as_of":"2026-11-01T00:00:00Z"}'
            with zipfile.ZipFile(p, "w") as z:
                z.writestr("latest.json", payload)
                z.writestr("SHA256SUMS", hashlib.sha256(payload).hexdigest() + "  latest.json\n")
            self.assertEqual(audit.verified_zip(p)["latest.json"], payload)

    def test_rejects_self_inconsistent_payload(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "tampered.zip"
            with zipfile.ZipFile(p, "w") as z:
                z.writestr("latest.json", b"tampered")
                z.writestr("SHA256SUMS", hashlib.sha256(b"original").hexdigest() + "  latest.json\n")
            with self.assertRaisesRegex(ValueError, "SHA mismatch"):
                audit.verified_zip(p)

    def test_lag_never_uses_future(self):
        utc = dt.timezone.utc
        times = [dt.datetime(2026, 11, 1, 0, 0, tzinfo=utc) +
                 dt.timedelta(minutes=30 * i) for i in range(5)]
        prices = [{"A": p} for p in (10, 11, 12, 13, 14)]
        self.assertEqual(audit.lag(times, prices, 2, "A", 60, 5), 10)
        self.assertIsNone(audit.lag(times, prices, 1, "A", 60, 5))
        self.assertEqual(audit.lag(times, prices, 4, "A", 60, 5), 12)

    def test_missing_source_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(FileNotFoundError):
                audit.analyze(Path(d))


if __name__ == "__main__":
    unittest.main()
