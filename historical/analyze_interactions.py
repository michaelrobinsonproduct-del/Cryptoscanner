"""Pre-surge interaction discovery on representative control anchors only.

Do not train on outcome-selected winner windows. Report evidence, not guaranteed returns.
Use distinct pair-days as the unit of analysis to reduce overlapping-window inflation.
"""
import collections,datetime as dt,itertools,json,math,pathlib,sys
src=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else "historical/output/research_training.ndjson")
dst=pathlib.Path(sys.argv[2] if len(sys.argv)>2 else "historical/output/interaction_model.json")
# All predicates must be measurable at anchor time. Signals describe combinations, not hindsight.
def features(r):
    p5=r["pre_return_5m_pct"];p15=r["pre_return_15m_pct"];p60=r["pre_return_60m_pct"]
    v=r["volume_accel"];t=r["trade_accel"];z=r["volatility_pct"]
    return {
      "early":abs(p60)<=3,
      "quiet_15m":abs(p15)<=1.5,
      "rising_15m":0.1<=p15<=2,
      "positive_5m":0<p5<=1.5,
      "volume_accel_1_5x":v>=1.5,
      "volume_accel_2x":v>=2,
      "trades_accel_1_5x":t>=1.5,
      "trades_accel_2x":t>=2,
      "trade_leads_volume":t>=1.5 and t>v*1.25,
      "volume_leads_trades":v>=1.5 and v>t*1.25,
      "compression":z<=0.6,
      "volatility_expansion":z>=1.5,
      "controlled_breakout":0.3<=p60<=3,
      "not_extended":abs(p60)<=5,
    }
# Select one systematically sampled anchor per pair-day, without looking at the label.
# Never use positive-oversampled anchors as controls.
daily={}
total=0;controls=0
for line in src.open():
    r=json.loads(line);total+=1
    if not r.get("control_sampled",False):continue
    controls+=1
    keys=("pre_return_5m_pct","pre_return_15m_pct","pre_return_60m_pct","volume_accel","trade_accel","volatility_pct","max_forward_return_pct")
    if any(r.get(k) is None for k in keys):continue
    if not all(math.isfinite(float(r[k])) for k in keys):continue
    day=r["anchor_at"][:10];key=(r["pair"],day)
    # Choose earliest control anchor deterministically (no outcome selection).
    if key not in daily or r["anchor_at"]<daily[key]["anchor_at"]:daily[key]=r
if controls<1000 or len(daily)<1000:
    raise SystemExit("UNBIASED_CONTROLS_MISSING: historical artifact does not preserve enough systematic control anchors; regenerate backfill, do not fit biased data")
# Chronological train / validation / final untouched test; avoid tuning on test.
splits={"train":[],"validation":[],"test":[]}
for r in daily.values():
    day=r["anchor_at"][:10]
    split="train" if day<"2026-03-01" else ("validation" if day<"2026-05-01" else "test")
    splits[split].append(r)
if min(map(len,splits.values()))<200:
    raise SystemExit("INSUFFICIENT_CHRONOLOGICAL_SPLITS: rebuild representative history")
feature_names=list(features(next(iter(daily.values()))))
# Restrict to meaningful 2- and 3-way interactions; no hundreds of uncorrected fishing tests.
combos=[]
for n in (2,3):
    combos.extend(itertools.combinations(feature_names,n))
def measure(rows,combo):
    subset=[r for r in rows if all(features(r)[f] for f in combo)]
    n=len(subset)
    wins=sum(r["max_forward_return_pct"]>=20 for r in subset)
    return {"n":n,"hits":wins,"rate":round(wins/n,5) if n else None,
            "pairs":len({r["pair"] for r in subset})}
def base(rows):return measure(rows,())
baselines={k:base(v) for k,v in splits.items()}
# Discovery on train, confirmation on validation, evaluation once on untouched test.
eligible=[]
for combo in combos:
    a=measure(splits["train"],combo)
    b=measure(splits["validation"],combo)
    if a["n"]<80 or b["n"]<40 or a["pairs"]<15 or b["pairs"]<10:continue
    tr=baselines["train"]["rate"];vr=baselines["validation"]["rate"]
    if not tr or not vr:continue
    if a["rate"]<tr*1.3 or b["rate"]<vr*1.2:continue
    eligible.append({"signals":list(combo),"train":a,"validation":b,
        "validation_lift":round(b["rate"]/vr,3)})
eligible.sort(key=lambda x:(-x["validation_lift"],-x["validation"]["n"]))
# Freeze selected rules before evaluating test.
for rule in eligible[:12]:
    m=measure(splits["test"],rule["signals"])
    rule["test"]=m
    rule["test_lift"]=round(m["rate"]/baselines["test"]["rate"],3) if m["rate"] is not None and baselines["test"]["rate"] else None
    rule["approved"]=m["n"]>=40 and m["pairs"]>=10 and m["hits"]>=8 and rule["test_lift"]>=1.2
model={"schema_version":2,"generated_at":dt.datetime.now(dt.timezone.utc).isoformat(),
 "source":"systematically sampled control anchors from Kraken historical 5m bars",
 "raw_rows":total,"control_rows":controls,"unique_pair_days":len(daily),
 "splits":{k:{"rows":len(v),"baseline":baselines[k]} for k,v in splits.items()},
 "tested_combinations":len(combos),"candidate_rules":eligible[:12],
 "approved_rules":[x["signals"] for x in eligible[:12] if x["approved"]],
 "caveats":["20% max forward return in 24h is not an executable profit",
 "Pair-day observations remain dependent across days and regimes",
 "No historical order-book data; live execution confirmation mandatory",
 "This is a screened exploratory study; prospective lift must still be measured"]}
dst.parent.mkdir(parents=True,exist_ok=True)
dst.write_text(json.dumps(model,indent=2)+"\n")
print(json.dumps({"raw":total,"controls":controls,"pair_days":len(daily),
 "baseline":baselines,"combinations":len(combos),"validated":len(eligible[:12]),
 "approved":len(model["approved_rules"])}))
