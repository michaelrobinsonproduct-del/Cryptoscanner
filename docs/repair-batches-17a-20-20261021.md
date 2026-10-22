# Batches 17A–20: safety-gated repair checklist

Production baseline: Railway service `b94f8368-d0c7-4146-8e8a-c7e3120c5869`, branch `manual-scan-isolation-20261015`. This branch is research-only. **Do not merge, deploy, run a second writer, or alter model weights.**

## 17A — observed evidence (complete, read-only)
- Railway: one live replica and 100 MB /data volume; scanner process is `python -m simple_scanner.daemon`.
- Latest inspected cron: `2026-10-22T03:00:15Z`, exit 0, history persisted, shadow evaluated, DEX cache reused.
- `STORAGE_FREE_BYTES=3768320`; SQLite audit at `2026-10-21T23:00Z`: 84,045,824 DB bytes, ~24.8 MB internally reusable pages. Internal freelist **does not** equal free filesystem bytes.
- `history.py` already drops redundant indexes, uses bounded market-observation retention and MEMORY journal, and explicitly avoids live VACUUM. Do not duplicate or remove those safeguards.
- Safety gate: cannot verify exact live file distribution, database backup/restore, and disk headroom from read-only logs. **No destructive reclamation permitted.**

## 17B — storage fix (blocked by 17A gate)
1. On an isolated copy of the persisted SQLite DB, snapshot row counts and hashes by table and validate `PRAGMA integrity_check`.
2. Measure database, WAL/journal, transient JSON and file-system occupancy separately. Verify retention limits and free-page reuse with realistic 100 MB quota.
3. Prefer bounded writes and fail-closed low-space diagnostics. Never VACUUM or DELETE live history solely to reclaim OS space.
4. Verify byte-level retention of required training/outcome rows, concurrent-writer exclusion, full-volume recovery and rollback.
5. Only commit a tested code change after those gates pass.

## 18 — DEX reliability (not executed)
- `dex.py` reuses cache for <61 min, while `execute_once.py` accepts age <=61 min. Boundary differs; reconcile only with tests for exactly 61 min, future timestamps, malformed cache, all-source failure, partial-source failure, and circuit recovery.
- DEX discovery is sampled public search, not comprehensive DEX coverage. Do not claim full discovery.
- Keep DEX failures research-only and unable to authorize buys; ensure Kraken cron remains functional.

## 19 — learning validation (not executed)
- `validate_accumulation_history` selects 6000 most recent signal rows and requires >=20 distinct matured timestamps. Logs reported 6000 rows but only 10 timestamps, so the evaluation is blocked.
- Research fix: evaluate complete timestamp cohorts across a wider, bounded window rather than simply increasing row LIMIT. Ensure no future-label leakage, equal candidate budgets and time-separated holdout.
- Keep `promotion_eligible=false`, `buy_approved=false`, and live weights unchanged until independently proven forward.

## 20 — final acceptance (not executed)
- Confirm identical manual/cron eligibility checks, same-run summary/history/shadow/DEX provenance, <=61-minute DEX cache, durable SQLite integrity, fail-closed behavior, and rollback.
- Run tests against isolated fixtures, then branch CI and final-commit CI. Stop on any failure; no merge/deploy/promotion.

## Status
17A diagnosis complete; **17A safety gate blocked** due to lack of isolated database/backup and filesystem measurements. 17B, 18, 19 and 20 are pending. This document is a checkpoint, not a claim of repaired production.
