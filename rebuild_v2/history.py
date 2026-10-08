"""Persistent SQLite scan history and prospective outcome labels.
SQLite is per-run on GitHub Actions unless database file is restored externally.
Optional Supabase REST persistence uses secret env vars and is fail-closed.
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
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("CREATE TABLE IF NOT EXISTS runs (id TEXT PRIMARY KEY, created_at TEXT NOT NULL, health TEXT NOT NULL, payload TEXT NOT NULL)")
    con.execute("CREATE TABLE IF NOT EXISTS observations (run_id TEXT NOT NULL, pair TEXT NOT NULL, price REAL, score REAL, status TEXT, PRIMARY KEY(run_id,pair))")
    con.execute("CREATE TABLE IF NOT EXISTS outcomes (run_id TEXT, pair TEXT, horizon_hours INTEGER, return_pct REAL, evaluated_at TEXT, PRIMARY KEY(run_id,pair,horizon_hours))")
    return con
def store_run(result):
    rid=result.get("started_at") or result.get("completed_at")
    with connect() as con:
        con.execute("INSERT OR IGNORE INTO runs VALUES (?,?,?,?)",(rid,result["completed_at"],result["health"],json.dumps(result)))
        for c in result.get("watch",[]):
            con.execute("INSERT OR IGNORE INTO observations VALUES (?,?,?,?,?)",(rid,c["pair"],c.get("price"),c["score"],c["status"]))
    # Durable history is restored and committed by the GitHub workflow.
    # No external secrets or Supabase API are needed.
def outcome_summary():
    with connect() as con:
        rows=con.execute("SELECT horizon_hours, COUNT(*), AVG(return_pct) FROM outcomes GROUP BY horizon_hours").fetchall()
    return [{"horizon_hours":h,"observations":n,"mean_return_pct":avg} for h,n,avg in rows]
