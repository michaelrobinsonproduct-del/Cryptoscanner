"""Run the existing E1 historical reconstruction and E-to-B learning handoff.

All input files are caller-supplied pinned historical archive evidence.
Never fetches live data, modifies scanner state or certifies source authenticity.
"""
import argparse
import hashlib
import json
from pathlib import Path

from .historical_outcome_execution import run_historical_outcomes
from .historical_execution_learning_bridge import project_historical_execution
from .historical_preselection_binding import bind_preselection_history


def bind_a2_projection(projection, predictions):
    """Consume the retained, receipt-bound A2 full-universe E projection.

    The projection is diagnostic evidence, not independent publisher authentication.
    All non-WATCH identities remain explicit in the B cohort.
    """
    from .historical_preselection_binding import bind_preselection_history
    if not isinstance(projection, dict) or projection.get("schema") != "a2_historical_e_preselection_v1":
        raise ValueError("Invalid retained A2 projection")
    if (projection.get("status") != "NO_QUALIFIED_RULE" or
            projection.get("source_authenticated") is not False or
            projection.get("historical_outcomes_available") is not False or
            projection.get("promotion_authorized") is not False or
            projection.get("production_applied") is not False):
        raise ValueError("Unsafe A2 projection qualification")
    receipt = projection.get("a_receipt_sha256")
    if not isinstance(receipt, str) or len(receipt) != 64 or any(c not in "0123456789abcdef" for c in receipt):
        raise ValueError("Missing A2 receipt identity")
    frozen, watches = projection.get("frozen_predictions"), projection.get("e1_watch_predictions")
    if not isinstance(frozen, list) or not isinstance(watches, list) or not frozen:
        raise ValueError("Missing A2 frozen universe")
    ids = [p.get("prediction_id") for p in frozen if isinstance(p, dict)]
    if len(ids) != len(frozen) or len(set(ids)) != len(ids):
        raise ValueError("Duplicate A2 frozen identity")
    for p in frozen:
        if not isinstance(p.get("pair"), str) or not p["pair"] or not isinstance(p.get("prediction_id"), str) or len(p["prediction_id"]) != 64:
            raise ValueError("Malformed A2 frozen identity")
        expected = hashlib.sha256(("paper-preselection-v1|" + receipt + "|" + p["pair"]).encode()).hexdigest()
        if p["prediction_id"] != expected:
            raise ValueError("A2 identity is not bound to sealed receipt")
    frozen_pairs = {p["prediction_id"]: p["pair"] for p in frozen}
    # New A2 projections carry every pre-outcome decision and timestamp.
    # Validate this full cohort before E1 can consume its WATCH subset.
    observations = projection.get("frozen_observations")
    if observations is not None:
        if not isinstance(observations, list) or len(observations) != len(frozen):
            raise ValueError("Incomplete A2 point-in-time universe")
        observed = {}
        for row in observations:
            if not isinstance(row, dict) or row.get("prediction_id") in observed:
                raise ValueError("Duplicate or malformed A2 observation")
            pid = row.get("prediction_id")
            if pid not in {p["prediction_id"] for p in frozen}:
                raise ValueError("Unknown A2 observation")
            if row.get("pair") != next(p["pair"] for p in frozen if p["prediction_id"] == pid):
                raise ValueError("A2 observation pair mismatch")
            if row.get("selection_status") not in ("WATCH", "SCREEN_REJECTED", "NOT_OHLC_SELECTED", "OHLC_ABSTAINED", "NOT_RANKED_WATCH"):
                raise ValueError("Invalid A2 frozen selection")
            if not isinstance(row.get("as_of"), str):
                raise ValueError("Missing A2 observation time")
            from .shadow_learning_evidence import utc_time
            utc_time(row["as_of"])
            observed[pid] = row
        if {pid for pid, row in observed.items() if row["selection_status"] == "WATCH"} != {p["prediction_id"] for p in watches}:
            raise ValueError("A2 WATCH cohort does not match frozen decisions")
        if any(observed[p["prediction_id"]]["as_of"] != p["as_of"] for p in watches):
            raise ValueError("A2 WATCH observation time mismatch")
    if any(not isinstance(p, dict) or p.get("status") != "PAPER_WATCH" or
           not isinstance(p.get("as_of"), str) or not p["as_of"] or
           frozen_pairs.get(p.get("prediction_id")) != p.get("pair")
           for p in watches):
        raise ValueError("Invalid A2 WATCH decision or timestamp")
    watch_ids = {p.get("prediction_id") for p in watches if isinstance(p, dict)}
    if len(watch_ids) != len(watches) or not watch_ids.issubset(set(ids)):
        raise ValueError("Invalid A2 WATCH subset")
    if predictions != watches:
        # Order is irrelevant, but the identity, time and decision are not.
        def indexed(rows):
            return {p["prediction_id"]: p for p in rows}
        if not isinstance(predictions, list) or len(predictions) != len(watches) or indexed(predictions) != indexed(watches):
            raise ValueError("E1 predictions differ from sealed A2 WATCH sample")
    if (projection.get("frozen_observation_count") != len(frozen) or
            projection.get("watch_count") != len(watches) or
            projection.get("nonwatch_without_outcomes") != len(frozen) - len(watches)):
        raise ValueError("A2 frozen universe arithmetic mismatch")
    return {"frozen_predictions": frozen, "e1_watch_predictions": watches,
            "preselection_observation_count": len(frozen),
            "watch_outcome_input_count": len(watches),
            "unobserved_nonwatch_count": len(frozen) - len(watches),
            "a_receipt_sha256": receipt, "unbiased_learning_qualified": False}


