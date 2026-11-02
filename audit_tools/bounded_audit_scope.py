"""Bounded, source-bound audit findings. GET-only, never authorizes deployment/deletion."""
import base64
import datetime
import hashlib
import json
import os
import pathlib
import re
import subprocess

REPO = "michaelrobinsonproduct-del/Cryptoscanner"
CASES = (
    {"pr": 7, "path": "simple_scanner/scan.py",
     "sha": "25539447cb9fb2b1d83dcc04fcc595e5fd9e38af",
     "kind": "LEGACY_BRANCH_CONSUMER", "require": ("SIMPLE_SCANNER_DATA_DIR", "market_prices"),
     "block_production": True, "block_deletion": True},
    {"pr": 4, "path": "evaluation/measure-forward.ts",
     "sha": "637c33daa01335163a29d2d0b3c41bd055f9a3fc",
     "kind": "CREDENTIAL_BACKED_EXTERNAL_WRITE", "require": ("CHALLENGER_SUPABASE_SERVICE_KEY", 'method:"PATCH"'),
     "block_production": True, "block_deletion": True},
    {"pr": 4, "path": "evaluation/shadow-cycle.ts",
     "sha": "09a6e90954a9d6462b57b382e28d119e00a0d85e",
     "kind": "CREDENTIAL_BACKED_EXTERNAL_WRITE", "require": ("CHALLENGER_SUPABASE_SERVICE_KEY", 'method:"POST"'),
     "block_production": True, "block_deletion": True},
    {"pr": 33, "path": ".github/workflows/kraken-simple.yml",
     "sha": "627719697f7a20758b420fd07b8fc4f31b4ed99d",
     "kind": "ADDITIONAL_LEGACY_HISTORY_WRITER", "require": ("contents: write", "refs/heads/simple-history", "workflow_dispatch:"),
     "block_production": True, "block_deletion": True},
    {"pr": 40, "path": ".github/workflows/paper-forward-audit.yml",
     "sha": "4a3ab29767d3fda365de5a085607868238194d84",
     "kind": "RAW_LEDGER_ONLY_VERIFIER", "require": ("paper-ledger.json", "git show"),
     "forbid": ("paper-segment-manifest.json", "paper-segments/"),
     "block_production": True, "block_deletion": True},
)
SCOPE = {
    "isolated_read_only_integration": "PREPARE_AND_TEST_ONLY_PENDING_B_V",
    "production_activation": "BLOCKED",
    "legacy_deletion": "BLOCKED",
}

