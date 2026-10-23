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
