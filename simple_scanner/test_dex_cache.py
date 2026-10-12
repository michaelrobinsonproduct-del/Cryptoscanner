"""Regression checks for DEX research cache and outage fallback."""
import datetime as dt
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner import dex

class DexCacheTests(unittest.TestCase):
    def test_recent_cache_skips_provider(self):
        with tempfile.TemporaryDirectory() as directory:
            record={"observed_at":dt.datetime.now(dt.timezone.utc).isoformat(),"candidates":[{"symbol":"ABC"}]}
            (Path(directory)/"dex_latest.json").write_text(json.dumps(record))
            with patch.dict(os.environ,{"SIMPLE_SCANNER_DATA_DIR":directory}),patch.object(dex,"fetch",side_effect=AssertionError("must not fetch")):
                dex.main()
    def test_stale_cache_preserved_during_outage(self):
        with tempfile.TemporaryDirectory() as directory:
            record={"observed_at":(dt.datetime.now(dt.timezone.utc)-dt.timedelta(hours=2)).isoformat(),"candidates":[{"symbol":"ABC"}]}
            path=Path(directory)/"dex_latest.json"
            original=json.dumps(record)
            path.write_text(original)
            with patch.dict(os.environ,{"SIMPLE_SCANNER_DATA_DIR":directory}),patch.object(dex,"fetch",side_effect=TimeoutError("offline")):
                dex.main()
            self.assertEqual(path.read_text(),original)
