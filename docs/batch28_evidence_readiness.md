# Batch 28 — Narrow offline release-readiness acceptance

## Scope
Batch 27 final commit `dc8c9c2ba58fb88e75d0b6f299867375fa3d7d37` passed Scanner Storage Safety CI run `39775118886`.

Batch 28 adds focused fixture-only tests for conflicting delivered comment IDs, tampered receipt digests, ambiguous duplicate comment evidence and interrupted atomic confirmation. The intended contract is **fail closed** and preserve prior state; no second scan or live GitHub POST is permitted.

## Evidence limitations
The outbox is not integrated into production. A supplied comment fixture is not proof of GitHub authorship, complete pagination or exactly-once posting. Synthetic historical/scoring tests are not genuine production replay or independent legacy-vs-production scoring parity. Isolated SQLite rollback tests are not live rollback or independently verified live backup. Manual/cron tests are fixture-only; live schedule reliability and Kraken/DEX coverage are unverified.

## Release decision
**BLOCKED** until independent live backup/restore, genuine production history replay, real scoring parity, live rollback and production-safe delivery reconciliation are separately proven. No merge, deployment, production access, history deletion, model promotion or release-gate weakening.
