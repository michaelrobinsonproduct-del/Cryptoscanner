# Batch 34 — Inactive durable manual acknowledgement transition

Baseline: Batch 32 CI #120 successful; Batch 33 audit `docs/batch33_architecture_readiness_audit.md`.

## Actual defect
`simple_scanner/execute_once.py` currently calls `acknowledge_requests(data_dir, manual_pending, ...)` after `publish_results` regardless of delivery outcome. Thus a failed or ambiguous POST may cause `plan_requests` to exclude an undelivered issue from subsequent handling. The wrapper is not wired to production, but this defect must be corrected before activation.

## Minimal offline-only correction
Extended the **existing** pure `manual_acknowledgement_policy.py` with `plan_manual_delivery_transition`. It accepts requests, independently confirmed issue/comment IDs, and durable outbox records; it rejects any confirmation lacking a matching `DELIVERED` record with the same comment ID, nonempty run ID and digest. Blocked/ambiguous requests stay pending; no automatic POST, rescan or ledger acknowledgement. This function does not authenticate GitHub evidence itself, does not write storage, and is **not imported by execute_once**.

## Future reviewed integration — NOT ACTIVATED
After a verified scan, persist a research-only receipt before any POST, then require authenticated and complete GitHub comment evidence. Reconcile unique receipt marker to the durable outbox and call the pure transition policy. Acknowledge only confirmed issues. An ambiguous response stays pending for reconciliation without rescanning or reposting. The current wrapper's unconditional acknowledgement must be removed only in a separately authorized integration. This is not a deployable live patch because authenticated GitHub evidence retrieval and complete pagination remain absent.

## Acceptance
Offline tests cover blocked/ambiguous delivery, false 201 evidence, durable confirmation, mismatched/duplicate evidence, parity and no wrapper activation. Existing backup, history, DEX and shadow-learning regression steps remain in CI.

**Release decision: BLOCKED.** Independent live backup, genuine production-history replay, live rollback, production delivery integration, real production/legacy scoring parity and live reliability remain unverified. No merge, deployment, production access, history deletion, model promotion or release-gate weakening.
