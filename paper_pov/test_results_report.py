"""Fail-closed paper results tests; no network or production writes."""
import copy
import datetime as dt
import unittest

from paper_pov.results_report import render

SHA = "a" * 40
LEDGER = "b" * 40
NOW = "2026-10-31T20:30:00+00:00"
QUOTE = "2026-10-31T20:29:00+00:00"


def fixture():
    scan = {
        "mode": "PAPER_ONLY", "buy_approved": False, "production_applied": False,
        "forward_labels": 0, "started_at": "2026-10-31T20:27:00+00:00",
        "as_of": NOW, "eligible_pairs": 620, "observed_markets": 2,
        "ohlc_screened": 2, "abstentions": [{"pair": "XYZUSD", "reason": "gap"}],
        "observations": [
            {"pair": "XBTUSD", "symbol": "XBT/USD", "price": 71000.0, "observed_at": QUOTE},
            {"pair": "ETHUSD", "symbol": "ETH/USD", "price": 4000.0, "observed_at": QUOTE},
        ],
        "watch": [],
    }
    for i, (pair, symbol, price) in enumerate(
        [("XBTUSD", "XBT/USD", 71000.0), ("ETHUSD", "ETH/USD", 4000.0)], 1
    ):
        scan["watch"].append({
            "pair": pair, "symbol": symbol, "price": price,
            "rank": i, "status": "PAPER_WATCH", "as_of": NOW,
            "quote_observed_at": QUOTE, "ohlc_age_seconds": 200,
            "move_since_utc_open_pct": 2.0, "move15_pct": 0.7,
            "volume_accel": 1.4, "spread_bps": 5.0,
            "baseline_score": 30.0, "challenger_score": 34.0,
            "prediction_id": str(i) * 64,
        })
    score = {
        "generation": 8, "actual_scans": 8, "immutable_predictions": 96,
        "market_observations": 4891, "matured_labels": 0,
        "gap_abstentions": 72, "observed_30pct_hits": 0,
        "held_out_lift": None, "production_applied": False,
        "ledger_sha256": "f" * 64,
    }
    return scan, score


