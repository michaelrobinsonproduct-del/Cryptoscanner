"""Consume an actual published A2 receipt artifact as historical E evidence.

No future bars are inferred from a current A2 snapshot. All 1/6/24/48h
outcomes abstain until independently pinned trade partitions are supplied.
"""
import argparse
import datetime as dt
import hashlib
import json
import tempfile
import zipfile
from pathlib import Path

from .preselection_universe import export_receipt_history
from .historical_preselection_binding import bind_preselection_history



def _legacy_research_history(receipt):
    """Freeze a pre-coverage-contract receipt for research, never live WATCH."""
    report = json.loads(receipt)
    if not isinstance(report, dict) or report.get("mode") != "PAPER_ONLY" or report.get("buy_approved") is not False:
        raise ValueError("Not a sealed paper research receipt")
    if "ticker_coverage_complete" in report:
        raise ValueError("Current receipts must use the strict A/B reader")
    rejects = report.get("ticker_rejections")
    eligible, observed = report.get("eligible_pairs"), report.get("observed_markets")
    if (not isinstance(rejects, dict) or not rejects or
            any(type(n) is not int or n < 0 for n in rejects.values()) or
            type(eligible) is not int or type(observed) is not int or
            observed + sum(rejects.values()) != eligible):
        raise ValueError("Legacy ticker accounting is not independently consistent")
    rows = report.get("preselection_universe")
    coverage = report.get("preselection_coverage")
    decisions = report.get("preselection_decisions")
    if (not isinstance(rows, list) or len(rows) != observed or
            not isinstance(coverage, dict) or coverage.get("valid_tickers") != observed or
            not isinstance(decisions, dict) or sum(decisions.values()) != observed):
        raise ValueError("Incomplete frozen legacy universe")
    allowed = {"SCREEN_REJECTED", "NOT_OHLC_SELECTED", "OHLC_ABSTAINED",
               "NOT_RANKED_WATCH", "WATCH"}
    if set(decisions) - allowed or any(
            not isinstance(row, dict) or row.get("selection_status") not in allowed or
            not isinstance(row.get("pair"), str) or not row["pair"]
            for row in rows):
        raise ValueError("Invalid frozen legacy decisions")
    if len({row["pair"] for row in rows}) != observed or any(
            sum(row["selection_status"] == status for row in rows) != count
            for status, count in decisions.items()):
        raise ValueError("Legacy selection accounting mismatch")
    if report.get("scan_status") != "WATCH" or len(report.get("watch", [])) != decisions.get("WATCH", 0):
        raise ValueError("Legacy WATCH accounting mismatch")
    as_of = report.get("as_of")
    if not isinstance(as_of, str):
        raise ValueError("Missing legacy UTC observation time")
    stamp = dt.datetime.fromisoformat(as_of.replace("Z", "+00:00"))
    if stamp.tzinfo is None or stamp.utcoffset() != dt.timedelta(0):
        raise ValueError("Legacy observation time must be UTC")
    digest = hashlib.sha256(receipt).hexdigest()
    markets = []
    for row in rows:
        item = dict(row)
        item["observation_id"] = hashlib.sha256(
            ("paper-preselection-v1|" + digest + "|" + row["pair"]).encode()).hexdigest()
        markets.append(item)
    # Incomplete ticker coverage makes every legacy WATCH non-actionable.
    # Preserve its historical decision for research only.
    snapshot = {"schema": "paper_preselection_v1", "snapshot_use": "HISTORICAL_RESEARCH_ONLY",
                "receipt_sha256": digest, "as_of": as_of, "markets": markets,
                "coverage": coverage, "selection_decisions": decisions,
                "legacy_incomplete_ticker_coverage": True}
    return {"schema": "paper_preselection_history_v1",
            "snapshot_use": "HISTORICAL_RESEARCH_ONLY",
            "future_outcomes_authenticated": False, "qualified_for_learning": False,
            "live_watch_eligible": False, "production_applied": False,
            "receipt_count": 1, "market_observation_count": observed,
            "snapshots": [snapshot]}


