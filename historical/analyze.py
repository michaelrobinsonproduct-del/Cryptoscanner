"""Historical Kraken archive analysis; retrospective, selection-biased research only."""
import collections,datetime as dt,json,math,pathlib,statistics,sys
source=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else "historical/output/research_training.ndjson")
out=pathlib.Path(sys.argv[2] if len(sys.argv)>2 else "historical/output/model.json")
# Backfill sampled all >=10% future movers but only sparse nonmovers.
# Consequently: NO calibrated probabilities, and NO absolute hit-rate claims.
rows=[]
for line in source.open():
    x=json.loads(line)
    if not all(x.get(k) is not None for k in ("pre_return_60m_pct","volume_accel","trade_accel","volatility_pct","max_forward_return_pct")):continue
    if not math.isfinite(float(x["volume_accel"])) or not math.isfinite(float(x["trade_accel"])):continue
    rows.append(x)
if len(rows)<1000:raise SystemExit("Insufficient historical rows")
rows.sort(key=lambda x:x["anchor_at"])
cut=rows[int(len(rows)*.8)]["anchor_at"]
train=[r for r in rows if r["anchor_at"]<cut]
test=[r for r in rows if r["anchor_at"]>=cut]
if len(train)<500 or len(test)<100:raise SystemExit("Insufficient chronological holdout")
rules={
 "early_1h":lambda r: abs(r["pre_return_60m_pct"])<=3,
 "volume_2x":lambda r:r["volume_accel"]>=2,
 "trades_2x":lambda r:r["trade_accel"]>=2,
 "early_volume":lambda r:abs(r["pre_return_60m_pct"])<=3 and r["volume_accel"]>=2,
 "early_trades":lambda r:abs(r["pre_return_60m_pct"])<=3 and r["trade_accel"]>=2,
 "volume_trades":lambda r:r["volume_accel"]>=2 and r["trade_accel"]>=2,
}
def stats(data,pred):
    subset=[r for r in data if pred(r)]
    positives=sum(r["max_forward_return_pct"]>=20 for r in subset)
    return {"rows":len(subset),"major_movers":positives,"sampled_positive_rate":round(positives/len(subset),5) if subset else None}
base_train=stats(train,lambda r:True);base_test=stats(test,lambda r:True)
results={}
for name,rule in rules.items():
    a,b=stats(train,rule),stats(test,rule)
    lift=(b["sampled_positive_rate"]/base_test["sampled_positive_rate"] if b["sampled_positive_rate"] is not None and base_test["sampled_positive_rate"] else 0)
    # A conservative fixed bonus only for patterns with positive out-of-time evidence.
    eligible=a["rows"]>=100 and b["rows"]>=50 and lift>=1.15 and a["sampled_positive_rate"]>base_train["sampled_positive_rate"]
    results[name]={"train":a,"holdout":b,"holdout_relative_lift":round(lift,3),"eligible":eligible}
model={"schema_version":1,"source":"Kraken 2026Q2 5m archive; historical/backfill.py","trained_at":dt.datetime.now(dt.timezone.utc).isoformat(),
"train_rows":len(train),"holdout_rows":len(test),"holdout_start":cut,"baseline_train":base_train,"baseline_holdout":base_test,
"rules":results,"approved_rules":[k for k,v in results.items() if v["eligible"]],
"limitations":["Backfill oversamples future >=10% movers: positive rates are NOT market probabilities",
"Overlapping anchors are correlated; holdout is chronological, not independent episodes",
"Archive ends June 2026; regime shift possible","No historical order-book or executable entry evidence",
"Research bonuses are bounded and never authorize buys"]}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(model,indent=2)+"\n")
print(json.dumps({"rows":len(rows),"holdout":len(test),"approved_rules":model["approved_rules"],"out":str(out)}))
