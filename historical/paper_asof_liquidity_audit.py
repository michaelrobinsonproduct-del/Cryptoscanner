"""Research-only six-hour as-of liquidity replay; never modifies scanner/ledger.

Input directory must contain the sealed gen45 ZIP named paper-ledger-latest.zip
and 10 original per-run ledger ZIPs named paper-ledger-<GitHub run ID>.zip.
Every internal SHA256SUMS, report SHA and as-of observation is verified.
This is exploratory retrospective research, NOT a held-out model or trading result.
"""
import argparse
import collections
import datetime as dt
import hashlib
import json
import math
import statistics
import zipfile
from pathlib import Path

RUN_IDS = {20: 41307201989, 21: 41309654993, 22: 41311926367,
           23: 41314165370, 24: 41316423836, 25: 41319133932,
           26: 41322013186, 27: 41324272237, 28: 41326715230,
           29: 41329629549}
GEN45_SHA = "70f60d2be8faa7b967536b5a474b371674facb77418f6f5c2c544f40ceabeeab"


def verified_zip(path):
    with zipfile.ZipFile(path) as z:
        for row in z.read("SHA256SUMS").decode().splitlines():
            expected, name = row.split()
            if hashlib.sha256(z.read(name)).hexdigest() != expected:
                raise ValueError("artifact SHA mismatch: " + str(path) + " " + name)
        return {name: z.read(name) for name in z.namelist() if name.endswith(".json")}


def lag(times, prices, i, pair, minutes, tolerance):
    prior = [(abs((times[i] - times[j]).total_seconds() / 60 - minutes),
              prices[j][pair]) for j in range(i) if pair in prices[j]
             and abs((times[i] - times[j]).total_seconds() / 60 - minutes) <= tolerance]
    return min(prior)[1] if prior else None



def evaluate_rankings(scores, eval_times, watch, labels, top_k=12):
    """Freeze selections from as-of features BEFORE consulting future outcomes.

    A selected candidate with an unavailable forward path stays selected and
    counts as an abstention. Never condition the candidate universe on labels.
    """
    names = ["momentum_1h", "volatility_3h", "volatility_direction",
             "liquidity_adjusted_volatility", "actual_paper_watch"]
    outcomes = {}
    for name in names:
        selected = []
        selected_by_time = {}
        for i in eval_times:
            pool = [p for j, p in scores if j == i]
            chosen = (sorted(watch.get(i, set()) & set(pool))
                      if name == "actual_paper_watch"
                      else sorted(pool, key=lambda p: (-scores[i, p][name], p))[:top_k])
            selected_by_time[str(i)] = chosen
            selected.extend((i, p, labels.get((i, p))) for p in chosen)
        labeled = [(i, p, v) for i, p, v in selected if v is not None]
        hits30 = sum(v >= 30 for _, _, v in labeled)
        outcomes[name] = {
            "picks": len(selected),
            "labeled_picks": len(labeled),
            "missing_forward_label_picks": len(selected) - len(labeled),
            "positive_windows": {str(th): sum(v >= th for _, _, v in labeled)
                                 for th in (5, 10, 20, 30)},
            "sampled_precision_on_labeled_30": round(hits30 / len(labeled), 6)
                                               if labeled else None,
            "distinct_positive_markets_30": sorted(
                {p for _, p, v in labeled if v >= 30}),
            "selected_pairs_by_time": selected_by_time,
            "missing_label_examples": [
                {"index": i, "pair": p} for i, p, v in selected if v is None
            ][:12],
        }
    return outcomes


