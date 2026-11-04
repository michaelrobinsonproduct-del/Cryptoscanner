"""Fetch an existing GitHub Actions artifact and independently verify its bytes.

This is a read-only consumer of the existing single-writer's published artifact.
It never dispatches workflows, publishes artifacts, or writes to a ledger.
"""
import argparse
import hashlib
import json
import os
import shutil
from pathlib import Path
import subprocess
import tempfile

from paper_pov.runtime_readback_integrity import IntegrityError, canonical_bytes, verify_readback


def _github_json(args, *, runner):
    raw = runner(["gh", "api", "-X", "GET", *args], timeout=45)
    return json.loads(raw)




def summarize_persisted_paper(files):
    """Read actual writer receipts; distinguish historical abstention from live certification."""
    def locate(name):
        matches = [data for path, data in files.items() if path == name or path.endswith("/" + name)]
        if len(matches) != 1:
            raise IntegrityError("Missing or ambiguous persisted " + name)
        try:
            value = json.loads(matches[0])
        except (ValueError, UnicodeError) as exc:
            raise IntegrityError("Malformed persisted " + name) from exc
        if not isinstance(value, dict):
            raise IntegrityError("Non-object persisted " + name)
        return value
    scan, ledger, scoreboard = (locate(name) for name in ("latest.json", "ledger.json", "scoreboard.json"))
    generation = ledger.get("generation")
    if not isinstance(generation, int) or isinstance(generation, bool) or generation < 0:
        raise IntegrityError("Invalid recovered ledger generation")
    if scoreboard.get("generation") != generation:
        raise IntegrityError("Recovered ledger and scoreboard generation mismatch")
    status = scan.get("status")
    if not isinstance(status, str) or not status:
        raise IntegrityError("Recovered scan status absent")
    return {"ledger_generation": generation, "scan_status": status,
            "quote_evidence_certified": scan.get("exchange_event_freshness_verified") is True
                                        and scan.get("published_quote_evidence") is True,
            "outcome": "ABSTAIN" if status.startswith("ABSTAIN") else "HISTORICAL_RESULT_ONLY",
            "live_replay_performed": False}

