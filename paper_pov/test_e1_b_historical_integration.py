"""Exercise actual E1 pinned trade files through E's handoff and B's consumer.

CI supplies E1 and B source from their existing owner branches at runtime.
No production writer, network market data, or qualified learning decisions.
"""
import datetime as dt
import hashlib
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

from .historical_execution_learning_bridge import project_historical_execution


class RealHistoricalE1ToBTests(unittest.TestCase):
    def test_pinned_csv_to_four_horizons_to_b_read_only(self):
        from .historical_outcome_execution import run_historical_outcomes
        # B's module imports its transport at import time; the projection below
        # only needs _learning_evidence, not any transport or external services.
        with patch.dict(sys.modules, {
            "paper_pov.github_sealed_bundle_readback":
                types.ModuleType("paper_pov.github_sealed_bundle_readback")
        }):
            from .github_delivery_projection import _learning_evidence

        start = dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = b"".join(
                f"{int((start + dt.timedelta(minutes=5*i)).timestamp())},{100+i*0.01:.2f},1\n".encode()
                for i in range(578))
            (root / "XUSD.csv").write_bytes(raw)
            manifest = {"schema": "kraken_archive_manifest_v1", "source": "Kraken",
                        "partitions": [{"file": "XUSD.csv", "size_bytes": len(raw),
                                        "sha256": hashlib.sha256(raw).hexdigest()}]}
            schema = {"format": "kraken_trade_csv_explicit_v1",
                      "timestamp_unit": "seconds",
                      "columns": {"timestamp": 0, "price": 1, "volume": 2},
                      "header": False, "column_count": 3}
            predictions = [
                {"prediction_id": "p1", "pair": "XUSD", "status": "PAPER_WATCH",
                 "as_of": start.isoformat()},
                {"prediction_id": "p2", "pair": "YUSD", "status": "PAPER_WATCH",
                 "as_of": start.isoformat()}]
            result = run_historical_outcomes(
                manifest, root, schema, {"XUSD": "XUSD.csv"}, predictions,
                (start + dt.timedelta(hours=49)).isoformat())
            handoff = project_historical_execution(result, frozen_predictions=predictions)
            projected = _learning_evidence(handoff)
            self.assertEqual(result["status_counts"]["48h:MATURED_OBSERVED"], 1)
            self.assertEqual(result["status_counts"]["48h:ABSTAIN_ENTRY"], 1)
            self.assertEqual(handoff["diagnostic_horizon_status_counts"]["48"]["ABSTAIN_ENTRY"], 1)
            self.assertEqual(projected["observed_prediction_count"], 2)
            self.assertEqual(projected["complete_cohort_count"], 0)
            self.assertEqual(projected["excluded_prediction_count"], 2)
            self.assertEqual(projected["status"], "NO_QUALIFIED_RULE")
            self.assertFalse(projected["promotion_authorized"])
            # Mutation of pinned bytes must fail BEFORE E can hand anything to B.
            (root / "XUSD.csv").write_bytes(raw.replace(b"100.00", b"101.00", 1))
            with self.assertRaisesRegex(ValueError, "checksum"):
                run_historical_outcomes(
                    manifest, root, schema, {"XUSD": "XUSD.csv"}, predictions,
                    (start + dt.timedelta(hours=49)).isoformat())


if __name__ == "__main__":
    unittest.main()
