"""Cross-component acceptance checks; offline, deterministic, research only."""
import datetime as dt
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner import dex_guard, history

class AcceptanceTests(unittest.TestCase):
    def test_dex_outage_does_not_raise_or_destroy_history(self):
        with tempfile.TemporaryDirectory() as directory:
            ledger=Path(directory)/"history.sqlite3"
            ledger.write_bytes(b"preserve-me")
            with patch.dict(os.environ,{"SIMPLE_SCANNER_DATA_DIR":directory}),patch.object(dex_guard.dex,"main",side_effect=RuntimeError("HTTP 429")):
                dex_guard.run()
            self.assertEqual(ledger.read_bytes(),b"preserve-me")
            self.assertTrue((Path(directory)/"dex_circuit.json").exists())
    def test_circuit_persists_across_independent_calls(self):
        with tempfile.TemporaryDirectory() as directory:
            state=Path(directory)/"dex_circuit.json"
            state.write_text(json.dumps({"blocked_at":dt.datetime.now(dt.timezone.utc).isoformat(),"error":"HTTP 429"}))
            with patch.dict(os.environ,{"SIMPLE_SCANNER_DATA_DIR":directory}),patch.object(dex_guard.dex,"main",side_effect=AssertionError("must skip")):
                dex_guard.run()
                dex_guard.run()
            self.assertTrue(state.exists())
    def test_forward_horizon_configuration(self):
        self.assertEqual(history.HORIZONS,(1,3,6,24))
