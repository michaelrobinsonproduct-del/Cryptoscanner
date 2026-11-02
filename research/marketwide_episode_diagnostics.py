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


def lagged_return_diagnostic(series, times, index, minutes, conflicting_times=()):
    """As-of finite price return and mutually exclusive missingness reason.

    Preserve exact Decimal arithmetic and all historical quote-conflict checks.
    Missing anchors are never backfilled by a later observation.
    """
    at, entry, _ = series[index]
    target = at - dt.timedelta(minutes=minutes)
    j = bisect.bisect_right(times, target, hi=index) - 1
    if j < 0:
        return None, "no_prior_anchor"
    if target - times[j] > MAX_GAP:
        return None, "stale_prior_anchor"
    first_anchor = bisect.bisect_left(times, times[j], hi=j)
    if any(series[k][1] != series[j][1] for k in range(first_anchor, j)):
        return None, "conflicting_anchor"
    if any(times[k] == times[k+1] and series[k][1] != series[k+1][1]
           for k in range(j, index)):
        return None, "conflicting_history"
    if bisect.bisect_left(conflicting_times, times[j]) < bisect.bisect_right(conflicting_times, at):
        return None, "conflicting_history"
    segment = times[j:index+1]
    if any(b-a > MAX_GAP for a,b in zip(segment, segment[1:])):
        return None, "discontinuous_history"
    value = entry / series[j][1] - 1
    try:
        display = float(value)
    except (OverflowError, ValueError):
        return None, "nonfinite_return"
    if not math.isfinite(display):
        return None, "nonfinite_return"
    return display, "covered"


def lagged_return(series, times, index, minutes, conflicting_times=()):
    """Backward-compatible value-only API; no lookahead or imputation."""
    return lagged_return_diagnostic(series, times, index, minutes, conflicting_times)[0]


