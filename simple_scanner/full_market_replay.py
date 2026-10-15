"""Offline full-market feature replay from recorded point-in-time observations.

Uses only past observations; never touches live rankings or trading approvals.
Historical price-only replay is diagnostic, not proof of production feature parity.
"""
import math
import sqlite3
from pathlib import Path

def replay(db_path, *, gain_threshold_pct=5, max_gap_minutes=90):
    con=sqlite3.connect(f"file:{Path(db_path).resolve()}?mode=ro",uri=True)
    try:
        rows=con.execute("""SELECT pair,run_at,price FROM market_observations
            WHERE price>0 ORDER BY pair,run_at""").fetchall()
        selected=set(con.execute("SELECT run_at,pair FROM snapshots").fetchall())
    finally:
        con.close()
    from datetime import datetime
    by_pair={}
    for pair,t,price in rows:
        if isinstance(price,(int,float)) and math.isfinite(price) and price>0:
            by_pair.setdefault(pair,[]).append((datetime.fromisoformat(t),t,price))
    events=[]
    for pair,series in by_pair.items():
        for i in range(1,len(series)-1):
            previous,current,future=series[i-1],series[i],series[i+1]
            age=(current[0]-previous[0]).total_seconds()/60
            gap=(future[0]-current[0]).total_seconds()/60
            if not (0<age<=max_gap_minutes and 0<gap<=max_gap_minutes):
                continue
            prior_momentum=100*(current[2]/previous[2]-1)
            gain=100*(future[2]/current[2]-1)
            events.append({"pair":pair,"run_at":current[1],
                "prior_momentum_pct":round(prior_momentum,6),
                "future_gain_pct":round(gain,6),
                "breakout":gain>=gain_threshold_pct,
                "baseline_selected":(current[1],pair) in selected})
    return {"status":"REPLAY_DIAGNOSTIC","scope":"FULL_MARKET_PRICES_ONLY",
            "feature_parity_verified":False,"promotion_eligible":False,
            "events":events}
