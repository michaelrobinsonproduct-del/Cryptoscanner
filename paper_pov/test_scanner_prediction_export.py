import json
import tempfile
import unittest
from pathlib import Path
from .scanner_prediction_export import export_predictions

class ExportAcceptance(unittest.TestCase):
    def test_sealed_scored_watch_to_learning(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report = {"mode": "PAPER_ONLY", "production_applied": False,
                      "scan_status": "WATCH", "as_of": "2026-11-05T23:00:00+00:00",
                      "watch": [{"prediction_id": "p1", "rank": 1, "status": "PAPER_WATCH",
                                 "buy_approved": False, "as_of": "2026-11-05T23:00:00+00:00",
                                 "quote_timestamp_semantics": "client_observed_not_exchange_event_time",
                                 "ohlc_last_closed_at": "2026-11-05T22:55:00+00:00",
                                 "pair": "XBTUSD", "symbol": "XBT/USD", "price": 100,
                                 "baseline_score": 60, "challenger_score": 75,
                                 "move15_pct": 2, "volume_accel": 1.5,
                                 "spread_bps": 4, "notional_24h_usd": 500000}]}
            raw = json.dumps(report).encode()
            (root / "latest.json").write_bytes(raw)
            (root / "receipt.json").write_bytes(raw)
            result = export_predictions(root / "latest.json", root / "receipt.json")
            self.assertEqual(result["predictions"][0]["challenger_score"], 75)
            self.assertFalse(result["predictions"][0]["future_outcome_authenticated"])
            (root / "receipt.json").write_bytes(raw + b" ")
            with self.assertRaises(ValueError):
                export_predictions(root / "latest.json", root / "receipt.json")
if __name__ == "__main__":
    unittest.main()
