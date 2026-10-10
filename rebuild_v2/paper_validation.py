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
    # Lock the first decision at signal time, regardless of later outcome availability.
    first_decision={}
    # First observed outcome per coin/day is only a proxy, not a fill price.
    controls=[]
    entry_quotes={}
    for run_id,created,payload in rows:
        try:
            report=json.loads(payload)
            policy=report.get("paper_entry_research")
            if not isinstance(policy,dict):continue
            eligible={x["pair"] for x in policy.get("candidates",[]) if x.get("status")=="PAPER_ELIGIBLE"}
            if not eligible:continue
            watched={c["pair"] for c in report.get("watch",[])}
            controls_for_run=watched-eligible
            for pair in sorted(eligible | controls_for_run):
                key=(created[:10],pair)
                if key not in first_decision:
                    first_decision[key]=(run_id,"eligible" if pair in eligible else "control")
            quotes={q["pair"]:q for q in report.get("market_quotes",[]) if isinstance(q,dict) and "pair" in q}
            for pair in eligible | controls_for_run:
                if first_decision.get((created[:10],pair),(None,))[0]!=run_id:continue
                q=quotes.get(pair,{})
                bid,spread=q.get("bid"),q.get("spread_bps")
                if isinstance(bid,(int,float)) and bid>0 and isinstance(spread,(int,float)) and 0<=spread<=1000:
                    entry_quotes[(run_id,pair)]=bid*(1+spread/10000)
            for pair,ret,horizon in db.execute("""SELECT pair,return_pct,horizon_hours FROM outcomes
                WHERE run_id=? AND horizon_hours IN (1,4,24,72)""",(run_id,)):
                decision=first_decision.get((created[:10],pair))
                if decision is None or decision[0]!=run_id:continue
                if decision[1]=="eligible":
                    key=(created[:10],pair,horizon)
                    if key not in first_eligible:
                        first_eligible[key]=True
                        samples.append((created[:10],pair,horizon,ret))
                elif decision[1]=="control":
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
    for horizon in (1,4,24,72):
        key=str(horizon)+"h"
        for label,cohort in (("paper",samples),("control",controls)):
            returns=[]
            for day,pair,h,raw in cohort:
                if h!=horizon:continue
                rid=first_decision.get((day,pair),(None,))[0]
                ask=entry_quotes.get((rid,pair))
                if not ask:continue
                original=db.execute("SELECT price FROM observations WHERE run_id=? AND pair=?",(rid,pair)).fetchone()
                if not original or not original[0] or original[0]<=0:continue
                future_bid=original[0]*(1+raw/100)
                if future_bid>0:returns.append(future_bid/ask)
            result["metrics"][key][label+"_spread_samples"]=len(returns)
            for bps in (0,40,100):
                values=[100*(ratio*(1-bps/10000)-1) for ratio in returns]
                result["metrics"][key][label+"_net_"+str(bps)+"bps_mean_pct"]=round(sum(values)/len(values),3) if values else None
    result["execution_costs"]="Estimated entry ask from same-scan bid and spread; exit bid inferred from stored outcome; 0/40/100bps cost scenarios are hypothetical and exclude fill/depth uncertainty."
    result["first_decision_cohorts"]={"eligible":sum(v[1]=="eligible" for v in first_decision.values()),"control":sum(v[1]=="control" for v in first_decision.values())}
    result["selection_limitation"]="First observed watch decision per UTC coin-day is locked before outcome lookup; missing outcomes are excluded and reported as a coverage limitation"
    # No promotion without a prospective, out-of-sample evaluation with controls.
    return result

if __name__=="__main__":
    with sqlite3.connect(DB) as db: result=validate(db)
    REPORT.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result))
