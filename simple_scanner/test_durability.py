"""Regression checks for persistent history across separate simulated scan runs."""
import datetime as dt
import json
import os
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner import history

class DurableHistoryTests(unittest.TestCase):
    def test_data_directory_survives_separate_persist_invocations(self):
        with tempfile.TemporaryDirectory() as directory:
            data=Path(directory)
            start=dt.datetime(2026,10,11,12,tzinfo=dt.timezone.utc)
            with patch.dict(os.environ,{"SIMPLE_SCANNER_DATA_DIR":directory}):
                for minute,price in ((0,10),(65,11)):
                    t=(start+dt.timedelta(minutes=minute)).isoformat()
                    (data/"latest.json").write_text(json.dumps({"status":"RESEARCH_ONLY","buy_approved":False,"matched_tickers":100,"universe":100,"validated_watch":1,"completed_at":t,"market_prices":{"TESTUSD":price},"watch":[{"pair":"TESTUSD","price":price,"score":75,"status":"WATCH_RESEARCH_ONLY"}]}))
                    # Emulate fresh Python interpreter module loading on each scheduled run.
                    from importlib import reload
                    reload(history)
                    history.persist()
                db=sqlite3.connect(data/"history.sqlite3")
                self.assertEqual(db.execute("SELECT COUNT(*) FROM snapshots").fetchone()[0],2)
                self.assertEqual(db.execute("SELECT return_pct FROM outcomes WHERE horizon_hours=1 ORDER BY run_at LIMIT 1").fetchone()[0],10.0)
                self.assertEqual(db.execute("PRAGMA integrity_check").fetchone()[0],"ok")
                db.close()
            reload(history)
