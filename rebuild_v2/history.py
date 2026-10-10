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
    con.execute("CREATE TABLE IF NOT EXISTS scan_cycles (cycle_id TEXT PRIMARY KEY, run_id TEXT NOT NULL UNIQUE, recorded_at TEXT NOT NULL)")
    con.execute("CREATE INDEX IF NOT EXISTS obs_pair_idx ON observations(pair)")
    return con
def store_run(result):
    rid=result.get("started_at") or result.get("completed_at")
    cycle_id=os.environ.get("SCAN_CYCLE_ID","").strip()
    with connect() as con:
        if cycle_id:
            existing=con.execute("SELECT run_id FROM scan_cycles WHERE cycle_id=?",(cycle_id,)).fetchone()
            if existing:
                print("DUPLICATE_SCAN_CYCLE_SKIPPED",cycle_id,"original_run",existing[0])
                return
            con.execute("INSERT INTO scan_cycles VALUES (?,?,?)",(cycle_id,rid,result["completed_at"]))
        con.execute("INSERT OR IGNORE INTO runs VALUES (?,?,?,?)",(rid,result["completed_at"],result["health"],json.dumps(result)))
        watched={c["pair"] for c in result.get("watch",[])}
        for c in (result.get("market_quotes") or result.get("watch",[])):
            if c.get("price") is None or c.get("price",0)>0:
                con.execute("INSERT OR IGNORE INTO observations VALUES (?,?,?,?,?)",(rid,c["pair"],c.get("price"),c.get("score",0),"WATCH" if c["pair"] in watched else "NOT_SELECTED"))
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
    """Count missed pair-days from earliest non-selected observations only.\n    Avoid hindsight-selected winners and repeated overlapping scans."""
    with connect() as con:
        rows=con.execute("""WITH earliest AS (
            SELECT o.pair, x.return_pct,
                   ROW_NUMBER() OVER (
                     PARTITION BY substr(r.created_at,1,10),o.pair
                     ORDER BY r.created_at ASC,r.id ASC
                   ) AS rn
            FROM outcomes x
            JOIN observations o ON o.run_id=x.run_id AND o.pair=x.pair
            JOIN runs r ON r.id=o.run_id
            WHERE x.horizon_hours=? AND o.status='NOT_SELECTED'
          )
          SELECT pair,COUNT(*),MAX(return_pct) FROM earliest
          WHERE rn=1 AND return_pct>=?
          GROUP BY pair ORDER BY COUNT(*) DESC,MAX(return_pct) DESC LIMIT 20""",
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
    """No tuning from correlated observations of the same pair."""
    return 0

def prospective_learning(min_days=10, min_pairs=8):
    """Chronological validation of high-score vs lower-score 4h hit rates.
    Earliest labeled observation per pair-day; prevents hindsight-max score/outcome leakage.\n    No unvalidated score adjustments.
    """
    with connect() as con:
        rows=con.execute("""WITH ranked AS (
              SELECT substr(r.created_at,1,10) AS day, o.pair,
                     o.score, CASE WHEN x.return_pct>=5 THEN 1 ELSE 0 END AS hit,
                     ROW_NUMBER() OVER (
                       PARTITION BY substr(r.created_at,1,10),o.pair
                       ORDER BY r.created_at ASC,r.id ASC
                     ) AS rn
              FROM outcomes x
              JOIN observations o ON o.run_id=x.run_id AND o.pair=x.pair
              JOIN runs r ON r.id=o.run_id
              WHERE x.horizon_hours=4
            )
            SELECT day,pair,score,hit FROM ranked WHERE rn=1
            ORDER BY day,pair""").fetchall()
    days=sorted({x[0] for x in rows})
    result={"status":"INSUFFICIENT_DATA","pair_days":len(rows),
            "days":len(days),"validated":False,"adjustment":0,"score_threshold":60}
    if len(days)<min_days or len({x[1] for x in rows})<min_pairs:return result
    cutoff=days[int(len(days)*0.7)]
    def stats(before):
        groups={"HIGH":[],"LOW":[]}
        for day,pair,score,hit in rows:
            if (day<cutoff)==before:
                groups["HIGH" if score>=60 else "LOW"].append(hit)
        if min(map(len,groups.values()))<20:return None
        return {k:sum(v)/len(v) for k,v in groups.items()}
    train=stats(True);test=stats(False)
    result.update(train=train,test=test)
    if train is None or test is None:return result
    delta=train["HIGH"]-train["LOW"]
    verified=delta>=0.05 and test["HIGH"]-test["LOW"]>=0.03
    result.update(status="VALIDATED" if verified else "NO_VALIDATED_IMPROVEMENT",
                  validated=verified,adjustment=round(min(4,delta*20),2) if verified else 0)
    return result

def historical_cohort_analysis(horizon=1):
    """Analyze existing labeled observations without assuming independent samples."""
    with connect() as con:
        rows=con.execute("""SELECT o.status,COUNT(*),COUNT(DISTINCT o.pair),
          AVG(x.return_pct),AVG(CASE WHEN x.return_pct>=2 THEN 1.0 ELSE 0 END),
          AVG(CASE WHEN x.return_pct>=5 THEN 1.0 ELSE 0 END)
          FROM outcomes x JOIN observations o ON o.run_id=x.run_id AND o.pair=x.pair
          WHERE x.horizon_hours=? GROUP BY o.status""",(horizon,)).fetchall()
    return {"horizon_hours":horizon,"cohorts":[{"status":s,"observations":n,"unique_pairs":pairs,
        "mean_return_pct":round(avg,3),"gain_2pct_rate":round(hit2,4),
        "gain_5pct_rate":round(hit5,4)} for s,n,pairs,avg,hit2,hit5 in rows],
        "interpretation":"Diagnostic only; overlapping scan observations are correlated. No automated score tuning."}

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
    """Unique successful scheduled cycles, not retry/run counts.

    A recovered or retried cycle counts once. Do not claim measured coverage
    unless the cycle ledger spans the entire observation window.
    """
    now=now or dt.datetime.now(dt.timezone.utc)
    with connect() as con:
        rows=con.execute("""SELECT c.cycle_id FROM scan_cycles c
            JOIN runs r ON r.id=c.run_id
            WHERE r.health='COMPLETE' ORDER BY c.cycle_id""").fetchall()
    cycles=set()
    for (value,) in rows:
        try:
            stamp=dt.datetime.fromisoformat(value.replace("Z","+00:00"))
            if stamp.tzinfo is not None:
                cycles.add(stamp.astimezone(dt.timezone.utc))
        except (ValueError,TypeError):
            continue
    result={}
    for hours in (24,168):
        start=now-dt.timedelta(hours=hours)
        # Aligned 15-minute slots in (start, now], including a short
        # processing grace: the current slot may still be executing.
        grace=dt.timedelta(minutes=7)
        end=now-grace
        expected_slots=[]
        slot=start.replace(minute=(start.minute//15)*15,second=0,microsecond=0)
        if slot<=start:
            slot+=dt.timedelta(minutes=15)
        while slot<=end:
            expected_slots.append(slot)
            slot+=dt.timedelta(minutes=15)
        observed=sum(slot in cycles for slot in expected_slots)
        sufficient=bool(cycles) and min(cycles)<=start
        expected=len(expected_slots)
        result[f"{hours}h"]={
            "observed_completed":observed,
            "expected_scheduled":expected if sufficient else None,
            "coverage_pct":round(100*observed/expected,2) if sufficient and expected else None,
            "status":"MEASURED" if sufficient else "INSUFFICIENT_HISTORY",
            "measurement":"UNIQUE_15M_CYCLE_LEDGER",
            "grace_minutes":7
        }
    return result


def early_detection_benchmark(horizon=4, gain_pct=5, min_pair_days=100):
    """Compare earliest watched vs non-watched pair-days at a fixed horizon.

    This is a descriptive prospective hit-rate benchmark, not a causal
    performance estimate. Only pairs with actual matured outcome labels enter.
    One observation per pair-day prevents repeated scans inflating evidence.
    """
    with connect() as con:
        rows=con.execute("""WITH ranked AS (
            SELECT substr(r.created_at,1,10) AS day,o.pair,o.status,
                   x.return_pct,
                   ROW_NUMBER() OVER (
                       PARTITION BY substr(r.created_at,1,10),o.pair
                       ORDER BY r.created_at ASC,r.id ASC
                   ) AS rn
            FROM outcomes x
            JOIN observations o ON o.run_id=x.run_id AND o.pair=x.pair
            JOIN runs r ON r.id=o.run_id
            WHERE x.horizon_hours=? AND o.status IN ('WATCH','NOT_SELECTED')
        ) SELECT day,pair,status,return_pct FROM ranked WHERE rn=1""",
            (horizon,)).fetchall()
    groups={"WATCH":[],"NOT_SELECTED":[]}
    for day,pair,status,ret in rows:
        groups[status].append(float(ret))
    def stats(values):
        n=len(values)
        return {"n":n,"hits":sum(v>=gain_pct for v in values),
                "hit_rate":round(sum(v>=gain_pct for v in values)/n,5) if n else None,
                "mean_return_pct":round(sum(values)/n,4) if n else None}
    a=stats(groups["WATCH"]);b=stats(groups["NOT_SELECTED"])
    days=len({day for day,_,_,_ in rows})
    ready=len(rows)>=min_pair_days and min(a["n"],b["n"])>=20 and days>=10
    return {"status":"DESCRIPTIVE_ONLY" if ready else "INSUFFICIENT_DATA",
            "horizon_hours":horizon,"gain_threshold_pct":gain_pct,
            "pair_days":len(rows),"days":days,"watch":a,"baseline":b,
            "lift":round(a["hit_rate"]/b["hit_rate"],3) if ready and b["hit_rate"] else None,
            "ranking_adjustment_allowed":False,
            "limitations":["Only matured prospective labels","Earliest labeled pair-day only",
                           "Selection and liquidity bias remain","Not an executable entry backtest"]}
