"""Offline market-wide breakout recall evaluation from point-in-time observations.

This computes a baseline recall measure; it does not claim challenger improvement.
No production scanner imports this module.
"""
import sqlite3
from pathlib import Path

def baseline_recall(db_path, *, min_gain_pct=5.0, max_gap_minutes=90):
    con=sqlite3.connect(f"file:{Path(db_path).resolve()}?mode=ro",uri=True)
    try:
        rows=con.execute("""WITH pairs AS (
          SELECT pair,run_at,price,
            LEAD(run_at) OVER (PARTITION BY pair ORDER BY run_at) AS next_at,
            LEAD(price) OVER (PARTITION BY pair ORDER BY run_at) AS next_price
          FROM market_observations
        )
        SELECT p.pair,p.run_at,
          100.0*(p.next_price/p.price-1.0) AS gain,
          EXISTS(SELECT 1 FROM snapshots s WHERE s.run_at=p.run_at AND s.pair=p.pair)
        FROM pairs p
        WHERE p.price>0 AND p.next_price IS NOT NULL
          AND (julianday(p.next_at)-julianday(p.run_at))*1440 BETWEEN 0 AND ?
          AND p.next_price>=p.price*(1+?/100.0)
        ORDER BY p.run_at,p.pair""",(max_gap_minutes,min_gain_pct)).fetchall()
        total=len(rows)
        caught=sum(int(r[3]) for r in rows)
        return {"status":"MEASURED","scope":"FULL_MARKET_PRICE_OBSERVATIONS",
                "metric":"next_observation_gain","gain_threshold_pct":min_gain_pct,
                "max_gap_minutes":max_gap_minutes,
                "breakouts":total,"caught":caught,"missed":total-caught,
                "recall":caught/total if total else None,
                "challenger_recall":None,"promotion_eligible":False}
    finally:
        con.close()
