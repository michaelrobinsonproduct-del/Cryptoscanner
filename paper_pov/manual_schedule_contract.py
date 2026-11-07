"""Read-only manual/scheduled paper result contract acceptance.

Compares schema and provenance, NOT candidate equality across different market times.
Never dispatches, fetches, writes ledger, or asserts live Kraken freshness.
"""
import argparse
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path

SHA40 = re.compile(r"[0-9a-f]{40}\Z")
SHA64 = re.compile(r"[0-9a-f]{64}\Z")
CANDIDATE_KEYS = frozenset(("rank", "symbol", "price_usd", "status", "confidence",
    "risk", "move_since_utc_open_pct", "move15_pct", "volume_accel", "spread_bps",
    "baseline_score", "challenger_score", "quote_observed_at", "ohlc_age_seconds",
    "prediction_id", "quote_source", "client_quote_age_seconds",
    "exchange_event_freshness_verified"))


def inspect(manual, scheduled):
    """Fail closed unless both published results have compatible, sealed paper contracts."""
    if not isinstance(manual, dict) or not isinstance(scheduled, dict):
        raise ValueError("Both result artifacts must be JSON objects")
    if manual.get("github_event") != "workflow_dispatch" or scheduled.get("github_event") != "schedule":
        raise ValueError("Expected distinct authenticated manual and scheduled events")
    if manual.get("originating_cron") is not None or manual.get("scheduled_slot_verified") is not False:
        raise ValueError("Manual result spoofed a scheduled slot")
    cron = scheduled.get("originating_cron")
    if cron not in ("10 * * * *", "40 * * * *") or scheduled.get("scheduled_slot_verified") is not True:
        raise ValueError("Unverified scheduled slot")
    if scheduled.get("scheduled_slot_utc_minute") != int(cron.split()[0]):
        raise ValueError("Scheduled cron minute mismatch")
    if manual.get("scheduled_slot_utc_minute") is not None:
        raise ValueError("Manual result has a scheduled minute")
    for label, payload in (("manual", manual), ("scheduled", scheduled)):
        if payload.get("schema") != 1 or payload.get("status") not in ("SUCCESS_PAPER_ONLY", "ABSTAIN_NO_WATCH", "ABSTAIN_NO_OBSERVATIONS"):
            raise ValueError(label + " has incompatible result schema/status")
        if payload.get("production_applied") is not False or payload.get("buy_approved") is not False:
            raise ValueError(label + " violates paper-only safety")
        if payload.get("remote_readback_verified") is not True:
            raise ValueError(label + " lacks ledger readback")
        if not isinstance(payload.get("run_id"), str) or not payload["run_id"].isdigit():
            raise ValueError(label + " lacks run provenance")
        if not SHA40.fullmatch(str(payload.get("source_sha", ""))) or not SHA40.fullmatch(str(payload.get("ledger_commit", ""))):
            raise ValueError(label + " lacks immutable SHA provenance")
        if not SHA64.fullmatch(str(payload.get("ledger_sha256", ""))):
            raise ValueError(label + " lacks ledger checksum")
        if type(payload.get("ledger_generation")) is not int or payload["ledger_generation"] < 1:
            raise ValueError(label + " lacks ledger generation")
        if payload.get("max_client_quote_age_seconds") is not None:
            if type(payload["max_client_quote_age_seconds"]) not in (int, float) or not 0 <= payload["max_client_quote_age_seconds"] <= 600:
                raise ValueError(label + " has stale/invalid client quote evidence")
        elif payload["status"] != "ABSTAIN_NO_OBSERVATIONS":
            raise ValueError(label + " lacks quote freshness evidence")
        if payload.get("exchange_event_freshness_verified") is not False:
            raise ValueError(label + " overclaims exchange event freshness")
        candidates = payload.get("candidates")
        if not isinstance(candidates, list) or len(candidates) > 12 or (payload["status"] == "SUCCESS_PAPER_ONLY") != bool(candidates):
            raise ValueError(label + " WATCH/status mismatch")
        if payload["status"] == "ABSTAIN_NO_OBSERVATIONS" and payload.get("observed_markets") != 0:
            raise ValueError(label + " zero-observation abstention contradicts coverage")
        if payload["status"] == "ABSTAIN_NO_WATCH" and (type(payload.get("observed_markets")) is not int or payload["observed_markets"] <= 0):
            raise ValueError(label + " no-WATCH abstention lacks observations")
        for i, candidate in enumerate(candidates, 1):
            if not isinstance(candidate, dict) or frozenset(candidate) != CANDIDATE_KEYS:
                raise ValueError(label + " candidate schema mismatch")
            if candidate["rank"] != i or candidate["status"] != "WATCH_PAPER_ONLY":
                raise ValueError(label + " candidate rank/status mismatch")
    if frozenset(manual) != frozenset(scheduled):
        raise ValueError("Manual/scheduled result schema differs")
    return {"status": "FIXTURE_OR_ARTIFACT_CONTRACT_VERIFIED_NOT_LIVE_PARITY",
            "manual_run": manual["run_id"], "scheduled_run": scheduled["run_id"],
            "manual_watch_count": len(manual["candidates"]),
            "scheduled_watch_count": len(scheduled["candidates"]),
            "manual_generation": manual["ledger_generation"],
            "scheduled_generation": scheduled["ledger_generation"],
            "same_source_sha": manual["source_sha"] == scheduled["source_sha"],
            "candidate_schema_parity": True, "market_time_candidate_equality_claimed": False}


