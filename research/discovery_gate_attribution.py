"""Research-only gate attribution from separately captured Kraken ticker snapshots.

No network calls, production writes, ranking changes, or trade approvals.
"""
import json
import math

def classify(record):
    """Mirror production's exact daily move, spread, and notional eligibility gates."""
    try:
        last=float(record["last"]); bid=float(record["bid"]); ask=float(record["ask"])
        daily_open=float(record["open"]); volume=float(record["volume24"])
        if not all(math.isfinite(x) for x in (last,bid,ask,daily_open,volume)):
            return ["invalid_market_data"]
        if min(last,bid,ask,daily_open)<=0 or volume<0 or ask<bid:
            return ["invalid_market_data"]
        move=100*(last/daily_open-1)
        spread=10000*(ask/bid-1)
        notional=volume*last
        reasons=[]
        if move<0.25: reasons.append("daily_move_below_0_25pct")
        if move>12: reasons.append("daily_move_above_12pct")
        if spread>45: reasons.append("spread_above_45bps")
        if notional<100000: reasons.append("notional_below_100k")
        return reasons or ["passes_initial_gates"]
    except (KeyError,ValueError,TypeError,ZeroDivisionError):
        return ["invalid_market_data"]

def summarize(records):
    from collections import Counter
    results={str(pair):classify(record) for pair,record in records.items()}
    counts=Counter(reason for reasons in results.values() for reason in reasons)
    return {"mode":"RESEARCH_ONLY","pairs":len(results),
            "reason_counts":dict(sorted(counts.items())),
            "per_pair_reasons":results,
            "caveat":"Ticker snapshot gate results alone do not prove a pre-breakout signal."}

if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument("ticker_snapshot_json",help="Offline JSON object: pair to {last,bid,ask,open,volume24}")
    args=p.parse_args()
    with open(args.ticker_snapshot_json,encoding="utf-8") as f: records=json.load(f)
    print(json.dumps(summarize(records),indent=2))
