# Batch 30 — Manual delivery acknowledgement defect and offline repair prototype

## Baseline
Batch 29 commit `d6d897334b18eb03890a9681d1e6f72dd28b0999` passed CI #105 (`39880413032`).

## Confirmed source-level defect
In `simple_scanner/execute_once.py`, `publish_results` returns only issue dictionaries with successful HTTP 201 responses. The wrapper then calls `acknowledge_requests(data_dir, manual_pending, ...)` for **all** pending requests, including those whose POST failed or timed out. `manual_requests.plan_requests` excludes acknowledged issues from future runs. This loses the delivery retry path even though the scan completed. The wrapper itself says it is not wired to production; no production behavior was changed in Batch 30.

## Fixture-only minimal repair model
`fixture_manual_delivery_decision.classify_delivery` stages the existing durable outbox before simulated delivery, separates scan completion from delivery confirmation, and **never** marks a request delivered or repostable based solely on the `publish_results` return value. It has no network calls, ledger writes or production imports. The existing fixture reconciler can confirm an outbox receipt when given an isolated comment fixture; it does not authenticate GitHub evidence.

## Offline acceptance cases
- Reproduces the current acknowledgement defect by calling the existing ledger helper after a simulated undelivered scan.
- Blocked/ambiguous delivery retains a pending durable receipt and no acknowledgement.
- A reported HTTP 201 without a confirmed comment ID is insufficient to close the delivery record.
- Idempotent reclassification does not trigger a second scan or POST.
- Interrupted atomic stage does not mutate the ledger.
- Manual/cron fixture decisions match.
- Duplicate and foreign delivery evidence fails closed.

## Remaining blockers
- Authenticated, complete GitHub comment pagination and ambiguous-POST reconciliation are unverified.
- No production integration or live delivery is authorized.
- **Independent live backup**, **genuine production-history replay**, **live rollback**, real production/legacy scoring parity and live scheduled reliability remain **BLOCKED**.
- No merge, deployment, production access, history deletion, model promotion or release-gate weakening.

**Release decision: BLOCKED.**
