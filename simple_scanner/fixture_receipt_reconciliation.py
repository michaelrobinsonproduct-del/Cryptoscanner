"""Offline-only receipt reconciliation for fixture outbox; never performs HTTP.

A returned GitHub comment list must be supplied by an isolated caller. A timeout
with no matching comment remains unresolved: never blindly repost.
"""
import hashlib
import json
import re
from . import fixture_delivery_outbox as outbox

def marker(issue_number,run_id,digest):
    if type(issue_number) is not int or issue_number<=0 or not isinstance(run_id,str) or not run_id:
        raise ValueError("Invalid identity")
    if not isinstance(digest,str) or len(digest)!=64 or any(c not in "0123456789abcdef" for c in digest):
        raise ValueError("Invalid digest")
    return "SCANNER_RECEIPT:"+str(issue_number)+":"+run_id+":"+digest

def reconcile(root,issue_number,comments):
    """Read fixture comments; fail closed on duplicates/ambiguous data."""
    if not isinstance(comments,list):
        raise ValueError("Comments must be a complete fixture list")
    entries=[e for e in outbox.pending(root) if e["issue_number"]==issue_number]
    if len(entries)!=1:
        return "NOT_PENDING"
    entry=entries[0]
    expected=marker(issue_number,entry["run_id"],entry["sha256"])
    matches=[]
    for comment in comments:
        if not isinstance(comment,dict) or type(comment.get("id")) is not int or not isinstance(comment.get("body"),str):
            raise ValueError("Incomplete comment evidence")
        if re.search(r"(?<![A-Za-z0-9_])"+re.escape(expected)+r"(?![A-Za-z0-9_])",comment["body"]):
            matches.append(comment["id"])
    if len(matches)>1:
        return "DUPLICATE_REQUIRES_OPERATOR"
    if len(matches)==1:
        outbox.confirm(root,issue_number,entry["run_id"],entry["sha256"],matches[0])
        return "DELIVERED"
    return "UNRESOLVED_NO_REPOST"

def receipt_digest(receipt):
    return hashlib.sha256(json.dumps(receipt,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
