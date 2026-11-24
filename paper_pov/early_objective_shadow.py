"""Learned early-gainer objectives using only historical as-of features.

Research only. A 30% candle-high excursion is not an executable return.
Missing coverage is not a negative; early-positive timing is conservative.
"""
import math
from datetime import timedelta

from .frozen_historical_shadow import NAMES
from .heldout_outcome_adapter import train_shadow_challenger
from .shadow_learning_evidence import canonical_digest, utc_time

EXTRA = ("log_volume_accel", "log_trade_accel", "activity_x_quiet",
         "activity_x_positive_momentum", "momentum_acceleration", "reversal_activity",
         "extended_rally")
FEATURES = NAMES + EXTRA


def interaction_features(f):
    if not all(type(f.get(n)) in (int, float) and math.isfinite(f[n]) for n in NAMES):
        return None
    m5, m15, m60, volume, trades, sigma = (f[n] for n in NAMES)
    if min(volume, trades, sigma) < 0:
        return None
    v, t = math.log1p(min(volume,100)), math.log1p(min(trades,100))
    activity = v+t
    # Predeclared transformations, not fit using holdout observations.
    bounded = lambda x: max(-1., min(1., x))
    quiet = 1 / (1 + 40*abs(m60) + 80*sigma)
    extras = (v, t, activity*quiet, activity*max(0.,bounded(m15)),
              bounded(m5)-bounded(m60)/12, activity*max(0.,-bounded(m60))*max(0.,bounded(m5)),
              max(0.,bounded(m60)-.03))
    return {**{n:f[n] for n in NAMES}, **dict(zip(EXTRA, extras))}


def early_label(p, o):
    """Complete target: +30%, >=1h conservative lead, <=3% prior 60m move."""
    if o.get("coverage_complete") is not True or type(o.get("hit")) is not bool:
        return None
    if not o["hit"]:
        return False
    momentum=p.get("features",{}).get("momentum_60m")
    if type(momentum) not in (int,float) or not math.isfinite(momentum):
        return None
    if abs(momentum) > .03:
        return False
    lead=o.get("observed_lead_hours_upper_bound")
    if type(lead) not in (int,float) or not math.isfinite(lead) or not 0<lead<=48:
        return None
    return lead >= 1+5/60


