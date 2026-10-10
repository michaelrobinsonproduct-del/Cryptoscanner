"""Zero-credential Kraken shadow discovery. No trading, no buy signals."""
import datetime as dt
import json
import os
import pathlib
import time
import urllib.request

API = "https://api.kraken.com/0/public/"
OUTPUT = pathlib.Path("rebuild_v2/output/latest.json")

def api(method, attempts=3):
    for n in range(attempts):
        try:
            request = urllib.request.Request(API + method, headers={"User-Agent": "kraken-shadow-rebuild/0.3", "Cache-Control": "no-cache"})
            with urllib.request.urlopen(request, timeout=25) as response:
                result = json.load(response)
            if result.get("error"):
                raise RuntimeError(str(result["error"]))
            return result["result"]
        except Exception:
            if n == attempts - 1:
                raise
            time.sleep(2 ** n)

def rank(t):
    price = float(t["c"][0])
    open24 = float(t["o"])
    vol = float(t["v"][1])
    trades = int(t["t"][1])
    bid = float(t["b"][0])
    ask = float(t["a"][0])
    if not (price > 0 and open24 > 0 and bid > 0 and ask >= bid):
        raise ValueError("invalid executable quote")
    move = (price / open24 - 1) * 100
    spread = (ask - bid) / bid * 10000
    score = min(48, max(0, move) * 12) + min(22, trades / 120) + min(15, vol * price / 250000) + max(0, 15 - spread * 2)
    return {"price": price, "score": round(score, 2), "move24_pct": round(move, 2), "spread_bps": round(spread, 2)}

def confirm_watch(pair, snapshot, fetch=api):
    """Independent REST depth/trades checks. No entry approval from one confirmation."""
    import urllib.parse
    encoded = urllib.parse.quote(pair, safe="")
    depth = fetch("Depth?pair=" + encoded + "&count=10")
    trades = fetch("Trades?pair=" + encoded)
    d = next(value for value in depth.values() if isinstance(value,dict) and "bids" in value)
    t = next(value for value in trades.values() if isinstance(value,list))
    if not isinstance(t, list) or not t or not isinstance(t[0], list):
        raise ValueError("no recent trade")
    bids, asks = d.get("bids", []), d.get("asks", [])
    if not bids or not asks:
        raise ValueError("empty order book")
    bid, ask = float(bids[0][0]), float(asks[0][0])
    trade_time = max(float(row[2]) for row in t if isinstance(row, list) and len(row) > 2)
    age = time.time() - trade_time
    if not (0 <= age <= 120 and 0 < bid <= ask):
        raise ValueError("stale trade or invalid book")
    spread = (ask / bid - 1) * 10000
    if spread > 100:
        raise ValueError("spread too wide")
    return {"confirmed_at": dt.datetime.now(dt.timezone.utc).isoformat(), "trade_age_seconds": round(age, 2), "spread_bps": round(spread, 2), "status": "WATCH_CONFIRMED", "entry_approved": False}

def confirm_twice(pair, snapshot, fetch=api, wait=lambda seconds: time.sleep(seconds)):
    first = confirm_watch(pair, snapshot, fetch)
    wait(2)
    second = confirm_watch(pair, snapshot, fetch)
    first_time = dt.datetime.fromisoformat(first["confirmed_at"])
    second_time = dt.datetime.fromisoformat(second["confirmed_at"])
    if second_time <= first_time:
        raise ValueError("confirmation timestamps not ordered")
    return {"pair": pair, "first": first, "second": second, "status": "DOUBLE_CONFIRMED_WATCH", "entry_approved": False}

NON_TARGET_BASES = {"USD", "ZUSD", "EUR", "ZEUR", "GBP", "ZGBP", "AUD", "ZAUD", "CAD", "ZCAD", "CHF", "ZCHF", "JPY", "ZJPY", "USDT", "USDC", "DAI", "PYUSD", "TUSD", "EURC", "RLUSD", "FDUSD", "USDG", "USDD", "USDE", "USDS", "UST", "USTC"}

def eligible_crypto_pair(meta):
    return meta.get("base", "").upper() not in NON_TARGET_BASES

def eligible_watch(metrics):
    return metrics["score"] >= 35 and 0.5 <= metrics["move24_pct"] <= 12 and metrics["spread_bps"] <= 40

