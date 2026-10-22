"""Fixture-only durable manual-result outbox; NOT imported by production execution.

Store a verified result before attempting delivery. Reconcile confirmed receipts
without rerunning a scan. No GitHub calls or production storage access.
"""
import hashlib
import json
import os
from pathlib import Path
import tempfile

FILENAME="fixture_delivery_outbox.json"
MAX_BYTES=65536

def _read(root):
    path=Path(root)/FILENAME
    if not path.exists():
        return {"entries":{}}
    raw=path.read_bytes()
    if len(raw)>MAX_BYTES:
        raise RuntimeError("Outbox too large")
    state=json.loads(raw)
    if not isinstance(state,dict) or not isinstance(state.get("entries"),dict):
        raise RuntimeError("Invalid outbox")
    for key,value in state["entries"].items():
        if not isinstance(key,str) or not isinstance(value,dict) or value.get("status") not in ("PENDING","DELIVERED"):
            raise RuntimeError("Invalid outbox entry")
    return state

def _write(root,state):
    directory=Path(root)
    encoded=json.dumps(state,sort_keys=True,separators=(",",":"),allow_nan=False).encode()
    if len(encoded)>MAX_BYTES:
        raise RuntimeError("Outbox too large")
    with tempfile.NamedTemporaryFile(dir=directory,prefix=".fixture_outbox_",delete=False) as handle:
        temp=Path(handle.name)
        try:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        except BaseException:
            temp.unlink(missing_ok=True)
            raise
    try:
        os.replace(temp,directory/FILENAME)
    finally:
        temp.unlink(missing_ok=True)

def stage(root,issue_number,run_id,receipt):
    """Idempotently persist one verified, research-only receipt."""
    if type(issue_number) is not int or issue_number<=0 or not isinstance(run_id,str) or not run_id:
        raise ValueError("Invalid request identity")
    if not isinstance(receipt,dict) or receipt.get("buy_approved") is not False or receipt.get("status")!="VERIFIED":
        raise ValueError("Only verified research receipts may be staged")
    key=str(issue_number)
    payload=json.dumps(receipt,sort_keys=True,separators=(",",":"),allow_nan=False)
    digest=hashlib.sha256(payload.encode()).hexdigest()
    state=_read(root)
    previous=state["entries"].get(key)
    if previous:
        if previous["run_id"]!=run_id or previous["sha256"]!=digest:
            raise RuntimeError("Conflicting receipt identity; manual reconciliation required")
        return previous
    entry={"issue_number":issue_number,"run_id":run_id,"sha256":digest,"receipt":receipt,"status":"PENDING"}
    state["entries"][key]=entry
    _write(root,state)
    return entry

def pending(root):
    return [item for _,item in sorted(_read(root)["entries"].items()) if item["status"]=="PENDING"]

def confirm(root,issue_number,run_id,receipt_sha256,comment_id):
    """Only a confirmed external comment ID transitions to delivered."""
    if type(comment_id) is not int or comment_id<=0:
        raise ValueError("Confirmed comment ID required")
    state=_read(root)
    entry=state["entries"].get(str(issue_number))
    if not entry or entry["run_id"]!=run_id or entry["sha256"]!=receipt_sha256:
        raise RuntimeError("Unmatched receipt confirmation")
    if entry["status"]=="DELIVERED":
        if entry.get("comment_id")!=comment_id:
            raise RuntimeError("Conflicting confirmation")
        return entry
    entry["status"]="DELIVERED"
    entry["comment_id"]=comment_id
    _write(root,state)
    return entry