def project_a2_historical_artifact(archive):
    archive = Path(archive)
    if archive.is_symlink() or not archive.is_file() or archive.stat().st_size > 8_000_000:
        raise ValueError("Missing or unsafe downloaded A2 archive")
    with zipfile.ZipFile(archive) as z:
        infos = z.infolist()
        receipts = [i for i in infos if i.filename.startswith("receipts/") and i.filename.endswith(".json")]
        if len(receipts) != 1 or len(infos) > 30 or len({i.filename for i in infos}) != len(infos):
            raise ValueError("Unexpected A2 archive membership")
        if any(i.file_size > 2_000_000 or i.filename.startswith("/") or ".." in Path(i.filename).parts
               or (i.external_attr >> 16) & 0o170000 == 0o120000 for i in infos):
            raise ValueError("Unsafe A2 artifact member")
        receipt = z.read(receipts[0])
        if "latest.json" not in z.namelist() or z.read("latest.json") != receipt:
            raise ValueError("A2 immutable receipt mismatch")
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "receipts").mkdir()
        (root / receipts[0].filename).write_bytes(receipt)
        try:
            history = export_receipt_history(root / "receipts")
        except ValueError:
            # Only the legacy missing-coverage-field contract is eligible.
            # Current malformed receipts still fail in the strict reader.
            if "ticker_coverage_complete" in json.loads(receipt):
                raise
            history = _legacy_research_history(receipt)
    watch = []
    for snapshot in history["snapshots"]:
        for market in snapshot["markets"]:
            if market["selection_status"] == "WATCH":
                watch.append({"prediction_id": market["observation_id"],
                              "pair": market["pair"], "as_of": snapshot["as_of"],
                              "status": "PAPER_WATCH"})
    binding = bind_preselection_history(history, watch)
    # Preserve point-in-time decisions for every A candidate, not just WATCH.
    observations = []
    for snapshot in history["snapshots"]:
        as_of = snapshot["as_of"]
        when = dt.datetime.fromisoformat(as_of.replace("Z", "+00:00"))
        if when.tzinfo is None or when.utcoffset() != dt.timedelta(0):
            raise ValueError("A2 observation timestamp must be UTC")
        for market in snapshot["markets"]:
            observations.append({"prediction_id": market["observation_id"],
                                 "pair": market["pair"], "as_of": as_of,
                                 "selection_status": market["selection_status"]})
    observations.sort(key=lambda row: (row["as_of"], row["prediction_id"]))
    if len(observations) != binding["preselection_observation_count"]:
        raise ValueError("A2 full-universe observation coverage mismatch")
    return {"schema": "a2_historical_e_preselection_v1",
            "a_receipt_sha256": history["snapshots"][0]["receipt_sha256"],
            "as_of": history["snapshots"][0]["as_of"],
            "frozen_observation_count": binding["preselection_observation_count"],
            "watch_count": binding["watch_outcome_input_count"],
            "nonwatch_without_outcomes": binding["unobserved_nonwatch_count"],
            "frozen_predictions": binding["frozen_predictions"],
            "frozen_observations": observations,
            "e1_watch_predictions": binding["e1_watch_predictions"],
            "source_authenticated": False,
            "legacy_incomplete_ticker_coverage": bool(history["snapshots"][0].get("legacy_incomplete_ticker_coverage")),
            "legacy_watch_authorized": False,
            "historical_outcomes_available": False,
            "status": "NO_QUALIFIED_RULE",
            "promotion_authorized": False, "production_applied": False}


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--a2-artifact", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args(argv)
    out = Path(args.output)
    if out.exists():
        raise FileExistsError("Refusing to overwrite A2 historical projection")
    result = project_a2_historical_artifact(args.a2_artifact)
    out.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("a_receipt_sha256", "frozen_observation_count",
                                            "watch_count", "nonwatch_without_outcomes", "status")}, sort_keys=True))


if __name__ == "__main__":
    main()
