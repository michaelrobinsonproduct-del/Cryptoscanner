"""Read-only delivery adapter for authenticated GitHub paper-run transport.

The transport verifies GitHub run metadata and file checksums; that alone
never authorizes live WATCH delivery. No ledger writes or scanner dispatches.
"""
import argparse
import json
from .github_sealed_bundle_readback import read_run


def _writer_evidence(readback):
    """Project D's already-verified recovery report without equating scan cohorts."""
    if not isinstance(readback, dict) or readback.get("status") not in ("WRITER_CHECKSUM_ONLY", "VERIFIED_REMOTE_READBACK"):
        raise ValueError("writer recovery did not succeed")
    if (readback.get("remote_downloaded") is not True or
            readback.get("ledger_writer_invoked") is not False or
            readback.get("production_applied") is not False):
        raise ValueError("writer readback is not read-only")
    independent = readback.get("independently_authenticated")
    if independent is not (readback["status"] == "VERIFIED_REMOTE_READBACK"):
        raise ValueError("writer authentication claim inconsistent")
    run_id, sha = readback.get("run_id"), readback.get("source_sha")
    if not isinstance(run_id, str) or not run_id.isdigit() or int(run_id) <= 0 or not isinstance(sha, str) or len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha.lower()):
        raise ValueError("writer source identity invalid")
    persisted = readback.get("persisted_paper")
    if not isinstance(persisted, dict) or type(persisted.get("ledger_generation")) is not int or persisted["ledger_generation"] < 0 or not isinstance(persisted.get("scan_status"), str) or not persisted["scan_status"] or persisted.get("live_replay_performed") is not False:
        raise ValueError("writer persisted evidence invalid")
    reconciliation = readback.get("remote_ledger_reconciliation")
    status = "UNAVAILABLE"
    if reconciliation is not None:
        if (not isinstance(reconciliation, dict) or reconciliation.get("status") not in ("MATCH", "DIVERGED", "UNAVAILABLE") or reconciliation.get("independently_authenticated") is not False or reconciliation.get("production_applied") is not False):
            raise ValueError("writer reconciliation invalid")
        status = reconciliation["status"]
        if status == "UNAVAILABLE" and reconciliation.get("reason") != "REMOTE_LEDGER_QUERY_FAILED":
            raise ValueError("unexplained remote ledger unavailability")
        if status in ("MATCH", "DIVERGED"):
            import re
            a, z = reconciliation.get("recovered_sha256"), reconciliation.get("remote_sha256")
            if not all(isinstance(d, str) and re.fullmatch(r"[0-9a-f]{64}", d) for d in (a, z)):
                raise ValueError("writer reconciliation digest missing")
            # D's canonical ledger identity can match despite different JSON bytes.
            ca = reconciliation.get("recovered_ledger_sha256", a)
            cz = reconciliation.get("remote_ledger_sha256", z)
            if not all(isinstance(d, str) and re.fullmatch(r"[0-9a-f]{64}", d) for d in (ca, cz)) or (ca == cz) != (status == "MATCH"):
                raise ValueError("writer reconciliation digest contradiction")
            rg = reconciliation.get("recovered_generation")
            mg = reconciliation.get("remote_generation")
            if rg is not None and rg != persisted["ledger_generation"]:
                raise ValueError("writer recovered generation mismatch")
            if mg is not None and (type(mg) is not int or mg < 0 or (status == "MATCH" and mg != persisted["ledger_generation"])):
                raise ValueError("writer remote generation contradiction")
    return {"source_run_id": int(run_id), "source_sha": sha,
            "recovery_status": readback["status"], "ledger_generation": persisted["ledger_generation"],
            "scan_status": persisted["scan_status"], "reconciliation_status": status,
            "independently_authenticated": independent, "same_scan_as_delivery": False,
            "live_watch_authorized": False, "production_applied": False}