def learned_replay(predictions, outcomes, batches, *, training_end_utc, holdout_start_utc):
    """Fit two frozen hypotheses, compare only on identical candidate batches.

    Original complete labels and complete early labels stay separate.
    All observed outcomes are retained in the evaluation; no holdout
    selection using the target, including missingness. Pairwise complete
    comparisons with the existing learned challenger complement broad bounds.
    """
    cutoff=utc_time(training_end_utc)
    start=utc_time(holdout_start_utc)
    if start < cutoff+timedelta(hours=48):
        raise ValueError("48h chronological purge required")
    by_id={}
    transformed=[]
    for p in predictions:
        key=p["prediction_id"]
        if key in by_id:
            raise ValueError("Duplicate learned candidate")
        if utc_time(p["feature_asof_utc"]) > utc_time(p["entry_utc"]):
            raise ValueError("Feature lookahead")
        by_id[key]=p
        f=interaction_features(p.get("features",{}))
        if f is not None:
            transformed.append(dict(p,features=f))
    labels={}
    early=[]
    original=[]
    for o in outcomes:
        key=o["prediction_id"]
        if o.get("horizon_hours")!=48 or key not in by_id:
            continue
        if key in labels:
            raise ValueError("Duplicate learned outcome")
        if utc_time(o["label_mature_utc"]) != utc_time(by_id[key]["entry_utc"])+timedelta(hours=48):
            raise ValueError("Invalid learned outcome maturity")
        labels[key]=o
        original.append(o)
        target=early_label(by_id[key],o)
        if target is not None:
            early.append(dict(o,hit=target))
    fitted={}
    for name,target in (("learned_interactions",original),("learned_early_objective",early)):
        fit=train_shadow_challenger(transformed,target,training_end_utc=training_end_utc,
                                    holdout_start_utc=holdout_start_utc,feature_names=FEATURES)
        scores=fit.pop("shadow_scores",{})
        fit["version"]=canonical_digest({k:v for k,v in fit.items() if k!="version"})
        fitted[name]=(fit,scores)
    names=("baseline","challenger",*fitted)
    def empty():
        return dict(selected=0,complete_hits=0,complete_misses=0,unknown=0,
                    partial_observed_hits=0,early_hits=0,early_unknown=0,
                    known_positive_anchors=0,known_missed_positive_anchors=0,
                    paired_batches_vs_challenger=0,paired_alerts_each=0,
                    paired_hits=0,paired_challenger_hits=0,
                    paired_early_alerts_each=0,paired_early_hits=0,paired_challenger_early_hits=0)
    metrics={n:empty() for n in names}
    for rows,base,control in batches:
        ids=[p["prediction_id"] for p in rows]
        budget=len(control)
        if (not budget or len(base)!=budget or len(ids)!=len(set(ids))
            or len(set(base))!=budget or len(set(control))!=budget
            or not set(base+control)<=set(ids)):
            raise ValueError("Invalid learned replay batch")
        if any(utc_time(by_id[k]["entry_utc"])<start for k in ids):
            raise ValueError("Pre-holdout candidate")
        ranks={"baseline":base,"challenger":control}
        for name,(fit,scores) in fitted.items():
            if fit["status"]=="SHADOW_ONLY" and all(k in scores for k in ids):
                ranks[name]=sorted(ids,key=lambda k:(-scores[k],k))[:budget]
        known={k:labels[k]["hit"] for k in ids if k in labels
               and labels[k].get("coverage_complete") is True and type(labels[k].get("hit")) is bool}
        early_known={k:v for k in known if (v:=early_label(by_id[k],labels[k])) is not None}
        positives=sum(known.values())
        for name,selection in ranks.items():
            m=metrics[name]
            m["known_positive_anchors"]+=positives
            m["known_missed_positive_anchors"]+=positives-sum(known.get(k,False) for k in selection)
            m["selected"]+=budget
            for k in selection:
                if k in known:
                    m["complete_hits" if known[k] else "complete_misses"]+=1
                else:
                    m["unknown"]+=1
                    o=labels.get(k,{})
                    if o.get("crossing_evidence")=="PARTIAL_WINDOW" and o.get("observed_crossing_candle_close_utc"):
                        crossing=utc_time(o["observed_crossing_candle_close_utc"])
                        entry=utc_time(by_id[k]["entry_utc"])
                        if entry<crossing<=entry+timedelta(hours=48):
                            m["partial_observed_hits"]+=1
                if k in early_known:
                    m["early_hits"]+=int(early_known[k])
                else:
                    m["early_unknown"]+=1
            if all(k in known for k in selection+control):
                m["paired_batches_vs_challenger"]+=1
                m["paired_alerts_each"]+=budget
                m["paired_hits"]+=sum(known[k] for k in selection)
                m["paired_challenger_hits"]+=sum(known[k] for k in control)
            if all(k in early_known for k in selection+control):
                m["paired_early_alerts_each"]+=budget
                m["paired_early_hits"]+=sum(early_known[k] for k in selection)
                m["paired_challenger_early_hits"]+=sum(early_known[k] for k in control)
    for m in metrics.values():
        n=m["selected"]
        m["observed_hit_lower_bound"]=m["complete_hits"]+m["partial_observed_hits"]
        m["precision_lower_bound"]=m["observed_hit_lower_bound"]/n if n else None
        m["precision_upper_bound"]=(m["complete_hits"]+m["unknown"])/n if n else None
        m["early_precision_lower_bound"]=m["early_hits"]/n if n else None
        m["early_precision_upper_bound"]=(m["early_hits"]+m["early_unknown"])/n if n else None
    result=dict(schema="learned_early_objectives_replay_v1",
                models={n:fit for n,(fit,_) in fitted.items()},metrics=metrics,
                scope="RETROSPECTIVE_ARCHIVE_FEATURE_COMPLETE_UNIVERSE",
                early_definition="COMPLETE_30PCT_48H_60M_ABS_LE_3PCT_LEAD_LOWER_BOUND_GE_1H",
                calibrated_probability=False,measured_lift_verified=False,
                production_applied=False,promotion_authorized=False)
    result["digest"]=canonical_digest(result)
    return result