MAX_ZIP_BYTES = 2_000_000
MAX_RESULT_BYTES = 500_000
EXPECTED_MEMBERS = frozenset(("results.json", "results.md", "SHA256SUMS"))


def load_verified_artifact(path):
    """Read an immutable GitHub results ZIP; reject unsigned, ambiguous or unsafe input."""
    if path.stat().st_size > MAX_ZIP_BYTES:
        raise ValueError("Oversized results ZIP")
    with zipfile.ZipFile(path) as archive:
        entries = archive.infolist()
        names = [entry.filename for entry in entries]
        if len(names) != 3 or frozenset(names) != EXPECTED_MEMBERS:
            raise ValueError("Unexpected or duplicate ZIP members")
        for entry in entries:
            if entry.is_dir() or entry.file_size > MAX_RESULT_BYTES:
                raise ValueError("Invalid or oversized ZIP member")
            if (entry.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError("ZIP symlink prohibited")
        raw = {name: archive.read(name) for name in EXPECTED_MEMBERS}
    try:
        manifest = raw["SHA256SUMS"].decode("ascii").splitlines()
        if len(manifest) != 2:
            raise ValueError("Invalid checksum manifest")
        found = {}
        for line in manifest:
            digest, name = line.split("  ", 1)
            if name not in ("results.json", "results.md") or name in found or not SHA64.fullmatch(digest):
                raise ValueError("Invalid checksum entry")
            found[name] = digest
        if frozenset(found) != EXPECTED_MEMBERS - {"SHA256SUMS"}:
            raise ValueError("Incomplete checksum manifest")
        for name, digest in found.items():
            if hashlib.sha256(raw[name]).hexdigest() != digest:
                raise ValueError("Artifact checksum mismatch: " + name)
        return json.loads(raw["results.json"])
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError("Invalid result artifact encoding") from exc



def main():
    p = argparse.ArgumentParser()
    p.add_argument("--manual", type=Path, required=True)
    p.add_argument("--scheduled", type=Path, required=True)
    p.add_argument("--zip-artifacts", action="store_true", help="Require checksummed GitHub Actions result ZIPs")
    args = p.parse_args()
    loader = load_verified_artifact if args.zip_artifacts else lambda path: json.loads(path.read_text())
    print(json.dumps(inspect(loader(args.manual), loader(args.scheduled)), sort_keys=True))


if __name__ == "__main__":
    main()
