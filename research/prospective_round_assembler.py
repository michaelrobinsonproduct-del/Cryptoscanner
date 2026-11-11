"""Assemble factual prospective rounds; never synthesize a missing five-minute slot.

Input is an ordered sequence of independently retained one-shot batch directories.
The adapter verifies source bytes and receipt identities for every round.
"""
from collections import defaultdict
from bisect import bisect_left, bisect_right
from research.prospective_outcome_adapter import verified_rows
from research.source_qualified_outcomes import qualify, STEP, SLOT_TOLERANCE


def evaluate_rounds(batch_directories, horizon_hours=1):
    if horizon_hours not in (1, 6, 24, 48):
        raise ValueError("unsupported horizon")
    paths = list(batch_directories)
    if len(set(map(str, paths))) != len(paths):
        raise ValueError("duplicate batch directory")
    by_pair = defaultdict(list)
    abstentions = []
    for batch in paths:
        rows, missing = verified_rows(batch)
        abstentions.extend({"batch": str(batch), **a} for a in missing)
        for row in rows:
            by_pair[row["pair"]].append(row)
    outcomes = []
    forward_count = horizon_hours * 12
    for pair, rows in sorted(by_pair.items()):
        rows.sort(key=lambda r: (float(r["first_observed_at"]), float(r["event_at"])))
        observed_times = [float(row["first_observed_at"]) for row in rows]
        for index, entry in enumerate(rows):
            # Binary-search the actual first-observed receipt timeline. Older
            # code re-scanned the entire suffix for each of 576 future slots,
            # making a factual 48h cohort impractically expensive to evaluate.
            # The complete interval still requires exactly ONE source row
            # inside each +/-60s slot; gaps and duplicates abstain.
            start = observed_times[index]
            selected = []
            for offset in range(1, forward_count + 1):
                target = start + offset * STEP
                left = max(index + 1, bisect_left(
                    observed_times, target - SLOT_TOLERANCE))
                right = bisect_right(observed_times, target + SLOT_TOLERANCE)
                if right - left != 1:
                    break
                selected.append(rows[left])
            result = qualify(entry, selected, horizon_hours)
            outcomes.append({"pair": pair, "entry_event_at": entry["event_at"],
                             "entry_first_observed_at": entry["first_observed_at"],
                             "entry_source_sha256": entry["source_sha256"],
                             "entry_liquidity_usd": entry.get("entry_liquidity_usd"),
                             **result})
    return {"rounds_verified": len(paths),
            "snapshots_verified": sum(len(v) for v in by_pair.values()),
            "qualified_first_entry_episodes": sum(
                o["status"] == "QUALIFIED_OBSERVED_PATH" for o in outcomes),
            "abstentions": abstentions, "outcomes": outcomes,
            "held_out_lift": None, "production_applied": False}