def project_delivery(transport, writer_readback=None, historical_a2=None):
    if not isinstance(transport, dict):
        raise ValueError("invalid readback")
    run_id = transport.get("source_run_id")
    source_sha = transport.get("source_sha")
    if type(run_id) is not int or run_id <= 0 or not isinstance(source_sha, str) or len(source_sha) != 40 or any(c not in "0123456789abcdef" for c in source_sha.lower()):
        raise ValueError("invalid run provenance")
    if transport.get("watch_delivery_authorized") is not False or transport.get("publisher_authenticated") is not False:
        raise ValueError("unsupported WATCH authorization claim")
    if transport.get("sealed") is True:
        bundle = transport.get("bundle")
        if not isinstance(bundle, dict) or bundle.get("schema") != "paper_sealed_bundle_v1":
            raise ValueError("invalid sealed bundle")
        report = json.loads(bundle["receipt_json"])
        snapshot = bundle.get("candidate_snapshot")
        if not isinstance(report, dict) or not isinstance(snapshot, dict) or snapshot.get("watch") != report.get("watch"):
            raise ValueError("inconsistent candidate snapshot")
        historical_watch_count = len(report["watch"])
        status = "SEALED_HISTORICAL_READ_ONLY"
        coverage = {key: report.get(key) for key in ("eligible_pairs", "matched_tickers", "observed_markets", "ohlc_screened")}
    elif transport.get("sealed") is False and transport.get("artifact_status") == "CHECKSUM_VERIFIED_LEGACY_NO_RECEIPT":
        if not isinstance(transport.get("scoreboard"), dict):
            raise ValueError("invalid legacy scoreboard")
        historical_watch_count = None
        status = "LEGACY_CHECKSUM_ONLY"
        coverage = None
    else:
        raise ValueError("unsupported readback")
    writer = _writer_evidence(writer_readback) if writer_readback is not None else None
    replay = None
    if historical_a2 is not None:
        from .c_candidate_handoff import consume
        replay = consume(historical_a2)
        # Historical A2 is a different cohort, never an authorized live signal.
        replay = {"status": replay["status"], "receipt_sha256": replay["receipt_sha256"],
                  "watch_count": replay["watch_count"], "source_as_of": replay["source_as_of"],
                  "live_watch_certified": False}
    return {"schema": "paper_delivery_readback_v1", "source_run_id": run_id,
            "source_sha": source_sha, "status": status, "historical_watch_count": historical_watch_count,
            "historical_coverage": coverage, "live_watch": [], "live_watch_authorized": False,
            "production_applied": False, "single_writer_read_only": True,
            "writer_recovery": writer, "writer_reconciliation_status": writer["reconciliation_status"] if writer else "UNAVAILABLE",
            "historical_a2": replay}


def _a2_evidence(delivery):
    """Carry A's independently receipt-verified client quote cohort, not writer output."""
    import re
    if not isinstance(delivery, dict) or delivery.get("schema") != "a2_published_watch_delivery_v1":
        raise ValueError("invalid A2 delivery evidence")
    if any(delivery.get(key) is not False for key in ("single_writer_ledger_verified", "exchange_event_freshness_verified", "production_applied", "buy_approved")):
        raise ValueError("A2 falsely claims writer, exchange freshness or production approval")
    if delivery.get("client_quote_freshness_verified") is not True or delivery.get("source") != "kraken_public_rest_client_observed":
        raise ValueError("A2 freshness/source evidence absent")
    digest = delivery.get("receipt_sha256")
    if not isinstance(digest, str) or re.fullmatch(r"[0-9a-f]{64}", digest) is None:
        raise ValueError("A2 receipt identity missing")
    watch = delivery.get("watch")
    count = delivery.get("watch_count")
    if not isinstance(watch, list) or type(count) is not int or count != len(watch) or count > 12:
        raise ValueError("A2 WATCH count mismatch")
    if delivery.get("scan_status") not in ("WATCH", "ABSTAIN_NO_LIQUID_CANDIDATES", "ABSTAIN_NO_QUALIFIED_OHLC"):
        raise ValueError("A2 scan status invalid")
    if (delivery["scan_status"] == "WATCH") != bool(watch):
        raise ValueError("A2 WATCH/status mismatch")
    eligible, observed = delivery.get("eligible_pairs"), delivery.get("observed_markets")
    if any(type(v) is not int or v < 0 for v in (eligible, observed)) or observed > eligible or count > observed:
        raise ValueError("A2 coverage mismatch")
    if any(not isinstance(c, dict) or type(c.get("rank")) is not int or c["rank"] != i or c.get("buy_approved") is not False for i, c in enumerate(watch, 1)):
        raise ValueError("A2 candidate ranking or approval invalid")
    return {"receipt_sha256": digest, "as_of": delivery.get("as_of"),
            "status": delivery["scan_status"], "watch_count": count, "watch": watch,
            "eligible_pairs": eligible, "observed_markets": observed,
            "same_scan_as_writer": False, "single_writer_ledger_verified": False,
            "exchange_event_freshness_verified": False, "production_applied": False}


