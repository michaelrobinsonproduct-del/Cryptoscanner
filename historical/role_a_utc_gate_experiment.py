"""Offline Kraken historical UTC-midnight gate and early-mover ranking proxies.

No live ticker UTC open, spreads, notional, fills, or live scorer replay.
Strict source SHA256 and population provenance; research-only, no writer.
"""
import argparse
import hashlib
import json
import math
import zipfile
from pathlib import Path
import numpy as np
import pandas as pd

RUN_ID = 38029912468
ARTIFACT_ID = 11662155953
RESEARCH_SHA = "0f42814dcf1cc63167f24dbc571534964fbaad564ef3e5ae7ed321a19bda905d"
TRAIN_SHA = "766683bae34744d825f0ee68335fd2e474ccc77d77849e46b2e4a8ecaf81778c"
FIELDS = ("pre_return_5m_pct", "pre_return_15m_pct", "pre_return_60m_pct",
          "volume_accel", "trade_accel", "volatility_pct", "max_forward_return_pct")


def attach_midnight_proxy(df):
    """Use observed SAME-DAY 00:00 UTC sampled close, never future interpolation."""
    df = df.copy()
    df["date"] = df["at"].str.slice(0, 10)
    df["hour"] = df["at"].str.slice(11, 16)
    midnight = df.loc[df.hour == "00:00", ["pair", "date", "price"]].rename(
        columns={"price": "sampled_midnight_close"})
    if midnight.duplicated(["pair", "date"]).any():
        raise ValueError("duplicate midnight proxy")
    df = df.merge(midnight, on=["pair", "date"], how="left", validate="many_to_one")
    df["utc_close_proxy_pct"] = 100 * (df.price / df.sampled_midnight_close - 1)
    df["gate_status"] = np.select([
        df.sampled_midnight_close.isna(),
        df.utc_close_proxy_pct < .25,
        df.utc_close_proxy_pct > 12,
    ], ["NO_UTC_MIDNIGHT_CLOSE", "BELOW_0_25", "ABOVE_12"],
        default="PASS_PRICE_PROXY")
    return df


def load(path):
    with zipfile.ZipFile(path) as z:
        required = {"research.ndjson", "research_training.ndjson",
                    "research_training_manifest.json", "moves.ndjson", "summary.json"}
        if set(z.namelist()) != required:
            raise ValueError("unexpected strict archive inventory")
        for name, expected in (("research.ndjson", RESEARCH_SHA),
                               ("research_training.ndjson", TRAIN_SHA)):
            with z.open(name) as f:
                digest = hashlib.sha256()
                for block in iter(lambda: f.read(1048576), b""):
                    digest.update(block)
                if digest.hexdigest() != expected:
                    raise ValueError("source SHA mismatch " + name)
        m = json.loads(z.read("research_training_manifest.json"))
        if (m.get("training_sha256") != TRAIN_SHA or
            m.get("sampling_policy") != "outcome_independent_hourly_utc" or
            m.get("research_population_policy") != "all_eligible_15m_anchors"):
            raise ValueError("not strict unbiased research population")
        rows = []
        with z.open("research.ndjson") as f:
            for line in f:
                r = json.loads(line)
                if not r.get("pair", "").endswith("USD"):
                    continue
                if any(not isinstance(r.get(k), (float, int)) or
                       not math.isfinite(r[k]) for k in FIELDS):
                    continue
                if not isinstance(r.get("anchor_price"), (float, int)) or r["anchor_price"] <= 0:
                    continue
                if not r["anchor_at"].endswith("+00:00"):
                    raise ValueError("non-UTC anchor")
                rows.append({k: r[k] for k in FIELDS} | {
                    "pair": r["pair"], "at": r["anchor_at"], "price": r["anchor_price"]})
    df = pd.DataFrame(rows)
    if len(df) < 300000 or df.duplicated(["pair", "at"]).any():
        raise ValueError("duplicate or missing source population")
    df = attach_midnight_proxy(df)
    df["split"] = np.select([
        df.date < "2026-02-28",
        (df.date >= "2026-03-01") & (df.date < "2026-04-30"),
        df.date >= "2026-05-01"],
        ["train", "validation", "test"], default="24H_EMBARGO")
    df["hit20"] = df.max_forward_return_pct >= 20
    df["hit30"] = df.max_forward_return_pct >= 30
    return df