class PaperResultsContracts(unittest.TestCase):
    def report(self, scan=None, score=None, event="schedule"):
        s, b = fixture()
        return render(s if scan is None else scan, b if score is None else score,
                      run_id="41235442591", source_sha=SHA, ledger_commit=LEDGER, event=event)

    def test_github_event_provenance_is_explicit_and_fail_closed(self):
        scheduled, scheduled_md = self.report(event="schedule")
        self.assertEqual(scheduled["github_event"], "schedule")
        self.assertFalse(scheduled["scheduled_slot_verified"])
        self.assertIn("GitHub trigger:** scheduled", scheduled_md)
        self.assertIn("exact cron slot NOT inferred", scheduled_md)
        manual, manual_md = self.report(event="workflow_dispatch")
        self.assertEqual(manual["github_event"], "workflow_dispatch")
        self.assertIn("GitHub trigger:** manual dispatch", manual_md)
        for invalid in (None, "", "push", "pull_request", "schedule:39", True):
            with self.subTest(event=invalid), self.assertRaisesRegex(ValueError, "GitHub trigger"):
                self.report(event=invalid)

    def test_realistic_report_is_readable_and_not_a_buy_signal(self):
        payload, md = self.report()
        self.assertEqual(payload["status"], "SUCCESS_PAPER_ONLY")
        self.assertEqual(len(payload["candidates"]), 2)
        self.assertTrue(payload["remote_readback_verified"])
        self.assertIsNone(payload["held_out_lift"])
        self.assertIsNone(payload["missed_movers"])
        self.assertIn("XBT/USD", md)
        self.assertIn("Challenger score", md)
        self.assertIn("Baseline score", md)
        self.assertIn("| 1 | XBT/USD | 71000 | 34.000 | 30.000 |", md)
        self.assertIn("2026-10-31T20:29:00+00:00", md)
        self.assertEqual(payload["candidates"][0]["challenger_score"], 34.0)
        self.assertEqual(payload["candidates"][0]["baseline_score"], 30.0)
        self.assertEqual(payload["candidates"][0]["quote_observed_at"], QUOTE)
        self.assertEqual(payload["candidates"][0]["ohlc_age_seconds"], 200)
        self.assertIn("not probabilities or validated improvement", md)
        self.assertIn("NOT MATURED", md)
        self.assertIn("WATCH", md)
        self.assertIn("NOT CALIBRATED", md)
        self.assertIn("exchange-event freshness is NOT independently proven", md)

    def test_reject_trading_authorization(self):
        s, b = fixture()
        s["buy_approved"] = True
        with self.assertRaises(ValueError):
            self.report(s, b)

    def test_reject_production_or_fabricated_lift(self):
        s, b = fixture()
        b["production_applied"] = True
        with self.assertRaises(ValueError):
            self.report(s, b)
        b["production_applied"] = False
        b["held_out_lift"] = 1.2
        with self.assertRaises(ValueError):
            self.report(s, b)

    def test_reject_stale_or_future_quotes(self):
        s, b = fixture()
        s["observations"][0]["observed_at"] = "2026-10-31T20:18:00+00:00"
        with self.assertRaises(ValueError):
            self.report(s, b)
        s, b = fixture()
        s["observations"][0]["observed_at"] = "2026-10-31T20:31:00+00:00"
        with self.assertRaises(ValueError):
            self.report(s, b)

    def test_reject_mismatched_asof_price_or_quote_timestamp(self):
        for key, bad in (("price", 70000), ("quote_observed_at", "2026-10-31T20:28:00+00:00"),
                         ("as_of", "2026-10-31T20:31:00+00:00")):
            s, b = fixture()
            s["watch"][0][key] = bad
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.report(s, b)

    def test_reject_stablecoin_watch(self):
        s, b = fixture()
        s["watch"][0]["symbol"] = "USDT/USD"
        with self.assertRaises(ValueError):
            self.report(s, b)

    def test_reject_symbol_spoofing_even_with_matching_pair_price_and_quote_time(self):
        # The old reporter trusted WATCH symbol independently of its observed
        # Kraken quote; a spoofed non-stable label could misidentify a coin.
        s, b = fixture()
        s["watch"][0]["symbol"] = "LTC/USD"
        with self.assertRaisesRegex(ValueError, "symbol differs"):
            self.report(s, b)
        s, b = fixture()
        s["observations"][0]["symbol"] = "LTC/USD"
        with self.assertRaisesRegex(ValueError, "symbol differs"):
            self.report(s, b)

    def test_reject_unattributed_or_excluded_observation_symbols(self):
        for value in (None, "", "/USD", "./USD", "-/USD", "LTC/EUR", "USDT/USD", "XBT/USD/EXTRA", True):
            s, b = fixture()
            s["observations"][0]["symbol"] = value
            with self.subTest(symbol=value), self.assertRaisesRegex(ValueError, "observed quote symbol"):
                self.report(s, b)

    def test_reject_spoofed_empty_base_even_if_watch_and_quote_agree(self):
        s, b = fixture()
        s["observations"][0]["symbol"] = "/USD"
        s["watch"][0]["symbol"] = "/USD"
        with self.assertRaisesRegex(ValueError, "observed quote symbol"):
            self.report(s, b)

    def test_reject_unsealed_ledger_and_unpersisted_counts(self):
        s, b = fixture()
        b["ledger_sha256"] = "bad"
        with self.assertRaises(ValueError):
            self.report(s, b)
        s, b = fixture()
        b["immutable_predictions"] = 1
        with self.assertRaises(ValueError):
            self.report(s, b)

    def test_reject_nonfinite_early_mover_evidence(self):
        s, b = fixture()
        s["watch"][0]["volume_accel"] = float("inf")
        with self.assertRaises(ValueError):
            self.report(s, b)

    def test_reject_nonfinite_scores_before_publication(self):
        for key, value in (("baseline_score", float("nan")),
                           ("challenger_score", float("inf")),
                           ("challenger_score", True)):
            s, b = fixture()
            s["watch"][0][key] = value
            with self.subTest(key=key, value=str(value)), self.assertRaises(ValueError):
                self.report(s, b)

    def test_reject_duplicate_predictions_and_noncontiguous_ranks(self):
        s, b = fixture()
        s["watch"][1]["pair"] = "XBTUSD"
        with self.assertRaises(ValueError):
            self.report(s, b)
        s, b = fixture()
        s["watch"][1]["rank"] = 3
        with self.assertRaises(ValueError):
            self.report(s, b)

    def test_reject_missing_immutable_identity(self):
        s, b = fixture()
        with self.assertRaises(ValueError):
            render(s, b, run_id="test", source_sha=SHA, ledger_commit=LEDGER, event="schedule")
        with self.assertRaises(ValueError):
            render(s, b, run_id="1", source_sha="unknown", ledger_commit=LEDGER, event="schedule")

    def test_all_four_horizons_are_explicit_without_invented_counts(self):
        payload, md = self.report()
        self.assertEqual(set(payload["horizons"]), {"1", "6", "24", "48"})
        for h in ("1", "6", "24", "48"):
            self.assertEqual(payload["horizons"][h]["status"], "NOT_MATURED_OR_INELIGIBLE")
            self.assertIsNone(payload["horizons"][h]["verified_matured_count"])
            self.assertIsNone(payload["horizons"][h]["verified_hits"])
            self.assertIn("| " + h + "h |", md)
        self.assertFalse(payload["storage_recovery_verified_this_run"])
        self.assertIn("NOT VERIFIED by this scan alone", md)

    def test_aggregate_maturity_never_claims_per_horizon_evidence(self):
        s, b = fixture()
        b["matured_labels"] = 2
        b["observed_30pct_hits"] = 1
        payload, md = self.report(s, b)
        for horizon in payload["horizons"].values():
            self.assertEqual(horizon["status"], "PER_HORIZON_NOT_INDEPENDENTLY_VERIFIED")
            self.assertIsNone(horizon["verified_hits"])
        self.assertIn("NOT INDEPENDENTLY VERIFIED", md)
        self.assertIsNone(payload["held_out_lift"])

    def test_reject_hits_without_matured_outcomes(self):
        s, b = fixture()
        b["observed_30pct_hits"] = 1
        with self.assertRaises(ValueError):
            self.report(s, b)
        b["matured_labels"] = 1
        b["observed_30pct_hits"] = 2
        with self.assertRaises(ValueError):
            self.report(s, b)

    def test_reject_inconsistent_market_coverage(self):
        for field, bad in (("eligible_pairs", 1), ("observed_markets", 3),
                           ("ohlc_screened", 3), ("eligible_pairs", True),
                           ("ohlc_screened", -1)):
            s, b = fixture()
            s[field] = bad
            with self.subTest(field=field, bad=bad), self.assertRaises(ValueError):
                self.report(s, b)

    def test_reject_nonregressing_but_wrong_scan_count(self):
        s, b = fixture()
        b["actual_scans"] = 9
        with self.assertRaises(ValueError):
            self.report(s, b)

    def test_matured_count_does_not_invent_per_horizon_lift(self):
        s, b = fixture()
        b["matured_labels"] = 4
        payload, md = self.report(s, b)
        self.assertEqual(payload["matured_labels"], 4)
        self.assertIn("Per-horizon counts require independent audit", md)
        self.assertNotIn("All horizons NOT MATURED", md)


if __name__ == "__main__":
    unittest.main()
