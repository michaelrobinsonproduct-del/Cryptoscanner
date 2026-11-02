"""Fail-closed, read-only integrity check for marketwide research artifacts.

This checks *artifact identity*, not exchange authentication or predictive lift.
The PAPER ledger is separately verified by segmented_repository full replay.
"""
import argparse
import hashlib
import json
from pathlib import Path
from research.marketwide_episode_diagnostics import wilson

FILES = ("marketwide-outcomes.json", "marketwide-episodes.json",
         "marketwide-provenance.json")
LEDGER = "verified-paper-ledger.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_strict_json(path):
    # Python's default json.loads accepts NaN/Infinity, which are not JSON
    # numbers and can silently contaminate descriptive research artifacts.
    def reject_nonfinite(value):
        raise ValueError("nonfinite research JSON value: " + value)
    return json.loads(path.read_text(), parse_constant=reject_nonfinite)


def verify_artifacts(directory, expected_head, expected_ledger_commit):
    base = Path(directory)
    if not isinstance(expected_head, str) or len(expected_head) != 40 or any(
            c not in "0123456789abcdef" for c in expected_head):
        raise ValueError("invalid expected exact source commit")
    if not isinstance(expected_ledger_commit, str) or len(expected_ledger_commit) != 40 or any(
            c not in "0123456789abcdef" for c in expected_ledger_commit):
        raise ValueError("invalid expected remote ledger commit")
    required = (*FILES, LEDGER, "marketwide-SHA256SUMS")
    for name in required:
        path = base / name
        if not path.is_file() or path.is_symlink():
            raise ValueError("missing or unsafe research evidence: " + name)
    lines = (base / "marketwide-SHA256SUMS").read_text().splitlines()
    expected = {}
    for line in lines:
        parts = line.split("  ", 1)
        if len(parts) != 2 or len(parts[0]) != 64 or any(
                c not in "0123456789abcdef" for c in parts[0]):
            raise ValueError("invalid SHA256SUMS entry")
        value, name = parts
        if name not in FILES or name in expected:
            raise ValueError("unexpected or repeated SHA256SUMS entry")
        expected[name] = value
    if set(expected) != set(FILES):
        raise ValueError("missing SHA256SUMS entry")
    for name in FILES:
        if digest(base / name) != expected[name]:
            raise ValueError("report checksum mismatch: " + name)
    ledger = load_strict_json((base / LEDGER))
    outcomes = load_strict_json((base / FILES[0]))
    episodes = load_strict_json((base / FILES[1]))
    provenance = load_strict_json((base / FILES[2]))
    if provenance.get("research_source_commit") != expected_head:
        raise ValueError("source head mismatch")
    if provenance.get("paper_ledger_branch_commit") != expected_ledger_commit:
        raise ValueError("remote ledger commit mismatch")
    for name, key in ((LEDGER, "verified_ledger_export_sha256"),
                      (FILES[0], "outcome_report_sha256"),
                      (FILES[1], "episode_report_sha256")):
        if provenance.get(key) != digest(base / name):
            raise ValueError("provenance checksum mismatch: " + name)
    if (episodes.get("source", {}).get("ledger_sha256") != ledger.get("sha256")
        or episodes.get("source", {}).get("generation") != ledger.get("generation")
        or episodes.get("source", {}).get("runs") != outcomes.get("observed_run_count")
        or episodes.get("source", {}).get("observations") != outcomes.get("observed_entry_count")
        or provenance.get("observed_run_count") != outcomes.get("observed_run_count")
        or provenance.get("observed_entry_count") != outcomes.get("observed_entry_count")):
        raise ValueError("cross-report ledger identity mismatch")
    # Check the two independent evaluator reports, not only their checksums.
    # An internally resealed artifact with inconsistent outcomes is invalid.
    horizons = ("1", "6", "24", "48")
    if (set(outcomes.get("horizons", {})) != set(horizons)
        or set(episodes.get("horizons", {})) != set(horizons)):
        raise ValueError("missing or unexpected evaluation horizon")
    matching = {
        "eligible": "eligible", "matured": "matured",
        "immature": "immature", "abstain_gap": "abstain_gap",
        "movers_20": "movers_20", "movers": "movers_30",
        "watch_eligible": "watch_eligible",
        "watch_immature": "watch_immature",
        "watch_abstain_gap": "watch_abstain_gap",
        "watch_matured": "watch_matured",
        "watch_positive_20": "watch_20",
        "watch_positive": "watch_30",
        "watch_false_positive_20": "watch_false_positive_20",
        "watch_false_positive_30": "watch_false_positive_30",
        "missed_20": "missed_20", "missed_30": "missed_30",
    }
    for horizon in horizons:
        window = outcomes["horizons"][horizon]
        episode = episodes["horizons"][horizon]
        coverage = episode["coverage"]
        # Reconciles all observed pairs, not hypothetical missing exchange markets.
        pair = episode.get("pair_coverage")
        pair_keys = ("eligible","matured","immature","abstain_gap","watch_eligible",
                     "watch_matured","watch_immature","watch_abstain_gap",
                     "movers_20","movers","watch_positive_20","watch_positive")
        reason_keys = ("conflicting_quotes","future_entry_quotes","no_future_observation",
                       "missing_horizon_anchor","stale_entry","discontinuous_path")
        def natural(value):
            return type(value) is int and value >= 0
        if (not isinstance(pair,dict) or
            pair.get("scope") != "observed PAPER pairs only; no inferred unobserved markets" or
            pair.get("top_gap_pairs_limit") != 10 or
            not natural(pair.get("observed_pairs")) or
            not natural(pair.get("pairs_with_gap")) or
            not isinstance(pair.get("totals"),dict) or
            set(pair["totals"]) != set(pair_keys) or
            any(not natural(pair["totals"][k]) or pair["totals"][k] != coverage[k] for k in pair_keys) or
            not isinstance(pair.get("gap_reason_totals"),dict) or
            set(pair["gap_reason_totals"]) != set(reason_keys) or
            any(not natural(pair["gap_reason_totals"][k]) or
                pair["gap_reason_totals"][k] != coverage["abstain_"+k] for k in reason_keys) or
            sum(pair["gap_reason_totals"].values()) != coverage["abstain_gap"] or
            not (0 <= pair["pairs_with_gap"] <= pair["observed_pairs"] <= coverage["eligible"]) or
            (coverage["eligible"] > 0 and pair["observed_pairs"] == 0) or
            not isinstance(pair.get("top_gap_pairs"),list) or
            len(pair["top_gap_pairs"]) > min(10,pair["pairs_with_gap"])):
            raise ValueError("invalid per-pair coverage conservation: " + horizon)
        top = pair["top_gap_pairs"]
        if (any(not isinstance(row,dict) or not isinstance(row.get("pair"),str) or not row["pair"] or
                any(not natural(row.get(k)) or row[k] > pair["totals"][k] for k in pair_keys) or
                not isinstance(row.get("gap_reasons"),dict) or
                set(row["gap_reasons"]) != set(reason_keys) or
                any(not natural(row["gap_reasons"][k]) or
                    row["gap_reasons"][k] > pair["gap_reason_totals"][k] for k in reason_keys) or
                row["abstain_gap"] == 0 or
                row["eligible"] != row["matured"]+row["immature"]+row["abstain_gap"] or
                row["watch_eligible"] != row["watch_matured"]+row["watch_immature"]+row["watch_abstain_gap"] or
                row["abstain_gap"] != sum(row["gap_reasons"].values()) for row in top) or
            len({row["pair"] for row in top}) != len(top) or
            top != sorted(top,key=lambda row:(-row["abstain_gap"],row["pair"]))):
            raise ValueError("invalid per-pair top-gap evidence: " + horizon)
        if any(coverage.get(k) != window.get(v) for k, v in matching.items()):
            raise ValueError("cross-report outcome mismatch: " + horizon)
        if (coverage["eligible"] != outcomes["observed_entry_count"]
            or coverage["eligible"] != (coverage["matured"] +
                coverage["immature"] + coverage["abstain_gap"])
            or coverage["watch_eligible"] != (coverage["watch_matured"] +
                coverage["watch_immature"] + coverage["watch_abstain_gap"])
            or coverage["movers_20"] != coverage["watch_positive_20"] + coverage["missed_20"]
            or coverage["movers"] != coverage["watch_positive"] + coverage["missed_30"]
            or episode["missed_mover_episodes_20"] != (episode["unique_mover_episodes_20"] -
                episode["watch_captured_episodes_20"])
            or episode["missed_mover_episodes_30"] != (episode["unique_mover_episodes"] -
                episode["watch_captured_episodes"])):
            raise ValueError("cross-report cohort partition mismatch: " + horizon)
        # The descriptive early-entry signal must not be inflated by a WATCH
        # arriving only after an episode's first qualifying observation.
        for suffix, captured in (("20", "watch_captured_episodes_20"),
                                 ("30", "watch_captured_episodes")):
            first = episode.get("watch_first_entry_episodes_" + suffix)
            late = episode.get("watch_late_only_episodes_" + suffix)
            total = episode.get(captured)
            if (not all(isinstance(x, int) and not isinstance(x, bool) and x >= 0
                        for x in (first, late, total)) or first + late != total):
                raise ValueError("invalid first-entry versus late WATCH episode partition: " + horizon)
            interval = episode.get("watch_first_entry_recall_wilson_95_naive_" + suffix)
            expected_interval = wilson(first, episode["unique_mover_episodes_20"
                if suffix == "20" else "unique_mover_episodes"])
            if interval != expected_interval:
                raise ValueError("invalid first-entry Wilson uncertainty: " + horizon)
        # First-entry recall and feature coverage are independently sealed
        # semantic contracts; checksums alone cannot detect fabricated ratios.
        for suffix, episodes_key, first_key, distributions_key in (
            ("20", "unique_mover_episodes_20", "watch_first_entry_episodes_20",
             "episode_first_entry_feature_distributions_20"),
            ("30", "unique_mover_episodes", "watch_first_entry_episodes_30",
             "episode_first_entry_feature_distributions")):
            total = episode[episodes_key]
            first = episode[first_key]
            recall = episode.get("watch_first_entry_recall_" + suffix)
            expected_recall = first / total if total else None
            if (not isinstance(total, int) or isinstance(total, bool) or total < 0
                or first > total or recall != expected_recall):
                raise ValueError("invalid first-entry WATCH recall: " + horizon)
            feature_coverage = episode.get("episode_first_entry_feature_coverage_" + suffix)
            distributions = episode.get(distributions_key)
            if (not isinstance(feature_coverage, dict) or not isinstance(distributions, dict)
                or set(feature_coverage) != {"30m", "60m", "180m"}
                or set(distributions) != set(feature_coverage)):
                raise ValueError("invalid first-entry feature coverage schema: " + horizon)
            for lag, stats in feature_coverage.items():
                distribution = distributions[lag]
                n = stats.get("with_asof_feature")
                missing = stats.get("without_asof_feature")
                pairs = stats.get("distinct_covered_pairs")
                reasons = stats.get("missing_reasons")
                allowed = {"no_prior_anchor", "stale_prior_anchor", "conflicting_anchor",
                           "conflicting_history", "discontinuous_history", "nonfinite_return"}
                if (not all(isinstance(x, int) and not isinstance(x, bool) and x >= 0
                            for x in (n, missing, pairs))
                    or stats.get("episodes") != total or n + missing != total
                    or pairs > n or n != distribution.get("n")
                    or pairs != distribution.get("distinct_pairs")
                    or stats.get("covered_fraction") != (n / total if total else None)
                    or not isinstance(reasons, dict) or not set(reasons) <= allowed
                    or any(not isinstance(v, int) or isinstance(v, bool) or v <= 0
                           for v in reasons.values())
                    or sum(reasons.values()) != missing):
                    raise ValueError("invalid first-entry feature coverage: " + horizon)
        # PAPER sample adequacy is not model-readiness or authenticated lift.
        # Rechecking partition denominators prevents resealed research JSON
        # from inventing eligible cohorts or retroactive first-entry features.
        for key, total_key in (("chronological_readiness", "unique_mover_episodes"),
                               ("chronological_readiness_20", "unique_mover_episodes_20")):
            readiness = episode.get(key)
            gates = ["exchange_authenticated_market_history",
                     "point_in_time_execution_features",
                     "independent_held_out_challenger"]
            if (not isinstance(readiness, dict)
                or readiness.get("model_evaluation_ready") is not False
                or readiness.get("unmet_evidence_gates") != gates
                or type(readiness.get("sample_thresholds_met")) is not bool):
                raise ValueError("invalid PAPER-only model-readiness gate: " + horizon)
            if readiness.get("status") == "INSUFFICIENT_SCAN_TIMES":
                if readiness["sample_thresholds_met"] or readiness.get("cutoff") is not None:
                    raise ValueError("invalid insufficient-scan readiness: " + horizon)
                continue
            if readiness.get("status") != "DESCRIPTIVE_SPLIT_ONLY_NO_TRAINED_CHALLENGER":
                raise ValueError("invalid chronological readiness status: " + horizon)
            expected_blockers = []
            partition_episodes = 0
            for partition in ("train", "test"):
                cohort = readiness.get(partition)
                if not isinstance(cohort, dict):
                    raise ValueError("invalid chronological cohort: " + horizon)
                episodes_n = cohort.get("positive_episodes")
                featured_n = cohort.get("positive_lag_60m_episodes")
                negatives_n = cohort.get("negative_lag_60m_pairs")
                if (not all(type(v) is int and v >= 0
                            for v in (episodes_n, featured_n, negatives_n))
                    or featured_n > episodes_n):
                    raise ValueError("invalid chronological cohort: " + horizon)
                partition_episodes += episodes_n
                first_features = cohort.get("positive_first_entry_feature_coverage")
                if not isinstance(first_features, dict) or set(first_features) != {"30m","60m","180m"}:
                    raise ValueError("invalid chronological first-entry feature schema: " + horizon)
                for lag, stats in first_features.items():
                    if not isinstance(stats, dict):
                        raise ValueError("invalid chronological first-entry coverage: " + horizon)
                    with_feature = stats.get("with_asof_feature")
                    without_feature = stats.get("without_asof_feature")
                    reasons = stats.get("missing_reasons")
                    allowed = {"no_prior_anchor","stale_prior_anchor","conflicting_anchor",
                               "conflicting_history","discontinuous_history",
                               "nonfinite_return","reason_unavailable"}
                    if (not all(type(v) is int and v >= 0 for v in (with_feature, without_feature))
                        or stats.get("episodes") != episodes_n
                        or with_feature + without_feature != episodes_n
                        or not isinstance(reasons, dict) or not set(reasons) <= allowed
                        or any(type(v) is not int or v <= 0 for v in reasons.values())
                        or sum(reasons.values()) != without_feature
                        or (lag == "60m" and with_feature != featured_n)):
                        raise ValueError("invalid chronological first-entry coverage: " + horizon)
                for requirement, observed in (("episode_first_positive_lag_60m",featured_n),
                                              ("distinct_negative_lag_60m_pairs",negatives_n)):
                    if observed < 10:
                        expected_blockers.append({"partition":partition,"requirement":requirement,
                                                  "required":10,"observed":observed})
            if (partition_episodes > episode[total_key]
                or readiness.get("minimum_sample_requirements") != expected_blockers
                or readiness["sample_thresholds_met"] != (not expected_blockers)):
                raise ValueError("invalid chronological sample requirements: " + horizon)
        # The count of dependent WATCH nonhit windows cannot exceed the
        # independently validated matured negative WATCH denominator.
        for suffix in ("20", "30"):
            windows = episode.get("watch_nonhit_windows_" + suffix)
            pairs = episode.get("watch_nonhit_distinct_pairs_" + suffix)
            nonhits = coverage["watch_false_positive_" + suffix]
            if (not all(isinstance(v, int) and not isinstance(v, bool) and v >= 0
                        for v in (windows, pairs))
                or windows > nonhits or pairs > windows
                or (windows == 0) != (nonhits == 0)
                or (pairs == 0) != (windows == 0)):
                raise ValueError("invalid WATCH nonhit window partition: " + horizon)
        # A self-resealed aggregate cannot contradict its actual +30% episode
        # records. The +20% evaluator does not currently export episode rows.
        actual_episodes = episode.get("episodes")
        if (not isinstance(actual_episodes, list)
            or len(actual_episodes) != episode["unique_mover_episodes"]
            or episode["unique_mover_episodes"] > coverage["movers"]
            or any(not isinstance(row, dict) for row in actual_episodes)):
            raise ValueError("invalid episode-row inventory: " + horizon)
        if (sum(row.get("watch_captured") is True for row in actual_episodes)
                != episode["watch_captured_episodes"]
            or sum(row.get("first_entry_watch") is True for row in actual_episodes)
                != episode["watch_first_entry_episodes_30"]
            or any(row.get("first_entry_watch") is True and
                   (row.get("watch_captured") is not True or
                    row.get("first_watch_decision_at") != row.get("first_decision_at"))
                   for row in actual_episodes)
            or any(row.get("watch_captured") is False and
                   row.get("first_watch_decision_at") is not None
                   for row in actual_episodes)):
            raise ValueError("inconsistent episode-row WATCH capture: " + horizon)
        # Mutually exclusive gap reasons must reconcile with BOTH market and
        # WATCH unknown outcomes. A resealed report cannot fabricate reasons.
        reasons = ("abstain_conflicting_quotes", "abstain_future_entry_quotes",
                   "abstain_no_future_observation", "abstain_missing_horizon_anchor",
                   "abstain_stale_entry", "abstain_discontinuous_path")
        if (any(not isinstance(coverage.get(k), int) or isinstance(coverage.get(k), bool)
                or coverage[k] < 0 or
                not isinstance(coverage.get("watch_" + k), int) or
                isinstance(coverage.get("watch_" + k), bool) or
                coverage["watch_" + k] < 0 or coverage["watch_" + k] > coverage[k]
                for k in reasons)
            or sum(coverage[k] for k in reasons) != coverage["abstain_gap"]
            or sum(coverage["watch_" + k] for k in reasons) != coverage["watch_abstain_gap"]):
            raise ValueError("invalid mutually exclusive gap-reason partition: " + horizon)
    for source in (outcomes, episodes.get("source", {}), provenance):
        if (source.get("source_authenticated") is not False
            or source.get("complete_market_history") is not False
            or source.get("eligible_for_model_promotion") is not False):
            raise ValueError("unverified research evidence claims authentication/promotion")
    return {"research_source_commit": expected_head,
            "ledger_sha256": ledger["sha256"],
            "generation": ledger["generation"],
            "reports_checked": len(FILES)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--directory", required=True)
    p.add_argument("--expected-head", required=True)
    p.add_argument("--expected-ledger-commit", required=True)
    args = p.parse_args()
    print(json.dumps(verify_artifacts(args.directory, args.expected_head,
                                      args.expected_ledger_commit),
                     sort_keys=True))


if __name__ == "__main__":
    main()
