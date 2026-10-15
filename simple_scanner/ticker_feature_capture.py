"""Pure, no-network extraction of full-market features from an existing Kraken ticker response.

Does not change scan selection, add Kraken requests, or persist anything.
"""
import math
from simple_scanner.market_feature_schema import validate_record

def extract_features(eligible, ticker, *, observed_at):
    records=[]
    rejected={}
    for pair in sorted(eligible):
        t=ticker.get(pair)
        if t is None:
            rejected[pair]="missing_ticker"
            continue
        try:
            last=float(t["c"][0]);bid=float(t["b"][0]);ask=float(t["a"][0])
            opening=float(t["o"]);volume=float(t["v"][1])
            if not all(math.isfinite(x) for x in (last,bid,ask,opening,volume)):
                raise ValueError("nonfinite")
            if min(last,bid,ask,opening)<=0 or ask<bid or volume<0:
                raise ValueError("invalid_market")
            record={"pair":pair,"observed_at":observed_at,"price":last,
                    "spread_bps":10000*(ask/bid-1),
                    "notional_24h_usd":last*volume,
                    "move_24h_pct":100*(last/opening-1)}
            quality=validate_record(record,observed_at=observed_at)
            if not quality["valid"]:
                rejected[pair]=quality["reason"]
                continue
            records.append(record)
        except (KeyError,IndexError,ValueError,TypeError,ZeroDivisionError,OverflowError):
            rejected[pair]="invalid_ticker"
    return {"status":"DIAGNOSTIC_ONLY","records":records,"rejected":rejected,
            "eligible_pairs":len(eligible),"coverage_pct":100*len(records)/len(eligible) if eligible else 0,
            "production_modified":False,"buy_approved":False}
