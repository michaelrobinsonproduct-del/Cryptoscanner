# Batch 24 — Isolated outbox and operational readiness

**Release decision: BLOCKED.** This work is offline-only and does not authorize production actions.

## Evidence
- Baseline commit `748bdc77880c5139962e81c1ec5696a1f82f3bd5`: GitHub Actions `39772428305` passed all 15 test steps.
- `fixture_delivery_outbox.py` is a separate, unimported test prototype. It stages bounded research-only receipts atomically, persists pending delivery across restart, and requires a matching run ID, receipt digest and confirmed comment ID before marking delivered.
- Tests cover corrupted state, conflicting identities, idempotent confirmation, partial confirmation, simulated interruption before atomic replace, ambiguous timeout remaining pending and subsequent explicit reconciliation.
- **Limitation:** no live GitHub GET/comment reconciliation is implemented. A timeout after a successful POST could lead to duplicate comments if naively retried. Automatic exactly-once delivery is NOT proven.
- Existing `execute_once.py` still acknowledges blocked manual results as satisfied; no production or shared scanner execution behavior was changed.
- Manual and cron share the same fixture execution pipeline; actual scheduled reliability is unverified.
- Historical feasibility and scoring comparisons use synthetic fixtures; no genuine production-history replay or independently verified production-vs-legacy scoring parity.
- Isolated SQLite rollback tests do not prove remote storage access, independent live backup or live rollback.

## Required before release
1. Independently verified live backup, restore, storage isolation and row/schema/value parity — **BLOCKED**.
2. Genuine production-history replay and production-vs-legacy scoring parity — **BLOCKED**.
3. Live rollback rehearsal — **BLOCKED**.
4. Production-safe outbox integration with GitHub reconciliation and retry deduplication, plus manual/scheduled operational proof — **BLOCKED**.
5. Live Kraken/DEX freshness, coverage and degraded-mode verification — **UNVERIFIED**.

No merge, deployment, production access, history deletion, model promotion or release-gate weakening.
