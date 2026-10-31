"""Select a deterministic cross-liquidity research cohort from verified Kraken inventory.

This is a source-data acquisition plan, not outcome evidence or a tradable ranking.
No network, production access, interpolation, or label generation.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

EXPECTED_SHA256 = "fc81b54cba6e12af3e9422dde9416179e6ef76af4831d48d839fbdb43018eaa4"
MAX_MEMBERS = 20000
MAX_SELECTED_MEMBER_BYTES = 64 * 1024 * 1024
BINS = ((0, .1), (.1, .25), (.25, .6), (.6, 1.000000001))


def select_cohorts(inventory, *, per_cohort=12):
    if not isinstance(per_cohort, int) or isinstance(per_cohort, bool) or not 1 <= per_cohort <= 32:
        raise ValueError("invalid cohort cap")
    verification = inventory.get("archive_verification", {})
    if verification.get("sha256") != EXPECTED_SHA256 or verification.get("integrity_verified") is not True:
        raise ValueError("source archive digest not independently verified")
    members = inventory.get("five_minute_csv_inventory")
    if not isinstance(members, list) or not members or len(members) > MAX_MEMBERS:
        raise ValueError("invalid inventory size")
    if inventory.get("five_minute_members") != len(members):
        raise ValueError("inventory count mismatch")
    seen = set()
    cohorts = [[] for _ in BINS]
    eligible = 0
    for row in members:
        name = row.get("member", "")
        if (not isinstance(name, str) or not name.endswith("_5.csv") or
                not re.fullmatch(r"[A-Za-z0-9._-]+", name[:-6]) or ".." in name or name in seen):
            raise ValueError("duplicate or unsafe source member")
        seen.add(name)
        if row.get("crc_checked") is not True or any(row.get(k) != 0 for k in
               ("invalid_rows", "adjacent_duplicates", "out_of_order_rows")):
            raise ValueError("source inventory integrity failure")
        first, last, n = row.get("earliest_epoch"), row.get("latest_epoch"), row.get("rows")
        if (not all(isinstance(x, int) and not isinstance(x, bool) for x in (first, last, n))
                or n < 1 or first < 0 or last < first or first % 300 or last % 300):
            raise ValueError("invalid source time or row count")
        span = (last - first) // 300 + 1
        missing = span - n
        gap_events = row.get("gap_intervals")
        if (missing < 0 or not isinstance(gap_events, int) or isinstance(gap_events, bool)
                or gap_events < 0 or gap_events > missing):
            raise ValueError("gap-event accounting mismatch")
        size = row.get("uncompressed_bytes")
        if not isinstance(size, int) or size < 0:
            raise ValueError("invalid source size")
        if n < 577 or span < 577 or size > MAX_SELECTED_MEMBER_BYTES:
            continue
        density = n / span
        eligible += 1
        idx = next(i for i, (lo, hi) in enumerate(BINS) if lo <= density < hi)
        cohorts[idx].append({"member": name, "rows": n, "density": round(density, 8),
                             "span_intervals": span, "missing_intervals": missing,
                             "gap_events": gap_events,
                             "uncompressed_bytes": size})
    selected = []
    counts = []
    for i, cohort in enumerate(cohorts):
        counts.append(len(cohort))
        if not cohort:
            raise ValueError("missing source density cohort")
        ordered = sorted(cohort, key=lambda x: hashlib.sha256(x["member"].encode()).hexdigest())
        selected.extend(dict(item, cohort=i) for item in ordered[:per_cohort])
    return {"status": "verified_inventory_cohort_selection_only",
            "archive_sha256": EXPECTED_SHA256, "inventory_members": len(members),
            "eligible_members": eligible, "cohort_eligible_counts": counts,
            "selection": "stable_sha256_member_order_within_four_density_strata",
            "selected_count": len(selected), "selected": selected,
            "independent_trade_completeness": False, "real_labels": 0,
            "held_out_evaluation": "not_authorized"}


def run(inventory_path, output_path, *, per_cohort=12):
    output = Path(output_path)
    if output.exists():
        raise FileExistsError("refuse evidence overwrite")
    with open(inventory_path, encoding="utf-8") as stream:
        inventory = json.load(stream)
    result = select_cohorts(inventory, per_cohort=per_cohort)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, sort_keys=True, separators=(",", ":"))
        stream.write("\n")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--per-cohort", type=int, default=12)
    args = parser.parse_args()
    print(json.dumps(run(args.inventory, args.output, per_cohort=args.per_cohort), sort_keys=True))
