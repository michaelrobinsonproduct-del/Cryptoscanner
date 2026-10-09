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
    """Match historical 5m anchor features using only completed OHLC candles."""
    import urllib.parse
    data=fetch("OHLC?pair="+urllib.parse.quote(pair,safe="")+"&interval=5")
    candles=next(v for k,v in data.items() if k!="last" and isinstance(v,list))
    bars=candles[:-1]
    if len(bars)<13:
        raise ValueError("insufficient completed 5m bars")
    b=bars[-13:]
    closes=[float(x[4]) for x in b]
    volumes=[float(x[6]) for x in b]
    trades=[float(x[7]) for x in b]
    pv=sum(volumes[-13:-7]); cv=sum(volumes[-7:-1])
    pt=sum(trades[-13:-7]); ct=sum(trades[-7:-1])
    return {"pre_return_60m_pct":round(100*(closes[-1]/closes[0]-1),3),
            "volume_accel":round(cv/pv,3) if pv>0 else None,
            "trade_accel":round(ct/pt,3) if pt>0 else None}

def historical_rule_bonus(features,model):
    if features.get("volume_accel") is None or features.get("trade_accel") is None:return 0,[]
    early=abs(features["pre_return_60m_pct"])<=3
    vol=features["volume_accel"]>=2
    trades=features["trade_accel"]>=2
    matched={"early_1h":early,"volume_2x":vol,"trades_2x":trades,
             "early_volume":early and vol,"early_trades":early and trades,
             "volume_trades":vol and trades}
    approved=[name for name in model.get("approved_rules",[]) if matched.get(name,False)]
    return min(8,2*len(approved)),approved

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
    from history import historical_signal_adjustments, pair_signal_adjustment
    calibration = historical_signal_adjustments()
    for candidate in watches:
        candidate["score"] = round(candidate["score"] + pair_signal_adjustment(candidate["pair"]) + (calibration["watch_score_adjustment"] if calibration["ready"] else 0),2)
    model_path=pathlib.Path("rebuild_v2/output/historical_model.json")
    model=None
    if model_path.exists():
        try:
            candidate_model=json.loads(model_path.read_text())
            if candidate_model.get("schema_version")==1 and candidate_model.get("holdout_rows",0)>=100:
                model=candidate_model
        except (ValueError,OSError):
            pass
    # The previous archive model used an outcome-selected sample. Do not score from it.
    # Require a representative-control interaction model and live feature parity.
    interaction_path=pathlib.Path("rebuild_v2/output/interaction_model.json")
    interaction=None
    if interaction_path.exists():
        try:
            candidate_interaction=json.loads(interaction_path.read_text())
            if candidate_interaction.get("schema_version")==2 and candidate_interaction.get("unique_pair_days",0)>=1000:
                interaction=candidate_interaction
        except (ValueError,OSError):
            pass
    model=None  # legacy single-factor boosts disabled pending unbiased interaction parity
    research={"status":("ACTIVE_BONUSES" if model.get("approved_rules") else "VALIDATED_NO_APPROVED_RULES") if model else "MODEL_NOT_RESTORED",
              "approved_rules":model.get("approved_rules",[]) if model else [],
              "candidates_enriched":0,"feature_failures":0,"ranking_changes_possible":False,"interaction_model_loaded":bool(interaction),"feature_parity":"NOT_IMPLEMENTED","legacy_bias_guard":"ENFORCED"}
    if model and model.get("approved_rules"):
        for candidate in sorted(watches,key=lambda x:-x["score"])[:12]:
            try:
                features=historical_live_features(candidate["pair"])
                bonus,matched=historical_rule_bonus(features,model)
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
    finished = dt.datetime.now(dt.timezone.utc)
    return {"started_at": started.isoformat(), "completed_at": finished.isoformat(), "engine": "rebuild-shadow-1.0", "health": "COMPLETE" if not failed else "PARTIAL", "universe": len(pairs), "scanned": len(pairs) - len(failed), "failures": len(failed), "failed_pairs": failed[:25], "watch": watches[:20], "market_quotes": market_quotes, "historical_research": research, "confirmations": confirmations, "recommendation": "NO VERIFIED BUYS", "note": "Double-confirmed shadow watches only; no verified buy model or trained learning"}

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
        store_run(result)
        result["historical_outcomes"] = outcome_summary()
        from history import learning_report, history_diagnostics, reliability_scorecard, miss_report, historical_signal_adjustments, historical_cohort_analysis
        result["learning_report"] = learning_report()
        result["historical_cohort_analysis"] = historical_cohort_analysis(1)
        result["missed_breakouts"] = miss_report()
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
