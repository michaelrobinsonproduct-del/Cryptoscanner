"""Adversarial unit tests for read-only PAPER liquidity replay."""
import datetime as dt
import hashlib
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

import paper_asof_liquidity_audit as audit


class LiquidityReplayTests(unittest.TestCase):
    def test_verifies_original_bytes(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "fixture.zip"
            payload = b'{"as_of":"2026-11-01T00:00:00Z"}'
            with zipfile.ZipFile(p, "w") as z:
                z.writestr("latest.json", payload)
                z.writestr("SHA256SUMS", hashlib.sha256(payload).hexdigest() + "  latest.json\n")
            self.assertEqual(audit.verified_zip(p)["latest.json"], payload)

    def test_rejects_self_inconsistent_payload(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "tampered.zip"
            with zipfile.ZipFile(p, "w") as z:
                z.writestr("latest.json", b"tampered")
                z.writestr("SHA256SUMS", hashlib.sha256(b"original").hexdigest() + "  latest.json\n")
            with self.assertRaisesRegex(ValueError, "SHA mismatch"):
                audit.verified_zip(p)

    def test_lag_never_uses_future(self):
        utc = dt.timezone.utc
        times = [dt.datetime(2026, 11, 1, 0, 0, tzinfo=utc) +
                 dt.timedelta(minutes=30 * i) for i in range(5)]
        prices = [{"A": p} for p in (10, 11, 12, 13, 14)]
        self.assertEqual(audit.lag(times, prices, 2, "A", 60, 5), 10)
        self.assertIsNone(audit.lag(times, prices, 1, "A", 60, 5))
        self.assertEqual(audit.lag(times, prices, 4, "A", 60, 5), 12)


    def test_highest_ranked_future_gap_is_not_dropped_before_top_k(self):
        keys = ("momentum_1h", "volatility_3h", "volatility_direction",
                "liquidity_adjusted_volatility")
        scores = {(1, pair): {key: score for key in keys}
                  for pair, score in (("GAP", 99), ("HIT", 80), ("NEG", 10))}
        labels = {(1, "HIT"): 35.0, (1, "NEG"): 0.0}
        watch = {1: {"HIT", "NEG"}}
        result = audit.evaluate_rankings(scores, [1], watch, labels, top_k=2)
        for name in keys:
            row = result[name]
            self.assertEqual(row["selected_pairs_by_time"]["1"], ["GAP", "HIT"])
            self.assertEqual(row["picks"], 2)
            self.assertEqual(row["labeled_picks"], 1)
            self.assertEqual(row["missing_forward_label_picks"], 1)
            self.assertEqual(row["positive_windows"]["30"], 1)
            self.assertEqual(row["missing_label_examples"], [{"index": 1, "pair": "GAP"}])
        self.assertEqual(result["actual_paper_watch"]["missing_forward_label_picks"], 0)

        # Changing ONLY future labels may change measured hits, never selection.
        labels[(1, "GAP")] = 100.0
        after = audit.evaluate_rankings(scores, [1], watch, labels, top_k=2)
        for name in keys:
            self.assertEqual(after[name]["selected_pairs_by_time"],
                             result[name]["selected_pairs_by_time"])
            self.assertEqual(after[name]["positive_windows"]["30"], 2)

    def test_all_missing_future_labels_are_explicit_abstentions(self):
        keys = ("momentum_1h", "volatility_3h", "volatility_direction",
                "liquidity_adjusted_volatility")
        scores = {(3, pair): {key: score for key in keys}
                  for pair, score in (("A", 3), ("B", 2))}
        row = audit.evaluate_rankings(scores, [3], {3: set()}, {}, top_k=2)
        for name in keys:
            self.assertEqual(row[name]["picks"], 2)
            self.assertEqual(row[name]["labeled_picks"], 0)
            self.assertEqual(row[name]["missing_forward_label_picks"], 2)
            self.assertIsNone(row[name]["sampled_precision_on_labeled_30"])

    def test_missing_source_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(FileNotFoundError):
                audit.analyze(Path(d))


if __name__ == "__main__":
    unittest.main()
