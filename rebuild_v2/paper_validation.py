"""Evaluate paper-eligible signals using strictly later, time-bounded observed outcomes."""
import json
import sqlite3
from pathlib import Path

DB=Path("rebuild_v2/output/history.sqlite3")
REPORT=Path("rebuild_v2/output/paper_validation.json")

def validate(db):
    # Only scans with published paper eligibility records are evaluated;
    # historic watch flags must not be relabeled as if the policy existed then.
    rows=db.execute("""SELECT r.id,r.created_at,r.payload FROM runs r ORDER BY r.created_at,r.id""").fetchall()
    samples=[]
    first_eligible={}
    first_control={}
    # First observed outcome per coin/day is only a proxy, not a fill price.
    controls=[]
    for run_id,created,payload in rows:
        try:
            report=json.loads(payload)
            policy=report.get("paper_entry_research")
            if not isinstance(policy,dict):continue
            eligible={x["pair"] for x in policy.get("candidates",[]) if x.get("status")=="PAPER_ELIGIBLE"}
            if not eligible:continue
            watched={c["pair"] for c in report.get("watch",[])}
            controls_for_run=watched-eligible
            for pair,ret,horizon in db.execute("""SELECT pair,return_pct,horizon_hours FROM outcomes
                WHERE run_id=? AND horizon_hours IN (1,4,24,72)""",(run_id,)):
                if pair in eligible:
                    key=(created[:10],pair,horizon)
                    if key not in first_eligible:
                        first_eligible[key]=True
                        samples.append((created[:10],pair,horizon,ret))
                elif pair in controls_for_run:
                    key=(created[:10],pair,horizon)
                    if key not in first_control:
                        first_control[key]=True
                        controls.append((created[:10],pair,horizon,ret))
        except (ValueError,TypeError,KeyError):continue
    result={"mode":"PAPER_ONLY","status":"INSUFFICIENT_FORWARD_DATA","validated":False,
            "observations":len(samples),"metrics":{}}
    for horizon in (1,4,24,72):
        # Deduplicate repeated scans: one observation per pair/day/horizon.
        unique={}
        for day,pair,h,ret in samples:
            if h==horizon:unique.setdefault((day,pair),ret)
        vals=list(unique.values())
        result["metrics"][str(horizon)+"h"]={"pair_days":len(vals),
            "mean_return_pct":round(sum(vals)/len(vals),3) if vals else None,
            "gain_5pct_rate":round(sum(v>=5 for v in vals)/len(vals),4) if vals else None,
            "loss_5pct_rate":round(sum(v<=-5 for v in vals)/len(vals),4) if vals else None}
    for horizon in (1,4,24,72):
        unique={}
        for day,pair,h,ret in controls:
            if h==horizon:unique.setdefault((day,pair),ret)
        vals=list(unique.values())
        result["metrics"][str(horizon)+"h"]["watch_control_pair_days"]=len(vals)
        result["metrics"][str(horizon)+"h"]["watch_control_mean_return_pct"]=round(sum(vals)/len(vals),3) if vals else None
    result["execution_costs"]="NOT_INCLUDED: fees, slippage, entry ask and fill uncertainty"
    result["selection_limitation"]="First labeled eligible outcome per coin/day/horizon; missing labels can bias the sample, so this is not yet a reproducible first-entry cohort"
    # No promotion without a prospective, out-of-sample evaluation with controls.
    return result

if __name__=="__main__":
    with sqlite3.connect(DB) as db: result=validate(db)
    REPORT.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result))
