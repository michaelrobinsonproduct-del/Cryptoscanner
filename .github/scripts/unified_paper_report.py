"""Read-only GitHub Actions published-paper report collector. Never starts a scanner."""
import datetime as dt
import hashlib
import io
import json
import os
from pathlib import Path
import urllib.error
import urllib.request
import zipfile
from urllib.parse import urlsplit

REPO = os.environ.get("GITHUB_REPOSITORY", "michaelrobinsonproduct-del/Cryptoscanner")
TOKEN = os.environ["GH_TOKEN"]
API = "https://api.github.com/repos/" + REPO
UTC = dt.timezone.utc

class ArtifactRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        redirected = super().redirect_request(req, fp, code, msg, headers, newurl)
        if redirected is not None and urlsplit(newurl).netloc != urlsplit(req.full_url).netloc:
            redirected.remove_header("Authorization")
            redirected.unredirected_hdrs.pop("Authorization", None)
        return redirected

REDIRECT_OPENER = urllib.request.build_opener(ArtifactRedirect())

def api(path, binary=False):
    request = urllib.request.Request(
        API + path, headers={"Authorization": "Bearer " + TOKEN,
                             "Accept": "application/vnd.github+json",
                             "X-GitHub-Api-Version": "2022-11-28"})
    with REDIRECT_OPENER.open(request, timeout=45) as response:
        return response.read() if binary else json.load(response)

def files_from_zip(artifact):
    data = api("/actions/artifacts/" + str(artifact["id"]) + "/zip", binary=True)
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)) or any(n.startswith("/") or ".." in Path(n).parts for n in names):
            raise ValueError("Unsafe artifact ZIP")
        entries = {Path(n).name: archive.read(n) for n in names if not n.endswith("/")}
    sums = entries.get("SHA256SUMS") or entries.get("LEGACY_SHA256SUMS")
    if sums is None:
        raise ValueError("Missing artifact checksum manifest")
    for line in sums.decode().splitlines():
        digest, name = line.split(None, 1)
        key = Path(name.strip().lstrip("*")).name
        if key not in entries or hashlib.sha256(entries[key]).hexdigest() != digest:
            raise ValueError("Artifact checksum mismatch: " + key)
    return entries

def artifact_map(run_id):
    return {a["name"]: a for a in api("/actions/runs/" + str(run_id) + "/artifacts?per_page=100")["artifacts"] if not a["expired"]}

def utc(value):
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(UTC)

def latest_published():
    # Query the actual writer workflow, not a fixed cron slot. Includes workflow_dispatch.
    for page in range(1, 4):
        runs = api("/actions/workflows/paper-pipeline.yml/runs?per_page=100&page=" + str(page))["workflow_runs"]
        for run in runs:
            if run["status"] != "completed" or run["conclusion"] != "success" or run["head_branch"] != "main":
                continue
            artifacts = artifact_map(run["id"])
            results = artifacts.get("public-paper-results-" + str(run["id"]))
            ledger = artifacts.get("public-paper-ledger-" + str(run["id"]))
            if results and ledger:
                return run, results, ledger
        if len(runs) < 100:
            break
    raise ValueError("SCAN NOT VERIFIED: no successful published writer run with both artifacts in last 300 workflow runs")

def legacy_for(paper_run, source_sha):
    # Legacy is a separate workflow run; never interpret baseline score as independent discovery.
    for page in range(1, 4):
        runs = api("/actions/workflows/paper-legacy-shadow.yml/runs?per_page=100&page=" + str(page))["workflow_runs"]
        for run in runs:
            if (run["status"] != "completed" or run["conclusion"] != "success"
                    or run["id"] == paper_run or run.get("event") not in ("workflow_run", "issue_comment")):
                continue
            artifacts = artifact_map(run["id"])
            for name, artifact in artifacts.items():
                if not ("legacy" in name.lower() and "shadow" in name.lower()):
                    continue
                entries = files_from_zip(artifact)
                for key, raw in entries.items():
                    if key.endswith(".json"):
                        obj = json.loads(raw)
                        if (obj.get("trigger_paper_run_id") == str(paper_run)
                                and obj.get("source_sha") == source_sha
                                and obj.get("independent_execution") is True
                                and obj.get("mode") == "LEGACY_INSPIRED_SHADOW"):
                            return obj, artifact, run
        if len(runs) < 100:
            break
    return None, None, None

