# Batch 21 release-readiness evidence (isolated repair branch)

**Disposition: NOT RELEASE READY.** This document does not authorize deployment, merge, promotion, data modification, or a backup operation.

## Verified CI baseline

- Commit `066d071e16dcd7123b8d000aece10a36fc08b4e8`: GitHub Actions run `39766234440` completed **successfully**.
- Fixture-based manual and scheduled execution acceptance, acknowledgement, DEX/shadow degraded behavior, malformed output, and invalid ledger were exercised by CI.
- Tests use temporary fixtures and mocks; they do not prove the live manual request endpoint, production scheduler, real GitHub posting, or production rollback.

## Added rollback rehearsal

- `tests/test_rollback_rehearsal.py` exercises fixture SQLite backup and restore inventory parity, isolation of source and restored copies, and corruption detection.
- The independent-device signal is mocked in CI. This does **not** validate an actual independent backup device.
- The rehearsal is not a deployed-code rollback and does not verify live recovery time or remote snapshot retention.

## Release blockers (must remain blocked)

1. **Independent live backup:** No verified production-source snapshot/export to an independent device with restoration and row/schema parity evidence. Do not run an unverified backup on the nearly full production volume.
2. **Genuine production-history replay:** No authorized safe historical export; synthetic cohorts and counts do not prove production vs legacy score parity.
3. **Live manual/scheduled delivery:** Fixture-based contract tests do not establish live scheduling, GitHub comment permissions, and acknowledgement reliability.
4. **Operational rollback:** No verified rollback of a deployed scanner with preserved historical data and monitoring.
5. **Final-commit CI:** Require completed, successful workflow on the latest repair-branch commit before treating Batch 21's offline test gates as passed.

## Safe next step

Verify final CI and stop at any failures. Continue read-only offline tests, independently validate backup and replay prerequisites, and obtain explicit release authorization separately. No merge, deploy, production access, history deletion, or model promotion.
