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
