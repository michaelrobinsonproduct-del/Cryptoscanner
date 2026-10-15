"""Diagnostic price-only ranking comparison on chronological unseen observations.

Not production feature parity. A successful diagnostic NEVER authorizes promotion.
"""
from collections import defaultdict

def compare_replay(events, *, min_cohorts=40):
    groups=defaultdict(list)
    for row in events:
        if isinstance(row,dict) and all(k in row for k in ("run_at","pair","prior_momentum_pct","future_gain_pct","baseline_selected","breakout")):
            groups[row["run_at"]].append(row)
    timestamps=sorted(groups)
    cut=int(len(timestamps)*0.7)
    holdout=timestamps[cut:]
    base_hits=challenger_hits=breakouts=0
    for t in holdout:
        cohort=groups[t]
        if not cohort:
            continue
        budget=sum(bool(r["baseline_selected"]) for r in cohort)
        # Strict equal selection budget. No budget means no simulated challenger selection.
        picks=sorted(cohort,key=lambda r:(-r["prior_momentum_pct"],r["pair"]))[:budget]
        breakouts+=sum(bool(r["breakout"]) for r in cohort)
        base_hits+=sum(bool(r["breakout"]) and bool(r["baseline_selected"]) for r in cohort)
        challenger_hits+=sum(bool(r["breakout"]) for r in picks)
    return {"status":"DIAGNOSTIC_ONLY","scope":"PRICE_ONLY_NOT_FEATURE_PARITY",
            "holdout_cohorts":len(holdout),"min_cohorts":min_cohorts,
            "breakouts":breakouts,"baseline_hits":base_hits,"challenger_hits":challenger_hits,
            "baseline_recall":base_hits/breakouts if breakouts else None,
            "challenger_recall":challenger_hits/breakouts if breakouts else None,
            "promotion_eligible":False,"live_weights_modified":False,"buy_approved":False}
