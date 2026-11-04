"""Read-only 48h cohort export gate between archive outcomes and held-out learning.

Keep all historical labels visible for diagnostics. Never pass unqualified
proxy-entry labels to the held-out evaluator or production promotion.
"""
import hashlib
import json


def export_learning_cohorts(execution, predictions):
    if execution.get("schema") != "historical_outcome_execution_v1":
        raise ValueError("Unknown historical execution schema")
    if not isinstance(predictions, list):
        raise ValueError("Missing candidate universe")
    by_id = {}
    for p in predictions:
        pid = p["prediction_id"]
        if pid in by_id:
            raise ValueError("Duplicate candidate")
        by_id[pid] = p
    rows = []
    excluded = {}
    records = execution["outcomes"]["records"]
    if len(records) != len(by_id):
        raise ValueError("Candidate/outcome count mismatch")
    for record in records:
        pid = record["prediction_id"]
        if pid not in by_id or record["pair"] != by_id[pid]["pair"]:
            raise ValueError("Unmatched historical candidate")
        labels = [x for x in record["labels"] if x["horizon_hours"] == 48]
        if len(labels) != 1:
            raise ValueError("Missing unique 48h label")
        label = labels[0]
        reasons = []
        if label["status"] != "MATURED_OBSERVED":
            reasons.append(label["status"])
        if not execution.get("source_authenticated", False) or not record.get("source_authenticated", False):
            reasons.append("UNAUTHENTICATED_ARCHIVE")
        if not label.get("qualified_for_learning", False):
            reasons.append("UNQUALIFIED_ENTRY_LIQUIDITY")
        if not by_id[pid].get("full_preselection_universe", False):
            reasons.append("MISSING_PRESELECTION_UNIVERSE")
        if reasons:
            for reason in reasons:
                excluded[reason] = excluded.get(reason, 0) + 1
        rows.append({"prediction_id": pid, "pair": record["pair"],
                     "horizon_hours": 48, "status": label["status"],
                     "observed_30pct_hit": label.get("observed_30pct_hit"),
                     "eligible": not reasons, "exclusion_reasons": reasons,
                     "source_sha256": record["source_sha256"]})
    qualified = [row for row in rows if row["eligible"]]
    # This interface is deliberately fail-closed. A future authenticated
    # pipeline needs a separately reviewed, source-qualified evaluator.
    if qualified:
        raise ValueError("Qualified cohorts require reviewed unbiased evaluator adapter")
    return {"schema": "historical_learning_cohort_gate_v1",
            "candidate_count": len(rows), "excluded_counts": excluded,
            "diagnostic_rows": rows, "qualified_cohorts": [],
            "learning_qualified_count": 0, "held_out_lift": None,
            "promotion_authorized": False, "production_applied": False}
