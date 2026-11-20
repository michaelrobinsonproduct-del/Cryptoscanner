"""Read-only learning receipt delivery contract.

The caller obtains GitHub run/job/artifact metadata and immutable canonical
publications using authenticated read-only access. This verifier does not
fetch, dispatch, promote, or write any production result.
"""
from .shadow_learning_evidence import canonical_digest, utc_time


def verify_learning_delivery(receipt, learning_run, owner_job, artifact,
                             source_publication, source_writer, delivered_publication):
    """Bind the exact completed main learning owner to its writer generation.

    The delivered publication must already have passed the normal scanner
    delivery checks. For a lagging receipt the source publication must be
    independently retrieved from its immutable ledger commit, not inferred
    from the latest generation. A checksum is not exchange authentication.
    """
    run_id = str(learning_run.get("id", ""))
    if (not run_id.isdigit() or learning_run.get("head_branch") != "main"
        or learning_run.get("event") != "workflow_dispatch"
        or owner_job.get("name") != "market-wide-shadow-learning"
        or str(owner_job.get("run_id")) != run_id
        or owner_job.get("head_sha") != learning_run.get("head_sha")
        or owner_job.get("status") != "completed"
        or owner_job.get("conclusion") != "success"):
        raise ValueError("Learning owner is not a successful main job")
    origin = artifact.get("workflow_run") or {}
    if (artifact.get("name") != "market-wide-learning-continuity-main-"+run_id
        or artifact.get("expired") is not False
        or str(origin.get("id")) != run_id
        or origin.get("head_branch") != "main"
        or origin.get("head_sha") != learning_run.get("head_sha")):
        raise ValueError("Learning artifact provenance mismatch")
    if (receipt.get("schema") != "market_wide_learning_receipt_v1"
        or receipt.get("learning_scope") != "main"
        or receipt.get("digest") != canonical_digest({k:v for k,v in receipt.items() if k!="digest"})
        or receipt.get("production_applied") is not False
        or receipt.get("promotion_authorized") is not False):
        raise ValueError("Invalid main learning receipt")
    if (source_publication.get("schema") != 2
        or source_publication.get("status") != "SUCCESS_PAPER_ONLY"
        or source_publication.get("publication_mode") != "ATOMIC_LEDGER_RESULTS"
        or source_publication.get("remote_readback_verified") is not True
        or source_publication.get("production_applied") is not False
        or source_publication.get("buy_approved") is not False
        or source_writer.get("status") != "completed"
        or source_writer.get("conclusion") != "success"
        or source_writer.get("head_branch") != "main"
        or str(source_writer.get("id")) != str(source_publication.get("run_id"))
        or source_writer.get("head_sha") != source_publication.get("source_sha")):
        raise ValueError("Learning source writer not verified")
    for a,b in (("writer_run_id","run_id"),("source_sha","source_sha"),
                ("ledger_generation","ledger_generation"),("ledger_sha256","ledger_sha256")):
        if str(receipt.get(a)) != str(source_publication.get(b)) or receipt.get(a) is None:
            raise ValueError("Learning receipt/writer provenance mismatch")
    if utc_time(receipt["evaluation_asof_utc"]) != utc_time(source_publication["as_of"]):
        raise ValueError("Learning receipt/writer timestamp mismatch")
    n,latest = receipt["ledger_generation"],delivered_publication["ledger_generation"]
    if type(n) is not int or type(latest) is not int or not 0<n<=latest:
        raise ValueError("Learning generation is outside delivered history")
    if n==latest:
        for key in ("run_id","source_sha","ledger_sha256"):
            if source_publication[key]!=delivered_publication[key]:
                raise ValueError("Equal-generation publication mismatch")
    elif utc_time(source_publication["as_of"])>=utc_time(delivered_publication["as_of"]):
        raise ValueError("Lagging learning timestamp is not older")
    return {"status":"CURRENT" if n==latest else "LAGGING",
            "learning_run_id":run_id,"learning_generation":n,
            "delivered_generation":latest,"generation_lag":latest-n,
            "evaluation_asof_utc":receipt["evaluation_asof_utc"],
            "receipt_digest":receipt["digest"],"receipt":receipt,
            "production_applied":False,"promotion_authorized":False}
