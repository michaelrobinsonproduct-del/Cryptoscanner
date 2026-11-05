"""Focused immutable A2 candidate readback acceptance tests."""
import datetime as dt
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from paper_pov.candidate_snapshot import read_snapshot

NOW = dt.datetime(2026, 11, 3, 17, 0, 30, tzinfo=dt.timezone.utc)
STAMP = "2026-11-03T17:00:00+00:00"

class SnapshotTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.latest = Path(self.tmp.name) / "latest.json"
        self.report = {"as_of": STAMP, "mode": "PAPER_ONLY", "buy_approved": False,
                       "scan_status": "WATCH", "eligible_pairs": 20, "observed_markets": 20,
                       "abstention_counts": {"ohlc_gap_or_schema": 2}, "watch": [self.candidate()]}
        self.seal()

    def candidate(self):
        pair = "TESTUSD"
        return {"pair": pair, "symbol": "TEST/USD", "rank": 1, "status": "PAPER_WATCH", "buy_approved": False,
                "as_of": STAMP, "quote_observed_at": STAMP, "ohlc_last_closed_at": STAMP,
                "quote_timestamp_semantics": "client_observed_not_exchange_event_time",
                "prediction_id": hashlib.sha256(("paper-v1|" + STAMP + "|" + pair).encode()).hexdigest(),
                "price": 1.5, "move15_pct": 2.0, "volume_accel": 1.4,
                "baseline_score": 45.0, "challenger_score": 60.0, "spread_bps": 5.0,
                "risk": "ELEVATED", "momentum_reference": "completed_5m_candles_15m",
                "volume_acceleration_reference": "last_30m_over_prior_30m"}

    def seal(self):
        raw = json.dumps(self.report, sort_keys=True, separators=(",", ":")).encode()
        self.latest.write_bytes(raw)
        directory = self.latest.parent / "receipts"
        directory.mkdir(exist_ok=True)
        (directory / "20261103T170000000000Z.json").write_bytes(raw)

    def test_incomplete_ticker_abstention_round_trip_and_contradiction(self):
        self.report["watch"] = []
        self.report["scan_status"] = "ABSTAIN_INCOMPLETE_TICKER_COVERAGE"
        self.report["ticker_coverage_complete"] = False
        self.report["ticker_rejections"] = {"missing_or_invalid_payload": 1}
        self.report["observed_markets"] = 19
        self.seal()
        result = read_snapshot(self.latest, NOW)
        self.assertEqual(result["watch"], [])
        self.assertEqual(result["scan_status"], "ABSTAIN_INCOMPLETE_TICKER_COVERAGE")
        self.report["ticker_coverage_complete"] = True
        self.seal()
        with self.assertRaisesRegex(ValueError, "missing source evidence"):
            read_snapshot(self.latest, NOW)

    def test_incomplete_coverage_all_rejection_categories(self):
        self.report["watch"] = []
        self.report["scan_status"] = "ABSTAIN_INCOMPLETE_TICKER_COVERAGE"
        self.report["ticker_coverage_complete"] = False
        self.report["observed_markets"] = 19
        for category in ("missing_or_invalid_payload", "invalid_price_or_volume",
                         "nonfinite_derived_metric"):
            with self.subTest(category=category):
                self.report["ticker_rejections"] = {
                    "missing_or_invalid_payload": 0,
                    "invalid_price_or_volume": 0,
                    "nonfinite_derived_metric": 0,
                }
                self.report["ticker_rejections"][category] = 1
                self.seal()
                self.assertEqual(read_snapshot(self.latest, NOW)["watch"], [])
        for bad in (0, -1, True, "1"):
            with self.subTest(bad=bad):
                self.report["ticker_rejections"] = {"invalid_price_or_volume": bad}
                self.seal()
                with self.assertRaisesRegex(ValueError, "ticker evidence"):
                    read_snapshot(self.latest, NOW)

    def test_realistic_watch_readback(self):
        result = read_snapshot(self.latest, NOW)
        self.assertEqual(result["watch"][0]["pair"], "TESTUSD")
        self.assertEqual(result["snapshot_age_seconds"], 30)
        self.assertEqual(result["abstention_counts"]["ohlc_gap_or_schema"], 2)

    def test_missing_or_forged_risk_and_metric_provenance_rejected(self):
        for field, bad, message in (
            ("risk", None, "risk classification"),
            ("risk", "HIGH", "risk classification"),
            ("momentum_reference", "unverified", "metric provenance"),
            ("volume_acceleration_reference", None, "metric provenance"),
        ):
            with self.subTest(field=field, bad=bad):
                original = self.report["watch"][0][field]
                self.report["watch"][0][field] = bad
                self.seal()
                with self.assertRaisesRegex(ValueError, message):
                    read_snapshot(self.latest, NOW)
                self.report["watch"][0][field] = original

    def test_display_symbol_required_for_b_delivery(self):
        for bad in (None, "", "TEST USD", "X" * 65, "TEST/EUR", "TEST/USD/USD", "/USD", "TEST/usd"):
            with self.subTest(symbol=bad):
                self.report["watch"][0]["symbol"] = bad
                self.seal()
                with self.assertRaisesRegex(ValueError, "invalid WATCH display symbol"):
                    read_snapshot(self.latest, NOW)
        self.report["watch"][0]["symbol"] = "TEST/USD"
        self.seal()
        self.assertEqual(read_snapshot(self.latest, NOW)["watch"][0]["symbol"], "TEST/USD")

    def test_persisted_watch_order_must_match_challenger_scores(self):
        first = self.report["watch"][0]
        second = dict(first, pair="OTHERUSD", symbol="OTHER/USD", rank=2,
                      challenger_score=first["challenger_score"] + 1)
        second["prediction_id"] = hashlib.sha256(
            ("paper-v1|" + STAMP + "|OTHERUSD").encode()).hexdigest()
        self.report["watch"].append(second)
        self.seal()
        with self.assertRaisesRegex(ValueError, "WATCH challenger ranking mismatch"):
            read_snapshot(self.latest, NOW)
        self.report["watch"] = [dict(second, rank=1), dict(first, rank=2)]
        self.seal()
        self.assertEqual(len(read_snapshot(self.latest, NOW)["watch"]), 2)

    def test_duplicate_display_symbol_different_pair_rejected(self):
        first = self.report["watch"][0]
        second = dict(first, pair="ALIASUSD", rank=2,
                      challenger_score=first["challenger_score"] - 1)
        second["prediction_id"] = hashlib.sha256(
            ("paper-v1|" + STAMP + "|ALIASUSD").encode()).hexdigest()
        self.report["watch"].append(second)
        self.seal()
        with self.assertRaisesRegex(ValueError, "duplicate WATCH display symbol"):
            read_snapshot(self.latest, NOW)

    def test_boolean_watch_rank_rejected(self):
        self.report["watch"][0]["rank"] = True
        self.seal()
        with self.assertRaisesRegex(ValueError, "invalid paper candidate contract"):
            read_snapshot(self.latest, NOW)

    def test_stablecoin_watch_rejected_at_persisted_boundary(self):
        self.report["watch"][0]["symbol"] = "USDT/USD"
        self.seal()
        with self.assertRaisesRegex(ValueError, "stablecoin WATCH"):
            read_snapshot(self.latest, NOW)

    def test_completed_ohlc_must_be_fresh_at_scan_and_readback(self):
        for closed, now, message in (
            (None, NOW, "missing completed OHLC"),
            ("2026-11-03T16:49:00+00:00", NOW, "stale completed OHLC"),
            ("2026-11-03T16:50:20+00:00", NOW, "expired completed OHLC"),
            ("2026-11-03T17:00:45+00:00", NOW, "stale completed OHLC"),
        ):
            with self.subTest(closed=closed):
                self.report["watch"][0]["ohlc_last_closed_at"] = closed
                self.seal()
                with self.assertRaisesRegex(ValueError, message):
                    read_snapshot(self.latest, now)
        self.report["watch"][0]["ohlc_last_closed_at"] = STAMP
        self.seal()
        self.assertEqual(len(read_snapshot(self.latest, NOW)["watch"]), 1)

    def test_zero_watch_abstention_readback(self):
        self.report.update(watch=[], scan_status="ABSTAIN_NO_QUALIFIED_OHLC")
        self.seal()
        self.assertEqual(read_snapshot(self.latest, NOW)["watch"], [])

    def test_read_time_quote_expiration_rejected_even_when_scan_fresh(self):
        # Scan is only 30 seconds old, but the quote is older than 10m.
        self.report["watch"][0]["quote_observed_at"] = "2026-11-03T16:50:00+00:00"
        self.seal()
        with self.assertRaisesRegex(ValueError, "expired candidate quote"):
            read_snapshot(self.latest, NOW)

    def test_quote_age_exposed_in_read_only_output(self):
        self.report["watch"][0]["quote_observed_at"] = "2026-11-03T16:59:00+00:00"
        self.seal()
        result = read_snapshot(self.latest, NOW)
        self.assertEqual(result["quote_age_seconds"], {"TESTUSD": 90.0})
        self.assertEqual(result["snapshot_age_seconds"], 30)

    def test_future_quote_relative_to_reader_rejected(self):
        self.report["watch"][0]["quote_observed_at"] = "2026-11-03T17:00:45+00:00"
        self.seal()
        with self.assertRaisesRegex(ValueError, "stale candidate quote"):
            read_snapshot(self.latest, NOW)

    def test_invalid_verification_clock_and_age_policy_rejected(self):
        with self.assertRaisesRegex(ValueError, "naive verification clock"):
            read_snapshot(self.latest, dt.datetime(2026, 11, 3, 17, 0, 30))
        for limit in (0, -1, True, float("nan"), 601):
            with self.subTest(limit=limit), self.assertRaisesRegex(ValueError, "invalid maximum quote age"):
                read_snapshot(self.latest, NOW, max_age_seconds=limit)

    def test_zero_watch_has_empty_quote_ages(self):
        self.report.update(watch=[], scan_status="ABSTAIN_NO_QUALIFIED_OHLC")
        self.seal()
        self.assertEqual(read_snapshot(self.latest, NOW)["quote_age_seconds"], {})

    def test_missing_receipt_rejected(self):
        next((self.latest.parent / "receipts").glob("*.json")).unlink()
        with self.assertRaisesRegex(ValueError, "immutable receipt"):
            read_snapshot(self.latest, NOW)

    def test_rechecksummed_forged_candidate_rejected(self):
        self.report["watch"][0]["prediction_id"] = "forged"
        self.seal()
        with self.assertRaisesRegex(ValueError, "provenance"):
            read_snapshot(self.latest, NOW)

    def test_stale_snapshot_rejected(self):
        with self.assertRaisesRegex(ValueError, "stale or future"):
            read_snapshot(self.latest, NOW + dt.timedelta(minutes=11))

    def test_quote_timestamp_forgery_rejected(self):
        self.report["watch"][0]["quote_observed_at"] = "2026-11-03T16:30:00+00:00"
        self.seal()
        with self.assertRaisesRegex(ValueError, "stale candidate quote"):
            read_snapshot(self.latest, NOW)

    def test_duplicate_candidate_rejected(self):
        self.report["watch"].append(dict(self.report["watch"][0], rank=2))
        self.seal()
        with self.assertRaisesRegex(ValueError, "duplicate"):
            read_snapshot(self.latest, NOW)

    def test_coverage_cannot_exceed_eligible(self):
        self.report["observed_markets"] = 21
        self.seal()
        with self.assertRaisesRegex(ValueError, "coverage exceeds"):
            read_snapshot(self.latest, NOW)

    def test_abstention_counts_reject_negative_and_boolean(self):
        for bad in (-1, True, 1.5):
            with self.subTest(bad=bad):
                self.report["abstention_counts"] = {"ohlc_gap_or_schema": bad}
                self.seal()
                with self.assertRaisesRegex(ValueError, "invalid abstention"):
                    read_snapshot(self.latest, NOW)

    def test_watch_cannot_exceed_observed(self):
        self.report["observed_markets"] = 0
        self.seal()
        with self.assertRaisesRegex(ValueError, "watch exceeds"):
            read_snapshot(self.latest, NOW)

    def test_receipt_directory_symlink_rejected(self):
        receipt_dir = self.latest.parent / "receipts"
        target = self.latest.parent / "external"
        receipt_dir.rename(target)
        receipt_dir.symlink_to(target, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "immutable receipt"):
            read_snapshot(self.latest, NOW)

    def test_non_object_json_rejected(self):
        self.latest.write_text("[]")
        with self.assertRaisesRegex(ValueError, "invalid snapshot object"):
            read_snapshot(self.latest, NOW)

if __name__ == "__main__":
    unittest.main()
