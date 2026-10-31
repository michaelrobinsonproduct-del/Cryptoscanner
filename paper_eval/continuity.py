"""Read-only, fail-closed proof that two paper ledger generations form one history.

No market requests, ledger writes, order placement, or model promotion.
The previous ledger snapshot is essential: a checksum on the new snapshot
alone cannot prove that earlier predictions were not rewritten or dropped.
"""
import argparse
import datetime as dt
import hashlib
import json
from collections import defaultdict
from pathlib import Path

from paper_eval.audit import _timeline, _validate
from paper_pov import ledger
from paper_pov.scanner import atomic_json, utc


def _delta(before, after, key):
    old = before.get("archived", {}).get(key, 0)
    new = after.get("archived", {}).get(key, 0)
    if type(old) is not int or type(new) is not int or new < old:
        raise ValueError("Regressing archived " + key)
    return new - old


def verify_transition(before, after):
    """Independently reconcile a single append, including a 50h compaction."""
    ledger.verify(before)
    ledger.verify(after)
    _validate(before)
    _validate(after)
    if after["generation"] != before["generation"] + 1:
        raise ValueError("Expected exactly one new ledger generation")
    if not after["runs"]:
        raise ValueError("Missing appended paper scan")
    old_runs, new_runs = before["runs"], after["runs"]
    added = new_runs[-1]
    if added["id"] in {r["id"] for r in old_runs}:
        raise ValueError("Replayed prior run")
    if old_runs and utc(added["as_of"]) <= utc(old_runs[-1]["as_of"]):
        raise ValueError("Appended run is not later than predecessor")
    retained_count = len(new_runs) - 1
    removed_count = len(old_runs) - retained_count
    if removed_count < 0 or new_runs[:-1] != old_runs[removed_count:]:
        raise ValueError("Prior run history was modified or reordered")
    removed = old_runs[:removed_count]
    removed_ids = {r["id"] for r in removed}
    new_id = added["id"]

    old_preds = before["predictions"]
    retained_preds = [p for p in old_preds if p["run_id"] not in removed_ids]
    removed_preds = [p for p in old_preds if p["run_id"] in removed_ids]
    new_preds = [p for p in after["predictions"] if p["run_id"] == new_id]
    if after["predictions"] != retained_preds + new_preds:
        raise ValueError("Immutable prediction history changed")
    if len(new_preds) != added["watch_count"]:
        raise ValueError("New prediction count mismatch")
    old_quotes = before["observations"]
    retained_quotes = [o for o in old_quotes if o["run_id"] not in removed_ids]
    removed_quotes = [o for o in old_quotes if o["run_id"] in removed_ids]
    new_quotes = [o for o in after["observations"] if o["run_id"] == new_id]
    if after["observations"] != retained_quotes + new_quotes:
        raise ValueError("Recorded market quote history changed")
    if len(new_quotes) != added["observation_count"]:
        raise ValueError("New observation count mismatch")

    removed_pred_ids = {p["prediction_id"] for p in removed_preds}
    old_outcomes = {(o["prediction_id"], o["horizon_hours"]): o
                    for o in before["outcomes"]
                    if o["prediction_id"] not in removed_pred_ids}
    new_outcomes = {(o["prediction_id"], o["horizon_hours"]): o
                    for o in after["outcomes"]}
    for key, outcome in old_outcomes.items():
        if new_outcomes.get(key) != outcome:
            raise ValueError("Previously recorded outcome was altered")
    if any(o["prediction_id"] in {p["prediction_id"] for p in new_preds}
           for o in after["outcomes"]):
        raise ValueError("New scan already has future outcomes")

    if _delta(before, after, "scans") != len(removed):
        raise ValueError("Archived run count does not match compaction")
    if _delta(before, after, "predictions") != len(removed_preds):
        raise ValueError("Archived prediction count does not match compaction")
    if _delta(before, after, "observations") != len(removed_quotes):
        raise ValueError("Archived observation count does not match compaction")
    expected_index = [r for r in before.get("archive_index", []) + removed
                      if utc(r["as_of"]) >= utc(added["as_of"]) - ledger.ARCHIVE_INDEX_RETENTION]
    if after.get("archive_index", []) != expected_index:
        raise ValueError("Archived run provenance index changed")

    # Independently reconstruct the exact aggregate labels that compaction
    # removes. Prior quotes plus this new scan are the full available sample
    # set; never infer exchange-complete highs from ticker snapshots.
    by_pair = defaultdict(list)
    for observation in old_quotes + new_quotes:
        by_pair[observation["pair"]].append(observation)
    reconstructed_matured = reconstructed_gaps = reconstructed_hits = 0
    for prediction in removed_preds:
        begin = utc(prediction["as_of"])
        for hours in ledger.HORIZONS:
            target = begin + dt.timedelta(hours=hours)
            if utc(added["as_of"]) < target + ledger.MAX_DELAY:
                raise ValueError("Compaction before outcome maturity")
            timeline = _timeline(prediction["pair"], begin, target, by_pair)
            if timeline is None:
                reconstructed_gaps += 1
            else:
                reconstructed_matured += 1
                window, _ = timeline
                peak = 100 * (max(o["price"] for o in window) / prediction["price"] - 1)
                reconstructed_hits += int(peak >= 30)
    if _delta(before, after, "matured_labels") != reconstructed_matured:
        raise ValueError("Archived matured-label totals disagree with recorded quotes")
    if _delta(before, after, "gap_abstentions") != reconstructed_gaps:
        raise ValueError("Archived gap totals disagree with recorded quotes")
    if _delta(before, after, "observed_30pct_hits") != reconstructed_hits:
        raise ValueError("Archived sampled-hit totals disagree with recorded quotes")
    if (ledger.scoreboard(after)["immutable_predictions"]
            != ledger.scoreboard(before)["immutable_predictions"] + len(new_preds)):
        raise ValueError("Lifetime prediction totals regressed")
    if (ledger.scoreboard(after)["market_observations"]
            != ledger.scoreboard(before)["market_observations"] + len(new_quotes)):
        raise ValueError("Lifetime observation totals regressed")
    return {
        "schema": 1, "mode": "READ_ONLY_PAPER_TRANSITION_AUDIT",
        "from_generation": before["generation"], "to_generation": after["generation"],
        "from_ledger_sha256": before["sha256"], "to_ledger_sha256": after["sha256"],
        "new_run_id": new_id, "new_run_as_of": added["as_of"],
        "new_predictions": len(new_preds), "new_observations": len(new_quotes),
        "compacted_runs": len(removed), "compacted_predictions": len(removed_preds),
        "compacted_observations": len(removed_quotes),
        "reconstructed_compacted_matured": reconstructed_matured,
        "reconstructed_compacted_gaps": reconstructed_gaps,
        "reconstructed_compacted_sampled_hits": reconstructed_hits,
        "prior_records_immutable": True, "production_applied": False,
        "limitations": "Client-observed sampled Kraken quotes; not authenticated exchange highs or independently proven predictive uplift."
    }


def main():
    parser = argparse.ArgumentParser()
    for flag in ("before", "after", "before-commit", "after-commit", "output"):
        parser.add_argument("--" + flag, required=True)
    args = parser.parse_args()
    for commit in (args.before_commit, args.after_commit):
        if len(commit) != 40 or any(c not in "0123456789abcdef" for c in commit):
            raise ValueError("Exact immutable Git commit SHA required")
    before = json.loads(Path(args.before).read_text())
    after = json.loads(Path(args.after).read_text())
    result = verify_transition(before, after)
    result["before_commit"] = args.before_commit
    result["after_commit"] = args.after_commit
    result["report_sha256"] = hashlib.sha256(ledger.canonical(result)).hexdigest()
    atomic_json(args.output, result)
    if json.loads(Path(args.output).read_text()) != result:
        raise ValueError("Atomic transition audit readback mismatch")
    print("PAPER_TRANSITION_AUDIT", json.dumps({
        "from_generation": result["from_generation"],
        "to_generation": result["to_generation"],
        "compacted_runs": result["compacted_runs"],
        "compacted_gaps": result["reconstructed_compacted_gaps"],
        "report_sha256": result["report_sha256"],
        "production_applied": False
    }, sort_keys=True))


if __name__ == "__main__":
    main()
