"""Audit-only independent heartbeat/recovery rehearsal; NEVER dispatches.

This composes the existing owner-authenticated issue-comment cadence gate and
the existing one-writer PAPER workflow. A GitHub cron is not an independent
clock. GitHub Actions noncancelling concurrency serializes jobs but is NOT a
durable per-slot idempotency guarantee.
"""
import datetime as dt
import re
from pathlib import Path

from .cadence_wake import authorize, decide

REPO = "michaelrobinsonproduct-del/Cryptoscanner"
WRITER = "paper-pipeline.yml"
MUTEX = "public-paper-proof-ledger-single-writer"
CONTROLLER_MUTEX = "public-paper-recovery-controller"
SHA = re.compile(r"[0-9a-f]{40}\Z")


def _require(condition, reason):
    if not condition:
        raise ValueError(reason)


def validate_workflows(sources):
    """Fail closed on drift in the four exact-checkout workflow contracts."""
    _require(isinstance(sources, dict), "MISSING_WORKFLOW_SOURCES")
    required = ("paper-pipeline.yml", "paper-cadence-wake.yml",
                "paper-recovery.yml", "paper-external-heartbeat.yml")
    _require(all(isinstance(sources.get(n), str) and sources[n] for n in required),
             "MISSING_WORKFLOW_SOURCE")
    writer, cadence, recovery, external = (sources[n] for n in required)
    _require("on:\n  workflow_dispatch:" in writer and
             "- cron: '9 * * * *'" in writer and
             "- cron: '39 * * * *'" in writer, "WRITER_TRIGGER_DRIFT")
    _require("jobs:\n  public-paper:" in writer and
             writer.count("python -m paper_pov.scanner") == 1,
             "WRITER_ENTRYPOINT_DRIFT")
    _require(re.search(r"(?m)^  group: " + MUTEX + r"$", writer) is not None and
             "cancel-in-progress: false" in writer, "WRITER_MUTEX_DRIFT")
    for name, source in (("CADENCE", cadence), ("RECOVERY", recovery)):
        _require("group: " + CONTROLLER_MUTEX in source and
                 "cancel-in-progress: false" in source and
                 "actions: write" in source and
                 "paper-pipeline.yml/dispatches" in source and
                 "paper_pov.scanner" not in source,
                 name + "_CONTROLLER_DRIFT")
    for name, source, command in (
        ("CADENCE", cadence, "/paper-cadence-heartbeat"),
        ("EXTERNAL", external, "/paper-recovery-heartbeat")):
        _require("on:\n  issue_comment:" in source and
                 "github.event.comment.user.id == 336805669" in source and
                 "github.event.comment.body == '" + command + "'" in source and
                 "paper_pov.scanner" not in source and
                 "\n  schedule:" not in source,
                 name + "_OWNER_EVENT_DRIFT")
    _require("workflow_id = 'paper-recovery.yml'" in external and
             "actions: write" in external and
             "cancel-in-progress: false" in external and
             "ref: 'main'" in external, "EXTERNAL_RECOVERY_TARGET_DRIFT")
    return {"source_contracts": "VERIFIED_FOR_SUPPLIED_EXACT_CHECKOUT",
            "single_writer": WRITER, "writer_mutex": MUTEX,
            "controller_mutex": CONTROLLER_MUTEX,
            "independent_event": "OWNER_AUTHENTICATED_ISSUE_COMMENT",
            "github_native_schedule_guaranteed": False,
            "durable_slot_cas_proven": False}


def checkout_contracts(root):
    root = Path(root)
    names = ("paper-pipeline.yml", "paper-cadence-wake.yml",
             "paper-recovery.yml", "paper-external-heartbeat.yml")
    return validate_workflows({
        n: (root / ".github" / "workflows" / n).read_text(encoding="utf-8")
        for n in names
    })


def rehearse(*, event, repository, actor, ref, event_name, now,
             checkout_sha, main_sha, sources, runs_payload, comments,
             ledger, ledger_commit, ledger_message):
    """Execute real authorization and decision logic without any write path.

    Inputs must come from independently authenticated GitHub GETs for a live
    operational acceptance. Passing supplied fixtures is NOT live proof.
    """
    result = {"schema": 1, "mode": "NONPRODUCTION_DRY_RUN",
              "dispatch_executed": False, "ledger_written": False,
              "scanner_executed": False, "native_schedule_claimed": False,
              "production_authorized": False, "durable_slot_cas_proven": False,
              "action": "BLOCKED", "reason": "UNVERIFIED"}
    try:
        _require(isinstance(now, dt.datetime) and now.tzinfo is not None,
                 "INVALID_CLOCK")
        _require(repository == REPO and isinstance(main_sha, str) and
                 SHA.fullmatch(main_sha) is not None and
                 checkout_sha == main_sha, "EXACT_MAIN_SOURCE_MISMATCH")
        result["source_sha"] = main_sha
        result["contracts"] = validate_workflows(sources)
        intent = authorize(event, repository=repository, actor=actor,
                           ref=ref, event_name=event_name, now=now)
        decision = decide(runs_payload, comments, ledger, ledger_commit,
                          ledger_message, main_sha, intent, now)
        _require(isinstance(decision, dict) and
                 decision.get("action") in
                 ("BLOCKED", "NO_DISPATCH", "DISPATCH_EXISTING_WORKFLOW"),
                 "UNTRUSTED_CONTROLLER_DECISION")
        result["controller_action"] = decision["action"]
        result["controller_reason"] = decision.get("reason")
        result["target_slot"] = decision.get("target_slot")
        result["ledger_generation"] = decision.get("ledger_generation")
        result["anchor_run_id"] = decision.get("anchor_run_id")
        if decision["action"] == "DISPATCH_EXISTING_WORKFLOW":
            _require(decision.get("source_sha") == main_sha and
                     isinstance(decision.get("attempt_marker"), str) and
                     decision["attempt_marker"].startswith("PAPER_CADENCE_ATTEMPT:"),
                     "UNBOUND_CANDIDATE_SOURCE_OR_MARKER")
            result["action"] = "DRY_RUN_CANDIDATE_ONLY"
            result["reason"] = "DURABLE_SLOT_CAS_AND_AUDIT_NOT_CERTIFIED"
            result["proposed_target"] = WRITER
        else:
            result["action"] = "NO_DISPATCH" if decision["action"] == "NO_DISPATCH" else "BLOCKED"
            result["reason"] = decision.get("reason", "CONTROLLER_ABSTAINED")
    except (ValueError, KeyError, TypeError, AttributeError, OverflowError, OSError) as exc:
        result["action"] = "BLOCKED"
        result["reason"] = str(exc)[:120]
    return result
