# Batch 32 — Offline GitHub delivery evidence contract

## Baseline
Batch 31 final commit `9c038cd4dabf6e72b3119d0c73bbd586bc280968` passed CI #115 (`39880691565`).

## Minimum future integration contract
1. **Comment identity:** positive unique GitHub comment IDs; reject missing, duplicated or invalid IDs.
2. **Authorship:** verify the actual GitHub comment `user.login` against an independently configured expected bot identity. The fixture's `author` field is caller-supplied and **not authenticated**.
3. **Issue binding:** confirm comment `issue_url` or API endpoint binding to the exact repository and requested issue; reject cross-issue data. Fixture `issue_number` is caller-supplied.
4. **Complete pagination:** fetch and verify every page from GitHub, including rate-limit/error handling and consistent repository/issue identity. `complete=True` in the fixture is an assertion, **not proof** of complete pagination.
5. **Ambiguous POST:** persist verified research receipt and issue/run/digest identity before attempting a POST. After a timeout, reconcile authenticated complete comments; never automatically POST again or rescan because an empty/incomplete snapshot cannot establish absence.
6. **Durability:** confirm receipt identity and positive comment ID in existing outbox, then atomically acknowledge only confirmed issue IDs. Interrupted writes must leave pending state and require reconciliation.
7. **Go/no-go:** accept only verified immutable issue/run/receipt binding, independently authenticated authorship, complete pages, a unique matching comment, durable outbox confirmation, and explicit operator-approved activation after independent backups and rollback readiness. Any missing/ambiguous evidence => BLOCKED.

## Offline implementation
`simple_scanner/fixture_github_evidence_contract.py` checks caller-supplied fixture consistency: unique comment IDs, author and issue binding, complete snapshot flag, bounded receipt marker and duplicate detection. It has no network, credential or storage access. Tests prove this isolated contract can feed the pure acknowledgement policy, not that the caller's assertions are trustworthy. The production wrapper `execute_once` remains unchanged.

## Release decision: BLOCKED
Authenticated GitHub evidence retrieval and complete pagination are not implemented; **production delivery integration** remains blocked. **Independent live backup**, **genuine production-history replay**, **live rollback**, real production/legacy scoring parity and live scheduler reliability remain blocked. No merge, deployment, production access, history deletion, model promotion or release-gate weakening.
