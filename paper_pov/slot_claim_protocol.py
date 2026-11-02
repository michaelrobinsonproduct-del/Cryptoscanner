"""Nonproduction GitHub annotated-tag slot-CAS contract; NO network or dispatch.

Future authorized controller adapter can implement GitHub's create-tag/create-ref/
get-ref/get-tag endpoints. A unique tag ref is an atomic cooperative claim,
NOT a guarantee of GitHub cron delivery, global writer exclusion or exactly-once
execution. Any uncertain GitHub response blocks; a claimed-but-undispatched
slot requires human reconciliation rather than an automatic retry.
"""
import datetime as dt
import hashlib
import json
import re

UTC = dt.timezone.utc
SHA40 = re.compile(r"[0-9a-f]{40}\Z")
SHA64 = re.compile(r"[0-9a-f]{64}\Z")
NAMESPACE = "refs/tags/paper-recovery-slot-v1/"
OWNER_ID = 336805669
ORIGIN = "external_owner_recovery"


def _check(ok, reason):
    if not ok:
        raise ValueError(reason)


def prepare(*, slot, now, source_sha, main_sha, ledger_commit,
            decision_sha256, controller_run_id, owner_comment_id,
            owner_id, origin=ORIGIN):
    """Prepare immutable tag payload; does not touch GitHub or invoke a writer."""
    _check(isinstance(slot, dt.datetime) and slot.tzinfo is not None and
           isinstance(now, dt.datetime) and now.tzinfo is not None, "NAIVE_CLOCK")
    slot, now = slot.astimezone(UTC), now.astimezone(UTC)
    _check(slot.minute in (0, 30) and slot.second == 0 and
           slot.microsecond == 0, "INVALID_UTC_HALF_HOUR_SLOT")
    _check(dt.timedelta(0) <= now - slot <= dt.timedelta(minutes=29),
           "SLOT_OUTSIDE_BOUNDED_RECOVERY_WINDOW")
    _check(isinstance(source_sha, str) and SHA40.fullmatch(source_sha) and
           source_sha == main_sha and isinstance(ledger_commit, str) and
           SHA40.fullmatch(ledger_commit), "UNAUTHENTICATED_SOURCE_OR_LEDGER")
    _check(isinstance(decision_sha256, str) and SHA64.fullmatch(decision_sha256),
           "INVALID_DECISION_DIGEST")
    _check(type(controller_run_id) is int and controller_run_id > 0 and
           type(owner_comment_id) is int and owner_comment_id > 0 and
           type(owner_id) is int and owner_id == OWNER_ID and
           origin == ORIGIN, "INVALID_OWNER_OR_CONTROLLER_ORIGIN")
    record = {"schema": 1, "slot_utc": slot.isoformat(),
              "source_sha": source_sha, "ledger_commit": ledger_commit,
              "decision_sha256": decision_sha256,
              "controller_run_id": controller_run_id,
              "owner_comment_id": owner_comment_id,
              "owner_id": owner_id, "origin": ORIGIN,
              "target_workflow": "paper-pipeline.yml",
              "native_schedule": False}
    canonical = json.dumps(record, sort_keys=True, separators=(",", ":"),
                           allow_nan=False)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return {"ref": NAMESPACE + slot.strftime("%Y%m%dT%H%MZ"),
            "tag_name": "paper-recovery-slot-v1-" + slot.strftime("%Y%m%dT%H%MZ"),
            "target_sha": source_sha,
            "message": "PAPER_RECOVERY_SLOT_CLAIM_V1\n" + canonical +
                       "\nSHA256=" + digest + "\n",
            "digest": digest, "slot_utc": slot.isoformat(),
            "source_sha": source_sha}


