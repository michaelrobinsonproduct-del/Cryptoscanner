import json
from pathlib import Path

import pytest

from paper_pov.runtime_readback_integrity import (
    IntegrityError, main, make_manifest, verify_readback,
)


def sample():
    receipts = {"scan.json": b'{"status":"WATCH"}', "ledger.json": b'{"generation":7}'}
    return receipts, make_manifest(receipts, source_sha="a" * 40, run_id="123")


def test_verified_exact_remote_bytes():
    receipts, manifest = sample()
    result = verify_readback(manifest, receipts, expected_source_sha="a" * 40, expected_run_id="123")
    assert result["status"] == "VERIFIED_REMOTE_READBACK"
    assert result["ledger_writer_invoked"] is False


@pytest.mark.parametrize("change", ["tamper", "missing", "extra", "source", "run", "metadata"])
def test_fail_closed(change):
    receipts, manifest = sample()
    if change == "tamper":
        receipts["scan.json"] += b" "
    elif change == "missing":
        del receipts["scan.json"]
    elif change == "extra":
        receipts["extra"] = b""
    elif change == "source":
        manifest["source_sha"] = "b" * 40
    elif change == "run":
        manifest["run_id"] = "456"
    else:
        manifest["receipts"]["scan.json"]["bytes"] += 1
    with pytest.raises(IntegrityError):
        verify_readback(manifest, receipts, expected_source_sha="a" * 40, expected_run_id="123")


def test_reject_unsafe_names():
    with pytest.raises(IntegrityError):
        make_manifest({"../secret": b"x"}, source_sha="a", run_id="1")


def test_cli_failure_report_is_atomic(tmp_path):
    receipts, manifest = sample()
    manifest_path = tmp_path / "manifest.json"
    manifest_path.write_text(json.dumps(manifest))
    remote = tmp_path / "remote"
    remote.mkdir()
    for name, data in receipts.items():
        (remote / name).write_bytes(data)
    output = tmp_path / "report.json"
    args = ["--manifest", str(manifest_path), "--remote-dir", str(remote),
            "--source-sha", "a" * 40, "--run-id", "123", "--output", str(output)]
    assert main(args) == 0
    assert json.loads(output.read_text())["status"] == "VERIFIED_REMOTE_READBACK"
    (remote / "scan.json").write_bytes(b"corrupted")
    assert main(args) == 2
    assert json.loads(output.read_text())["status"] == "REMOTE_READBACK_FAILED"
