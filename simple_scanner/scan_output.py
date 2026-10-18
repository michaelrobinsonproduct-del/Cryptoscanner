"""Atomic publication of scanner results; never expose a truncated latest.json."""
import json
import os
import tempfile
from pathlib import Path

def publish_latest_atomic(destination, report):
    """Write complete JSON then replace; preserve last good report on write failure."""
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".latest-", suffix=".json.tmp", dir=str(destination.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(report, stream, indent=2, allow_nan=False)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, destination)
        # Flush the directory entry after atomic replacement on POSIX systems.
        if os.name == "posix":
            directory_fd = os.open(str(destination.parent), os.O_RDONLY)
            try:
                os.fsync(directory_fd)
            finally:
                os.close(directory_fd)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)

def verify_market_evidence(report):
    """Read-only completeness and freshness audit; no scoring side effects."""
    import datetime as dt
    prices = report.get("market_prices", {})
    signals = report.get("market_signals", {})
    identities = report.get("asset_pairs", {})
    missing = sorted(set(signals) - set(prices) | (set(signals) - set(identities)))
    try:
        started = dt.datetime.fromisoformat(report["started_at"])
        completed = dt.datetime.fromisoformat(report["completed_at"])
        duration = (completed - started).total_seconds()
        valid_time = started.tzinfo is not None and completed.tzinfo is not None and duration >= 0
    except (KeyError, ValueError, TypeError):
        duration = None
        valid_time = False
    return {"status": "COMPLETE" if not missing and valid_time and signals else "INCOMPLETE",
            "signals": len(signals), "prices": len(prices),
            "canonical_identities": len(identities), "missing_pairs": missing,
            "scan_duration_seconds": duration if valid_time else None}

def persist_scan_archive(directory, report):
    """Atomically publish one immutable scan snapshot, without replacing older data."""
    import hashlib
    if verify_market_evidence(report)["status"] != "COMPLETE":
        raise ValueError("incomplete market evidence")
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    stamp = report["completed_at"]
    target = directory / (hashlib.sha256(stamp.encode()).hexdigest() + ".json")
    payload = json.dumps(report, allow_nan=False, sort_keys=True).encode("utf-8")
    # Never silently evict history. Fail closed if the configured evidence budget is full.
    max_bytes = int(os.getenv("SIMPLE_SCANNER_ARCHIVE_MAX_BYTES", "10485760"))
    max_record = int(os.getenv("SIMPLE_SCANNER_ARCHIVE_MAX_RECORD_BYTES", "1048576"))
    if max_bytes <= 0 or max_record <= 0 or len(payload) > max_record:
        raise ValueError("scan evidence exceeds configured record budget")
    if target.exists():
        raise FileExistsError(str(target))
    used = sum(p.stat().st_size for p in directory.glob("*.json") if p.is_file())
    if used + len(payload) > max_bytes:
        raise OSError("scan evidence archive budget exceeded; no records removed")
    fd, temporary = tempfile.mkstemp(prefix=".scan-", suffix=".tmp", dir=str(directory))
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        # Hard-link creates a new name only if absent; readers never see partial data.
        os.link(temporary, target)
        if os.name == "posix":
            dirfd = os.open(str(directory), os.O_RDONLY)
            try:
                os.fsync(dirfd)
            finally:
                os.close(dirfd)
    finally:
        Path(temporary).unlink(missing_ok=True)
    return target

def verify_scan_archive(path):
    """Reject corrupt or incomplete archived market evidence."""
    import hashlib
    path = Path(path)
    report = json.loads(path.read_text(encoding="utf-8"))
    expected_name = hashlib.sha256(report["completed_at"].encode()).hexdigest() + ".json"
    if path.name != expected_name:
        raise ValueError("scan archive timestamp identity mismatch")
    if verify_market_evidence(report)["status"] != "COMPLETE":
        raise ValueError("incomplete archived market evidence")
    return report

def compare_sqlite_run_timestamp(run_at, archived_report):
    """Exact, read-only timestamp reconciliation; never infer a same-run join."""
    import datetime as dt
    try:
        sqlite_time = dt.datetime.fromisoformat(str(run_at).replace("Z", "+00:00"))
        archive_time = dt.datetime.fromisoformat(archived_report["completed_at"].replace("Z", "+00:00"))
        if sqlite_time.tzinfo is None or archive_time.tzinfo is None:
            return {"status": "UNVERIFIED_TIMEZONE"}
        offset = (sqlite_time - archive_time).total_seconds()
        return {"status": "EXACT_MATCH" if offset == 0 else "TIMESTAMP_MISMATCH",
                "offset_seconds": offset}
    except (KeyError, TypeError, ValueError, AttributeError):
        return {"status": "INVALID_TIMESTAMP"}

def archive_content_sha256(path):
    """Hash actual persisted bytes, for independent future integrity comparisons."""
    import hashlib
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def publish_scan_with_archive(directory, report):
    """Always publish a valid scan; explicitly disclose missing archive evidence."""
    directory = Path(directory)
    report = dict(report)
    try:
        archive_path = persist_scan_archive(directory / "scan_archive", report)
        report["archive_status"] = "RECORDED"
        report["archive_record"] = archive_path.name
        verify_scan_archive(archive_path)
        report["archive_sha256"] = archive_content_sha256(archive_path)
    except (OSError, ValueError, TypeError) as error:
        # Never pretend missing evidence was saved, or suppress valid scan output.
        report["archive_status"] = "NOT_RECORDED"
        report["archive_error"] = type(error).__name__
        report["learning_status"] = "NOT_VALIDATED"
    publish_latest_atomic(directory / "latest.json", report)
    return report

def verify_archive_against_latest(directory):
    """Compare persisted archive to the separately published latest digest."""
    import hmac
    directory = Path(directory)
    latest = json.loads((directory / "latest.json").read_text(encoding="utf-8"))
    if latest.get("archive_status") != "RECORDED":
        return {"status": "UNVERIFIED_NOT_RECORDED"}
    filename = latest.get("archive_record")
    digest = latest.get("archive_sha256")
    if not isinstance(filename, str) or Path(filename).name != filename:
        return {"status": "INVALID_ARCHIVE_REFERENCE"}
    if not isinstance(digest, str) or len(digest) != 64:
        return {"status": "INVALID_ARCHIVE_DIGEST"}
    path = directory / "scan_archive" / filename
    try:
        archive = verify_scan_archive(path)
        actual = archive_content_sha256(path)
    except (OSError, ValueError, TypeError, KeyError):
        return {"status": "ARCHIVE_READBACK_FAILED"}
    if not hmac.compare_digest(actual, digest):
        return {"status": "ARCHIVE_DIGEST_MISMATCH"}
    if archive.get("completed_at") != latest.get("completed_at"):
        return {"status": "ARCHIVE_SCAN_MISMATCH"}
    return {"status": "VERIFIED", "completed_at": latest["completed_at"]}
