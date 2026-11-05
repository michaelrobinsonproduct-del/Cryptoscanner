import json
import subprocess
from pathlib import Path

try:
    import pytest
except ImportError as exc:
    # This module contains pytest function tests, not unittest.TestCase tests.
    # Broad unittest discovery must not fail importing a pytest-only module;
    # focused pytest CI still collects and executes every test here.
    import unittest
    raise unittest.SkipTest("pytest-only tests require the focused pytest runner") from exc

from paper_pov.github_artifact_readback import retrieve_and_verify
from paper_pov.runtime_readback_integrity import IntegrityError, make_manifest


REPO = "example/scanner"
SHA = "a" * 40
RECEIPTS = {"scan.json": b'{"watch":1}', "ledger.json": b'{"generation":2}'}


def runner_factory(tmp_path, *, mismatch=None):
    calls = []
    def run(args, timeout):
        calls.append(args)
        if args[:4] == ["gh", "api", "-X", "GET"]:
            if "/artifacts" in args[4]:
                return json.dumps({"total_count": 1, "artifacts": [
                    {"id": 88, "name": "paper-ledger", "expired": False}]}).encode()
            return json.dumps({"id": 123, "head_sha": "b" * 40 if mismatch == "sha" else SHA,
                "status": "completed", "conclusion": "failure" if mismatch == "failed" else "success",
                "repository": {"full_name": REPO}, "html_url": "https://github.com/example/scanner/actions/runs/123"}).encode()
        assert args[:3] == ["gh", "run", "download"]
        from pathlib import Path
        root = Path(args[-1])
        for name, value in RECEIPTS.items():
            (root / name).write_bytes(value + (b"x" if mismatch == "tamper" and name == "scan.json" else b""))
        return b""
    return run, calls


def test_verified_remote_download(tmp_path):
    run, calls = runner_factory(tmp_path)
    manifest = make_manifest(RECEIPTS, source_sha=SHA, run_id="123")
    result = retrieve_and_verify(REPO, "123", "paper-ledger", manifest, SHA, runner=run)
    assert result["remote_downloaded"] is True
    assert result["artifact_id"] == 88
    assert len(calls) == 3
    assert all(c[:2] in (["gh", "api"], ["gh", "run"]) for c in calls)


@pytest.mark.parametrize("mismatch", ["sha", "failed", "tamper"])
def test_remote_evidence_fail_closed(tmp_path, mismatch):
    run, calls = runner_factory(tmp_path, mismatch=mismatch)
    manifest = make_manifest(RECEIPTS, source_sha=SHA, run_id="123")
    with pytest.raises(IntegrityError):
        retrieve_and_verify(REPO, "123", "paper-ledger", manifest, SHA, runner=run)
    if mismatch != "tamper":
        assert not any(c[:3] == ["gh", "run", "download"] for c in calls)



@pytest.mark.parametrize("origin", [
    {"id": 999, "head_sha": SHA},
    {"id": 123, "head_sha": "b" * 40},
    {"id": 123},
    "not-a-workflow-run",
])
def test_cross_run_artifact_metadata_rejected_before_download(tmp_path, origin):
    run, calls = runner_factory(tmp_path)
    def with_origin(args, timeout):
        raw = run(args, timeout)
        if args[:4] == ["gh", "api", "-X", "GET"] and "/artifacts" in args[4]:
            listing = json.loads(raw)
            listing["artifacts"][0]["workflow_run"] = origin
            return json.dumps(listing).encode()
        return raw
    with pytest.raises(IntegrityError, match="artifact provenance"):
        retrieve_and_verify(REPO, "123", "paper-ledger",
                            make_manifest(RECEIPTS, source_sha=SHA, run_id="123"),
                            SHA, runner=with_origin)
    assert not any(call[:3] == ["gh", "run", "download"] for call in calls)


def test_expired_artifact_explicitly_rejected_before_download(tmp_path):
    run, calls = runner_factory(tmp_path)
    def expired(args, timeout):
        raw = run(args, timeout)
        if args[:4] == ["gh", "api", "-X", "GET"] and "/artifacts" in args[4]:
            listing = json.loads(raw)
            listing["artifacts"][0]["expired"] = True
            return json.dumps(listing).encode()
        return raw
    with pytest.raises(IntegrityError, match="expired"):
        retrieve_and_verify(REPO, "123", "paper-ledger",
                            make_manifest(RECEIPTS, source_sha=SHA, run_id="123"),
                            SHA, runner=expired)
    assert not any(call[:3] == ["gh", "run", "download"] for call in calls)


