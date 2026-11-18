"""Bounded resumable historical trade-window recovery; isolated paper research."""
import argparse
from datetime import timedelta
import gzip
import hashlib
import json
from pathlib import Path
import shutil
import time
from .historical_trade_recovery import recover, replay
from .shadow_learning_evidence import utc_time, canonical_digest

SCHEMA="historical_trade_recovery_manifest_v1"

def window_keys(pairs):
    start,end=utc_time("2026-10-01T00:00:00Z"),utc_time("2026-11-06T00:00:00Z")
    dates=[]
    while start<end:
        stop=min(start+timedelta(days=3),end)
        dates.append((start.isoformat(),stop.isoformat()))
        start=stop
    return [(pair,a,b) for a,b in dates for pair in sorted(set(pairs))]

def key_name(key):
    pair,a,b=key
    return canonical_digest([pair,utc_time(a).isoformat(),utc_time(b).isoformat()])

def checked_state(directory, rec):
    path=directory/rec["key"]/"cursor-state.json.gz"
    if hashlib.sha256(path.read_bytes()).hexdigest()!=rec["sha256"]:
        raise ValueError("Cursor file checksum mismatch")
    with gzip.open(path,"rt") as f:
        state=json.load(f)
    if state.get("digest")!=canonical_digest({k:v for k,v in state.items() if k!="digest"}):
        raise ValueError("Cursor payload checksum mismatch")
    if key_name([state[k] for k in ("pair","start_utc","end_utc")])!=rec["key"]:
        raise ValueError("Cursor identity mismatch")
    if replay(state)[1]!=rec["completed"]:
        raise ValueError("Cursor completion mismatch")
    return state

def store(directory,state,cohort,summary,attempts):
    key=key_name([state[k] for k in ("pair","start_utc","end_utc")])
    folder=directory/key
    folder.mkdir(parents=True,exist_ok=True)
    p=folder/"cursor-state.json.gz"
    with gzip.open(p,"wt") as f:
        json.dump(state,f,separators=(",",":"))
    c=folder/"cohort.jsonl.gz"
    with gzip.open(c,"wt") as f:
        f.write(json.dumps(cohort,separators=(",",":"))+"\n")
    return {"key":key,"window":[state[k] for k in ("pair","start_utc","end_utc")],
            "sha256":hashlib.sha256(p.read_bytes()).hexdigest(),
            "cohort_sha256":hashlib.sha256(c.read_bytes()).hexdigest(),
            "completed":summary["cursor_window_reached"],"attempts":attempts,"summary":summary}