def audit_a2_trade_partition_overlap(projection, manifest, root, schema, partitions):
    """Read-only, checksum-gated overlap inventory for the FULL frozen A2 cohort.

    This never calls a trade hit a qualified learning label. It exposes exactly
    which pre-outcome observations have pinned trade-bar evidence and which
    abstain because no partition or matching observation window exists.
    """
    binding = bind_a2_projection(projection, projection["e1_watch_predictions"])
    rows = projection.get("frozen_observations")
    if not isinstance(rows, list) or len(rows) != binding["preselection_observation_count"]:
        raise ValueError("Complete timestamped A2 universe required")
    from .kraken_trade_csv_adapter import convert_pinned_csv
    from .shadow_learning_evidence import utc_time
    from datetime import timedelta
    from bisect import bisect_left
    if not isinstance(partitions, dict):
        raise ValueError("Missing explicit partition map")
    pairs = {row["pair"] for row in rows}
    bars = {}
    provenance = {}
    for pair in sorted(pairs):
        partition = partitions.get(pair)
        if partition is None:
            bars[pair] = []
            provenance[pair] = {"status": "NO_PINNED_PARTITION"}
            continue
        result = convert_pinned_csv(manifest, root, partition_file=partition,
                                    pair=pair, schema=schema)
        bars[pair] = sorted(utc_time(b["open_at"]) for b in result["bars"])
        provenance[pair] = {"status": "PINNED_BYTES_VERIFIED",
                            "partition": partition,
                            "partition_sha256": result["partition_sha256"],
                            "trade_count": result["parsed_trade_count"],
                            "bar_count": result["bar_count"]}
    status_counts = {"NO_PINNED_PARTITION": 0, "NO_ENTRY_BAR": 0,
                     "ENTRY_BAR_PRESENT_UNQUALIFIED": 0}
    by_selection = {}
    for row in rows:
        at = utc_time(row["as_of"])
        times = bars[row["pair"]]
        if not times:
            status = ("NO_PINNED_PARTITION" if row["pair"] not in partitions
                      else "NO_ENTRY_BAR")
        else:
            # A next-five-minute bar is diagnostic, never executable liquidity.
            start = at.replace(second=0, microsecond=0)
            start -= timedelta(minutes=start.minute % 5)
            target = start + timedelta(minutes=5)
            idx = bisect_left(times, target)
            status = ("ENTRY_BAR_PRESENT_UNQUALIFIED"
                      if idx < len(times) and times[idx] == target
                      else "NO_ENTRY_BAR")
        status_counts[status] += 1
        by_selection.setdefault(row["selection_status"], {})
        d = by_selection[row["selection_status"]]
        d[status] = d.get(status, 0) + 1
    if sum(status_counts.values()) != len(rows):
        raise ValueError("Historical overlap cohort mismatch")
    return {"schema": "a2_trade_partition_overlap_v1",
            "a_receipt_sha256": binding["a_receipt_sha256"],
            "frozen_observation_count": len(rows),
            "status_counts": status_counts, "selection_status_counts": by_selection,
            "partition_provenance": provenance,
            "qualified_outcome_count": 0, "source_authenticated": False,
            "qualified_for_learning": False, "promotion_authorized": False,
            "read_only": True}