def test_wrong_manifest_run_never_fetches(tmp_path):
    run, calls = runner_factory(tmp_path)
    manifest = make_manifest(RECEIPTS, source_sha=SHA, run_id="999")
    with pytest.raises(IntegrityError):
        retrieve_and_verify(REPO, "123", "paper-ledger", manifest, SHA, runner=run)
    assert calls == []


def test_source_bound_receipt_never_upgrades_remote_match_to_same_run(tmp_path):
    from paper_pov import ledger
    from paper_pov.github_artifact_readback import retrieve_and_verify
    import hashlib
    state = ledger.empty()
    raw = ledger.canonical(state)
    files = {"latest.json": b'{"status":"ABSTAIN"}',
             "ledger.json": raw,
             "scoreboard.json": b'{"generation":0}'}
    files["SHA256SUMS"] = "".join(
        hashlib.sha256(data).hexdigest() + "  " + name + "\n"
        for name, data in files.items()).encode()
    def runner(args, timeout):
        if args[:4] == ["gh", "api", "-X", "GET"]:
            endpoint = args[4]
            if "/artifacts" in endpoint:
                return json.dumps({"total_count":1,"artifacts":[
                    {"id":91,"name":"public-paper-ledger-123","expired":False}]}).encode()
            if "/actions/runs/" in endpoint:
                return json.dumps({"id":123,"head_sha":SHA,"status":"completed",
                    "conclusion":"success","repository":{"full_name":REPO}}).encode()
            raise subprocess.CalledProcessError(1, args, output=b"Not Found")
        root = Path(args[-1])
        for name, data in files.items():
            (root / name).write_bytes(data)
        return b""
    result = retrieve_and_verify(REPO, "123", "public-paper-ledger", None, SHA,
                                 runner=runner, ledger_ref="historical-ledger")
    bound = result["source_bound_receipt"]
    assert bound["run_id"] == "123" and bound["source_sha"] == SHA
    assert bound["ledger_receipt_sha256"] == hashlib.sha256(raw).hexdigest()
    assert bound["sha256sums_sha256"] == hashlib.sha256(files["SHA256SUMS"]).hexdigest()
    assert result["same_run_reconciliation"]["status"] == "ABSTAIN"
    assert result["same_run_reconciliation"]["live_watch_authorized"] is False


def test_real_writer_artifact_name_and_nested_paths(tmp_path):
    """Use actual paper-pipeline artifact name and nested receipt layout."""
    from pathlib import Path
    from paper_pov import ledger as ledger_module
    receipts = {
        "paper_pov/output/latest.json": b'{"status":"ABSTAIN_LEGACY_QUOTE_EVIDENCE"}',
        "paper_pov/output/ledger.json": ledger_module.canonical(ledger_module.empty()),
        "paper_pov/output/scoreboard.json": b'{"actual_scans":0,"generation":0}',
    }
    import hashlib
    sums = "".join(hashlib.sha256(receipts[name]).hexdigest() + "  " + name.split("/")[-1] + "\n"
                   for name in receipts)
    receipts["paper_pov/output/SHA256SUMS"] = sums.encode()
    manifest = make_manifest(receipts, source_sha=SHA, run_id="123")
    def run(args, timeout):
        if args[:4] == ["gh", "api", "-X", "GET"]:
            if "/artifacts" in args[4]:
                return json.dumps({"total_count": 1, "artifacts": [
                    {"id": 91, "name": "public-paper-ledger-123", "expired": False}]}).encode()
            return json.dumps({"id": 123, "head_sha": SHA, "status": "completed",
                "conclusion": "success", "repository": {"full_name": REPO}}).encode()
        assert args[:3] == ["gh", "run", "download"]
        assert args[args.index("--name") + 1] == "public-paper-ledger-123"
        root = Path(args[-1])
        for name, data in receipts.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        return b""
    result = retrieve_and_verify(REPO, "123", "public-paper-ledger", manifest, SHA,
                                 runner=run, restore_dir=tmp_path / "recovered")
    assert result["receipt_count"] == 4
    assert (tmp_path / "recovered/paper_pov/output/ledger.json").read_bytes() == receipts["paper_pov/output/ledger.json"]


