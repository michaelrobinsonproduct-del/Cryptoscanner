"""Adversarial, offline OHLC hindsight-candidate tests."""
import csv
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

from research.kraken_archive_readiness import ARCHIVE_SHA
from research.retained_first_entry_candidates import _forward_max, inspect_candidates


class CandidateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "retained.zip"

    def make(self, n=30, *, high_at=None, gap_at=None, corrupt=False):
        rows = []
        for i in range(n):
            ts = 1700000100 + 300 * (i + (10 if gap_at is not None and i >= gap_at else 0))
            high = "1.31" if i == high_at else "1.1"
            rows.append([ts, "1", high, "0.9", "1", "20", "2"])
        stream = io.StringIO()
        csv.writer(stream, lineterminator="\n").writerows(rows)
        data = stream.getvalue().encode()
        meta = {"retained_sha256": hashlib.sha256(data).hexdigest(),
                "retained_rows": n, "retained_first_open": rows[0][0],
                "retained_last_open": rows[-1][0]}
        manifest = {"schema": 1, "source_archive_sha256": ARCHIVE_SHA,
                    "real_labels": 0, "independent_trade_completeness": False,
                    "source_timestamp_semantics": "candle_open_candidate",
                    "held_out_evaluation": "not_authorized",
                    "markets": {"XBTUSD_5.csv": meta}}
        with zipfile.ZipFile(self.path, "w") as z:
            z.writestr("candles/XBTUSD_5.csv", data + (b"X" if corrupt else b""))
            z.writestr("manifest.json", json.dumps(manifest))
        return self.path

    def test_forward_high_excludes_entry_and_requires_full_horizon(self):
        self.assertEqual(_forward_max([10, 30, 20, 5], 2), [30, 20, None, None])

    def test_future_high_counts_only_completed_windows(self):
        r = inspect_candidates(self.make(high_at=13))["horizons"]["1"]
        self.assertEqual(r["contiguous_entry_windows"], 18)
        self.assertEqual(r["hindsight_high_ge30pct_windows"], 12)
        self.assertEqual(r["nonoverlap_cohort_entries"], 1)
        self.assertEqual(r["cohort_hindsight_ge30pct"], 1)

    def test_high_at_entry_does_not_count_as_future_hit(self):
        r = inspect_candidates(self.make(high_at=0))["horizons"]["1"]
        self.assertEqual(r["hindsight_high_ge30pct_windows"], 0)

    def test_discontinuity_abstains_cross_gap(self):
        r = inspect_candidates(self.make(gap_at=15))["horizons"]["1"]
        self.assertEqual(r["contiguous_entry_windows"], 6)
        self.assertEqual(r["nonoverlap_cohort_entries"], 0)

    def test_no_historical_promotion_or_fake_episode_labels(self):
        r = inspect_candidates(self.make())
        self.assertEqual(r["authenticated_first_entry_episodes"], 0)
        self.assertIsNone(r["held_out_lift"])
        self.assertFalse(r["production_applied"])
        self.assertFalse(r["first_observed_at_available"])

    def test_phase_sensitivity_exposes_fixed_stride_selection(self):
        p = inspect_candidates(self.make(high_at=13))["horizons"]["1"]["phase_sensitivity"]
        self.assertEqual(p["offsets_tested"], 12)
        self.assertEqual(p["offsets_with_entries"], 6)
        self.assertEqual(p["offsets_with_ge30pct"], 1)
        self.assertEqual((p["min_ge30pct_per_offset"], p["max_ge30pct_per_offset"]), (0, 1))
        self.assertEqual((p["min_entries_per_offset"], p["max_entries_per_offset"]), (0, 1))

    def test_phase_sensitivity_no_false_hit_from_entry_candle(self):
        r = inspect_candidates(self.make(high_at=0))["horizons"]["1"]
        self.assertEqual(r["phase_sensitivity"]["offsets_with_ge30pct"], 0)
        self.assertEqual(r["phase_sensitivity"]["max_ge30pct_per_offset"], 0)

    def test_phase_sensitivity_never_crosses_missing_candle(self):
        r = inspect_candidates(self.make(gap_at=15))["horizons"]["1"]
        self.assertEqual(r["phase_sensitivity"]["offsets_with_entries"], 0)
        self.assertEqual(r["phase_sensitivity"]["max_entries_per_offset"], 0)

    def test_reject_retained_hash_tamper(self):
        with self.assertRaisesRegex(ValueError, "SHA256 mismatch"):
            inspect_candidates(self.make(corrupt=True))

    def test_nonoverlap_cohort_partition(self):
        r = inspect_candidates(self.make(high_at=13))["horizons"]["1"]
        self.assertEqual(r["cohort_hindsight_ge30pct"] + r["cohort_hindsight_lt30pct"],
                         r["nonoverlap_cohort_entries"])


if __name__ == "__main__":
    unittest.main()
