"""E2 research-only chronological same-cohort comparison; fail closed on weak evidence."""
from collections import Counter
from datetime import datetime, timezone
import math

PURGE_SECONDS = 48 * 3600


def compare(rows, *, split_at, min_test=20):
    """Compare precomputed point-in-time scores on identical qualified outcomes.

    Each row has pair, entry_first_observed_at (unix seconds), status,
    ge30pct, baseline_score, challenger_score. Neither model may train on
    the held-out cohort. A 48-hour purge separates training and evaluation.
    """
    if not math.isfinite(float(split_at)) or min_test < 1:
        raise ValueError("invalid split")
    seen = set()
    train, held, excluded = [], [], Counter()
    for row in rows:
        key = (row["pair"], row["entry_first_observed_at"])
        if key in seen:
            raise ValueError("duplicate cohort entry")
        seen.add(key)
        if row["status"] != "QUALIFIED_OBSERVED_PATH":
            excluded[row["status"]] += 1
            continue
        if not isinstance(row["ge30pct"], bool):
            raise ValueError("nonboolean qualified outcome")
        scores = [row.get("baseline_score"), row.get("challenger_score")]
        if any(type(s) not in (int, float) or not math.isfinite(s) for s in scores):
            excluded["MISSING_POINT_IN_TIME_SCORES"] += 1
            continue
        t = float(row["entry_first_observed_at"])
        if t < split_at - PURGE_SECONDS:
            train.append(row)
        elif t >= split_at:
            held.append(row)
        else:
            excluded["PURGED_48H"] += 1
    def metrics(cohort, score):
        ordered = sorted(cohort, key=lambda r: (-r[score],r["entry_first_observed_at"],r["pair"]))
        top = ordered[:max(1,len(ordered)//10)]
        return {"top_decile_n":len(top),"top_decile_hits":sum(r["ge30pct"] for r in top),
                "top_decile_hit_rate":sum(r["ge30pct"] for r in top)/len(top) if top else None}
    result={"train_n":len(train),"held_out_n":len(held),"excluded":dict(excluded),
            "purge_seconds":PURGE_SECONDS,"production_applied":False,
            "rule":"NO QUALIFIED RULE","held_out_lift":None}
    if len(train)<min_test or len(held)<min_test:
        return result
    base=metrics(held,"baseline_score")
    challenge=metrics(held,"challenger_score")
    result.update({"baseline":base,"challenger":challenge})
    if base["top_decile_hit_rate"] is not None:
        result["held_out_lift"]=challenge["top_decile_hit_rate"]-base["top_decile_hit_rate"]
    # Numeric lift alone never authorizes a production change.
    return result
