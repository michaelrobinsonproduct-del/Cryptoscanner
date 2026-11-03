"""E1 adapter: verify retained prospective batch receipts before outcome eligibility.

No backdating a snapshot to a five-minute grid; observation time is factual.
"""
import hashlib
import json
from pathlib import Path

from research.source_qualified_outcomes import qualify


def verified_rows(batch_directory):
    root = Path(batch_directory)
    manifest = json.loads((root / "manifest.json").read_bytes())
    if manifest.get("mode") != "ONE_SHOT_PROSPECTIVE_PUBLIC_TLS_RESEARCH_ONLY":
        raise ValueError("unsupported manifest")
    entries = manifest.get("entries")
    if not isinstance(entries, list) or len(entries) != manifest.get("pairs_requested"):
        raise ValueError("manifest coverage mismatch")
    if len({e.get("pair") for e in entries}) != len(entries):
        raise ValueError("duplicate pair")
    rows, abstentions = [], []
    for entry in entries:
        pair = entry["pair"]
        if entry["status"] != "ELIGIBLE":
            abstentions.append({"pair": pair, "reason": "NO_ELIGIBLE_SNAPSHOT"})
            continue
        receipts = entry["raw"]
        if len(receipts) != 2 or {r["stage"] for r in receipts} != {"depth", "trades"}:
            raise ValueError("incomplete source receipts")
        for receipt in receipts:
            filename = receipt["file"]
            if Path(filename).name != filename or "/" in filename or "\\" in filename:
                raise ValueError("unsafe receipt path")
            raw = (root / filename).read_bytes()
            if len(raw) != receipt["bytes"] or hashlib.sha256(raw).hexdigest() != receipt["sha256"]:
                raise ValueError("raw receipt mismatch")
        evidence_file = entry["evidence_file"]
        if Path(evidence_file).name != evidence_file:
            raise ValueError("unsafe evidence path")
        evidence = json.loads((root / evidence_file).read_bytes())
        if (evidence.get("pair_requested") != pair or
                evidence.get("pair_source") != entry["source_market"] or
                not evidence.get("eligible_point_in_time_snapshot")):
            raise ValueError("source identity mismatch")
        depth = next(r for r in receipts if r["stage"] == "depth")
        trades = next(r for r in receipts if r["stage"] == "trades")
        if (evidence["depth_receipt"]["sha256"] != depth["sha256"] or
                evidence["trades_receipt"]["sha256"] != trades["sha256"]):
            raise ValueError("evidence receipt mismatch")
        observed = evidence["depth_receipt"]["first_observed_at"]
        bid_event = float(evidence["bid_level_event_at"])
        ask_event = float(evidence["ask_level_event_at"])
        if not (0 <= observed - bid_event <= 600 and 0 <= observed - ask_event <= 600):
            raise ValueError("stale quote")
        rows.append({"pair": pair, "event_at": bid_event,
                     "first_observed_at": observed,
                     "source_sha256": depth["sha256"],
                     "bid": evidence["best_bid"], "ask": evidence["best_ask"],
                     "ask_event_at": ask_event,
                     "trade_source_sha256": trades["sha256"]})
    return rows, abstentions


def coverage(batch_directory, horizon_hours=1):
    rows, abstentions = verified_rows(batch_directory)
    # One-shot batches do not provide contiguous future intervals. Never
    # manufacture missing timestamps or treat a single quote as an episode.
    results = [qualify(row, [], horizon_hours) for row in rows]
    return {"snapshots_verified": len(rows),
            "abstentions": abstentions,
            "qualified_first_entry_episodes": sum(
                r["status"] == "QUALIFIED_OBSERVED_PATH" for r in results),
            "outcome_statuses": [r["status"] for r in results],
            "held_out_lift": None, "production_applied": False}
