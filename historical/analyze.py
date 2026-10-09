"""Stream historical Kraken archive research with chronological holdout.
Backfill oversampled future movers: no calibrated probabilities or trading claims.
"""
import datetime as dt,json,math,pathlib,sys
source=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else "historical/output/research_training.ndjson")
out=pathlib.Path(sys.argv[2] if len(sys.argv)>2 else "historical/output/model.json")
cut="2026-05-01"
rules={
 "early_1h":lambda r:abs(r["pre_return_60m_pct"])<=3,
 "volume_2x":lambda r:r["volume_accel"]>=2,
 "trades_2x":lambda r:r["trade_accel"]>=2,
 "early_volume":lambda r:abs(r["pre_return_60m_pct"])<=3 and r["volume_accel"]>=2,
 "early_trades":lambda r:abs(r["pre_return_60m_pct"])<=3 and r["trade_accel"]>=2,
 "volume_trades":lambda r:r["volume_accel"]>=2 and r["trade_accel"]>=2,
}
counts={split:{name:{"rows":0,"major_movers":0} for name in ["baseline",*rules]} for split in ("train","holdout")}
for line in source.open():
    r=json.loads(line)
    # Only systematic controls provide an unbiased market-wide denominator.
    if not r.get("control_sampled",False):continue
    keys=("pre_return_60m_pct","volume_accel","trade_accel","max_forward_return_pct")
    if any(r.get(k) is None for k in keys):continue
    if not all(math.isfinite(float(r[k])) for k in keys):continue
    split="train" if r["anchor_at"][:10]<cut else "holdout"
    selected=["baseline"]+[name for name,pred in rules.items() if pred(r)]
    for name in selected:
        counts[split][name]["rows"]+=1
        counts[split][name]["major_movers"]+=int(r["max_forward_return_pct"]>=20)
def summary(split,name):
    v=counts[split][name];n=v["rows"]
    return {**v,"sampled_positive_rate":round(v["major_movers"]/n,5) if n else None}
train=summary("train","baseline");holdout=summary("holdout","baseline")
if train["rows"]<500 or holdout["rows"]<100:raise SystemExit("Insufficient historical train or holdout data")
results={}
for name in rules:
    a,b=summary("train",name),summary("holdout",name)
    lift=b["sampled_positive_rate"]/holdout["sampled_positive_rate"] if b["sampled_positive_rate"] is not None and holdout["sampled_positive_rate"] else 0
    eligible=a["rows"]>=100 and b["rows"]>=50 and lift>=1.15 and a["sampled_positive_rate"]>train["sampled_positive_rate"]
    results[name]={"train":a,"holdout":b,"holdout_relative_lift":round(lift,3),"eligible":eligible}
model={"schema_version":1,"source":"Kraken 2026Q2 5m archive; historical/backfill.py",
"trained_at":dt.datetime.now(dt.timezone.utc).isoformat(),"train_rows":train["rows"],
"holdout_rows":holdout["rows"],"holdout_start":cut,"baseline_train":train,"baseline_holdout":holdout,
"rules":results,"approved_rules":[k for k,v in results.items() if v["eligible"]],
"limitations":["Only systematic weekly/hourly controls used; temporal overlap and sampling variance remain",
"Overlapping anchors are correlated; holdout is chronological, not independent episodes",
"Archive ends June 2026; regime shift possible","No historical order-book or executable entry evidence",
"Research bonuses are bounded and never authorize buys"]}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(model,indent=2)+"\n")
print(json.dumps({"train_rows":train["rows"],"holdout_rows":holdout["rows"],
"approved_rules":model["approved_rules"],"out":str(out)}))
