"""Fail-closed read-only consumer of persisted A2 paper candidate snapshots."""
import argparse
import datetime as dt
import hashlib
import json
import math
from pathlib import Path

from .scanner import STABLE

def read_snapshot(latest_path, now=None, max_age_seconds=600):
    latest = Path(latest_path)
    if latest.is_symlink() or not latest.is_file():
        raise ValueError("missing or linked latest snapshot")
    raw = latest.read_bytes()
    report = json.loads(raw)
    if not isinstance(report, dict):
        raise ValueError("invalid snapshot object")
    stamp = dt.datetime.fromisoformat(report["as_of"].replace("Z", "+00:00"))
    if stamp.tzinfo is None or stamp.utcoffset() is None:
        raise ValueError("naive scan timestamp")
    now = now if now is not None else dt.datetime.now(dt.timezone.utc)
    if now.tzinfo is None or now.utcoffset() is None:
        raise ValueError("naive verification clock")
    if not isinstance(max_age_seconds, (int, float)) or isinstance(max_age_seconds, bool) or not math.isfinite(max_age_seconds) or max_age_seconds <= 0 or max_age_seconds > 600:
        raise ValueError("invalid maximum quote age")
    age = (now - stamp).total_seconds()
    if not 0 <= age <= max_age_seconds:
        raise ValueError("stale or future paper snapshot")
    receipt = latest.parent / "receipts" / (stamp.astimezone(dt.timezone.utc).strftime("%Y%m%dT%H%M%S%fZ") + ".json")
    if receipt.parent.is_symlink() or receipt.is_symlink() or not receipt.is_file() or receipt.read_bytes() != raw:
        raise ValueError("missing or mismatched immutable receipt")
    if report.get("mode") != "PAPER_ONLY" or report.get("buy_approved") is not False:
        raise ValueError("non-paper report")
    watch = report.get("watch")
    if not isinstance(watch, list) or len(watch) > 12:
        raise ValueError("invalid watch collection")
    if watch and report.get("scan_status") != "WATCH":
        raise ValueError("scan status disagrees with candidates")
    if not watch and report.get("scan_status") not in {"ABSTAIN_NO_LIQUID_CANDIDATES", "ABSTAIN_NO_QUALIFIED_OHLC", "ABSTAIN_INCOMPLETE_TICKER_COVERAGE"}:
        raise ValueError("invalid abstention status")
    if report.get("scan_status") == "ABSTAIN_INCOMPLETE_TICKER_COVERAGE":
        if report.get("ticker_coverage_complete") is not False:
            raise ValueError("incomplete coverage abstention missing source evidence")
        rejections = report.get("ticker_rejections")
        if (not isinstance(rejections, dict) or not rejections or 
                any(type(v) is not int or v < 0 for v in rejections.values()) or 
                sum(rejections.values()) <= 0):
            raise ValueError("incomplete coverage abstention without missing ticker evidence")
    elif report.get("ticker_coverage_complete") is False:
        raise ValueError("incomplete ticker coverage cannot authorize WATCH")
    for field in ("eligible_pairs", "observed_markets"):
        value = report.get(field)
        if type(value) is not int or value < 0:
            raise ValueError("invalid coverage count: " + field)
    if report["observed_markets"] > report["eligible_pairs"]:
        raise ValueError("observed coverage exceeds eligible markets")
    # A sealed receipt must not claim complete source coverage while its own
    # per-category Kraken rejection accounting proves otherwise. Older local
    # fixture receipts without these fields retain their historical contract.
    if "ticker_rejections" in report or "ticker_coverage_complete" in report:
        rejections = report.get("ticker_rejections")
        complete = report.get("ticker_coverage_complete")
        if (not isinstance(rejections, dict) or
                not rejections or not set(rejections).issubset({
                    "missing_or_invalid_payload", "invalid_price_or_volume",
                    "nonfinite_derived_metric"}) or
                any(type(v) is not int or v < 0 for v in rejections.values()) or
                type(complete) is not bool or
                report["observed_markets"] + sum(rejections.values()) != report["eligible_pairs"] or
                complete != (sum(rejections.values()) == 0)):
            raise ValueError("contradictory ticker source coverage")
        if not complete and (watch or report.get("scan_status") != "ABSTAIN_INCOMPLETE_TICKER_COVERAGE"):
            raise ValueError("incomplete ticker coverage cannot authorize WATCH")
    abstentions = report.get("abstention_counts")
    if not isinstance(abstentions, dict) or any(not isinstance(k, str) or not k or type(v) is not int or v < 0 for k, v in abstentions.items()):
        raise ValueError("invalid abstention counts")
    if len(watch) > report["observed_markets"]:
        raise ValueError("watch exceeds observed markets")
    # Preserve deterministic challenger ranking in the sealed WATCH handoff.
    if any(not isinstance(c, dict) for c in watch):
        raise ValueError("invalid paper candidate contract")
    seen = set()
    seen_symbols = set()
    previous_sort_key = None
    for rank, candidate in enumerate(watch, 1):
        if type(candidate.get("rank")) is not int or candidate["rank"] != rank or candidate.get("status") != "PAPER_WATCH" or candidate.get("buy_approved") is not False:
            raise ValueError("invalid paper candidate contract")
        pair = candidate.get("pair")
        if not isinstance(pair, str) or not pair or pair in seen:
            raise ValueError("duplicate or invalid pair")
        seen.add(pair)
        # Recheck the Kraken online /USD market contract at sealed readback.
        # An alternate quote or extra separator cannot bypass stablecoin gates.
        symbol = candidate.get("symbol")
        if (not isinstance(symbol, str) or len(symbol) > 64
                or symbol.count("/") != 1 or not symbol.endswith("/USD")
                or not symbol.split("/")[0]
                or any(ch.isspace() or ord(ch) < 33 for ch in symbol)):
            raise ValueError("invalid WATCH display symbol")
        if symbol.split("/")[0].upper() in STABLE:
            raise ValueError("stablecoin WATCH candidate prohibited")
        if symbol in seen_symbols:
            raise ValueError("duplicate WATCH display symbol")
        seen_symbols.add(symbol)
        if candidate.get("as_of") != report["as_of"] or candidate.get("prediction_id") != hashlib.sha256(("paper-v1|" + report["as_of"] + "|" + pair).encode()).hexdigest():
            raise ValueError("candidate provenance mismatch")
        if candidate.get("quote_timestamp_semantics") != "client_observed_not_exchange_event_time":
            raise ValueError("unverified quote timestamp semantics")
        quote = dt.datetime.fromisoformat(candidate["quote_observed_at"].replace("Z", "+00:00"))
        if quote.tzinfo is None or quote.utcoffset() is None or not 0 <= (stamp - quote).total_seconds() <= 600:
            raise ValueError("stale candidate quote")
        # A fresh ticker cannot make stale completed OHLC momentum valid.
        closed_at_raw = candidate.get("ohlc_last_closed_at")
        if not isinstance(closed_at_raw, str):
            raise ValueError("missing completed OHLC provenance")
        closed_at = dt.datetime.fromisoformat(closed_at_raw.replace("Z", "+00:00"))
        if closed_at.tzinfo is None or closed_at.utcoffset() is None or not 0 <= (stamp - closed_at).total_seconds() <= 600:
            raise ValueError("stale completed OHLC evidence")
        if not 0 <= (now - closed_at).total_seconds() <= max_age_seconds:
            raise ValueError("expired completed OHLC at read time")
        # Scan freshness alone is insufficient: a quote may be 9m old at scan
        # time and 9m old again when read. Enforce the actual read-time age.
        quote_age = (now - quote).total_seconds()
        if not 0 <= quote_age <= max_age_seconds:
            raise ValueError("expired candidate quote at read time")
        for field in ("price", "move15_pct", "volume_accel", "baseline_score", "challenger_score", "spread_bps"):
            value = candidate.get(field)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                raise ValueError("invalid numeric candidate field: " + field)
        if candidate["price"] <= 0 or candidate["volume_accel"] <= 0 or candidate["spread_bps"] < 0:
            raise ValueError("invalid candidate market metrics")
        sort_key = (-candidate["challenger_score"], pair)
        if previous_sort_key is not None and sort_key < previous_sort_key:
            raise ValueError("WATCH challenger ranking mismatch")
        previous_sort_key = sort_key
        if (candidate.get("momentum_reference") != "completed_5m_candles_15m" or
                candidate.get("volume_acceleration_reference") != "last_30m_over_prior_30m"):
            raise ValueError("missing WATCH metric provenance")
        expected_risk = ("HIGH" if candidate["spread_bps"] > 30 or
                         candidate["volume_accel"] < 0.8 or abs(candidate["move15_pct"]) > 8
                         else "ELEVATED")
        if candidate.get("risk") != expected_risk:
            raise ValueError("invalid WATCH risk classification")
    # A current scanner receipt carries the full ticker inventory and the
    # selected-market decision ledger. The WATCH projection must agree with
    # that source evidence, not merely be internally well-formed. Historical
    # fixture receipts without either ledger retain their older contract.
    observations = report.get("observations")
    preselection = report.get("preselection_universe")
    if preselection is not None:
        if not isinstance(observations, list) or not isinstance(preselection, list):
            raise ValueError("incomplete WATCH source inventory")
        if len(observations) != report["observed_markets"] or len(preselection) != len(observations):
            raise ValueError("WATCH source inventory coverage mismatch")
        observed_by_pair = {}
        for row in observations:
            if not isinstance(row, dict) or not isinstance(row.get("pair"), str) or row["pair"] in observed_by_pair:
                raise ValueError("duplicate or invalid source observation")
            # Every frozen observation is used by E's point-in-time learner,
            # not only the ranked WATCH subset. Reject future/stale/nonpositive
            # source quotes before exporting a receipt-bound historical cohort.
            source_time = row.get("observed_at")
            if (row.get("source") != "kraken_public_ticker_client_observed" or
                    not isinstance(source_time, str) or
                    type(row.get("price")) not in (int, float) or
                    not math.isfinite(row["price"]) or row["price"] <= 0):
                raise ValueError("invalid source observation provenance")
            try:
                source_stamp = dt.datetime.fromisoformat(source_time.replace("Z", "+00:00"))
            except ValueError as exc:
                raise ValueError("invalid source observation timestamp") from exc
            if (source_stamp.tzinfo is None or source_stamp.utcoffset() is None or
                    not 0 <= (stamp - source_stamp).total_seconds() <= 600):
                raise ValueError("stale or future source observation")
            observed_by_pair[row["pair"]] = row
        selection_by_pair = {}
        for row in preselection:
            if not isinstance(row, dict) or not isinstance(row.get("pair"), str) or row["pair"] in selection_by_pair:
                raise ValueError("duplicate or invalid preselection source")
            selection_by_pair[row["pair"]] = row
        if set(observed_by_pair) != set(selection_by_pair):
            raise ValueError("WATCH source inventory identity mismatch")
        watch_by_pair = {c["pair"]: c for c in watch}
        for pair, row in selection_by_pair.items():
            observed = observed_by_pair[pair]
            if (row.get("symbol") != observed.get("symbol") or
                    row.get("price") != observed.get("price") or
                    row.get("quote_observed_at") != observed.get("observed_at")):
                raise ValueError("preselection quote contradicts observed source")
            if row.get("selection_status") == "WATCH":
                candidate = watch_by_pair.get(pair)
                if (candidate is None or row.get("screen_passed") is not True or
                        row.get("watch_rank") != candidate["rank"] or
                        row.get("baseline_score") != candidate["baseline_score"]):
                    raise ValueError("WATCH source selection contradiction")
            elif pair in watch_by_pair:
                raise ValueError("WATCH candidate not authorized by selection ledger")
        for candidate in watch:
            observed = observed_by_pair.get(candidate["pair"])
            if (observed is None or candidate["symbol"] != observed.get("symbol") or
                    candidate["price"] != observed.get("price") or
                    candidate["quote_observed_at"] != observed.get("observed_at")):
                raise ValueError("WATCH candidate contradicts source quote")
    if latest.is_symlink() or latest.read_bytes() != raw:
        raise ValueError("snapshot changed during verification")
    return {"as_of": report["as_of"], "scan_status": report["scan_status"],
            "eligible_pairs": report.get("eligible_pairs"), "observed_markets": report.get("observed_markets"),
            "abstention_counts": report.get("abstention_counts", {}), "watch": watch,
            "receipt_sha256": hashlib.sha256(raw).hexdigest(), "snapshot_age_seconds": round(age, 3),
            "quote_age_seconds": {c["pair"]: round((now - dt.datetime.fromisoformat(c["quote_observed_at"].replace("Z", "+00:00"))).total_seconds(), 3) for c in watch}}

def main():
    parser = argparse.ArgumentParser(description="Verify and emit immutable A2 paper candidate snapshot")
    parser.add_argument("latest", help="path to scanner latest.json")
    args = parser.parse_args()
    print(json.dumps(read_snapshot(args.latest), sort_keys=True, allow_nan=False))

if __name__ == "__main__":
    main()
