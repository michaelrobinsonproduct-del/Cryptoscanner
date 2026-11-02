"""Freeze a finite, source-bound audit decision; never certify a live scanner."""
import json
import pathlib

VALID = {"integrated", "superseded", "needed", "conflicting", "unknown"}
RISK = {
    4: ("credential-backed Supabase PATCH/POST", "production_activation", "legacy_deletion"),
    7: ("branch-pinned legacy source consumer", "production_activation", "legacy_deletion"),
    33: ("additional simple-history writer", "production_activation", "legacy_deletion"),
    40: ("raw-ledger verifier lacks segmented replay", "production_activation", "legacy_deletion"),
}
REPAIRS = (
    {"scope": "isolated_read_only_integration", "owner": "B/V",
     "condition": "Current combined draft must be GET-only and exact-head tested",
     "acceptance": "Independent V no-write review and B concurrence at exact current head; no merge"},
    {"scope": "production_activation", "owner": "D/B/V",
     "condition": "Native/manual cadence, writer/credential isolation, source freshness and delivery unverified",
     "acceptance": "Repeated authenticated real runs, SHA256 remote readback, manual parity and one-writer proof"},
    {"scope": "legacy_deletion", "owner": "C/V",
     "condition": "Branch-pinned history and deployed iOS/Bun/Railway/Supabase/pg_cron consumers unknown",
     "acceptance": "New authorized read-only deployed-consumer and scheduler attestation; no deletion until proven"},
    {"scope": "full_certification", "owner": "C/B/V",
     "condition": "Source-bound PR semantics and production/runtime evidence remain incomplete",
     "acceptance": "B concurs and independent V rules on this exact SHA-bound decision, with P/L restrictions"},
)

