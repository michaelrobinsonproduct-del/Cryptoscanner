import copy
import datetime as dt
import unittest

from contracts import (ContractError, ZERO_HASH, record_hash, verify_artifact,
                       verify_continuity, verify_ledger, verify_outcome)

NOW = "2026-10-31T15:15:00Z"
SRC = "a" * 64


def prediction(**changes):
    row = dict(prediction_id="p1", pair="XBT/USD",
               as_of="2026-10-31T14:00:00Z",
               source_observed_at="2026-10-31T13:59:30Z",
               recorded_at="2026-10-31T14:00:01Z",
               source_sha256=SRC, status="PAPER_WATCH",
               entry_price=100.0, score=40.0, prev_hash=ZERO_HASH)
    row.update(changes)
    row["hash"] = record_hash(row)
    return row


def outcome(**changes):
    row = dict(prediction_id="p1", horizon_hours=1, status="EVALUATED",
               observed_at="2026-10-31T15:01:00Z",
               exit_price=110.0, return_pct=10.0, gap_count=0,
               quote_liquidity_usd=200000, spread_bps=10,
               source_proof=dict(source="Kraken", interval_complete=True,
                                 sha256=SRC, verification_run_id=123))
    row.update(changes)
    return row


class PaperContracts(unittest.TestCase):
    def test_valid_prediction_and_hash(self):
        self.assertEqual(verify_ledger([prediction()], now=NOW)["records"], 1)

    def test_source_future_rejected(self):
        with self.assertRaises(ContractError):
            verify_ledger([prediction(source_observed_at="2026-10-31T14:01:00Z")])

    def test_stale_source_rejected(self):
        with self.assertRaises(ContractError):
            verify_ledger([prediction(source_observed_at="2026-10-31T13:40:00Z")])

    def test_backdated_or_late_recording_rejected(self):
        with self.assertRaises(ContractError):
            verify_ledger([prediction(recorded_at="2026-10-31T14:10:00Z")])

    def test_stablecoin_rejected(self):
        with self.assertRaises(ContractError):
            verify_ledger([prediction(pair="USDT/USD")])

    def test_prediction_tampering_rejected(self):
        p = prediction()
        p["score"] = 99
        with self.assertRaises(ContractError):
            verify_ledger([p])

    def test_duplicate_identity_rejected(self):
        p = prediction()
        q = prediction(prev_hash=p["hash"])
        with self.assertRaises(ContractError):
            verify_ledger([p, q])

    def test_abstention_carries_no_paper_signal(self):
        p = prediction(status="ABSTAIN", entry_price=None, score=None,
                       reason="insufficient liquidity")
        self.assertEqual(verify_ledger([p])["records"], 1)
        with self.assertRaises(ContractError):
            verify_ledger([prediction(status="ABSTAIN", reason="gap")])

    def test_missing_history_never_resets(self):
        with self.assertRaises(ContractError):
            verify_continuity(None, [prediction()])
        with self.assertRaises(ContractError):
            verify_continuity([], [prediction()])
        self.assertEqual(verify_continuity([], [prediction()],
                                           genesis_authorized=True), 1)

    def test_history_mutation_and_shrink_rejected(self):
        p = prediction()
        q = prediction(prediction_id="p2", as_of="2026-10-31T14:01:00Z",
                       recorded_at="2026-10-31T14:01:01Z",
                       source_observed_at="2026-10-31T14:00:30Z",
                       prev_hash=p["hash"])
        self.assertEqual(verify_continuity([p], [p, q]), 1)
        with self.assertRaises(ContractError):
            verify_continuity([p, q], [p])
        modified = copy.deepcopy(p)
        modified["score"] = 44
        modified["hash"] = record_hash(modified)
        with self.assertRaises(ContractError):
            verify_continuity([p], [modified])

    def test_immature_48_hour_rejected(self):
        with self.assertRaises(ContractError):
            verify_outcome(prediction(), outcome(horizon_hours=48),
                           now=NOW)

    def test_missing_source_completeness_rejected(self):
        with self.assertRaises(ContractError):
            verify_outcome(prediction(), outcome(source_proof={}), now=NOW)

    def test_gap_and_illiquidity_rejected(self):
        for changed in (dict(gap_count=1), dict(quote_liquidity_usd=0),
                        dict(spread_bps=90)):
            with self.subTest(changed=changed), self.assertRaises(ContractError):
                verify_outcome(prediction(), outcome(**changed), now=NOW)

    def test_no_future_or_late_outcome(self):
        for changed in (dict(observed_at="2026-10-31T15:20:00Z"),
                        dict(observed_at="2026-10-31T14:59:00Z")):
            with self.subTest(changed=changed), self.assertRaises(ContractError):
                verify_outcome(prediction(), outcome(**changed), now=NOW)

    def test_real_return_arithmetic_and_abstain(self):
        self.assertEqual(verify_outcome(prediction(), outcome(), now=NOW),
                         "EVALUATED")
        with self.assertRaises(ContractError):
            verify_outcome(prediction(), outcome(return_pct=30), now=NOW)
        self.assertEqual(verify_outcome(prediction(),
                         outcome(status="ABSTAIN", reason="missing candles",
                                 return_pct=None), now=NOW), "ABSTAIN")

    def test_checksum_verification(self):
        import hashlib
        raw = b"immutable artifact"
        self.assertTrue(verify_artifact(raw, hashlib.sha256(raw).hexdigest()))
        with self.assertRaises(ContractError):
            verify_artifact(raw + b"x", hashlib.sha256(raw).hexdigest())


if __name__ == "__main__":
    unittest.main()
