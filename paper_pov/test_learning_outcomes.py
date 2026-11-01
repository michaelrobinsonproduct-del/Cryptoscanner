"""Synthetic adversarial tests only; no claimed real market outcomes."""
import copy
import datetime as dt
import hashlib
import unittest

from paper_pov import ledger
from paper_pov.learning_outcomes import (
    sampled_outcomes, coverage_summary, shadow_rank_diagnostic)

UTC = dt.timezone.utc
START = dt.datetime(2026, 10, 20, tzinfo=UTC)


def fixture(offsets, prices=None, watch=("AAAUSD",)):
    """Three observed markets, 1+ WATCH, immutable identities and valid seal."""
    prices = prices or {}
    state = ledger.empty()
    for minutes in offsets:
        at = (START + dt.timedelta(minutes=minutes)).isoformat()
        rid = hashlib.sha256(("run|" + at).encode()).hexdigest()
        state["runs"].append({"id": rid, "as_of": at,
            "source_sha": "a" * 40, "report_sha256": "b" * 64,
            "watch_count": len(watch), "observation_count": 3})
        for pair in ("AAAUSD", "BBBUSD", "CCCUSD"):
            state["observations"].append({"run_id": rid, "pair": pair,
                "at": at, "price": prices.get((minutes, pair), 1.0)})
        for rank, pair in enumerate(watch, 1):
            state["predictions"].append({"run_id": rid, "pair": pair,
                "as_of": at, "price": prices.get((minutes, pair), 1.0),
                "prediction_id": hashlib.sha256(("paper-v1|" + at + "|" + pair).encode()).hexdigest(),
                "baseline_score": 10 + rank, "challenger_score": 30 - rank,
                "rank": rank})
    state["generation"] = len(state["runs"])
    ledger.seal(state)
    ledger.verify(state)
    return state


def select(rows, pair="BBBUSD", offset=0, horizon=1):
    return next(r for r in rows if r["pair"] == pair and
        r["as_of"] == (START + dt.timedelta(minutes=offset)).isoformat()
        and r["horizon_hours"] == horizon)


