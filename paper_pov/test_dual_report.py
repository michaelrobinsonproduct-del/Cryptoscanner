"""Offline integration tests for independently sealed two-scanner report delivery."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from paper_pov.dual_report import combine, main, markdown

SHA = "a" * 40


def fixtures():
    paper = {
        "schema": 2, "publication_mode": "ATOMIC_LEDGER_RESULTS",
        "status": "SUCCESS_PAPER_ONLY", "remote_readback_verified": True,
        "production_applied": False, "buy_approved": False,
        "ledger_sha256": "b" * 64, "ledger_generation": 369,
        "run_id": "777", "source_sha": SHA,
        "as_of": "2026-11-13T23:13:27+00:00", "observed_markets": 607,
        "rankings": {
            "population": "SAME_OHLC_VERIFIED_WATCH_POOL",
            "challenger": [{"rank": 1, "symbol": "INJ/USD", "score": 91.0},
                           {"rank": 2, "symbol": "NEAR/USD", "score": 67.0}],
            "baseline": [{"rank": 1, "symbol": "NEAR/USD", "score": 80.0},
                         {"rank": 2, "symbol": "INJ/USD", "score": 74.0}],
        },
        "candidates": [
            {"rank": 1, "symbol": "INJ/USD", "price_usd": 8.01,
             "challenger_score": 91.0, "status": "WATCH_PAPER_ONLY",
             "quote_observed_at": "2026-11-13T23:13:24+00:00",
             "move15_pct": 0.6, "volume_accel": 4.0},
            {"rank": 2, "symbol": "NEAR/USD", "price_usd": 3.4,
             "challenger_score": 67.0, "status": "WATCH_PAPER_ONLY",
             "quote_observed_at": "2026-11-13T23:13:24+00:00",
             "move15_pct": -0.2, "volume_accel": 1.1},
        ],
    }
    shadow = {
        "schema": 1, "mode": "LEGACY_INSPIRED_SHADOW",
        "independent_execution": True, "source_sha": SHA,
        "run_id": "888", "trigger_paper_run_id": "777",
        "status": "WATCH_PAPER_ONLY", "production_applied": False,
        "buy_approved": False, "trade_executed": False, "held_out_lift": None,
        "as_of": "2026-11-13T23:14:02+00:00",
        "candidates": [
            {"rank": 1, "symbol": "PUMP/USD", "price_usd": 0.003,
             "legacy_score": 91.0, "move15_pct": 0.8, "volume_accel": 3.0,
             "trades_24h": 25000, "status": "WATCH_PAPER_ONLY",
             "quote_observed_at": "2026-11-13T23:14:00+00:00"},
            {"rank": 2, "symbol": "INJ/USD", "price_usd": 8.02,
             "legacy_score": 77.0, "move15_pct": 0.5, "volume_accel": 2.0,
             "trades_24h": 12000, "status": "WATCH_PAPER_ONLY",
             "quote_observed_at": "2026-11-13T23:14:00+00:00"},
        ],
    }
    return paper, shadow


def sealed(root, files, manifest):
    for name, content in files.items():
        (root / name).write_bytes(content)
    (root / manifest).write_text("".join(
        hashlib.sha256(content).hexdigest() + "  " + name + "\n"
        for name, content in files.items()))


class DualScannerReportTests(unittest.TestCase):
    def test_true_challenger_and_independent_legacy_lists_with_overlap_star(self):
        paper, legacy = fixtures()
        r = combine(paper, legacy)
        self.assertEqual(r["writer_run_id"], "777")
        self.assertEqual(r["legacy_run_id"], "888")
        self.assertEqual(r["overlap_symbols"], ["INJ/USD"])
        self.assertEqual([x["symbol"] for x in r["challenger_watch"]],
                         ["INJ/USD", "NEAR/USD"])
        self.assertEqual([x["symbol"] for x in r["legacy_watch"]],
                         ["PUMP/USD", "INJ/USD"])
        self.assertIn("INJ/USD ⭐", markdown(r))
        self.assertIn("PUMP/USD", markdown(r))
        self.assertFalse(r["production_applied"])
        self.assertEqual(r["read_only_learning"], "SEPARATE_WORKFLOW")

    def test_dual_lists_preserve_distinct_risk_and_advisory_action(self):
        paper, legacy = fixtures()
        result = combine(paper, legacy)
        self.assertIn("Confidence", markdown(result))
        self.assertIn("Risk", markdown(result))
        self.assertIn("Action", markdown(result))
        for key in ("challenger_watch", "legacy_watch"):
            self.assertTrue(result[key])
            for row in result[key]:
                g = row["guidance"]
                self.assertIsNone(g["gain_probability_pct"])
                self.assertEqual(g["target_gain_pct"], 30)
                self.assertEqual(g["horizon_hours"], 48)
                self.assertIn(g["risk"], ("HIGH", "VERY_HIGH", "EXTREME"))
                self.assertFalse(g["recommendation_is_trade_authorization"])
        self.assertTrue(result["challenger_watch"][0]["guidance"]
                        ["independent_legacy_overlap_verified"])
        self.assertTrue(result["legacy_watch"][1]["guidance"]
                        ["independent_legacy_overlap_verified"])
        self.assertFalse(result["legacy_watch"][0]["guidance"]
                         ["independent_legacy_overlap_verified"])
        self.assertFalse(result["production_applied"])

    def test_nonmatching_independent_run_or_source_never_gets_overlap(self):
        paper, legacy = fixtures()
        legacy["trigger_paper_run_id"] = "778"
        with self.assertRaisesRegex(ValueError, "independently linked"):
            combine(paper, legacy)
        legacy["trigger_paper_run_id"] = "777"
        legacy["source_sha"] = "c" * 40
        with self.assertRaisesRegex(ValueError, "independently linked"):
            combine(paper, legacy)

    def test_no_independent_signals_is_explicit_not_a_missing_scanner(self):
        paper, legacy = fixtures()
        legacy["status"] = "NO_SIGNALS"
        legacy["candidates"] = []
        r = combine(paper, legacy)
        self.assertEqual(r["legacy_watch"], [])
        self.assertEqual(r["overlap_symbols"], [])
        self.assertIn("No confirmed WATCH signals", markdown(r))

    def test_both_checksums_are_validated_and_combined_report_is_sealed(self):
        paper, legacy = fixtures()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            pd, ld, od = root / "paper", root / "legacy", root / "joined"
            pd.mkdir()
            ld.mkdir()
            sealed(pd, {
                "results.json": json.dumps(paper).encode(),
                "results.md": b"Paper canonical result",
            }, "SHA256SUMS")
            sealed(ld, {
                "legacy-shadow.json": json.dumps(legacy).encode(),
            }, "LEGACY_SHA256SUMS")
            args = ["dual-report", "--paper-dir", str(pd), "--legacy-dir", str(ld),
                    "--paper-run-id", "777", "--shadow-run-id", "888",
                    "--output-dir", str(od)]
            with patch("sys.argv", args):
                main()
            result = json.loads((od / "dual-scanner.json").read_text())
            self.assertEqual(result["overlap_symbols"], ["INJ/USD"])
            for line in (od / "DUAL_SHA256SUMS").read_text().splitlines():
                digest, name = line.split("  ", 1)
                self.assertEqual(hashlib.sha256((od / name).read_bytes()).hexdigest(),
                                 digest)
            (ld / "legacy-shadow.json").write_text("{}")
            with patch("sys.argv", args), self.assertRaisesRegex(ValueError, "checksum"):
                main()


if __name__ == "__main__":
    unittest.main()
