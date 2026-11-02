# Batch 27 — Fixture integrity acceptance and hard release gates

## Offline evidence
- Baseline commit `f4deb52fe56155349c6c755b0e6afd7bb89797e3` passed Scanner Storage Safety CI run `39775020878` (21 regression-test steps).
- The isolated outbox now verifies canonical receipt hashes, issue identities, and delivered comment confirmations when reading stored fixture state.
- Negative-case tests cover corrupted receipt payload, invalid issue identity, invalid delivered comment ID, interrupted atomic stage/confirmation, and recovery by supplied fixture comments without starting another scan.
- Manual and scheduled paths have a shared fixture execution/reporting contract. Historical cohort holdouts and independent scoring checks are synthetic and cannot authorize production model promotion. Isolated rollback is local only.

## Known gaps
- GitHub comment author authentication, complete pagination, ambiguous network success and exactly-once delivery are not proven.
- Fixture outbox remains disconnected from `execute_once`; blocked-result acknowledgements in production code are unchanged.
- Actual production scheduler reliability, live Kraken/DEX freshness and DEX discovery coverage are unverified.
- Independent live backup and restore, genuine production-history replay, real legacy-vs-production scoring parity, and live rollback are **BLOCKED**.

**Release decision: BLOCKED.** No merge, deployment, production access, history deletion, model promotion or release-gate weakening.