def analyze(directory):
    source = verified_zip(directory / "paper-ledger-latest.zip")
    ledger = json.loads(source["ledger.json"])
    if ledger["generation"] != 45 or ledger["sha256"] != GEN45_SHA:
        raise ValueError("unexpected immutable ledger version")
    runs = sorted(ledger["runs"], key=lambda r: r["as_of"])
    times = [dt.datetime.fromisoformat(r["as_of"]) for r in runs]
    index = {r["id"]: i for i, r in enumerate(runs)}
    prices = [{} for _ in runs]
    for obs in ledger["observations"]:
        prices[index[obs["run_id"]]][obs["pair"]] = obs["price"]
    watch = collections.defaultdict(set)
    for pred in ledger["predictions"]:
        watch[index[pred["run_id"]]].add(pred["pair"])

    snapshots, source_runs = {}, []
    for i, action_id in RUN_IDS.items():
        data = verified_zip(directory / ("paper-ledger-" + str(action_id) + ".zip"))
        latest = json.loads(data["latest.json"])
        if latest["as_of"] != runs[i]["as_of"]:
            raise ValueError("as-of mismatch for " + str(action_id))
        if hashlib.sha256(data["latest.json"]).hexdigest() != runs[i]["report_sha256"]:
            raise ValueError("ledger-to-report hash mismatch")
        quotes = {q["pair"]: q for q in latest["observations"]}
        if set(quotes) != set(prices[i]) or any(
            quotes[p]["price"] != prices[i][p] for p in quotes
        ):
            raise ValueError("price/pair mismatch")
        snapshots[i] = quotes
        source_runs.append({"run_id": action_id, "as_of": latest["as_of"],
                            "report_sha256": runs[i]["report_sha256"]})

    labels = {}
    for i in RUN_IDS:
        target = times[i] + dt.timedelta(hours=6)
        if times[-1] < target + dt.timedelta(minutes=45):
            continue
        inside = [j for j in range(i + 1, len(times)) if times[j] <= target]
        anchor = [j for j in range(i + 1, len(times))
                  if target <= times[j] <= target + dt.timedelta(minutes=45)]
        if not inside or not anchor:
            continue
        if max((times[j + 1] - times[j]).total_seconds() / 60
               for j in range(i, anchor[0])) > 45:
            continue
        for pair, entry in prices[i].items():
            if any(pair not in prices[j] for j in inside + [anchor[0]]):
                continue
            labels[i, pair] = 100 * (max(prices[j][pair] for j in inside) / entry - 1)

    scores = {}
    for i in RUN_IDS:
        for pair, quote in snapshots[i].items():
            if quote["spread_bps"] > 45 or quote["notional_24h_usd"] < 100000:
                continue
            p1 = lag(times, prices, i, pair, 60, 30)
            p2 = lag(times, prices, i, pair, 120, 35)
            if p1 is None or p2 is None:
                continue
            past = [(times[j], prices[j][pair]) for j in range(i)
                    if pair in prices[j] and (times[i] - times[j]).total_seconds() <= 14400]
            moves = [100 * (b[1] / a[1] - 1) for a, b in zip(past, past[1:])
                     if 0 < (b[0] - a[0]).total_seconds() / 60 <= 75]
            if len(moves) < 2:
                continue
            r1 = 100 * (quote["price"] / p1 - 1)
            vol = statistics.pstdev(moves)
            direction = vol * (1 if r1 > 0 else -0.5) + 0.2 * r1
            scores[i, pair] = {
                "momentum_1h": r1, "volatility_3h": vol,
                "volatility_direction": direction,
                "liquidity_adjusted_volatility": direction
                  + 0.8 * math.log10(quote["notional_24h_usd"] / 100000)
                  - 0.02 * quote["spread_bps"],
            }

    # Time eligibility depends only on as-of features and elapsed maturity,
    # never on whether any selected market happens to have a future label.
    eval_times = [i for i in RUN_IDS
                  if times[-1] >= times[i] + dt.timedelta(hours=6, minutes=45)
                  and sum(j == i for j, _ in scores) >= 12]
    outcomes = evaluate_rankings(scores, eval_times, watch, labels)

    positives = [{"index": i, "pair": pair, "peak_pct": round(value, 3),
                  "notional_usd": snapshots[i][pair]["notional_24h_usd"],
                  "spread_bps": snapshots[i][pair]["spread_bps"]}
                 for (i, pair), value in labels.items()
                 if i in eval_times and value >= 30]
    return {"source_generation": 45, "source_sha256": GEN45_SHA,
            "source_runs": source_runs, "evaluated_times": len(eval_times),
            "pool_sizes": {str(i): sum(j == i for j, _ in scores) for i in eval_times},
            "strategies": outcomes, "all_30pct_windows": positives,
            "research_only": True, "held_out_lift": None}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    print(json.dumps(analyze(args.directory), sort_keys=True, indent=2))
