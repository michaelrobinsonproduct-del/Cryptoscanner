"""Read-only, deterministic audit of missed breakouts and preselection gates.

Does not modify scanner output, rankings, live weights, or database.
"""
import argparse
import datetime as dt
import json
import sqlite3
from collections import Counter

def audit(path, days=7):
    con=sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    try:
        assert con.execute("PRAGMA integrity_check").fetchone()[0]=="ok"
        cutoff=(dt.datetime.now(dt.timezone.utc)-dt.timedelta(days=days)).isoformat()
        rows=con.execute("""WITH ticks AS (
          SELECT pair,run_at,price,
                 LEAD(run_at) OVER (PARTITION BY pair ORDER BY run_at) next_at,
                 LEAD(price) OVER (PARTITION BY pair ORDER BY run_at) next_price
          FROM market_observations WHERE run_at>=?
        ) SELECT t.pair,t.run_at,ROUND(100*(t.next_price/t.price-1),2),
                 CASE WHEN s.pair IS NOT NULL THEN 1 ELSE 0 END selected,
                 CASE WHEN f.pair IS NOT NULL THEN 1 ELSE 0 END has_features
          FROM ticks t
          LEFT JOIN snapshots s ON s.run_at=t.run_at AND s.pair=t.pair
          LEFT JOIN candidate_features f ON f.run_at=t.run_at AND f.pair=t.pair
          WHERE t.next_price>=t.price*1.05
            AND (julianday(t.next_at)-julianday(t.run_at))*1440 BETWEEN 0 AND 90
          ORDER BY t.run_at,t.pair""",(cutoff,)).fetchall()
        missed=[r for r in rows if not r[3]]
        # Cannot determine the exact preselection gate from market_prices alone.
        # Gate classification requires per-pair daily-open, spread and notional
        # values, which the current scanner does not persist for excluded pairs.
        return {"status":"READ_ONLY_DIAGNOSTIC","window_days":days,
                "breakout_observations":len(rows),"not_on_watch":len(missed),
                "on_watch":len(rows)-len(missed),
                "unique_missed_pairs":len({r[0] for r in missed}),
                "missing_candidate_features":sum(not r[4] for r in missed),
                "top_missed":[{"pair":p,"observed_at":t,"next_scan_gain_pct":gain}
                              for p,t,gain,*_ in sorted(missed,key=lambda r:r[2],reverse=True)[:10]],
                "gate_attribution":"UNAVAILABLE_FROM_RECORDED_DATA",
                "caveat":"Next observation can be up to 90 minutes later; no pre-breakout execution guarantee"}
    finally:con.close()

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("database")
    parser.add_argument("--days",type=int,default=7)
    args=parser.parse_args()
    if args.days<1 or args.days>90:parser.error("days must be between 1 and 90")
    print(json.dumps(audit(args.database,args.days),indent=2))
