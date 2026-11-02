"""Read-only, SHA-bound, point-in-time cross-sectional crypto discovery.
No live scoring, trading, ledger writer or production promotion.
"""
import argparse
import json
from pathlib import Path
import numpy as np
import pandas as pd
from role_a_utc_gate_experiment import ARTIFACT_ID, RESEARCH_SHA, RUN_ID, TRAIN_SHA, load, metrics, select

def attach_peer_context(df):
    """Same-UTC leave-one-out peer features; never future observations."""
    d = df.copy()
    n = d.groupby("at", sort=False)["pair"].transform("size")
    d["peer_count"] = n - 1
    for field, name in (("pre_return_60m_pct", "peer_60m"), ("pre_return_15m_pct", "peer_15m")):
        x = d[field].clip(-30, 30)
        total = x.groupby(d["at"], sort=False).transform("sum")
        d[name] = (total - x) / (n - 1).replace(0, np.nan)
    positive = (d.pre_return_15m_pct > 0).astype(float)
    total_positive = positive.groupby(d["at"], sort=False).transform("sum")
    d["peer_breadth15"] = (total_positive - positive) / (n - 1).replace(0, np.nan)
    d["peer_eligible"] = d.peer_count >= 5
    for f in ("peer_60m", "peer_15m", "peer_breadth15"):
        d.loc[~d.peer_eligible, f] = np.nan
    return d

def hypothesis_scores(df):
    """All features are observable at entry, never use forward outcomes."""
    r60 = df.pre_return_60m_pct.clip(-100, 100)
    r15 = df.pre_return_15m_pct.clip(-100, 100)
    r5 = df.pre_return_5m_pct.clip(-100, 100)
    trades = df.trade_accel.clip(0, 100)
    vol = df.volume_accel.clip(0, 100)
    peer60, peer15, breadth = df.peer_60m, df.peer_15m, df.peer_breadth15
    baseline = r60.abs()
    eligible = df.peer_eligible & peer60.notna() & peer15.notna() & breadth.notna()
    def prioritize(mask, signal):
        return np.where(eligible & mask, 10000 + np.asarray(signal), baseline)
    acceleration = (3 * r5 - r15).clip(-100, 100)
    relative = (r60 - peer60).clip(-100, 100)
    quiet = r60.abs() <= 3
    up = (peer60 > .5) & (peer15 > 0) & (breadth >= .6)
    return {
        "baseline_abs60": baseline,
        "peer_relative_strength": prioritize(relative > 0, relative + .1 * np.log1p(trades)),
        "peer_breadth_acceleration": prioritize(up & (acceleration > 0), acceleration + np.log1p(trades)),
        "quiet_activity_market_up": prioritize(quiet & up & (trades >= 1.5) & (vol >= 1.2) & (r5 > 0), np.log1p(trades) + np.log1p(vol) + r5.clip(0, 10)),
        "laggard_catchup": prioritize((peer60 >= 1) & (r60 < peer60) & quiet & (trades >= 1.5) & (r5 > 0), (peer60 - r60).clip(0, 30) + np.log1p(trades)),
        "peer_divergence": prioritize(relative.abs() >= 2, relative.abs() + np.log1p(trades)),
        "market_down_relative_strength": prioritize((peer60 < -.5) & (relative > 1) & (r5 > 0), relative + r5.clip(0, 10)),
        "alphabetic_negative_control": df.pair.map(lambda p: -sum(map(ord, p))),
    }

def pairdays(p):
    return set(zip(p.loc[p.hit30, "pair"], p.loc[p.hit30, "date"]))

def evaluate(df):
    df = attach_peer_context(df)
    df = df[df.peer_eligible].copy()
    if df.empty:
        raise ValueError("no timestamp with at least five peers")
    scores = hypothesis_scores(df)
    report = {
        "schema": 1, "mode": "READ_ONLY_OFFLINE_HISTORICAL_CROSS_SECTIONAL",
        "source_run": RUN_ID, "source_artifact": ARTIFACT_ID,
        "source_research_sha256": RESEARCH_SHA, "source_training_sha256": TRAIN_SHA,
        "label": "max_forward_24h_5m_close_return_ge_30pct",
        "population_rows": len(df), "population_pairs": df.pair.nunique(),
        "min_independent_peer_count": 5,
        "split_policy": "train before 2026-02-28; validation Mar01-Apr29; test May01-Jun29; 24h embargo",
        "limitations": ["15m sampled Kraken USD anchors, not full live universe", "source ends June 2026, not November", "no historical spreads, executable fills, or funding/news", "24h overlapping outcomes; unique pair-days and cooldown govern claims", "hypotheses fixed before validation/test; no production promotion"],
        "top12": {}, "top3_diagnostic": {}, "test_incremental_pairdays": {},
    }
    for k, dest in ((12, "top12"), (3, "top3_diagnostic")):
        picks = {name: select(df, score, k) for name, score in scores.items()}
        report[dest] = {name: metrics(df, p, k) for name, p in picks.items()}
        if k == 12:
            base = pairdays(picks["baseline_abs60"][picks["baseline_abs60"].split == "test"])
            for name, p in picks.items():
                actual = pairdays(p[p.split == "test"])
                report["test_incremental_pairdays"][name] = {
                    "unique_vs_baseline": len(actual - base), "lost_vs_baseline": len(base - actual),
                    "total_distinct_positive_pairdays": len(actual)}
    candidates = [n for n in scores if n != "alphabetic_negative_control"]
    for k, dest in (("top12", "validation_selected_top12"), ("top3_diagnostic", "validation_selected_top3")):
        report[dest] = sorted(candidates, key=lambda n: (
            -report[k][n]["validation"]["positive_pairdays"],
            -report[k][n]["validation"]["cooldown24h_hits30"],
            -report[k][n]["validation"]["hits30"], n))[0]
    return report

def compact(report):
    fields = ("picks", "hits20", "hits30", "false_positives30", "positive_pairdays", "cooldown24h_picks", "cooldown24h_hits30", "missed_observed_windows30")
    return {
        "schema": report["schema"], "source_research_sha256": report["source_research_sha256"],
        "population_rows": report["population_rows"], "population_pairs": report["population_pairs"],
        "validation_selected_top3": report["validation_selected_top3"],
        "validation_selected_top12": report["validation_selected_top12"],
        "test_top12": {n: {k: v["test"][k] for k in fields} for n, v in report["top12"].items()},
        "test_top3": {n: {k: v["test"][k] for k in fields} for n, v in report["top3_diagnostic"].items()},
        "test_incremental_pairdays": report["test_incremental_pairdays"],
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("source_zip")
    p.add_argument("--output")
    p.add_argument("--compact", action="store_true")
    a = p.parse_args()
    result = evaluate(load(a.source_zip))
    if a.compact:
        result = compact(result)
    payload = json.dumps(result, sort_keys=True, indent=None if a.compact else 2,
                         separators=(",", ":") if a.compact else None) + "\n"
    if a.output:
        Path(a.output).write_text(payload)
    else:
        print(payload, end="")

if __name__ == "__main__":
    main()
