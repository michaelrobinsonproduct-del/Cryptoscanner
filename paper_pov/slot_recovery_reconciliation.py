"""Offline-only reconciliation of claimed PAPER recovery slots. No API/dispatch/write."""
import json
from .slot_claim_protocol import valid_plan, SHA40, SHA64


def _result(status, reason, run_id=None, published=False, received=False):
    return dict(status=status, reason=reason, linked_run_id=run_id,
                github_publication_verified=published, user_receipt_verified=received,
                native_schedule_proven=False, global_writer_exclusivity_proven=False,
                retry_authorized=False, dispatch_executed=False, ledger_written=False)


def reconcile(claim, *, tag_ref_sha, tag, runs, receipts, ledger, delivery=None):
    """Classify independently authenticated bounded evidence; NEVER authorize retry.

    The caller must verify API provenance, complete candidate-run coverage and
    capture-time bounds. An 'authenticated' fixture is NOT live source proof.
    """
    if not valid_plan(claim):
        return _result("BLOCKED", "INVALID_CLAIM")
    if not isinstance(tag_ref_sha, str) or not SHA40.fullmatch(tag_ref_sha):
        return _result("UNVERIFIED", "CLAIM_REF_NOT_AUTHENTICATED")
    if not isinstance(tag, dict) or tag.get("authenticated") is not True or (
        tag.get("sha") != tag_ref_sha or tag.get("name") != claim["tag_name"] or
        tag.get("target_sha") != claim["target_sha"] or
        tag.get("message") != claim["message"]
    ):
        return _result("FAILED", "CLAIM_REF_OR_TAG_MISMATCH")
    if not isinstance(runs, list) or not isinstance(receipts, list) or not isinstance(ledger, dict):
        return _result("UNVERIFIED", "INCOMPLETE_EVIDENCE")
    if any(not isinstance(x, dict) for x in runs + receipts):
        return _result("UNVERIFIED", "MALFORMED_RUN_OR_RECEIPT")
    record = json.loads(claim["message"].splitlines()[1])
    relevant = [r for r in receipts if r.get("claim_digest") == claim["digest"]]
    if not relevant:
        return _result("UNVERIFIED", "CLAIMED_WITHOUT_DISPATCH_RECEIPT")
    if any(r.get("authenticated") is not True or
           r.get("slot_utc") != claim["slot_utc"] or
           r.get("source_sha") != claim["source_sha"] or
           r.get("controller_run_id") != record["controller_run_id"] or
           r.get("origin") != "external_owner_recovery" or
           type(r.get("run_id")) is not int or r["run_id"] <= 0 for r in relevant):
        return _result("FAILED", "CONFLICTING_OR_UNAUTHENTICATED_RECEIPT")
    if len(relevant) != 1:
        return _result("FAILED", "MULTIPLE_DISPATCH_RECEIPTS")
    run_id = relevant[0]["run_id"]
    same_slot = [r for r in runs if r.get("slot_utc") == claim["slot_utc"]]
    if len(same_slot) > 1:
        return _result("FAILED", "MULTIPLE_WRITER_RUNS_FOR_SLOT")
    linked = [r for r in runs if r.get("id") == run_id]
    if len(linked) != 1:
        return _result("UNVERIFIED", "LINKED_RUN_MISSING_OR_AMBIGUOUS", run_id)
    run = linked[0]
    if run.get("authenticated") is not True or (
        run.get("workflow") != "paper-pipeline.yml" or
        run.get("event") != "workflow_dispatch" or
        run.get("head_sha") != claim["source_sha"] or
        run.get("run_attempt") != 1 or
        run.get("slot_utc") != claim["slot_utc"]
    ):
        return _result("FAILED", "WRITER_RUN_ORIGIN_MISMATCH", run_id)
    if run.get("status") != "completed" or run.get("conclusion") != "success":
        return _result("UNVERIFIED", "WRITER_NOT_SUCCESSFULLY_COMPLETED", run_id)
    if ledger.get("authenticated") is not True or ledger.get("remote_readback") is not True or (
        ledger.get("source_sha") != claim["source_sha"] or
        ledger.get("run_id") != run_id or
        ledger.get("claim_digest") != claim["digest"] or
        type(ledger.get("generation")) is not int or ledger["generation"] < 1 or
        not isinstance(ledger.get("sha256"), str) or
        not SHA64.fullmatch(ledger["sha256"]) or
        not isinstance(ledger.get("scan_id"), str) or not ledger["scan_id"]
    ):
        return _result("UNVERIFIED", "CANONICAL_LEDGER_LINK_NOT_PROVEN", run_id)
    if not isinstance(delivery, dict) or delivery.get("authenticated") is not True or (
        delivery.get("run_id") != run_id or delivery.get("published") is not True
    ):
        return _result("UNVERIFIED", "RESULTS_PUBLICATION_NOT_PROVEN", run_id)
    return _result("RECONCILED", "BOUNDED_LINKAGE_ONLY_NOT_GLOBAL_EXCLUSIVITY",
                   run_id, published=True, received=delivery.get("user_receipt") is True)
