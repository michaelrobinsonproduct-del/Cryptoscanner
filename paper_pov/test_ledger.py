"""Paper-ledger regression tests use synthetic fixtures, never claimed as real outcomes."""
import copy
import datetime as dt
import hashlib
import json
import unittest
from paper_pov import ledger
from paper_pov.test_scanner import run, NOW

SHA = "a" * 40

def synthetic(offset_minutes, price=1.01):
    report = copy.deepcopy(run())
    when = (NOW + dt.timedelta(minutes=offset_minutes)).isoformat()
    report["as_of"] = when
    report["started_at"] = when
    for p in report["watch"]:
        p["as_of"] = when
        p["quote_observed_at"] = when
        p["prediction_id"] = hashlib.sha256(
            ("paper-v1|" + when + "|" + p["pair"]).encode()).hexdigest()
    for o in report["observations"]:
        o["observed_at"] = when
        o["price"] = price
    return report

class LedgerTests(unittest.TestCase):
    def test_initial_checksum_and_no_implicit_reset(self):
        state = ledger.empty()
        self.assertEqual(state["generation"], 0)
        ledger.verify(state)
        with self.assertRaises(FileNotFoundError):
            ledger.update_file("/nonexistent/paper-ledger.json", "unused", SHA, "unused")

    def test_append_is_immutable_and_idempotent_duplicate_rejected(self):
        before = ledger.empty()
        report = synthetic(0)
        after = ledger.advance(before, report, SHA)
        self.assertEqual(before["generation"], 0)
        self.assertEqual(after["generation"], 1)
        self.assertEqual(len(after["predictions"]), 12)
        self.assertEqual(len(after["observations"]), 25)
        self.assertEqual(len({p["prediction_id"] for p in after["predictions"]}), 12)
        with self.assertRaisesRegex(ValueError, "Out-of-order"):
            ledger.advance(after, report, SHA)

    def test_checksum_tampering_rejected(self):
        state = ledger.advance(ledger.empty(), synthetic(0), SHA)
        state["predictions"][0]["price"] = 999
        with self.assertRaisesRegex(ValueError, "checksum"):
            ledger.verify(state)

    def test_no_immature_forward_labels(self):
        state = ledger.advance(ledger.empty(), synthetic(0), SHA)
        state = ledger.advance(state, synthetic(30), SHA)
        self.assertEqual(ledger.scoreboard(state)["matured_labels"], 0)
        self.assertEqual(len(state["outcomes"]), 0)

    def test_matured_one_hour_requires_contiguous_observations(self):
        state = ledger.empty()
        for offset in (0, 30, 60, 90, 120):
            state = ledger.advance(state, synthetic(offset), SHA)
        score = ledger.scoreboard(state)
        self.assertEqual(score["actual_scans"], 5)
        self.assertEqual(score["matured_labels"], 12)
        self.assertEqual(score["gap_abstentions"], 0)
        self.assertEqual(score["observed_30pct_hits"], 0)
        self.assertIsNone(score["held_out_lift"])
        self.assertTrue(all(x["horizon_hours"] == 1 for x in state["outcomes"]))

    def test_gap_abstention_not_success(self):
        state = ledger.advance(ledger.empty(), synthetic(0), SHA)
        state = ledger.advance(state, synthetic(120), SHA)
        score = ledger.scoreboard(state)
        self.assertEqual(score["matured_labels"], 0)
        self.assertEqual(score["gap_abstentions"], 12)

    def test_unchanged_prediction_identity_across_maturation(self):
        state = ledger.advance(ledger.empty(), synthetic(0), SHA)
        first = copy.deepcopy(state["predictions"])
        for offset in (30, 60, 90, 120):
            state = ledger.advance(state, synthetic(offset), SHA)
        self.assertEqual(first, state["predictions"][:len(first)])

    def test_invalid_source_sha_rejected(self):
        with self.assertRaisesRegex(ValueError, "source commit"):
            ledger.advance(ledger.empty(), synthetic(0), "main")

    def test_nonmonotonic_or_duplicate_predictions_rejected(self):
        state = ledger.advance(ledger.empty(), synthetic(0), SHA)
        state["predictions"].append(copy.deepcopy(state["predictions"][0]))
        ledger.seal(state)
        with self.assertRaisesRegex(ValueError, "Duplicate immutable"):
            ledger.verify(state)

    def test_invalid_quote_timestamp_rejected(self):
        report = synthetic(0)
        report["watch"][0]["quote_observed_at"] = (NOW + dt.timedelta(minutes=1)).isoformat()
        with self.assertRaisesRegex(ValueError, "quote time"):
            ledger.advance(ledger.empty(), report, SHA)

    def test_maturity_safe_50h_compaction_and_monotonic_totals(self):
        state = ledger.advance(ledger.empty(), synthetic(0), SHA)
        state = ledger.advance(state, synthetic(51 * 60), SHA)
        score = ledger.scoreboard(state)
        self.assertEqual(score["generation"], 2)
        self.assertEqual(score["actual_scans"], 2)
        self.assertEqual(score["immutable_predictions"], 24)
        self.assertEqual(score["market_observations"], 50)
        self.assertEqual(score["gap_abstentions"], 48)
        self.assertEqual(len(state["runs"]), 1)
        self.assertEqual(len(state["predictions"]), 12)
        self.assertEqual(len(state["archive_index"]), 1)
        self.assertEqual(state["archived"]["scans"], 1)
        ledger.verify(state)

    def test_compacted_archive_tampering_fails_closed(self):
        state = ledger.advance(ledger.empty(), synthetic(0), SHA)
        state = ledger.advance(state, synthetic(51 * 60), SHA)
        state["archived"]["scans"] = 0
        ledger.seal(state)
        with self.assertRaisesRegex(ValueError, "generation/scan"):
            ledger.verify(state)

if __name__ == "__main__":
    unittest.main()