def scores(df):
    r60, r5 = df.pre_return_60m_pct, df.pre_return_5m_pct
    vol = df.volume_accel.clip(0, 100)
    trades = df.trade_accel.clip(0, 100)
    sigma = df.volatility_pct.clip(0, 100)
    quiet = r60.abs() <= 3
    baseline = r60.abs().clip(0, 100)
    def priority(condition, score):
        # Fill remaining budget from frozen baseline, not cherry-picked winners.
        return np.where(condition, 10000 + score, baseline)
    return {
        "momentum_abs60_proxy": r60.abs(),
        "momentum_positive60_proxy": r60,
        "trade_count_accel": trades,
        "trade_leads_volume_quiet": priority(quiet & (trades >= 1.5),
            np.log1p(trades) - np.log1p(vol)),
        "volume_leads_trades_quiet": priority(quiet & (vol >= 1.5),
            np.log1p(vol) - np.log1p(trades)),
        "quiet_high_activity": priority(quiet & (trades >= 2) & (vol >= 1.5),
            1 + np.log1p(trades) + np.log1p(vol)),
        "compression_breakout_proxy": priority((sigma <= .5) & (r5 > .2) &
            (trades >= 1.5), 1 + r5.clip(-10, 10) + np.log1p(trades)),
        "volatility_expansion": sigma,
        "volatility_with_early_direction": priority((r60 >= -3) & (r60 <= 6) &
            (r5 > 0), sigma + .2 * r5.clip(0, 10) + .2 * np.log1p(trades)),
        "alphabetic_negative_control": df.pair.map(lambda p: -sum(map(ord, p))),
    }


def select(df, score, k, gate=False):
    a = df[["pair", "at", "date", "split", "hit20", "hit30", "gate_status"]].copy()
    a["score"] = np.asarray(score)
    if gate:
        a = a[a.gate_status == "PASS_PRICE_PROXY"]
    a = a.sort_values(["at", "score", "pair"], ascending=[True, False, True])
    return a.groupby("at", sort=False).head(k)


def metrics(df, picks, k):
    result = {}
    for split in ("train", "validation", "test"):
        u = df[df.split == split]
        s = picks[picks.split == split]
        pos = u[u.hit30]
        picked = s[s.hit30]
        cd = s.sort_values(["pair", "at"])
        times = pd.to_datetime(cd["at"], utc=True).astype("int64").to_numpy()
        cooldown_count = 0
        cooldown_hits = 0
        last = {}
        for pair, stamp, hit in zip(cd.pair.to_numpy(), times, cd.hit30.to_numpy()):
            if pair in last and stamp - last[pair] < 86400000000000:
                continue
            last[pair] = stamp
            cooldown_count += 1
            cooldown_hits += int(hit)
        result[split] = {
            "universe_rows": len(u), "timestamps": u["at"].nunique(),
            "universe_hit20": int(u.hit20.sum()),
            "universe_hit30": int(u.hit30.sum()),
            "universe_positive_pairdays": int(pos.groupby(["pair", "date"]).ngroups),
            "budget_per_timestamp": k, "picks": len(s),
            "unfilled_budget": int(k * u["at"].nunique() - len(s)),
            "hits20": int(s.hit20.sum()), "hits30": int(s.hit30.sum()),
            "false_positives30": int(len(s) - s.hit30.sum()),
            "precision30": round(float(s.hit30.mean()), 6) if len(s) else None,
            "recall_observed_windows30": round(float(s.hit30.sum() / u.hit30.sum()), 6)
                if u.hit30.sum() else None,
            "missed_observed_windows30": int(u.hit30.sum() - s.hit30.sum()),
            "positive_pairdays": int(picked.groupby(["pair", "date"]).ngroups),
            "cooldown24h_picks": cooldown_count,
            "cooldown24h_hits30": cooldown_hits,
        }
    return result


