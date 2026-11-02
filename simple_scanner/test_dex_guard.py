"""Verify DEX provider outage is isolated and repeated requests suppressed."""
import datetime as dt
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner import dex_guard

class DexGuardTests(unittest.TestCase):
    def test_failure_trips_circuit_and_skips_next_call(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.dict(os.environ,{"SIMPLE_SCANNER_DATA_DIR":directory}),patch.object(dex_guard.dex,"main",side_effect=RuntimeError("rate limited")) as fetch:
                dex_guard.run()
                dex_guard.run()
                self.assertEqual(fetch.call_count,1)
                self.assertTrue((Path(directory)/"dex_circuit.json").exists())
    def test_expired_circuit_allows_recovery(self):
        with tempfile.TemporaryDirectory() as directory:
            state=Path(directory)/"dex_circuit.json"
            state.write_text(json.dumps({"blocked_at":(dt.datetime.now(dt.timezone.utc)-dt.timedelta(hours=4)).isoformat(),"error":"old"}))
            with patch.dict(os.environ,{"SIMPLE_SCANNER_DATA_DIR":directory}),patch.object(dex_guard.dex,"main") as fetch:
                dex_guard.run()
                fetch.assert_called_once()
                self.assertFalse(state.exists())