def main():
    run, results_art, ledger_art = latest_published()
    results_files = files_from_zip(results_art)
    ledger_files = files_from_zip(ledger_art)
    result = json.loads(results_files["results.json"])
    score = json.loads(ledger_files["scoreboard.json"])
    ledger = json.loads(ledger_files["ledger.json"])
    if (result["run_id"] != str(run["id"]) or result["source_sha"] != run["head_sha"]
            or result["ledger_generation"] != score["generation"]
            or result["ledger_sha256"] != score["ledger_sha256"]
            or result.get("remote_readback_verified") is not True
            or result.get("status") != "SUCCESS_PAPER_ONLY"):
        raise ValueError("SCAN NOT VERIFIED: source/ledger/report mismatch")
    # Recompute the canonical ledger seal through the existing verifier.
    from paper_pov.ledger import verify
    from paper_pov.segmented_storage import MAX_RAW_BYTES
    state = verify(ledger, MAX_RAW_BYTES)
    if state["generation"] != result["ledger_generation"] or state["sha256"] != result["ledger_sha256"]:
        raise ValueError("SCAN NOT VERIFIED: ledger SHA256 verification failed")
    candidates = sorted(result["candidates"], key=lambda x: -x["challenger_score"])
    as_of = utc(result["as_of"])
    quote_ages = [(as_of - utc(x["quote_observed_at"])).total_seconds() for x in candidates]
    age_now = (dt.datetime.now(UTC) - as_of).total_seconds() 
    fresh = (bool(quote_ages) and min(quote_ages) >= 0 and max(quote_ages) <= 600 
             and 0 <= age_now <= 600)
    legacy, legacy_art, legacy_run = legacy_for(run["id"], run["head_sha"])
    independent = sorted(legacy["candidates"], key=lambda x: -x["legacy_score"]) if legacy else []
    overlaps = sorted({x["symbol"] for x in candidates} & {x["symbol"] for x in independent}) if legacy else []
    output = {
        "schema": 1, "status": "PASS" if fresh else "STALE",
        "paper_run_id": run["id"], "paper_run_url": run["html_url"],
        "paper_results_artifact_id": results_art["id"], "ledger_artifact_id": ledger_art["id"],
        "source_sha": run["head_sha"], "as_of_utc": result["as_of"],
        "eligible_pairs": result["eligible_pairs"], "watch_count": len(candidates),
        "ledger_generation": result["ledger_generation"], "ledger_sha256": result["ledger_sha256"],
        "max_quote_age_seconds": max(quote_ages) if quote_ages else None, 
        "report_age_seconds": round(age_now, 2),
        "challenger_top5": candidates[:5], "legacy_independent": legacy is not None,
        "legacy_run_id": legacy_run["id"] if legacy_run else None,
        "legacy_artifact_id": legacy_art["id"] if legacy_art else None,
        "legacy_top5": independent[:5],
        "verified_independent_overlaps": overlaps,
        "matured_labels": result.get("matured_labels"),
        "horizons": result.get("horizons"),
        "held_out_lift": result.get("held_out_lift"),
        "production_applied": result.get("production_applied"),
        "missing_evidence": (["independent legacy results"] if not legacy else [])
            + ["1h price movement and volume baseline window not recorded"],
    }
    Path("verified-report.json").write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: output[k] for k in ("status", "paper_run_id", "ledger_generation", "watch_count", "legacy_independent", "verified_independent_overlaps")}, sort_keys=True))

if __name__ == "__main__":
    main()
