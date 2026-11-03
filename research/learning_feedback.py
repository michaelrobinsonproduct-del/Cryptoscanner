"""E3 deterministic, versioned research-only learning decision and append-only ledger.

A challenger is never promoted by this module. Every decision is traceable to
an authenticated held-out comparison; insufficient or nonpositive lift keeps
the previous shadow version. Production configuration is never written.
"""
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path


def decide(comparison, *, baseline_version, challenger_version, evidence_sha256,
           min_held_out=20, min_positive_hits=1):
    if not all(isinstance(x, str) and x.strip() for x in (baseline_version, challenger_version)):
        raise ValueError("missing version")
    if baseline_version == challenger_version:
        raise ValueError("identical versions")
    if not isinstance(evidence_sha256,str) or len(evidence_sha256)!=64 or any(c not in "0123456789abcdef" for c in evidence_sha256):
        raise ValueError("invalid evidence hash")
    if comparison.get("production_applied") is not False:
        raise ValueError("comparison must be research-only")
    n=comparison.get("held_out_n")
    base=comparison.get("baseline")
    challenge=comparison.get("challenger")
    lift=comparison.get("held_out_lift")
    eligible=(type(n) is int and n>=min_held_out
              and isinstance(base,dict) and isinstance(challenge,dict)
              and type(lift) in (int,float) and math.isfinite(lift)
              and type(base.get("top_decile_hits")) is int
              and type(challenge.get("top_decile_hits")) is int
              and type(base.get("top_decile_n")) is int
              and type(challenge.get("top_decile_n")) is int
              and base["top_decile_n"]==challenge["top_decile_n"]>0
              and base["top_decile_hits"]<=base["top_decile_n"]
              and challenge["top_decile_hits"]<=challenge["top_decile_n"]
              and challenge["top_decile_hits"]>=min_positive_hits
              and abs(lift-(challenge["top_decile_hits"]-base["top_decile_hits"])/base["top_decile_n"])<1e-10)
    improved=bool(eligible and lift>0)
    return {"schema_version":1,"baseline_version":baseline_version,
            "challenger_version":challenger_version,"evidence_sha256":evidence_sha256,
            "held_out_n":n,"held_out_lift":lift if eligible else None,
            "decision":"SHADOW_ELIGIBLE_REVIEW" if improved else "KEEP_BASELINE",
            "active_shadow_version":challenger_version if improved else baseline_version,
            "production_applied":False}


def append_decision(path, decision):
    """Append only with lock/fsync and hash chain; never mutate previous entries."""
    if decision.get("production_applied") is not False:
        raise ValueError("production decision forbidden")
    path=Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("a+",encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(),fcntl.LOCK_EX)
        handle.seek(0)
        previous="0"*64
        for line in handle:
            row=json.loads(line)
            if row["previous_sha256"]!=previous:
                raise ValueError("broken learning ledger chain")
            payload=json.dumps(row["decision"],sort_keys=True,separators=(",",":"))
            expected=hashlib.sha256((previous+payload).encode()).hexdigest()
            if row["record_sha256"]!=expected:
                raise ValueError("tampered learning ledger")
            previous=expected
        if any(k not in decision for k in ("schema_version","decision","evidence_sha256")):
            raise ValueError("incomplete learning decision")
        payload=json.dumps(decision,sort_keys=True,separators=(",",":"))
        digest=hashlib.sha256((previous+payload).encode()).hexdigest()
        record={"previous_sha256":previous,"record_sha256":digest,"decision":decision}
        handle.seek(0,os.SEEK_END)
        handle.write(json.dumps(record,sort_keys=True,separators=(",",":"))+"\n")
        handle.flush()
        os.fsync(handle.fileno())
    return record