def valid_plan(claim):
    """Reject forged/incomplete plan before even reading a GitHub ref."""
    try:
        if not isinstance(claim, dict):
            return False
        required = ("ref", "tag_name", "target_sha", "message", "digest",
                    "slot_utc", "source_sha")
        if any(not isinstance(claim.get(k), str) for k in required):
            return False
        lines = claim["message"].splitlines()
        if len(lines) != 3 or lines[0] != "PAPER_RECOVERY_SLOT_CLAIM_V1":
            return False
        record = json.loads(lines[1])
        if not isinstance(record, dict) or json.dumps(
            record, sort_keys=True, separators=(",", ":"), allow_nan=False
        ) != lines[1]:
            return False
        digest = hashlib.sha256(lines[1].encode("utf-8")).hexdigest()
        slot = dt.datetime.fromisoformat(record["slot_utc"])
        if slot.tzinfo is None or slot.utcoffset() != dt.timedelta(0) or (
            slot.minute not in (0, 30) or slot.second or slot.microsecond
        ):
            return False
        suffix = slot.strftime("%Y%m%dT%H%MZ")
        return (
            claim["message"].endswith("\n") and
            claim["ref"] == NAMESPACE + suffix and
            claim["tag_name"] == "paper-recovery-slot-v1-" + suffix and
            claim["slot_utc"] == slot.isoformat() and
            claim["source_sha"] == claim["target_sha"] ==
            record["source_sha"] and SHA40.fullmatch(record["source_sha"]) is not None and
            SHA40.fullmatch(record["ledger_commit"]) is not None and
            SHA64.fullmatch(record["decision_sha256"]) is not None and
            record["owner_id"] == OWNER_ID and
            type(record["controller_run_id"]) is int and record["controller_run_id"] > 0 and
            type(record["owner_comment_id"]) is int and record["owner_comment_id"] > 0 and
            record["origin"] == ORIGIN and record["target_workflow"] ==
            "paper-pipeline.yml" and record["native_schedule"] is False and
            lines[2] == "SHA256=" + digest and claim["digest"] == digest and
            set(record) == {"schema", "slot_utc", "source_sha", "ledger_commit",
                            "decision_sha256", "controller_run_id",
                            "owner_comment_id", "owner_id", "origin",
                            "target_workflow", "native_schedule"} and
            type(record["schema"]) is int and record["schema"] == 1
        )
    except (ValueError, TypeError, KeyError, AttributeError, OverflowError):
        return False


def attempt(api, claim):
    """Use injected GitHub Git-data adapter. NEVER dispatch, retry or write ledger.

    Required adapter methods: create_tag(tag_name,target_sha,message)->sha;
    create_ref(ref,sha); get_ref(ref)->sha or None; get_tag(sha)->dict
    with name,target_sha,message. All errors fail closed, including HTTP 422,
    timeout and ambiguous success. The adapter is NOT instantiated here.
    """
    result = {"status": "BLOCKED", "reason": "UNVERIFIED",
              "dispatch_executed": False, "scanner_executed": False,
              "ledger_written": False, "native_schedule_claimed": False,
              "global_writer_exclusivity_proven": False}
    if not valid_plan(claim):
        result["reason"] = "INVALID_CLAIM"
        return result
    try:
        existing = api.get_ref(claim["ref"])
        if existing is not None:
            result["reason"] = "SLOT_REF_ALREADY_EXISTS"
            return result
        tag_sha = api.create_tag(claim["tag_name"], claim["target_sha"],
                                 claim["message"])
        if not isinstance(tag_sha, str) or SHA40.fullmatch(tag_sha) is None:
            result["reason"] = "INVALID_TAG_SHA"
            return result
        api.create_ref(claim["ref"], tag_sha)
        actual_sha = api.get_ref(claim["ref"])
        tag = api.get_tag(actual_sha)
        if (actual_sha != tag_sha or not isinstance(tag, dict) or
            tag.get("name") != claim["tag_name"] or
            tag.get("target_sha") != claim["target_sha"] or
            tag.get("message") != claim["message"]):
            result["reason"] = "CLAIM_READBACK_MISMATCH"
            return result
        result.update(status="CLAIMED_NOT_DISPATCHED",
                      reason="AUDIT_AND_DISPATCH_AUTHORIZATION_REQUIRED",
                      claim_ref=claim["ref"], claim_tag_sha=tag_sha,
                      claim_digest=claim["digest"])
        return result
    except Exception:
        # A timeout after create_ref may have committed the claim. No retry.
        result["reason"] = "GITHUB_CLAIM_OUTCOME_UNCERTAIN_NO_RETRY"
        return result
