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
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
