"""Bounded read-only historical Kraken Trades recovery with replayable receipts.

The since/last nanosecond cursor is documented by Kraken's Advanced API FAQ.
Preserve raw response bytes with the cursor chain. Never synthesize a bar,
infer a missing label as negative, or replace live market eligibility.
"""
import argparse
import base64
from datetime import datetime, timezone, timedelta
from decimal import Decimal
import gzip
import hashlib
import json
from pathlib import Path
import time
from urllib.parse import urlencode
from urllib.request import urlopen
from .shadow_learning_evidence import utc_time, canonical_digest
from .market_wide_learning import build_market_cohort

NS = 1_000_000_000
BAR = 300 * NS
SCHEMA = "kraken_historical_trade_cursor_v1"


def ns(value):
    return int(utc_time(value).timestamp()) * NS


def stamp(value):
    return datetime.fromtimestamp(value // NS, timezone.utc).isoformat()


def fetch(pair, cursor):
    query=urlencode({"pair":pair,"since":str(cursor)})
    with urlopen("https://api.kraken.com/0/public/Trades?"+query,timeout=25) as response:
        return response.read()


def decode_page(raw, cursor):
    d=json.loads(raw,parse_float=Decimal)
    if d.get("error"):
        raise ValueError("Kraken trade API error: "+str(d["error"]))
    result=d["result"]
    keys=[k for k in result if k!="last"]
    if len(keys)!=1:
        raise ValueError("Ambiguous trade pair alias")
    last=int(result["last"])
    if last<=cursor:
        raise ValueError("Historical trade cursor did not advance")
    trades=[]
    for row in result[keys[0]]:
        if len(row)<3:
            raise ValueError("Malformed trade")
        price,volume=Decimal(row[0]),Decimal(row[1])
        timestamp=Decimal(str(row[2]))*NS
        if not (price.is_finite() and volume.is_finite() and price>0 and volume>0
                and timestamp.is_finite()):
            raise ValueError("Invalid trade")
        at=int(timestamp)
        ident=str(row[6]) if len(row)>6 else None
        trades.append((at,price,volume,ident))
    if not trades or any(b[0]<a[0] for a,b in zip(trades,trades[1:])):
        raise ValueError("Empty or unordered historical trade page")
    return keys[0],last,trades


def replay(state):
    if state.get("schema")!=SCHEMA:
        raise ValueError("Invalid historical cursor schema")
    start,end=ns(state["start_utc"]),ns(state["end_utc"])
    if not start<end<=start+7*24*3600*NS or start%BAR or end%BAR:
        raise ValueError("Invalid bounded historical window")
    cursor=start-1
    last_trade=None
    key=None
    ids=set()
    bars={}
    count=0
    for page in state["pages"]:
        raw=base64.b64decode(page["raw_b64"],validate=True)
        if page["since"]!=cursor or hashlib.sha256(raw).hexdigest()!=page["sha256"]:
            raise ValueError("Historical page receipt mismatch")
        alias,next_cursor,trades=decode_page(raw,cursor)
        if (key is not None and alias!=key) or next_cursor!=page["last"]:
            raise ValueError("Historical pair/cursor mismatch")
        key=alias
        for at,price,volume,ident in trades:
            if last_trade is not None and at<last_trade:
                raise ValueError("Historical page overlap out of order")
            last_trade=at
            if ident is not None:
                if ident in ids:
                    raise ValueError("Duplicate historical trade ID")
                ids.add(ident)
            if not start<=at<end:
                continue
            close_at=(at//BAR+1)*BAR
            b=bars.setdefault(close_at,[price,price,Decimal(0),0])
            b[0]=price
            b[1]=max(b[1],price)
            b[2]+=volume
            b[3]+=1
            count+=1
        cursor=next_cursor
    complete=last_trade is not None and last_trade>=end
    watermark=end if complete else min(end,max(start,(last_trade or start)//BAR*BAR))
    candles=[dict(pair=state["pair"],timestamp_utc=stamp(t),close=float(b[0]),
                  high=float(b[1]),volume=float(b[2]),trades=b[3])
             for t,b in sorted(bars.items()) if t<=watermark]
    return cursor,complete,watermark,candles,count


def recover(pair,start,end,*,max_pages=20,previous=None,fetch_page=fetch,pause=time.sleep):
    if not 1<=max_pages<=60:
        raise ValueError("Invalid page budget")
    state=dict(schema=SCHEMA,pair=pair,start_utc=start,end_utc=end,pages=[])
    if previous is not None:
        if previous.get("digest")!=canonical_digest({k:v for k,v in previous.items() if k!="digest"}):
            raise ValueError("Historical checkpoint checksum mismatch")
        if any(previous.get(k)!=state[k] for k in ("schema","pair","start_utc","end_utc")):
            raise ValueError("Historical checkpoint identity mismatch")
        state["pages"]=list(previous["pages"])
    cursor,done,watermark,candles,count=replay(state)
    for _ in range(max_pages):
        if done:
            break
        raw=fetch_page(pair,cursor)
        _,last,trades=decode_page(raw,cursor)
        state["pages"].append(dict(since=cursor,last=last,sha256=hashlib.sha256(raw).hexdigest(),
                                   raw_b64=base64.b64encode(raw).decode("ascii")))
        cursor=last
        done=trades[-1][0]>=ns(end)
        if not done:
            pause(1.1)
    cursor,done,watermark,candles,count=replay(state)
    state["digest"]=canonical_digest(state)
    # Outcome windows end only at the last cursor-supported completed bar.
    # Even with paginated trades, strict candle labels remain unchanged.
    cohort=build_market_cohort(candles,eligible_pairs=[pair],evaluation_asof_utc=stamp(watermark),
                               anchor_start_utc=start)
    for row in cohort["anchors"]+cohort["outcomes"]:
        row["source_sha256"]=state["digest"]
    cohort.update(source_kind="KRAKEN_PUBLIC_HISTORICAL_TRADES_CURSOR",
                  source_cursor_state_sha256=state["digest"],
                  eligibility_scope="HISTORICAL_PAIR_NOT_LIVE_ELIGIBILITY")
    summary=dict(schema="historical_trade_recovery_v1",pair=pair,start_utc=start,end_utc=end,
                 cursor=cursor,pages=len(state["pages"]),cursor_window_reached=done,
                 observed_through_utc=stamp(watermark),observed_trades=count,
                 completed_candles=len(candles),anchors=len(cohort["anchors"]),
                 feature_complete_anchors=cohort["feature_complete_anchors"],
                 per_horizon=cohort["per_horizon"],source_cursor_state_sha256=state["digest"],
                 source_authenticated=False,production_applied=False,promotion_authorized=False,
                 coverage_scope="SINGLE_PAIR_CURSOR_SUPPORTED_NOT_MARKET_WIDE")
    return state,cohort,summary


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--pair",required=True)
    p.add_argument("--start",required=True)
    p.add_argument("--end",required=True)
    p.add_argument("--max-pages",type=int,default=20)
    p.add_argument("--previous",type=Path)
    p.add_argument("--output-dir",type=Path,required=True)
    a=p.parse_args()
    prior=None
    if a.previous:
        with gzip.open(a.previous,"rt") as src:
            prior=json.load(src)
    state,cohort,summary=recover(a.pair,a.start,a.end,max_pages=a.max_pages,previous=prior)
    a.output_dir.mkdir(parents=True,exist_ok=True)
    with gzip.open(a.output_dir/"cursor-state.json.gz","wt") as out:
        json.dump(state,out,separators=(",",":"))
    with gzip.open(a.output_dir/"cohort.jsonl.gz","wt") as out:
        out.write(json.dumps(cohort,separators=(",",":"))+"\n")
    (a.output_dir/"summary.json").write_text(json.dumps(summary,sort_keys=True)+"\n")
    print(json.dumps(summary,sort_keys=True))


if __name__=="__main__":
    main()
