"""Adversarial, offline, source-bound historical readiness tests."""
import csv
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

from research.kraken_archive_readiness import ARCHIVE_SHA, inspect_retained

NAME = "XBTUSD_5.csv"
BASE = 1700000100


class ReadinessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "retained.zip"

    def make(self, timestamps=None, *, manifest_patch=None, member_patch=None,
             extra=None, duplicate=False):
        if timestamps is None:
            timestamps = [BASE + 300 * i for i in range(14)]
        stream = io.StringIO()
        writer = csv.writer(stream, lineterminator="\n")
        for ts in timestamps:
            writer.writerow([ts, "1.0", "1.4", "0.9", "1.1", "20", "2"])
        payload = stream.getvalue().encode()
        if member_patch is not None:
            payload = member_patch
        manifest = {
            "schema": 1,
            "source_archive_sha256": ARCHIVE_SHA,
            "real_labels": 0,
            "independent_trade_completeness": False,
            "source_timestamp_semantics": "candle_open_candidate",
            "held_out_evaluation": "not_authorized",
            "markets": {NAME: {
                "retained_sha256": hashlib.sha256(payload).hexdigest(),
                "retained_rows": len(timestamps),
                "retained_first_open": timestamps[0],
                "retained_last_open": timestamps[-1],
            }},
        }
        if manifest_patch:
            manifest.update(manifest_patch)
        with zipfile.ZipFile(self.path, "w") as z:
            z.writestr("candles/" + NAME, payload)
            z.writestr("manifest.json", json.dumps(manifest))
            if extra:
                z.writestr(extra, b"unexpected")
            if duplicate:
                z.writestr("manifest.json", json.dumps(manifest))
        return self.path

    def test_contiguous_candidate_windows_not_authenticated_episodes(self):
        result = inspect_retained(self.make())
        self.assertEqual(result["markets"], 1)
        self.assertEqual(result["retained_rows"], 14)
        self.assertEqual(result["candidate_windows"]["1"], 2)
        self.assertEqual(result["candidate_windows"]["6"], 0)
        self.assertEqual(result["authenticated_first_entry_episodes"], 0)
        self.assertFalse(result["has_first_observed_at"])
        self.assertFalse(result["independent_trade_completeness"])
        self.assertIsNone(result["held_out_lift"])

    def test_discontinuity_never_fills_future_window(self):
        stamps = [BASE + 300 * i for i in range(8)]
        stamps += [BASE + 300 * (i + 30) for i in range(8)]
        result = inspect_retained(self.make(stamps))
        self.assertEqual(result["candidate_windows"]["1"], 0)
        self.assertEqual(result["per_market"][NAME]["contiguous_segments"], 2)

    def test_reject_claim_of_independent_trade_completeness(self):
        with self.assertRaisesRegex(ValueError, "untrusted"):
            inspect_retained(self.make(manifest_patch={"independent_trade_completeness": True}))

    def test_reject_forged_historical_labels(self):
        with self.assertRaisesRegex(ValueError, "untrusted"):
            inspect_retained(self.make(manifest_patch={"real_labels": 1}))

    def test_reject_wrong_archive_identity(self):
        with self.assertRaisesRegex(ValueError, "untrusted"):
            inspect_retained(self.make(manifest_patch={"source_archive_sha256": "0" * 64}))

    def test_reject_corrupt_retained_hash(self):
        path = self.make()
        with zipfile.ZipFile(path) as z:
            payload = z.read("candles/" + NAME)
        with zipfile.ZipFile(path, "w") as z:
            z.writestr("candles/" + NAME, payload + b"\n")
            z.writestr("manifest.json", json.dumps({
                "schema": 1, "source_archive_sha256": ARCHIVE_SHA,
                "real_labels": 0, "independent_trade_completeness": False,
                "source_timestamp_semantics": "candle_open_candidate",
                "held_out_evaluation": "not_authorized",
                "markets": {NAME: {"retained_sha256": hashlib.sha256(payload).hexdigest()}}
            }))
        with self.assertRaisesRegex(ValueError, "SHA256 mismatch"):
            inspect_retained(path)

    def test_reject_duplicate_archive_members(self):
        with self.assertWarns(UserWarning):
            self.make(duplicate=True)
        with self.assertRaisesRegex(ValueError, "duplicate"):
            inspect_retained(self.path)

    def test_reject_extra_archive_member(self):
        with self.assertRaisesRegex(ValueError, "unexpected"):
            inspect_retained(self.make(extra="unverified.json"))

    def test_reject_nonmonotonic_timestamps(self):
        stamps = [BASE, BASE + 300, BASE + 300]
        with self.assertRaisesRegex(ValueError, "invalid OHLCVT"):
            inspect_retained(self.make(stamps))

    def test_reject_invalid_candle_geometry(self):
        payload = (f"{BASE},1,0.5,0.9,1.1,20,2\n").encode()
        with self.assertRaisesRegex(ValueError, "invalid OHLCVT"):
            inspect_retained(self.make([BASE], member_patch=payload))

    def test_reject_metadata_row_count_forgery(self):
        path = self.make()
        with zipfile.ZipFile(path) as z:
            payload = z.read("candles/" + NAME)
            manifest = json.loads(z.read("manifest.json"))
        manifest["markets"][NAME]["retained_rows"] = 999
        with zipfile.ZipFile(path, "w") as z:
            z.writestr("candles/" + NAME, payload)
            z.writestr("manifest.json", json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "metadata mismatch"):
            inspect_retained(path)


if __name__ == "__main__":
    unittest.main()
