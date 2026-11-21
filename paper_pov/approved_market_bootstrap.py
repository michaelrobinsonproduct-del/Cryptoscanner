"""Verify the explicit, owner-approved first main shadow checkpoint; never reset state."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import tempfile
import zipfile

from .learning_retention import allowed_checkpoint_file, verify_checkpoint_directory

REPO = "michaelrobinsonproduct-del/Cryptoscanner"
PIN = {
    "schema": "approved_market_learning_bootstrap_v1",
    "approved_public_release": "market-wide-research-v1",
    "release_verify_run": 44666481725,
    "release_verify_job": 136056898120,
    "research_run": 44529882265,
    "research_sha": "0411959db3093f048d7a49170a483430e646ec4b",
    "research_artifact": 14532804413,
    "state_digest": "7785f362dc7795a54ae40474dbde6ab481e7fd4ab6004ea0ead63e2eb76f9459",
    "model_origin_run": 44529483795,
    "scope": "shadow_only",
    "allow_reset": False,
}
ARTIFACT_SHA = "552b265242ec19e9ced4073ea14ce5ae084bd15425f9289b79e77ab022a6ac64"
RELEASE_SHA = "bdc7e68f7fa75fae6636b7738d52f10a65d92038"
ASSETS = {
    "market-wide-research-backup.tar.gz": "sha256:aefc1fe3a2756d9b730d8ab30ce2159e7962668458f762e0dae980a7bc604c5d",
    "market-wide-strict-seed.tar.gz": "sha256:177851f0929de8a015355641419097197b0fa9867a7b0516619422c1fd31434f",
    "SHA256SUMS": "sha256:ed43d98431b0ca5f88be7cd21f53c41e0202ae2b35fa99f8dce5eacd1ff8e7e4",
}


def api(path):
    return json.loads(subprocess.check_output(["gh", "api", f"repos/{REPO}/{path}"]))


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def verify(marker):
    require(os.environ.get("GITHUB_REPOSITORY") == REPO, "Unexpected repository")
    require(json.loads(Path(marker).read_text()) == PIN, "Unapproved bootstrap marker")
    job = api(f"actions/jobs/{PIN['release_verify_job']}")
    require(job["run_id"] == PIN["release_verify_run"] and
            job["head_sha"] == RELEASE_SHA and job["name"] == "publish-approved-research-backup" and
            job["status"] == "completed" and job["conclusion"] == "success", "Release readback job not verified")
    release = api(f"releases/tags/{PIN['approved_public_release']}")
    require(not release["draft"] and release["tag_name"] == PIN["approved_public_release"], "Release unavailable")
    present = {a["name"]: a["digest"] for a in release["assets"]}
    require(all(present.get(k) == v for k, v in ASSETS.items()), "Changed research release assets")
    run = api(f"actions/runs/{PIN['research_run']}")
    require(run["head_branch"] == "learning-market-wide-20261117" and run["event"] == "pull_request" and
            run["head_sha"] == PIN["research_sha"] and run["status"] == "completed" and
            run["conclusion"] == "success", "Unapproved research source")
    owners = api(f"actions/runs/{PIN['research_run']}/jobs?per_page=100")["jobs"]
    require(any(j["name"] == "market-wide-shadow-learning" and j["head_sha"] == PIN["research_sha"]
                and j["status"] == "completed" and j["conclusion"] == "success" for j in owners),
            "Research owner job not verified")
    artifacts = api(f"actions/runs/{PIN['research_run']}/artifacts?per_page=100")["artifacts"]
    require(any(a["id"] == PIN["research_artifact"] and not a["expired"] and
                a["name"] == f"market-wide-learning-continuity-pr-{PIN['research_run']}" and
                a["digest"] == "sha256:" + ARTIFACT_SHA for a in artifacts), "Research artifact mismatch")
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        archive = root / "checkpoint.zip"
        with archive.open("wb") as out:
            subprocess.run(["gh", "api", f"repos/{REPO}/actions/artifacts/{PIN['research_artifact']}/zip"],
                           stdout=out, check=True)
        require(hashlib.sha256(archive.read_bytes()).hexdigest() == ARTIFACT_SHA, "Checkpoint ZIP digest mismatch")
        checkpoint = root / "checkpoint"
        checkpoint.mkdir()
        with zipfile.ZipFile(archive) as z:
            seen = set()
            for member in z.infolist():
                p = PurePosixPath(member.filename)
                require(not p.is_absolute() and ".." not in p.parts, "Unsafe archive member")
                if member.is_dir():
                    continue
                require(member.filename not in seen and allowed_checkpoint_file(member.filename)
                        and member.file_size <= 128 * 1024 * 1024, "Unexpected checkpoint member")
                seen.add(member.filename)
                dst = checkpoint / member.filename
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(z.read(member))
        state, receipt = verify_checkpoint_directory(checkpoint, required_scope="pr", expected_state=PIN["state_digest"])
        origin = (checkpoint / "market-wide-model-origin-run.txt").read_text().strip()
        require(origin == str(PIN["model_origin_run"]), "Pinned candidate origin mismatch")
        print("APPROVED_SHADOW_BOOTSTRAP_VERIFIED", state["ledger_generation"], receipt["digest"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["verify"])
    parser.add_argument("--marker", required=True)
    args = parser.parse_args()
    verify(args.marker)