def chronological_readiness(records, runs, hours, positive_key="hit_30"):
    """Audit whether an as-of, label-embargoed split is even measurable.

    Split is determined from ALL scan decision times, never from outcome labels.
    This is not a fitted model or a claim of predictive lift.
    """
    times = sorted(set(runs.values()))
    if len(times) < 2:
        return {"status":"INSUFFICIENT_SCAN_TIMES","cutoff":None,
                "model_evaluation_ready":False,"sample_thresholds_met":False,
                "unmet_evidence_gates":["exchange_authenticated_market_history",
                                        "point_in_time_execution_features",
                                        "independent_held_out_challenger"]}
    cutoff = times[min(len(times)-1, max(1, int(len(times)*0.7)))]
    embargo = dt.timedelta(hours=hours) + MAX_GAP
    train = [r for r in records if runs[r["run_id"]] + embargo <= cutoff]
    test = [r for r in records if runs[r["run_id"]] >= cutoff]
    # Identify episode first entries BEFORE partitioning, otherwise a later
    # post-cutoff entry can masquerade as a fresh held-out opportunity and
    # backfill a pre-surge feature missing from the actual first entry.
    global_episode_first = set()
    first_by_pair = {}
    for r in sorted((r for r in records if r[positive_key]),
                    key=lambda x:(x["pair"], runs[x["run_id"]])):
        decision = runs[r["run_id"]]
        first = first_by_pair.get(r["pair"])
        if first is None or decision-first > dt.timedelta(hours=hours):
            first_by_pair[r["pair"]] = decision
            global_episode_first.add((r["pair"], r["run_id"]))
    def first_entry_feature_reasons(first_positives):
        """Conserve missingness at globally identified first positive decisions.

        Later overlapping positives cannot replace an embargoed first entry.
        """
        result = {lag:{"episodes":0,"with_asof_feature":0,
                       "without_asof_feature":0,"missing_reasons":{}}
                  for lag in ("30m","60m","180m")}
        for r in first_positives:
            for lag, stats in result.items():
                stats["episodes"] += 1
                if r["lagged_returns"].get(lag) is not None:
                    stats["with_asof_feature"] += 1
                else:
                    stats["without_asof_feature"] += 1
                    reason = r.get("lagged_return_reasons", {}).get(lag) or "reason_unavailable"
                    stats["missing_reasons"][reason] = stats["missing_reasons"].get(reason,0)+1
        for stats in result.values():
            stats["missing_reasons"] = dict(sorted(stats["missing_reasons"].items()))
            assert stats["episodes"] == stats["with_asof_feature"] + stats["without_asof_feature"]
            assert stats["without_asof_feature"] == sum(stats["missing_reasons"].values())
        return result

    def summary(rows):
        featured = [r for r in rows if r["lagged_returns"]["60m"] is not None]
        positive = [r for r in rows if r[positive_key]]
        featured_positive = [r for r in positive if r["lagged_returns"]["60m"] is not None]
        featured_negative = [r for r in featured if not r[positive_key]]
        first_positives = [r for r in positive if
                           (r["pair"], r["run_id"]) in global_episode_first]
        return {"matured_cases":len(rows), "positive_cases":len(positive),
                "positive_pairs":len({r["pair"] for r in positive}),
                "positive_episodes":len(first_positives),
                "lag_60m_covered":len(featured),
                "positive_lag_60m_covered":len(featured_positive),
                "positive_lag_60m_episodes":sum(r["lagged_returns"]["60m"] is not None
                    for r in first_positives),
                "positive_first_entry_feature_coverage":first_entry_feature_reasons(first_positives),
                "negative_lag_60m_pairs":len({r["pair"] for r in featured_negative})}
    a,b=summary(train),summary(test)
    for cohort in (a,b):
        reasons = cohort["positive_first_entry_feature_coverage"]
        assert reasons["60m"]["with_asof_feature"] == cohort["positive_lag_60m_episodes"]
        assert all(stats["episodes"] == cohort["positive_episodes"] for stats in reasons.values())
    # Concrete missing sample requirements, not a fabricated trained model.
    # The >=10 thresholds are a minimal readiness diagnostic, not statistical
    # proof of generalization or independent exchange-authenticated coverage.
    blockers = []
    for name, cohort in (("train",a),("test",b)):
        if cohort["positive_lag_60m_episodes"] < 10:
            blockers.append({"partition":name,"requirement":"episode_first_positive_lag_60m",
                             "required":10,"observed":cohort["positive_lag_60m_episodes"]})
        if cohort["negative_lag_60m_pairs"] < 10:
            blockers.append({"partition":name,"requirement":"distinct_negative_lag_60m_pairs",
                             "required":10,"observed":cohort["negative_lag_60m_pairs"]})
    return {"status":"DESCRIPTIVE_SPLIT_ONLY_NO_TRAINED_CHALLENGER",
            "cutoff":cutoff.isoformat(),
            "embargo_hours":hours + MAX_GAP.total_seconds()/3600,
            "excluded_crossing_cutoff":len(records)-len(train)-len(test),
            "train":a,"test":b,
            "minimum_sample_requirements":blockers,
            "sample_thresholds_met":not blockers,
            "unmet_evidence_gates":["exchange_authenticated_market_history",
                                    "point_in_time_execution_features",
                                    "independent_held_out_challenger"],
            "model_evaluation_ready":False}


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
            episodes[-1]["last_decision_at"] = t.isoformat()
            if case["watch"] and episodes[-1]["first_watch_decision_at"] is None:
                episodes[-1]["first_watch_decision_at"] = t.isoformat()
            episodes[-1]["watch_captured"] |= case["watch"]
            # Same-decision observations are unordered; WATCH is first-entry.
            if case["watch"] and t == timestamp(episodes[-1]["first_decision_at"]):
                episodes[-1]["first_entry_watch"] = True
        else:
            episodes.append({"pair":case["pair"],"first_entry_at":case["entry_at"],
                             "first_decision_at":t.isoformat(),
                             "last_decision_at":t.isoformat(),
                             "last_entry_at":case["entry_at"],"entry_cases":1,
                             "watch_captured":case["watch"],
                             "first_entry_watch":bool(case["watch"]),
                             "first_watch_decision_at":t.isoformat() if case["watch"] else None,
                             "first_lagged_60m":case["lagged_returns"]["60m"],
                             "first_lagged_returns":dict(case["lagged_returns"]),
                             "first_lagged_reasons":dict(case.get("lagged_return_reasons", {})),
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
        positives, negatives, negatives20, cases, cases20 = [], [], [], [], []
        coverage = {"eligible": 0, "immature": 0, "abstain_gap": 0,
                    "abstain_conflicting_quotes": 0, "abstain_future_entry_quotes": 0,
                    "abstain_no_future_observation": 0, "abstain_missing_horizon_anchor": 0,
                    "abstain_stale_entry": 0, "abstain_discontinuous_path": 0,
                    "matured": 0,
                    "watch_eligible": 0, "watch_immature": 0, "watch_abstain_gap": 0,
                    "watch_abstain_conflicting_quotes": 0, "watch_abstain_future_entry_quotes": 0,
                    "watch_abstain_no_future_observation": 0,
                    "watch_abstain_missing_horizon_anchor": 0,
                    "watch_abstain_stale_entry": 0, "watch_abstain_discontinuous_path": 0,
                    "watch_matured": 0, "watch_positive": 0, "movers": 0,
                    "watch_positive_20": 0, "movers_20": 0,
                    "feature_30m": 0, "feature_60m": 0, "feature_180m": 0,
                    "mover_feature_60m": 0}
        # Per-observed-pair denominators. No inferred unobserved Kraken markets.
        pair_keys = ("eligible", "matured", "immature", "abstain_gap",
                     "watch_eligible", "watch_matured", "watch_immature",
                     "watch_abstain_gap", "movers_20", "movers",
                     "watch_positive_20", "watch_positive")
        gap_reason_keys = ("conflicting_quotes", "future_entry_quotes",
                           "no_future_observation", "missing_horizon_anchor",
                           "stale_entry", "discontinuous_path")
        per_pair = {pair: {**{key: 0 for key in pair_keys},
                           "gap_reasons":{reason:0 for reason in gap_reason_keys}}
                    for pair in by_pair}
        for pair, series in by_pair.items():
            pair_counts = per_pair[pair]
            series.sort()
            times = [s[0] for s in series]
            conflicts = sorted(conflicting_quotes[pair])
            for i, (at, entry, rid) in enumerate(series):
                coverage["eligible"] += 1
                pair_counts["eligible"] += 1
                selected = (rid,pair) in watches
                if selected:
                    coverage["watch_eligible"] += 1
                    pair_counts["watch_eligible"] += 1
                start = runs[rid]
                target = start + dt.timedelta(hours=hours)
                if latest is None or latest < target + MAX_GAP:
                    coverage["immature"] += 1
                    pair_counts["immature"] += 1
                    if selected:
                        coverage["watch_immature"] += 1
                        pair_counts["watch_immature"] += 1
                    continue
                # A quote timestamp later than its own decision cannot be an as-of entry.
                if at > start:
                    coverage["abstain_gap"] += 1
                    pair_counts["abstain_gap"] += 1
                    coverage["abstain_future_entry_quotes"] += 1
                    pair_counts["gap_reasons"]["future_entry_quotes"] += 1
                    if selected:
                        coverage["watch_abstain_gap"] += 1
                        pair_counts["watch_abstain_gap"] += 1
                        coverage["watch_abstain_future_entry_quotes"] += 1
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
                    pair_counts["abstain_gap"] += 1
                    coverage["abstain_conflicting_quotes"] += 1
                    pair_counts["gap_reasons"]["conflicting_quotes"] += 1
                    if selected:
                        coverage["watch_abstain_gap"] += 1
                        pair_counts["watch_abstain_gap"] += 1
                        coverage["watch_abstain_conflicting_quotes"] += 1
                    continue
                # One mutually exclusive primary reason for every unknown label.
                reason = None
                if not before:
                    reason = "abstain_no_future_observation"
                elif not anchors:
                    reason = "abstain_missing_horizon_anchor"
                elif start-at > MAX_GAP:
                    reason = "abstain_stale_entry"
                elif (any(b-a > MAX_GAP for a,b in zip(timeline,timeline[1:]))
                      or anchors[0][0]-timeline[-1] > MAX_GAP):
                    reason = "abstain_discontinuous_path"
                if reason is not None:
                    coverage["abstain_gap"] += 1
                    pair_counts["abstain_gap"] += 1
                    coverage[reason] += 1
                    pair_counts["gap_reasons"][reason.removeprefix("abstain_")] += 1
                    if selected:
                        coverage["watch_abstain_gap"] += 1
                        pair_counts["watch_abstain_gap"] += 1
                        coverage["watch_" + reason] += 1
                    continue
                coverage["matured"] += 1
                pair_counts["matured"] += 1
                if selected:
                    coverage["watch_matured"] += 1
                    pair_counts["watch_matured"] += 1
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
                    pair_counts["movers_20"] += 1
                    if selected:
                        coverage["watch_positive_20"] += 1
                        pair_counts["watch_positive_20"] += 1
                if hit:
                    coverage["movers"] += 1
                    pair_counts["movers"] += 1
                    if selected:
                        coverage["watch_positive"] += 1
                        pair_counts["watch_positive"] += 1
                lag = {}
                lag_reasons = {}
                for minutes in (30,60,180):
                    value, reason = lagged_return_diagnostic(series,times,i,minutes,conflicts)
                    lag[str(minutes)+"m"] = value
                    lag_reasons[str(minutes)+"m"] = reason
                    if value is not None:
                        coverage["feature_"+str(minutes)+"m"] += 1
                if hit and lag["60m"] is not None:
                    coverage["mover_feature_60m"] += 1
                record = {"pair":pair,"entry_at":at.isoformat(),"run_id":rid,"decision_at":start.isoformat(),
                          "peak_observed_return":round(peak,8) if peak is not None else None,
                          "entry_quote_age_minutes":(start-at).total_seconds()/60,
                          "hit_20":hit20,"hit_30":hit,
                          "watch":selected,"lagged_returns":lag,
                          "lagged_return_reasons":lag_reasons}
                if hit20:
                    cases20.append(record)
                else:
                    negatives20.append(record)
                if hit:
                    positives.append(record)
                    cases.append(record)
                else:
                    negatives.append(record)
        # Conservation holds over every observed pair, not merely the top-N
        # display. The bounded list is descriptive coverage triage, not an
        # invented list of missing/unseen exchange markets.
        pair_totals = {key: sum(row[key] for row in per_pair.values())
                       for key in pair_keys}
        assert all(pair_totals[key] == coverage[key] for key in pair_keys)
        assert all(row["eligible"] == row["matured"] + row["immature"] +
                   row["abstain_gap"] and
                   row["watch_eligible"] == row["watch_matured"] +
                   row["watch_immature"] + row["watch_abstain_gap"] and
                   row["abstain_gap"] == sum(row["gap_reasons"].values())
                   for row in per_pair.values())
        assert all(sum(row["gap_reasons"][reason] for row in per_pair.values())
                   == coverage["abstain_" + reason] for reason in gap_reason_keys)
        top_gap_pairs = [
            {"pair":pair, **per_pair[pair]}
            for pair in sorted(per_pair,
                               key=lambda p: (-per_pair[p]["abstain_gap"], p))
            if per_pair[pair]["abstain_gap"] > 0
        ][:10]
        # Repeated overlapping entry/horizon labels are not independent movers.
        # Cluster same-pair positives whose entry times fall within one horizon.
        episodes = cluster_episodes(cases,hours)
        episodes20 = cluster_episodes(cases20,hours)
        episode_watch_count = sum(e["watch_captured"] for e in episodes)
        episode_watch_count_20 = sum(e["watch_captured"] for e in episodes20)
        # First qualifying entry is not necessarily the true pre-surge onset.
        first_watch_count = sum(e["first_entry_watch"] for e in episodes)
        first_watch_count_20 = sum(e["first_entry_watch"] for e in episodes20)
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
        # Attribute first-entry missingness without using later surge entries.
        def first_entry_coverage(distributions, episode_rows):
            result = {}
            for lag,stats in distributions.items():
                reasons = defaultdict(int)
                for episode in episode_rows:
                    if episode["first_lagged_returns"][lag] is None:
                        reasons[episode["first_lagged_reasons"][lag]] += 1
                total = len(episode_rows)
                result[lag] = {"episodes":total,
                               "with_asof_feature":stats["n"],
                               "without_asof_feature":total-stats["n"],
                               "missing_reasons":dict(sorted(reasons.items())),
                               "distinct_covered_pairs":stats["distinct_pairs"],
                               "covered_fraction":stats["n"]/total if total else None}
                assert sum(reasons.values()) == result[lag]["without_asof_feature"]
            return result
        first_coverage_20 = first_entry_coverage(episode_features_20,episodes20)
        first_coverage_30 = first_entry_coverage(episode_features,episodes)
        assert all(v["with_asof_feature"]+v["without_asof_feature"]==v["episodes"]
                   and 0 <= v["distinct_covered_pairs"] <= v["with_asof_feature"]
                   for v in list(first_coverage_20.values())+list(first_coverage_30.values()))
        assert coverage["eligible"]==coverage["matured"]+coverage["abstain_gap"]+coverage["immature"]
        gap_reasons = ("abstain_conflicting_quotes", "abstain_future_entry_quotes",
                       "abstain_no_future_observation", "abstain_missing_horizon_anchor",
                       "abstain_stale_entry", "abstain_discontinuous_path")
        assert coverage["abstain_gap"] == sum(coverage[k] for k in gap_reasons)
        assert coverage["watch_abstain_gap"] == sum(coverage["watch_" + k] for k in gap_reasons)
        assert all(coverage["watch_" + k] <= coverage[k] for k in gap_reasons)
        assert coverage["movers"]==len(positives)
        assert coverage["movers_20"]==len(cases20)
        assert coverage["matured"]==len(cases20)+len(negatives20)
        assert coverage["watch_eligible"] == (coverage["watch_matured"] +
            coverage["watch_immature"] + coverage["watch_abstain_gap"])
        coverage["matured_fraction"] = (coverage["matured"]/coverage["eligible"]
                                        if coverage["eligible"] else None)
        coverage["distinct_matured_pairs"] = len({r["pair"] for r in positives+negatives})
        coverage["distinct_positive_pairs"] = len({r["pair"] for r in positives})
        # Overlapping matured WATCH nonhits are not independent negative bets.
        nonhit_windows_20 = cluster_episodes([r for r in negatives20 if r["watch"]],hours)
        nonhit_windows_30 = cluster_episodes([r for r in negatives if r["watch"]],hours)
        assert len(nonhit_windows_20) <= sum(r["watch"] for r in negatives20)
        assert len(nonhit_windows_30) <= sum(r["watch"] for r in negatives)
        # Only matured, non-abstained WATCH cases can be labeled nonhits.
        coverage["watch_false_positive_30"] = coverage["watch_matured"] - coverage["watch_positive"]
        coverage["watch_false_positive_20"] = coverage["watch_matured"] - coverage["watch_positive_20"]
        coverage["missed_20"] = coverage["movers_20"] - coverage["watch_positive_20"]
        coverage["missed_30"] = coverage["movers"] - coverage["watch_positive"]
        output[str(hours)] = {"coverage":coverage,
            "pair_coverage":{"observed_pairs":len(per_pair),
                             "pairs_with_gap":sum(v["abstain_gap"] > 0 for v in per_pair.values()),
                             "totals":pair_totals,
                             "gap_reason_totals":{
                                 reason:sum(row["gap_reasons"][reason]
                                            for row in per_pair.values())
                                 for reason in gap_reason_keys},
                             "top_gap_pairs":top_gap_pairs,
                             "top_gap_pairs_limit":10,
                             "scope":"observed PAPER pairs only; no inferred unobserved markets"},
            "unique_mover_episodes":len(episodes),
            "unique_mover_pairs":len({e["pair"] for e in episodes}),
            "unique_mover_episodes_20":len(episodes20),
            "watch_nonhit_windows_20":len(nonhit_windows_20),
            "watch_nonhit_windows_30":len(nonhit_windows_30),
            "watch_nonhit_distinct_pairs_20":len({e["pair"] for e in nonhit_windows_20}),
            "watch_nonhit_distinct_pairs_30":len({e["pair"] for e in nonhit_windows_30}),
            "missed_mover_episodes_20":len(episodes20)-episode_watch_count_20,
            "missed_mover_episodes_30":len(episodes)-episode_watch_count,
            "watch_captured_episodes_20":episode_watch_count_20,
            "watch_first_entry_episodes_20":first_watch_count_20,
            "watch_first_entry_recall_20":first_watch_count_20/len(episodes20) if episodes20 else None,
            "watch_first_entry_recall_wilson_95_naive_20":wilson(first_watch_count_20,len(episodes20)),
            "watch_late_only_episodes_20":episode_watch_count_20-first_watch_count_20,
            "watch_episode_recall_wilson_95_naive_20":wilson(episode_watch_count_20,len(episodes20)),
            "episode_first_entry_feature_distributions_20":episode_features_20,
            "episode_first_entry_feature_coverage_20":first_coverage_20,
            "watch_episode_recall_20":(sum(e["watch_captured"] for e in episodes20)/len(episodes20)
                                      if episodes20 else None),
            "watch_recall_20":(coverage["watch_positive_20"]/coverage["movers_20"]
                               if coverage["movers_20"] else None),
            "watch_precision_20":(coverage["watch_positive_20"]/coverage["watch_matured"]
                                  if coverage["watch_matured"] else None),
            "watch_recall_wilson_95_naive_20":wilson(coverage["watch_positive_20"],coverage["movers_20"]),
            "watch_precision_wilson_95_naive_20":wilson(coverage["watch_positive_20"],coverage["watch_matured"]),
            "episodes":episodes,"mover_cases":cases,
            "watch_captured_episodes":episode_watch_count,
            "watch_first_entry_episodes_30":first_watch_count,
            "watch_first_entry_recall_30":first_watch_count/len(episodes) if episodes else None,
            "watch_first_entry_recall_wilson_95_naive_30":wilson(first_watch_count,len(episodes)),
            "watch_late_only_episodes_30":episode_watch_count-first_watch_count,
            "watch_episode_recall_30":episode_watch_count/len(episodes) if episodes else None,
            "watch_episode_recall_wilson_95_naive":wilson(episode_watch_count,len(episodes)),
            "episode_first_entry_feature_distributions":episode_features,
            "episode_first_entry_feature_coverage_30":first_coverage_30,
            "episode_first_lag_60m":{"n":len(episode_first_lags),
                "mean":sum(episode_first_lags)/len(episode_first_lags) if episode_first_lags else None},
            "watch_recall_30":coverage["watch_positive"]/coverage["movers"] if coverage["movers"] else None,
            "watch_precision_30":coverage["watch_positive"]/coverage["watch_matured"] if coverage["watch_matured"] else None,
            "watch_recall_wilson_95_naive":wilson(coverage["watch_positive"],coverage["movers"]),
            "watch_precision_wilson_95_naive":wilson(coverage["watch_positive"],coverage["watch_matured"]),
            "chronological_readiness":chronological_readiness(positives+negatives,runs,hours),
            "chronological_readiness_20":chronological_readiness(positives+negatives,runs,hours,
                                                                 positive_key="hit_20"),
            "lag_60m_positive":summarize_feature(positives,"60m"),
            "lag_60m_negative":summarize_feature(negatives,"60m"),
            "pre_entry_price_feature_distributions":{
                key:{"positive_20":summarize_feature(cases20,key),
                     "negative_20":summarize_feature(negatives20,key),
                     "positive_30":summarize_feature(positives,key),
                     "negative_30":summarize_feature(negatives,key)}
                for key in ("30m","60m","180m")}}
    return {"status":"DESCRIPTIVE_ONLY_NO_HELD_OUT_LIFT",
            "limitations":["Sampled PAPER ticker prices, not intrabar highs or complete Kraken history",
                           "Repeated pair/time entries and overlapping horizons are dependent",
                           "WATCH nonhit windows are descriptive, not independent negative trials",
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
