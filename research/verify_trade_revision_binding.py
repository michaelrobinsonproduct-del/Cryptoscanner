"""Offline, fail-closed binding of bounded trade and manifest probes to one Kraken ZIP revision.

A strong ETag is a revision validator, not a content checksum, signed
attestation, proof of historical completeness, or authorization for labels.
"""
import argparse
import json
from pathlib import Path

MAX_REPORT_BYTES = 32768


def _same_source_identity(trade, official):
    url = trade.get("source_url")
    size = trade.get("source_archive_bytes_expected")
    return (isinstance(url, str) and url.startswith("https://assets.kraken.com/")
            and url == official.get("source_url")
            and type(size) is int and size > 0
            and type(official.get("source_expected_archive_bytes")) is int
            and size == official["source_expected_archive_bytes"])


def _strong_etag(value):
    # HTTP entity tags are quoted; reject weak, control and malformed validators.
    return (isinstance(value, str) and len(value) > 2
            and value[0] == value[-1] == '"'
            and all(0x21 <= ord(c) <= 0x7e and c != '"' for c in value[1:-1]))


def bounded_reuse_decision(trade, official):
    """Fail closed on revision drift; permit ONE bounded recapture on metadata drift.

    This does not authenticate a ZIP, relax verify(), or authorize labels.
    An ETag mismatch is a source revision conflict, not a cache refresh.
    """
    if not isinstance(trade, dict) or not isinstance(official, dict):
        return "abort_invalid_revision_evidence"
    if not _same_source_identity(trade, official):
        return "abort_source_identity_mismatch"
    tv, ov = trade.get("source_revision_validator"), official.get("source_revision_validator")
    if not isinstance(tv, dict) or not isinstance(ov, dict):
        return "abort_missing_revision_validator"
    te, oe = tv.get("strong_etag"), ov.get("strong_etag")
    if not _strong_etag(te) or not _strong_etag(oe) or te != oe:
        return "abort_source_revision_conflict"
    if (not isinstance(tv.get("last_modified"), str) or not tv["last_modified"] or
            not isinstance(ov.get("last_modified"), str) or not ov["last_modified"] or
            tv["last_modified"] != ov["last_modified"]):
        return "refresh_bounded_trade_once"
    return "reuse"


def verify(trade, official):
    result = {
        "status": "abstain_unverified_source_revision",
        "same_source_revision": False,
        "source_trade_archive_sha256_verified": False,
        "complete_trade_intervals_verified": 0,
        "real_labels": 0,
        "held_out_evaluation": "not_authorized",
        "production_modified": False,
    }
    if not isinstance(trade, dict) or not isinstance(official, dict):
        return result
    if not _same_source_identity(trade, official):
        result["status"] = "abstain_source_identity_mismatch"
        return result
    t = trade.get("source_revision_validator")
    m = official.get("source_revision_validator")
    if not isinstance(t, dict) or not isinstance(m, dict):
        return result
    te, me = t.get("strong_etag"), m.get("strong_etag")
    if not _strong_etag(te) or not _strong_etag(me) or te != me:
        result["status"] = "abstain_missing_or_mismatched_strong_etag"
        return result
    if (not isinstance(t.get("last_modified"), str) or not t["last_modified"] or
            not isinstance(m.get("last_modified"), str) or not m["last_modified"] or
            t["last_modified"] != m["last_modified"]):
        result["status"] = "abstain_last_modified_mismatch"
        return result
    summary = official.get("manifest_schema_summary")
    consistency = summary.get("structural_consistency") if isinstance(summary, dict) else None
    if not isinstance(consistency, dict) or not (
            consistency.get("manifest_file_count_matches_zip_csv_count") is True
            and consistency.get("file_count_matches_pair_count") is True):
        result["status"] = "abstain_manifest_directory_inconsistent"
        return result
    markets = trade.get("markets")
    selected = official.get("selected_members")
    if not isinstance(markets, dict) or not 1 <= len(markets) <= 4 or not isinstance(selected, dict):
        result["status"] = "abstain_trade_market_selection_unverified"
        return result
    for market in markets:
        if (not isinstance(market, str) or not market.endswith(".csv") or
                not market[:-4].isalnum() or len(market) > 28 or
                market not in selected or not isinstance(selected[market], dict)
                or selected[market].get("present") is not True):
            result["status"] = "abstain_trade_market_selection_unverified"
            return result
    result["status"] = "same_revision_and_directory_consistent_not_source_authenticated"
    result["same_source_revision"] = True
    result["strong_etag"] = te
    result["trade_markets_crosschecked"] = sorted(markets)
    return result


def read_json(path):
    path = Path(path)
    if not path.is_file() or path.stat().st_size > MAX_REPORT_BYTES:
        raise ValueError("missing or oversized revision evidence")
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trades", required=True)
    parser.add_argument("--official", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    report = verify(read_json(args.trades), read_json(args.official))
    path = Path(args.output)
    if path.exists():
        raise FileExistsError("refuse report overwrite")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(report, stream, sort_keys=True)
        stream.write("\n")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
