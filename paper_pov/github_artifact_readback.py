"""Fetch an existing GitHub Actions artifact and independently verify its bytes.

This is a read-only consumer of the existing single-writer's published artifact.
It never dispatches workflows, publishes artifacts, or writes to a ledger.
"""
import argparse
import binascii
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
    if scoreboard.get("generation") != generation or (scan.get("generation") is not None and scan["generation"] != generation):
        raise IntegrityError("Recovered ledger and scoreboard generation mismatch")
    status = scan.get("status")
    if not isinstance(status, str) or not status:
        # Historical writer receipts predate the explicit scan-status field.
        # Valid writer checksums remain recoverable, but no WATCH/ABSTAIN
        # conclusion can be inferred from the missing field.
        status = "UNKNOWN_LEGACY"
    return {"ledger_generation": generation, "scan_status": status,
            "quote_evidence_certified": scan.get("exchange_event_freshness_verified") is True
                                        and scan.get("published_quote_evidence") is True,
            "outcome": ("ABSTAIN" if status.startswith("ABSTAIN") else
                        "HISTORICAL_UNCLASSIFIED" if status == "UNKNOWN_LEGACY" else
                        "HISTORICAL_RESULT_ONLY"),
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
            # Pin both packed objects to one immutable branch checkpoint.
            # A moving writer ref must not mix a manifest from one generation
            # with a snapshot from another while the read-only consumer runs.
            try:
                ref_data = _github_json([f"repos/{repo}/git/ref/heads/{quote(ref, safe='')}"], runner=runner)
                pinned_sha = ref_data.get("object", {}).get("sha") if isinstance(ref_data, dict) else None
                if not isinstance(pinned_sha, str) or len(pinned_sha) != 40 or any(c not in "0123456789abcdef" for c in pinned_sha):
                    raise IntegrityError("Remote writer checkpoint SHA unavailable")
            except (IntegrityError, subprocess.CalledProcessError, subprocess.TimeoutExpired,
                    OSError, ValueError, KeyError, TypeError) as checkpoint_error:
                return {"status": "UNAVAILABLE", "reason": "REMOTE_CHECKPOINT_UNAVAILABLE",
                        "failure_type": type(checkpoint_error).__name__,
                        "remote_ref": ref, "remote_path": segments.SNAPSHOT,
                        "recovered_sha256": hashlib.sha256(recovered[ledger_paths[0]]).hexdigest(),
                        "independently_authenticated": False, "production_applied": False}
            def remote_object(name):
                endpoint = f"repos/{repo}/contents/{quote(name, safe='/')}?ref={pinned_sha}"
                obj = _github_json([endpoint], runner=runner)
                if not isinstance(obj, dict) or obj.get("type") != "file":
                    raise IntegrityError("Remote packed ledger object unavailable")
                if obj.get("encoding") == "base64":
                    payload = base64.b64decode("".join(obj["content"].split()), validate=True)
                    # Contents API inline bytes must match their immutable Git
                    # blob identity, not just a checksum in the packed manifest.
                    blob_sha = obj.get("sha")
                    expected_blob = hashlib.sha1(
                        b"blob " + str(len(payload)).encode("ascii") + b"\x00" + payload
                    ).hexdigest()
                    if (obj.get("size") != len(payload) or
                            not isinstance(blob_sha, str) or blob_sha != expected_blob):
                        raise IntegrityError("Remote packed ledger Git blob identity mismatch")
                    return payload
                # GitHub Contents API omits inline bytes for large blobs.
                # Resolve the immutable blob SHA through the read-only Git Data API.
                blob_sha = obj.get("sha")
                if obj.get("encoding") != "none" or not isinstance(blob_sha, str) or len(blob_sha) != 40 or any(c not in "0123456789abcdef" for c in blob_sha):
                    raise IntegrityError("Remote packed ledger blob identity unavailable")
                blob = _github_json([f"repos/{repo}/git/blobs/{blob_sha}"], runner=runner)
                if (not isinstance(blob, dict) or blob.get("sha") != blob_sha
                        or blob.get("encoding") != "base64"):
                    raise IntegrityError("Remote packed ledger blob identity mismatch")
                payload = base64.b64decode("".join(blob["content"].split()), validate=True)
                expected_blob = hashlib.sha1(
                    b"blob " + str(len(payload)).encode("ascii") + b"\x00" + payload
                ).hexdigest()
                if len(payload) != obj.get("size") or expected_blob != blob_sha:
                    raise IntegrityError("Remote packed ledger blob identity mismatch")
                return payload
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
                        "remote_ref": ref, "remote_checkpoint_sha": pinned_sha, "remote_path": segments.SNAPSHOT,
                        "remote_generation": state["generation"],
                        "recovered_generation": old_generation,
                        "remote_sha256": state["sha256"],
                        "remote_snapshot_sha256": hashlib.sha256(packed).hexdigest(),
                        "recovered_sha256": old_sha,
                        "recovered_artifact_sha256": hashlib.sha256(recovered[ledger_paths[0]]).hexdigest(),
                        "remote_ledger_sha256": state["sha256"],
                        "recovered_ledger_sha256": old_sha,
                        "independently_authenticated": False, "production_applied": False}
            except (IntegrityError, subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError, ValueError, KeyError, TypeError, AttributeError, binascii.Error, UnicodeError) as inner:
                return {"status": "UNAVAILABLE", "reason": "REMOTE_LEDGER_QUERY_FAILED",
                        "failure_type": type(inner).__name__,
                        "failure_detail": str(inner)[:240] if not isinstance(inner, subprocess.CalledProcessError) else "GITHUB_API_HTTP_" + str(inner.returncode),
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
    except (subprocess.TimeoutExpired, OSError, ValueError, TypeError, KeyError) as exc:
        # Transport failures are not evidence of a missing packed path. Avoid
        # a speculative fallback and retain the verified historical receipt.
        return {"status": "UNAVAILABLE", "reason": "REMOTE_LEDGER_QUERY_FAILED",
                "failure_type": type(exc).__name__,
                "remote_ref": ref, "remote_path": path,
                "independently_authenticated": False, "production_applied": False}
    # A malformed or missing remote comparison is not evidence that a
    # checksum-verified historical writer receipt is corrupt.
    if not isinstance(remote, dict) or remote.get("type") != "file" or remote.get("encoding") != "base64":
        return {"status": "UNAVAILABLE", "reason": "REMOTE_LEDGER_QUERY_FAILED",
                "failure_type": "REMOTE_LEDGER_FORMAT_INVALID",
                "remote_ref": ref, "remote_path": path,
                "independently_authenticated": False, "production_applied": False}
    try:
        remote_bytes = base64.b64decode("".join(remote["content"].split()), validate=True)
    except (ValueError, KeyError, TypeError, AttributeError, binascii.Error) as exc:
        return {"status": "UNAVAILABLE", "reason": "REMOTE_LEDGER_QUERY_FAILED",
                "failure_type": "REMOTE_LEDGER_BASE64_INVALID",
                "remote_ref": ref, "remote_path": path,
                "independently_authenticated": False, "production_applied": False}
    # Reconcile canonical ledger identities, not JSON serialization bytes:
    # the writer and Git branch may encode the same ledger differently.
    from paper_pov import ledger as ledger_module, segmented_storage as storage
    try:
        remote_state = json.loads(remote_bytes)
        recovered_state = json.loads(recovered[ledger_paths[0]])
        ledger_module.verify(remote_state, storage.MAX_RAW_BYTES)
        ledger_module.verify(recovered_state, storage.MAX_RAW_BYTES)
    except (ValueError, TypeError, KeyError, IntegrityError) as exc:
        return {"status": "UNAVAILABLE", "reason": "REMOTE_LEDGER_QUERY_FAILED",
                "remote_ref": ref, "remote_path": path,
                "independently_authenticated": False, "production_applied": False}
    remote_sha, recovered_sha = remote_state["sha256"], recovered_state["sha256"]
    same = (remote_sha == recovered_sha and
            remote_state["generation"] == recovered_state["generation"])
    return {"status": "MATCH" if same else "DIVERGED",
            "remote_ref": ref, "remote_path": path, "remote_sha256": remote_sha,
            "recovered_sha256": recovered_sha,
            "remote_generation": remote_state["generation"],
            "recovered_generation": recovered_state["generation"],
            "remote_artifact_sha256": hashlib.sha256(remote_bytes).hexdigest(),
            "recovered_artifact_sha256": hashlib.sha256(recovered[ledger_paths[0]]).hexdigest(),
            "remote_git_blob_sha": remote.get("sha"),
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
    if any(not isinstance(a, dict) for a in artifacts):
        raise IntegrityError("Malformed remote artifact listing")
    matches = [a for a in artifacts if a.get("name") == artifact_name]
    if len(matches) != 1:
        raise IntegrityError("Missing or duplicated remote artifact")
    if matches[0].get("expired") is not False:
        raise IntegrityError("Remote artifact expired or expiration unknown")
    origin = matches[0].get("workflow_run")
    if origin is not None and (not isinstance(origin, dict)
            or str(origin.get("id")) != str(run_id)
            or origin.get("head_sha") != source_sha):
        raise IntegrityError("Remote artifact provenance differs from source run")
    with tempfile.TemporaryDirectory(prefix="scanner-remote-readback-") as directory:
        runner(["gh", "run", "download", str(run_id), "--repo", repo,
                "--name", artifact_name, "--dir", directory], timeout=120)
        root = Path(directory)
        # Bound downloaded artifacts before reading bytes into memory.
        paths = list(root.rglob("*"))
        if len(paths) > 64:
            raise IntegrityError("Remote artifact contains too many entries")
        if any(p.is_symlink() or not (p.is_file() or p.is_dir()) for p in paths):
            raise IntegrityError("Unexpected symlink or special artifact entry")
        files = {}
        total_size = 0
        for p in paths:
            if not p.is_file():
                continue
            size = p.stat().st_size
            total_size += size
            if size > 32 * 1024 * 1024 or total_size > 64 * 1024 * 1024:
                raise IntegrityError("Remote artifact exceeds recovery size limit")
            files[p.relative_to(root).as_posix()] = p.read_bytes()
        if artifact_name == f"public-paper-ledger-{run_id}":
            index = [name for name in files if name == "SHA256SUMS" or name.endswith("/SHA256SUMS")]
            if len(index) != 1:
                raise IntegrityError("Writer checksum index missing or ambiguous")
            parent = index[0].rpartition("/")[0]
            seen = set()
            try:
                checksum_lines = files[index[0]].decode("utf-8").splitlines()
            except UnicodeDecodeError as exc:
                raise IntegrityError("Writer checksum inventory is not UTF-8") from exc
            for line in checksum_lines:
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
            expected_paths = {index[0]} | {(parent + "/" if parent else "") + name for name in seen}
            if set(files) != expected_paths:
                raise IntegrityError("Unexpected files outside writer checksum inventory")
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
            # Bind the restored receipt to the immutable source run, exact
            # checksum inventory and logical ledger. This is not independent
            # authentication of the advancing remote branch.
            inventory_path = next(name for name in files
                                  if name == "SHA256SUMS" or name.endswith("/SHA256SUMS"))
            ledger_file = next(name for name in files
                               if name == "ledger.json" or name.endswith("/ledger.json"))
            from paper_pov import ledger as ledger_module, segmented_storage as storage
            try:
                ledger_state = json.loads(files[ledger_file])
                ledger_module.verify(ledger_state, storage.MAX_RAW_BYTES)
            except (ValueError, TypeError, KeyError, IntegrityError) as exc:
                raise IntegrityError("Restored writer ledger failed logical verification") from exc
            result["source_bound_receipt"] = {
                "run_id": str(run_id),
                "source_sha": source_sha,
                "artifact_id": matches[0].get("id"),
                "sha256sums_sha256": hashlib.sha256(files[inventory_path]).hexdigest(),
                "ledger_receipt_sha256": hashlib.sha256(files[ledger_file]).hexdigest(),
                "ledger_sha256": ledger_state["sha256"],
                "ledger_generation": ledger_state["generation"],
                "independently_authenticated": False,
            }
        if ledger_ref is not None:
            reconciliation = reconcile_remote_ledger(
                repo, ledger_ref, ledger_path, files, runner=runner)
            result["remote_ledger_reconciliation"] = reconciliation
            # MATCH to a moving branch does not prove the branch checkpoint
            # was published by this specific historical source run.
            result["same_run_reconciliation"] = {
                "status": "ABSTAIN",
                "reason": "REMOTE_" + reconciliation["status"] + "_NOT_IMMUTABLY_BOUND_TO_SOURCE_RUN",
                "run_id": str(run_id),
                "source_sha": source_sha,
                "remote_checkpoint_sha": reconciliation.get("remote_checkpoint_sha"),
                "ledger_receipt_sha256": result.get("source_bound_receipt", {}).get("ledger_receipt_sha256"),
                "live_watch_authorized": False,
                "independently_authenticated": False,
            }
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
              "run_id": args.run_id, "source_sha": args.source_sha,
              "artifact_name": args.artifact_name, "ledger_writer_invoked": False,
              "production_applied": False, "independently_authenticated": False,
              "live_watch_authorized": False}
    try:
        manifest = json.loads(Path(args.manifest).read_text()) if args.manifest else None
        report = retrieve_and_verify(args.repo, args.run_id, args.artifact_name, manifest, args.source_sha,
                                     restore_dir=args.restore_dir, ledger_ref=args.ledger_ref, ledger_path=args.ledger_path)
    except (IntegrityError, OSError, ValueError, KeyError, TypeError, AttributeError,
            UnicodeError, binascii.Error, subprocess.CalledProcessError,
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