def historical_live_features(pair, fetch=api):
    """Reproduce archive features from completed 5-minute Kraken candles only."""
    import urllib.parse,statistics
    data=fetch("OHLC?pair="+urllib.parse.quote(pair,safe="")+"&interval=5")
    candles=next(v for k,v in data.items() if k!="last" and isinstance(v,list))
    bars=candles[:-1]  # Kraken includes current incomplete candle
    if len(bars)<13:raise ValueError("insufficient completed 5m bars")
    b=bars[-13:]
    # The Kraken endpoint may return cached candles during an outage. Never
    # evaluate historical research rules on an old completed bar.
    last_open=dt.datetime.fromtimestamp(float(b[-1][0]),dt.timezone.utc)
    age=(dt.datetime.now(dt.timezone.utc)-last_open).total_seconds()
    # The last completed bar opened in the previous five-minute slot;
    # its opening timestamp is normally 0-600 seconds old, not 300-900.
    # Allow one delayed slot, but reject future or substantially stale bars.
    if not 0 <= age <= 900:
        raise ValueError("stale or future historical OHLC candle")
    closes=[float(x[4]) for x in b]
    volumes=[float(x[6]) for x in b]
    trades=[float(x[7]) for x in b]
    if any(p<=0 for p in closes):raise ValueError("invalid OHLC price")
    prevv=sum(volumes[:6]);curv=sum(volumes[6:12])
    prevt=sum(trades[:6]);curt=sum(trades[6:12])
    returns=[100*(closes[j]/closes[j-1]-1) for j in range(1,13)]
    return {"pre_return_5m_pct":100*(closes[-1]/closes[-2]-1),
            "pre_return_15m_pct":100*(closes[-1]/closes[-4]-1),
            "pre_return_60m_pct":100*(closes[-1]/closes[0]-1),
            "volume_accel":curv/prevv if prevv>0 else None,
            "trade_accel":curt/prevt if prevt>0 else None,
            "volatility_pct":statistics.pstdev(returns)}

def historical_rule_bonus(features,model):
    """Bounded bonus for rules that passed chronological out-of-sample evaluation."""
    p5=features["pre_return_5m_pct"];p15=features["pre_return_15m_pct"]
    p60=features["pre_return_60m_pct"];v=features["volume_accel"]
    t=features["trade_accel"];z=features["volatility_pct"]
    if v is None or t is None:return 0,[]
    predicates={"early":abs(p60)<=3,"quiet_15m":abs(p15)<=1.5,
      "rising_15m":0.1<=p15<=2,"positive_5m":0<p5<=1.5,
      "volume_accel_1_5x":v>=1.5,"volume_accel_2x":v>=2,
      "trades_accel_1_5x":t>=1.5,"trades_accel_2x":t>=2,
      "trade_leads_volume":t>=1.5 and t>v*1.25,
      "volume_leads_trades":v>=1.5 and v>t*1.25,
      "compression":z<=0.6,"volatility_expansion":z>=1.5,
      "controlled_breakout":0.3<=p60<=3,"not_extended":abs(p60)<=5}
    matched=[rule for rule in model.get("approved_rules",[])
             if isinstance(rule,list) and len(rule)>=2 and all(predicates.get(name,False) for name in rule)]
    return min(8,2*len(matched)),matched

def evaluate_watch_continuity(watches, previous, now, max_age_seconds=1800):
    """Fail closed on fading prices; never promote stale or unconfirmed watches."""
    prior={c.get("pair"):c for c in (previous or {}).get("watch",[]) if isinstance(c,dict)}
    stamp=(previous or {}).get("completed_at")
    try:
        age=(now-dt.datetime.fromisoformat(stamp.replace("Z","+00:00"))).total_seconds()
    except (TypeError,ValueError,AttributeError):
        age=None
    usable=age is not None and 0<=age<=max_age_seconds
    counts={"compared":0,"downgraded":0,"prior_report_fresh":usable}
    for c in watches:
        c["continuity_state"]="NEW_OR_UNVERIFIED"
        c["entry_approved"]=False
        old=prior.get(c["pair"]) if usable else None
        if not old:continue
        try:
            old_price=float(old["price"]);new_price=float(c["price"])
            if old_price<=0 or new_price<=0:continue
            change=100*(new_price/old_price-1)
            c["change_since_previous_watch_pct"]=round(change,3)
            counts["compared"]+=1
            # Conservative research downgrade; not a buy trigger.
            if change<=-2 or c["move24_pct"]<0 or c["spread_bps"]>40:
                c["continuity_state"]="DOWNGRADED_PRICE_OR_LIQUIDITY"
                counts["downgraded"]+=1
            else:
                c["continuity_state"]="MONITOR_ONLY"
        except (ValueError,TypeError,KeyError,ZeroDivisionError):
            continue
    return counts