def reconcile_remote_ledger(repo, ref, path, recovered, *, runner=subprocess.check_output):
    """Compare recovered writer bytes to the remote ledger ref without modifying either."""
    import base64
    from urllib.parse import quote
    if not ref or not path or path.startswith("/") or ".." in Path(path).parts:
        raise IntegrityError("Invalid read-only ledger ref or path")
    ledger_paths = [name for name in recovered if name == "ledger.json" or name.endswith("/ledger.json")]
    if len(ledger_paths) != 1:
        raise IntegrityError("Recovered ledger missing or ambiguous")
    endpoint = f"repos/{repo}/contents/{quote(path, safe='/')}?ref={quote(ref, safe='')}"
    try:
        remote = _github_json([endpoint], runner=runner)
    except subprocess.CalledProcessError as exc:
        # The current writer persists a packed snapshot and segment manifest,
        # NOT paper_pov/output/ledger.json on its Git branch. Read those
        # immutable GitHub objects without invoking a second ledger writer.
        if ref == "paper-proof-ledger" and path == "paper_pov/output/ledger.json":
            from paper_pov import segmented_repository as segments, segmented_storage as storage
            def remote_object(name):
                endpoint = f"repos/{repo}/contents/{quote(name, safe='/')}?ref={quote(ref, safe='')}"
                obj = _github_json([endpoint], runner=runner)
                if obj.get("type") != "file" or obj.get("encoding") != "base64":
                    raise IntegrityError("Remote packed ledger object unavailable")
                return base64.b64decode(obj["content"], validate=True)
            try:
                manifest_bytes = remote_object(segments.MANIFEST)
                if len(manifest_bytes) > segments.MAX_MANIFEST_BYTES:
                    raise IntegrityError("Remote manifest exceeds limit")
                manifest = json.loads(manifest_bytes)
                segments._check_manifest(manifest)
                packed = remote_object(segments.SNAPSHOT)
                if hashlib.sha256(packed).hexdigest() != manifest["head"]["snapshot_sha256"]:
                    raise IntegrityError("Remote snapshot SHA mismatch")
                state = storage.unpack_snapshot(packed)
                head = manifest["head"]
                if state["generation"] != head["generation"] or state["sha256"] != head["ledger_sha256"]:
                    raise IntegrityError("Remote packed ledger head mismatch")
                old = json.loads(recovered[ledger_paths[0]])
                from paper_pov import ledger as ledger_module
                ledger_module.verify(old, storage.MAX_RAW_BYTES)
                old_sha, old_generation = old["sha256"], old["generation"]
                same = old_sha == state["sha256"] and old_generation == state["generation"]
                return {"status": "MATCH" if same else "DIVERGED",
                        "reason": "PACKED_LEDGER_HEAD_COMPARISON",
                        "remote_ref": ref, "remote_path": segments.SNAPSHOT,
                        "remote_generation": state["generation"],
                        "recovered_generation": old_generation,
                        "remote_sha256": hashlib.sha256(ledger_module.canonical(state)).hexdigest(),
                        "remote_snapshot_sha256": hashlib.sha256(packed).hexdigest(),
                        "recovered_sha256": hashlib.sha256(recovered[ledger_paths[0]]).hexdigest(),
                        "remote_ledger_sha256": state["sha256"],
                        "recovered_ledger_sha256": old_sha,
                        "independently_authenticated": False, "production_applied": False}
            except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError, ValueError, KeyError, TypeError) as inner:
                return {"status": "UNAVAILABLE", "reason": "REMOTE_LEDGER_QUERY_FAILED",
                        "remote_ref": ref, "remote_path": segments.SNAPSHOT,
                        "recovered_sha256": hashlib.sha256(recovered[ledger_paths[0]]).hexdigest(),
                        "independently_authenticated": False, "production_applied": False}
        # The historical writer artifact is still recoverable if the independently
        # advancing branch has no ledger at the configured path. Do not convert
        # missing comparison evidence into MATCH or authenticated recovery.
        return {"status": "UNAVAILABLE", "reason": "REMOTE_LEDGER_QUERY_FAILED",
                "remote_ref": ref, "remote_path": path,
                "recovered_sha256": hashlib.sha256(recovered[ledger_paths[0]]).hexdigest(),
                "independently_authenticated": False, "production_applied": False}
    if remote.get("type") != "file" or remote.get("encoding") != "base64":
        raise IntegrityError("Remote ledger not a base64 file")
    try:
        remote_bytes = base64.b64decode(remote["content"], validate=False)
    except (ValueError, KeyError, TypeError) as exc:
        raise IntegrityError("Remote ledger content malformed") from exc
    remote_sha = hashlib.sha256(remote_bytes).hexdigest()
    recovered_sha = hashlib.sha256(recovered[ledger_paths[0]]).hexdigest()
    return {"status": "MATCH" if remote_sha == recovered_sha else "DIVERGED",
            "remote_ref": ref, "remote_path": path, "remote_sha256": remote_sha,
            "recovered_sha256": recovered_sha, "remote_git_blob_sha": remote.get("sha"),
            "independently_authenticated": False, "production_applied": False}


