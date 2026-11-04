import json
import subprocess

import pytest

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


def test_wrong_manifest_run_never_fetches(tmp_path):
    run, calls = runner_factory(tmp_path)
    manifest = make_manifest(RECEIPTS, source_sha=SHA, run_id="999")
    with pytest.raises(IntegrityError):
        retrieve_and_verify(REPO, "123", "paper-ledger", manifest, SHA, runner=run)
    assert calls == []


def test_real_writer_artifact_name_and_nested_paths(tmp_path):
    """Use actual paper-pipeline artifact name and nested receipt layout."""
    from pathlib import Path
    receipts = {
        "paper_pov/output/latest.json": b'{"status":"ABSTAIN_LEGACY_QUOTE_EVIDENCE"}',
        "paper_pov/output/ledger.json": b'{"generation":3}',
        "paper_pov/output/scoreboard.json": b'{"actual_scans":3,"generation":3}',
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
    receipts = {"paper_pov/output/latest.json": b'{"status":"WATCH"}',
                "paper_pov/output/ledger.json": b'{"generation":3}',
                "paper_pov/output/scoreboard.json": b'{"actual_scans":3,"generation":3}'}
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
    assert report["persisted_paper"]["ledger_generation"] == 3
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
    """Recovered writer bytes are compared to remote ref without any write API."""
    import base64
    from paper_pov.github_artifact_readback import reconcile_remote_ledger
    ledger = b'{"generation":65}'
    calls = []
    def fake(args, timeout):
        calls.append(args)
        assert args[:4] == ["gh", "api", "-X", "GET"]
        return json.dumps({"type": "file", "encoding": "base64",
                           "content": base64.b64encode(ledger).decode(), "sha": "git-blob"}).encode()
    report = reconcile_remote_ledger(REPO, "paper-proof-ledger", "paper_pov/output/ledger.json",
                                     {"ledger.json": ledger}, runner=fake)
    assert report["status"] == "MATCH"
    assert report["independently_authenticated"] is False
    mismatch = reconcile_remote_ledger(REPO, "paper-proof-ledger", "paper_pov/output/ledger.json",
                                       {"ledger.json": b'{"generation":64}'}, runner=fake)
    assert mismatch["status"] == "DIVERGED"
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
    assert result["reason"] == "REMOTE_LEDGER_QUERY_FAILED"
    assert result["recovered_sha256"] == hashlib.sha256(recovered).hexdigest()
    assert result["independently_authenticated"] is False
    assert result["production_applied"] is False
