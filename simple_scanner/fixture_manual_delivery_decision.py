"""Fixture-only Batch 30 manual delivery decision, NOT imported by execute_once.

Never resend an ambiguous POST or acknowledge a request as delivered merely
because its scan completed. A durable outbox entry is a prerequisite.
"""
from . import fixture_delivery_outbox as outbox

def classify_delivery(root, requests, delivered, run_id, receipt):
    """Return offline delivery/acknowledgement decisions without side effects beyond staging.

    Staging happens before a simulated POST. No network calls or ledger writes.
    """
    if not isinstance(requests,list) or not isinstance(delivered,list):
        raise ValueError("Invalid request collections")
    requested={}
    for item in requests:
        if not isinstance(item,dict) or type(item.get("issue_number")) is not int or item["issue_number"]<=0:
            raise ValueError("Invalid manual request")
        number=item["issue_number"]
        if number in requested:
            raise ValueError("Duplicate manual request")
        requested[number]=item
    delivered_ids=[]
    for item in delivered:
        if not isinstance(item,dict) or type(item.get("issue_number")) is not int:
            raise ValueError("Invalid delivery evidence")
        number=item["issue_number"]
        if number not in requested or number in delivered_ids:
            raise ValueError("Unmatched or duplicate delivery")
        delivered_ids.append(number)
    # The real publish_results returns issue dictionaries, not confirmed comment
    # IDs. Such results are insufficient proof for durable DELIVERED status.
    for number in requested:
        outbox.stage(root,number,run_id,receipt)
    return {
        "scan_satisfied_issue_numbers":sorted(requested),
        "delivery_reported_issue_numbers":sorted(delivered_ids),
        "confirmed_delivery_issue_numbers":[],
        "pending_reconciliation_issue_numbers":sorted(requested),
        "safe_to_repost_issue_numbers":[],
        "safe_to_acknowledge_as_delivered_issue_numbers":[],
        "status":"RECONCILIATION_REQUIRED" if requested else "NO_REQUESTS",
    }
