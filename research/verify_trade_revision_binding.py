"""Offline, fail-closed binding of bounded trade and manifest probes to one Kraken ZIP revision.

A strong ETag is a revision validator, not a content checksum, signed
attestation, proof of historical completeness, or authorization for labels.
"""
import argparse
import json
from pathlib import Path

MAX_REPORT_BYTES = 32768


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
    if (trade.get("source_url") != official.get("source_url")
            or not isinstance(trade.get("source_url"), str)
            or not trade["source_url"].startswith("https://assets.kraken.com/")
            or type(trade.get("source_archive_bytes_expected")) is not int
            or trade["source_archive_bytes_expected"] != official.get("source_expected_archive_bytes")):
        result["status"] = "abstain_source_identity_mismatch"
        return result
    t = trade.get("source_revision_validator")
    m = official.get("source_revision_validator")
    if not isinstance(t, dict) or not isinstance(m, dict):
        return result
    te, me = t.get("strong_etag"), m.get("strong_etag")
    if not isinstance(te, str) or not te or te.startswith("W/") or not isinstance(me, str) or te != me:
        result["status"] = "abstain_missing_or_mismatched_strong_etag"
        return result
    if (t.get("last_modified") and m.get("last_modified")
            and t["last_modified"] != m["last_modified"]):
        result["status"] = "abstain_last_modified_mismatch"
        return result
    consistency = (official.get("manifest_schema_summary") or {}).get("structural_consistency")
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
        if (not isinstance(market, str) or market not in selected
                or not isinstance(selected[market], dict)
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
