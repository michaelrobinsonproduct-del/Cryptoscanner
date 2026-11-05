"""Bind historical E1 WATCH-only outcomes to A's frozen complete preselection universe.

E1 currently accepts only PAPER_WATCH rows. Do not pretend its WATCH-only
sample is an unbiased historical candidate universe. Export every observed A
identity, with explicit missing non-WATCH outcomes, for B's read-only abstention.
"""
import hashlib
import json


def bind_preselection_history(history, watch_predictions):
    if not isinstance(history, dict) or history.get("schema") != "paper_preselection_history_v1":
        raise ValueError("Expected receipt-verified A preselection history")
    if (history.get("snapshot_use") != "HISTORICAL_RESEARCH_ONLY" or
            history.get("future_outcomes_authenticated") is not False or
            history.get("qualified_for_learning") is not False):
        raise ValueError("Unsafe historical preselection provenance")
    snapshots = history.get("snapshots")
    if not isinstance(snapshots, list) or not snapshots:
        raise ValueError("Missing historical A receipts")
    universe = {}
    watch = {}
    receipts = set()
    for snapshot in snapshots:
        if snapshot.get("schema") != "paper_preselection_v1" or snapshot.get("snapshot_use") != "HISTORICAL_RESEARCH_ONLY":
            raise ValueError("Nonhistorical A snapshot")
        receipt = snapshot.get("receipt_sha256")
        if not isinstance(receipt, str) or len(receipt) != 64 or receipt in receipts:
            raise ValueError("Invalid or duplicate sealed receipt")
        receipts.add(receipt)
        markets = snapshot.get("markets")
        if not isinstance(markets, list) or len(markets) != snapshot.get("coverage", {}).get("valid_tickers"):
            raise ValueError("Incomplete preselection coverage")
        for market in markets:
            pair = market.get("pair")
            pid = market.get("observation_id")
            if not isinstance(pair, str) or not pair or not isinstance(pid, str) or len(pid) != 64:
                raise ValueError("Invalid preselection identity")
            expected = hashlib.sha256(("paper-preselection-v1|" + receipt + "|" + pair).encode()).hexdigest()
            if pid != expected or pid in universe:
                raise ValueError("Unbound or duplicate A observation")
            status = market.get("selection_status")
            if status not in ("SCREEN_REJECTED", "NOT_OHLC_SELECTED", "OHLC_ABSTAINED", "WATCH", "NOT_RANKED_WATCH"):
                raise ValueError("Unknown A selection decision")
            universe[pid] = {"prediction_id": pid, "pair": pair}
            if status == "WATCH":
                watch[pid] = {"prediction_id": pid, "pair": pair, "as_of": snapshot["as_of"], "status": "PAPER_WATCH"}
    if len(universe) != history.get("market_observation_count") or len(snapshots) != history.get("receipt_count"):
        raise ValueError("Historical A universe count mismatch")
    if not isinstance(watch_predictions, list):
        raise ValueError("Missing E1 WATCH predictions")
    supplied = {p.get("prediction_id"): p for p in watch_predictions}
    if len(supplied) != len(watch_predictions) or set(supplied) != set(watch):
        raise ValueError("E1 WATCH sample differs from frozen A WATCH identities")
    for pid, expected in watch.items():
        if supplied[pid] != expected:
            raise ValueError("E1 WATCH timestamps or market mismatch A receipt")
    return {"frozen_predictions": [universe[k] for k in sorted(universe)],
            "e1_watch_predictions": [watch[k] for k in sorted(watch)],
            "preselection_observation_count": len(universe),
            "watch_outcome_input_count": len(watch),
            "unobserved_nonwatch_count": len(universe) - len(watch),
            "preselection_history_sha256": hashlib.sha256(json.dumps(
                history, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
            "unbiased_learning_qualified": False}
