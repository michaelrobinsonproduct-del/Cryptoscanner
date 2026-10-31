import hashlib
import io
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from reconcile_retained_trade_evidence import reconcile, _candidate_windows
from inventory_kraken_archive import EXPECTED_SHA256


class RetainedReconciliationTests(unittest.TestCase):
    def fixture(self, root, *, bad_volume=False, duplicate_id=False, missing_trade=False):
        candle = ('300,100,101,100,101,7,2\n' if bad_volume
                  else '300,100,101,100,101,5,2\n').encode()
        trade = ('timestamp,price,volume,type,order_type,misc,trade_id\n'
                 '300,100,2,b,l,,id1\n')
        if not missing_trade:
            trade += '301,101,3,s,m,,id2\n'
        if duplicate_id:
            trade += '302,101,1,b,l,,id1\n'
        trade = trade.encode()
        om = {"schema": 1, "source_archive_sha256": EXPECTED_SHA256,
              "independent_trade_completeness": False,
              "markets": {"ABUSD_5.csv": {
                  "retained_sha256": hashlib.sha256(candle).hexdigest(),
                  "retained_rows": 1}}}
        tm = {"schema_version": 1, "source_archive_full_sha256_verified": False,
              "real_labels": 0, "markets": {"ABUSD.csv": {
                  "member_sha256": hashlib.sha256(trade).hexdigest(),
                  "member_bytes": len(trade), "member_crc_verified": True}}}
        def nested(path, name, entries):
            buf = io.BytesIO()
            with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as z:
                for entry, data in entries.items():
                    z.writestr(entry, data)
            with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as z:
                z.writestr(name, buf.getvalue())
        o, t = Path(root)/"o.zip", Path(root)/"t.zip"
        nested(o, "reusable_ohlc_evidence.zip",
               {"manifest.json": json.dumps(om), "candles/ABUSD_5.csv": candle})
        nested(t, "bounded_independent_trade_members.zip",
               {"manifest.json": json.dumps(tm), "trades/ABUSD.csv": trade})
        return o, t

    def test_realistic_exact_match_is_not_a_real_label(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root)
            r = reconcile(o, t,
                          expected_ohlc_digest=hashlib.sha256(o.read_bytes()).hexdigest(),
                          expected_trade_digest=hashlib.sha256(t.read_bytes()).hexdigest())
            m = r["markets"]["ABUSD.csv"]
            self.assertEqual(m["exact_trade_ohlc_candidate_intervals"], 1)
            self.assertEqual(m["verified_complete_intervals"], 0)
            self.assertEqual(r["real_labels"], 0)
            self.assertFalse(r["source_trade_archive_sha256_verified"])
            audit = m["candidate_outcome_audit"]
            self.assertEqual(audit["real_labels"], 0)
            self.assertEqual(audit["held_out_evaluation"], "not_authorized")
            self.assertEqual(audit["horizons"]["1"]["candidate_entries"], 1)
            self.assertEqual(audit["horizons"]["1"]["excluded_immature"], 1)

    def test_volume_mismatch_not_accepted(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root, bad_volume=True)
            m = reconcile(o, t)["markets"]["ABUSD.csv"]
            self.assertEqual(m["exact_trade_ohlc_candidate_intervals"], 0)
            self.assertEqual(m["mismatch_counts"]["aggregation_mismatch"], 1)

    def test_missing_trade_not_assumed_no_trade(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root, missing_trade=True)
            m = reconcile(o, t)["markets"]["ABUSD.csv"]
            self.assertEqual(m["exact_trade_ohlc_candidate_intervals"], 0)
            self.assertEqual(m["no_trade_or_source_gap_semantics"], "unknown")

    def test_duplicate_trade_id_fails_closed(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root, duplicate_id=True)
            with self.assertRaises(ValueError):
                reconcile(o, t)

    def test_artifact_digest_mismatch_fails_closed(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root)
            with self.assertRaises(ValueError):
                reconcile(o, t, expected_trade_digest="0"*64)

    def test_unpacked_actions_inner_zip_reuse(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root)
            oi, ti = Path(root)/"inner_o.zip", Path(root)/"inner_t.zip"
            with zipfile.ZipFile(o) as z:
                oi.write_bytes(z.read("reusable_ohlc_evidence.zip"))
            with zipfile.ZipFile(t) as z:
                ti.write_bytes(z.read("bounded_independent_trade_members.zip"))
            r = reconcile(oi, ti)
            self.assertEqual(r["markets"]["ABUSD.csv"]["exact_trade_ohlc_candidate_intervals"], 1)
            self.assertEqual(r["real_labels"], 0)

    def test_missing_future_candles_cannot_create_candidate_windows(self):
        timestamps = {300 + i*300 for i in range(13)}
        self.assertEqual(_candidate_windows(timestamps)["1"], 1)
        self.assertEqual(_candidate_windows(timestamps)["48"], 0)
        self.assertEqual(_candidate_windows(timestamps - {900})["1"], 0)

    def test_oversized_artifact_rejected_before_reading(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root)
            with o.open("r+b") as stream:
                stream.truncate(80 * 1024 * 1024 + 1)
            with self.assertRaisesRegex(ValueError, "oversized input artifact"):
                reconcile(o, t)

    def test_report_never_converts_exact_match_to_predictive_label(self):
        with tempfile.TemporaryDirectory() as root:
            o, t = self.fixture(root)
            report = reconcile(o, t)
            self.assertEqual(report["real_labels"], 0)
            self.assertEqual(report["held_out_evaluation"], "not_authorized")
            m = report["markets"]["ABUSD.csv"]
            self.assertEqual(m["candidate_outcome_audit"]["horizons"]["48"]["candidate_full_future_windows"], 0)
            self.assertEqual(m["verified_complete_intervals"], 0)
            self.assertEqual(m["no_trade_or_source_gap_semantics"], "unknown")


if __name__ == "__main__":
    unittest.main()