def scan():
    started = dt.datetime.now(dt.timezone.utc)
    pairs = {k: v for k, v in api("AssetPairs").items() if v.get("status") == "online" and v.get("quote") in ("ZUSD", "USD") and not k.endswith(".d") and eligible_crypto_pair(v)}
    tickers = api("Ticker")
    watches, failed, market_quotes = [], [], []
    for pair, meta in pairs.items():
        try:
            ticker = tickers.get(pair) or tickers.get(meta.get("altname", ""))
            if ticker is None:
                raise ValueError("missing ticker")
            metrics = rank(ticker)
            market_quotes.append({"pair":pair,"bid":float(ticker["b"][0]),"price":metrics["price"],"score":metrics["score"],"move24_pct":metrics["move24_pct"],"spread_bps":metrics["spread_bps"]})
            if eligible_watch(metrics):
                watches.append({"pair": pair, **metrics, "status": "WATCH"})
        except (KeyError, ValueError, TypeError, ZeroDivisionError) as exc:
            failed.append({"pair": pair, "error": str(exc)})
    # Calibrate conservatively from prospectively observed hits and misses.
    from history import prospective_learning
    calibration = prospective_learning()
    for candidate in watches:
        candidate["score"] = round(candidate["score"] + (calibration["adjustment"] if calibration["validated"] and candidate["score"] >= calibration["score_threshold"] else 0),2)
    interaction_path=pathlib.Path("rebuild_v2/output/interaction_model.json")
    interaction=None
    if interaction_path.exists():
        try:
            candidate=json.loads(interaction_path.read_text())
            if candidate.get("schema_version")==2 and candidate.get("unique_pair_days",0)>=1000:
                interaction=candidate
        except (ValueError,OSError):
            pass
    # Prospective-only diagnostics: observe historically supported trade acceleration,
    # but do not adjust ranking or claim execution readiness.
    simple_path=pathlib.Path("rebuild_v2/output/historical_model.json")
    simple=None
    if simple_path.exists():
        try:
            m=json.loads(simple_path.read_text())
            if m.get("schema_version")==1 and m.get("holdout_rows",0)>=1000:
                simple=m
        except (ValueError,OSError):
            pass
    trade_research={"mode":"OBSERVE_ONLY","model_loaded":bool(simple),
                    "approved_historical_rules":simple.get("approved_rules",[]) if simple else [],
                    "candidates_evaluated":0,"trade_accel_2x_count":0,
                    "volume_and_trade_2x_count":0,"feature_failures":0,
                    "score_adjustment_applied":0}
    if simple:
        for candidate in watches[:12]:
            try:
                features=historical_live_features(candidate["pair"])
                t=features.get("trade_accel");v=features.get("volume_accel")
                candidate["prospective_trade_research"]={
                    "trade_accel":t,"volume_accel":v,
                    "trades_2x":t is not None and t>=2,
                    "volume_trades":t is not None and t>=2 and v is not None and v>=2,
                    "score_adjustment":0}
                trade_research["candidates_evaluated"]+=1
                trade_research["trade_accel_2x_count"]+=int(t is not None and t>=2)
                trade_research["volume_and_trade_2x_count"]+=int(t is not None and t>=2 and v is not None and v>=2)
            except Exception as exc:
                candidate["prospective_trade_research_error"]=str(exc)
                trade_research["feature_failures"]+=1
    research={"status":("APPROVED_INTERACTION_RULES" if interaction.get("approved_rules") else "INTERACTION_MODEL_NO_APPROVED_RULES") if interaction else "INTERACTION_MODEL_NOT_RESTORED",
              "approved_rules":interaction.get("approved_rules",[]) if interaction else [],
              "candidates_enriched":0,"feature_failures":0,
              "ranking_changes_possible":False,"interaction_model_loaded":bool(interaction),
              "feature_parity":"IMPLEMENTED","legacy_bias_guard":"ENFORCED",
              "prospective_trade_research":trade_research}
    if interaction and interaction.get("approved_rules"):
        for candidate in sorted(watches,key=lambda x:-x["score"])[:12]:
            try:
                features=historical_live_features(candidate["pair"])
                bonus,matched=historical_rule_bonus(features,interaction)
                candidate["historical_features"]=features
                candidate["historical_rules_matched"]=matched
                candidate["historical_bonus"]=bonus
                candidate["score"]=round(candidate["score"]+bonus,2)
                research["candidates_enriched"]+=1
                research["ranking_changes_possible"] |= bonus>0
            except Exception as exc:
                candidate["historical_feature_error"]=str(exc)
                research["feature_failures"]+=1
    watches.sort(key=lambda x: -x["score"])
    # Avoid treating coins already extended >15% in 24h as early discoveries.
    watches = [c for c in watches if -10 <= c["move24_pct"] <= 15]
    confirmations = []
    for candidate in watches[:5]:
        try:
            check = confirm_twice(candidate["pair"], candidate)
            confirmations.append({"pair": candidate["pair"], **check})
        except Exception as exc:
            confirmations.append({"pair": candidate["pair"], "status": "CONFIRMATION_FAILED", "error": str(exc), "entry_approved": False})
    # Never imply that an unconfirmed research watch is an actionable entry.
    confirmed_pairs={c["pair"] for c in confirmations if c.get("status")=="DOUBLE_CONFIRMED_WATCH"}
    for candidate in watches:
        candidate["entry_approved"]=False
        candidate["signal_state"]="DOUBLE_CONFIRMED_RESEARCH_WATCH" if candidate["pair"] in confirmed_pairs else "UNCONFIRMED_RESEARCH_WATCH"
        candidate["requires_fresh_revalidation"]=True
        candidate["signal_observed_at"]=started.isoformat()
    previous_path=pathlib.Path("rebuild_v2/output/previous.json")
    try:
        previous=json.loads(previous_path.read_text()) if previous_path.exists() else None
    except (OSError,ValueError):
        previous=None
    continuity=evaluate_watch_continuity(watches,previous,dt.datetime.now(dt.timezone.utc))
    finished = dt.datetime.now(dt.timezone.utc)
    return {"started_at": started.isoformat(), "completed_at": finished.isoformat(), "engine": "rebuild-shadow-1.0", "health": "COMPLETE" if not failed else "PARTIAL", "universe": len(pairs), "scanned": len(pairs) - len(failed), "failures": len(failed), "failed_pairs": failed[:25], "watch": watches[:20], "market_quotes": market_quotes, "source_coverage": {"kraken": {"enabled": True, "pairs_scanned": len(pairs)-len(failed)}, "dex": {"enabled": False, "pairs_scanned": 0, "status": "NOT_IMPLEMENTED", "entry_approved": False}}, "prospective_learning": calibration, "historical_research": research, "confirmations": confirmations, "continuity_research": continuity, "recommendation": "NO VERIFIED BUYS", "note": "Double-confirmed shadow watches only; no verified buy model or trained learning"}