def test_real_writer_checksum_only_restores_without_independent_manifest(tmp_path):
    """Recover real-layout single-writer bytes while explicitly refusing independent-auth claim."""
    from pathlib import Path
    import hashlib
    from paper_pov import ledger as ledger_module
    receipts = {"paper_pov/output/latest.json": b'{"status":"ABSTAIN_LEGACY_QUOTE_EVIDENCE"}',
                "paper_pov/output/ledger.json": ledger_module.canonical(ledger_module.empty()),
                "paper_pov/output/scoreboard.json": b'{"actual_scans":0,"generation":0}'}
    sums = "".join(hashlib.sha256(value).hexdigest() + "  " + name.rsplit("/", 1)[-1] + "\n"
                   for name, value in receipts.items())
    receipts["paper_pov/output/SHA256SUMS"] = sums.encode()
    def run(args, timeout):
        if args[:4] == ["gh", "api", "-X", "GET"]:
            if "/artifacts" in args[4]:
                return json.dumps({"total_count": 1, "artifacts": [
                    {"id": 91, "name": "public-paper-ledger-123", "expired": False}]}).encode()
            return json.dumps({"id": 123, "head_sha": SHA, "status": "completed",
                "conclusion": "success", "repository": {"full_name": REPO}}).encode()
        root = Path(args[-1])
        for name, data in receipts.items():
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        return b""
    restored = tmp_path / "recovered"
    report = retrieve_and_verify(REPO, "123", "public-paper-ledger", None, SHA,
                                 runner=run, restore_dir=restored)
    assert report["status"] == "WRITER_CHECKSUM_ONLY"
    assert report["independently_authenticated"] is False
    assert report["remote_downloaded"] is True
    assert report["persisted_paper"]["ledger_generation"] == 0
    assert report["persisted_paper"]["outcome"] == "ABSTAIN"
    assert report["persisted_paper"]["quote_evidence_certified"] is False
    assert (restored / "paper_pov/output/ledger.json").read_bytes() == receipts["paper_pov/output/ledger.json"]
    with pytest.raises(IntegrityError):
        retrieve_and_verify(REPO, "123", "public-paper-ledger", None, SHA,
                            runner=run, restore_dir=restored)


def test_recovered_generation_mismatch_fails_closed():
    from paper_pov.github_artifact_readback import summarize_persisted_paper
    receipts = {"latest.json": b'{"status":"WATCH"}',
                "ledger.json": b'{"generation":3}',
                "scoreboard.json": b'{"generation":4}'}
    with pytest.raises(IntegrityError, match="generation mismatch"):
        summarize_persisted_paper(receipts)


def test_read_only_remote_ledger_reconciliation_matches_and_diverges():
    """Logical ledger identity, not byte formatting, determines MATCH."""
    import base64
    from paper_pov import ledger as ledger_module
    from paper_pov.github_artifact_readback import reconcile_remote_ledger
    state = ledger_module.empty()
    remote = json.dumps(state, indent=2).encode()
    recovered = ledger_module.canonical(state)
    calls = []
    def fake(args, timeout):
        calls.append(args)
        assert args[:4] == ["gh", "api", "-X", "GET"]
        return json.dumps({"type": "file", "encoding": "base64",
                           "content": base64.b64encode(remote).decode(), "sha": "git-blob"}).encode()
    report = reconcile_remote_ledger(REPO, "historical-ledger", "ledger.json",
                                     {"ledger.json": recovered}, runner=fake)
    assert report["status"] == "MATCH"
    assert report["remote_sha256"] == state["sha256"]
    assert report["remote_artifact_sha256"] != report["recovered_artifact_sha256"]
    changed = dict(state, generation=state["generation"] + 1)
    mismatch = reconcile_remote_ledger(REPO, "historical-ledger", "ledger.json",
                                       {"ledger.json": json.dumps(changed).encode()}, runner=fake)
    assert mismatch["status"] == "UNAVAILABLE"
    assert mismatch["reason"] == "REMOTE_LEDGER_QUERY_FAILED"
    assert len(calls) == 2