def run(source):
    df = load(source)
    census = {}
    for split in ("train", "validation", "test"):
        d = df[df.split == split]
        census[split] = {str(g): {
            "anchors": len(v), "hit20": int(v.hit20.sum()),
            "hit30": int(v.hit30.sum()),
            "positive_pairdays30": int(v[v.hit30].groupby(["pair", "date"]).ngroups)}
            for g, v in d.groupby("gate_status")}
    s = scores(df)
    result = {
        "schema": 1, "mode": "READ_ONLY_OFFLINE_HISTORICAL_PROXY",
        "source_run": RUN_ID, "source_artifact": ARTIFACT_ID,
        "source_research_sha256": RESEARCH_SHA,
        "source_training_sha256": TRAIN_SHA,
        "population_usd_rows": len(df), "usd_pairs": df.pair.nunique(),
        "label": "max_forward_24h_5m_close_pct_ge_20_or_30",
        "split_policy": "train before 2026-02-28, validation Mar01-Apr29, test May01-Jun29; 24h embargo",
        "utc_open_gate": "price-only counterfactual using actual observed 00:00 UTC 5m close; NOT Kraken ticker UTC-open; spread/notional absent",
        "gate_census": census, "same_budget_top12": {}, "secondary_top3": {},
        "production_applied": False,
        "limitations": ["no true historical Kraken ticker UTC-open/spread/notional or OHLC preselection replay",
            "USD universe ~15 markets per 15m timestamp vs 604 live; top12 nearly saturates",
            "correlated 15m anchors and overlapping 24h forward labels; episode metrics essential",
            "source ends June 2026, not November; no executable fills or live lift",
            "thresholds fixed before validation/test; negative control is non-predictive"],
    }
    for name, score in s.items():
        result["same_budget_top12"][name] = metrics(df, select(df, score, 12), 12)
        result["secondary_top3"][name] = metrics(df, select(df, score, 3), 3)
    for name in ("momentum_abs60_proxy", "volatility_expansion",
                 "volatility_with_early_direction"):
        result["same_budget_top12"][name + "_with_utc_price_gate_proxy"] = metrics(
            df, select(df, s[name], 12, gate=True), 12)
    candidates = [n for n in s if n != "alphabetic_negative_control"]
    result["validation_selected_top3"] = sorted(candidates, key=lambda n: (
        -result["secondary_top3"][n]["validation"]["positive_pairdays"],
        -result["secondary_top3"][n]["validation"]["hits30"],
        -result["secondary_top3"][n]["validation"]["hits20"], n))[0]
    return result


def compact(result):
    fields12 = ("picks", "hits20", "hits30", "false_positives30",
                "positive_pairdays", "cooldown24h_hits30")
    fields3 = ("picks", "hits30", "positive_pairdays", "cooldown24h_hits30")
    return {
        "source_research_sha256": result["source_research_sha256"],
        "population_usd_rows": result["population_usd_rows"],
        "usd_pairs": result["usd_pairs"],
        "validation_selected_top3": result["validation_selected_top3"],
        "gate_census": result["gate_census"],
        "test_top12": {k: {f: v["test"][f] for f in fields12}
                       for k, v in result["same_budget_top12"].items()},
        "test_top3": {k: {f: v["test"][f] for f in fields3}
                      for k, v in result["secondary_top3"].items()},
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("source_zip")
    p.add_argument("--output")
    p.add_argument("--compact", action="store_true")
    args = p.parse_args()
    result = run(args.source_zip)
    if args.compact:
        result = compact(result)
    output = json.dumps(result, sort_keys=True, separators=(",", ":") if args.compact else None,
                        indent=None if args.compact else 2) + "\n"
    if args.output:
        Path(args.output).write_text(output)
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
