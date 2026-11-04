"""Research-only, fail-closed binding of point-in-time score receipts to retained depth.

Never reconstruct a historical receipt from a later paper ledger. A score must
have been captured independently, before the depth entry observation.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

from research.prospective_outcome_adapter import verified_rows
from paper_pov.ledger import verify, canonical


def bind(ledger, batch_directory, score_receipts):
    verify(ledger)
    rows, abstentions = verified_rows(batch_directory)
    by_source = {(r["pair"], r["source_sha256"]): r for r in rows}
    predictions = {p["prediction_id"]: p for p in ledger["predictions"]}
    accepted, excluded, seen = [], [], set()
    for receipt in score_receipts:
        pid = receipt.get("prediction_id")
        if not isinstance(pid, str) or pid in seen:
            raise ValueError("duplicate or invalid acquisition prediction ID")
        seen.add(pid)
        prediction = predictions.get(pid)
        if prediction is None:
            excluded.append({"prediction_id": pid, "reason": "ORPHAN_SCORE_RECEIPT"})
            continue
        if receipt.get("pair") != prediction["pair"] or any(
            type(receipt.get(k)) not in (int, float)
            or not math.isfinite(receipt[k])
            or receipt[k] != prediction[k]
            for k in ("baseline_score", "challenger_score")
        ):
            excluded.append({"prediction_id": pid, "reason": "SCORE_IDENTITY_MISMATCH"})
            continue
        row = by_source.get((receipt["pair"], receipt.get("source_sha256")))
        if row is None:
            excluded.append({"prediction_id": pid, "reason": "NO_VERIFIED_DEPTH_SOURCE"})
            continue
        observed = receipt.get("score_observed_at")
        if (type(observed) not in (int, float) or not math.isfinite(observed)
                or observed < 0 or observed > row["first_observed_at"]):
            excluded.append({"prediction_id": pid, "reason": "SCORE_NOT_PRE_ENTRY"})
            continue
        if row.get("entry_liquidity_usd") is None or row["entry_liquidity_usd"] < 20:
            excluded.append({"prediction_id": pid, "reason": "INSUFFICIENT_VERIFIED_LIQUIDITY"})
            continue
        accepted.append({**receipt, "entry_first_observed_at": row["first_observed_at"],
                         "source_sha256": row["source_sha256"]})
    return {"schema": 1, "mode": "RESEARCH_ONLY_ACQUISITION_BINDING",
            "production_applied": False, "accepted": accepted, "excluded": excluded,
            "source_abstentions": abstentions, "verified_depth_rows": len(rows),
            "receipt_count": len(score_receipts),
            "accepted_count": len(accepted), "excluded_count": len(excluded)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--paper-ledger", required=True)
    p.add_argument("--batch-directory", required=True)
    p.add_argument("--score-receipts", required=True)
    p.add_argument("--output", required=True)
    a = p.parse_args()
    ledger = json.loads(Path(a.paper_ledger).read_bytes())
    receipts = json.loads(Path(a.score_receipts).read_bytes())
    if not isinstance(receipts, list):
        raise ValueError("score receipts must be a list")
    report = bind(ledger, a.batch_directory, receipts)
    from paper_pov.scanner import atomic_json
    atomic_json(a.output, report)
    print(json.dumps({k: report[k] for k in ("verified_depth_rows", "receipt_count",
                                             "accepted_count", "excluded_count")}, sort_keys=True))


if __name__ == "__main__":
    main()
