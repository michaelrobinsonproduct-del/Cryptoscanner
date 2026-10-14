"""Read-only historical check for risk-related signals. Never alters scanner or DB."""
import json, sqlite3, sys
from collections import defaultdict
from pathlib import Path

def evaluate(path):
    con=sqlite3.connect("file:"+str(Path(path).resolve())+"?mode=ro",uri=True)
    try:
        rows=con.execute("""SELECT f.run_at,f.pair,f.move_15m_pct,f.volume_accel,o.return_pct
        FROM candidate_features f JOIN outcomes o
        ON f.run_at=o.run_at AND f.pair=o.pair
        WHERE o.horizon_hours=1 ORDER BY f.run_at,f.pair""").fetchall()
    finally:
        con.close()
    signals=defaultdict(list)
    for run_at,pair,momentum,volume,ret in rows:
        if momentum is not None and momentum<0:
            signals["NEGATIVE_15M_MOMENTUM"].append(ret)
        if volume is not None and volume>4:
            signals["VOLUME_SPIKE_REVIEW"].append(ret)
    return {"mode":"SHADOW_READ_ONLY","observations":len(rows),
            "cohorts":len(set(r[0] for r in rows)),"outcome_horizon_hours":1,
            "partial_signal_outcomes":{k:{"samples":len(v),"average_return_pct":round(sum(v)/len(v),4)}
                for k,v in sorted(signals.items())},
            "full_risk_validation_possible":False,
            "reason":"Historical candidate_features does not persist spread_bps or notional_24h_usd",
            "buy_approved":False,"production_modified":False}

if __name__=="__main__":
    print(json.dumps(evaluate(sys.argv[1]),indent=2))
