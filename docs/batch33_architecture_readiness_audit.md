# Batch 33 — Repository architecture and release-readiness audit

**Baseline:** Batch 32 final commit `571686dcb90e26137649779e23c393dec827671c` passed GitHub Actions #120 (`39880831388`).

**Scope:** Read-only review of `simple_scanner/external_backup.py`, `offline_replay.py`, `offline_scoring_comparison.py`, `fixture_delivery_outbox.py`, `fixture_receipt_reconciliation.py`, `manual_requests.py`, `execute_once.py` and the Batch 32 evidence contract. No production access, code changes or new test infrastructure.

## Evidence-backed gaps

| Priority | Area | Verified implementation | Unresolved evidence or defect | Next safe action |
|---|---|---|---|---|
| P0 | Manual result delivery | `execute_once.execute` calls `publish_results` and then unconditionally acknowledges **all** pending requests after a VERIFIED scan; `manual_requests.plan_requests` excludes acknowledged issues | Failed/ambiguous POST may lose delivery visibility; published result has no durable authenticated comment ID | Prepare a minimal, explicitly inactive patch design and review existing tests. Activation requires separate approval and real evidence |
| P0 | Independent backup | `external_backup.export_verified` checks different filesystem devices, SQLite inventory and a restore copy | No evidence of a real independent destination, retention, recovery drill or live verification | Obtain operator-authorized read-only inventory of storage topology and separately authorized backup/restore proof |
| P1 | Production-history replay | `offline_replay.replay_feasibility` only counts `market_signals` and `market_observations`; `cohort_split` is pure | No actual historical feature/outcome replay, lineage completeness or unbiased unseen holdout verification | Inspect an authorized immutable production-history export offline, then assess completeness and replay feasibility |
| P1 | Scoring parity | `offline_scoring_comparison.compare_cohorts` chooses one winner per timestamp using supplied baseline score and challenger function | Supplied feature tuples do not prove either real production or legacy implementation equivalence | Map exact legacy and production scoring versions and reproduce their scores against the same approved archived cohorts |
| P1 | GitHub delivery evidence | `fixture_github_evidence_contract` validates caller-supplied snapshot; `fixture_receipt_reconciliation` checks receipt markers | No authenticated author/issue binding or provably complete API pagination; ambiguous POST cannot be safely retried | Specify the narrow authenticated read-only evidence adapter; do not connect it or POST |
| P1 | Rollback | Backup restore rehearsal and fixture rollback tests exist | No independently observed live rollback or restoration of all required state | Document operator-approved rollback drill prerequisites and success evidence |
| P2 | Scheduled reliability | Shared lock and offline contract checks exist in `execute_once` | No proof of live schedule delivery, run-to-run freshness or uninterrupted source coverage | Analyze existing CI and operational run records only after authorization |

## Minimal path, avoiding duplicate infrastructure

1. **Offline now:** Preserve the existing outbox and pure acknowledgement policy; review a minimal execution integration diff without activating it. Do not add another writer, queue, scanner or scheduler. Keep the current implementation untouched unless a specifically justified offline-only correction is found.
2. **Requires authorization:** Obtain independent backup/restore evidence and immutable historical data export. Validate actual history lineage and production/legacy scoring parity on the same frozen cohorts.
3. **Requires authorization:** Authenticate GitHub comments and pagination, reconcile uncertain POST outcomes against durable receipt identity, then test controlled delivery and rollback. No live integration before all gates are met.
4. **Only after verified evidence:** Evaluate a separately approved release. Fixture-only CI is not production acceptance.

## Audit outcome
No clearly justified **new safe offline code correction** was found beyond the isolated acknowledgement and evidence-contract work already in Batches 30–32. Additional fixture modules would be redundant. This report changes documentation only; the Batch 32 final code CI remains the last tested executable baseline. No new code or workflow CI is claimed.

**Release decision: BLOCKED.** Independent live backup, genuine production-history replay, real production/legacy scoring parity, authenticated production delivery, live rollback and live scheduler reliability remain unverified. No merge, deployment, production access, history deletion, model promotion or release-gate weakening.
