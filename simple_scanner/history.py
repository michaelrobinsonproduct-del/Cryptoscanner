"""Durable, paper-only snapshots and retrospective price outcome evaluation."""
import datetime as dt
import json
import math
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
    con.execute("CREATE TABLE IF NOT EXISTS candidate_features (run_at TEXT NOT NULL, pair TEXT NOT NULL, base_score REAL NOT NULL, early_signal_score REAL, move_15m_pct REAL, volume_accel REAL, research_rank INTEGER, base_rank INTEGER, PRIMARY KEY(run_at,pair))")
    existing_columns={r[1] for r in con.execute("PRAGMA table_info(candidate_features)")}
    if "base_rank" not in existing_columns:
        con.execute("ALTER TABLE candidate_features ADD COLUMN base_rank INTEGER")
    con.execute("CREATE TABLE IF NOT EXISTS market_observations (run_at TEXT NOT NULL, pair TEXT NOT NULL, price REAL NOT NULL CHECK(price>0), PRIMARY KEY(run_at,pair))")
    con.execute("CREATE INDEX IF NOT EXISTS idx_market_pair_time ON market_observations(pair,run_at)")
    con.execute("CREATE INDEX IF NOT EXISTS idx_market_time ON market_observations(run_at)")
    con.execute("CREATE INDEX IF NOT EXISTS idx_snapshots_time ON snapshots(run_at)")
    con.execute("CREATE TABLE IF NOT EXISTS outcomes (run_at TEXT NOT NULL, pair TEXT NOT NULL, horizon_hours INTEGER NOT NULL, evaluated_at TEXT NOT NULL, return_pct REAL NOT NULL, PRIMARY KEY(run_at,pair,horizon_hours))")
    con.execute("CREATE INDEX IF NOT EXISTS idx_outcomes_horizon ON outcomes(horizon_hours)")
    now = dt.datetime.fromisoformat(report["completed_at"])
    assert now.tzinfo is not None and now.utcoffset() is not None, "Scan timestamp must be timezone-aware"
    with con:
        for pair,price in report.get("market_prices",{}).items():
            if isinstance(price,(int,float)) and math.isfinite(price) and price>0:
                con.execute("INSERT OR IGNORE INTO market_observations VALUES (?,?,?)",(report["completed_at"],pair,price))
        if not report.get("market_prices"):
            for candidate in report["watch"]:
                if candidate.get("status")=="WATCH_RESEARCH_ONLY":
                    con.execute("INSERT OR IGNORE INTO market_observations VALUES (?,?,?)",(report["completed_at"],candidate["pair"],candidate["price"]))
        for candidate in report["watch"]:
            if candidate.get("status") == "WATCH_RESEARCH_ONLY":
                con.execute("INSERT OR IGNORE INTO snapshots VALUES (?,?,?,?)", (report["completed_at"], candidate["pair"], candidate["price"], candidate["score"]))
                con.execute("INSERT OR IGNORE INTO candidate_features (run_at,pair,base_score,early_signal_score,move_15m_pct,volume_accel,research_rank,base_rank) VALUES (?,?,?,?,?,?,?,?)", (report["completed_at"],candidate["pair"],candidate["score"],candidate.get("early_signal_score"),candidate.get("move_15m_pct"),candidate.get("volume_accel"),candidate.get("research_rank"),candidate.get("base_rank")))
        current = report.get("market_prices") or {c["pair"]: c["price"] for c in report["watch"] if c.get("status") == "WATCH_RESEARCH_ONLY"}
        # Only fetch unresolved snapshots inside an eligible horizon window.
        # This avoids rescanning the entire ledger on every scheduled execution.
        # Use the first actual observation in [horizon, horizon+1h), even when
        # a scheduled scan was missed. Do not substitute the latest price for
        # an old target: that would create false horizon returns.
        for hours in HORIZONS:
            # Revisit all matured unresolved snapshots: outages must not make
            # valid observations permanently ineligible for later backfill.
            mature=(now-dt.timedelta(hours=hours)).isoformat()
            pending=con.execute("""SELECT s.run_at,s.pair,s.price FROM snapshots s
                WHERE s.run_at<=?
                AND NOT EXISTS (SELECT 1 FROM outcomes o WHERE o.run_at=s.run_at
                AND o.pair=s.pair AND o.horizon_hours=?)""",(mature,hours)).fetchall()
            for run_at,pair,price in pending:
                target=(dt.datetime.fromisoformat(run_at)+dt.timedelta(hours=hours)).isoformat()
                deadline=(dt.datetime.fromisoformat(run_at)+dt.timedelta(hours=hours+1)).isoformat()
                observed=con.execute("""SELECT run_at,price FROM market_observations
                    WHERE pair=? AND run_at>=? AND run_at<? ORDER BY run_at LIMIT 1""",(pair,target,deadline)).fetchone()
                if observed is None: continue
                observed_at,observed_price=observed
                ret=100*(observed_price/price-1)
                con.execute("INSERT OR IGNORE INTO outcomes VALUES (?,?,?,?,?)", (run_at,pair,hours,observed_at,round(ret,4)))
    assert con.execute("PRAGMA integrity_check").fetchone()[0] == "ok"
    n = con.execute("SELECT COUNT(*) FROM snapshots").fetchone()[0]
    outcomes = con.execute("SELECT COUNT(*) FROM outcomes").fetchone()[0]
    feature_rows=con.execute("SELECT COUNT(*) FROM candidate_features").fetchone()[0]
    market_observations=con.execute("SELECT COUNT(*) FROM market_observations").fetchone()[0]
    unresolved=con.execute("""SELECT COUNT(*) FROM snapshots s WHERE s.run_at<=?
      AND NOT EXISTS (SELECT 1 FROM outcomes o WHERE o.run_at=s.run_at AND o.pair=s.pair AND o.horizon_hours=1)""",((now-dt.timedelta(hours=1)).isoformat(),)).fetchone()[0]
    # LEAD uses the next observed scan, not the maximum future price. A 90-minute
    # gap is excluded: long outages must not masquerade as intrahour breakouts.
    missed_rows=con.execute("""WITH observations AS (
      SELECT pair,run_at,price,
        LEAD(run_at) OVER (PARTITION BY pair ORDER BY run_at) AS next_at,
        LEAD(price) OVER (PARTITION BY pair ORDER BY run_at) AS next_price
      FROM market_observations WHERE run_at>=?)
      SELECT o.pair,o.run_at,ROUND(100*(o.next_price/o.price-1),2)
      FROM observations o
      WHERE o.next_price>=o.price*1.05
        AND (julianday(o.next_at)-julianday(o.run_at))*1440 BETWEEN 0 AND 90
        AND NOT EXISTS (SELECT 1 FROM snapshots s WHERE s.run_at=o.run_at AND s.pair=o.pair)
      ORDER BY (o.next_price/o.price) DESC""",((now-dt.timedelta(days=7)).isoformat(),)).fetchall()
    missed=len(missed_rows)
    missed_examples=missed_rows[:10]
    evaluated_outcomes=con.execute("SELECT COUNT(*) FROM outcomes").fetchone()[0]
    winning_outcomes=con.execute("SELECT COUNT(*) FROM outcomes WHERE return_pct>0").fetchone()[0]
    avg_return=con.execute("SELECT ROUND(AVG(return_pct),3) FROM outcomes").fetchone()[0]
    comparison=con.execute("""SELECT o.horizon_hours,COUNT(*),
      ROUND(AVG(CASE WHEN f.early_signal_score IS NOT NULL THEN o.return_pct END),3),
      ROUND(AVG(o.return_pct),3),
      ROUND(AVG(CASE WHEN f.early_signal_score IS NOT NULL AND f.early_signal_score>f.base_score THEN o.return_pct END),3)
      FROM outcomes o JOIN candidate_features f ON o.run_at=f.run_at AND o.pair=f.pair
      GROUP BY o.horizon_hours ORDER BY o.horizon_hours""").fetchall()
    # Historical association only; different scores were applied to the same selected cohort.
    # This is not a randomized or out-of-sample comparison and cannot approve trading.
    rank_shift=con.execute("""SELECT COUNT(*),ROUND(AVG(f.base_rank-f.research_rank),2) FROM candidate_features f WHERE f.base_rank IS NOT NULL AND f.research_rank IS NOT NULL""").fetchone()
    promoted=sum(1 for c in report["watch"] if c.get("status")=="WATCH_RESEARCH_ONLY" and c.get("base_rank",0)>12)
    outcome_lags=con.execute("""SELECT horizon_hours,COUNT(*),ROUND(AVG((julianday(evaluated_at)-julianday(run_at))*24-horizon_hours),3) FROM outcomes GROUP BY horizon_hours ORDER BY horizon_hours""").fetchall()
    # Coverage is measured only for snapshots old enough to have matured.
    horizon_coverage=[]
    for hours in HORIZONS:
        mature=(now-dt.timedelta(hours=hours)).isoformat()
        eligible_count=con.execute("SELECT COUNT(*) FROM snapshots WHERE run_at<=?",(mature,)).fetchone()[0]
        evaluated_count=con.execute("SELECT COUNT(*) FROM outcomes WHERE horizon_hours=?",(hours,)).fetchone()[0]
        horizon_coverage.append({"hours":hours,"matured_snapshots":eligible_count,"evaluated":evaluated_count,"coverage_pct":round(100*evaluated_count/eligible_count,1) if eligible_count else None})
    summary = {"forward_horizon_coverage":horizon_coverage,"outcome_lag_hours_by_horizon":[{"hours":h,"samples":n,"average_delay_hours":lag} for h,n,lag in outcome_lags],"unresolved_1h_snapshots":unresolved,"rank_comparison":{"historical_ranked_samples":rank_shift[0],"mean_base_minus_early_rank":rank_shift[1]},"newly_discovered_outside_base_top12":promoted,"signal_outcomes_by_horizon":[{"hours":h,"samples":n,"early_scored_avg_return_pct":e,"all_selected_avg_return_pct":a,"early_score_above_base_avg_return_pct":b} for h,n,e,a,b in comparison],"outcome_evaluation_coverage":{"evaluated":evaluated_outcomes,"positive":winning_outcomes,"average_return_pct":avg_return},"missed_breakout_examples":[{"pair":p,"observed_at":t,"next_scan_gain_pct":g} for p,t,g in missed_examples],"unselected_gainers_5pct_observations":missed,"market_observations":market_observations,"market_price_coverage":len(report.get("market_prices",{})),"feature_rows":feature_rows,"snapshots":n,"outcomes":outcomes,"history_db_integrity":"ok","evaluation":"FULL_MARKET_PRICE_FORWARD_PENDING_HORIZON_COVERAGE" if report.get("market_prices") else "INCOMPLETE_WATCHLIST_ONLY","model_updates":"DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION","buy_approved":False}
    (DB.parent / "learning.json").write_text(json.dumps(summary,indent=2))
    print("HISTORY_PERSISTED",json.dumps(summary))
    con.close()

if __name__ == "__main__": persist()
