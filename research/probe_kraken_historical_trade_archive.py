"""Bounded, read-only probe of Kraken's official 2026Q2 time-and-sales ZIP.

Only reads remote ZIP metadata and bounded CSV prefix; does not claim complete
trade coverage until the entire source ZIP is downloaded and authenticated.
"""
import argparse
import hashlib
import json
import urllib.request
from pathlib import Path

URL = "https://assets.kraken.com/marketing/institutions/Kraken_Trades_2026Q2.zip"
MAX_SAMPLE = 65536
TIMEOUT = 25


def probe(opener=None):
    opener = opener or urllib.request.urlopen
    req = urllib.request.Request(URL, headers={"Range": f"bytes=0-{MAX_SAMPLE-1}",
        "Accept-Encoding": "identity", "User-Agent": "Cryptoscanner-isolated-research/1.0"})
    with opener(req, timeout=TIMEOUT) as response:
        if response.status != 206:
            raise RuntimeError("range request not honored; refuse unbounded download")
        if response.headers.get("Content-Encoding", "identity").lower() != "identity":
            raise RuntimeError("unexpected content encoding")
        content_range = response.headers.get("Content-Range", "")
        if not content_range.startswith(f"bytes 0-{MAX_SAMPLE-1}/"):
            raise RuntimeError("unexpected content range")
        total = int(content_range.rsplit("/", 1)[1])
        if total <= MAX_SAMPLE or total > 20 * 1024**3:
            raise RuntimeError("unexpected archive size")
        raw = response.read(MAX_SAMPLE + 1)
    if len(raw) != MAX_SAMPLE or raw[:4] != b"PK\\x03\\x04":
        raise RuntimeError("not an expected ZIP prefix")
    return {"status": "official_trade_archive_range_verified_not_full_checksum",
            "source": URL, "bytes_total": total, "bytes_sampled": len(raw),
            "sample_sha256": hashlib.sha256(raw).hexdigest(),
            "complete_trade_interval_verified": False, "historical_labels": 0}


def run(output):
    output = Path(output)
    if output.exists():
        raise FileExistsError("refuse overwrite")
    result = probe()
    payload = (json.dumps(result, sort_keys=True) + "\n").encode()
    if len(payload) > 4096:
        raise RuntimeError("oversized report")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("xb") as out:
        out.write(payload)
    return result


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    print(json.dumps(run(args.output), sort_keys=True))
