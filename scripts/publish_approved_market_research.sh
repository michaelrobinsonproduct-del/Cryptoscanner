#!/usr/bin/env bash
# Publish only the exact owner-approved, public Kraken research backup.
set -euo pipefail
mode="${1:-verify}"
[[ "$mode" == verify || "$mode" == publish ]]
repo=michaelrobinsonproduct-del/Cryptoscanner
test "$GITHUB_REPOSITORY" = "$repo"
run=44529483795
artifact=14532478948
digest=14d6332fb1960b51faa26d2e5c0477214b470b5d492b4c55ed939d285ad1341b
tag=market-wide-research-v1
root=$(mktemp -d)
trap 'rm -rf "$root"' EXIT
gh api "repos/$repo/actions/runs/$run/jobs?per_page=100" --jq '.jobs[]|select(.name=="stage-learning-durable-backup")|.status+":"+.conclusion+":"+.head_sha' | grep -Fx 'completed:success:37c7c5dd847748ae3315cb54995e4e47edde7d4d'
gh api "repos/$repo/actions/runs/$run/artifacts?per_page=100" > "$root/artifacts.json"
jq -e --argjson id "$artifact" --arg digest "sha256:$digest" '.artifacts[]|select(.id==$id and .name=="market-wide-durable-backup-44244937090-v1" and .expired==false and .digest==$digest)' "$root/artifacts.json" >/dev/null
gh api "repos/$repo/actions/artifacts/$artifact/zip" > "$root/approved.zip"
printf '%s  %s\n' "$digest" "$root/approved.zip" | sha256sum -c -
mkdir "$root/staged" "$root/readback" "$root/unpacked"
python - "$root" <<'PY'
import pathlib, sys, tarfile, zipfile
root=pathlib.Path(sys.argv[1])
expected={"SHA256SUMS","market-wide-strict-seed.tar.gz","market-wide-research-backup.tar.gz"}
with zipfile.ZipFile(root/"approved.zip") as z:
    assert len(z.namelist())==3 and set(z.namelist())==expected
    z.extractall(root/"staged")
with tarfile.open(root/"staged/market-wide-research-backup.tar.gz") as t:
    for m in t.getmembers():
        p=pathlib.PurePosixPath(m.name)
        assert not p.is_absolute() and ".." not in p.parts
        assert m.isfile() or m.isdir()
        assert not p.parts or p.parts[0] in {"q2","q3","november","live","trades","RECOVERY.md","SHA256SUMS","market-wide-strict-seed.tar.gz"},p
        assert not any(x.lower() in {".env",".git","credentials","secrets","id_rsa","id_ed25519"} or x.lower().endswith((".pem",".key")) for x in p.parts),p
        print("APPROVED_RESEARCH_MEMBER",m.name,m.size)
    t.extractall(root/"unpacked",filter="data")
PY
(cd "$root/staged" && sha256sum -c SHA256SUMS)
(cd "$root/unpacked" && sha256sum -c SHA256SUMS >/dev/null)
cmp "$root/staged/market-wide-strict-seed.tar.gz" "$root/unpacked/market-wide-strict-seed.tar.gz"
python -m paper_pov.learning_retention unpack-seed --archive "$root/staged/market-wide-strict-seed.tar.gz" --directory "$root/seed"
jq -e '.digest=="98059c9e5019a125202ccbe71dcc23cfeed60f88587a3bb4332d9c1a0e67b6e5"' "$root/seed/manifest.json" >/dev/null
echo APPROVED_RESEARCH_BACKUP_VERIFIED
if [[ "$mode" == verify ]]; then exit 0; fi
test "$GITHUB_EVENT_NAME" = push
test "$GITHUB_REF" = refs/heads/main
# This is a research-only release, not a scanner deployment. No clobber.
if ! gh release view "$tag" --repo "$repo" >/dev/null 2>&1; then
  gh release create "$tag" --repo "$repo" --target "$GITHUB_SHA" --title "Market-wide paper research backup v1" --notes "Owner-approved public Kraken paper research; pinned verified backup, no trading or production model promotion." --latest=false
fi
for name in market-wide-strict-seed.tar.gz market-wide-research-backup.tar.gz SHA256SUMS; do
  if ! gh release view "$tag" --repo "$repo" --json assets --jq '.assets[].name' | grep -Fx "$name"; then
    gh release upload "$tag" "$root/staged/$name" --repo "$repo"
  fi
  gh release download "$tag" --repo "$repo" --pattern "$name" --dir "$root/readback"
  cmp "$root/staged/$name" "$root/readback/$name"
done
(cd "$root/readback" && sha256sum -c SHA256SUMS)
echo PUBLIC_RESEARCH_RELEASE_READBACK_VERIFIED
