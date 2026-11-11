# Batch 35 — Evidence readiness and release-gate checklist

**Baseline:** Batch 34 final commit `5f7d7155966fb1aa8bfd2427924e02acff720f59`, GitHub Actions #127 (`39881070967`) **success**. This batch is documentation-only; no new executable CI is claimed.

**Evidence rule:** A passing fixture or CI run proves only the offline contract tested. Do not accept self-declared flags, simulated comments, or synthetic historical cohorts as independently verified live evidence. Retain immutable, timestamped artifacts and reviewer sign-off for every gate.

| Gate / order | Existing repo artifacts | Evidence needed to close | Owner / authorization | Pass criterion |
|---|---|---|---|---|
| **1. Independent live backup + restore (P0)** | `simple_scanner/external_backup.py`, `storage_safety.py`, backup/restore regression tests | Approved source SQLite identity and timestamp; independently located destination and device/storage ownership; verified export inventory; restored-copy integrity/table/row parity; retention/access proof and reproducible logs | Infrastructure/storage operator; explicit authorization for source read and backup/restore drill; separate reviewer | Source remains unchanged, destination truly independent, integrity and restore parity proven, recovery time documented. **BLOCKED** |
| **2. Genuine production-history replay (P0)** | `simple_scanner/offline_replay.py`, `history.py`, offline replay tests | Authorized immutable export with provenance and checksum; full run/timestamp, symbol, feature, outcome, missing-data and observation lineage; chronological embargoed train/holdout split; replay outputs reproducible from same snapshot | Data owner and security approver for export; research reviewer | No synthetic substitutions, no lookahead/leakage, no missing critical lineage, holdout results independently reproduced. **BLOCKED** |
| **3. Real production-versus-legacy scoring parity (P1)** | `simple_scanner/offline_scoring_comparison.py`, `scan.py`, `history.py`, scoring tests | Pinned legacy and production code/config/weights and versions; same approved historical feature snapshot; per-pair/per-cohort scores, tie-breaks, selections and differences; documented justified deviations | Scanner code owner and independent scoring reviewer; read-only artifact access | Deterministic independently reproduced parity or explicit explained deviations; no promotion on offline fixture results. **BLOCKED** |
| **4. Authenticated GitHub delivery + manual acknowledgement (P0)** | `simple_scanner/manual_requests.py`, `execute_once.py`, `fixture_delivery_outbox.py`, `fixture_receipt_reconciliation.py`, `fixture_github_evidence_contract.py`, `manual_acknowledgement_policy.py` | GitHub-authenticated comment ID, author identity, repository and issue binding, complete API pagination evidence, immutable issue/run/digest marker, durable confirmed outbox; ambiguous POST timeout reconciliation and permission-error cases | GitHub integration owner and security reviewer; explicit read-only evidence access first, separately approved live POST/integration later | Unique matching authenticated comment, durable confirmation before ledger acknowledgement, no duplicate POST or rescan; verified blocked-delivery recovery. Current `execute_once` still prematurely acknowledges all pending requests. **BLOCKED** |
| **5. Live rollback (P0 before release)** | `external_backup.py`, isolated rollback tests and recovery docs | Signed operator runbook; complete state inventory; restore target isolation; real rollback drill logs, independent validation, RTO/RPO and decision authority | Infrastructure/on-call owner; separate drill authorization and independent observer | Verified restoration of scanner state and history without destructive changes, documented time/recovery outcome. **BLOCKED** |
| **6. Scheduled reliability and source freshness (P1)** | `simple_scanner/execute_once.py`, `dex_guard.py`, `scan.py`, CI source freshness and execution tests | Actual schedule and runtime identity; run IDs/timestamps, source age, failures/retries, Kraken/DEX coverage and delivery receipts across representative live windows; comparison to manual invocation | Operations/scheduler owner; authorized read-only run logs and schedule inventory | Repeatable scheduled and manual results, freshness gates met, failures observable and recoverable, no duplicate scanner or history writer. **BLOCKED** |

## Shortest safe sequence

1. **No additional fixtures or infrastructure.** Inventory approved existing operational artifacts, owners and immutable hashes; verify whether any gate already has independent evidence before requesting new work.
2. **Backup first:** with explicit operator approval, demonstrate independent backup and isolated restore. No deletion or changes to live history.
3. **History + parity:** use the same approved immutable export to replay genuine cohorts and compare pinned legacy/production scoring; no model promotion.
4. **Delivery:** read-only authenticate GitHub comments, pagination and ambiguous POST evidence. Only after separate authorization may the inactive acknowledgement policy be considered for integration.
5. **Rollback + reliability:** separately authorized rollback rehearsal, then demonstrate actual scheduled/manual behavior and freshness. Review all gates independently before any release decision.

## Approval / go-no-go

- **GO only for offline documentation and tests** already isolated on `repair-batches-17a-20-20261021`.
- **NO-GO for release, deployment, integration, live testing or promotion** while any gate above lacks independent evidence and explicit authorization.
- This checklist is not evidence of a completed live backup, historical replay, authenticated delivery, rollback or production parity.
- No merge, deployment, production access, history deletion, model promotion, release-gate weakening, new service or volume changes.

**Release decision: BLOCKED.**
