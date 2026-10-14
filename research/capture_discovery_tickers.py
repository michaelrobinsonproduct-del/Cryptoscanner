"""Capture independent Kraken ticker data for research gate attribution.

Read-only public Kraken endpoints; no production scanner calls or database writes.
Writes a local JSON artifact only. Never places this snapshot in production.
"""
import argparse
import datetime as dt
import json
import math
import urllib.request
from pathlib import Path
from research.discovery_gate_attribution import summarize

ROOT="https://api.kraken.com/0/public/"
def fetch(endpoint):
    req=urllib.request.Request(ROOT+endpoint,headers={"User-Agent":"KrakenDiscoveryResearch/1.0"})
    with urllib.request.urlopen(req,timeout=35) as response: data=json.load(response)
    if data.get("error"):raise RuntimeError(str(data["error"]))
    return data["result"]

def collect():
    pairs=fetch("AssetPairs")
    eligible={k:v for k,v in pairs.items() if v.get("status")=="online"
      and v.get("wsname","").endswith("/USD")
      and v.get("base","").upper() not in {"ZUSD","USD","USDT","USDC","DAI","PYUSD","EURC","RLUSD","TUSD"}}
    ticker=fetch("Ticker")
    records={}
    for pair in eligible:
        t=ticker.get(pair)
        if not t:continue
        try:
            records[pair]={"last":float(t["c"][0]),"bid":float(t["b"][0]),
              "ask":float(t["a"][0]),"open":float(t["o"]),"volume24":float(t["v"][1])}
        except (ValueError,TypeError,KeyError,IndexError):
            records[pair]={"invalid":True}
    if len(records)<max(50,int(len(eligible)*.8)):
        raise RuntimeError("Insufficient ticker coverage; refusing incomplete snapshot")
    return {"captured_at":dt.datetime.now(dt.timezone.utc).isoformat(),
      "universe":len(eligible),"matched":len(records),"records":records,
      "attribution":summarize(records)}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="discovery-ticker-snapshot.json")
    args=p.parse_args()
    data=collect()
    target=Path(args.output)
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(data,indent=2),encoding="utf-8")
    print(json.dumps({"captured_at":data["captured_at"],"universe":data["universe"],
      "matched":data["matched"],"reason_counts":data["attribution"]["reason_counts"],
      "output":str(target),"mode":"RESEARCH_ONLY"},sort_keys=True))