def run_batch(pairs,directory,*,prior=None,seed=None,batch_size=3,page_budget=10,fetch_page=None,pause=time.sleep,priority_windows=()):
    if not 1<=batch_size<=6 or not 1<=page_budget<=20:
        raise ValueError("Invalid bounded batch budget")
    directory=Path(directory)
    directory.mkdir(parents=True,exist_ok=True)
    pairs=sorted(set(pairs))
    if not pairs:
        raise ValueError("Empty observed market universe")
    records,failures={},{}
    if prior:
        prior=Path(prior)
        old=json.loads((prior/"manifest.json").read_text())
        if old.get("schema")!=SCHEMA or old.get("digest")!=canonical_digest({k:v for k,v in old.items() if k!="digest"}):
            raise ValueError("Manifest checksum mismatch")
        for rec in old["records"]:
            if rec["key"]!=key_name(rec["window"]) or rec["key"] in records:
                raise ValueError("Manifest identity mismatch")
            checked_state(prior,rec)
            c=prior/rec["key"]/"cohort.jsonl.gz"
            if hashlib.sha256(c.read_bytes()).hexdigest()!=rec["cohort_sha256"]:
                raise ValueError("Cohort checksum mismatch")
            shutil.copytree(prior/rec["key"],directory/rec["key"],dirs_exist_ok=True)
            records[rec["key"]]=rec
        failures=dict(old["failures"])
    elif seed:
        with gzip.open(Path(seed)/"cursor-state.json.gz","rt") as f:
            state=json.load(f)
        def reject_fetch(*args):
            raise ValueError("Seed must already be completed")
        state,cohort,summary=recover(state["pair"],state["start_utc"],state["end_utc"],
                                    previous=state,max_pages=1,fetch_page=reject_fetch)
        rec=store(directory,state,cohort,summary,1)
        records[rec["key"]]=rec
    keys=window_keys(pairs)
    pending=[k for k in keys if not records.get(key_name(k),{}).get("completed")]
    pending.sort(key=lambda k:(records.get(key_name(k),{}).get("attempts",0)+failures.get(key_name(k),{}).get("attempts",0),k[1],k[0]))
    priorities={key_name(k) for k in priority_windows}
    # Reserve one fair background/control window each batch. Prioritize
    # observed event windows, then resume an incomplete cursor if available.
    chosen=[]
    if batch_size>=2 and pending:
        chosen.append(pending[0])
        candidates=[k for k in pending if k not in chosen and key_name(k) in priorities]
        if candidates:
            chosen.append(candidates[0])
        resume=[k for k in pending if k not in chosen and key_name(k) in records]
        if resume and len(chosen)<batch_size:
            chosen.append(resume[0])
    chosen.extend(k for k in pending if k not in chosen)
    attempted=[]
    for key in chosen[:batch_size]:
        name=key_name(key)
        old=records.get(name)
        previous=checked_state(directory,old) if old else None
        # Preserve original timestamp spelling for resumable cursor identity.
        actual=tuple(old["window"]) if old else key
        options=dict(previous=previous,max_pages=page_budget,pause=pause)
        if fetch_page is not None:
            options["fetch_page"]=fetch_page
        try:
            state,cohort,summary=recover(*actual,**options)
            records[name]=store(directory,state,cohort,summary,(old or {}).get("attempts",0)+1)
            failures.pop(name,None)
            attempted.append(dict(window=list(key),completed=summary["cursor_window_reached"],
                pages=summary["pages"],candles=summary["completed_candles"],anchors=summary["anchors"]))
        except (ValueError,OSError,KeyError) as exc:
            failures[name]=dict(window=list(key),reason=str(exc)[:300],
                                attempts=failures.get(name,{}).get("attempts",0)+1)
            attempted.append(dict(window=list(key),error=str(exc)[:300]))
        pause(1.1)
    result=dict(schema=SCHEMA,universe_scope="CURRENT_OBSERVED_MARKETS_NOT_HISTORICAL_ELIGIBILITY",
        pairs=pairs,planned_windows=len(keys),completed_windows=sum(bool(records.get(key_name(k),{}).get("completed")) for k in keys),
        records=[records[k] for k in sorted(records)],failures=failures,attempted=attempted,
        source_authenticated=False,production_applied=False,promotion_authorized=False)
    result["digest"]=canonical_digest(result)
    (directory/"manifest.json").write_text(json.dumps(result,sort_keys=True)+"\n")
    print(json.dumps(dict(schema=SCHEMA,universe_count=len(pairs),planned_windows=len(keys),
        completed_windows=result["completed_windows"],retained_windows=len(records),
        failed_windows=len(failures),attempted=attempted),sort_keys=True))
    return result

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--ledger",type=Path,required=True)
    p.add_argument("--output-dir",type=Path,required=True)
    p.add_argument("--prior",type=Path)
    p.add_argument("--seed",type=Path)
    a=p.parse_args()
    ledger=json.loads(a.ledger.read_text())
    latest=ledger["runs"][-1]
    pairs={x["pair"] for x in ledger["observations"] if x["run_id"]==latest["id"]}
    if len(pairs)!=latest["observation_count"]:
        raise ValueError("Incomplete observed universe")
    from .historical_coarse_discovery import discover, prioritized_windows
    prior_discovery=None
    if a.prior and (a.prior/"coarse-discovery.json").is_file():
        prior_discovery=json.loads((a.prior/"coarse-discovery.json").read_text())
    discovery=discover(pairs,prior_discovery)
    run_batch(pairs,a.output_dir,prior=a.prior,seed=a.seed,
              priority_windows=prioritized_windows(discovery))
    (a.output_dir/"coarse-discovery.json").write_text(json.dumps(discovery,sort_keys=True)+"\n")

if __name__=="__main__":
    main()
