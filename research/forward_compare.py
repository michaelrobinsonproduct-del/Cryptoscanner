"""Read-only forward observation comparison for research lane.

Store a bounded JSON state as a workflow artifact; no database, live signals or trade approval.
Subsequent runs may pass the previous state to evaluate observed forward returns.
"""
import argparse,json,datetime as dt
from research.shadow_momentum_lane import evaluate

def compare(previous,current):
    old=previous["snapshot"];new=current
    old_t=dt.datetime.fromisoformat(old["captured_at"])
    new_t=dt.datetime.fromisoformat(new["captured_at"])
    minutes=(new_t-old_t).total_seconds()/60
    if not 10<=minutes<=120:raise ValueError("Snapshots must be 10–120 minutes apart")
    lane=evaluate(old)
    result={"mode":"OFFLINE_FORWARD_RESEARCH","elapsed_minutes":round(minutes,1),
        "baseline":[],"shadow":[],"trade_approval":False}
    for group,key in (("baseline","baseline_pairs"),("shadow","shadow_pairs")):
        for pair in lane[key]:
            a=old["records"].get(pair);b=new["records"].get(pair)
            if not a or not b:continue
            p=float(a["last"]);q=float(b["last"])
            if p<=0 or q<=0:continue
            result[group].append({"pair":pair,"forward_pct":round(100*(q/p-1),3),
                "breakout_5pct":q/p>=1.05})
    for group in ("baseline","shadow"):
        vals=result[group]
        result[group+"_summary"]={"matched":len(vals),"breakouts_5pct":sum(v["breakout_5pct"] for v in vals),
            "mean_forward_pct":round(sum(v["forward_pct"] for v in vals)/len(vals),3) if vals else None}
    result["caveat"]="Observational comparison only; selection bias and limited horizon; not trading validation"
    return result

if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("previous");p.add_argument("current");p.add_argument("--output",default="discovery-forward-comparison.json")
    a=p.parse_args()
    with open(a.previous) as f:prev=json.load(f)
    with open(a.current) as f:curr=json.load(f)
    r=compare(prev,curr)
    with open(a.output,"w") as f:json.dump(r,f,indent=2)
    print(json.dumps({k:v for k,v in r.items() if k not in ("baseline","shadow")},sort_keys=True))
