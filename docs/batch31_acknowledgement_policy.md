# Batch 31 — Pure manual acknowledgement policy (offline)

## Baseline
Batch 30 commit `425c8f05b023628960b3b96c33c6991d2012066d` passed CI #110 (`39880548609`).

## Scope and decision
`simple_scanner/manual_acknowledgement_policy.py` is a pure function that separates confirmed deliveries from unresolved requests. It is designed to be importable by the existing `execute_once` wrapper **in a future separately reviewed change**, but is intentionally **not imported or called** by that wrapper now. No production execution behavior or live delivery integration changes.

A verified scan, an HTTP 201 response, or a caller-supplied issue dictionary alone is not durable proof of delivery. The policy requires a unique positive comment ID for each confirmed issue. Even then, the policy only evaluates **caller-supplied** evidence and does not authenticate comment authorship or pagination completeness.

## Offline test coverage
Blocked and ambiguous POST => no acknowledgement, no automatic repost, no scan rerun. Partial confirmations stay pending. Duplicate, foreign and invalid IDs fail closed. Existing outbox persists through ambiguous responses and can be reconciled with fixture comment evidence. Interrupted write does not create an outbox. Manual/cron use the same pure policy. A source assertion prevents accidental activation in `execute_once`.

## Release decision: BLOCKED
- Real GitHub comment identity, authorship and complete pagination unverified.
- Production manual acknowledgement remains premature until a separately authorized integration.
- **Independent live backup**, **genuine production-history replay**, **live rollback**, **production delivery integration** and real production/legacy scoring parity remain blocked.
- No merge, deployment, production access, history deletion, model promotion or release-gate weakening.
