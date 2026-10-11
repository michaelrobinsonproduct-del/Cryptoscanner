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
    con.execute("CREATE TABLE IF NOT EXISTS market_observations (run_at TEXT NOT NULL, pair TEXT NOT NULL, price REAL NOT NULL CHECK(price>0), PRIMARY KEY(run_at,pair))")
    con.execute("CREATE INDEX IF NOT EXISTS idx_market_pair_time ON market_observations(pair,run_at)")
    con.execute("CREATE TABLE IF NOT EXISTS outcomes (run_at TEXT NOT NULL, pair TEXT NOT NULL, horizon_hours INTEGER NOT NULL, evaluated_at TEXT NOT NULL, return_pct REAL NOT NULL, PRIMARY KEY(run_at,pair,horizon_hours))")
    now = dt.datetime.fromisoformat(report["completed_at"])
    assert now.tzinfo is not None and now.utcoffset() is not None, "Scan timestamp must be timezone-aware"
    with con:
        for pair,price in report.get("market_prices",{}).items():
            if isinstance(price,(int,float)) and price>0:
                con.execute("INSERT OR IGNORE INTO market_observations VALUES (?,?,?)",(report["completed_at"],pair,price))
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
    market_observations=con.execute("SELECT COUNT(*) FROM market_observations").fetchone()[0]
    # LEAD uses the next observed scan, not the maximum future price. A 90-minute
    # gap is excluded: long outages must not masquerade as intrahour breakouts.
    missed_rows=con.execute("""WITH observations AS (
      SELECT pair,run_at,price,
        LEAD(run_at) OVER (PARTITION BY pair ORDER BY run_at) AS next_at,
        LEAD(price) OVER (PARTITION BY pair ORDER BY run_at) AS next_price
      FROM market_observations)
      SELECT o.pair,o.run_at,ROUND(100*(o.next_price/o.price-1),2)
      FROM observations o
      WHERE o.next_price>=o.price*1.05
        AND (julianday(o.next_at)-julianday(o.run_at))*1440 BETWEEN 0 AND 90
        AND NOT EXISTS (SELECT 1 FROM snapshots s WHERE s.run_at=o.run_at AND s.pair=o.pair)
      ORDER BY (o.next_price/o.price) DESC""").fetchall()
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
    summary = {"signal_outcomes_by_horizon":[{"hours":h,"samples":n,"early_scored_avg_return_pct":e,"all_selected_avg_return_pct":a,"early_score_above_base_avg_return_pct":b} for h,n,e,a,b in comparison],"outcome_evaluation_coverage":{"evaluated":evaluated_outcomes,"positive":winning_outcomes,"average_return_pct":avg_return},"missed_breakout_examples":[{"pair":p,"observed_at":t,"next_scan_gain_pct":g} for p,t,g in missed_examples],"unselected_gainers_5pct_observations":missed,"market_observations":market_observations,"market_price_coverage":len(report.get("market_prices",{})),"feature_rows":feature_rows,"snapshots":n,"outcomes":outcomes,"history_db_integrity":"ok","evaluation":"FULL_MARKET_PRICE_FORWARD_PENDING_HORIZON_COVERAGE" if report.get("market_prices") else "INCOMPLETE_WATCHLIST_ONLY","model_updates":"DISABLED_PENDING_UNBIASED_FORWARD_VALIDATION","buy_approved":False}
    (DB.parent / "learning.json").write_text(json.dumps(summary,indent=2))
    print("HISTORY_PERSISTED",json.dumps(summary))
    con.close()

if __name__ == "__main__": persist()
