"""Offline-only GitHub comment evidence contract. Never calls GitHub.

Caller assertions about identity or complete pagination are NOT authentication.
They are an explicit input contract for a future independently verified adapter.
"""
from .fixture_receipt_reconciliation import marker

def authenticated_comment_ids(issue_number, run_id, digest, snapshot, expected_author):
    """Return matched comment IDs only for a complete, internally consistent fixture.

    Raises on ambiguous, incomplete, foreign or malformed evidence. An empty
    result is unresolved, not permission to POST or rerun a scan.
    """
    if not isinstance(expected_author,str) or not expected_author.strip():
        raise ValueError("Expected author required")
    if not isinstance(snapshot,dict) or snapshot.get("complete") is not True:
        raise ValueError("Complete pagination evidence required")
    if type(snapshot.get("issue_number")) is not int or snapshot["issue_number"]!=issue_number:
        raise ValueError("Issue binding mismatch")
    if not isinstance(snapshot.get("comments"),list):
        raise ValueError("Comment list required")
    token=marker(issue_number,run_id,digest)
    import re
    pattern=re.compile(r"(?<![A-Za-z0-9_])"+re.escape(token)+r"(?![A-Za-z0-9_])")
    seen=set()
    matched=[]
    for comment in snapshot["comments"]:
        if not isinstance(comment,dict):
            raise ValueError("Malformed comment")
        cid=comment.get("id")
        if type(cid) is not int or cid<=0 or cid in seen:
            raise ValueError("Invalid or repeated comment identity")
        seen.add(cid)
        if type(comment.get("issue_number")) is not int or comment["issue_number"]!=issue_number:
            raise ValueError("Foreign issue comment")
        if not isinstance(comment.get("author"),str) or not comment["author"]:
            raise ValueError("Comment author required")
        if not isinstance(comment.get("body"),str):
            raise ValueError("Comment body required")
        if pattern.search(comment["body"]):
            if comment["author"]!=expected_author:
                raise ValueError("Receipt marker from unexpected author")
            matched.append(cid)
    if len(matched)>1:
        raise ValueError("Ambiguous duplicate receipt confirmations")
    return matched
