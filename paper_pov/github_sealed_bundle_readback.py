"""Read-only GitHub Actions artifact transport for the existing sealed paper bundle.

Requires authenticated gh CLI; never writes a ledger or starts a scan.
"""
import argparse
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path
from paper_pov.sealed_http_bundle import build_bundle


def _bounded_gh(args):
    return subprocess.check_output(args, timeout=20)


def read_run(repo, run_id, *, runner=_bounded_gh):
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repo or '') or not run_id.isdigit() or int(run_id) <= 0:
        raise ValueError("invalid GitHub artifact locator")
    run = json.loads(runner(["gh", "run", "view", run_id, "-R", repo,
                             "--json", "databaseId,status,conclusion,headSha,event,workflowName,headBranch"]).decode())
    if run.get("databaseId") != int(run_id) or run.get("status") != "completed" or run.get("conclusion") != "success":
        raise ValueError("paper workflow has not completed successfully")
    if run.get("event") not in ("schedule", "workflow_dispatch") or run.get("headBranch") != "main" or run.get("workflowName") != "Public Kraken Paper POV (scheduled, isolated ledger)":
        raise ValueError("untrusted paper workflow origin")
    with tempfile.TemporaryDirectory() as folder:
        root = Path(folder)
        runner(["gh", "run", "download", run_id, "-R", repo,
                "-n", "public-paper-ledger-" + run_id, "-D", str(root)])
        # gh download may flatten the original paper_pov/output prefix.
        output = root if (root / "latest.json").is_file() else root / "paper_pov" / "output"
        # Artifact-level integrity is distinct from projection/receipt consistency.
        # GitHub's archived SHA256SUMS must bind the actual downloaded files.
        sums = (output / "SHA256SUMS").read_text().splitlines()
        expected = {}
        for line in sums:
            match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_.-]+)", line)
            if not match or match.group(2) in expected:
                raise ValueError("invalid artifact checksum manifest")
            expected[match.group(2)] = match.group(1)
        for name in ("latest.json", "scoreboard.json", "ledger.json"):
            if name not in expected:
                raise ValueError("incomplete artifact checksum manifest")
            if hashlib.sha256((output / name).read_bytes()).hexdigest() != expected[name]:
                raise ValueError("downloaded artifact checksum mismatch: " + name)
        # Legacy public-paper-ledger artifacts have only latest, scoreboard and
        # ledger. Expose their checksum-verified status without claiming sealed WATCH.
        if not (output / "slot_receipt.json").is_file():
            if (output / "sealed-http-bundle.json").exists():
                raise ValueError("sealed bundle without originating slot receipt")
            latest = json.loads((output / "latest.json").read_bytes())
            scoreboard = json.loads((output / "scoreboard.json").read_bytes())
            if not isinstance(latest, dict) or not isinstance(scoreboard, dict):
                raise ValueError("invalid legacy paper artifact")
            return {"source_run_id": int(run_id), "source_sha": run["headSha"],
                    "publisher_authenticated": False, "sealed": False,
                    "watch_delivery_authorized": False,
                    "artifact_status": "CHECKSUM_VERIFIED_LEGACY_NO_RECEIPT",
                    "scoreboard": scoreboard}
        for name in ("slot_receipt.json", "sealed-http-bundle.json"):
            if name not in expected or hashlib.sha256((output / name).read_bytes()).hexdigest() != expected[name]:
                raise ValueError("sealed artifact checksum mismatch: " + name)
        slot = json.loads((output / "slot_receipt.json").read_bytes())
        if slot.get("source_sha") != run.get("headSha") or str(slot.get("run_id")) != run_id or slot.get("historical_quotes_reconstructed") is not False:
            raise ValueError("artifact run provenance mismatch")
        bundle = build_bundle(output)
        saved = json.loads((output / "sealed-http-bundle.json").read_bytes())
        if saved != bundle:
            raise ValueError("downloaded sealed HTTP bundle differs from immutable receipt")
        return {"source_run_id": int(run_id), "source_sha": run["headSha"],
                "publisher_authenticated": False, "sealed": True, "watch_delivery_authorized": False, "bundle": bundle}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    print(json.dumps(read_run(args.repo, args.run_id), sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
