"""Bounded research-only OHLC validation for the momentum shadow lane.

Fetch at most 12 shadow pairs; no production changes, no trade approvals.
"""
import argparse
import datetime as dt
import json
import math
import time
from research.capture_discovery_tickers import fetch
from research.shadow_momentum_lane import evaluate

def validate(snapshot,limit=12):
    if not 1<=limit<=12:raise ValueError("OHLC research cap is 12")
    lane=evaluate(snapshot)
    selected=lane["shadow_pairs"][:limit]
    output=[]
    now=dt.datetime.now(dt.timezone.utc).timestamp()
    for pair in selected:
        row={"pair":pair,"status":"UNVERIFIED"}
        try:
            candles=next(v for k,v in fetch("OHLC?pair="+pair+"&interval=5").items() if k!="last")[:-1]
            if len(candles)<13:raise ValueError("insufficient completed candles")
            age=now-float(candles[-1][0])
            if age<0 or age>900:raise ValueError("stale candles")
            close=[float(x[4]) for x in candles[-13:]]
            volume=[float(x[6]) for x in candles[-13:]]
            if not all(math.isfinite(x) and x>0 for x in close):raise ValueError("invalid close")
            if not all(math.isfinite(x) and x>=0 for x in volume):raise ValueError("invalid volume")
            row.update({"status":"VALIDATED","move_15m_pct":round(100*(close[-1]/close[-4]-1),2),
                "volume_accel":round(sum(volume[-6:])/max(sum(volume[-12:-6]),1e-9),2),
                "age_seconds":round(age)})
        except Exception as error:row["reason"]=str(error)
        output.append(row)
        time.sleep(.25)
    return {"mode":"RESEARCH_ONLY","requested":len(selected),
        "validated":sum(r["status"]=="VALIDATED" for r in output),
        "signals":output,"trade_approval":False,"forward_returns_tested":False,
        "note":"Alphabetical bounded sample; not representative and not a predictive backtest."}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("snapshot");p.add_argument("--output",default="discovery-shadow-ohlc.json")
    args=p.parse_args()
    with open(args.snapshot,encoding="utf-8") as f:snapshot=json.load(f)
    result=validate(snapshot)
    with open(args.output,"w",encoding="utf-8") as f:json.dump(result,f,indent=2)
    print(json.dumps({k:v for k,v in result.items() if k!="signals"},sort_keys=True))
