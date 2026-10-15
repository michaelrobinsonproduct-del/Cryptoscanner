"""Immutable model-version decisions; never writes live state or approves trading."""
import hashlib
import json

def fingerprint(weights):
    if not isinstance(weights, dict) or not weights:
        raise ValueError("missing model weights")
    if any(type(v) not in (int,float) or not (-1000 < v < 1000) for v in weights.values()):
        raise ValueError("invalid model weights")
    encoded=json.dumps(weights,sort_keys=True,separators=(",",":"),allow_nan=False)
    return hashlib.sha256(encoded.encode()).hexdigest()

def plan_transition(current, challenger, evidence, *, rollback_verified=False):
    """Produces a proposal, not a deployment or mutation."""
    if not isinstance(evidence,dict) or evidence.get("sufficient") is not True:
        return {"approved":False,"reason":"insufficient_evidence","live_weights_modified":False}
    if not rollback_verified:
        return {"approved":False,"reason":"rollback_not_verified","live_weights_modified":False}
    try:
        old=fingerprint(current);new=fingerprint(challenger)
    except (TypeError,ValueError):
        return {"approved":False,"reason":"invalid_model","live_weights_modified":False}
    if old==new:
        return {"approved":False,"reason":"unchanged_model","live_weights_modified":False}
    return {"approved":True,"reason":"proposal_only","from":old,"to":new,
            "rollback_to":old,"live_weights_modified":False,"buy_approved":False}
