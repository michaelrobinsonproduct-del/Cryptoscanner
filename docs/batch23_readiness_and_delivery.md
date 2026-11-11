# Batch 23 — Delivery acknowledgement and rollback readiness

**Disposition: offline acceptance only; production release BLOCKED.**

## CI evidence
- Commit `e2c3fddc4fb1488589ad5b3197c0cccb987f9e58`: Scanner Storage Safety CI run `39766811515`, **success**.
- Tests exercise manual and cron with identical fixture modules and reports, lock contention, corrupt/mismatched history rejection, DEX degraded suppression, offline holdout equal-budget scoring, read-only SQLite inventory, and isolated rollback rehearsal.
- These tests do not prove live scanner schedule reliability, actual trading outcomes, or independent production scoring parity.

## Delivery semantics — unresolved, not silently approved
- `execute_once.execute` invokes `publish_results`, then writes `manual_pending` to the completed-issue ledger even when `delivered` is empty or partial.
- Consequently the current ledger means **scan attempted/satisfied**, not **GitHub result receipt confirmed**. `plan_requests` excludes that issue on future runs, so failed comment delivery is not automatically retried.
- Current logs emit `MANUAL_RESULT_DELIVERY_PENDING` and `delivery_status=BLOCKED`; they do not provide durable successful receipt evidence.
- Simply acknowledging only delivered issues would cause a new scan on every retry, risking duplicate scans. A safe eventual design needs a durable outbox of verified result payloads, stable request/run identity, independently retryable delivery, and duplicate-comment reconciliation. Do not change execution semantics until isolated acceptance tests prove this.
- GitHub HTTP 403 and ambiguous network timeout require separate outcomes; exactly-once delivery cannot be claimed without a reconciliation mechanism.
- **Delivery retry/reconciliation remains a release blocker.** No code-path change or live comment posting was made.

## Offline scoring and rollback evidence
- `compare_cohorts` has equal per-cohort selection budget and explicit `production_scoring_parity_verified=False` and `promotion_eligible=False`.
- `replay_feasibility` inventories all fixture rows, but `full_replay_verified=False`; no genuine production archive was read.
- Fixture SQLite backup/restore checks cannot establish independent live backup, remote rollback or production restoration.

## Explicit gates
1. Independent live backup, external storage proof and full restore/row/schema/value parity: **BLOCKED**.
2. Genuine production-history replay and independently verified legacy-vs-production scoring: **BLOCKED**.
3. Live rollback and operational restoration: **BLOCKED**.
4. Production manual/scheduled reliability and receipt reconciliation: **UNVERIFIED / BLOCKED**.
5. Production Kraken/DEX freshness and complete DEX coverage: **UNVERIFIED**.

No merge, deployment, production access, history deletion, model promotion, or release-gate weakening is authorized.
