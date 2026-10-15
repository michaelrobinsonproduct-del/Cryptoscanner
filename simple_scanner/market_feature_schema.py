"""Pure point-in-time feature record validation for future market-wide collection.

No network, persistence, ranking changes, or trading actions.
"""
import datetime as dt
import math

FIELDS=("price","spread_bps","notional_24h_usd","move_24h_pct")

def validate_record(record, *, observed_at):
    if not isinstance(record,dict):
        return {"valid":False,"reason":"invalid_record"}
    try:
        now=dt.datetime.fromisoformat(observed_at)
        stamped=dt.datetime.fromisoformat(record["observed_at"])
        if now.tzinfo is None or stamped.tzinfo is None:
            return {"valid":False,"reason":"naive_timestamp"}
        lag=(now-stamped).total_seconds()
        if not 0<=lag<=120:
            return {"valid":False,"reason":"stale_or_future"}
        if not isinstance(record.get("pair"),str) or not record["pair"]:
            return {"valid":False,"reason":"missing_pair"}
        for key in FIELDS:
            val=record.get(key)
            if type(val) not in (int,float) or not math.isfinite(val):
                return {"valid":False,"reason":"invalid_"+key}
        if record["price"]<=0 or record["spread_bps"]<0 or record["notional_24h_usd"]<0:
            return {"valid":False,"reason":"invalid_market_values"}
        return {"valid":True,"reason":"point_in_time_valid"}
    except (KeyError,ValueError,TypeError,OverflowError):
        return {"valid":False,"reason":"invalid_timestamp_or_fields"}
