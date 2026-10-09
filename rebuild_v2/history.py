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
        watched={c["pair"] for c in result.get("watch",[])}
        for c in (result.get("market_quotes") or result.get("watch",[])):
            if c.get("price",0)>0:
                con.execute("INSERT OR IGNORE INTO observations VALUES (?,?,?,?,?)",(rid,c["pair"],c["price"],c.get("score",0),"WATCH" if c["pair"] in watched else "NOT_SELECTED"))
    # Durable history is restored and committed by the GitHub workflow.
    # No external secrets or Supabase API are needed.
def evaluate_outcomes(result, horizons=(1, 4, 24, 72)):
    """Mark only elapsed prospective horizons using current executable bid quotes.
    Never label an outcome if the original price or current bid is missing.
    """
    now=dt.datetime.fromisoformat(result["completed_at"])
    prices={c["pair"]: c["bid"] for c in result.get("market_quotes",[]) if c.get("bid",0)>0}
    with connect() as con:
        rows=con.execute("SELECT o.run_id,o.pair,o.price,r.created_at FROM observations o JOIN runs r ON r.id=o.run_id WHERE o.price > 0 AND r.created_at >= ?", ((now-dt.timedelta(hours=73)).isoformat(),)).fetchall()
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

def miss_report(horizon=4, threshold=5):
    """Find historical breakouts that were never selected for the watchlist."""
    with connect() as con:
        rows=con.execute("""SELECT o.pair, COUNT(*), MAX(x.return_pct)
          FROM outcomes x JOIN observations o ON o.run_id=x.run_id AND o.pair=x.pair
          WHERE x.horizon_hours=? AND x.return_pct>=? AND o.status='NOT_SELECTED'
          GROUP BY o.pair ORDER BY COUNT(*) DESC, MAX(x.return_pct) DESC LIMIT 20""",
          (horizon,threshold)).fetchall()
    return [{"pair":p,"missed_breakouts":n,"best_return_pct":round(ret,2)} for p,n,ret in rows]

def historical_signal_adjustments(min_samples=30):
    """Conservative, bounded score adjustment from observed 4h outcomes.
    Adjust watch and non-watch populations only when both have enough samples.
    """
    with connect() as con:
        rows=con.execute("""SELECT o.status, COUNT(*),
          AVG(CASE WHEN x.return_pct>=5 THEN 1.0 ELSE 0 END)
          FROM outcomes x JOIN observations o ON o.run_id=x.run_id AND o.pair=x.pair
          WHERE x.horizon_hours=4 GROUP BY o.status""").fetchall()
    stats={s:{"samples":n,"hit_rate":round(rate,4)} for s,n,rate in rows}
    a=stats.get("WATCH",{}); b=stats.get("NOT_SELECTED",{})
    ready=a.get("samples",0)>=min_samples and b.get("samples",0)>=min_samples
    delta=(a["hit_rate"]-b["hit_rate"]) if ready else 0
    return {"ready":ready,"groups":stats,"watch_score_adjustment":round(max(-8,min(8,delta*40)),2) if ready else 0}

def pair_signal_adjustment(pair, min_samples=3):
    with connect() as con:
        row=con.execute("SELECT COUNT(*), AVG(CASE WHEN x.return_pct>=5 THEN 1.0 ELSE 0 END) FROM outcomes x JOIN observations o ON o.run_id=x.run_id AND o.pair=x.pair WHERE x.horizon_hours=4 AND o.pair=?",(pair,)).fetchone()
    n,rate=row
    if n<min_samples:
        return 0
    return round(max(-6,min(6,(rate-0.10)*12*n/(n+20))),2)

def history_diagnostics():
    """Expose actual durable history and prospective labeling readiness."""
    with connect() as con:
        runs=con.execute("SELECT COUNT(*) FROM runs").fetchone()[0]
        observations=con.execute("SELECT COUNT(*) FROM observations").fetchone()[0]
        outcomes=con.execute("SELECT COUNT(*) FROM outcomes").fetchone()[0]
        oldest=con.execute("SELECT MIN(created_at) FROM runs").fetchone()[0]
        newest=con.execute("SELECT MAX(created_at) FROM runs").fetchone()[0]
        unlabeled=con.execute("SELECT COUNT(*) FROM observations o WHERE NOT EXISTS (SELECT 1 FROM outcomes x WHERE x.run_id=o.run_id AND x.pair=o.pair)").fetchone()[0]
    return {"runs":runs,"observations":observations,"outcomes":outcomes,"unlabeled_observations":unlabeled,"oldest_run_at":oldest,"newest_run_at":newest,"learning_status":"OUTCOMES_AVAILABLE" if outcomes else "AWAITING_PROSPECTIVE_OUTCOMES","history_available":runs>0}

def reliability_scorecard(now=None):
    """Observed scan completion coverage, not an estimate from individual successes."""
    now=now or dt.datetime.now(dt.timezone.utc)
    with connect() as con:
        stamps=[dt.datetime.fromisoformat(row[0]) for row in con.execute("SELECT created_at FROM runs WHERE health='COMPLETE' ORDER BY created_at")]
    result={}
    for hours in (24,168):
        start=now-dt.timedelta(hours=hours)
        observed=sum(start<=stamp<=now for stamp in stamps)
        # Do not infer past scheduled attempts from a database younger than the window.
        span=(now-min(stamps)).total_seconds()/3600 if stamps else 0
        sufficient=span>=hours
        expected=hours*4
        result[f"{hours}h"]={"observed_completed":observed,"expected_scheduled":expected if sufficient else None,"coverage_pct":round(100*min(observed,expected)/expected,2) if sufficient else None,"status":"MEASURED" if sufficient else "INSUFFICIENT_HISTORY"}
    return result
