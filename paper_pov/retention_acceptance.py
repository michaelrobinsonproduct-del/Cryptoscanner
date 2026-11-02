"""Independent, fail-closed active-to-archive identity acceptance for PAPER dry-runs.

50h compaction legitimately reduces active counts. Check cumulative preservation,
unchanged surviving records, exact archive counter deltas and archived run IDs
instead of asserting active counts never fall. No network or production writes.
"""
import datetime as dt
import hashlib
from . import ledger


def _require(condition, reason):
    if not condition:
        raise ValueError("RETENTION_ACCEPTANCE_" + reason)


def _by_id(items, key):
    values = {item[key]: item for item in items}
    _require(len(values) == len(items), "DUPLICATE_" + key.upper())
    return values


def verify_transition(before, after, report, source_sha):
    """Prove one new run plus lossless *accounted* active/archive transition.

    Archived prediction details are not stored in the active Git branch; their
    individual bytes require separately retained, authenticated run artifacts.
    This function proves known pre-transition IDs are either unchanged active
    or associated with an indexed archived run and exactly counted.
    """
    ledger.verify(before)
    ledger.verify(after)
    _require(after["generation"] == before["generation"] + 1, "GENERATION")
    _require(isinstance(report, dict) and isinstance(report.get("watch"), list)
             and isinstance(report.get("observations"), list), "REPORT")
    old_runs = _by_id(before["runs"], "id")
    new_runs = _by_id(after["runs"], "id")
    added_runs = set(new_runs) - set(old_runs)
    _require(len(added_runs) == 1, "NEW_RUN_COUNT")
    new_run_id = next(iter(added_runs))
    new_run = new_runs[new_run_id]
    report_hash = hashlib.sha256(ledger.canonical(report)).hexdigest()
    expected_run_id = hashlib.sha256((source_sha + "|" + report_hash).encode()).hexdigest()
    _require(new_run_id == expected_run_id and new_run["source_sha"] == source_sha
             and new_run["as_of"] == report["as_of"]
             and new_run["report_sha256"] == report_hash, "NEW_RUN_PROVENANCE")
    _require(new_run["watch_count"] == len(report["watch"])
             and new_run["observation_count"] == len(report["observations"]),
             "NEW_RUN_COUNTS")

    cutoff = ledger.utc(report["as_of"]) - ledger.RETENTION
    removed_runs = set(old_runs) - set(new_runs)
    for rid, value in old_runs.items():
        if rid in new_runs:
            _require(new_runs[rid] == value, "MUTATED_OLD_RUN")
        else:
            _require(ledger.utc(value["as_of"]) < cutoff, "PREMATURE_RUN_ARCHIVE")
    _require(set(new_runs) == (set(old_runs) - removed_runs) | {new_run_id},
             "RUN_IDENTITY_LOSS")

    old_predictions = _by_id(before["predictions"], "prediction_id")
    new_predictions = _by_id(after["predictions"], "prediction_id")
    removed_predictions = set(old_predictions) - set(new_predictions)
    added_predictions = set(new_predictions) - set(old_predictions)
    _require(added_predictions == {p["prediction_id"] for p in report["watch"]}
             and len(added_predictions) == len(report["watch"]), "NEW_PREDICTION_IDENTITIES")
    for pid, value in old_predictions.items():
        if pid in new_predictions:
            _require(new_predictions[pid] == value, "MUTATED_OLD_PREDICTION")
        else:
            _require(value["run_id"] in removed_runs, "PREMATURE_PREDICTION_ARCHIVE")
    _require(all(new_predictions[pid]["run_id"] == new_run_id for pid in added_predictions),
             "NEW_PREDICTION_RUN")

    def observation_key(o):
        return (o["run_id"], o["pair"])

    old_observations = {observation_key(o): o for o in before["observations"]}
    new_observations = {observation_key(o): o for o in after["observations"]}
    _require(len(old_observations) == len(before["observations"])
             and len(new_observations) == len(after["observations"]), "OBSERVATION_DUPLICATE")
    removed_observations = set(old_observations) - set(new_observations)
    added_observations = set(new_observations) - set(old_observations)
    _require(added_observations == {(new_run_id, o["pair"]) for o in report["observations"]}
             and len(added_observations) == len(report["observations"]), "NEW_OBSERVATION_IDENTITIES")
    for key, value in old_observations.items():
        if key in new_observations:
            _require(new_observations[key] == value, "MUTATED_OLD_OBSERVATION")
        else:
            _require(key[0] in removed_runs, "PREMATURE_OBSERVATION_ARCHIVE")
    for o in report["observations"]:
        actual = new_observations[(new_run_id, o["pair"])]
        _require(actual["at"] == o["observed_at"]
                 and actual["price"] == float(o["price"]), "NEW_OBSERVATION_PROVENANCE")

    old_outcomes = {(o["prediction_id"], o["horizon_hours"]): o
                    for o in before["outcomes"]}
    new_outcomes = {(o["prediction_id"], o["horizon_hours"]): o
                    for o in after["outcomes"]}
    _require(len(old_outcomes) == len(before["outcomes"])
             and len(new_outcomes) == len(after["outcomes"]), "OUTCOME_DUPLICATE")
    for key, value in old_outcomes.items():
        if key in new_outcomes:
            _require(new_outcomes[key] == value, "MUTATED_OLD_OUTCOME")
        else:
            _require(key[0] in removed_predictions, "PREMATURE_OUTCOME_ARCHIVE")

    barch, aarch = before.get("archived", {}), after.get("archived", {})
    for field, removed in (("scans", len(removed_runs)),
                           ("predictions", len(removed_predictions)),
                           ("observations", len(removed_observations))):
        _require(aarch.get(field, 0) - barch.get(field, 0) == removed,
                 "ARCHIVE_COUNTER_" + field.upper())
    for field in ("matured_labels", "gap_abstentions", "observed_30pct_hits"):
        _require(aarch.get(field, 0) >= barch.get(field, 0),
                 "ARCHIVE_COUNTER_REGRESSION_" + field.upper())

    archive_cutoff = ledger.utc(report["as_of"]) - ledger.ARCHIVE_INDEX_RETENTION
    expected_index = [r for r in before.get("archive_index", [])
                      if ledger.utc(r["as_of"]) >= archive_cutoff]
    expected_index += [r for r in before["runs"] if r["id"] in removed_runs]
    _require(after.get("archive_index", []) == expected_index, "ARCHIVE_INDEX_IDENTITY")

    bscore, ascore = ledger.scoreboard(before), ledger.scoreboard(after)
    for field, increment in (("actual_scans", 1),
                             ("immutable_predictions", len(report["watch"])),
                             ("market_observations", len(report["observations"]))):
        _require(ascore[field] == bscore[field] + increment,
                 "CUMULATIVE_" + field.upper())
    _require(ascore["matured_labels"] >= bscore["matured_labels"]
             and ascore["gap_abstentions"] >= bscore["gap_abstentions"],
             "OUTCOME_TOTAL_REGRESSION")
    return {"generation_before": before["generation"],
            "generation_after": after["generation"],
            "archived_runs": len(removed_runs),
            "archived_predictions": len(removed_predictions),
            "archived_observations": len(removed_observations),
            "new_predictions": len(added_predictions),
            "new_observations": len(added_observations),
            "cumulative_predictions": ascore["immutable_predictions"],
            "cumulative_observations": ascore["market_observations"]}
