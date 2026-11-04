"""Fetch an existing GitHub Actions artifact and independently verify its bytes.

This is a read-only consumer of the existing single-writer's published artifact.
It never dispatches workflows, publishes artifacts, or writes to a ledger.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile

from paper_pov.runtime_readback_integrity import IntegrityError, canonical_bytes, verify_readback


def _github_json(args, *, runner):
    raw = runner(["gh", "api", "-X", "GET", *args], timeout=45)
    return json.loads(raw)


def retrieve_and_verify(repo, run_id, artifact_name, manifest, source_sha, *, runner=subprocess.check_output):
    """Fail closed on run identity, source SHA, artifact ambiguity and byte drift."""
    if not repo or "/" not in repo or not str(run_id).isdigit() or not artifact_name:
        raise IntegrityError("Invalid repository, run ID or artifact")
    if not isinstance(manifest, dict) or manifest.get("run_id") != str(run_id):
        raise IntegrityError("Untrusted or mismatched manifest run ID")
    run = _github_json([f"repos/{repo}/actions/runs/{run_id}"], runner=runner)
    if (str(run.get("id")) != str(run_id) or run.get("head_sha") != source_sha
            or run.get("status") != "completed" or run.get("conclusion") != "success"
            or run.get("repository", {}).get("full_name") != repo):
        raise IntegrityError("Run not completed successfully or provenance differs")
    listing = _github_json([f"repos/{repo}/actions/runs/{run_id}/artifacts", "-f", "per_page=100"], runner=runner)
    artifacts = listing.get("artifacts")
    if (not isinstance(artifacts, list) or not isinstance(listing.get("total_count"), int)
            or listing["total_count"] != len(artifacts)):
        raise IntegrityError("Artifact listing incomplete")
    if artifact_name == "public-paper-ledger":
        artifact_name = f"public-paper-ledger-{run_id}"
    matches = [a for a in artifacts if a.get("name") == artifact_name]
    if len(matches) != 1 or matches[0].get("expired") is not False:
        raise IntegrityError("Missing, duplicated or expired artifact")
    with tempfile.TemporaryDirectory(prefix="scanner-remote-readback-") as directory:
        runner(["gh", "run", "download", str(run_id), "--repo", repo,
                "--name", artifact_name, "--dir", directory], timeout=120)
        root = Path(directory)
        paths = list(root.rglob("*"))
        if any(p.is_symlink() for p in paths):
            raise IntegrityError("Unexpected nested or symlinked artifact entries")
        files = {p.relative_to(root).as_posix(): p.read_bytes() for p in paths if p.is_file()}
        result = verify_readback(manifest, files, expected_source_sha=source_sha,
                                 expected_run_id=run_id)
    result.update(remote_run_url=run.get("html_url"), artifact_id=matches[0].get("id"),
                  remote_downloaded=True)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--artifact-name", default="public-paper-ledger")
    parser.add_argument("--manifest", required=True, help="Trusted manifest saved separately from remote artifact")
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    report = {"status": "REMOTE_READBACK_FAILED", "remote_downloaded": False,
              "ledger_writer_invoked": False, "production_applied": False}
    try:
        manifest = json.loads(Path(args.manifest).read_text())
        report = retrieve_and_verify(args.repo, args.run_id, args.artifact_name, manifest, args.source_sha)
    except (IntegrityError, OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError,
            subprocess.TimeoutExpired) as exc:
        report["reason"] = type(exc).__name__
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    temp = output.with_name(output.name + ".tmp")
    temp.write_bytes(canonical_bytes(report) + b"\n")
    os.replace(temp, output)
    print(json.dumps(report, sort_keys=True))
    return 0 if report["status"] == "VERIFIED_REMOTE_READBACK" else 2


if __name__ == "__main__":
    raise SystemExit(main())