def _learning_evidence(h):
    """E's unpromotable held-out evidence is separate from live scan scoring."""
    import re
    if not isinstance(h, dict) or h.get("schema") != "paper_learning_handoff_v1" or h.get("status") != "NO_QUALIFIED_RULE" or h.get("read_only") is not True:
        raise ValueError("invalid learning handoff")
    if any(h.get(k) is not False for k in ("source_authenticated", "measured_lift_verified", "live_watch_authorized", "promotion_authorized", "production_applied")):
        raise ValueError("unsafe learning authorization")
    if any(not isinstance(h.get(k), str) or not re.fullmatch(r"[0-9a-f]{64}", h[k]) for k in ("evidence_digest", "cohort_join_digest")):
        raise ValueError("missing learning digest")
    n = [h.get(k) for k in ("observed_prediction_count", "complete_cohort_count", "excluded_prediction_count")]
    if any(type(v) is not int or v < 0 for v in n) or n[0] != n[1] + n[2]:
        raise ValueError("inconsistent learning cohort counts")
    if not isinstance(h.get("abstention_counts"), dict) or not isinstance(h.get("incomplete_prediction_horizons"), dict) or len(h["incomplete_prediction_horizons"]) != n[2]:
        raise ValueError("missing learning abstentions")
    return {"schema": "paper_learning_delivery_v1", "status": "NO_QUALIFIED_RULE",
            "baseline_version": h["baseline_version"], "challenger_version": h["challenger_version"],
            "evaluation_asof_utc": h["evaluation_asof_utc"], "evidence_digest": h["evidence_digest"],
            "cohort_join_digest": h["cohort_join_digest"], "observed_prediction_count": n[0],
            "complete_cohort_count": n[1], "excluded_prediction_count": n[2],
            "abstention_counts": h["abstention_counts"], "source_authenticated": False,
            "measured_lift_verified": False, "promotion_authorized": False, "production_applied": False}


