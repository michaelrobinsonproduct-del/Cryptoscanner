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
        "online_usd_pairs": 632, "excluded_stablecoin_pairs": 10,
        "excluded_other_pairs": 2,
        "ohlc_screened": 2, "abstentions": [{"pair": "XYZUSD", "reason": "gap"}],
        "observations": [
            {"pair": "XBTUSD", "symbol": "XBT/USD", "price": 71000.0, "observed_at": QUOTE, "source": "kraken_public_ticker_client_observed"},
            {"pair": "ETHUSD", "symbol": "ETH/USD", "price": 4000.0, "observed_at": QUOTE, "source": "kraken_public_ticker_client_observed"},
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
    def report(self, scan=None, score=None, event="schedule", cron="40 * * * *"):
        s, b = fixture()
        if event == "workflow_dispatch" and cron == "40 * * * *":
            cron = None
        return render(s if scan is None else scan, b if score is None else score,
                      run_id="41235442591", source_sha=SHA, ledger_commit=LEDGER,
                      event=event, originating_cron=cron)

    def test_github_event_provenance_is_explicit_and_fail_closed(self):
        scheduled, scheduled_md = self.report(event="schedule")
        self.assertEqual(scheduled["github_event"], "schedule")
        self.assertTrue(scheduled["scheduled_slot_verified"])
        self.assertEqual(scheduled["originating_cron"], "40 * * * *")
        self.assertEqual(scheduled["scheduled_slot_utc_minute"], 40)
        self.assertFalse(scheduled["scheduled_start_punctuality_verified"])
        self.assertIn("GitHub trigger:** scheduled", scheduled_md)
        self.assertIn("intended UTC minute=:40", scheduled_md)
        self.assertIn("punctuality NOT verified", scheduled_md)
        manual, manual_md = self.report(event="workflow_dispatch")
        self.assertEqual(manual["github_event"], "workflow_dispatch")
        self.assertFalse(manual["scheduled_slot_verified"])
        self.assertIsNone(manual["scheduled_slot_utc_minute"])
        self.assertIn("GitHub trigger:** manual dispatch", manual_md)
        for invalid in (None, "", "push", "pull_request", "schedule:39", True):
            with self.subTest(event=invalid), self.assertRaisesRegex(ValueError, "GitHub trigger"):
                self.report(event=invalid)

    def test_both_exact_crons_and_missing_or_spoofed_attribution(self):
        for cron, minute in (("40 * * * *", 40), ("10 * * * *", 10)):
            with self.subTest(cron=cron):
                payload, md = self.report(cron=cron)
                self.assertTrue(payload["scheduled_slot_verified"])
                self.assertEqual(payload["scheduled_slot_utc_minute"], minute)
                self.assertEqual(payload["originating_cron"], cron)
                self.assertIn(f"intended UTC minute=:{minute:02d}", md)
                self.assertFalse(payload["scheduled_start_punctuality_verified"])
        for bad in (None, "", "9,10 * * * *", "24 * * * *",
                    "10 * * * *; echo spoof", "40 * * * *\\n10 * * * *", True):
            with self.subTest(bad=bad), self.assertRaisesRegex(ValueError, "originating scheduled cron"):
                self.report(cron=bad)
        with self.assertRaisesRegex(ValueError, "Manual dispatch cannot claim"):
            self.report(event="workflow_dispatch", cron="10 * * * *")

    def test_single_writer_workflow_passes_github_schedule_as_data(self):
        from pathlib import Path
        workflow = (Path(__file__).resolve().parent.parent
                    / ".github/workflows/paper-pipeline.yml").read_text()
        self.assertIn("PAPER_ORIGINATING_CRON: ${{ github.event.schedule }}", workflow)
        self.assertIn('--originating-cron "$PAPER_ORIGINATING_CRON"', workflow)
        self.assertIn("- cron: '40 * * * *'", workflow)
        self.assertIn("- cron: '10 * * * *'", workflow)
        self.assertIn("group: public-paper-proof-ledger-single-writer", workflow)
        self.assertIn("cancel-in-progress: false", workflow)
        self.assertIn("git push origin HEAD:refs/heads/paper-proof-ledger", workflow)
        self.assertNotIn("git push --force", workflow)

    def test_cli_writes_checked_event_attested_artifacts(self):
        import hashlib
        import json
        import tempfile
        from pathlib import Path
        from unittest.mock import patch
        from paper_pov.results_report import main
        scan, score = fixture()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            scan_path, score_path, output = root / "scan.json", root / "score.json", root / "out"
            scan_path.write_text(json.dumps(scan))
            score_path.write_text(json.dumps(score))
            argv = ["paper-results", "--scan", str(scan_path),
                    "--scoreboard", str(score_path), "--run-id", "41235442591",
                    "--source-sha", SHA, "--ledger-commit", LEDGER,
                    "--event", "schedule", "--originating-cron", "10 * * * *",
                    "--output-dir", str(output)]
            with patch("sys.argv", argv):
                main()
            payload = json.loads((output / "results.json").read_text())
            self.assertEqual(payload["github_event"], "schedule")
            self.assertTrue(payload["scheduled_slot_verified"])
            self.assertEqual(payload["scheduled_slot_utc_minute"], 10)
            self.assertFalse(payload["scheduled_start_punctuality_verified"])
            self.assertIn("intended UTC minute=:10", (output / "results.md").read_text())
            for line in (output / "SHA256SUMS").read_text().splitlines():
                digest, filename = line.split("  ", 1)
                self.assertEqual(hashlib.sha256((output / filename).read_bytes()).hexdigest(), digest)

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
        self.assertEqual(payload["online_usd_pairs"], 632)
        self.assertEqual(payload["excluded_stablecoin_pairs"], 10)
        self.assertEqual(payload["stablecoin_exclusion_count"], 10)
        self.assertIn("stablecoin-base exclusions: 10", md)
        self.assertIn("counted from this scan's online AssetPairs metadata", md)


    def test_zero_qualifying_watch_is_successful_abstention(self):
        scan, score = fixture()
        scan["watch"] = []
        payload, markdown = self.report(scan, score)
        self.assertEqual(payload["status"], "ABSTAIN_NO_WATCH")
        self.assertEqual(payload["candidates"], [])
        self.assertTrue(payload["remote_readback_verified"])
        self.assertIn("No qualifying WATCH candidates", markdown)
        self.assertIn("ABSTAIN", markdown)
        self.assertNotIn("FAILED run", markdown)


    def test_zero_observations_disclose_unverified_freshness(self):
        scan, score = fixture()
        scan["watch"] = []
        scan["observations"] = []
        scan["observed_markets"] = 0
        scan["ohlc_screened"] = 0
        payload, markdown = self.report(scan, score)
        self.assertEqual(payload["candidates"], [])
        self.assertEqual(payload["status"], "ABSTAIN_NO_OBSERVATIONS")
        self.assertIn("ABSTAIN_NO_OBSERVATIONS", markdown)
        self.assertIn("NOT VERIFIED (zero observations)", markdown)
        self.assertIn("No qualifying WATCH candidates", markdown)


    def test_reject_inconsistent_market_evidence_before_reporting(self):
        for mode in ("screened_without_quotes", "watch_exceeds_screened"):
            with self.subTest(mode=mode):
                scan, score = fixture()
                if mode == "screened_without_quotes":
                    scan["observations"] = []
                    scan["observed_markets"] = 0
                    scan["watch"] = []
                    scan["ohlc_screened"] = 1
                    error = "No quote observations"
                else:
                    scan["ohlc_screened"] = 1
                    error = "WATCH count exceeds screened"
                with self.assertRaisesRegex(ValueError, error):
                    self.report(scan, score)

    def test_zero_observation_cli_artifact_and_checksums(self):
        import hashlib
        import json
        import tempfile
        from pathlib import Path
        from unittest.mock import patch
        from paper_pov.results_report import main
        scan, score = fixture()
        scan.update(observations=[], observed_markets=0, ohlc_screened=0, watch=[])
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source, board, output = root / "scan.json", root / "score.json", root / "results"
            source.write_text(json.dumps(scan))
            board.write_text(json.dumps(score))
            args = ["results", "--scan", str(source), "--scoreboard", str(board),
                    "--run-id", "41235442591", "--source-sha", SHA,
                    "--ledger-commit", LEDGER, "--event", "workflow_dispatch",
                    "--output-dir", str(output)]
            with patch("sys.argv", args):
                main()
            payload = json.loads((output / "results.json").read_text())
            self.assertEqual(payload["status"], "ABSTAIN_NO_OBSERVATIONS")
            self.assertIsNone(payload["max_client_quote_age_seconds"])
            self.assertEqual(payload["candidates"], [])
            self.assertFalse(payload["buy_approved"])
            for line in (output / "SHA256SUMS").read_text().splitlines():
                digest, name = line.split("  ", 1)
                self.assertEqual(hashlib.sha256((output / name).read_bytes()).hexdigest(), digest)


    def test_atomic_result_publication_rejects_existing_and_cleans_failed_stage(self):
        import json
        import tempfile
        from pathlib import Path
        from unittest.mock import patch
        from paper_pov.results_report import main
        scan, score = fixture()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source, board, output = root / "scan.json", root / "score.json", root / "results"
            source.write_text(json.dumps(scan))
            board.write_text(json.dumps(score))
            args = ["results", "--scan", str(source), "--scoreboard", str(board),
                    "--run-id", "41235442591", "--source-sha", SHA,
                    "--ledger-commit", LEDGER, "--event", "workflow_dispatch",
                    "--output-dir", str(output)]
            with patch("sys.argv", args):
                main()
            old = {p.name: p.read_bytes() for p in output.iterdir()}
            with patch("sys.argv", args), self.assertRaises(FileExistsError):
                main()
            self.assertEqual({p.name: p.read_bytes() for p in output.iterdir()}, old)
            self.assertFalse(list(root.glob(".paper-results-*")))
            fresh = root / "fresh"
            args[-1] = str(fresh)
            with patch("sys.argv", args), patch(
                "paper_pov.results_report.hashlib.sha256", side_effect=OSError("checksum failure")
            ), self.assertRaisesRegex(OSError, "checksum failure"):
                main()
            self.assertFalse(fresh.exists())
            self.assertFalse(list(root.glob(".paper-results-*")))


    def test_published_result_readback_rejects_tamper_and_wrong_ledger(self):
        import json
        import tempfile
        from pathlib import Path
        from unittest.mock import patch
        from paper_pov.results_report import main, verify_published
        scan, score = fixture()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source, board, output = root / "scan.json", root / "score.json", root / "results"
            source.write_text(json.dumps(scan))
            board.write_text(json.dumps(score))
            args = ["results", "--scan", str(source), "--scoreboard", str(board),
                    "--run-id", "41235442591", "--source-sha", SHA,
                    "--ledger-commit", LEDGER, "--event", "workflow_dispatch",
                    "--output-dir", str(output)]
            with patch("sys.argv", args):
                main()
            expected = dict(run_id="41235442591", source_sha=SHA,
                            ledger_commit=LEDGER, ledger_sha256=score["ledger_sha256"])
            self.assertEqual(verify_published(output, **expected)["status"], "SUCCESS_PAPER_ONLY")
            verify_args = ["results", "--verify-only", "--run-id", expected["run_id"],
                           "--source-sha", SHA, "--ledger-commit", LEDGER,
                           "--ledger-sha256", score["ledger_sha256"],
                           "--output-dir", str(output)]
            with patch("sys.argv", verify_args):
                main()
            for field, bad in (("run_id", "1"), ("ledger_commit", SHA),
                               ("ledger_sha256", "0" * 64)):
                wrong = dict(expected)
                wrong[field] = bad
                with self.subTest(field=field), self.assertRaisesRegex(ValueError, "identity"):
                    verify_published(output, **wrong)
            original = (output / "results.md").read_bytes()
            (output / "results.md").write_bytes(original + b"tampered")
            with self.assertRaisesRegex(ValueError, "checksum mismatch"):
                verify_published(output, **expected)
            (output / "results.md").write_bytes(original)
            (output / "unexpected.txt").write_text("extra")
            with self.assertRaisesRegex(ValueError, "unexpected result"):
                verify_published(output, **expected)

    def test_independent_quote_freshness_and_candidate_provenance_readback(self):
        import json
        import hashlib
        import tempfile
        from pathlib import Path
        from unittest.mock import patch
        from paper_pov.results_report import main, verify_published
        scan, score = fixture()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source, board, output = root / "scan.json", root / "score.json", root / "results"
            source.write_text(json.dumps(scan))
            board.write_text(json.dumps(score))
            args = ["results", "--scan", str(source), "--scoreboard", str(board),
                    "--run-id", "41235442591", "--source-sha", SHA,
                    "--ledger-commit", LEDGER, "--event", "workflow_dispatch",
                    "--output-dir", str(output)]
            with patch("sys.argv", args):
                main()
            expected = dict(run_id="41235442591", source_sha=SHA,
                            ledger_commit=LEDGER, ledger_sha256=score["ledger_sha256"])
            original = json.loads((output / "results.json").read_text())
            self.assertEqual(len(verify_published(output, **expected)["quote_evidence"]), 2)
            for mode in ("stale", "future", "wrong_max", "wrong_price", "missing", "duplicate"):
                with self.subTest(mode=mode):
                    payload = json.loads(json.dumps(original))
                    if mode == "stale":
                        payload["quote_evidence"][0]["observed_at"] = "2026-10-31T20:00:00+00:00"
                    elif mode == "future":
                        payload["quote_evidence"][0]["observed_at"] = "2026-10-31T21:00:00+00:00"
                    elif mode == "wrong_max":
                        payload["max_client_quote_age_seconds"] = 0
                    elif mode == "wrong_price":
                        payload["quote_evidence"][0]["price"] += 1
                    elif mode == "missing":
                        payload["quote_evidence"].pop()
                    else:
                        payload["quote_evidence"][1]["pair"] = payload["quote_evidence"][0]["pair"]
                    raw = json.dumps(payload).encode()
                    (output / "results.json").write_bytes(raw)
                    md = (output / "results.md").read_bytes()
                    (output / "SHA256SUMS").write_text(
                        hashlib.sha256(raw).hexdigest() + "  results.json\\n" +
                        hashlib.sha256(md).hexdigest() + "  results.md\\n")
                    with self.assertRaises(ValueError):
                        verify_published(output, **expected)

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

    def test_reject_missing_or_fabricated_exclusion_partition(self):
        for field, bad in (("online_usd_pairs", 631),
                           ("excluded_stablecoin_pairs", 11),
                           ("excluded_other_pairs", -1),
                           ("excluded_stablecoin_pairs", True),
                           ("online_usd_pairs", None)):
            s, b = fixture()
            s[field] = bad
            with self.subTest(field=field, bad=bad), self.assertRaises(ValueError):
                self.report(s, b)
        s, b = fixture()
        del s["excluded_stablecoin_pairs"]
        with self.assertRaises(ValueError):
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