class PointInTimeOutcomeTests(unittest.TestCase):
    def test_matured_nonwatch_missed_20_and_30_and_watch_hit(self):
        prices = {(30, "BBBUSD"): 1.25, (60, "BBBUSD"): 1.35,
                  (60, "AAAUSD"): 1.30}
        state = fixture([0, 30, 60, 90, 120], prices)
        rows = sampled_outcomes(state, START + dt.timedelta(minutes=120), (1,))
        missed = select(rows)
        self.assertEqual(missed["status"], "MATURED_OBSERVED")
        self.assertEqual(missed["observed_peak_pct"], 35)
        self.assertTrue(missed["observed_20pct_hit"])
        self.assertTrue(missed["observed_30pct_hit"])
        self.assertFalse(missed["watch"])
        watch = select(rows, "AAAUSD")
        self.assertTrue(watch["watch"])
        self.assertTrue(watch["observed_30pct_hit"])
        summary = coverage_summary(rows)["by_horizon"]["1"]
        self.assertGreaterEqual(summary["nonwatch_missed_20pct"], 1)
        self.assertGreaterEqual(summary["nonwatch_missed_30pct"], 1)
        self.assertGreaterEqual(summary["watch_30pct_hits"], 1)

    def test_immature_target_plus_45m_not_assumed_complete(self):
        state = fixture([0, 30, 60, 90])
        r = select(sampled_outcomes(state, START + dt.timedelta(minutes=90), (1,)))
        self.assertEqual(r["status"], "IMMATURE")
        self.assertNotIn("observed_peak_pct", r)
        r = select(sampled_outcomes(state, START + dt.timedelta(minutes=105), (1,)))
        self.assertEqual(r["status"], "MATURED_OBSERVED")

    def test_future_peak_after_target_must_not_leak_into_one_hour(self):
        state = fixture([0, 30, 60, 90, 120], {(90, "BBBUSD"): 2.0})
        r = select(sampled_outcomes(state, START + dt.timedelta(minutes=120), (1,)))
        self.assertEqual(r["observed_peak_pct"], 0)
        self.assertFalse(r["observed_30pct_hit"])

    def test_peak_includes_entry_when_every_followup_declines(self):
        # Entry at 1.0 is itself a client-observed price at the start.
        # A decline cannot produce a negative maximum return over [start,target].
        prices = {(30, "BBBUSD"): 0.8, (60, "BBBUSD"): 0.7,
                  (90, "BBBUSD"): 0.6, (120, "BBBUSD"): 0.5}
        state = fixture([0, 30, 60, 90, 120], prices)
        rows = sampled_outcomes(state, START + dt.timedelta(minutes=120), (1,))
        result = select(rows)
        self.assertEqual(result["status"], "MATURED_OBSERVED")
        self.assertEqual(result["observed_peak_pct"], 0)
        self.assertAlmostEqual(result["observed_terminal_pct"], -30)
        self.assertFalse(result["observed_20pct_hit"])
        self.assertFalse(result["observed_30pct_hit"])

    def test_gap_is_abstention_not_miss(self):
        state = fixture([0, 120])
        r = select(sampled_outcomes(state, START + dt.timedelta(minutes=120), (1,)))
        self.assertEqual(r["status"], "ABSTAIN_GAP")
        summary = coverage_summary(sampled_outcomes(state, START + dt.timedelta(minutes=120), (1,)))["by_horizon"]["1"]
        self.assertEqual(summary["gap_abstentions"], 3)
        self.assertEqual(summary["sampled_20pct_windows"], 0)

    def test_missing_target_anchor_abstains(self):
        state = fixture([0, 30, 120])
        r = select(sampled_outcomes(state, START + dt.timedelta(minutes=120), (1,)))
        self.assertEqual(r["status"], "ABSTAIN_GAP")

    def test_no_future_lookahead_after_evaluation_time(self):
        state = fixture([0, 30, 60, 90, 120], {(120, "BBBUSD"): 1.8})
        rows = sampled_outcomes(state, START + dt.timedelta(minutes=105), (1,))
        self.assertEqual(select(rows)["observed_peak_pct"], 0)

    def test_four_horizons_have_independent_maturity(self):
        state = fixture(range(0, 3001, 30))
        rows = sampled_outcomes(state, START + dt.timedelta(minutes=3000))
        for horizon in (1, 6, 24, 48):
            self.assertEqual(select(rows, horizon=horizon)["status"], "MATURED_OBSERVED")
        earlier = sampled_outcomes(state, START + dt.timedelta(hours=24))
        self.assertEqual(select(earlier, horizon=48)["status"], "IMMATURE")
        self.assertEqual(select(earlier, horizon=24)["status"], "IMMATURE")

    def test_sealed_corruption_rejected_and_original_not_mutated(self):
        state = fixture([0, 30, 60, 90, 120])
        original = copy.deepcopy(state)
        sampled_outcomes(state, START + dt.timedelta(minutes=120))
        self.assertEqual(state, original)
        state["observations"][0]["price"] = -1
        ledger.seal(state)
        with self.assertRaises(ValueError):
            sampled_outcomes(state, START + dt.timedelta(minutes=120))

    def test_tampered_checksum_and_orphan_rejected(self):
        state = fixture([0, 30, 60, 90, 120])
        state["observations"][0]["price"] = 3
        with self.assertRaisesRegex(ValueError, "checksum"):
            sampled_outcomes(state, START + dt.timedelta(minutes=120))
        state = fixture([0, 30, 60, 90, 120])
        state["observations"][0]["run_id"] = "f" * 64
        ledger.seal(state)
        with self.assertRaisesRegex(ValueError, "Orphan"):
            sampled_outcomes(state, START + dt.timedelta(minutes=120))

    def test_naive_timestamp_and_unsupported_horizon_rejected(self):
        state = fixture([0, 30])
        with self.assertRaisesRegex(ValueError, "timezone-aware"):
            sampled_outcomes(state, dt.datetime(2026, 10, 20))
        with self.assertRaisesRegex(ValueError, "horizons"):
            sampled_outcomes(state, START, (1, 1))
        with self.assertRaisesRegex(ValueError, "horizons"):
            sampled_outcomes(state, START, (2,))

    def test_nonwatch_never_receives_fabricated_as_of_score(self):
        state = fixture([0, 30, 60, 90, 120])
        missed = select(sampled_outcomes(state, START + dt.timedelta(minutes=120), (1,)))
        self.assertIsNone(missed["baseline_score"])
        self.assertIsNone(missed["challenger_score"])

    def test_shadow_diagnostic_fails_closed_for_short_history(self):
        state = fixture(range(0, 3001, 30), watch=("AAAUSD", "CCCUSD"))
        rows = sampled_outcomes(state, START + dt.timedelta(minutes=3000), (1,))
        diag = shadow_rank_diagnostic(rows, START, top_k=1)
        self.assertEqual(diag["status"], "INSUFFICIENT_INDEPENDENT_TEST_RUNS")
        self.assertIsNone(diag["held_out_lift"])
        self.assertTrue(diag["sampled_quote_only"])

    def test_shadow_cohort_requires_all_watch_mature_and_purge(self):
        state = fixture(range(0, 3001, 30), watch=("AAAUSD", "CCCUSD"))
        rows = sampled_outcomes(state, START + dt.timedelta(minutes=3000), (1,))
        diag = shadow_rank_diagnostic(rows, START, min_test_runs=2)
        self.assertEqual(diag["nonoverlapping_test_runs"], 1)
        self.assertIsNone(diag["held_out_lift"])
        with self.assertRaisesRegex(ValueError, "parameters"):
            shadow_rank_diagnostic(rows, START, embargo_hours=1)

    def test_summary_is_explicit_about_sampled_quotes_and_no_promotion(self):
        state = fixture([0, 30, 60, 90, 120])
        result = coverage_summary(sampled_outcomes(state, START + dt.timedelta(minutes=120)))
        self.assertTrue(result["correlated_overlapping_windows"])
        self.assertIsNone(result["held_out_lift"])
        self.assertFalse(result["production_applied"])
        self.assertEqual(result["by_horizon"]["48"]["immature"], 15)


