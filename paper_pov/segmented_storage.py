"""Fail-closed, lossless Git-native storage building blocks for the paper ledger.

This module is isolated until independent integration acceptance. It never
writes the live paper-proof-ledger branch, never trades, and never promotes rules.

A committed run segment contains the *complete original paper report*, source
SHA, before/after ledger digests and generation. Its digest chain is replayable
from genesis without relying on expiring GitHub Actions artifacts. The active
ledger may be represented by a compressed, SHA-bound snapshot. One Git commit
must atomically add the segment and advance the snapshot; a non-force push and
remote byte-for-byte readback remain mandatory at workflow integration.
"""
import base64
import hashlib
import json
import zlib

from . import ledger

MAX_PACKED_BYTES = 12_000_000
MAX_RAW_BYTES = 32_000_000
FORMAT = "paper-zlib-sha256-v1"
SEGMENT_KIND = "paper-run-transition-v1"
SNAPSHOT_KIND = "paper-ledger-snapshot-v1"


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def pack_blob(obj, kind):
    """Deterministic JSON envelope; bound both on-disk and inflated bytes."""
    raw = ledger.canonical(obj)
    if len(raw) > MAX_RAW_BYTES:
        raise ValueError("Raw storage payload exceeds bounded limit")
    compressed = zlib.compress(raw, level=9)
    envelope = {"format": FORMAT, "kind": kind, "raw_size": len(raw),
                "raw_sha256": _sha(raw),
                "payload": base64.b64encode(compressed).decode("ascii")}
    output = ledger.canonical(envelope)
    if len(output) > MAX_PACKED_BYTES:
        raise ValueError("Packed storage exceeds 12 MB limit")
    return output


def unpack_blob(data, kind):
    """Bounded decompression, strict base64, exact canonical bytes and checksum."""
    if not isinstance(data, bytes) or len(data) > MAX_PACKED_BYTES:
        raise ValueError("Invalid or oversized packed payload")
    try:
        envelope = json.loads(data)
        if not isinstance(envelope, dict) or set(envelope) != {
                "format", "kind", "raw_size", "raw_sha256", "payload"}:
            raise ValueError("Unexpected packed envelope fields")
        if envelope["format"] != FORMAT or envelope["kind"] != kind:
            raise ValueError("Packed envelope format/kind mismatch")
        n = envelope["raw_size"]
        if type(n) is not int or n < 0 or n > MAX_RAW_BYTES:
            raise ValueError("Invalid uncompressed size")
        if not isinstance(envelope["raw_sha256"], str) or len(envelope["raw_sha256"]) != 64:
            raise ValueError("Invalid raw checksum")
        compressed = base64.b64decode(envelope["payload"], validate=True)
        inflater = zlib.decompressobj()
        raw = inflater.decompress(compressed, n + 1)
        if (len(raw) != n or not inflater.eof or inflater.unused_data
                or inflater.unconsumed_tail):
            raise ValueError("Truncated, trailing or oversized compressed data")
        if _sha(raw) != envelope["raw_sha256"]:
            raise ValueError("Storage checksum mismatch")
        result = json.loads(raw)
        if ledger.canonical(result) != raw:
            raise ValueError("Noncanonical packed JSON")
        return result
    except (UnicodeError, json.JSONDecodeError, zlib.error, TypeError,
            KeyError, OverflowError) as exc:
        raise ValueError("Invalid packed storage payload") from exc


def pack_snapshot(state):
    ledger.verify(state)
    return pack_blob(state, SNAPSHOT_KIND)


def unpack_snapshot(data):
    state = unpack_blob(data, SNAPSHOT_KIND)
    ledger.verify(state)
    return state


def make_segment(before, after, report, source_sha):
    """Capture immutable input evidence and independently replay transition."""
    ledger.verify(before)
    ledger.verify(after)
    replayed = ledger.advance(before, report, source_sha)
    if ledger.canonical(replayed) != ledger.canonical(after):
        raise ValueError("Segment does not replay to exact after-state")
    return pack_blob({
        "schema": SEGMENT_KIND, "generation": after["generation"],
        "source_sha": source_sha, "before_sha256": before["sha256"],
        "after_sha256": after["sha256"], "report": report,
    }, SEGMENT_KIND)


def read_segment(data):
    segment = unpack_blob(data, SEGMENT_KIND)
    if not isinstance(segment, dict) or set(segment) != {
            "schema", "generation", "source_sha", "before_sha256",
            "after_sha256", "report"} or segment["schema"] != SEGMENT_KIND:
        raise ValueError("Invalid segment schema")
    if type(segment["generation"]) is not int or segment["generation"] < 1:
        raise ValueError("Invalid segment generation")
    for key in ("before_sha256", "after_sha256"):
        v = segment[key]
        if not isinstance(v, str) or len(v) != 64 or any(c not in "0123456789abcdef" for c in v):
            raise ValueError("Invalid segment chain digest")
    return segment


def replay_segments(segments, start=None):
    """Deterministically recover from genesis or a separately verified checkpoint.

    The caller must enumerate the complete ordered segment chain, not merely
    the segments it happens to find. Missing/duplicated generations fail closed.
    """
    state = ledger.empty() if start is None else unpack_snapshot(start)
    for packed in segments:
        segment = read_segment(packed)
        if segment["generation"] != state["generation"] + 1:
            raise ValueError("Missing, duplicated or out-of-order segment")
        if segment["before_sha256"] != state["sha256"]:
            raise ValueError("Segment predecessor mismatch")
        next_state = ledger.advance(state, segment["report"], segment["source_sha"])
        if next_state["sha256"] != segment["after_sha256"]:
            raise ValueError("Segment transition mismatch")
        state = next_state
    return state


def manifest_entry(segment_bytes):
    segment = read_segment(segment_bytes)
    return {"generation": segment["generation"],
            "segment_sha256": _sha(segment_bytes),
            "before_sha256": segment["before_sha256"],
            "after_sha256": segment["after_sha256"]}


def verify_manifest_chain(entries, segments, checkpoint=None):
    """Validate exact manifest inventory, bytes and chain; no silent skips."""
    if len(entries) != len(segments):
        raise ValueError("Manifest/segment inventory mismatch")
    for entry, data in zip(entries, segments):
        if entry != manifest_entry(data):
            raise ValueError("Segment manifest mismatch")
    return replay_segments(segments, start=checkpoint)
