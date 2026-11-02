"""Read-only market-wide point-in-time evaluation of PAPER observations.

Input is an exported, independently verified ledger JSON. This tool never
writes a ledger, contacts an exchange, or claims a complete historical cohort.
Missing price coverage is an abstention, never a negative label.
"""
import argparse
import datetime as dt
import json
import math
from collections import defaultdict

HORIZONS = (1, 6, 24, 48)
MAX_GAP = dt.timedelta(minutes=45)

def timestamp(s):
    t = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    if t.tzinfo is None:
        raise ValueError("timezone required")
    return t.astimezone(dt.timezone.utc)

def evaluate(state):
    from paper_pov.ledger import verify
    verify(state, 32_000_000)
    runs = {r["id"]: r for r in state["runs"]}
    prices = defaultdict(list)
    for o in state["observations"]:
        prices[o["pair"]].append((timestamp(o["at"]), float(o["price"]), o["run_id"]))
    for series in prices.values():
        series.sort()
    watches = {(p["run_id"], p["pair"]) for p in state["predictions"]}
    results = {str(h): {"eligible": 0, "matured": 0, "abstain_gap": 0,
                         "immature": 0, "movers_20": 0, "movers_30": 0,
                         "watch_20": 0, "watch_30": 0, "missed_20": 0,
                         "missed_30": 0, "watch_false_positive_20": 0,
                         "watch_false_positive_30": 0} for h in HORIZONS}
    latest = max((timestamp(r["as_of"]) for r in runs.values()), default=None)
    for pair, series in prices.items():
        for i, (at, entry, rid) in enumerate(series):
            # One point per actual market/run observation, not just WATCH.
            start = timestamp(runs[rid]["as_of"])
            selected = (rid, pair) in watches
            for h in HORIZONS:
                row = results[str(h)]
                row["eligible"] += 1
                target = start + dt.timedelta(hours=h)
                if latest is None or latest < target + MAX_GAP:
                    row["immature"] += 1
                    continue
                future = [(t, p) for t, p, _ in series[i+1:]
                          if at < t <= target + MAX_GAP]
                before = [(t, p) for t, p in future if t <= target]
                anchors = [(t, p) for t, p in future if target <= t <= target + MAX_GAP]
                timeline = [at] + [t for t, _ in before]
                if (not before or not anchors or start - at > MAX_GAP
                    or any(b-a > MAX_GAP for a,b in zip(timeline,timeline[1:]))
                    or anchors[0][0]-timeline[-1] > MAX_GAP):
                    row["abstain_gap"] += 1
                    continue
                row["matured"] += 1
                peak = max(p for _, p in before) / entry - 1
                for threshold, suffix in ((0.20,"20"),(0.30,"30")):
                    hit = peak >= threshold
                    if hit:
                        row["movers_"+suffix] += 1
                        if selected: row["watch_"+suffix] += 1
                        else: row["missed_"+suffix] += 1
                    elif selected:
                        row["watch_false_positive_"+suffix] += 1
    for row in results.values():
        assert row["eligible"] == row["matured"] + row["abstain_gap"] + row["immature"]
        for suffix in ("20","30"):
            row["recall_"+suffix] = (row["watch_"+suffix] / row["movers_"+suffix]
                                     if row["movers_"+suffix] else None)
            denom = row["watch_"+suffix] + row["watch_false_positive_"+suffix]
            row["watch_precision_"+suffix] = row["watch_"+suffix] / denom if denom else None
    return {"status":"DESCRIPTIVE_ONLY_NOT_HELD_OUT_LIFT",
            "coverage_warning":"Only observed run/pair timestamps; not complete historical market or intrabar highs. Incomplete periods abstain.",
            "horizons":results}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--verified-ledger",required=True)
    p.add_argument("--output",required=True)
    args=p.parse_args()
    with open(args.verified_ledger) as f: state=json.load(f)
    result=evaluate(state)
    with open(args.output,"w") as f: json.dump(result,f,indent=2,sort_keys=True,allow_nan=False)
    print(json.dumps(result,sort_keys=True))

if __name__=="__main__": main()
