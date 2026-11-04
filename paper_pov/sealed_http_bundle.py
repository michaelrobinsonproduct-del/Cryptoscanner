"""Export an existing sealed paper scan as a read-only HTTP transport bundle.

Does not run the scanner, modify the ledger or certify the remote publisher.
"""
import argparse
import json
from pathlib import Path
from paper_pov.manual_scheduled_parity import load_sealed_scan


def build_bundle(root):
    root = Path(root)
    load_sealed_scan(root)
    raw = (root / "latest.json").read_bytes()
    return {
        "schema": "paper_sealed_bundle_v1",
        "receipt_json": raw.decode("utf-8"),
        "candidate_snapshot": json.loads((root / "candidate-snapshot.json").read_bytes()),
        "preselection_universe": json.loads((root / "preselection-universe.json").read_bytes()),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output_directory", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.parent.resolve() != args.output_directory.resolve():
        raise ValueError("bundle must stay inside the existing scanner output directory")
    from paper_pov.scanner import atomic_json
    atomic_json(args.output, build_bundle(args.output_directory))


if __name__ == "__main__":
    main()
