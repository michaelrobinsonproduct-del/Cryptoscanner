"""Pure fail-closed acknowledgement policy for offline integration planning.

Safe to import from execute_once in a future reviewed change; this module
does not perform I/O, post comments, trigger scans, or acknowledge a ledger.
"""
def acknowledgement_decision(requested, confirmed):
    """Only confirmed, uniquely identified deliveries can be acknowledged.

    Confirmations must include a positive GitHub comment ID; a 201 response
    alone is not durable confirmation. This is a policy decision, not proof
    of authenticity or pagination completeness.
    """
    if not isinstance(requested,list) or not isinstance(confirmed,list):
        raise ValueError("Invalid request or confirmation list")
    requested_ids=set()
    for item in requested:
        if not isinstance(item,dict) or type(item.get("issue_number")) is not int or item["issue_number"]<=0:
            raise ValueError("Invalid request identity")
        if item["issue_number"] in requested_ids:
            raise ValueError("Duplicate request")
        requested_ids.add(item["issue_number"])
    confirmations={}
    comment_ids=set()
    for item in confirmed:
        if not isinstance(item,dict) or type(item.get("issue_number")) is not int or type(item.get("comment_id")) is not int:
            raise ValueError("Invalid confirmation identity")
        issue=item["issue_number"]
        comment=item["comment_id"]
        if issue not in requested_ids or comment<=0 or issue in confirmations or comment in comment_ids:
            raise ValueError("Duplicate, foreign or invalid confirmation")
        confirmations[issue]=comment
        comment_ids.add(comment)
    return {
        "acknowledge_issue_numbers":sorted(confirmations),
        "pending_issue_numbers":sorted(requested_ids-set(confirmations)),
        "safe_to_repost_issue_numbers":[],
        "scan_rerun_required":False,
        "status":"ALL_CONFIRMED" if requested_ids and len(confirmations)==len(requested_ids) else ("NO_REQUESTS" if not requested_ids else "RECONCILIATION_REQUIRED"),
    }

def plan_manual_delivery_transition(requests, confirmed_comments, outbox_entries):
    """Offline-only preflight for a future wrapper integration.

    Fail closed unless every requested issue has one matching durable DELIVERED
    outbox record with the same confirmed comment ID. Does not write ledger,
    call GitHub, rescan, or post; never treat HTTP 201 as confirmation.
    """
    decision=acknowledgement_decision(requests,confirmed_comments)
    if not isinstance(outbox_entries,list):
        raise ValueError("Durable outbox evidence required")
    entries={}
    for entry in outbox_entries:
        if not isinstance(entry,dict) or type(entry.get("issue_number")) is not int:
            raise ValueError("Invalid outbox entry")
        issue=entry["issue_number"]
        if issue in entries:
            raise ValueError("Duplicate outbox identity")
        entries[issue]=entry
    confirmed={item["issue_number"]:item["comment_id"] for item in confirmed_comments}
    for issue,comment_id in confirmed.items():
        entry=entries.get(issue)
        if (not entry or entry.get("status")!="DELIVERED"
                or type(entry.get("comment_id")) is not int
                or entry["comment_id"]!=comment_id
                or not isinstance(entry.get("run_id"),str) or not entry["run_id"]
                or not isinstance(entry.get("sha256"),str) or len(entry["sha256"])!=64):
            raise ValueError("Confirmed comment lacks matching durable delivered receipt")
    return decision
