"""Read-only independent audit of paired downloaded GitHub paper artifacts."""
import argparse
import json
from datetime import datetime
from pathlib import Path
from .replay_downloaded_artifacts import read_archive, verify_checksums, LEDGER_FILES, RESULT_FILES


def audit(ledger_zip, results_zip):
    ledger = read_archive(ledger_zip, LEDGER_FILES)
    results = read_archive(results_zip, RESULT_FILES)
    verify_checksums(ledger, LEDGER_FILES - {"SHA256SUMS"})
    verify_checksums(results, RESULT_FILES - {"SHA256SUMS"})
    scan = json.loads(ledger["latest.json"])
    board = json.loads(ledger["scoreboard.json"])
    state = json.loads(ledger["ledger.json"])
    report = json.loads(results["results.json"])
    if (board["ledger_sha256"] != report["ledger_sha256"]
            or board["generation"] != report["ledger_generation"]
            or state["sha256"] != board["ledger_sha256"]
            or state["generation"] != board["generation"]):
        raise ValueError("Ledger identities disagree")
    if report["eligible_pairs"] != scan["eligible_pairs"] or report["observed_markets"] != len(scan["observations"]):
        raise ValueError("Scan coverage differs from publication")
    if len(report["candidates"]) != len(scan["watch"]):
        raise ValueError("WATCH count differs")
    as_of = datetime.fromisoformat(scan["as_of"])
    quotes = scan["observations"]
    ages = [(as_of - datetime.fromisoformat(q["observed_at"])).total_seconds() for q in quotes]
    if any(not 0 <= age <= 600 for age in ages):
        raise ValueError("Stale or future retained quote")
    by_symbol = {q["symbol"]: q for q in quotes}
    if len(by_symbol) != len(quotes):
        raise ValueError("Duplicate quote symbol")
    for candidate in report["candidates"]:
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
    return {"run_id": report["run_id"], "generation": board["generation"],
            "observed": len(quotes), "watch": len(report["candidates"]),
            "max_client_quote_age_seconds": max(ages) if ages else None,
            "published_quote_evidence": published is not None,
            "exchange_event_freshness_verified": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger-zip", required=True)
    parser.add_argument("--results-zip", required=True)
    args = parser.parse_args()
    print(json.dumps(audit(Path(args.ledger_zip), Path(args.results_zip)), sort_keys=True))


if __name__ == "__main__":
    main()
