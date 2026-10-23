import datetime as dt
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch
from simple_scanner import dex, dex_guard

UTC = dt.timezone.utc

class DexReliabilityTests(unittest.TestCase):
    def test_freshness_boundaries(self):
        now = dt.datetime(2026, 10, 22, tzinfo=UTC)
        for minutes, valid in [(0, True), (60, True), (61, True), (62, False), (-1, False)]:
            with self.subTest(minutes=minutes):
                observed = (now - dt.timedelta(minutes=minutes)).isoformat()
                self.assertEqual(dex.cache_is_fresh(observed, now), valid)
        self.assertFalse(dex.cache_is_fresh('2026-10-22T00:00:00', now))
        self.assertFalse(dex.cache_is_fresh('invalid', now))

    def test_partial_failure_still_reports_errors(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict('os.environ', {'SIMPLE_SCANNER_DATA_DIR': tmp}):
            def fetch(query):
                if query == 'solana':
                    raise RuntimeError('source unavailable')
                return {'pairs': []}
            output = io.StringIO()
            with patch.object(dex, 'fetch', side_effect=fetch), redirect_stdout(output):
                dex.main()
            report = json.loads((Path(tmp)/'dex_latest.json').read_text())
            self.assertEqual(len(report['errors']), 1)
            self.assertEqual(report['scope'], 'sampled_search_not_full_dex_universe')
            self.assertIn('DEX_SUMMARY', output.getvalue())

    def test_all_sources_fail_closed_and_circuit_recovers(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict('os.environ', {'SIMPLE_SCANNER_DATA_DIR': tmp}):
            with patch.object(dex, 'fetch', side_effect=RuntimeError('offline')):
                with redirect_stdout(io.StringIO()):
                    dex_guard.run()
            state = Path(tmp)/'dex_circuit.json'
            self.assertTrue(state.exists())
            with patch.object(dex, 'main') as scanner, redirect_stdout(io.StringIO()):
                dex_guard.run()
                scanner.assert_not_called()
            state.write_text(json.dumps({'blocked_at': (dt.datetime.now(UTC)-dt.timedelta(hours=4)).isoformat()}))
            with patch.object(dex, 'fetch', return_value={'pairs': []}), redirect_stdout(io.StringIO()):
                dex_guard.run()
            self.assertFalse(state.exists())

if __name__ == '__main__':
    unittest.main()
