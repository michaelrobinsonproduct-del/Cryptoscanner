"""Read-only missed-mover episode and pre-entry feature coverage diagnostics.

A price-only descriptive audit of the sealed PAPER market-wide observations.
NOT a model, independent trade opportunities, held-out lift, or intrabar highs.
No exchange requests or production writes.
"""
import argparse
import bisect
import datetime as dt
import json
import math
from decimal import Decimal
from collections import defaultdict

from research.marketwide_paper_outcomes import MAX_GAP, HORIZONS, timestamp


def wilson(successes, trials, z=1.96):
    """Descriptive binomial interval; temporal overlap violates independence."""
    if not trials:
        return None
    p = successes / trials
    denom = 1 + z*z/trials
    center = (p + z*z/(2*trials)) / denom
    radius = z*math.sqrt(p*(1-p)/trials + z*z/(4*trials*trials)) / denom
    return [max(0, center-radius), min(1, center+radius)]


def lagged_return(series, times, index, minutes, conflicting_times=()):
    """As-of return only if an older quote and continuous coverage exist."""
    at, entry, _ = series[index]
    target = at - dt.timedelta(minutes=minutes)
    j = bisect.bisect_right(times, target, hi=index) - 1
    if j < 0 or target - times[j] > MAX_GAP:
        return None
    # A past feature is not reliable when the retained quotes disagree at
    # any timestamp used to construct its lookback window.
    if bisect.bisect_left(conflicting_times, times[j]) < bisect.bisect_right(conflicting_times, at):
        return None
    segment = times[j:index+1]
    if any(b-a > MAX_GAP for a,b in zip(segment, segment[1:])):
        return None
    # Convert to a finite display statistic only after exact decimal division;
    # extreme but valid quote ratios must not become JSON Infinity/NaN.
    value = entry / series[j][1] - 1
    try:
        display = float(value)
    except (OverflowError, ValueError):
        return None
    return display if math.isfinite(display) else None



def chronological_readiness(records, runs, hours):
    """Audit whether an as-of, label-embargoed split is even measurable.

    Split is determined from ALL scan decision times, never from outcome labels.
    This is not a fitted model or a claim of predictive lift.
    """
    times = sorted(set(runs.values()))
    if len(times) < 2:
        return {"status":"INSUFFICIENT_SCAN_TIMES","cutoff":None}
    cutoff = times[min(len(times)-1, max(1, int(len(times)*0.7)))]
    embargo = dt.timedelta(hours=hours) + MAX_GAP
    train = [r for r in records if runs[r["run_id"]] + embargo <= cutoff]
    test = [r for r in records if runs[r["run_id"]] >= cutoff]
    def summary(rows):
        featured = [r for r in rows if r["lagged_returns"]["60m"] is not None]
        positive = [r for r in rows if r["hit_30"]]
        featured_positive = [r for r in positive if r["lagged_returns"]["60m"] is not None]
        return {"matured_cases":len(rows), "positive_cases":len(positive),
                "positive_pairs":len({r["pair"] for r in positive}),
                "lag_60m_covered":len(featured),
                "positive_lag_60m_covered":len(featured_positive)}
    a,b=summary(train),summary(test)
    return {"status":"DESCRIPTIVE_SPLIT_ONLY_NO_TRAINED_CHALLENGER",
            "cutoff":cutoff.isoformat(),
            "embargo_hours":hours + MAX_GAP.total_seconds()/3600,
            "excluded_crossing_cutoff":len(records)-len(train)-len(test),
            "train":a,"test":b,
            "model_evaluation_ready":(a["positive_lag_60m_covered"]>=10
                 and b["positive_lag_60m_covered"]>=10
                 and a["lag_60m_covered"]-a["positive_lag_60m_covered"]>=10
                 and b["lag_60m_covered"]-b["positive_lag_60m_covered"]>=10)}


