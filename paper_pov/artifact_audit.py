"""Read-only independent audit of paired downloaded GitHub paper artifacts."""
import argparse
import json
from datetime import datetime
from pathlib import Path
from .replay_downloaded_artifacts import read_archive, verify_checksums, LEDGER_FILES, RESULT_FILES


def audit(ledger_zip, results_zip, *, run_id, source_sha, ledger_commit):
    ledger = read_archive(ledger_zip, LEDGER_FILES)
    results = read_archive(results_zip, RESULT_FILES)
    verify_checksums(ledger, LEDGER_FILES - {"SHA256SUMS"})
    verify_checksums(results, RESULT_FILES - {"SHA256SUMS"})
    scan = json.loads(ledger["latest.json"])
    board = json.loads(ledger["scoreboard.json"])
    state = json.loads(ledger["ledger.json"])
    report = json.loads(results["results.json"])
    if (str(report.get("run_id")) != str(run_id) or report.get("source_sha") != source_sha
            or report.get("ledger_commit") != ledger_commit):
        raise ValueError("Downloaded artifact run/source/remote identity mismatch")
    if (board["ledger_sha256"] != report["ledger_sha256"]
            or board["generation"] != report["ledger_generation"]
            or state["sha256"] != board["ledger_sha256"]
            or state["generation"] != board["generation"]):
        raise ValueError("Ledger identities disagree")
    if report["eligible_pairs"] != scan["eligible_pairs"] or report["observed_markets"] != len(scan["observations"]):
        raise ValueError("Scan coverage differs from publication")
    if not isinstance(report.get("candidates"), list) or not isinstance(scan.get("watch"), list):
        raise ValueError("Missing WATCH arrays")
    if len(report["candidates"]) != len(scan["watch"]):
        raise ValueError("WATCH count differs")
    if not isinstance(scan.get("observations"), list):
        raise ValueError("Missing retained observations")
    as_of = datetime.fromisoformat(scan["as_of"])
    quotes = scan["observations"]
    ages = [(as_of - datetime.fromisoformat(q["observed_at"])).total_seconds() for q in quotes]
    if any(not 0 <= age <= 600 for age in ages):
        raise ValueError("Stale or future retained quote")
    by_symbol = {q["symbol"]: q for q in quotes}
    if len(by_symbol) != len(quotes):
        raise ValueError("Duplicate quote symbol")
    watch_symbols = [item["symbol"] for item in scan["watch"]]
    reported_symbols = [item["symbol"] for item in report["candidates"]]
    if len(set(watch_symbols)) != len(watch_symbols) or reported_symbols != watch_symbols:
        raise ValueError("Published WATCH membership/order differs from retained scan")
    retained = {q["symbol"]: q for q in scan["watch"]}
    if len(retained) != len(scan["watch"]):
        raise ValueError("Duplicate retained WATCH identity")
    for rank, candidate in enumerate(report["candidates"], 1):
        if (candidate.get("rank") != rank or candidate.get("status") != "WATCH_PAPER_ONLY"
                or candidate.get("symbol") not in retained):
            raise ValueError("Published WATCH identity/rank/status mismatch")
        quote = by_symbol.get(candidate["symbol"])
        if quote is None or candidate["price_usd"] != quote["price"] or candidate["quote_observed_at"] != quote["observed_at"]:
            raise ValueError("Published WATCH lacks retained quote")
    if report.get("buy_approved") is not False or report.get("production_applied") is not False:
        raise ValueError("Unexpected trading authorization")
    published = report.get("quote_evidence")
    if published is not None:
        expected = [{k: q[k] for k in ("pair", "symbol", "observed_at", "price")} for q in quotes]
        if published != expected:
            raise ValueError("Published quote evidence differs")
    return {"status": "VERIFIED" if published is not None else "ABSTAIN_LEGACY_QUOTE_EVIDENCE",
            "client_quote_evidence_verified": published is not None,
            "certified": published is not None,
            "run_id": report["run_id"], "generation": board["generation"],
            "observed": len(quotes), "watch": len(report["candidates"]),
            "max_client_quote_age_seconds": max(ages) if ages else None,
            "published_quote_evidence": published is not None,
            "exchange_event_freshness_verified": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger-zip", required=True)
    parser.add_argument("--results-zip", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--ledger-commit", required=True)
    args = parser.parse_args()
    print(json.dumps(audit(Path(args.ledger_zip), Path(args.results_zip), run_id=args.run_id,
                          source_sha=args.source_sha, ledger_commit=args.ledger_commit), sort_keys=True))


if __name__ == "__main__":
    main()
