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


def lagged_return(series, times, index, minutes):
    """As-of return only if an older quote and continuous coverage exist."""
    at, entry, _ = series[index]
    target = at - dt.timedelta(minutes=minutes)
    j = bisect.bisect_right(times, target, hi=index) - 1
    if j < 0 or target - times[j] > MAX_GAP:
        return None
    segment = times[j:index+1]
    if any(b-a > MAX_GAP for a,b in zip(segment, segment[1:])):
        return None
    return entry / series[j][1] - 1



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
    """Collapse overlapping same-pair entry windows into descriptive episodes."""
    episodes = []
    for case in sorted(cases,key=lambda x:(x["pair"],x["entry_at"])):
        t = timestamp(case["entry_at"])
        if (episodes and episodes[-1]["pair"]==case["pair"]
            and t-timestamp(episodes[-1]["last_entry_at"]) <= dt.timedelta(hours=hours)):
            episodes[-1]["entry_cases"] += 1
            episodes[-1]["last_entry_at"] = case["entry_at"]
            episodes[-1]["watch_captured"] |= case["watch"]
        else:
            episodes.append({"pair":case["pair"],"first_entry_at":case["entry_at"],
                             "last_entry_at":case["entry_at"],"entry_cases":1,
                             "watch_captured":case["watch"],
                             "first_lagged_60m":case["lagged_returns"]["60m"],
                             "first_peak_observed_return":case["peak_observed_return"]})
    return episodes

def analyze(state):
    from paper_pov.ledger import verify
    verify(state, 32_000_000)
    runs = {r["id"]: timestamp(r["as_of"]) for r in state["runs"]}
    latest = max(runs.values(), default=None)
    watches = {(p["run_id"], p["pair"]) for p in state["predictions"]}
    by_pair = defaultdict(list)
    for o in state["observations"]:
        by_pair[o["pair"]].append((timestamp(o["at"]), float(o["price"]), o["run_id"]))
    output = {}
    for hours in HORIZONS:
        positives, negatives, cases, cases20 = [], [], [], []
        coverage = {"eligible": 0, "immature": 0, "abstain_gap": 0, "matured": 0,
                    "watch_matured": 0, "watch_positive": 0, "movers": 0,
                    "watch_positive_20": 0, "movers_20": 0,
                    "feature_30m": 0, "feature_60m": 0, "feature_180m": 0,
                    "mover_feature_60m": 0}
        for pair, series in by_pair.items():
            series.sort()
            times = [s[0] for s in series]
            for i, (at, entry, rid) in enumerate(series):
                coverage["eligible"] += 1
                start = runs[rid]
                target = start + dt.timedelta(hours=hours)
                if latest is None or latest < target + MAX_GAP:
                    coverage["immature"] += 1
                    continue
                end = bisect.bisect_right(times, target+MAX_GAP, lo=i+1)
                future = series[i+1:end]
                # The PAPER decision is the immutable run as_of, not its
                # up-to-three-minute-old quote. A price move before the
                # decision is NOT a valid future mover.
                before = [(t,p) for t,p,_ in future if start < t <= target]
                anchors = [(t,p) for t,p,_ in future if target <= t <= target+MAX_GAP]
                timeline = [start] + [t for t,_ in before]
                if (not before or not anchors or start-at > MAX_GAP
                    or any(b-a > MAX_GAP for a,b in zip(timeline,timeline[1:]))
                    or anchors[0][0]-timeline[-1] > MAX_GAP):
                    coverage["abstain_gap"] += 1
                    continue
                coverage["matured"] += 1
                selected = (rid,pair) in watches
                if selected:
                    coverage["watch_matured"] += 1
                peak = max(p for _,p in before)/entry - 1
                hit = peak >= 0.30
                if peak >= 0.20:
                    coverage["movers_20"] += 1
                    if selected:
                        coverage["watch_positive_20"] += 1
                if hit:
                    coverage["movers"] += 1
                    if selected:
                        coverage["watch_positive"] += 1
                lag = {}
                for minutes in (30,60,180):
                    value = lagged_return(series,times,i,minutes)
                    lag[str(minutes)+"m"] = value
                    if value is not None:
                        coverage["feature_"+str(minutes)+"m"] += 1
                if hit and lag["60m"] is not None:
                    coverage["mover_feature_60m"] += 1
                record = {"pair":pair,"entry_at":at.isoformat(),"run_id":rid,"decision_at":start.isoformat(),
                          "peak_observed_return":round(peak,8),
                          "hit_20":peak>=0.20,"hit_30":hit,
                          "watch":selected,"lagged_returns":lag}
                if peak >= 0.20:
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
        episode_first_lags = [e["first_lagged_60m"] for e in episodes
                              if e["first_lagged_60m"] is not None]
        # Descriptive only: features cannot be backfilled for most first observations.
        def summarize_feature(records,key):
            vals = [r["lagged_returns"][key] for r in records
                    if r["lagged_returns"][key] is not None]
            return {"n":len(vals),"mean":sum(vals)/len(vals) if vals else None,
                    "positive_fraction":sum(v>0 for v in vals)/len(vals) if vals else None}
        assert coverage["eligible"]==coverage["matured"]+coverage["abstain_gap"]+coverage["immature"]
        assert coverage["movers"]==len(positives)
        assert coverage["movers_20"]==len(cases20)
        output[str(hours)] = {"coverage":coverage,"unique_mover_episodes":len(episodes),
            "unique_mover_pairs":len({e["pair"] for e in episodes}),
            "unique_mover_episodes_20":len(episodes20),
            "watch_captured_episodes_20":sum(e["watch_captured"] for e in episodes20),
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
            "episode_first_lag_60m":{"n":len(episode_first_lags),
                "mean":sum(episode_first_lags)/len(episode_first_lags) if episode_first_lags else None},
            "watch_recall_30":coverage["watch_positive"]/coverage["movers"] if coverage["movers"] else None,
            "watch_precision_30":coverage["watch_positive"]/coverage["watch_matured"] if coverage["watch_matured"] else None,
            "watch_recall_wilson_95_naive":wilson(coverage["watch_positive"],coverage["movers"]),
            "watch_precision_wilson_95_naive":wilson(coverage["watch_positive"],coverage["watch_matured"]),
            "chronological_readiness":chronological_readiness(positives+negatives,runs,hours),
            "lag_60m_positive":summarize_feature(positives,"60m"),
            "lag_60m_negative":summarize_feature(negatives,"60m")}
    return {"status":"DESCRIPTIVE_ONLY_NO_HELD_OUT_LIFT",
            "limitations":["Sampled PAPER ticker prices, not intrabar highs or complete Kraken history",
                           "Repeated pair/time entries and overlapping horizons are dependent",
                           "Wilson intervals assume independence and must NOT be used as model confidence",
                           "Only lagged price returns are available; no authenticated pre-entry volume, spread or order-book features",
                           "No predictive challenger was trained or tested"],
            "source":{"ledger_sha256":state["sha256"],"generation":state["generation"],
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
