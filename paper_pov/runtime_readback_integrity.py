"""Read-only verification of remotely persisted scanner receipts.

No ledger mutation, trading, or workflow dispatch. Compare independently
downloaded bytes against an immutable local manifest and fail closed.
"""
import argparse
import hashlib
import json
from pathlib import Path


class IntegrityError(ValueError):
    pass


def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()


def make_manifest(receipts, *, source_sha, run_id):
    if not source_sha or not run_id or not isinstance(receipts, dict) or not receipts:
        raise IntegrityError("Source SHA, run ID and receipts are required")
    entries = {}
    for name, data in sorted(receipts.items()):
        if not isinstance(name, str) or not name or "/" in name or "\\" in name or name in (".", ".."):
            raise IntegrityError("Unsafe receipt name")
        if not isinstance(data, bytes):
            raise IntegrityError("Receipt must contain raw persisted bytes")
        entries[name] = {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
    return {"schema": "runtime_remote_readback_v1", "source_sha": source_sha,
            "run_id": str(run_id), "receipts": entries}


def verify_readback(manifest, remote_receipts, *, expected_source_sha, expected_run_id):
    """Verify exact bytes fetched from the remote store, not a local copy."""
    if not isinstance(manifest, dict) or manifest.get("schema") != "runtime_remote_readback_v1":
        raise IntegrityError("Invalid manifest schema")
    if manifest.get("source_sha") != expected_source_sha or manifest.get("run_id") != str(expected_run_id):
        raise IntegrityError("Source or run provenance mismatch")
    entries = manifest.get("receipts")
    if not isinstance(entries, dict) or not entries or set(entries) != set(remote_receipts):
        raise IntegrityError("Missing or unexpected remote receipts")
    for name, expected in entries.items():
        if not isinstance(expected, dict) or set(expected) != {"sha256", "bytes"}:
            raise IntegrityError("Malformed receipt metadata")
        data = remote_receipts[name]
        if not isinstance(data, bytes) or len(data) != expected["bytes"] or hashlib.sha256(data).hexdigest() != expected["sha256"]:
            raise IntegrityError("Remote readback mismatch: " + name)
    return {"status": "VERIFIED_REMOTE_READBACK", "source_sha": expected_source_sha,
            "run_id": str(expected_run_id), "receipt_count": len(entries),
            "ledger_writer_invoked": False, "production_applied": False}


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--remote-dir", required=True, help="Directory of independently downloaded remote bytes")
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    report = {"status": "REMOTE_READBACK_FAILED", "ledger_writer_invoked": False,
              "production_applied": False}
    try:
        manifest = json.loads(Path(args.manifest).read_text())
        names = manifest.get("receipts", {})
        if not isinstance(names, dict) or not names:
            raise IntegrityError("Missing receipt inventory")
        root = Path(args.remote_dir)
        if not root.is_dir():
            raise IntegrityError("Remote download directory missing")
        remote = {}
        for name in names:
            if not isinstance(name, str) or not name or "/" in name or "\\" in name or name in (".", ".."):
                raise IntegrityError("Unsafe receipt name")
            remote[name] = (root / name).read_bytes()
        if set(p.name for p in root.iterdir() if p.is_file()) != set(names):
            raise IntegrityError("Unexpected or missing downloaded receipt")
        report = verify_readback(manifest, remote, expected_source_sha=args.source_sha,
                                 expected_run_id=args.run_id)
    except (IntegrityError, OSError, ValueError, TypeError, KeyError) as exc:
        report["reason"] = type(exc).__name__
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    temp = output.with_name(output.name + ".tmp")
    temp.write_bytes(canonical_bytes(report) + b"\n")
    temp.replace(output)
    print(json.dumps(report, sort_keys=True))
    return 0 if report["status"] == "VERIFIED_REMOTE_READBACK" else 2


if __name__ == "__main__":
    raise SystemExit(main())
