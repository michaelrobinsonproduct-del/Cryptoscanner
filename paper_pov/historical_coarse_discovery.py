"""Coarse historical event discovery ONLY: never five-minute training labels."""
import base64
import hashlib
import json
from datetime import datetime, timedelta, timezone
from math import isfinite
import time
from urllib.parse import urlencode
from urllib.request import urlopen
from .shadow_learning_evidence import canonical_digest, utc_time

SCHEMA="historical_coarse_discovery_v1"
START=utc_time("2026-10-01T00:00:00Z")
END=utc_time("2026-11-06T00:00:00Z")
STEP=timedelta(hours=4)

def fetch(pair):
    url="https://api.kraken.com/0/public/OHLC?"+urlencode({"pair":pair,"interval":240})
    with urlopen(url,timeout=15) as response:
        return response.read()

def inspect(pair,raw):
    payload=json.loads(raw)
    if payload.get("error"):
        raise ValueError("Kraken OHLC error: "+repr(payload["error"]))
    data=payload["result"]
    keys=[k for k in data if k!="last"]
    if len(keys)!=1:
        raise ValueError("Ambiguous coarse pair")
    bars={}
    for row in data[keys[0]][:-1]:
        stamp=datetime.fromtimestamp(int(row[0]),timezone.utc)+STEP
        close,high=float(row[4]),float(row[2])
        if not (isfinite(close) and isfinite(high) and 0<close<=high) or stamp in bars:
            raise ValueError("Invalid coarse candle")
        bars[stamp]=(close,high)
    events={}
    # Candidate reference close precedes every following high; no within-bar lookahead.
    # Missing intervals never become a negative label.
    for entry,(close,_) in sorted(bars.items()):
        if not START<=entry<END:
            continue
        for n in range(1,13):
            t=entry+n*STEP
            if t>END or t not in bars:
                continue
            excursion=bars[t][1]/close-1
            if excursion>=.30:
                # Existing three-day trade windows are separate recovery units.
                # Include both reference and crossing windows when different.
                for stamp in (entry,t-STEP):
                    a=START+timedelta(days=3*((stamp-START).days//3))
                    if not START<=a<END:
                        continue
                    b=min(a+timedelta(days=3),END)
                    key=(pair,a.isoformat(),b.isoformat())
                    old=events.get(key)
                    if old is None or excursion>old["observed_coarse_excursion"]:
                        events[key]={"window":list(key),"reference_close_utc":entry.isoformat(),
                            "crossing_bar_close_utc":t.isoformat(),"observed_coarse_excursion":excursion}
                break
    count=sum(START<t<=END for t in bars)
    return {"pair":pair,"response_sha256":hashlib.sha256(raw).hexdigest(),
            "raw_b64":base64.b64encode(raw).decode("ascii"),
            "observed_bars_in_window":count,"events":[events[k] for k in sorted(events)],
            "source_scope":"240M_DISCOVERY_ONLY_NOT_TRAINING_OR_NEGATIVE_LABELS"}

def discover(pairs,prior=None,*,budget=30,fetch_page=fetch,pause=time.sleep):
    if not 1<=budget<=60:
        raise ValueError("Invalid discovery budget")
    results={}
    attempts={}
    errors={}
    if prior:
        if prior.get("schema")!=SCHEMA or prior.get("digest")!=canonical_digest({k:v for k,v in prior.items() if k!="digest"}):
            raise ValueError("Coarse prior checksum mismatch")
        for item in prior["results"]:
            raw=base64.b64decode(item["raw_b64"],validate=True)
            if inspect(item["pair"],raw)!=item:
                raise ValueError("Coarse prior evidence mismatch")
            results[item["pair"]]=item
        attempts=dict(prior["attempts"])
        errors=dict(prior["errors"])
    selected=sorted(set(pairs)-set(results),key=lambda p:(attempts.get(p,0),p))[:budget]
    for pair in selected:
        attempts[pair]=attempts.get(pair,0)+1
        try:
            results[pair]=inspect(pair,fetch_page(pair))
            errors.pop(pair,None)
        except (ValueError,OSError,KeyError) as exc:
            errors[pair]=str(exc)[:200]
        pause(1.1)
    state={"schema":SCHEMA,"results":[results[k] for k in sorted(results)],"attempts":attempts,
           "errors":errors,"source_authenticated":False,"production_applied":False,
           "scope":"CURRENT_OBSERVED_UNIVERSE_COARSE_HISTORICAL_DISCOVERY_ONLY"}
    state["digest"]=canonical_digest(state)
    print(json.dumps({"coarse_discovery_scope":state["scope"],"observed_markets":len(set(pairs)&set(results)),
        "eligible_markets":len(set(pairs)),"new_attempts":len(selected),"errors":len(errors),
        "markets_with_events":sum(bool(x["events"]) for x in results.values()),
        "candidate_windows":sum(len(x["events"]) for x in results.values())},sort_keys=True))
    return state

def prioritized_windows(state):
    return [tuple(e["window"]) for item in state["results"] for e in item["events"]]
