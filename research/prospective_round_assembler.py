"""Assemble factual prospective rounds; never synthesize a missing five-minute slot.

Input is an ordered sequence of independently retained one-shot batch directories.
The adapter verifies source bytes and receipt identities for every round.
"""
from collections import defaultdict
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
        rows.sort(key=lambda r: (int(r["first_observed_at"]), int(r["event_at"])))
        for index, entry in enumerate(rows):
            # Never round exchange event times into fictitious grid slots.
            # Select actual first-observed receipts in each bounded cadence slot; duplicates
            # and missing slots must abstain rather than be silently dropped.
            start = float(entry["first_observed_at"])
            selected = []
            for offset in range(1, forward_count + 1):
                target = start + offset * STEP
                matching = [r for r in rows[index + 1:] if abs(float(r["first_observed_at"]) - target) <= SLOT_TOLERANCE]
                if len(matching) != 1:
                    break
                selected.append(matching[0])
            result = qualify(entry, selected, horizon_hours)
            outcomes.append({"pair": pair, "entry_event_at": entry["event_at"],
                             "entry_first_observed_at": entry["first_observed_at"],
                             "entry_source_sha256": entry["source_sha256"],
                             **result})
    return {"rounds_verified": len(paths),
            "snapshots_verified": sum(len(v) for v in by_pair.values()),
            "qualified_first_entry_episodes": sum(
                o["status"] == "QUALIFIED_OBSERVED_PATH" for o in outcomes),
            "abstentions": abstentions, "outcomes": outcomes,
            "held_out_lift": None, "production_applied": False}
