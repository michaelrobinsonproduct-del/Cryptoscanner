"""Durable, paper-only snapshots and retrospective price outcome evaluation."""
import datetime as dt
import json
import sqlite3
from pathlib import Path

DB = Path("simple_scanner/output/history.sqlite3")
LATEST = Path("simple_scanner/output/latest.json")
HORIZONS = (1, 3, 6, 24)

def persist():
    report = json.loads(LATEST.read_text())
    assert report["status"] == "RESEARCH_ONLY" and report["buy_approved"] is False
    assert report["matched_tickers"] >= max(50, int(report["universe"] * 0.8))
    assert report["validated_watch"] > 0
    DB.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    con.execute("PRAGMA journal_mode=DELETE")
    con.execute("CREATE TABLE IF NOT EXISTS snapshots (run_at TEXT NOT NULL, pair TEXT NOT NULL, price REAL NOT NULL CHECK(price>0), score REAL NOT NULL, PRIMARY KEY(run_at,pair))")
    con.execute("CREATE TABLE IF NOT EXISTS candidate_features (run_at TEXT NOT NULL, pair TEXT NOT NULL, base_score REAL NOT NULL, early_signal_score REAL, move_15m_pct REAL, volume_accel REAL, research_rank INTEGER, PRIMARY KEY(run_at,pair))")
    con.execute("CREATE TABLE IF NOT EXISTS outcomes (run_at TEXT NOT NULL, pair TEXT NOT NULL, horizon_hours INTEGER NOT NULL, evaluated_at TEXT NOT NULL, return_pct REAL NOT NULL, PRIMARY KEY(run_at,pair,horizon_hours))")
    now = dt.datetime.fromisoformat(report["completed_at"])
    assert now.tzinfo is not None and now.utcoffset() is not None, "Scan timestamp must be timezone-aware"
    with con:
        for candidate in report["watch"]:
            if candidate.get("status") == "WATCH_RESEARCH_ONLY":
                con.execute("INSERT OR IGNORE INTO snapshots VALUES (?,?,?,?)", (report["completed_at"], candidate["pair"], candidate["price"], candidate["score"]))
                con.execute("INSERT OR IGNORE INTO candidate_features VALUES (?,?,?,?,?,?,?)", (report["completed_at"],candidate["pair"],candidate["score"],candidate.get("early_signal_score"),candidate.get("move_15m_pct"),candidate.get("volume_accel"),candidate.get("research_rank")))
        current = report.get("market_prices") or {c["pair"]: c["price"] for c in report["watch"] if c.get("status") == "WATCH_RESEARCH_ONLY"}
        # Price every prior watch candidate against the full Kraken ticker universe.
        # Missing/delisted pairs remain unevaluated; never count missing as a loss or win.
        for run_at, pair, price in con.execute("SELECT run_at,pair,price FROM snapshots").fetchall():
            observed_at = dt.datetime.fromisoformat(run_at)
            assert observed_at.tzinfo is not None and observed_at.utcoffset() is not None
            age = (now - observed_at).total_seconds()
            if pair not in current or age <= 0: continue
            for hours in HORIZONS:
                if hours*3600 <= age < (hours+1)*3600:
                    ret = 100*(current[pair]/price-1)
                    con.execute("INSERT OR IGNORE INTO outcomes VALUES (?,?,?,?,?)", (run_at,pair,hours,report["completed_at"],round(ret,4)))
    assert con.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
    n = con.execute("SELECT COUNT(*) FROM snapshots").fetchone()[0]
    outcomes = con.execute("SELECT COUNT(*) FROM outcomes").fetchone()[0]
    feature_rows=con.execute("SELECT COUNT(*) FROM candidate_features").fetchone()[0]
    eligible_outcome_pairs=con.execute("SELECT COUNT(DISTINCT pair) FROM snapshots WHERE pair IN (SELECT pair FROM snapshots)").fetchone()[0]
    summary = {"market_price_coverage":len(report.get("market_prices",{})),"feature_rows":feature_rows,"snapshots":n,"outcomes":outcomes,"history_db_integrity":"ok","evaluation":"FULL_MARKET_PRICE_FORWARD_PENDING_HORIZON_COVERAGE" if report.get("market_prices") else "INCOMPLETE_WATCHLIST_ONLY","model_updates":"DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION","buy_approved":False}
    (DB.parent / "learning.json").write_text(json.dumps(summary,indent=2))
    print("HISTORY_PERSISTED",json.dumps(summary))
    con.close()

if __name__ == "__main__": persist()
