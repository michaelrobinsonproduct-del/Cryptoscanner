# Batch 22 — Offline release-acceptance evidence

**Release disposition: BLOCKED.** This report does not authorize production activity.

## Verified baseline
- Commit `922cf7c1550fba24a594bc2f6638824c3f239d5b`: GitHub Actions run `39766490992` **passed**.
- Batch 21 commit `8b7f8e24414d4809b17f65ee843629e42918c00a`: run `39766351481` **passed**.
- The initial Batch 22 test failed because the fixture parsed a literal escaped Markdown fence. Repair corrected test parsing only, not live scanner behavior.

## Added Batch 22 offline acceptance
- `tests/test_batch22_delivery_recovery.py`: request filtering, duplicate and stale request handling, GitHub 403 non-acknowledgement, idempotent acknowledgement and sanitized research-only receipt.
- `tests/test_batch22_source_recovery.py`: Kraken transient retry, exhausted retry fail-closed, DEX stale-cache rejection during outage and DEX circuit recovery.
- Manual and scheduled scanner use the same `execute_once` pipeline, but CI mocks subprocesses and outbound delivery; live parity is **not verified**.
- CI validates only temporary files and fixture responses; does not access production history or trigger any live scanner.
- Final-commit CI must pass before declaring the offline Batch 22 acceptance complete.

## Outstanding blockers
1. Independent **live** backup with external-device proof, restore, schema/row/value parity, and sufficient headroom: **BLOCKED**.
2. Full genuine production-history replay and independently verified legacy-vs-production scoring parity: **BLOCKED**.
3. Live deployment rollback, restoration and observability: **BLOCKED**.
4. Real manual request delivery and scheduled-run reliability in production: **UNVERIFIED**.
5. DEX universe coverage beyond sampled searches and live freshness, and Kraken live source availability: **UNVERIFIED**.

No merge, deployment, production access, history deletion, model promotion or release-gate weakening is authorized. All production promotion gates remain closed.