def cluster_episodes(cases, hours):
    """Collapse overlapping same-pair entries within a fixed horizon from first entry.

    Do not chain through last-entry time: a continuous series of overlapping
    windows could otherwise merge unrelated moves days apart into one episode.
    """
    episodes = []
    for case in sorted(cases,key=lambda x:(x["pair"],x.get("decision_at",x["entry_at"]))):
        # An episode is defined by immutable PAPER decisions, not by stale
        # quote timestamps that can predate those decisions by minutes.
        t = timestamp(case.get("decision_at",case["entry_at"]))
        if (episodes and episodes[-1]["pair"]==case["pair"]
            and t-timestamp(episodes[-1]["first_decision_at"]) <= dt.timedelta(hours=hours)):
            episodes[-1]["entry_cases"] += 1
            episodes[-1]["last_entry_at"] = case["entry_at"]
            episodes[-1]["watch_captured"] |= case["watch"]
        else:
            episodes.append({"pair":case["pair"],"first_entry_at":case["entry_at"],
                             "first_decision_at":t.isoformat(),
                             "last_entry_at":case["entry_at"],"entry_cases":1,
                             "watch_captured":case["watch"],
                             "first_lagged_60m":case["lagged_returns"]["60m"],
                             "first_lagged_returns":dict(case["lagged_returns"]),
                             "first_peak_observed_return":case["peak_observed_return"]})
    return episodes

