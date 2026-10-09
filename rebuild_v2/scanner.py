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
    score = min(35, trades / 35) + min(30, vol * price / 100000) + max(0, 20 - spread * 2) + max(0, 15 - abs(move) * 2)
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
    return metrics["score"] >= 60 and metrics["move24_pct"] > 0

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
            market_quotes.append({"pair":pair,"bid":float(ticker["b"][0])})
            if eligible_watch(metrics):
                watches.append({"pair": pair, **metrics, "status": "WATCH"})
        except (KeyError, ValueError, TypeError, ZeroDivisionError) as exc:
            failed.append({"pair": pair, "error": str(exc)})
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
    return {"started_at": started.isoformat(), "completed_at": finished.isoformat(), "engine": "rebuild-shadow-1.0", "health": "COMPLETE" if not failed else "PARTIAL", "universe": len(pairs), "scanned": len(pairs) - len(failed), "failures": len(failed), "failed_pairs": failed[:25], "watch": watches[:20], "market_quotes": market_quotes, "confirmations": confirmations, "recommendation": "NO VERIFIED BUYS", "note": "Double-confirmed shadow watches only; no verified buy model or trained learning"}

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
        from history import learning_report, history_diagnostics
        result["learning_report"] = learning_report()
        result["history_diagnostics"] = history_diagnostics()
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