def project_published_result(result, writer_readback=None, a2_delivery=None, learning_handoff=None):
    """Consume the real results.json emitted by the ONE paper-pipeline writer.

    This is the same schema for scheduled and manual dispatch; it does not
    re-run Kraken, mutate the ledger, or infer exchange-event freshness.
    """
    import re
    if not isinstance(result, dict) or result.get("schema") != 1:
        raise ValueError("invalid published paper result")
    event = result.get("github_event")
    if event not in ("schedule", "workflow_dispatch"):
        raise ValueError("untrusted scan trigger")
    if event == "schedule":
        cron = result.get("originating_cron")
        if cron not in ("9 * * * *", "39 * * * *") or result.get("scheduled_slot_verified") is not True or result.get("scheduled_slot_utc_minute") != int(cron.split()[0]):
            raise ValueError("invalid scheduled provenance")
    elif result.get("originating_cron") is not None or result.get("scheduled_slot_verified") is not False or result.get("scheduled_slot_utc_minute") is not None:
        raise ValueError("manual result claims scheduled provenance")
    run_id, sha = result.get("run_id"), result.get("source_sha")
    if not isinstance(run_id, str) or not run_id.isdigit() or int(run_id) <= 0 or not isinstance(sha, str) or re.fullmatch(r"[0-9a-f]{40}", sha) is None:
        raise ValueError("invalid published source identity")
    if result.get("production_applied") is not False or result.get("buy_approved") is not False or result.get("exchange_event_freshness_verified") is not False:
        raise ValueError("unsupported production or freshness claim")
    if result.get("remote_readback_verified") is not True or re.fullmatch(r"[0-9a-f]{64}", str(result.get("ledger_sha256", ""))) is None or re.fullmatch(r"[0-9a-f]{40}", str(result.get("ledger_commit", ""))) is None:
        raise ValueError("missing single-writer readback evidence")
    generation = result.get("ledger_generation")
    if type(generation) is not int or generation < 1:
        raise ValueError("invalid published ledger generation")
    status = result.get("status")
    if status not in ("SUCCESS_PAPER_ONLY", "ABSTAIN_NO_WATCH", "ABSTAIN_NO_OBSERVATIONS"):
        raise ValueError("unsupported published scan status")
    candidates = result.get("candidates")
    if not isinstance(candidates, list) or (status == "SUCCESS_PAPER_ONLY") != bool(candidates) or len(candidates) > 12:
        raise ValueError("published WATCH/status inconsistency")
    if candidates:
        age = result.get("max_client_quote_age_seconds")
        if type(age) not in (int, float) or not 0 <= age <= 600:
            raise ValueError("WATCH quote freshness invalid")
    # Re-evaluate the actual quote observations instead of trusting a producer's
    # aggregate max-age flag. This is client-observed freshness, never exchange time.
    from .results_report import _utc, STABLE
    as_of = _utc(result.get("as_of"))
    quotes = result.get("quote_evidence")
    if not isinstance(quotes, list) or type(result.get("observed_markets")) is not int or len(quotes) != result["observed_markets"]:
        raise ValueError("published quote evidence missing or incomplete")
    by_symbol = {}
    ages = []
    for quote in quotes:
        if not isinstance(quote, dict):
            raise ValueError("malformed published quote evidence")
        symbol, pair = quote.get("symbol"), quote.get("pair")
        if not isinstance(symbol, str) or not symbol.endswith("/USD") or symbol.split("/")[0].upper() in STABLE or not isinstance(pair, str) or not pair or symbol in by_symbol:
            raise ValueError("invalid or excluded published quote")
        age = (as_of - _utc(quote.get("observed_at"))).total_seconds()
        price = quote.get("price")
        if not 0 <= age <= 600 or type(price) not in (int, float) or not 0 < price < float("inf"):
            raise ValueError("stale or invalid published quote")
        by_symbol[symbol] = quote
        ages.append(age)
    if result.get("max_client_quote_age_seconds") != (max(ages) if ages else None):
        raise ValueError("published quote freshness summary mismatch")
    if (status == "ABSTAIN_NO_OBSERVATIONS") != (not quotes) or (status == "ABSTAIN_NO_WATCH") != (bool(quotes) and not candidates):
        raise ValueError("published abstention/coverage contradiction")
    for i, candidate in enumerate(candidates, 1):
        if not isinstance(candidate, dict) or candidate.get("rank") != i or candidate.get("status") != "WATCH_PAPER_ONLY" or candidate.get("exchange_event_freshness_verified") is not False:
            raise ValueError("invalid WATCH candidate")
        for key in ("symbol", "price_usd", "quote_observed_at", "baseline_score", "challenger_score", "move15_pct", "volume_accel", "risk"):
            if key not in candidate:
                raise ValueError("incomplete WATCH candidate")
        quote = by_symbol.get(candidate["symbol"])
        if quote is None or candidate["price_usd"] != quote["price"] or _utc(candidate["quote_observed_at"]) != _utc(quote["observed_at"]):
            raise ValueError("WATCH candidate lacks matching fresh quote")
    writer = _writer_evidence(writer_readback) if writer_readback is not None else None
    a2 = _a2_evidence(a2_delivery) if a2_delivery is not None else None
    learning = _learning_evidence(learning_handoff) if learning_handoff is not None else None
    return {"schema": "paper_delivery_readback_v1", "source_run_id": int(run_id),
            "source_sha": sha, "github_event": event, "status": status,
            "ledger_generation": generation, "ledger_commit": result["ledger_commit"],
            "writer_reconciliation_status": writer["reconciliation_status"] if writer else "UNAVAILABLE",
            "writer_recovery": writer, "a2_receipt_cohort": a2, "learning": learning, "historical_watch_count": None, "historical_coverage": None,
            "live_watch": candidates, "live_watch_authorized": False,
            "client_quote_freshness_verified": bool(candidates),
            "exchange_event_freshness_verified": False,
            "single_writer_read_only": True, "production_applied": False}


