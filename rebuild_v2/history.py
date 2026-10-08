"""Persistent SQLite scan history and prospective outcome labels.
SQLite is per-run on GitHub Actions unless database file is restored externally.
The GitHub Actions workflow restores and saves this database on a dedicated branch.
"""
import datetime as dt
import json
import os
import pathlib
import sqlite3
import urllib.request

DB=pathlib.Path(os.environ.get("KRAKEN_HISTORY_DB","rebuild_v2/output/history.sqlite3"))
def connect():
    DB.parent.mkdir(parents=True,exist_ok=True)
    con=sqlite3.connect(DB)
    con.execute("PRAGMA journal_mode=DELETE")
    con.execute("CREATE TABLE IF NOT EXISTS runs (id TEXT PRIMARY KEY, created_at TEXT NOT NULL, health TEXT NOT NULL, payload TEXT NOT NULL)")
    con.execute("CREATE TABLE IF NOT EXISTS observations (run_id TEXT NOT NULL, pair TEXT NOT NULL, price REAL, score REAL, status TEXT, PRIMARY KEY(run_id,pair))")
    con.execute("CREATE TABLE IF NOT EXISTS outcomes (run_id TEXT, pair TEXT, horizon_hours INTEGER, return_pct REAL, evaluated_at TEXT, PRIMARY KEY(run_id,pair,horizon_hours))")
    con.execute("CREATE INDEX IF NOT EXISTS obs_pair_idx ON observations(pair)")
    return con
def store_run(result):
    rid=result.get("started_at") or result.get("completed_at")
    with connect() as con:
        con.execute("INSERT OR IGNORE INTO runs VALUES (?,?,?,?)",(rid,result["completed_at"],result["health"],json.dumps(result)))
        for c in result.get("watch",[]):
            con.execute("INSERT OR IGNORE INTO observations VALUES (?,?,?,?,?)",(rid,c["pair"],c.get("price"),c["score"],c["status"]))
    # Durable history is restored and committed by the GitHub workflow.
    # No external secrets or Supabase API are needed.
def evaluate_outcomes(result, horizons=(1, 4, 24, 72)):
    """Mark only elapsed prospective horizons using current executable bid quotes.
    Never label an outcome if the original price or current bid is missing.
    """
    now=dt.datetime.fromisoformat(result["completed_at"])
    prices={c["pair"]: c["bid"] for c in result.get("market_quotes",[]) if c.get("bid",0)>0}
    with connect() as con:
        rows=con.execute("SELECT o.run_id,o.pair,o.price,r.created_at FROM observations o JOIN runs r ON r.id=o.run_id WHERE o.price > 0").fetchall()
        for run_id,pair,entry,created in rows:
            bid=prices.get(pair)
            if bid is None:
                continue
            age=(now-dt.datetime.fromisoformat(created)).total_seconds()/3600
            for horizon in horizons:
                # Require an observation near the requested horizon, not any later snapshot.
                if horizon <= age <= horizon + 0.5:
                    con.execute("INSERT OR IGNORE INTO outcomes VALUES (?,?,?,?,?)",
                                (run_id,pair,horizon,100*(bid/entry-1),now.isoformat()))

def outcome_summary():
    with connect() as con:
        rows=con.execute("SELECT horizon_hours, COUNT(*), AVG(return_pct) FROM outcomes GROUP BY horizon_hours").fetchall()
    return [{"horizon_hours":h,"observations":n,"mean_return_pct":avg} for h,n,avg in rows]

def learning_report():
    """Observed prospective results only. No auto-tuning until sample size supports it."""
    with connect() as con:
        rows=con.execute("""SELECT o.horizon_hours, COUNT(*), AVG(CASE WHEN o.return_pct >= 5 THEN 1.0 ELSE 0 END),
                         AVG(CASE WHEN o.return_pct <= -5 THEN 1.0 ELSE 0 END)
                         FROM outcomes o GROUP BY o.horizon_hours ORDER BY o.horizon_hours""").fetchall()
    return [{"horizon_hours":h,"sample_size":n,"gain_5pct_rate":round(g,4),
             "loss_5pct_rate":round(l,4),"model_tuning_allowed":n>=100}
            for h,n,g,l in rows]
