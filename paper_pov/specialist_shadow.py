"""Frozen specialist hypotheses for research-only early mover evaluation.

Scores are fixed, not calibrated probabilities. Historical replay is
retrospective even when all inputs are point-in-time. Never promote a winner
from this report or infer missing outcomes are negatives.
"""
import math

from .frozen_historical_shadow import NAMES
from .shadow_learning_evidence import canonical_digest, utc_time

HYPOTHESIS_VERSION = "fixed_early_surge_specialists_v1"
SPECIALISTS = ("accumulation", "continuation", "volume_anomaly", "reversal",
               "shard_relative_strength")


def specialist_scores(features):
    """Only existing as-of candles; avoid absolute prices and future outcomes."""
    if not all(type(features.get(n)) in (int, float)
               and math.isfinite(features[n]) for n in NAMES):
        return None
    m5, m15, m60, vol, trades, sigma = (features[n] for n in NAMES)
    if vol < 0 or trades < 0 or sigma < 0:
        return None
    activity = math.log1p(min(vol, 100)) + math.log1p(min(trades, 100))
    # Fixed scales declared before looking at outcomes; intentionally penalize
    # already large advances for the accumulation and anomaly hypotheses.
    return {
        "accumulation": activity - 20*abs(m60) - 40*sigma + 5*m15,
        "continuation": 10*max(0., min(m60, .10)) + 20*m15 + 5*m5
                        + .5*activity - 15*max(0., m60-.10),
        "volume_anomaly": activity - 10*max(0., m60-.03),
        "reversal": -10*m60 + 20*m15 + 10*m5 + .5*activity,
        # Within a contemporaneous shard this is a relative ranking, not
        # a market-index-adjusted return or evidence of full-market coverage.
        "shard_relative_strength": 10*m60 + 20*m15 - 10*sigma,
    }


def compare_specialists(batches, labels, *, scope):
    """Same candidate set, alert budget and common complete batches.

    Batches contain (rows, baseline_ids, challenger_ids); membership and
    scores are determined without inspecting labels. Include incomplete
    selections in observation bounds. Evaluate known positive anchor
    recall separately, not as full-market event recall.
    """
    names = ("baseline", "challenger") + SPECIALISTS
    result = {n: {"selected": 0, "complete_hits": 0, "complete_misses": 0,
                  "unknown": 0, "paired_selected": 0, "paired_hits": 0,
                  "known_hits": 0, "early_known_hits": 0} for n in names}
    paired = unavailable = skipped = positive_anchors = 0
    for rows, baseline, challenger in batches:
        by_id = {p["prediction_id"]: p for p in rows}
        if len(by_id) != len(rows):
            raise ValueError("Duplicate specialist candidate")
        budget = len(baseline)
        if not budget or budget != len(challenger):
            skipped += 1
            continue
        if (len(set(baseline)) != budget or len(set(challenger)) != budget
                or not set(baseline+challenger) <= set(by_id)):
            raise ValueError("Invalid specialist controls")
        scores = {k: specialist_scores(p.get("features", {})) for k,p in by_id.items()}
        if any(v is None for v in scores.values()):
            skipped += 1
            continue
        selected = {"baseline": baseline, "challenger": challenger}
        for name in SPECIALISTS:
            selected[name] = sorted(by_id, key=lambda k: (-scores[k][name], k))[:budget]
        known = {k:o for k in by_id if (o:=labels.get(k)) is not None
                 and o.get("coverage_complete") is True and type(o.get("hit")) is bool}
        positive_anchors += sum(o["hit"] for o in known.values())
        complete = all(k in known for ids in selected.values() for k in ids)
        paired += int(complete)
        unavailable += int(not complete)
        for name, ids in selected.items():
            m = result[name]
            for key in ids:
                m["selected"] += 1
                if key not in known:
                    m["unknown"] += 1
                    continue
                o = known[key]
                m["complete_hits" if o["hit"] else "complete_misses"] += 1
                if complete:
                    m["paired_selected"] += 1
                    m["paired_hits"] += int(o["hit"])
                if o["hit"]:
                    m["known_hits"] += 1
                    lead = o.get("observed_lead_hours_upper_bound")
                    if (type(lead) in (int,float) and math.isfinite(lead)
                        and 1+5/60 <= lead <= 48
                        and abs(by_id[key]["features"]["momentum_60m"]) <= .03):
                        m["early_known_hits"] += 1
    for m in result.values():
        n = m["selected"]
        m["precision_lower_bound"] = m["complete_hits"]/n if n else None
        m["precision_upper_bound"] = (m["complete_hits"]+m["unknown"])/n if n else None
        m["paired_precision"] = m["paired_hits"]/m["paired_selected"] if m["paired_selected"] else None
        m["paired_false_positives"] = m["paired_selected"]-m["paired_hits"]
        m["known_positive_anchor_recall"] = m["known_hits"]/positive_anchors if positive_anchors else None
        m["known_missed_positive_anchors"] = positive_anchors-m["known_hits"]
    report = {"schema": HYPOTHESIS_VERSION, "scope": scope, "common_complete_batches": paired,
              "incomplete_batches": unavailable, "skipped_batches": skipped,
              "known_positive_anchors": positive_anchors, "metrics": result,
              "measured_lift_verified": False, "promotion_authorized": False,
              "production_applied": False, "calibrated_probability": False}
    report["digest"] = canonical_digest(report)
    return report