def git_blob_sha(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def source_identity(case, pr_row, payload):
    """Verify GitHub Contents GET at exact PR head, including raw bytes and blob identity."""
    if not pr_row or not re.fullmatch(r"[0-9a-f]{40}", str(pr_row.get("head_sha", ""))):
        return {"status": "MISSING_OR_INVALID_PR_HEAD"}
    if pr_row["head_sha"] != case["expected_head_sha"]:
        return {"status": "PR_HEAD_DRIFT", "actual_head_sha": pr_row["head_sha"]}
    if not isinstance(payload, dict) or payload.get("encoding") != "base64":
        return {"status": "UNVERIFIED_SOURCE_RESPONSE"}
    try:
        encoded = payload["content"]
        if not isinstance(encoded, str):
            return {"status": "UNVERIFIED_SOURCE_BYTES"}
        # GitHub Contents wraps base64 with CR/LF; reject all other invalid bytes.
        raw = base64.b64decode(encoded.replace("\n", "").replace("\r", ""), validate=True)
        content = raw.decode("utf-8")
    except (KeyError, ValueError, UnicodeError, TypeError, base64.binascii.Error):
        return {"status": "UNVERIFIED_SOURCE_BYTES"}
    calculated = git_blob_sha(raw)
    if payload.get("sha") != calculated or calculated != case["sha"]:
        return {"status": "SOURCE_BLOB_MISMATCH", "calculated_sha": calculated,
                "github_contents_sha": payload.get("sha")}
    required = case.get("require", ())
    forbidden = case.get("forbid", ())
    if not all(token in content for token in required) or any(token in content for token in forbidden):
        return {"status": "SOURCE_CONTRACT_MISMATCH", "calculated_sha": calculated}
    file_row = next((r for r in pr_row.get("file_blob_comparisons", [])
                     if r.get("path") == case["path"]), None)
    pr_files_sha = file_row.get("pr_blob_sha") if file_row else None
    return {"status": "VERIFIED_EXACT_HEAD_SOURCE", "calculated_sha": calculated,
            "github_contents_sha": payload["sha"],
            "pr_files_api_sha": pr_files_sha,
            "pr_files_api_status": ("MISSING" if pr_files_sha is None else
                                    "MATCH" if pr_files_sha == calculated else "MISMATCH"),
            "pr_files_api_discrepancy": pr_files_sha is not None and pr_files_sha != calculated}

def assess(inventory, responses):
    """Produce finite scope restrictions; no unknown consumer is deemed safe to delete."""
    rows = {p["number"]: p for p in inventory["open_prs"]}
    cases = []
    for original in CASES:
        c = dict(original)
        row = rows.get(c["pr"])
        c["head_sha"] = row.get("head_sha") if row else None
        c["expected_head_sha"] = original["expected_head_sha"]
        identity = source_identity(c, row, responses.get((c["pr"], c["path"])))
        cases.append({"pr": c["pr"], "path": c["path"], "head_sha": c["head_sha"],
                      "expected_head_sha": c["expected_head_sha"], "expected_blob_sha": c["sha"],
                      "kind": c["kind"], "source": identity,
                      "blocks": {"isolated_read_only_integration": False,
                                 "production_activation": c["block_production"],
                                 "legacy_deletion": c["block_deletion"]},
                      "restriction": "No workflow execution, external credential use, production activation or deletion from this audit; isolate read-only tests only."})
    verified = sum(x["source"]["status"] == "VERIFIED_EXACT_HEAD_SOURCE" for x in cases)
    return {"schema": "cryptoscanner-bounded-source-audit-v1",
            "main_sha": inventory["main_sha"], "ledger_sha_read_only": inventory["ledger_sha"],
            "audit_checkout_sha": inventory["checkout_sha"],
            "source_cases": cases, "source_verified": verified,
            "source_total": len(cases), "source_discrepancies":
                [x["pr"] for x in cases if x["source"].get("pr_files_api_discrepancy")],
            "scopes": SCOPE,
            "independent_b_v_concurrence": "REQUIRED_NOT_INFERRED",
            "full_audit_certified": False, "cleanup_authorized": False,
            "production_mutation_authorized": False,
            "finite_blockers": [
                {"scope": "isolated_read_only_integration", "owner": "B/V",
                 "condition": "Exact-head combined draft with GET-only tests and explicit independent B/V concurrence; no merge"},
                {"scope": "production_activation", "owner": "D/B/V",
                 "condition": "Actual native/manual writer proof, single-writer isolation, credential write-surface and runtime consumer attestation"},
                {"scope": "legacy_deletion", "owner": "C/V",
                 "condition": "Deployed iOS/Bun/Supabase/pg_cron and branch-pinned history consumers independently resolved"},
            ]}

def github_get_contents(pr, path, head):
    if not re.fullmatch(r"[0-9a-f]{40}", str(head)):
        raise ValueError("Invalid exact PR head")
    target = "repos/" + REPO + "/contents/" + path + "?ref=" + head
    p = subprocess.run(["gh", "api", target], capture_output=True, text=True, timeout=30)
    if p.returncode:
        return {"error": "GITHUB_READ_FAILED", "stderr": p.stderr[:200]}
    try:
        return json.loads(p.stdout)
    except json.JSONDecodeError:
        return {"error": "INVALID_GITHUB_JSON"}

def main():
    path = pathlib.Path("audit-evidence/scanner-inventory.json")
    inventory = json.loads(path.read_text())
    current = {p["number"]: p for p in inventory["open_prs"]}
    responses = {}
    for c in CASES:
        row = current.get(c["pr"])
        if row and row.get("head_sha") == c["expected_head_sha"]:
            responses[(c["pr"], c["path"])] = github_get_contents(c["pr"], c["path"], row["head_sha"])
    result = assess(inventory, responses)
    pathlib.Path("audit-evidence/bounded-source-audit.json").write_text(
        json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("BOUNDED_SOURCE_AUDIT", result["source_verified"], result["source_total"],
          "PR_FILES_API_DISCREPANCIES", result["source_discrepancies"])
    print("SCOPE", json.dumps(result["scopes"], sort_keys=True))
    # A source drift is a finite evidence blocker, not a reason to mutate the live scanner.
    if result["source_verified"] != result["source_total"]:
        print("SOURCE_VERIFICATION_INCOMPLETE: fail closed; no certification")

# Pinned source heads are evidence checkpoints, not guessed from stale snapshots.
for _case in CASES:
    _case["expected_head_sha"] = {
        7: "940a4af9d976fb271c7534ad3e3e9eae33c376cf",
        4: "7284645c1dbeb21c67fb07dc23200770500475d3",
        33: "3a58194ec9c11649111f29450c5e28e3585c0068",
        40: "9c66e45b2a7d674e60fc47c761d44788f9bb15c5",
    }[_case["pr"]]

if __name__ == "__main__":
    main()
