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
    return {"score": round(score, 2), "move24_pct": round(move, 2), "spread_bps": round(spread, 2)}

def scan():
    started = dt.datetime.now(dt.timezone.utc)
    pairs = {k: v for k, v in api("AssetPairs").items() if v.get("status") == "online" and v.get("quote") in ("ZUSD", "USD") and not k.endswith(".d")}
    tickers = api("Ticker")
    watches, failed = [], []
    for pair, meta in pairs.items():
        try:
            ticker = tickers.get(pair) or tickers.get(meta.get("altname", ""))
            if ticker is None:
                raise ValueError("missing ticker")
            metrics = rank(ticker)
            if metrics["score"] >= 60:
                watches.append({"pair": pair, **metrics, "status": "WATCH"})
        except (KeyError, ValueError, TypeError, ZeroDivisionError) as exc:
            failed.append({"pair": pair, "error": str(exc)})
    watches.sort(key=lambda x: -x["score"])
    finished = dt.datetime.now(dt.timezone.utc)
    return {"started_at": started.isoformat(), "completed_at": finished.isoformat(), "engine": "rebuild-shadow-0.3", "health": "COMPLETE" if not failed else "PARTIAL", "universe": len(pairs), "scanned": len(pairs) - len(failed), "failures": len(failed), "failed_pairs": failed[:25], "watch": watches[:20], "recommendation": "NO VERIFIED BUYS", "note": "Single-snapshot discovery; no execution confirmation or learning yet"}

def main():
    try:
        result = scan()
    except Exception as exc:
        result = {"completed_at": dt.datetime.now(dt.timezone.utc).isoformat(), "engine": "rebuild-shadow-0.3", "health": "FAILED", "error": str(exc), "recommendation": "NO VERIFIED BUYS"}
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))
    if result["health"] == "FAILED":
        raise SystemExit(1)

if __name__ == "__main__":
    main()
