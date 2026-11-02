# OWNER D — Native cadence and recovery repair proposal (audit-only)

Evidence baseline (2026-11-02 17:26:32 UTC): in the complete six-hour GitHub run listing, 12 matured nominal :09/:39 opportunities, 2 native schedule run creations (#41438473450, #41473947157) and 1 workflow_dispatch (#41484528561). At least 10 native creations unrepresented **as of observation**, not 10 permanently dropped named cron events. Native creation gap 4h01m46s; maximum canonical writer queue delay 21s. Writer source SHA: `e3fb5ec272d74a72f19e306c1825aae1b7960576`. Recovery controller #41484427220 logged a 16:09 missed-slot marker and HTTP dispatch acceptance; correlation to #41484528561 is temporal, not causally attested.

## Smallest production repair, NOT authorized to implement here

Keep one existing canonical PAPER writer workflow and existing production ledger. Introduce a separate, independently clocked **controller** that checks matured :09/:39 slots after a defined grace period, authenticates the actual GitHub native run listing and persisted scan IDs, and requests a recovery only when missing. The controller must carry a durable slot idempotency key (UTC slot + writer source SHA), compare-and-swap ownership lease and a globally shared writer lock across native, recovery and explicit owner-manual entry points. On uncertainty, abstain and report rather than dispatch. Never equate GitHub `workflow_dispatch` with owner-manual. Do not modify live cron/writer/ledger until audit certification and explicit approval.

For causal attribution, write immutable signed/verified controller request ID, intended UTC slot, controller run ID, dispatch request time, writer run ID, source SHA and readback receipt into an independently readable audit record. The current GitHub event and timing alone do not supply this link. Distinguish owner-manual requests using authenticated initiating actor/request context, not merely workflow event type. Record exchange-event timestamp and first-observed time for each quote; abstain when exchange time is unavailable or age exceeds 600s. Confirm end-user results receipt with an independent delivery acknowledgment; GitHub artifact publication is insufficient.

## Failure-injection acceptance

1. Delayed, skipped, boundary-early and rerun `schedule` events never get invented cron-slot provenance.
2. Duplicate dispatch IDs, controller IDs, shared controller request for two writer runs, foreign branch/workflow/source and malformed times abstain; controller timing is candidate-only.
3. Recovery/manual/native race for same UTC slot yields at most one persisted scan and one ledger generation increment, including crash/retry/replay.
4. Writer job overlap across *all* entry points is rejected before any persistence; external writers must be independently inventoried and excluded.
5. Source-authenticated Kraken event age <=600s and identical source/decision semantics for contemporaneous owner-manual/native runs; unknown timestamps fail closed.
6. Delivery verified by independently observed user receipt, not only `PAPER_RESULTS_VERIFIED` log or GitHub artifact.

Current isolated patch changes only read-only recovery-correlation diagnostics and adversarial tests. No scanner dispatch, writer, ledger, cron, scoring, production infrastructure or trading mutation.