def main():
    try:
        result = scan()
    except Exception as exc:
        result = {"completed_at": dt.datetime.now(dt.timezone.utc).isoformat(), "engine": "rebuild-shadow-0.7", "health": "FAILED", "error": str(exc), "recommendation": "NO VERIFIED BUYS"}
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    try:
        from history import store_run, outcome_summary, evaluate_outcomes
        evaluate_outcomes(result) if result["health"] != "FAILED" else None
        from paper_entries import assess as assess_paper_entries
        result["paper_entry_research"] = assess_paper_entries(result)
        store_run(result)
        result["historical_outcomes"] = outcome_summary()
        from history import learning_report, history_diagnostics, reliability_scorecard, miss_report, historical_signal_adjustments, historical_cohort_analysis
        result["learning_report"] = learning_report()
        result["historical_cohort_analysis"] = historical_cohort_analysis(1)
        result["missed_breakouts"] = miss_report()
        from history import early_detection_benchmark
        result["early_detection_benchmark"] = early_detection_benchmark()
        result["historical_calibration"] = historical_signal_adjustments()
        result["history_diagnostics"] = history_diagnostics()
        result["reliability_scorecard"] = reliability_scorecard()
        result["persistence_health"] = "COMPLETE"
        OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    except Exception as exc:
        result["persistence_health"] = "FAILED"
        result["persistence_error"] = str(exc)
        OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
        print("PERSISTENCE_FAILED:", str(exc))
        raise SystemExit(1)
    print(json.dumps(result))
    if result["health"] == "FAILED":
        raise SystemExit(1)

if __name__ == "__main__":
    main()
