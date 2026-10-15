"""Pure diagnostic checks for historical replay comparability."""
import math

def validate_replay(replay, comparison, *, min_cohorts=40, min_breakouts=20):
    reasons=[]
    if not isinstance(replay,dict) or not isinstance(comparison,dict):
        return {"valid":False,"reasons":["missing_input"],"promotion_eligible":False}
    if replay.get("scope")!="FULL_MARKET_PRICES_ONLY":
        reasons.append("unexpected_replay_scope")
    if comparison.get("scope")!="PRICE_ONLY_NOT_FEATURE_PARITY":
        reasons.append("unexpected_comparison_scope")
    if replay.get("feature_parity_verified") is not True:
        reasons.append("full_feature_parity_unverified")
    if type(comparison.get("holdout_cohorts")) is not int or comparison["holdout_cohorts"]<min_cohorts:
        reasons.append("insufficient_holdout_cohorts")
    if type(comparison.get("breakouts")) is not int or comparison["breakouts"]<min_breakouts:
        reasons.append("insufficient_breakout_events")
    for key in ("baseline_recall","challenger_recall"):
        v=comparison.get(key)
        if type(v) not in (float,int) or not math.isfinite(v) or not 0<=v<=1:
            reasons.append("invalid_"+key)
    return {"valid":not reasons,"reasons":reasons,"promotion_eligible":False,
            "mode":"DIAGNOSTIC_ONLY"}
