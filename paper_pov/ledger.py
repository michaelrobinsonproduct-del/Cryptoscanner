"""Fail-closed paper ledger: immutable as-of predictions, delayed observed outcomes.

No model promotion or production IO. This is a staging contract, not yet a
30-day storage design; oversized state aborts rather than resetting history.
"""
import datetime as dt
import hashlib
import json
import math
from pathlib import Path
from .scanner import utc, atomic_json

HORIZONS = (1, 6, 24, 48)
MAX_BYTES = 12_000_000
RETENTION = dt.timedelta(hours=50)
ARCHIVE_INDEX_RETENTION = dt.timedelta(days=30)
MAX_DELAY = dt.timedelta(minutes=45)

def canonical(data):
    return json.dumps(data, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()

def seal(state):
    payload = {k: v for k, v in state.items() if k != "sha256"}
    state["sha256"] = hashlib.sha256(canonical(payload)).hexdigest()
    return state

def empty():
    return seal({"schema": 1, "generation": 0, "runs": [],
                 "predictions": [], "observations": [], "outcomes": []})

def verify(state):
    if not isinstance(state, dict) or state.get("schema") != 1:
        raise ValueError("Missing or incompatible ledger schema")
    if not isinstance(state.get("generation"), int) or state["generation"] < 0:
        raise ValueError("Invalid ledger generation")
    if any(not isinstance(state.get(k), list) for k in ("runs", "predictions", "observations", "outcomes")):
        raise ValueError("Invalid ledger collections")
    digest = state.get("sha256")
    if not isinstance(digest, str) or len(digest) != 64:
        raise ValueError("Missing ledger checksum")
    if seal(dict(state))["sha256"] != digest:
        raise ValueError("Ledger checksum mismatch")
    runs = state["runs"]
    if len({x["id"] for x in runs}) != len(runs):
        raise ValueError("Duplicate run IDs")
    if any(utc(b["as_of"]) <= utc(a["as_of"]) for a, b in zip(runs, runs[1:])):
        raise ValueError("Nonmonotonic run timestamps")
    ids = [p["prediction_id"] for p in state["predictions"]]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate immutable prediction ID")
    keys = [(o["prediction_id"], o["horizon_hours"]) for o in state["outcomes"]]
    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate outcome")
    # A checksum authenticates bytes, not the ledger's internal relationships.
    # Reject partial, orphaned or re-sealed data before it can generate labels.
    run_map = {}
    for r in runs:
        rid = r.get("id")
        if not isinstance(rid, str) or len(rid) != 64 or any(c not in "0123456789abcdef" for c in rid):
            raise ValueError("Invalid run identity")
        if rid in run_map:
            raise ValueError("Duplicate run IDs")
        if not isinstance(r.get("source_sha"), str) or len(r["source_sha"]) != 40 or any(c not in "0123456789abcdef" for c in r["source_sha"]):
            raise ValueError("Invalid run source SHA")
        if not isinstance(r.get("report_sha256"), str) or len(r["report_sha256"]) != 64 or any(c not in "0123456789abcdef" for c in r["report_sha256"]):
            raise ValueError("Invalid run report checksum")
        if type(r.get("watch_count")) is not int or not 1 <= r["watch_count"] <= 12:
            raise ValueError("Invalid run watch count")
        if type(r.get("observation_count")) is not int or r["observation_count"] < r["watch_count"]:
            raise ValueError("Invalid run observation count")
        utc(r["as_of"])
        run_map[rid] = r
    prediction_counts = {rid: 0 for rid in run_map}
    observation_counts = {rid: 0 for rid in run_map}
    prediction_pairs = {rid: set() for rid in run_map}
    observation_pairs = {rid: set() for rid in run_map}
    prediction_ranks = {rid: set() for rid in run_map}
    for p in state["predictions"]:
        rid = p.get("run_id")
        if rid not in run_map:
            raise ValueError("Orphan paper prediction")
        r = run_map[rid]
        pair = p.get("pair")
        if not isinstance(pair, str) or not pair or pair in prediction_pairs[rid]:
            raise ValueError("Invalid or duplicate prediction market")
        if utc(p["as_of"]) != utc(r["as_of"]):
            raise ValueError("Prediction as-of mismatch")
        expected = hashlib.sha256(("paper-v1|" + p["as_of"] + "|" + pair).encode()).hexdigest()
        if p["prediction_id"] != expected:
            raise ValueError("Prediction identity mismatch")
        price = float(p["price"])
        if not math.isfinite(price) or price <= 0:
            raise ValueError("Invalid prediction price")
        rank = p.get("rank")
        if type(rank) is not int or not 1 <= rank <= r["watch_count"] or rank in prediction_ranks[rid]:
            raise ValueError("Invalid prediction rank")
        for key in ("baseline_score", "challenger_score"):
            if not math.isfinite(float(p[key])):
                raise ValueError("Invalid prediction score")
        prediction_pairs[rid].add(pair)
        prediction_ranks[rid].add(rank)
        prediction_counts[rid] += 1
    for o in state["observations"]:
        rid = o.get("run_id")
        if rid not in run_map:
            raise ValueError("Orphan market observation")
        pair = o.get("pair")
        if not isinstance(pair, str) or not pair or pair in observation_pairs[rid]:
            raise ValueError("Invalid or duplicate observation market")
        at = utc(o["at"])
        as_of = utc(run_map[rid]["as_of"])
        if at > as_of or (as_of - at).total_seconds() > 180:
            raise ValueError("Observation timestamp outside run")
        price = float(o["price"])
        if not math.isfinite(price) or price <= 0:
            raise ValueError("Invalid observation price")
        observation_pairs[rid].add(pair)
        observation_counts[rid] += 1
    for rid, r in run_map.items():
        if prediction_counts[rid] != r["watch_count"] or prediction_ranks[rid] != set(range(1, r["watch_count"] + 1)):
            raise ValueError("Prediction count/rank mismatch")
        if observation_counts[rid] != r["observation_count"]:
            raise ValueError("Observation count mismatch")
        if not prediction_pairs[rid].issubset(observation_pairs[rid]):
            raise ValueError("Prediction market lacks observed quote")
    valid_predictions = set(ids)
    for o in state["outcomes"]:
        if o.get("prediction_id") not in valid_predictions or type(o.get("horizon_hours")) is not int or o["horizon_hours"] not in HORIZONS:
            raise ValueError("Orphan or invalid paper outcome")
        if o.get("status") not in ("ABSTAIN_GAP", "MATURED_OBSERVED"):
            raise ValueError("Invalid paper outcome status")
    summary = state.get("archived", {})
    if not isinstance(summary, dict) or any(not isinstance(v, int) or v < 0 for v in summary.values()):
        raise ValueError("Invalid archive summary")
    if not isinstance(state.get("archive_index", []), list):
        raise ValueError("Invalid archive index")
    if state["generation"] != summary.get("scans", 0) + len(runs):
        raise ValueError("Nonregressing generation/scan count mismatch")
    if len(canonical(state)) > MAX_BYTES:
        raise ValueError("Ledger capacity reached: archive/partition before proceeding")
    return state

def advance(original, report, source_sha):
    verify(original)
    if not isinstance(source_sha, str) or len(source_sha) != 40 or any(c not in "0123456789abcdef" for c in source_sha):
        raise ValueError("Invalid immutable source commit SHA")
    if not isinstance(report, dict) or report.get("schema") != 1 or report.get("mode") != "PAPER_ONLY" or report.get("buy_approved") is not False or report.get("production_applied") is not False:
        raise ValueError("Not an approved paper-only report")
    as_of = utc(report["as_of"])
    if original["runs"] and as_of <= utc(original["runs"][-1]["as_of"]):
        raise ValueError("Out-of-order or duplicate scan; do not reset ledger")
    if utc(report["started_at"]) > as_of or (as_of - utc(report["started_at"])).total_seconds() > 300:
        raise ValueError("Invalid scan duration")
    watch = report["watch"]
    observations = report["observations"]
    if not watch or not observations or len(watch) > 12 or len({x["pair"] for x in watch}) != len(watch):
        raise ValueError("Empty, duplicate or oversized watch")
    if len({x["pair"] for x in observations}) != len(observations):
        raise ValueError("Duplicate market observation")
    if report.get("observed_markets") != len(observations):
        raise ValueError("Market observation count mismatch")
    report_hash = hashlib.sha256(canonical(report)).hexdigest()
    run_id = hashlib.sha256((source_sha + "|" + report_hash).encode()).hexdigest()
    state = {k: list(v) if isinstance(v, list) else
        (dict(v) if isinstance(v, dict) else v) for k, v in original.items()}
    state.setdefault("archived", {"scans": 0, "predictions": 0,
        "observations": 0, "matured_labels": 0,
        "gap_abstentions": 0, "observed_30pct_hits": 0})
    state.setdefault("archive_index", [])
    state["runs"].append({"id": run_id, "as_of": report["as_of"],
        "source_sha": source_sha, "report_sha256": report_hash,
        "watch_count": len(watch), "observation_count": len(observations)})
    seen = set()
    for p in watch:
        price = float(p["price"])
        if not math.isfinite(price) or price <= 0 or p["status"] != "PAPER_WATCH":
            raise ValueError("Invalid paper prediction")
        if utc(p["as_of"]) != as_of or not utc(p["quote_observed_at"]) <= as_of:
            raise ValueError("Prediction as-of or quote time invalid")
        if (as_of - utc(p["quote_observed_at"])).total_seconds() > 180:
            raise ValueError("Stale prediction quote")
        expected = hashlib.sha256(("paper-v1|" + report["as_of"] + "|" + p["pair"]).encode()).hexdigest()
        if p["prediction_id"] != expected or expected in seen:
            raise ValueError("Prediction identity mismatch")
        seen.add(expected)
        state["predictions"].append({"prediction_id": expected, "run_id": run_id,
            "as_of": report["as_of"], "pair": p["pair"], "price": price,
            "baseline_score": p["baseline_score"], "challenger_score": p["challenger_score"],
            "rank": p["rank"]})
    for o in observations:
        price = float(o["price"])
        at = utc(o["observed_at"])
        if not math.isfinite(price) or price <= 0 or at > as_of or (as_of - at).total_seconds() > 180:
            raise ValueError("Invalid or stale market observation")
        state["observations"].append({"run_id": run_id, "at": o["observed_at"],
            "pair": o["pair"], "price": price})
    existing = {(x["prediction_id"], x["horizon_hours"]) for x in state["outcomes"]}
    by_pair = {}
    for o in state["observations"]:
        by_pair.setdefault(o["pair"], []).append(o)
    for p in state["predictions"]:
        begin = utc(p["as_of"])
        for hours in HORIZONS:
            key = (p["prediction_id"], hours)
            if key in existing:
                continue
            target = begin + dt.timedelta(hours=hours)
            if as_of < target + MAX_DELAY:
                continue  # Never use an immature horizon.
            series = sorted((o for o in by_pair.get(p["pair"], [])
                if begin < utc(o["at"]) <= target + MAX_DELAY), key=lambda o: o["at"])
            anchors = [o for o in series if target <= utc(o["at"]) <= target + MAX_DELAY]
            in_window = [o for o in series if utc(o["at"]) <= target]
            timeline = [begin] + [utc(o["at"]) for o in in_window]
            contiguous = bool(anchors) and bool(in_window) and all(
                b - a <= MAX_DELAY for a, b in zip(timeline, timeline[1:]))
            if not contiguous or utc(anchors[0]["at"]) - timeline[-1] > MAX_DELAY:
                state["outcomes"].append({"prediction_id": p["prediction_id"],
                    "horizon_hours": hours, "status": "ABSTAIN_GAP",
                    "target_at": target.isoformat()})
            else:
                final = anchors[0]
                ret = 100 * (final["price"] / p["price"] - 1)
                peak = 100 * (max(x["price"] for x in in_window) / p["price"] - 1)
                state["outcomes"].append({"prediction_id": p["prediction_id"],
                    "horizon_hours": hours, "status": "MATURED_OBSERVED",
                    "target_at": target.isoformat(), "observed_at": final["at"],
                    "return_pct": round(ret, 4), "observed_peak_pct": round(peak, 4),
                    "observed_30pct_hit": peak >= 30})
            existing.add(key)
    # Compact only after all four 1/6/24/48h horizons have matured or abstained.
    # Individual historical records remain in 90-day checksummed run artifacts;
    # the Git branch retains the latest 50h and 30d run provenance index.
    cutoff = as_of - RETENTION
    old_runs = [r for r in state["runs"] if utc(r["as_of"]) < cutoff]
    old_predictions = [p for p in state["predictions"] if utc(p["as_of"]) < cutoff]
    old_ids = {p["prediction_id"] for p in old_predictions}
    archived_outcomes = [o for o in state["outcomes"] if o["prediction_id"] in old_ids]
    if any(sum((o["prediction_id"] == p["prediction_id"]) for o in archived_outcomes) != len(HORIZONS)
           for p in old_predictions):
        raise ValueError("Cannot archive prediction with immature or missing outcomes")
    # Preserve quotes by owning run, not their slightly earlier client timestamp.
    # Otherwise a retained run can lose a quote at the 50-hour boundary.
    old_run_ids = {r["id"] for r in old_runs}
    old_observations = [o for o in state["observations"] if o["run_id"] in old_run_ids]
    summary = state["archived"]
    summary["scans"] += len(old_runs)
    summary["predictions"] += len(old_predictions)
    summary["observations"] += len(old_observations)
    summary["matured_labels"] += sum(o["status"] == "MATURED_OBSERVED" for o in archived_outcomes)
    summary["gap_abstentions"] += sum(o["status"] == "ABSTAIN_GAP" for o in archived_outcomes)
    summary["observed_30pct_hits"] += sum(o.get("observed_30pct_hit") is True for o in archived_outcomes)
    state["archive_index"].extend(old_runs)
    state["archive_index"] = [r for r in state["archive_index"]
        if utc(r["as_of"]) >= as_of - ARCHIVE_INDEX_RETENTION]
    state["runs"] = [r for r in state["runs"] if utc(r["as_of"]) >= cutoff]
    state["predictions"] = [p for p in state["predictions"] if p["prediction_id"] not in old_ids]
    state["observations"] = [o for o in state["observations"] if o["run_id"] not in old_run_ids]
    state["outcomes"] = [o for o in state["outcomes"] if o["prediction_id"] not in old_ids]
    state["generation"] += 1
    seal(state)
    verify(state)
    return state

def scoreboard(state):
    verify(state)
    outcomes = state["outcomes"]
    archived = state.get("archived", {})
    return {"generation": state["generation"],
        "actual_scans": archived.get("scans", 0) + len(state["runs"]),
        "immutable_predictions": archived.get("predictions", 0) + len(state["predictions"]),
        "market_observations": archived.get("observations", 0) + len(state["observations"]),
        "matured_labels": archived.get("matured_labels", 0) + sum(x["status"] == "MATURED_OBSERVED" for x in outcomes),
        "gap_abstentions": archived.get("gap_abstentions", 0) + sum(x["status"] == "ABSTAIN_GAP" for x in outcomes),
        "observed_30pct_hits": archived.get("observed_30pct_hits", 0) + sum(x.get("observed_30pct_hit") is True for x in outcomes),
        "held_out_lift": None, "production_applied": False,
        "ledger_sha256": state["sha256"]}

def update_file(input_path, report_path, source_sha, output_path):
    source = Path(input_path)
    if not source.is_file():
        raise FileNotFoundError("Existing ledger absent; explicit bootstrap required")
    state = json.loads(source.read_text())
    report = json.loads(Path(report_path).read_text())
    next_state = advance(state, report, source_sha)
    atomic_json(output_path, next_state)
    return scoreboard(next_state)
