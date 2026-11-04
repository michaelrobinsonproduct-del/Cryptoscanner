# Cryptoscanner — 24-hour executable delivery queue

**Purpose:** This file is the authoritative next-action queue for five staggered ChatGPT workers. Issue #34 is the evidence/handoff log. Do not turn this into another audit or status-only workflow. Preserve production and avoid paid Codex/OpenAI API calls.

## Rules (every invocation)
1. Read this queue and the **latest** relevant issue #34 handoff. Pick the first READY item owned by your role. Do not redo an unchanged investigation or test.
2. Check only source files and PRs necessary for that item. Implement as many coherent related changes as safely fit. Make a real diff on an isolated branch, focused tests, and a PR. Never merge/deploy/restart/change production writers or trade without explicit authorization and passing gates.
3. At end, comment on issue #34: item ID, exact changed paths, commit/PR, test command and result, what now works, what is still missing, and the **next exact code action**. A green no-op does not count.
4. If blocked by a missing credential, external service, archive or deployment permission, state the concrete blocker once and immediately work on an independently useful local fallback. No repeated GET-only probes.
5. Claim only work not already owned by an active PR; inspect changed paths to prevent conflicts. Keep existing good components; do not rebuild them.
6. A task is DELIVERED only with verified functional delta; BLOCKED and FAILED are not completion. Do not fabricate labels, held-out uplift, runtime success or deadlines.

## Ordered implementation queue

| ID | Owner | Status | Exact deliverable | Acceptance evidence |
|---|---|---|---|---|
| A1 | A :00 | READY | Trace current scanner entry point and implement any missing deterministic fresh Kraken quote -> ranked WATCH candidate execution path, preserving stablecoin and <=10-minute freshness filters | Executable test proving nonempty candidate on valid fixture, abstention on stale/stablecoin, commit/PR |
| B1 | B :12 | READY | Integrate existing scanner core with the actual manual and scheduled entry points; resolve conflicting open PR implementation only where necessary | Same candidate/schema for manual vs scheduled fixture, focused test and PR |
| D1 | D :24 | READY | Fix current executable runtime and durable scan result persistence/recovery; make failed runs visible instead of silently green | Repro of failing case then passing targeted test, persisted result/readback or explicit environment blocker |
| C1 | C :36 | READY | Identify and remove ONE proven duplicated or disconnected implementation blocking integration, with preserved imports and tests | Bounded diff, tests, no removal of active functionality |
| E1 | E :48 | READY | Connect existing historical source rows to source-qualified point-in-time outcome labels; explicit coverage/abstention on incomplete intervals | Real eligible label counts if authenticated, otherwise code/test demonstrating truthful abstention and next source gap |
| E2 | E :48 | NEXT | Compare identical-cohort baseline/challenger chronologically, with 48h purge, liquidity assumptions and held-out results | Numerical evidence with sample sizes, or NO QUALIFIED RULE |
| A2 | A :00 | NEXT | Wire ranked WATCH output to persisted candidate snapshots with price, timestamp, momentum, volume acceleration, risk/status | Contract test and real or fixture-backed output with provenance |
| B2 | B :12 | NEXT | Connect evaluated challenger version and outcome ledger to shadow scoring; no automatic production promotion | Deterministic end-to-end shadow test |
| D2 | D :24 | NEXT | Validate real GitHub scheduled and manually dispatched scanner execution, output persistence, readback, failure reporting | Exact run URLs, actual output freshness and persistence |
| C2 | C :36 | NEXT | Remove remaining proven obsolete duplicate modules/workflows only after verifying they are unused | Focused import/workflow regression tests |
| E3 | E :48 | NEXT | Implement versioned learning feedback and no-improvement fallback; only qualified evidence can promote | Deterministic regression test and held-out comparison |
| ALL | All | FINAL | Integrated acceptance across manual/scheduled parity, stale data, stablecoins, outcomes, recovery, rollback | Actual end-to-end runs, no second writer, exact-code evidence |

**Scheduling:** A :00, B :12, D :24, C :36, E :48 hourly. These are opportunities to execute, not proof of unattended independent execution. Manual run requests may be inline and must not be reported as background runs.

**Progress scoreboard:** Verified live scanner / manual trigger / scheduled trigger / durable ledger / authenticated labels / held-out uplift / applied learning — all remain UNKNOWN until directly evidenced. Record facts, not estimates.

## Consolidated completion batches — 2026-11-04

**Purpose:** Replace repeated tiny test/audit loops with one substantial, implementation-first batch per owner. The prior deadline was missed. No date-based completion claim replaces actual functionality.

**Shared execution contract:** Each owner works its existing active PR/branch, reads only necessary handoffs, and completes multiple coherent functional changes per invocation. Spend effort on implementation and actual blockers, not repeated inventory, new verification frameworks, duplicate CI or status-only reports. Run the minimum focused test needed for changed code, fix observed failures, and continue to the next implementation step. Preserve production: no merge, deploy, trade, second ledger writer, or unauthorized scoring promotion. Never modify another owner's active paths without explicit coordination. Each batch posts exact commit, changed files, functioning output, real CI result if available, unresolved blocker and next code action to issue #34.

| Completion batch | Existing ownership | Functional finish line |
|---|---|---|
| **A — Core WATCH delivery** | #169; paper_pov/scanner.py and preselection | Fresh Kraken quotes through stablecoin/freshness filters to ranked WATCH with price, risk, timestamps, momentum, volume acceleration and durable candidate snapshots. Complete A1+A2 in one batch. |
| **B — Single scan integration** | #159 and #177; scanner/src and manual/scheduled parity | Connect real manual HTTP and scheduled triggers to the same candidate schema and one existing writer, reconcile authentic source receipts, expose useful results and fail visibly. Complete B1+B2 only when learning qualification is available; otherwise keep shadow separate. |
| **C — Architecture convergence** | Existing cleanup PR ownership, avoid A/B/D/E paths | Resolve actual duplicate execution paths, conflicting PR bases/imports and obsolete modules proven unused. Do not delete useful code or create more frameworks. |
| **D — Persistence & recovery** | #178; paper_pov/github_artifact_readback.py and runtime readback | Consume genuine existing public-paper-ledger artifact and SHA256SUMS, restore safely, connect restored data to the existing read-only result consumer, make failed/missing runs visible. Reuse the single writer. Fix the observed flattened artifact acceptance path (commit 1e2b8cd); complete D1+D2. |
| **E — Actual learning** | #172–176; historical outcome and shadow learning modules | Source-qualified historical 1/6/24/48h outcomes, actual hits/misses, chronological same-cohort baseline/challenger, shadow candidate and no-improvement fallback. Never label unverified archives as authenticated or claim uplift without held-out evidence. Complete E1–E3 as far as genuine source data allows; explicitly identify the external source blocker once. |

**Integration order:** A and D independently, B consumes A/D, C resolves only concrete conflicts, E runs independently and supplies qualified shadow evidence to B. Final acceptance is one coordinated manual/scheduled and persistence/recovery check, not a new verification subsystem.

**Success metric:** Functional output and committed code per batch. A green test-only run, repeated status check, or unmerged isolated utility is not completion.
