"""Synthetic, read-only storage forecasts. Never authorizes a second writer."""
import datetime as dt
import hashlib
import unittest
from unittest import mock

from paper_eval.capacity import capacity_report
from paper_pov import ledger, segmented_storage as storage


def fixture(scans=3, quotes=100):
    state = ledger.empty()
    for i in range(scans):
        stamp = (dt.datetime(2026, 10, 31, 12, tzinfo=dt.timezone.utc)
                 + dt.timedelta(hours=i)).isoformat()
        rid = ("a" * 63) + format(i, "x")
        pid = hashlib.sha256(("paper-v1|" + stamp + "|C0USD").encode()).hexdigest()
        state["runs"].append({
            "id": rid, "as_of": stamp, "source_sha": "b" * 40,
            "report_sha256": "c" * 64, "watch_count": 1,
            "observation_count": quotes,
        })
        state["predictions"].append({
            "prediction_id": pid, "run_id": rid, "as_of": stamp,
            "pair": "C0USD", "price": 1.1,
            "baseline_score": 12.0, "challenger_score": 13.0, "rank": 1,
        })
        for n in range(quotes):
            state["observations"].append({
                "run_id": rid, "at": stamp, "pair": "C" + str(n) + "USD",
                "price": 1.1,
            })
    state["generation"] = scans
    ledger.seal(state)
    ledger.verify(state)
    return state


class StorageForecastTests(unittest.TestCase):
    def test_two_per_hour_uses_more_capacity_than_one(self):
        r = capacity_report(fixture())
        self.assertGreater(r["cadences"]["2"]["forecast_ledger_bytes"],
                           r["cadences"]["1"]["forecast_ledger_bytes"])
        self.assertEqual(r["cadences"]["2"]["modeled_active_runs"], 104)
        self.assertEqual(r["cadences"]["2"]["modeled_30d_index_runs"], 1444)

    def test_20pct_headroom_required(self):
        r = capacity_report(fixture(), max_bytes=100)
        self.assertFalse(r["stage2_storage_gate_pass"])
        self.assertFalse(r["cadences"]["2"]["storage_capacity_pass"])

    def test_generous_limit_passes_storage_only(self):
        r = capacity_report(fixture(), max_bytes=1_000_000_000)
        self.assertTrue(r["stage2_storage_gate_pass"])
        self.assertIs(r["stage2_authorized"], False)
        self.assertIsNone(r["independent_held_out_lift"])

    def test_requires_multiple_actual_ledger_samples(self):
        r = capacity_report(fixture(scans=2), max_bytes=1_000_000_000)
        self.assertFalse(r["stage2_storage_gate_pass"])
        self.assertFalse(r["sample_sufficient"])

    def test_tiny_market_sample_cannot_clear_gate(self):
        r = capacity_report(fixture(quotes=2), max_bytes=1_000_000_000)
        self.assertFalse(r["stage2_storage_gate_pass"])

    def test_resealed_but_orphaned_history_rejected(self):
        s = fixture()
        s["observations"][0]["run_id"] = "d" * 64
        ledger.seal(s)
        with self.assertRaises(ValueError):
            capacity_report(s)

    def test_tampered_checksum_rejected(self):
        s = fixture()
        s["observations"][0]["price"] = 2.0
        with self.assertRaises(ValueError):
            capacity_report(s)

    def test_capacity_parameter_must_be_positive_int(self):
        for bad in (True, -1, 0, 1.2):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                capacity_report(fixture(), max_bytes=bad)

    def test_forecast_includes_matured_not_only_gap_outcomes(self):
        s = fixture()
        r = capacity_report(s)
        self.assertGreater(r["serialized_max_record_bytes"]["outcome"], 200)

    def test_more_market_quotes_cannot_reduce_forecast(self):
        small = capacity_report(fixture(quotes=100))
        large = capacity_report(fixture(quotes=200))
        self.assertGreater(large["cadences"]["2"]["forecast_ledger_bytes"],
                           small["cadences"]["2"]["forecast_ledger_bytes"])

    def test_packed_snapshot_is_lossless_and_not_cadence_authorization(self):
        state = fixture()
        report = capacity_report(state)
        packed = storage.pack_snapshot(state)
        self.assertEqual(report["candidate_packed_snapshot_bytes"], len(packed))
        self.assertEqual(report["packed_snapshot_limit_bytes"], storage.MAX_PACKED_BYTES)
        self.assertEqual(storage.unpack_snapshot(packed), state)
        self.assertIs(report["stage2_authorized"], False)
        self.assertIn("rehearsal", report["limitations"])

    def test_large_logical_capacity_verified_without_weakening_packed_limit(self):
        state = fixture()
        with mock.patch.object(ledger, "verify", wraps=ledger.verify) as verifier:
            capacity_report(state)
            self.assertTrue(any(
                call.args == (state, storage.MAX_RAW_BYTES)
                for call in verifier.call_args_list))
        self.assertEqual(storage.MAX_PACKED_BYTES, 12_000_000)

    def test_current_bytes_exact_canonical(self):
        s = fixture()
        r = capacity_report(s)
        self.assertEqual(r["current_ledger_bytes"], len(ledger.canonical(s)))


if __name__ == "__main__":
    unittest.main()
