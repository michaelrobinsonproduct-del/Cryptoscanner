"""Read-only, fail-closed verification of the downloadable A2 GitHub artifact ZIP.

This is a transport adapter for Owner B, not a persistent HTTPS endpoint.
"""
import argparse
import datetime as dt
import hashlib
import io
import json
import tempfile
import zipfile
from pathlib import Path
from paper_pov.candidate_snapshot import read_snapshot

def read_artifact_zip(archive, now=None):
    data = Path(archive).read_bytes() if isinstance(archive, (str, Path)) else archive
    if len(data) > 2_000_000:
        raise ValueError("oversized A2 artifact")
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        infos = z.infolist()
        names = [i.filename for i in infos]
        if len(names) != 3 or len(set(names)) != 3 or "latest.json" not in names or "verified-snapshot.json" not in names:
            raise ValueError("invalid A2 artifact members")
        receipts = [n for n in names if n.startswith("receipts/") and n.endswith(".json") and n.count("/") == 1]
        if len(receipts) != 1:
            raise ValueError("missing immutable A2 receipt")
        for info in infos:
            if info.is_dir() or info.file_size > 1_000_000 or info.compress_size > 500_000 or (info.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError("unsafe A2 artifact member")
        latest = z.read("latest.json")
        receipt = z.read(receipts[0])
        exported = json.loads(z.read("verified-snapshot.json"))
        if latest != receipt:
            raise ValueError("A2 receipt mismatch")
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        (root / "receipts").mkdir()
        (root / "latest.json").write_bytes(latest)
        (root / receipts[0]).write_bytes(receipt)
        verified = read_snapshot(root / "latest.json", now=now)
    # Ages legitimately increase between export and download. Validate immutable fields
    # against the receipt, and enforce the *current* read-time freshness separately.
    for key in ("as_of", "scan_status", "eligible_pairs", "observed_markets", "abstention_counts", "watch", "receipt_sha256"):
        if exported.get(key) != verified[key]:
            raise ValueError("A2 exported consumer snapshot mismatch: " + key)
    if exported.get("snapshot_age_seconds", -1) < 0 or not isinstance(exported.get("quote_age_seconds"), dict):
        raise ValueError("invalid exported age evidence")
    if set(exported["quote_age_seconds"]) != set(verified["quote_age_seconds"]):
        raise ValueError("A2 quote age coverage mismatch")
    if exported["receipt_sha256"] != hashlib.sha256(receipt).hexdigest():
        raise ValueError("A2 artifact digest mismatch")
    return verified

def read_published_artifact(directory, now=None):
    """Consume the exact downloaded Actions artifact directory, not a reconstructed ZIP.

    Require both the immutable WATCH transport and complete preselection universe
    to agree on the same sealed receipt. Never authorize historical/stale WATCH.
    """
    from paper_pov.preselection_universe import export_universe
    root = Path(directory)
    if root.is_symlink() or not root.is_dir():
        raise ValueError("invalid downloaded A2 artifact directory")
    transport = root / "a2-verified-transport.zip"
    universe_file = root / "preselection-universe.json"
    latest = root / "latest.json"
    if any(p.is_symlink() or not p.is_file() for p in (transport, universe_file, latest)):
        raise ValueError("incomplete downloaded A2 artifact")
    if universe_file.stat().st_size > 2_000_000:
        raise ValueError("oversized preselection evidence")
    snapshot = read_artifact_zip(transport, now=now)
    published = json.loads(universe_file.read_bytes())
    verified_universe = export_universe(latest, now=now)
    if published != verified_universe:
        raise ValueError("published preselection universe mismatch")
    if verified_universe["receipt_sha256"] != snapshot["receipt_sha256"]:
        raise ValueError("preselection and WATCH receipt mismatch")
    if verified_universe["selection_decisions"]["WATCH"] != len(snapshot["watch"]):
        raise ValueError("preselection WATCH coverage mismatch")
    return {"snapshot": snapshot, "preselection": verified_universe}



def project_watch_delivery(directory, now=None):
    """B-facing read-only delivery from the SAME published A receipt and universe.

    This is not the production paper-ledger result and never claims the
    single-writer ledger has persisted it. It is safe for manual/scheduled
    presentation only while the original Kraken client quotes remain fresh.
    """
    verified = read_published_artifact(directory, now=now)
    snapshot, universe = verified["snapshot"], verified["preselection"]
    watch = []
    for candidate in snapshot["watch"]:
        watch.append({
            "rank": candidate["rank"], "symbol": candidate["symbol"],
            "price": candidate["price"], "quote_observed_at": candidate["quote_observed_at"],
            "baseline_score": candidate["baseline_score"],
            "challenger_score": candidate["challenger_score"],
            "move15_pct": candidate["move15_pct"],
            "volume_accel": candidate["volume_accel"], "risk": candidate["risk"],
            "status": candidate["status"], "buy_approved": False,
            "prediction_id": candidate["prediction_id"],
        })
    return {
        "schema": "a2_published_watch_delivery_v1",
        "source": "kraken_public_rest_client_observed",
        "as_of": snapshot["as_of"], "scan_status": snapshot["scan_status"],
        "receipt_sha256": snapshot["receipt_sha256"],
        "watch": watch, "watch_count": len(watch),
        "eligible_pairs": snapshot["eligible_pairs"],
        "observed_markets": snapshot["observed_markets"],
        "preselection_observations": len(universe["markets"]),
        "selection_decisions": universe["selection_decisions"],
        "abstention_counts": snapshot["abstention_counts"],
        "snapshot_age_seconds": snapshot["snapshot_age_seconds"],
        "quote_age_seconds": snapshot["quote_age_seconds"],
        "client_quote_freshness_verified": True,
        "exchange_event_freshness_verified": False,
        "single_writer_ledger_verified": False,
        "production_applied": False, "buy_approved": False,
    }

def read_published_delivery(directory, now=None):
    """Authenticate B's published JSON against the sealed A2 receipt at read time.

    A copied a2-delivery.json is not trusted by itself. Require the complete
    downloaded artifact and compare all immutable delivery fields to a fresh
    projection. Age evidence is recomputed rather than copied from publication.
    """
    root = Path(directory)
    published_file = root / "a2-delivery.json"
    if published_file.is_symlink() or not published_file.is_file() or published_file.stat().st_size > 2_000_000:
        raise ValueError("missing or unsafe published A2 delivery")
    published = json.loads(published_file.read_bytes())
    if not isinstance(published, dict):
        raise ValueError("invalid published A2 delivery")
    verified = project_watch_delivery(root, now=now)
    age_keys = {"snapshot_age_seconds", "quote_age_seconds"}
    if set(published) != set(verified):
        raise ValueError("published A2 delivery field coverage mismatch")
    for key, value in verified.items():
        if key not in age_keys and published[key] != value:
            raise ValueError("published A2 delivery mismatch: " + key)
    if type(published["snapshot_age_seconds"]) not in (int, float) or published["snapshot_age_seconds"] < 0:
        raise ValueError("invalid published A2 snapshot age")
    if not isinstance(published["quote_age_seconds"], dict) or set(published["quote_age_seconds"]) != set(verified["quote_age_seconds"]):
        raise ValueError("invalid published A2 quote age coverage")
    return verified


def main():
    p = argparse.ArgumentParser()
    p.add_argument("zip", help="A2 transport ZIP or downloaded Actions artifact directory")
    p.add_argument("--delivery", action="store_true", help="verify and emit B-facing published WATCH delivery from downloaded artifact directory")
    args = p.parse_args()
    if args.delivery and not Path(args.zip).is_dir():
        p.error("--delivery requires the complete downloaded A2 artifact directory")
    result = read_published_delivery(args.zip) if args.delivery else (read_published_artifact(args.zip) if Path(args.zip).is_dir() else read_artifact_zip(args.zip))
    print(json.dumps(result, sort_keys=True, allow_nan=False))

if __name__ == "__main__":
    main()