def test_remote_ledger_ref_rejects_unsafe_path_without_api():
    from paper_pov.github_artifact_readback import reconcile_remote_ledger
    def fail(*args, **kwargs):
        raise AssertionError("Network must not be used")
    with pytest.raises(IntegrityError):
        reconcile_remote_ledger(REPO, "paper-proof-ledger", "../ledger.json",
                                {"ledger.json": b"{}"}, runner=fail)


def test_missing_independent_ledger_keeps_real_writer_readback_truthful():
    """A 404 on the branch comparison must not invalidate writer checksummed bytes."""
    import hashlib
    from paper_pov.github_artifact_readback import reconcile_remote_ledger
    recovered = b'{"generation":65}'
    def missing(args, timeout):
        assert args[:4] == ["gh", "api", "-X", "GET"]
        raise subprocess.CalledProcessError(1, args, output=b"Not Found")
    result = reconcile_remote_ledger(REPO, "paper-proof-ledger",
                                     "paper_pov/output/ledger.json",
                                     {"ledger.json": recovered}, runner=missing)
    assert result["status"] == "UNAVAILABLE"
    assert result["reason"] == "REMOTE_CHECKPOINT_UNAVAILABLE"
    assert result["recovered_sha256"] == hashlib.sha256(recovered).hexdigest()
    assert result["independently_authenticated"] is False
    assert result["production_applied"] is False


def test_packed_single_writer_remote_reconciliation_real_storage_layout():
    """The production branch contains a packed manifest/snapshot, not output/ledger.json."""
    import base64
    import hashlib
    from paper_pov import ledger, segmented_repository as repo_storage, segmented_storage as packed
    from paper_pov.github_artifact_readback import reconcile_remote_ledger
    state = ledger.empty()
    raw = ledger.canonical(state)
    blob = packed.pack_snapshot(state)
    # Build an internally valid zero-generation manifest anchored to a checkpoint.
    checkpoint = {"git_commit": "a" * 40, "generation": 0,
                  "ledger_sha256": state["sha256"], "file_sha256": hashlib.sha256(raw).hexdigest()}
    manifest = {"schema": repo_storage.SCHEMA, "checkpoint": checkpoint,
                "head": {"generation": 0, "ledger_sha256": state["sha256"],
                         "snapshot_sha256": hashlib.sha256(blob).hexdigest()},
                "segments": []}
    calls = []
    def github(args, timeout):
        calls.append(args)
        endpoint = args[4]
        if "/git/ref/heads/paper-proof-ledger" in endpoint:
            return json.dumps({"object": {"sha": "e" * 40}}).encode()
        if "paper_pov/output/ledger.json" in endpoint:
            raise subprocess.CalledProcessError(1, args, output=b"Not Found")
        data = (json.dumps(manifest).encode() if repo_storage.MANIFEST in endpoint else
                raw if repo_storage.CHECKPOINT in endpoint else blob)
        git_sha = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\x00" + data).hexdigest()
        return json.dumps({"type": "file", "encoding": "base64", "sha": git_sha,
                           "size": len(data),
                           "content": "\n".join([base64.b64encode(data).decode()[i:i+60] for i in range(0, len(base64.b64encode(data).decode()), 60)])}).encode()
    report = reconcile_remote_ledger(REPO, "paper-proof-ledger", "paper_pov/output/ledger.json",
                                     {"ledger.json": raw}, runner=github)
    assert report["status"] == "MATCH"
    assert report["remote_generation"] == 0
    assert report["remote_sha256"] == report["recovered_sha256"]
    assert report["independently_authenticated"] is False
    assert len(calls) == 5
    assert report["remote_checkpoint_sha"] == "e" * 40
    assert report["remote_path"] == repo_storage.SNAPSHOT


