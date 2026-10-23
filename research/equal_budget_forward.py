"""Read-only, equal-budget point-in-time candidate comparison.

Input JSONL records: {"run_at":"ISO8601","pair":"ABCUSD","baseline_score":1,
"challenger_score":2,"price":1,"spread_bps":10,"notional_usd":100000,
"outcomes":{"1":{"return_pct":1,"evaluated_at":"ISO8601"}, ...}}.
All scores and liquidity are required to be captured at run_at, not reconstructed
from later market observations. Missing future outcomes remain unevaluated.
"""
import argparse
import collections
import datetime as dt
import json

HORIZONS=(1,3,6,24)

def _time(value):
    t=dt.datetime.fromisoformat(value.replace("Z","+00:00"))
    if t.tzinfo is None:
        raise ValueError("timestamps must have timezone")
    return t.astimezone(dt.timezone.utc)

def compare(records, budget=12, min_notional=100000, max_spread_bps=75):
    if budget<1:
        raise ValueError("budget must be positive")
    cohorts=collections.defaultdict(list)
    for row in records:
        at=_time(row["run_at"])
        if not row.get("pair") or row["price"]<=0:
            raise ValueError("invalid observation")
        if row.get("features_observed_at") and _time(row["features_observed_at"])>at:
            raise ValueError("future features are forbidden")
        cohorts[row["run_at"]].append(row)
    totals={h:{side:{"selected":0,"matured":0,"hits20":0,"false_positives":0,"sum_return":0.0}
               for side in ("baseline","challenger")} for h in HORIZONS}
    for run_at,group in sorted(cohorts.items()):
        if len({r["pair"] for r in group})!=len(group):
            raise ValueError("duplicate pair in cohort")
        eligible=[r for r in group if r.get("notional_usd",0)>=min_notional
                  and 0<=r.get("spread_bps",float("inf"))<=max_spread_bps]
        for side in ("baseline","challenger"):
            selected=sorted(eligible,key=lambda r:(-r[side+"_score"],r["pair"]))[:budget]
            for h in HORIZONS:
                result=totals[h][side]
                result["selected"]+=len(selected)
                for r in selected:
                    outcome=r.get("outcomes",{}).get(str(h))
                    if not outcome:
                        continue
                    due=_time(run_at)+dt.timedelta(hours=h)
                    evaluated=_time(outcome["evaluated_at"])
                    if evaluated<due:
                        raise ValueError("outcome before maturity")
                    ret=float(outcome["return_pct"])
                    result["matured"]+=1
                    result["hits20"]+=ret>=20
                    result["false_positives"]+=ret<=0
                    result["sum_return"]+=ret
    for h in HORIZONS:
        for side in ("baseline","challenger"):
            m=totals[h][side]
            m["mean_matured_return_pct"]=round(m["sum_return"]/m["matured"],4) if m["matured"] else None
            del m["sum_return"]
    return {"status":"RESEARCH_ONLY","selection_budget":budget,"cohorts":len(cohorts),
            "horizons":totals,"limitations":["No full-market breakout recall without all-pair matured labels",
            "No tradability proof from notional/spread screening alone",
            "Equal selected budget does not guarantee equal matured sample coverage"],
            "promotion_eligible":False}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("jsonl")
    p.add_argument("--budget",type=int,default=12)
    args=p.parse_args()
    with open(args.jsonl,encoding="utf8") as f:
        print(json.dumps(compare([json.loads(x) for x in f if x.strip()],args.budget),indent=2))

if __name__=="__main__":
    main()
