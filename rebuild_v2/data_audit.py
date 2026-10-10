"""Audit historical scan quality without treating repeated outcomes as independent trades."""
import datetime as dt
import json
import sqlite3
from pathlib import Path

DB=Path("rebuild_v2/output/history.sqlite3")
OUT=Path("rebuild_v2/output/data_audit.json")

def audit(db):
    runs=db.execute("SELECT id,created_at,health,payload FROM runs ORDER BY created_at,id").fetchall()
    observations=db.execute("SELECT COUNT(*),COUNT(DISTINCT pair),COUNT(DISTINCT run_id) FROM observations").fetchone()
    outcomes=db.execute("SELECT horizon_hours,COUNT(*),COUNT(DISTINCT pair),COUNT(DISTINCT substr(run_id,1,10)||':'||pair) FROM outcomes GROUP BY horizon_hours ORDER BY horizon_hours").fetchall()
    invalid_times=0
    missing_quotes=0
    missing_confirmation=0
    healthy=0
    covered_days=set()
    for rid,stamp,state,payload in runs:
        try:
            t=dt.datetime.fromisoformat(stamp.replace("Z","+00:00"))
            covered_days.add(t.date().isoformat())
            r=json.loads(payload)
            if state=="COMPLETE":healthy+=1
            if not isinstance(r.get("market_quotes"),list):missing_quotes+=1
            if not isinstance(r.get("confirmations"),list):missing_confirmation+=1
        except (ValueError,TypeError,KeyError):
            invalid_times+=1
    return {"status":"AUDIT_ONLY","runs":len(runs),"complete_runs":healthy,
            "oldest":runs[0][1] if runs else None,"newest":runs[-1][1] if runs else None,
            "utc_days":len(covered_days),"observations":observations[0],
            "unique_pairs":observations[1],"observation_runs":observations[2],
            "outcome_horizons":[{"hours":h,"rows":n,"unique_pairs":p,"approx_pair_days":pd} for h,n,p,pd in outcomes],
            "invalid_run_timestamps_or_payloads":invalid_times,
            "runs_missing_market_quotes":missing_quotes,
            "runs_missing_confirmations":missing_confirmation,
            "caution":"Outcome rows overlap across runs and are not independent trading opportunities."}

if __name__=="__main__":
    with sqlite3.connect(DB) as db:r=audit(db)
    OUT.write_text(json.dumps(r,indent=2)+"\n")
    print(json.dumps(r))