def analyze(state):
    from paper_pov.ledger import verify
    verify(state, 32_000_000)
    runs = {r["id"]: timestamp(r["as_of"]) for r in state["runs"]}
    latest = max(runs.values(), default=None)
    watches = {(p["run_id"], p["pair"]) for p in state["predictions"]}
    by_pair = defaultdict(list)
    quote_prices = defaultdict(dict)
    conflicting_quotes = defaultdict(set)
    for o in state["observations"]:
        at = timestamp(o["at"])
        price = Decimal(str(o["price"]))
        previous = quote_prices[o["pair"]].setdefault(at, price)
        if previous != price:
            conflicting_quotes[o["pair"]].add(at)
        by_pair[o["pair"]].append((at, price, o["run_id"]))
    output = {}
    for hours in HORIZONS:
        positives, negatives, cases, cases20 = [], [], [], []
        coverage = {"eligible": 0, "immature": 0, "abstain_gap": 0,
                    "abstain_conflicting_quotes": 0, "abstain_future_entry_quotes": 0, "matured": 0,
                    "watch_matured": 0, "watch_positive": 0, "movers": 0,
                    "watch_positive_20": 0, "movers_20": 0,
                    "feature_30m": 0, "feature_60m": 0, "feature_180m": 0,
                    "mover_feature_60m": 0}
        for pair, series in by_pair.items():
            series.sort()
            times = [s[0] for s in series]
            conflicts = sorted(conflicting_quotes[pair])
            for i, (at, entry, rid) in enumerate(series):
                coverage["eligible"] += 1
                start = runs[rid]
                target = start + dt.timedelta(hours=hours)
                if latest is None or latest < target + MAX_GAP:
                    coverage["immature"] += 1
                    continue
                # A quote timestamp later than its own decision cannot be an as-of entry.
                if at > start:
                    coverage["abstain_gap"] += 1
                    coverage["abstain_future_entry_quotes"] += 1
                    continue
                end = bisect.bisect_right(times, target+MAX_GAP, lo=i+1)
                future = series[i+1:end]
                # The PAPER decision is the immutable run as_of, not its
                # up-to-three-minute-old quote. A price move before the
                # decision is NOT a valid future mover.
                before = [(t,p) for t,p,_ in future if start < t <= target]
                anchors = [(t,p) for t,p,_ in future if target <= t <= target+MAX_GAP]
                timeline = [start] + [t for t,_ in before]
                ambiguous = (at in conflicting_quotes[pair] or
                             bisect.bisect_right(conflicts, start) <
                             bisect.bisect_right(conflicts, target+MAX_GAP))
                if ambiguous:
                    coverage["abstain_gap"] += 1
                    coverage["abstain_conflicting_quotes"] += 1
                    continue
                if (not before or not anchors or start-at > MAX_GAP
                    or any(b-a > MAX_GAP for a,b in zip(timeline,timeline[1:]))
                    or anchors[0][0]-timeline[-1] > MAX_GAP):
                    coverage["abstain_gap"] += 1
                    continue
                coverage["matured"] += 1
                selected = (rid,pair) in watches
                if selected:
                    coverage["watch_matured"] += 1
                peak_price = max(p for _,p in before)
                peak_decimal = peak_price/entry - 1
                try:
                    peak = float(peak_decimal)
                except (OverflowError, ValueError):
                    peak = None
                if peak is not None and not math.isfinite(peak):
                    peak = None
                # Convert the source's finite decimal price representation,
                # not the rounded floating-point return, into exact labels.
                # E.g. 120/100 must be a +20% hit, not 19.999999999999996%.
                hit20 = Decimal(str(peak_price)) >= Decimal(str(entry))*Decimal('1.20')
                hit = Decimal(str(peak_price)) >= Decimal(str(entry))*Decimal('1.30')
                if hit20:
                    coverage["movers_20"] += 1
                    if selected:
                        coverage["watch_positive_20"] += 1
                if hit:
                    coverage["movers"] += 1
                    if selected:
                        coverage["watch_positive"] += 1
                lag = {}
                for minutes in (30,60,180):
                    value = lagged_return(series,times,i,minutes,conflicts)
                    lag[str(minutes)+"m"] = value
                    if value is not None:
                        coverage["feature_"+str(minutes)+"m"] += 1
                if hit and lag["60m"] is not None:
                    coverage["mover_feature_60m"] += 1
                record = {"pair":pair,"entry_at":at.isoformat(),"run_id":rid,"decision_at":start.isoformat(),
                          "peak_observed_return":round(peak,8) if peak is not None else None,
                          "entry_quote_age_minutes":(start-at).total_seconds()/60,
                          "hit_20":hit20,"hit_30":hit,
                          "watch":selected,"lagged_returns":lag}
                if hit20:
                    cases20.append(record)
                if hit:
                    positives.append(record)
                    cases.append(record)
                else:
                    negatives.append(record)
        # Repeated overlapping entry/horizon labels are not independent movers.
        # Cluster same-pair positives whose entry times fall within one horizon.
        episodes = cluster_episodes(cases,hours)
        episodes20 = cluster_episodes(cases20,hours)
        episode_watch_count = sum(e["watch_captured"] for e in episodes)
        episode_watch_count_20 = sum(e["watch_captured"] for e in episodes20)
        episode_first_lags = [e["first_lagged_60m"] for e in episodes
                              if e["first_lagged_60m"] is not None]
        # Descriptive only: features cannot be backfilled for most first observations.
        def summarize_feature(records,key):
            vals = [r["lagged_returns"][key] for r in records
                    if r["lagged_returns"][key] is not None]
            ordered = sorted(vals)
            return {"n":len(vals),
                    "distinct_pairs":len({r["pair"] for r in records
                                          if r["lagged_returns"][key] is not None}),
                    "mean":(sum(vals)/len(vals) if vals and math.isfinite(sum(vals)) else None),
                    "positive_fraction":sum(v>0 for v in vals)/len(vals) if vals else None,
                    "median":(float((ordered[(len(ordered)-1)//2] + ordered[len(ordered)//2])/2)
                              if ordered else None),
                    "min":float(ordered[0]) if ordered else None,
                    "max":float(ordered[-1]) if ordered else None}
        # Episode-first-entry feature cohorts reduce, but do not eliminate,
        # overlapping-entry dependence. Keep distinct-pair sample counts visible.
        first_entries = [{"pair":e["pair"],"lagged_returns":e["first_lagged_returns"]}
                         for e in episodes]
        episode_features = {
            key:dict(summarize_feature(first_entries,key),
                     distinct_pairs=len({r["pair"] for r in first_entries
                                         if r["lagged_returns"][key] is not None}))
            for key in ("30m","60m","180m")}
        first_entries_20 = [{"pair":e["pair"],"lagged_returns":e["first_lagged_returns"]}
                            for e in episodes20]
        episode_features_20 = {key:summarize_feature(first_entries_20,key)
                               for key in ("30m","60m","180m")}
        assert coverage["eligible"]==coverage["matured"]+coverage["abstain_gap"]+coverage["immature"]
        assert coverage["movers"]==len(positives)
        assert coverage["movers_20"]==len(cases20)
        coverage["matured_fraction"] = (coverage["matured"]/coverage["eligible"]
                                        if coverage["eligible"] else None)
        coverage["distinct_matured_pairs"] = len({r["pair"] for r in positives+negatives})
        coverage["distinct_positive_pairs"] = len({r["pair"] for r in positives})
        # Only matured, non-abstained WATCH cases can be labeled nonhits.
        coverage["watch_false_positive_30"] = coverage["watch_matured"] - coverage["watch_positive"]
        coverage["watch_false_positive_20"] = coverage["watch_matured"] - coverage["watch_positive_20"]
        output[str(hours)] = {"coverage":coverage,"unique_mover_episodes":len(episodes),
            "unique_mover_pairs":len({e["pair"] for e in episodes}),
            "unique_mover_episodes_20":len(episodes20),
            "watch_captured_episodes_20":episode_watch_count_20,
            "watch_episode_recall_wilson_95_naive_20":wilson(episode_watch_count_20,len(episodes20)),
            "episode_first_entry_feature_distributions_20":episode_features_20,
            "watch_episode_recall_20":(sum(e["watch_captured"] for e in episodes20)/len(episodes20)
                                      if episodes20 else None),
            "watch_recall_20":(coverage["watch_positive_20"]/coverage["movers_20"]
                               if coverage["movers_20"] else None),
            "watch_precision_20":(coverage["watch_positive_20"]/coverage["watch_matured"]
                                  if coverage["watch_matured"] else None),
            "episodes":episodes,"mover_cases":cases,
            "watch_captured_episodes":episode_watch_count,
            "watch_episode_recall_30":episode_watch_count/len(episodes) if episodes else None,
            "watch_episode_recall_wilson_95_naive":wilson(episode_watch_count,len(episodes)),
            "episode_first_entry_feature_distributions":episode_features,
            "episode_first_lag_60m":{"n":len(episode_first_lags),
                "mean":sum(episode_first_lags)/len(episode_first_lags) if episode_first_lags else None},
            "watch_recall_30":coverage["watch_positive"]/coverage["movers"] if coverage["movers"] else None,
            "watch_precision_30":coverage["watch_positive"]/coverage["watch_matured"] if coverage["watch_matured"] else None,
            "watch_recall_wilson_95_naive":wilson(coverage["watch_positive"],coverage["movers"]),
            "watch_precision_wilson_95_naive":wilson(coverage["watch_positive"],coverage["watch_matured"]),
            "chronological_readiness":chronological_readiness(positives+negatives,runs,hours),
            "lag_60m_positive":summarize_feature(positives,"60m"),
            "lag_60m_negative":summarize_feature(negatives,"60m"),
            "pre_entry_price_feature_distributions":{
                key:{"positive_30":summarize_feature(positives,key),
                     "negative_30":summarize_feature(negatives,key)}
                for key in ("30m","60m","180m")}}
    return {"status":"DESCRIPTIVE_ONLY_NO_HELD_OUT_LIFT",
            "limitations":["Sampled PAPER ticker prices, not intrabar highs or complete Kraken history",
                           "Repeated pair/time entries and overlapping horizons are dependent",
                           "Wilson intervals assume independence and must NOT be used as model confidence",
                           "Only lagged price returns are available; no authenticated pre-entry volume, spread or order-book features",
                           "No predictive challenger was trained or tested"],
            "source":{"ledger_sha256":state["sha256"],"generation":state["generation"],
                      "source_authenticated":False,
                      "complete_market_history":False,
                      "eligible_for_model_promotion":False,
                      "data_scope":"SHA-verified PAPER snapshot ledger, not exchange-authenticated full history",
                      "runs":len(state["runs"]),"observations":len(state["observations"])},
            "horizons":output}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verified-ledger",required=True)
    parser.add_argument("--output",required=True)
    args = parser.parse_args()
    with open(args.verified_ledger) as f:
        state=json.load(f)
    result=analyze(state)
    with open(args.output,"w") as f:
        json.dump(result,f,indent=2,sort_keys=True,allow_nan=False)
    print(json.dumps({"source":result["source"],"horizons":{
        k:{"coverage":v["coverage"],"unique_mover_episodes":v["unique_mover_episodes"],
           "unique_mover_pairs":v["unique_mover_pairs"]}
        for k,v in result["horizons"].items()}},sort_keys=True))


if __name__=="__main__":
    main()