def retrieve_and_verify(repo, run_id, artifact_name, manifest, source_sha, *, runner=subprocess.check_output, restore_dir=None, ledger_ref=None, ledger_path="paper_pov/output/ledger.json"):
    """Fail closed on run identity, source SHA, artifact ambiguity and byte drift."""
    if not repo or "/" not in repo or not str(run_id).isdigit() or not artifact_name:
        raise IntegrityError("Invalid repository, run ID or artifact")
    if manifest is not None and (not isinstance(manifest, dict) or manifest.get("run_id") != str(run_id)):
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
        if artifact_name == f"public-paper-ledger-{run_id}":
            index = [name for name in files if name == "SHA256SUMS" or name.endswith("/SHA256SUMS")]
            if len(index) != 1:
                raise IntegrityError("Writer checksum index missing or ambiguous")
            parent = index[0].rpartition("/")[0]
            seen = set()
            for line in files[index[0]].decode("utf-8").splitlines():
                digest, sep, relative = line.partition("  ")
                target = (parent + "/" if parent else "") + relative
                if (not sep or len(digest) != 64 or
                    any(char not in "0123456789abcdef" for char in digest) or
                    relative not in ("latest.json", "ledger.json", "scoreboard.json") or
                    relative in seen or target not in files):
                    raise IntegrityError("Malformed writer checksum inventory")
                seen.add(relative)
                if hashlib.sha256(files[target]).hexdigest() != digest:
                    raise IntegrityError("Writer checksum mismatch")
            if seen != {"latest.json", "ledger.json", "scoreboard.json"}:
                raise IntegrityError("Incomplete writer checksum inventory")
        if manifest is None:
            if artifact_name != f"public-paper-ledger-{run_id}":
                raise IntegrityError("Writer-only verification requires the known single-writer artifact")
            result = {"status": "WRITER_CHECKSUM_ONLY", "source_sha": source_sha,
                      "run_id": str(run_id), "receipt_count": len(files),
                      "ledger_writer_invoked": False, "production_applied": False,
                      "independently_authenticated": False}
        else:
            result = verify_readback(manifest, files, expected_source_sha=source_sha,
                                     expected_run_id=run_id)
            result["independently_authenticated"] = True
        if artifact_name == f"public-paper-ledger-{run_id}":
            result["persisted_paper"] = summarize_persisted_paper(files)
        if ledger_ref is not None:
            result["remote_ledger_reconciliation"] = reconcile_remote_ledger(
                repo, ledger_ref, ledger_path, files, runner=runner)
        if restore_dir is not None:
            destination = Path(restore_dir)
            if destination.exists():
                raise IntegrityError("Recovery destination exists; refusing overwrite")
            destination.parent.mkdir(parents=True, exist_ok=True)
            staging = Path(tempfile.mkdtemp(prefix=".paper-restore-", dir=destination.parent))
            try:
                for name, data in files.items():
                    target = staging / name
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(data)
                staging.rename(destination)
            finally:
                if staging.exists():
                    shutil.rmtree(staging)
            result["recovered_to"] = str(destination)
    result.update(remote_run_url=run.get("html_url"), artifact_id=matches[0].get("id"),
                  remote_downloaded=True)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--artifact-name", default="public-paper-ledger")
    parser.add_argument("--manifest", help="Independent trusted manifest; omit only for writer-checksum-only recovery")
    parser.add_argument("--source-sha", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--restore-dir", help="Restore verified artifact to new directory without overwriting")
    parser.add_argument("--ledger-ref", help="Optional read-only Git branch/tag containing the persisted ledger")
    parser.add_argument("--ledger-path", default="paper_pov/output/ledger.json")
    args = parser.parse_args(argv)
    report = {"status": "REMOTE_READBACK_FAILED", "remote_downloaded": False,
              "ledger_writer_invoked": False, "production_applied": False}
    try:
        manifest = json.loads(Path(args.manifest).read_text()) if args.manifest else None
        report = retrieve_and_verify(args.repo, args.run_id, args.artifact_name, manifest, args.source_sha,
                                     restore_dir=args.restore_dir, ledger_ref=args.ledger_ref, ledger_path=args.ledger_path)
    except (IntegrityError, OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError,
            subprocess.TimeoutExpired) as exc:
        report["reason"] = type(exc).__name__
        if isinstance(exc, IntegrityError):
            report["failure_detail"] = str(exc)[:240]
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    temp = output.with_name(output.name + ".tmp")
    temp.write_bytes(canonical_bytes(report) + b"\n")
    os.replace(temp, output)
    print(json.dumps(report, sort_keys=True))
    return 0 if report["status"] in ("VERIFIED_REMOTE_READBACK", "WRITER_CHECKSUM_ONLY") else 2


if __name__ == "__main__":
    raise SystemExit(main())