def test_packed_branch_corrupt_snapshot_does_not_claim_match():
    import base64
    from paper_pov import ledger, segmented_repository as layout
    from paper_pov.github_artifact_readback import reconcile_remote_ledger
    state = ledger.empty()
    manifest = {"schema": layout.SCHEMA,
                "checkpoint": {"git_commit": "a" * 40, "generation": 0,
                               "ledger_sha256": state["sha256"], "file_sha256": "b" * 64},
                "head": {"generation": 0, "ledger_sha256": state["sha256"],
                         "snapshot_sha256": "c" * 64}, "segments": []}
    def github(args, timeout):
        endpoint = args[4]
        if "/git/ref/heads/paper-proof-ledger" in endpoint:
            return json.dumps({"object": {"sha": "e" * 40}}).encode()
        if "paper_pov/output/ledger.json" in endpoint:
            raise subprocess.CalledProcessError(1, args, output=b"Not Found")
        raw = json.dumps(manifest).encode() if layout.MANIFEST in endpoint else b"tampered snapshot"
        return json.dumps({"type": "file", "encoding": "base64",
                           "content": base64.b64encode(raw).decode()}).encode()
    result = reconcile_remote_ledger(REPO, "paper-proof-ledger",
                                     "paper_pov/output/ledger.json",
                                     {"ledger.json": ledger.canonical(state)}, runner=github)
    assert result["status"] == "UNAVAILABLE"
    assert result["independently_authenticated"] is False


def test_legacy_real_writer_without_status_is_recovered_but_unclassified():
    from paper_pov.github_artifact_readback import summarize_persisted_paper
    receipts = {"latest.json": b'{"watch_count":0}',
                "ledger.json": b'{"generation":76}',
                "scoreboard.json": b'{"generation":76}'}
    result = summarize_persisted_paper(receipts)
    assert result["ledger_generation"] == 76
    assert result["scan_status"] == "UNKNOWN_LEGACY"
    assert result["outcome"] == "HISTORICAL_UNCLASSIFIED"
    assert result["quote_evidence_certified"] is False
    assert result["live_replay_performed"] is False


def test_scan_generation_mismatch_abstains():
    from paper_pov.github_artifact_readback import summarize_persisted_paper
    receipts = {"latest.json": b'{"generation":7,"status":"WATCH"}',
                "ledger.json": b'{"generation":8}',
                "scoreboard.json": b'{"generation":8}'}
    with pytest.raises(IntegrityError, match="generation mismatch"):
        summarize_persisted_paper(receipts)


def test_writer_checksum_only_rejects_uninventoried_payload(tmp_path):
    """Extra artifact payload must not silently become recovered trusted state."""
    import hashlib
    from pathlib import Path
    receipts = {"latest.json": b'{"status":"ABSTAIN"}',
                "ledger.json": b'{"generation":2}',
                "scoreboard.json": b'{"generation":2}'}
    sums = "".join(hashlib.sha256(data).hexdigest() + "  " + name + "\n"
                   for name, data in receipts.items()).encode()
    def runner(args, timeout):
        if args[:4] == ["gh", "api", "-X", "GET"]:
            if "/artifacts" in args[4]:
                return json.dumps({"total_count": 1, "artifacts": [
                    {"id": 91, "name": "public-paper-ledger-123", "expired": False}]}).encode()
            return json.dumps({"id": 123, "head_sha": SHA, "status": "completed",
                "conclusion": "success", "repository": {"full_name": REPO}}).encode()
        root = Path(args[-1])
        for name, data in {**receipts, "SHA256SUMS": sums,
                           "unexpected.json": b'{"fake":"trusted"}'}.items():
            (root / name).write_bytes(data)
        return b""
    destination = tmp_path / "recovered"
    with pytest.raises(IntegrityError, match="Unexpected files"):
        retrieve_and_verify(REPO, "123", "public-paper-ledger", None, SHA,
                            runner=runner, restore_dir=destination)
    assert not destination.exists()


