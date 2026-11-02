"""Validate all four forward outcome horizons using real, timestamped observations."""
import datetime as dt
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner import history

class ForwardHorizonTests(unittest.TestCase):
    def test_all_horizons_use_first_observation_and_persist(self):
        with tempfile.TemporaryDirectory() as folder:
            db=Path(folder)/"history.sqlite3"
            latest=Path(folder)/"latest.json"
            start=dt.datetime(2026,10,11,0,tzinfo=dt.timezone.utc)
            with patch.object(history,"DB",db),patch.object(history,"LATEST",latest):
                for minutes,price in [(0,100),(65,102),(185,104),(365,108),(1445,112)]:
                    stamp=(start+dt.timedelta(minutes=minutes)).isoformat()
                    latest.write_text(json.dumps({"status":"RESEARCH_ONLY","buy_approved":False,"matched_tickers":100,"universe":100,"validated_watch":1,"completed_at":stamp,"market_prices":{"TESTUSD":price},"watch":[{"pair":"TESTUSD","price":price,"score":70,"status":"WATCH_RESEARCH_ONLY"}]}))
                    history.persist()
                con=sqlite3.connect(db)
                actual=dict(con.execute("SELECT horizon_hours,return_pct FROM outcomes WHERE run_at=? AND pair='TESTUSD'",(start.isoformat(),)).fetchall())
                self.assertEqual(actual,{1:2.0,3:4.0,6:8.0,24:12.0})
                summary=json.loads((db.parent/"learning.json").read_text())
                for horizon in (1,3,6,24):
                    row=next(x for x in summary["forward_horizon_coverage"] if x["hours"]==horizon)
                    self.assertGreaterEqual(row["evaluated"],1)
                self.assertEqual(con.execute("PRAGMA integrity_check").fetchone()[0],"ok")
                con.close()