def run_pipeline(manifest, root, schema, partitions, predictions, observed_until, *, preselection_history=None, a2_projection=None):
    if preselection_history is not None and a2_projection is not None:
        raise ValueError("Select one frozen A provenance source")
    binding = bind_a2_projection(a2_projection, predictions) if a2_projection is not None else None
    if preselection_history is not None:
        binding = bind_preselection_history(preselection_history, predictions)
    execution = run_historical_outcomes(
        manifest, root, schema, partitions, predictions, observed_until)
    frozen = binding["frozen_predictions"] if binding is not None else predictions
    handoff = project_historical_execution(execution, frozen_predictions=frozen)
    # Consume B's existing strict read-only learning contract rather than
    # introducing a second evaluator or reimplementing its qualification.
    from .github_delivery_projection import _learning_evidence
    delivery = _learning_evidence(handoff)
    if delivery["status"] != "NO_QUALIFIED_RULE" or delivery["promotion_authorized"]:
        raise ValueError("Historical source cannot authorize a learning rule")
    return {"execution": execution, "handoff": handoff, "delivery": delivery,
            "preselection_binding": binding}


def main(argv=None):
    parser = argparse.ArgumentParser(description="E1 pinned historical outcomes to B read-only consumer")
    for key in ("manifest", "root", "schema", "partitions", "predictions", "observed-until", "output"):
        parser.add_argument("--" + key, required=True)
    parser.add_argument("--preselection-history", help="A receipt-verified historical full-universe JSON")
    parser.add_argument("--a2-projection", help="Retained E A2 receipt-bound preselection JSON")
    parser.add_argument("--full-cohort-overlap-output", help="Write checksum-gated A2 all-candidate trade overlap diagnostics")
    parser.add_argument("--a-receipts-dir", help="Original sealed A receipts; verify via A export_receipt_history")
    args = parser.parse_args(argv)
    if sum(bool(v) for v in (args.preselection_history, args.a_receipts_dir, args.a2_projection)) > 1:
        parser.error("Select only one A preselection provenance source")
    output = Path(args.output)
    if output.exists():
        raise FileExistsError("Refusing to overwrite prior historical evidence")
    def read(name):
        return json.loads(Path(getattr(args, name)).read_text(encoding="utf-8"))
    history = read("preselection_history") if args.preselection_history else None
    if args.a_receipts_dir:
        from .preselection_universe import export_receipt_history
        history = export_receipt_history(args.a_receipts_dir)
    manifest, schema, partitions, predictions = (read(k) for k in ("manifest", "schema", "partitions", "predictions"))
    projection = read("a2_projection") if args.a2_projection else None
    if args.full_cohort_overlap_output:
        if projection is None:
            parser.error("--full-cohort-overlap-output requires --a2-projection")
        overlap_path = Path(args.full_cohort_overlap_output)
        if overlap_path.exists():
            raise FileExistsError("Refusing to overwrite historical overlap evidence")
        overlap = audit_a2_trade_partition_overlap(projection, manifest, args.root, schema, partitions)
        overlap_path.write_text(json.dumps(overlap, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    result = run_pipeline(manifest, args.root, schema,
                          partitions, predictions, args.observed_until,
                          preselection_history=history,
                          a2_projection=projection)
    output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"prediction_count": result["execution"]["prediction_count"],
                      "status_counts": result["execution"]["status_counts"],
                      "qualified_cohort_count": result["handoff"]["qualified_cohort_count"],
                      "learning_status": result["delivery"]["status"]}, sort_keys=True))


if __name__ == "__main__":
    main()
