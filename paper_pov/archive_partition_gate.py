"""Immutable offline Kraken archive partition provenance gate.

A digest proves bytes match a pinned manifest, not that the manifest was
published by Kraken. Require independent attestation before qualifying labels.
No network, no production writes and no implicit source-authentication claim.
"""
import argparse
import hashlib
import json
from pathlib import Path


def validate_manifest(manifest):
    if manifest.get("schema") != "kraken_archive_manifest_v1":
        raise ValueError("Unknown archive manifest schema")
    if manifest.get("source") != "Kraken":
        raise ValueError("Unexpected archive source")
    entries = manifest.get("partitions")
    if not isinstance(entries, list) or not entries:
        raise ValueError("No pinned partitions")
    names = set()
    for entry in entries:
        name = entry.get("file")
        digest = entry.get("sha256")
        if (not isinstance(name, str) or not name or name.startswith("/")
                or "\\" in name or ".." in Path(name).parts
                or Path(name).as_posix() != name):
            raise ValueError("Unsafe archive partition path")
        if name in names:
            raise ValueError("Duplicate partition")
        names.add(name)
        if (not isinstance(digest, str) or len(digest) != 64
                or any(c not in "0123456789abcdef" for c in digest)):
            raise ValueError("Invalid pinned partition digest")
        if type(entry.get("size_bytes")) is not int or entry["size_bytes"] <= 0:
            raise ValueError("Invalid partition size")
    return entries


def verify_partitions(manifest, root):
    """Fail closed on absent, altered or unexpected partition bytes."""
    entries = validate_manifest(manifest)
    root = Path(root).resolve(strict=True)
    checked = []
    for entry in entries:
        path = (root / entry["file"]).resolve(strict=True)
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError("Partition escapes archive root")
        if path.stat().st_size != entry["size_bytes"]:
            raise ValueError("Partition size mismatch: " + entry["file"])
        digest = hashlib.sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
        if digest.hexdigest() != entry["sha256"]:
            raise ValueError("Partition checksum mismatch: " + entry["file"])
        checked.append({"file": entry["file"], "sha256": digest.hexdigest(),
                        "size_bytes": entry["size_bytes"]})
    return {"schema": "archive_partition_verification_v1",
            "status": "BYTES_MATCH_PINNED_MANIFEST",
            "partitions_verified": len(checked), "partitions": checked,
            "manifest_authenticated": False,
            "source_authenticated": False,
            "qualified_for_learning": False,
            "production_applied": False,
            "reason": "Independent publisher attestation of pinned manifest not provided"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--root", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    manifest = json.loads(Path(args.manifest).read_text())
    report = verify_partitions(manifest, args.root)
    from .scanner import atomic_json
    atomic_json(args.output, report)
    print(json.dumps({"status": report["status"],
                      "partitions_verified": report["partitions_verified"],
                      "source_authenticated": False}, sort_keys=True))


if __name__ == "__main__":
    main()
