"""Standalone, read-only Kraken early-breakout scan. Standard library only."""
import datetime as dt, json, math, statistics, time, urllib.request, os
from pathlib import Path
ROOT="https://api.kraken.com/0/public/"
def get(path):
    for attempt in range(3):
        try:
            req=urllib.request.Request(ROOT+path,headers={"User-Agent":"KrakenSimpleResearch/1.0","Cache-Control":"no-cache"})
            with urllib.request.urlopen(req,timeout=25) as r: data=json.load(r)
            if data.get("error"): raise RuntimeError(str(data["error"]))
            return data["result"]
        except Exception:
            if attempt==2:raise
            time.sleep(2**attempt)
def main():
    now=dt.datetime.now(dt.timezone.utc)
    pairs=get("AssetPairs")
    eligible={k:v for k,v in pairs.items() if v.get("status")=="online" and v.get("wsname","").endswith("/USD") and v.get("base","").upper() not in {"ZUSD","USD","USDT","USDC","DAI","PYUSD","EURC","RLUSD","TUSD"}}
    ticker=get("Ticker?pair="+",".join(eligible)) if len(eligible)<100 else get("Ticker")
    scored=[]; errors=[]; matched_tickers=0; market_prices={}; market_signals={}
    for pair,meta in eligible.items():
        t=ticker.get(pair)
        if not t:continue
        matched_tickers+=1
        try:
            last=float(t["c"][0]);bid=float(t["b"][0]);ask=float(t["a"][0]);op=float(t["o"]);volume=float(t["v"][1])
            if not all(math.isfinite(x) for x in (last,bid,ask,op,volume)) or min(last,bid,ask,op)<=0 or volume<0 or ask<bid:continue
            market_prices[pair]=last
            move=100*(last/op-1);spread=10000*(ask/bid-1);notional=volume*last
            market_signals[pair]={"move24_pct":round(move,4),"spread_bps":round(spread,3),"notional_24h_usd":round(notional,2)}
            if not (0.25<=move<=12 and spread<=45 and notional>=100000):continue
            score=round(min(45,move*7)+min(25,notional/150000)+max(0,30-spread/2),1)
            scored.append({"pair":pair,"symbol":meta.get("wsname",pair),"price":last,"move24_pct":round(move,2),"spread_bps":round(spread,2),"notional_24h_usd":round(notional),"score":score})
        except (ValueError,TypeError,KeyError,ZeroDivisionError) as e:errors.append({"pair":pair,"error":str(e)})
    # Fail before OHLC requests or publishing output when market coverage is incomplete.
    if matched_tickers<max(50,int(len(eligible)*0.8)):
        raise RuntimeError("Insufficient eligible-pair ticker coverage")
    scored.sort(key=lambda x:x["score"],reverse=True)
    # Diversify OHLC screening beyond the highest 24h momentum names.
    # Large, already-extended coins otherwise monopolize the research budget.
    selected=[]; seen=set()
    def take(items, limit):
        added=0
        for item in items:
            if item["pair"] in seen: continue
            selected.append(item); seen.add(item["pair"]); added+=1
            if added>=limit: break
    take(scored,12)
    take(sorted(scored,key=lambda x:(x["move24_pct"],-x["notional_24h_usd"])),8)
    take(sorted(scored,key=lambda x:(x["spread_bps"],-x["notional_24h_usd"])),6)
    take(sorted(scored,key=lambda x:(x["notional_24h_usd"],-x["move24_pct"])),6)
    screened=selected
    for base_rank,item in enumerate(screened,1):
        item["base_rank"]=base_rank
        pair=item["pair"]
        try:
            bars=get("OHLC?pair="+pair+"&interval=5")
            candles=next(v for k,v in bars.items() if k!="last")[:-1]
            if len(candles)<13:raise ValueError("too few completed candles")
            age=(now.timestamp()-float(candles[-1][0]))
            if age<0 or age>900:raise ValueError("stale OHLC")
            c=[float(x[4]) for x in candles[-13:]];v=[float(x[6]) for x in candles[-13:]]
            if not all(math.isfinite(x) and x>0 for x in c) or not all(math.isfinite(x) and x>=0 for x in v):raise ValueError("invalid OHLC close or volume")
            item.update({"move_15m_pct":round(100*(c[-1]/c[-4]-1),2),"move_60m_pct":round(100*(c[-1]/c[0]-1),2),"volume_accel":round(sum(v[-6:])/max(sum(v[-12:-6]),1e-9),2),"ohlc_age_seconds":round(age),"status":"WATCH_RESEARCH_ONLY"})
        except Exception as e:item.update({"status":"UNVERIFIED","reason":str(e)})
        time.sleep(.25)
    # Validate diversified candidates before selecting 12; otherwise strong intrahour
    # acceleration outside the 24h top 12 is invisible to the research watchlist.
    # Prioritize actual intrahour acceleration after candle validation.
    for item in screened:
        if item.get("status")=="WATCH_RESEARCH_ONLY":
            item["early_signal_score"]=round(item["score"]+max(-25,min(25,item["move_15m_pct"]*5))+max(-15,min(15,(item["volume_accel"]-1)*10)),1)
        else:
            item["early_signal_score"]=None
    watch=sorted((x for x in screened if x["early_signal_score"] is not None),key=lambda x:x["early_signal_score"],reverse=True)[:12]
    assert len(watch)<=12 and len({item["pair"] for item in watch})==len(watch)
    for rank,item in enumerate(watch,1):
        item["research_rank"]=rank
        item["early_signal_basis"]="15m_momentum_plus_volume_acceleration" if item["early_signal_score"] is not None else "UNVERIFIED"
    # Additive risk annotation only: selection, ranks, scores and approvals remain untouched.
    try:
        from simple_scanner.risk_labels import assess_risk
        for item in watch:
            item.update(assess_risk(item))
    except Exception as risk_error:
        # Risk display is optional; never fail the scanner for a display-only feature.
        for item in watch:
            item["risk"]="UNASSESSED"
            item["risk_reasons"]=["risk_annotation_unavailable"]
    finished=dt.datetime.now(dt.timezone.utc)
    result={"engine":"simple-kraken-1","started_at":now.isoformat(),"completed_at":finished.isoformat(),"universe":len(eligible),"ticker_pairs":len(ticker),"matched_tickers":matched_tickers,"ohlc_screened":len(screened),"validated_watch":sum(x.get("status")=="WATCH_RESEARCH_ONLY" for x in watch),"errors":errors,"watch":watch,"market_prices":market_prices,"market_signals":market_signals,"buy_approved":False,"learning_status":"NOT_VALIDATED","status":"RESEARCH_ONLY" if ticker else "FAILED"}
    if not watch:
        raise RuntimeError("No fresh verified OHLC watch candidates")
    Path(os.getenv("SIMPLE_SCANNER_DATA_DIR","simple_scanner/output")).mkdir(parents=True,exist_ok=True)
    (Path(os.getenv("SIMPLE_SCANNER_DATA_DIR","simple_scanner/output"))/"latest.json").write_text(json.dumps(result,indent=2))
    print("SCAN_SUMMARY "+json.dumps({k:result[k] for k in ("engine","started_at","completed_at","universe","ticker_pairs","matched_tickers","ohlc_screened","validated_watch","status","buy_approved")},separators=(",",":")),flush=True)
    print("WATCH_SUMMARY "+json.dumps([{"symbol":x["symbol"],"score":x["early_signal_score"],"move_15m_pct":x["move_15m_pct"],"volume_accel":x["volume_accel"],"risk":x.get("risk","UNASSESSED"),"risk_reasons":x.get("risk_reasons",[])} for x in watch],separators=(",",":")),flush=True)
if __name__=="__main__":main()
