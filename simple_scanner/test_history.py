"""Offline regression tests for the isolated paper-history ledger."""
import datetime as dt
import json
import os
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from simple_scanner import history

class HistoryTests(unittest.TestCase):
    def test_snapshot_idempotence_and_forward_outcome(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            db=root/"history.sqlite3"
            latest=root/"latest.json"
            output=root/"learning.json"
            start=dt.datetime(2026,10,11,12,tzinfo=dt.timezone.utc)
            def write(t, price, market_price=None):
                latest.write_text(json.dumps({"status":"RESEARCH_ONLY","buy_approved":False,"matched_tickers":100,"universe":100,"validated_watch":1,"completed_at":t.isoformat(),"market_prices":{"TESTUSD":market_price} if market_price is not None else {},"watch":[{"pair":"TESTUSD","price":price,"score":75,"status":"WATCH_RESEARCH_ONLY"}]}))
            with patch.object(history,"DB",db),patch.object(history,"LATEST",latest):
                original=history.Path
                # Redirect the fixed output path through a temporary working directory.
                cwd=os.getcwd()
                try:
                    os.chdir(directory)
                    write(start,10)
                    history.persist()
                    history.persist()
                    self.assertEqual(sqlite3.connect(db).execute("SELECT COUNT(*) FROM snapshots").fetchone()[0],1)
                    write(start+dt.timedelta(hours=1,minutes=5),11)
                    history.persist()
                    con=sqlite3.connect(db)
                    self.assertEqual(con.execute("SELECT COUNT(*) FROM snapshots").fetchone()[0],2)
                    value=con.execute("SELECT return_pct FROM outcomes WHERE horizon_hours=1").fetchone()
                    self.assertEqual(value[0],10.0)
                    history.persist()
                    self.assertEqual(con.execute("SELECT COUNT(*) FROM outcomes").fetchone()[0],1)
                    self.assertEqual(con.execute("PRAGMA integrity_check").fetchone()[0],"ok")
                    self.assertEqual(con.execute("SELECT COUNT(*) FROM candidate_features").fetchone()[0],2)
                    self.assertEqual(con.execute("SELECT COUNT(*) FROM candidate_features WHERE pair=\'TESTUSD\'").fetchone()[0],2)
                    summary=json.loads((db.parent/"learning.json").read_text())
                    self.assertFalse(summary["buy_approved"])
                    self.assertEqual(summary["signal_outcomes_by_horizon"][0]["hours"],1)
                    self.assertEqual(summary["signal_outcomes_by_horizon"][0]["samples"],1)
                    con.close()
                finally:
                    os.chdir(cwd)


    def test_forward_outcome_after_watchlist_exit(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            db=root/"history.sqlite3"
            latest=root/"latest.json"
            start=dt.datetime(2026,10,11,12,tzinfo=dt.timezone.utc)
            def report(t,watch,prices):
                latest.write_text(json.dumps({"status":"RESEARCH_ONLY","buy_approved":False,"matched_tickers":100,"universe":100,"validated_watch":1,"completed_at":t.isoformat(),"watch":watch,"market_prices":prices}))
            first=[{"pair":"TESTUSD","price":10,"score":75,"status":"WATCH_RESEARCH_ONLY"}]
            second=[{"pair":"OTHERUSD","price":5,"score":75,"status":"WATCH_RESEARCH_ONLY"}]
            with patch.object(history,"DB",db),patch.object(history,"LATEST",latest):
                report(start,first,{"TESTUSD":10,"OTHERUSD":5})
                history.persist()
                report(start+dt.timedelta(hours=1,minutes=5),second,{"TESTUSD":12,"OTHERUSD":5})
                history.persist()
                con=sqlite3.connect(db)
                self.assertEqual(con.execute("SELECT return_pct FROM outcomes WHERE pair='TESTUSD' AND horizon_hours=1").fetchone()[0],20.0)
                self.assertEqual(con.execute("SELECT COUNT(*) FROM market_observations").fetchone()[0],4)
                self.assertEqual(json.loads((db.parent/"learning.json").read_text())["unselected_gainers_5pct_observations"],0)
                con.close()

    def test_backfills_first_observation_not_later_price(self):
        with tempfile.TemporaryDirectory() as directory:
            db=Path(directory)/"history.sqlite3"
            latest=Path(directory)/"latest.json"
            start=dt.datetime(2026,10,11,12,tzinfo=dt.timezone.utc)
            with patch.object(history,"DB",db),patch.object(history,"LATEST",latest):
                for minute,price in ((0,10),(65,11),(80,15),(180,20)):
                    now=start+dt.timedelta(minutes=minute)
                    latest.write_text(json.dumps({"status":"RESEARCH_ONLY","buy_approved":False,"matched_tickers":100,"universe":100,"validated_watch":1,"completed_at":now.isoformat(),"watch":[{"pair":"OTHERUSD","price":5,"score":80,"status":"WATCH_RESEARCH_ONLY"}] if minute else [{"pair":"TESTUSD","price":10,"score":80,"status":"WATCH_RESEARCH_ONLY"}],"market_prices":{"TESTUSD":price,"OTHERUSD":5}}))
                    history.persist()
                con=sqlite3.connect(db)
                outcome=con.execute("SELECT return_pct,evaluated_at FROM outcomes WHERE pair='TESTUSD' AND horizon_hours=1").fetchone()
                self.assertEqual(outcome[0],10.0)
                self.assertEqual(outcome[1],(start+dt.timedelta(minutes=65)).isoformat())
                con.close()

    def test_late_backfill_uses_first_valid_horizon_observation(self):
        with tempfile.TemporaryDirectory() as directory:
            db=Path(directory)/"history.sqlite3"
            latest=Path(directory)/"latest.json"
            start=dt.datetime(2026,10,11,12,tzinfo=dt.timezone.utc)
            with patch.object(history,"DB",db),patch.object(history,"LATEST",latest):
                for minute,price,selected in ((0,10,True),(65,11,False),(180,20,False)):
                    watch=[{"pair":"TESTUSD" if selected else "OTHERUSD","price":10 if selected else 5,"score":80,"status":"WATCH_RESEARCH_ONLY"}]
                    latest.write_text(json.dumps({"status":"RESEARCH_ONLY","buy_approved":False,"matched_tickers":100,"universe":100,"validated_watch":1,"completed_at":(start+dt.timedelta(minutes=minute)).isoformat(),"watch":watch,"market_prices":{"TESTUSD":price,"OTHERUSD":5}}))
                    if minute==65:
                        # Simulate a missed evaluation job while retaining its observed price.
                        history.LATEST.read_text()
                        con=sqlite3.connect(db)
                        con.execute("INSERT INTO market_observations VALUES (?,?,?)",((start+dt.timedelta(minutes=65)).isoformat(),"TESTUSD",11))
                        con.commit();con.close()
                    else:
                        history.persist()
                con=sqlite3.connect(db)
                self.assertEqual(con.execute("SELECT return_pct FROM outcomes WHERE pair='TESTUSD' AND horizon_hours=1").fetchone()[0],10.0)
                con.close()

    def test_existing_feature_table_migrates_without_losing_history(self):
        with tempfile.TemporaryDirectory() as directory:
            db=Path(directory)/"history.sqlite3"
            latest=Path(directory)/"latest.json"
            con=sqlite3.connect(db)
            con.execute("CREATE TABLE candidate_features (run_at TEXT NOT NULL, pair TEXT NOT NULL, base_score REAL NOT NULL, early_signal_score REAL, move_15m_pct REAL, volume_accel REAL, research_rank INTEGER, PRIMARY KEY(run_at,pair))")
            con.execute("INSERT INTO candidate_features VALUES (?,?,?,?,?,?,?)",("2026-10-11T10:00:00+00:00","OLDUSD",50,60,2,1.5,1))
            con.commit();con.close()
            now=dt.datetime(2026,10,11,12,tzinfo=dt.timezone.utc)
            latest.write_text(json.dumps({"status":"RESEARCH_ONLY","buy_approved":False,"matched_tickers":100,"universe":100,"validated_watch":1,"completed_at":now.isoformat(),"watch":[{"pair":"NEWUSD","price":2,"score":70,"status":"WATCH_RESEARCH_ONLY","base_rank":17,"research_rank":1,"early_signal_score":90}],"market_prices":{"NEWUSD":2}}))
            with patch.object(history,"DB",db),patch.object(history,"LATEST",latest):
                history.persist()
            con=sqlite3.connect(db)
            self.assertEqual(con.execute("SELECT base_rank FROM candidate_features WHERE pair='NEWUSD'").fetchone()[0],17)
            self.assertIsNone(con.execute("SELECT base_rank FROM candidate_features WHERE pair='OLDUSD'").fetchone()[0])
            self.assertEqual(con.execute("SELECT COUNT(*) FROM candidate_features").fetchone()[0],2)
            con.close()

    def test_long_scan_gap_is_not_counted_as_rapid_breakout(self):
        with tempfile.TemporaryDirectory() as directory:
            db=Path(directory)/"history.sqlite3"
            latest=Path(directory)/"latest.json"
            start=dt.datetime(2026,10,11,12,tzinfo=dt.timezone.utc)
            with patch.object(history,"DB",db),patch.object(history,"LATEST",latest):
                for offset,price in ((0,10),(180,20)):
                    watch=[{"pair":"OTHERUSD","price":5,"score":80,"status":"WATCH_RESEARCH_ONLY"}]
                    latest.write_text(json.dumps({"status":"RESEARCH_ONLY","buy_approved":False,"matched_tickers":100,"universe":100,"validated_watch":1,"completed_at":(start+dt.timedelta(minutes=offset)).isoformat(),"watch":watch,"market_prices":{"OTHERUSD":5,"MISSEDUSD":price}}))
                    history.persist()
                result=json.loads((db.parent/"learning.json").read_text())
                self.assertEqual(result["unselected_gainers_5pct_observations"],0)

    def test_unselected_market_breakout_is_counted(self):
        with tempfile.TemporaryDirectory() as directory:
            db=Path(directory)/"history.sqlite3"
            latest=Path(directory)/"latest.json"
            start=dt.datetime(2026,10,11,12,tzinfo=dt.timezone.utc)
            with patch.object(history,"DB",db),patch.object(history,"LATEST",latest):
                for offset,price in ((0,10),(30,11)):
                    watch=[{"pair":"OTHERUSD","price":5,"score":80,"status":"WATCH_RESEARCH_ONLY"}]
                    latest.write_text(json.dumps({"status":"RESEARCH_ONLY","buy_approved":False,"matched_tickers":100,"universe":100,"validated_watch":1,"completed_at":(start+dt.timedelta(minutes=offset)).isoformat(),"watch":watch,"market_prices":{"OTHERUSD":5,"MISSEDUSD":price}}))
                    history.persist()
                report=json.loads((db.parent/"learning.json").read_text())
                self.assertEqual(report["unselected_gainers_5pct_observations"],1)
                self.assertEqual(report["missed_breakout_examples"][0]["pair"],"MISSEDUSD")
                self.assertEqual(report["missed_breakout_examples"][0]["next_scan_gain_pct"],10.0)

if __name__=="__main__":
    unittest.main()
