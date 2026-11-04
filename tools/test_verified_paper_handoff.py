"""Actual two-member scanner transport -> independently reusable paper handoff."""
import datetime as dt
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from tools.a2_verified_snapshot_bridge import (
    read_scanner_receipt_zip, assess_verified_a2, write_verified_handoff,
)

NOW = dt.datetime(2026, 11, 4, 0, 19, 20, tzinfo=dt.timezone.utc)


def scan():
    return {"as_of": "2026-11-04T00:19:09+00:00",
            "mode": "PAPER_ONLY", "buy_approved": False,
            "production_applied": False, "scan_status": "WATCH",
            "eligible_pairs": 605, "observed_markets": 602,
            "watch": [{"pair": "CAPUSD", "rank": 1, "status": "PAPER_WATCH",
                       "buy_approved": False,
                       "quote_observed_at": "2026-11-04T00:19:07+00:00",
                       "quote_timestamp_semantics": "client_observed_not_exchange_event_time"}]}


def transport(path, report, *, tampered=False):
    raw = (json.dumps(report, sort_keys=True) + "\n").encode()
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("latest.json", raw)
        archive.writestr("receipts/20261104T001909Z.json", b"{}" if tampered else raw)


class HandoffTests(unittest.TestCase):
    def test_actual_scanner_to_create_only_candidate_handoff(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            transport(root / "scanner.zip", scan())
            verified = read_scanner_receipt_zip(root / "scanner.zip", now=NOW)
            payload = write_verified_handoff(verified, root / "handoff.json")
            stored = json.loads((root / "handoff.json").read_bytes())
            self.assertEqual(stored, payload)
            self.assertEqual(stored["watch"][0]["pair"], "CAPUSD")
            self.assertEqual(stored["scan_status"], "WATCH")
            self.assertEqual(stored["eligible_pairs"], 605)
            self.assertEqual(stored["observed_markets"], 602)
            self.assertEqual(stored["mode"], "VERIFIED_PAPER_WATCH_HANDOFF")
            self.assertEqual(stored["receipt_sha256"], verified["receipt_sha256"])
            self.assertFalse(stored["live_watch_certified"])
            self.assertFalse(stored["production_applied"])
            self.assertFalse(stored["trading_approved"])
            original = (root / "handoff.json").read_bytes()
            with self.assertRaises(FileExistsError):
                write_verified_handoff(verified, root / "handoff.json")
            self.assertEqual((root / "handoff.json").read_bytes(), original)

    def test_tampered_or_expired_source_never_publishes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for bad in ("tampered", "stale"):
                with self.subTest(bad=bad):
                    zip_path = root / (bad + ".zip")
                    transport(zip_path, scan(), tampered=bad == "tampered")
                    with self.assertRaises(ValueError):
                        verified = read_scanner_receipt_zip(
                            zip_path, now=NOW + (dt.timedelta(minutes=12)
                                               if bad == "stale" else dt.timedelta()))
                        write_verified_handoff(verified, root / (bad + ".json"))
                    self.assertFalse((root / (bad + ".json")).exists())

    def test_stablecoin_and_wrong_semantics_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for field, value in (("pair", "USDTUSD"),
                                 ("quote_timestamp_semantics", "exchange_event_time")):
                with self.subTest(field=field):
                    report = scan()
                    report["watch"][0][field] = value
                    archive = root / (field + ".zip")
                    transport(archive, report)
                    verified = read_scanner_receipt_zip(archive, now=NOW)
                    self.assertFalse(assess_verified_a2(verified)["accepted"])
                    with self.assertRaises(ValueError):
                        write_verified_handoff(verified, root / (field + ".json"))
                    self.assertFalse((root / (field + ".json")).exists())


if __name__ == "__main__":
    unittest.main()
