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


CONTEXT = ("return_6h", "return_24h", "has_6h_reference", "has_24h_reference",
           "relative_momentum_60m", "relative_activity", "has_cross_section",
           "quiet_6h_activity", "momentum_vs_6h_trend")


def historical_context(predictions):
    """Point-in-time hourly price references and same-time market context.

    Exact earlier observed anchors only; no interpolation or assumption of
    continuous hourly prices. Unknown context is encoded by explicit flags
    and neutral numeric inputs. Relative strength is against the observed
    archive cross section, not a verified live eligible universe.
    """
    from statistics import median
    by_pair_time={}
    sections={}
    prepared=[]
    for p in predictions:
        f=interaction_features(p.get("features",{}))
        if f is None:
            continue
        at=utc_time(p["entry_utc"])
        if utc_time(p["feature_asof_utc"])>at:
            raise ValueError("Context feature lookahead")
        pair=p.get("pair")
        price=p.get("entry_price")
        valid_price=type(price) in (int,float) and math.isfinite(price) and price>0
        if isinstance(pair,str) and pair and valid_price:
            identity=(pair,at)
            if identity in by_pair_time:
                raise ValueError("Duplicate contextual market anchor")
            by_pair_time[identity]=price
        sections.setdefault(at,[]).append((f["momentum_60m"],f["log_volume_accel"]+f["log_trade_accel"]))
        prepared.append((p,at,pair,price if valid_price else None,f))
    medians={at:(median(x[0] for x in rows),median(x[1] for x in rows))
             for at,rows in sections.items() if len(rows)>=10}
    result={}
    for p,at,pair,price,f in prepared:
        reference6=by_pair_time.get((pair,at-timedelta(hours=6)))
        reference24=by_pair_time.get((pair,at-timedelta(hours=24)))
        has6=price is not None and reference6 is not None
        has24=price is not None and reference24 is not None
        # Clip only the model input, not outcome returns or reference prices.
        ret6=max(-2.,min(2.,price/reference6-1)) if has6 else 0.
        ret24=max(-2.,min(2.,price/reference24-1)) if has24 else 0.
        activity=f["log_volume_accel"]+f["log_trade_accel"]
        relative=medians.get(at)
        values=(ret6,ret24,float(has6),float(has24),
                f["momentum_60m"]-relative[0] if relative is not None else 0.,
                activity-relative[1] if relative is not None else 0.,
                float(relative is not None),
                activity/(1+20*abs(ret6)) if has6 else 0.,
                f["momentum_60m"]-ret6/6 if has6 else 0.)
        result[p["prediction_id"]]={**f,**dict(zip(CONTEXT,values))}
    return result


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
    context=historical_context(predictions)
    contextual=[dict(p,features=context[p["prediction_id"]]) for p in predictions
                if p["prediction_id"] in context]
    fitted={}
    for name,target,inputs,feature_names in (
            ("learned_interactions",original,transformed,FEATURES),
            ("learned_early_objective",early,transformed,FEATURES),
            ("contextual_48h_objective",original,contextual,FEATURES+CONTEXT),
            ("contextual_early_objective",early,contextual,FEATURES+CONTEXT)):
        fit=train_shadow_challenger(inputs,target,training_end_utc=training_end_utc,
                                    holdout_start_utc=holdout_start_utc,feature_names=feature_names)
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
    context_coverage={}
    for name,group in (("before_training_cutoff",[p for p in contextual if utc_time(p["entry_utc"])<cutoff]),
                       ("heldout",[p for p in contextual if utc_time(p["entry_utc"])>=start])):
        context_coverage[name]={"anchors":len(group)}
        for flag in ("has_6h_reference","has_24h_reference","has_cross_section"):
            context_coverage[name][flag]=sum(int(p["features"][flag]) for p in group)
    result=dict(schema="learned_early_objectives_replay_v1",
                models={n:fit for n,(fit,_) in fitted.items()},metrics=metrics,
                contextual_feature_coverage=context_coverage,
                scope="RETROSPECTIVE_ARCHIVE_FEATURE_COMPLETE_UNIVERSE",
                early_definition="COMPLETE_30PCT_48H_60M_ABS_LE_3PCT_LEAD_LOWER_BOUND_GE_1H",
                calibrated_probability=False,measured_lift_verified=False,
                production_applied=False,promotion_authorized=False)
    result["digest"]=canonical_digest(result)
    return result
