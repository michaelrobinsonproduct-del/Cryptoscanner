"""Isolated rebuild shadow scanner. Discovery only; never places orders."""
import json, datetime, urllib.request, urllib.parse
API="https://api.kraken.com/0/public/"
def api(method):
    req=urllib.request.Request(API+method,headers={"User-Agent":"kraken-shadow-rebuild/0.2","Cache-Control":"no-cache"})
    with urllib.request.urlopen(req,timeout=25) as resp: data=json.load(resp)
    if data.get("error"): raise RuntimeError(str(data["error"]))
    return data["result"]
def scan():
    ts=datetime.datetime.now(datetime.timezone.utc).isoformat()
    pairs={k:v for k,v in api("AssetPairs").items() if v.get("status")=="online" and v.get("quote") in ("ZUSD","USD") and not k.endswith(".d")}
    tickers=api("Ticker")
    watches=[]; failed=[]
    for pair,meta in pairs.items():
        try:
            t=tickers.get(pair) or tickers.get(meta.get("altname",""))
            if not t: raise ValueError("missing ticker")
            price=float(t["c"][0]); open24=float(t["o"]); vol=float(t["v"][1]); trades=int(t["t"][1])
            bid=float(t["b"][0]); ask=float(t["a"][0])
            if not (price>0 and open24>0 and bid>0 and ask>=bid): raise ValueError("invalid price")
            move=(price/open24-1)*100; spread=(ask-bid)/bid*10000
            score=min(35,trades/35)+min(30,vol*price/100000)+max(0,20-spread*2)+max(0,15-abs(move)*2)
            if score>=60: watches.append({"pair":pair,"score":round(score,2),"move24_pct":round(move,2),"spread_bps":round(spread,2),"status":"WATCH"})
        except (KeyError,ValueError,TypeError,ZeroDivisionError) as exc: failed.append({"pair":pair,"error":str(exc)})
    watches.sort(key=lambda x:-x["score"])
    return {"at":ts,"engine":"rebuild-shadow-0.2","health":"COMPLETE" if not failed else "PARTIAL","universe":len(pairs),"scanned":len(pairs)-len(failed),"failures":len(failed),"watch":watches[:20],"recommendation":"NO VERIFIED BUYS","note":"Single-snapshot discovery only; no execution confirmation"}
if __name__=="__main__":
    try: print(json.dumps(scan(),indent=2))
    except Exception as exc:
        print(json.dumps({"health":"FAILED","error":str(exc),"recommendation":"NO VERIFIED BUYS"}))
        raise
