"""Read-only B/D consumer of C's authenticated A2 candidate handoff.

A historical candidate artifact is useful for replay, never a live signal.
"""
import argparse
import json
import re
from pathlib import Path


def consume(payload):
    if not isinstance(payload, dict) or payload.get("schema") != "c_a2_read_only_candidates_v1":
        raise ValueError("unsupported C candidate contract")
    if payload.get("production_applied") is not False or payload.get("trading_approved") is not False or payload.get("live_watch_certified") is not False:
        raise ValueError("unsafe C candidate certification")
    if payload.get("status") != "ABSTAIN_LEGACY_QUOTE_EVIDENCE" or payload.get("freshness_status") != "HISTORICAL_ARTIFACT_NOT_LIVE":
        raise ValueError("historical freshness abstention missing")
    if payload.get("quote_timestamp_semantics") != "client_observed_not_exchange_event_time":
        raise ValueError("unqualified exchange timestamp")
    digest = payload.get("receipt_sha256")
    if not isinstance(digest, str) or not re.fullmatch(r"[a-f0-9]{64}", digest):
        raise ValueError("missing authenticated receipt identity")
    watch = payload.get("watch")
    count = payload.get("watch_count")
    if not isinstance(watch, list) or not watch or type(count) is not int or count != len(watch):
        raise ValueError("candidate count mismatch")
    eligible, observed = payload.get("eligible_pairs"), payload.get("observed_markets")
    if any(type(x) is not int or x < 0 for x in (eligible, observed)) or not count <= observed <= eligible:
        raise ValueError("invalid source coverage")
    if not isinstance(payload.get("source_as_of"), str) or not payload["source_as_of"]:
        raise ValueError("missing source time")
    if payload.get("source_cohort") != "authenticated_snapshot_distinct_from_historical_manual_scheduled":
        raise ValueError("invalid source cohort")
    if any(not isinstance(x, dict) for x in watch):
        raise ValueError("invalid candidate item")
    pairs, ranks = [], []
    for item in watch:
        pair, rank = item.get("pair"), item.get("rank")
        if not isinstance(pair, str) or not pair or type(rank) is not int or rank < 1:
            raise ValueError("candidate identity or rank invalid")
        if item.get("status") != "PAPER_WATCH":
            raise ValueError("candidate is not an explicit paper WATCH")
        pairs.append(pair)
        ranks.append(rank)
    if len(set(pairs)) != count or len(set(ranks)) != count:
        raise ValueError("duplicate candidate pair or rank")
    if sorted(ranks) != list(range(1, count + 1)):
        raise ValueError("candidate ranks are not contiguous")
    return {
        "schema": "bd_read_only_watch_handoff_v1",
        "status": "WATCH_REPLAY_ONLY_NOT_LIVE",
        "receipt_sha256": digest,
        "source_as_of": payload["source_as_of"],
        "watch_count": count,
        "watch": watch,
        "live_watch_certified": False,
        "production_applied": False,
        "trading_approved": False,
    }


def from_integration(integration):
    """Convert authenticated C integration evidence into the B/D replay contract."""
    if not isinstance(integration, dict) or integration.get("schema") != "c_read_only_integration_v1":
        raise ValueError("invalid C integration schema")
    if integration.get("historical_artifact_parity") is not True:
        raise ValueError("C historical parity not established")
    for key in ("manual_run", "scheduled_run"):
        if not isinstance(integration.get(key), str) or not integration[key].isdigit():
            raise ValueError("C historical run identity missing")
    if integration["manual_run"] == integration["scheduled_run"]:
        raise ValueError("C manual and scheduled runs must be distinct")
    if integration.get("status") != "ABSTAIN_LEGACY_QUOTE_EVIDENCE" or integration.get("recovery_verified") is not True:
        raise ValueError("C recovery is not verified")
    if integration.get("a2_snapshot_attached") is not True or integration.get("exchange_event_freshness_verified") is not False:
        raise ValueError("C A2 evidence is missing or falsely live-certified")
    if integration.get("production_applied") is not False or integration.get("trading_approved") is not False:
        raise ValueError("C integration is not read-only")
    payload = {
        "schema": "c_a2_read_only_candidates_v1",
        "receipt_sha256": integration.get("a2_receipt_sha256"),
        "source_as_of": integration.get("a2_as_of"),
        "quote_timestamp_semantics": "client_observed_not_exchange_event_time",
        "freshness_status": "HISTORICAL_ARTIFACT_NOT_LIVE",
        "source_cohort": integration.get("a2_source_cohort"),
        "eligible_pairs": integration.get("a2_eligible_pairs"),
        "observed_markets": integration.get("a2_observed_markets"),
        "watch_count": integration.get("a2_watch_count"),
        "watch": integration.get("a2_watch_candidates"),
        "status": "ABSTAIN_LEGACY_QUOTE_EVIDENCE",
        "live_watch_certified": False,
        "production_applied": False,
        "trading_approved": False,
    }
    consume(payload)
    # Detach the replay artifact from caller-owned nested WATCH objects.
    return json.loads(json.dumps(payload, allow_nan=False))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("candidates", type=Path)
    parser.add_argument("--from-integration", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = json.loads(args.candidates.read_text())
    result = from_integration(source) if args.from_integration else consume(source)
    args.output.write_text(json.dumps(result, sort_keys=True) + "\n")
    print(json.dumps({"status": result["status"], "watch_count": result["watch_count"], "receipt_sha256": result["receipt_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
