"""Reproducible audit of archived Kraken historical-rule aggregate evidence.

Exploratory analysis only: 24h forward maximum >=20% from 5m closes, not fills,
not +30% targets, not a live model or a proof of independent predictive lift.
"""
import argparse
import json
import math
from pathlib import Path


def _group(rows, hits):
    if type(rows) is not int or type(hits) is not int or rows < 0 or hits < 0 or hits > rows:
        raise ValueError("invalid historical aggregate")
    return {"rows": rows, "hits": hits, "hit_rate": round(hits / rows, 6) if rows else None}


def _subtract(a, b):
    return _group(a["rows"] - b["rows"], a["hits"] - b["hits"])


def _lift(a, b):
    return round(a["hit_rate"] / b["hit_rate"], 4) if a["hit_rate"] is not None and b["hit_rate"] else None


def _wilson(g):
    n, x = g["rows"], g["hits"]
    if not n:
        return None
    z = 1.959963984540054
    p = x / n
    d = 1 + z * z / n
    mid = (p + z * z / (2 * n)) / d
    half = z * math.sqrt((p * (1 - p) + z * z / (4 * n)) / n) / d
    return [round(mid - half, 6), round(mid + half, 6)]


def _fisher_greater(a, b):
    """One-sided exact hypergeometric tail: a has greater hit rate than b."""
    n = a["rows"]
    m = b["rows"]
    good = a["hits"] + b["hits"]
    total = n + m
    bad = total - good
    if not total:
        return None
    def logchoose(nn, kk):
        if kk < 0 or kk > nn:
            return float("-inf")
        return math.lgamma(nn + 1) - math.lgamma(kk + 1) - math.lgamma(nn - kk + 1)
    norm = logchoose(total, n)
    logs = [logchoose(good, k) + logchoose(bad, n - k) - norm
            for k in range(a["hits"], min(n, good) + 1)]
    top = max(logs)
    return sum(math.exp(x - top) for x in logs) * math.exp(top)


def _source(model, split, key):
    if key == "baseline":
        d = model["baseline_train" if split == "train" else "baseline_holdout"]
    else:
        d = model["rules"][key][split]
    return _group(d["rows"], d["major_movers"])


def analyze(model):
    if model.get("schema_version") != 1 or model.get("holdout_start") != "2026-05-01":
        raise ValueError("unexpected model version or holdout boundary")
    results = {}
    for split in ("train", "holdout"):
        base = _source(model, split, "baseline")
        early = _source(model, split, "early_1h")
        trades = _source(model, split, "trades_2x")
        early_trades = _source(model, split, "early_trades")
        volume = _source(model, split, "volume_2x")
        volume_trades = _source(model, split, "volume_trades")
        non_early = _subtract(base, early)
        early_no_trades = _subtract(early, early_trades)
        non_early_trades = _subtract(trades, early_trades)
        non_early_no_trades = _subtract(non_early, non_early_trades)
        trade_only = _subtract(trades, volume_trades)
        volume_only = _subtract(volume, volume_trades)
        neither = _subtract(_subtract(base, trades), volume_only)
        assert sum(x["rows"] for x in (early_trades, early_no_trades, non_early_trades, non_early_no_trades)) == base["rows"]
        assert sum(x["hits"] for x in (early_trades, early_no_trades, non_early_trades, non_early_no_trades)) == base["hits"]
        assert sum(x["rows"] for x in (volume_trades, trade_only, volume_only, neither)) == base["rows"]
        assert sum(x["hits"] for x in (volume_trades, trade_only, volume_only, neither)) == base["hits"]
        groups = {"baseline": base, "quiet_or_early_abs60_le3": early,
                  "abs60_gt3": non_early, "trades_2x": trades,
                  "early_and_trades_2x": early_trades,
                  "early_and_no_trades_2x": early_no_trades,
                  "abs60_gt3_and_trades_2x": non_early_trades,
                  "abs60_gt3_and_no_trades_2x": non_early_no_trades,
                  "volume_and_trades_2x": volume_trades,
                  "trades_only_2x": trade_only,
                  "volume_only_2x": volume_only, "neither_2x": neither}
        results[split] = {
            "groups": {k: {**v, "wilson_95": _wilson(v)} for k, v in groups.items()},
            "raw_trade2_vs_baseline_lift": _lift(trades, base),
            "trade2_within_early_lift": _lift(early_trades, early_no_trades),
            "trade2_within_abs60_gt3_lift": _lift(non_early_trades, non_early_no_trades),
            "abs60_gt3_vs_early_lift": _lift(non_early, early),
            "abs60_gt3_vs_early_fisher_one_sided_p": _fisher_greater(non_early, early),
        }
    return {
        "schema_version": 1,
        "source": "historical/evidence/kraken_20261010_historical_model.json",
        "source_original_branch": "rebuild-history",
        "source_original_blob_sha": "7a082fdf394e06b5de6ceee50e09ade8c97b2b97",
        "outcome": "max_forward_24h_return_from_5m_closes_ge_20pct",
        "results": results,
        "interpretation": [
            "The historical early_1h rule is abs(pre_return_60m_pct)<=3, NOT the live UTC-open >=0.25% gate.",
            "Overall trade-count 2x lift is not independent evidence of early entry: check both pre-return strata.",
            "A strong abs(60m return)>3% effect can reflect already-extended momentum or rebounds; direction is unavailable in aggregates.",
            "These aggregate rules cannot quantify live top-12 ranking, +30% recall, spread/liquidity, or executable returns.",
            "Do not promote a live rule from this exploratory historical audit; request directional, time-aligned raw-anchor evaluation."
        ]
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model", nargs="?", default=str(Path(__file__).parent / "evidence/kraken_20261010_historical_model.json"))
    parser.add_argument("--output")
    args = parser.parse_args()
    report = analyze(json.loads(Path(args.model).read_text()))
    result = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(result)
    else:
        print(result, end="")


if __name__ == "__main__":
    main()