def freeze(inventory, semantic, bounded, gate, graph, writes, runtime):
    """All inputs come from one audit CI checkout. Contradictory identities fail closed."""
    main, ledger, checkout = (inventory.get(k) for k in ("main_sha", "ledger_sha", "checkout_sha"))
    for k, v in (("main", main), ("ledger", ledger), ("checkout", checkout)):
        if not isinstance(v, str) or len(v) != 40 or any(c not in "0123456789abcdef" for c in v):
            raise ValueError("Invalid " + k + " SHA")
    if (semantic.get("main_sha") != main or bounded.get("main_sha") != main or
        gate.get("main_sha") != main or graph.get("remote_main_sha") != main or
        writes.get("remote_main_sha") != main or
        bounded.get("ledger_sha_read_only") != ledger or gate.get("ledger_sha_read_only") != ledger or
        bounded.get("audit_checkout_sha") != checkout or graph.get("audit_checkout_sha") != checkout):
        raise ValueError("Cross-artifact source/ledger identity mismatch")
    if (gate.get("status") != "NOT_CERTIFIED" or not isinstance(gate.get("blockers"), list) or
        gate.get("cleanup_authorized") is not False or gate.get("production_mutation_authorized") is not False):
        raise ValueError("Unexpected authorization or certification claim")
    if runtime.get("current_main_sha") != main:
        raise ValueError("External runtime assessment main identity mismatch")
    if runtime.get("runtime_coverage_certified") is not False or runtime.get("cleanup_authorized") is not False:
        raise ValueError("External snapshot cannot certify deployed consumers")
    live = inventory.get("open_prs", [])
    rows = semantic.get("prs", [])
    if not isinstance(live, list) or not isinstance(rows, list):
        raise ValueError("Missing current PR rows")
    live_by_id = {p["number"]: p for p in live}
    reviewed_by_id = {p["number"]: p for p in rows}
    if (len(live_by_id) != len(live) or len(reviewed_by_id) != len(rows) or
        set(live_by_id) != set(reviewed_by_id) or semantic.get("open_pr_count") != len(live)):
        raise ValueError("Incomplete or duplicate PR census")
    if not isinstance(bounded.get("source_cases"), list) or not isinstance(graph.get("unknowns"), list):
        raise ValueError("Missing bounded source or consumer evidence")
    cases = bounded["source_cases"]
    if {x["pr"] for x in cases} != {4, 7, 33, 40}:
        raise ValueError("Expected risk source cases absent")
    source_status = {str(x["pr"]) + ":" + x["path"]: x["source"]["status"] for x in cases}
    main_writer = bounded.get("main_legacy_writer", {})
    if main_writer.get("main_sha") != main:
        raise ValueError("Main legacy writer not bound to current main")
    source_status["main:" + main_writer["path"]] = main_writer["source"]["status"]
    records = []
    for number in sorted(live_by_id):
        live_row, review = live_by_id[number], reviewed_by_id[number]
        if review.get("head_sha") != live_row.get("head_sha"):
            raise ValueError("Semantic decision uses a different PR head: " + str(number))
        valid = review.get("review_valid") is True and review.get("classification") in VALID
        disposition = review["classification"] if valid else "unknown"
        if disposition == "unknown":
            valid = False
        risk = RISK.get(number)
        records.append({
            "number": number, "head_sha": live_row["head_sha"],
            "disposition": disposition, "semantic_evidence_current": valid,
            "source_path": review.get("source_path"), "source_blob_sha": review.get("source_blob_sha"),
            "reason": review.get("reason"),
            "restrictions": list(risk[1:]) if risk else [],
            "risk": risk[0] if risk else None,
            "next_check": ("Independent exact-head semantic review" if not valid else
                           "Preserve restrictions until independently cleared"),
        })
    unresolved = [x["number"] for x in records if not x["semantic_evidence_current"]]
    source_failures = sorted(k for k, v in source_status.items() if v != "VERIFIED_EXACT_HEAD_SOURCE")
    if gate.get("unresolved_pr_count") != len(unresolved):
        raise ValueError("Gate and semantic unresolved counts disagree")
    if gate.get("unknown_consumer_count") != len(graph["unknowns"]):
        raise ValueError("Gate and consumer counts disagree")
    if gate.get("unknown_write_destination_count") != len(writes.get("unknown_write_destinations", [])):
        raise ValueError("Gate and write destination counts disagree")
    return {
        "schema": "cryptoscanner-finite-scope-decision-v1",
        "source": {"main_sha": main, "ledger_sha": ledger, "audit_checkout_sha": checkout},
        "full_audit": "NOT_CERTIFIED",
        "scope_decisions": {
            "isolated_read_only_integration": "CONDITIONAL_PREPARE_TEST_ONLY",
            "production_activation": "BLOCKED",
            "legacy_deletion": "BLOCKED",
        },
        "pr_count": len(records), "prs": records, "unresolved_semantic_prs": unresolved,
        "source_cases": source_status, "unverified_source_cases": source_failures,
        "unknown_consumer_count": len(graph["unknowns"]),
        "unknown_write_destinations": sorted(writes["unknown_write_destinations"]),
        "external_runtime_evidence": "SNAPSHOT_ONLY_NOT_INVOCATION_PROOF",
        "main_legacy_writer_execution_proven": False,
        "finite_repairs": list(REPAIRS),
        "b_v_current_head_signoff": "REQUIRED_NOT_INFERRED",
        "cleanup_authorized": False, "production_mutation_authorized": False,
    }

def main():
    root = pathlib.Path("audit-evidence")
    def load(name):
        return json.loads((root / name).read_text())
    result = freeze(load("scanner-inventory.json"), load("semantic-pr-matrix.json"),
                    load("bounded-source-audit.json"), load("audit-certification-gate.json"),
                    load("consumer-graph.json"), load("declared-write-surfaces.json"),
                    load("external-runtime-assessment.json"))
    (root / "finite-scope-decision.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("FINITE_SCOPE_DECISION", result["full_audit"], "PR", result["pr_count"],
          "UNRESOLVED", len(result["unresolved_semantic_prs"]),
          "SOURCE_UNVERIFIED", len(result["unverified_source_cases"]))

if __name__ == "__main__":
    main()