def test_packed_remote_large_snapshot_uses_sha_bound_git_blob():
    """GitHub Contents API returns encoding=none for large immutable blobs."""
    import base64
    import hashlib
    from paper_pov import ledger, segmented_repository as segments, segmented_storage as storage
    from paper_pov.github_artifact_readback import reconcile_remote_ledger
    state = ledger.empty()
    packed = storage.pack_snapshot(state)
    blob_sha = hashlib.sha1(b"blob " + str(len(packed)).encode() + b"\x00" + packed).hexdigest()
    manifest = {
        "schema": segments.SCHEMA,
        "checkpoint": {"git_commit": "a" * 40, "generation": 0,
                       "ledger_sha256": state["sha256"], "file_sha256": hashlib.sha256(ledger.canonical(state)).hexdigest()},
        "head": {"generation": 0, "ledger_sha256": state["sha256"],
                 "snapshot_sha256": hashlib.sha256(packed).hexdigest()},
        "segments": [],
    }
    calls = []
    def github(args, timeout):
        endpoint = args[4]
        if "/git/ref/heads/paper-proof-ledger" in endpoint:
            return json.dumps({"object": {"sha": "e" * 40}}).encode()
        calls.append(endpoint)
        if "paper_pov/output/ledger.json" in endpoint:
            raise subprocess.CalledProcessError(1, args)
        if "/git/blobs/" in endpoint:
            return json.dumps({"sha": blob_sha, "encoding": "base64",
                               "content": base64.b64encode(packed).decode()}).encode()
        if segments.SNAPSHOT in endpoint:
            return json.dumps({"type": "file", "encoding": "none",
                               "sha": blob_sha, "size": len(packed)}).encode()
        raw = ledger.canonical(state) if segments.CHECKPOINT in endpoint else json.dumps(manifest).encode()
        manifest_sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\x00" + raw).hexdigest()
        return json.dumps({"type": "file", "encoding": "base64", "sha": manifest_sha,
                           "size": len(raw),
                           "content": base64.b64encode(raw).decode()}).encode()
    result = reconcile_remote_ledger(REPO, "paper-proof-ledger", "paper_pov/output/ledger.json",
                                     {"ledger.json": ledger.canonical(state)}, runner=github)
    assert result["status"] == "MATCH"
    assert result["independently_authenticated"] is False
    assert any("/git/blobs/" in endpoint for endpoint in calls)


def test_packed_remote_blob_identity_mismatch_abstains():
    """A wrong Git blob SHA must never be treated as a verified ledger."""
    import base64
    from paper_pov.github_artifact_readback import reconcile_remote_ledger
    def github(args, timeout):
        endpoint = args[4]
        if "/git/ref/heads/paper-proof-ledger" in endpoint:
            return json.dumps({"object": {"sha": "e" * 40}}).encode()
        if "paper_pov/output/ledger.json" in endpoint:
            raise subprocess.CalledProcessError(1, args)
        if "/git/blobs/" in endpoint:
            return json.dumps({"sha": "d" * 40, "encoding": "base64",
                               "content": base64.b64encode(b"fake").decode()}).encode()
        if "paper-ledger.packed.json" in endpoint:
            return json.dumps({"type": "file", "encoding": "none",
                               "sha": "c" * 40, "size": 4}).encode()
        return json.dumps({"type": "file", "encoding": "base64",
                           "content": base64.b64encode(b'{}').decode()}).encode()
    result = reconcile_remote_ledger(REPO, "paper-proof-ledger", "paper_pov/output/ledger.json",
                                     {"ledger.json": b'{}'}, runner=github)
    assert result["status"] == "UNAVAILABLE"
    assert result["independently_authenticated"] is False


def test_malformed_remote_direct_ledger_preserves_historical_recovery_as_unavailable():
    """Remote corruption must not erase a valid restored writer artifact."""
    import base64
    import json
    from paper_pov import ledger
    from paper_pov.github_artifact_readback import reconcile_remote_ledger
    recovered = {"ledger.json": ledger.canonical(ledger.empty())}
    for remote in (
        {"type": "dir", "encoding": "none"},
        {"type": "file", "encoding": "base64", "content": "%%%"},
        {"type": "file", "encoding": "base64", "content": base64.b64encode(b"not-json").decode()},
    ):
        def runner(args, timeout):
            return json.dumps(remote).encode()
        report = reconcile_remote_ledger(
            REPO, "immutable-test-ref", "paper-ledger.json", recovered, runner=runner)
        assert report["status"] == "UNAVAILABLE"
        assert report["reason"] == "REMOTE_LEDGER_QUERY_FAILED"
        assert report["independently_authenticated"] is False
        assert report["production_applied"] is False

