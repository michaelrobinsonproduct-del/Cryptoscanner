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


def main():
    p = argparse.ArgumentParser()
    p.add_argument("zip", help="A2 transport ZIP or downloaded Actions artifact directory")
    args = p.parse_args()
    print(json.dumps(read_published_artifact(args.zip) if Path(args.zip).is_dir() else read_artifact_zip(args.zip), sort_keys=True, allow_nan=False))

if __name__ == "__main__":
    main()
