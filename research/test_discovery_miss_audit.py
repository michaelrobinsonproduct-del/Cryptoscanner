"""Offline deterministic regression checks for discovery_miss_audit."""
import datetime as dt
import sqlite3
import tempfile
from pathlib import Path
from research.discovery_miss_audit import audit

def test_audit():
    with tempfile.TemporaryDirectory() as directory:
        db=Path(directory)/"test.sqlite3"
        con=sqlite3.connect(db)
        con.executescript("""
        CREATE TABLE market_observations(run_at TEXT,pair TEXT,price REAL);
        CREATE TABLE snapshots(run_at TEXT,pair TEXT,price REAL,score REAL);
        CREATE TABLE candidate_features(run_at TEXT,pair TEXT,base_score REAL);
        """)
        t=dt.datetime.now(dt.timezone.utc).replace(microsecond=0)-dt.timedelta(minutes=40)
        a=t.isoformat();b=(t+dt.timedelta(minutes=15)).isoformat()
        con.executemany("INSERT INTO market_observations VALUES (?,?,?)",[(a,"MISSUSD",10),(b,"MISSUSD",11),(a,"WATCHUSD",10),(b,"WATCHUSD",10.6),(a,"FLATUSD",10),(b,"FLATUSD",10.1)])
        con.execute("INSERT INTO snapshots VALUES (?,?,?,?)",(a,"WATCHUSD",10,80))
        con.execute("INSERT INTO candidate_features VALUES (?,?,?)",(a,"WATCHUSD",80))
        con.commit();con.close()
        result=audit(str(db))
        assert result["breakout_observations"]==2,result
        assert result["not_on_watch"]==1,result
        assert result["on_watch"]==1,result
        assert result["unique_missed_pairs"]==1,result
        assert result["top_missed"][0]["pair"]=="MISSUSD",result
        assert result["gate_attribution"]=="UNAVAILABLE_FROM_RECORDED_DATA",result
        assert sqlite3.connect(db).execute("SELECT COUNT(*) FROM market_observations").fetchone()[0]==6
        print("PASS: audit classifications, missed example, immutable source database")
if __name__=="__main__":test_audit()