def test_non_utf8_writer_checksum_inventory_abstains(tmp_path):
    """A malformed remote receipt must be an integrity failure, not a traceback."""
    from paper_pov import ledger as ledger_module
    receipts = {
        "latest.json": b'{"status":"ABSTAIN"}',
        "ledger.json": ledger_module.canonical(ledger_module.empty()),
        "scoreboard.json": b'{"generation":0}',
        "SHA256SUMS": bytes([255, 254]),
    }
    def run(args, timeout):
        if args[:4] == ["gh", "api", "-X", "GET"]:
            if "/artifacts" in args[4]:
                return json.dumps({"total_count": 1, "artifacts": [
                    {"id": 91, "name": "public-paper-ledger-123", "expired": False}]}).encode()
            return json.dumps({"id": 123, "head_sha": SHA, "status": "completed",
                "conclusion": "success", "repository": {"full_name": REPO}}).encode()
        root = Path(args[-1])
        for name, data in receipts.items():
            (root / name).write_bytes(data)
        return b""
    with pytest.raises(IntegrityError, match="not UTF-8"):
        retrieve_and_verify(REPO, "123", "public-paper-ledger", None, SHA, runner=run)


def test_downloaded_artifact_rejects_oversized_receipt_before_read(tmp_path):
    """A valid run cannot force unbounded artifact bytes into memory."""
    manifest = make_manifest(RECEIPTS, source_sha=SHA, run_id="123")
    def oversized(args, timeout):
        if args[:4] == ["gh", "api", "-X", "GET"]:
            if "/artifacts" in args[4]:
                return json.dumps({"total_count": 1, "artifacts": [
                    {"id": 88, "name": "paper-ledger", "expired": False}]}).encode()
            return json.dumps({"id": 123, "head_sha": SHA, "status": "completed",
                "conclusion": "success", "repository": {"full_name": REPO}}).encode()
        root = Path(args[-1])
        with (root / "large.bin").open("wb") as stream:
            stream.truncate(32 * 1024 * 1024 + 1)
        return b""
    with pytest.raises(IntegrityError, match="size limit"):
        retrieve_and_verify(REPO, "123", "paper-ledger", manifest, SHA, runner=oversized)


def test_downloaded_artifact_rejects_special_file(tmp_path):
    """Never attempt to read FIFO nodes that could hang a recovery job."""
    import os
    if not hasattr(os, "mkfifo"):
        pytest.skip("FIFO unsupported")
    manifest = make_manifest(RECEIPTS, source_sha=SHA, run_id="123")
    def fifo(args, timeout):
        if args[:4] == ["gh", "api", "-X", "GET"]:
            if "/artifacts" in args[4]:
                return json.dumps({"total_count": 1, "artifacts": [
                    {"id": 88, "name": "paper-ledger", "expired": False}]}).encode()
            return json.dumps({"id": 123, "head_sha": SHA, "status": "completed",
                "conclusion": "success", "repository": {"full_name": REPO}}).encode()
        os.mkfifo(Path(args[-1]) / "blocked.fifo")
        return b""
    with pytest.raises(IntegrityError, match="special artifact"):
        retrieve_and_verify(REPO, "123", "paper-ledger", manifest, SHA, runner=fifo)


@pytest.mark.parametrize("remote_status,expected_exit", [
    ("DIVERGED", 2), ("MATCH", 0), ("UNAVAILABLE", 0),
])
def test_cli_does_not_silently_succeed_on_remote_divergence(
        tmp_path, monkeypatch, capsys, remote_status, expected_exit):
    """A valid downloaded historical artifact must not hide a divergent checkpoint."""
    from paper_pov import github_artifact_readback as readback
    def recovered(*args, **kwargs):
        return {"status": "WRITER_CHECKSUM_ONLY", "remote_downloaded": True,
                "independently_authenticated": False,
                "remote_ledger_reconciliation": {"status": remote_status},
                "same_run_reconciliation": {"status": "ABSTAIN",
                                             "live_watch_authorized": False}}
    monkeypatch.setattr(readback, "retrieve_and_verify", recovered)
    report_path = tmp_path / "recovery-report.json"
    result = readback.main([
        "--repo", REPO, "--run-id", "123", "--source-sha", SHA,
        "--ledger-ref", "paper-proof-ledger", "--output", str(report_path),
    ])
    assert result == expected_exit
    report = json.loads(report_path.read_text())
    assert report["remote_ledger_reconciliation"]["status"] == remote_status
    assert report["same_run_reconciliation"]["live_watch_authorized"] is False