def project_legacy_published_abstention(result, *, writer_readback=None, a2_delivery=None, learning_handoff=None):
    """Project genuine old published results into the SAME delivery schema.

    Missing quote observations cannot be reconstructed from aggregate age or
    historical A2 evidence. Preserve identities and abstain without a WATCH.
    """
    import re
    if not isinstance(result, dict) or result.get("schema") != 1:
        raise ValueError("invalid legacy published result")
    run_id, sha = result.get("run_id"), result.get("source_sha")
    if (type(run_id) not in (str, int) or not str(run_id).isdigit() or\n            not isinstance(sha, str) or re.fullmatch(r"[0-9a-f]{40}", sha) is None):
        raise ValueError("missing legacy run provenance")
    event = result.get("github_event")
    if event not in ("workflow_dispatch", "schedule") or result.get("remote_readback_verified") is not True:
        raise ValueError("unverified legacy event or writer")
    if result.get("production_applied") is not False or result.get("buy_approved") is not False or result.get("exchange_event_freshness_verified") is not False:
        raise ValueError("unsafe legacy authorization")
    if "quote_evidence" in result:
        raise ValueError("quote-complete results must use strict published projection")
    writer = _writer_evidence(writer_readback) if writer_readback is not None else None
    a2 = _a2_evidence(a2_delivery) if a2_delivery is not None else None
    learning = _learning_evidence(learning_handoff) if learning_handoff is not None else None
    return {"schema": "paper_delivery_readback_v1", "source_run_id": int(run_id),
            "source_sha": sha, "github_event": event,
            "status": "ABSTAIN_PUBLISHED_QUOTE_EVIDENCE_MISSING",
            "ledger_generation": result.get("ledger_generation"),
            "ledger_commit": result.get("ledger_commit"),
            "writer_reconciliation_status": writer["reconciliation_status"] if writer else "UNAVAILABLE",
            "writer_recovery": writer, "a2_receipt_cohort": a2, "learning": learning,
            "historical_watch_count": None, "historical_coverage": None,
            "live_watch": [], "live_watch_authorized": False,
            "client_quote_freshness_verified": False,
            "exchange_event_freshness_verified": False,
            "single_writer_read_only": True, "production_applied": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo")
    parser.add_argument("--run-id")
    parser.add_argument("--writer-readback", help="Existing D historical readback JSON")
    parser.add_argument("--historical-a2", help="Existing C/B historical WATCH handoff JSON")
    parser.add_argument("--output", help="Write read-only delivery JSON; never a ledger")
    parser.add_argument("--published-result", help="Actual verified paper-pipeline results.json")
    parser.add_argument("--published-artifact", help="Checksummed public-paper-results GitHub ZIP (read-only)")
    parser.add_argument("--expected-run-id", help="Expected immutable GitHub run identity")
    parser.add_argument("--expected-source-sha", help="Expected immutable GitHub source SHA")
    parser.add_argument("--a2-delivery", help="Complete A2 downloaded artifact directory (verified at read time), or legacy read-only JSON projection")
    parser.add_argument("--learning-handoff", help="E no-improvement learning handoff JSON")
    args = parser.parse_args()
    writer = json.loads(open(args.writer_readback, encoding="utf-8").read()) if args.writer_readback else None
    historical = json.loads(open(args.historical_a2, encoding="utf-8").read()) if args.historical_a2 else None
    if args.published_result and args.published_artifact:
        parser.error("select exactly one published input")
    if args.published_result or args.published_artifact:
        if args.run_id or args.repo or historical is not None:
            parser.error("--published-result is exclusive of historical artifact transport")
        a2 = None
        if args.a2_delivery:
            from pathlib import Path
            source = Path(args.a2_delivery)
            if source.is_dir():
                # A's complete downloaded Actions artifact, including immutable
                # receipt and preselection, is required for live-age evidence.
                from .a2_artifact_consumer import read_published_delivery
                a2 = read_published_delivery(source)
            else:
                # Legacy JSON handoffs are separate historical cohorts only;
                # they must never be represented as fresh A2 artifact readback.
                a2 = json.loads(source.read_text(encoding="utf-8"))
        learning = json.loads(open(args.learning_handoff, encoding="utf-8").read()) if args.learning_handoff else None
        if args.published_artifact:
            from .manual_schedule_contract import load_verified_artifact
            from pathlib import Path
            published = load_verified_artifact(Path(args.published_artifact))
        else:
            published = json.loads(open(args.published_result, encoding="utf-8").read())
        if args.published_artifact and (not args.expected_run_id or not args.expected_source_sha):
            parser.error("ZIP readback requires expected GitHub run ID and source SHA")
        if args.expected_run_id and str(published.get("run_id")) != args.expected_run_id:
            raise ValueError("published artifact run identity mismatch")
        if args.expected_source_sha and published.get("source_sha") != args.expected_source_sha:
            raise ValueError("published artifact source SHA mismatch")
        result = (project_legacy_published_abstention(published, writer_readback=writer, a2_delivery=a2, learning_handoff=learning)\n                  if "quote_evidence" not in published else project_published_result(published, writer, a2, learning))
    else:
        if args.a2_delivery or args.learning_handoff:
            parser.error("--a2-delivery and --learning-handoff require --published-result")
        if not args.repo or not args.run_id:
            parser.error("--repo and --run-id required for historical artifact transport")
        result = project_delivery(read_run(args.repo, args.run_id), writer, historical)
    rendered = json.dumps(result, sort_keys=True, allow_nan=False) + "\n"
    if args.output:
        from pathlib import Path
        target = Path(args.output)
        if target.exists():
            raise FileExistsError("refusing to overwrite delivery result")
        target.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
