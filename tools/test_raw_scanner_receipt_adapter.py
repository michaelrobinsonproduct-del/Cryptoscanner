import datetime as dt
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from tools.a2_verified_snapshot_bridge import read_scanner_receipt_zip, assess_verified_a2

NOW = dt.datetime(2026, 11, 4, 0, 19, 20, tzinfo=dt.timezone.utc)


def make_report():
    stamp = "2026-11-04T00:19:09.285867+00:00"
    return {"as_of": stamp, "mode": "PAPER_ONLY", "buy_approved": False,
            "production_applied": False, "scan_status": "WATCH",
            "eligible_pairs": 605, "observed_markets": 602,
            "watch": [{"pair": "CAPUSD", "rank": 1, "status": "PAPER_WATCH",
                       "buy_approved": False, "quote_observed_at": "2026-11-04T00:19:07.832469+00:00",
                       "quote_timestamp_semantics": "client_observed_not_exchange_event_time"}]}


class RawScannerReceiptTests(unittest.TestCase):
    def write_zip(self, report, mismatch=False):
        raw = json.dumps(report, sort_keys=True).encode()
        receipt = b'{}' if mismatch else raw
        tmp = tempfile.NamedTemporaryFile(suffix=".zip", delete=False)
        tmp.close()
        with zipfile.ZipFile(tmp.name, "w") as z:
            z.writestr("latest.json", raw)
            z.writestr("receipts/20261104T001909285867Z.json", receipt)
        self.addCleanup(Path(tmp.name).unlink, missing_ok=True)
        return tmp.name

    def test_actual_two_member_contract(self):
        verified = read_scanner_receipt_zip(self.write_zip(make_report()), now=NOW)
        result = assess_verified_a2(verified)
        self.assertTrue(result["accepted"], result)
        self.assertEqual(result["paper_watch_count"], 1)
        self.assertFalse(result["live_watch_certified"])

    def test_immutable_receipt_mismatch_rejected(self):
        with self.assertRaises(ValueError):
            read_scanner_receipt_zip(self.write_zip(make_report(), mismatch=True), now=NOW)

    def test_stale_snapshot_rejected(self):
        with self.assertRaises(ValueError):
            read_scanner_receipt_zip(self.write_zip(make_report()), now=NOW + dt.timedelta(minutes=11))

    def test_future_snapshot_rejected(self):
        with self.assertRaises(ValueError):
            read_scanner_receipt_zip(self.write_zip(make_report()), now=NOW - dt.timedelta(seconds=1))


if __name__ == "__main__":
    unittest.main()