if __name__ == "__main__":
    unittest.main()


class OfflineCLIContractTests(unittest.TestCase):
    def test_cli_emits_deterministic_sealed_evidence_without_writing_ledger(self):
        import contextlib
        import io
        import json
        from pathlib import Path
        import tempfile
        from paper_pov.learning_outcomes import main
        state = fixture([0, 30, 60, 90, 120], {(60, "BBBUSD"): 1.25})
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "sealed.json"
            raw = ledger.canonical(state)
            path.write_bytes(raw)
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                report = main(["--ledger", str(path)])
            self.assertEqual(path.read_bytes(), raw)
            self.assertEqual(json.loads(out.getvalue()), report)
            self.assertEqual(report["source_ledger_sha256"], state["sha256"])
            self.assertEqual(report["evaluation_as_of"], state["runs"][-1]["as_of"])
            self.assertEqual(report["coverage"]["by_horizon"]["1"]["nonwatch_missed_20pct"], 1)
            self.assertIsNone(report["held_out_lift"])
            self.assertFalse(report["production_applied"])

    def test_cli_refuses_resealed_or_tampered_evidence(self):
        import contextlib
        import io
        from pathlib import Path
        import tempfile
        from paper_pov.learning_outcomes import main
        state = fixture([0, 30, 60, 90, 120])
        state["observations"][0]["price"] = 99
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "tampered.json"
            path.write_bytes(ledger.canonical(state))
            with contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaisesRegex(ValueError, "checksum"):
                    main(["--ledger", str(path)])
