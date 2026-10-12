"""Independent, read-only DEX research discovery; never approves buys."""
import datetime as dt
import json
import os
import urllib.parse
import urllib.request
import time
from pathlib import Path

API="https://api.dexscreener.com/latest/dex/search/?q="
QUERIES=("solana","base","ethereum")
def fetch(query):
    req=urllib.request.Request(API+urllib.parse.quote(query),headers={"User-Agent":"SimpleScannerResearch/1.0"})
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req,timeout=15) as response:
                return json.load(response)
        except Exception:
            if attempt==1: raise
            time.sleep(2**attempt)

def main():
    candidates={}
    errors=[]
    for query in QUERIES:
        try:
            for pair in fetch(query).get("pairs") or []:
                if not isinstance(pair,dict):continue
                chain=str(pair.get("chainId") or "")
                if chain not in ("solana","base","ethereum"):continue
                liquidity=float((pair.get("liquidity") or {}).get("usd") or 0)
                volume=float((pair.get("volume") or {}).get("h24") or 0)
                age=pair.get("pairCreatedAt")
                address=pair.get("pairAddress")
                if not address or liquidity<25000 or volume<100000:continue
                key=chain+":"+address
                candidates[key]={"chain":chain,"pair_address":address,"symbol":str((pair.get("baseToken") or {}).get("symbol") or ""),"liquidity_usd":liquidity,"volume_24h_usd":volume,"price_change_1h_pct":(pair.get("priceChange") or {}).get("h1"),"created_at_ms":age,"status":"DEX_RESEARCH_UNVERIFIED"}
        except Exception as exc:errors.append({"query":query,"error":str(exc)})
    if len(errors)==len(QUERIES):
        print("DEX_SOURCE_ERRORS "+json.dumps(errors),flush=True)
        raise RuntimeError("All DEX discovery sources failed")
    report={"observed_at":dt.datetime.now(dt.timezone.utc).isoformat(),"source":"dexscreener_public_search","scope":"sampled_search_not_full_dex_universe","buy_approved":False,"candidates":sorted(candidates.values(),key=lambda x:x["volume_24h_usd"],reverse=True)[:30],"errors":errors}
    directory=Path(os.getenv("SIMPLE_SCANNER_DATA_DIR","simple_scanner/output"))
    directory.mkdir(parents=True,exist_ok=True)
    (directory/"dex_latest.json").write_text(json.dumps(report,indent=2))
    print("DEX_SUMMARY "+json.dumps({"observed_at":report["observed_at"],"candidates":len(report["candidates"]),"errors":len(errors),"buy_approved":False}),flush=True)
if __name__=="__main__":main()
