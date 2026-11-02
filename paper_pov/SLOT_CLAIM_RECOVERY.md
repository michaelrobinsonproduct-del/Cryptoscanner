# D isolated recovery slot-claim implementation (not live)

## Failure mode and proposed architecture

Native GitHub `schedule` at :09/:39 has a measured run-creation deficit. Another
GitHub cron is **not** an independent clock. Existing `paper-external-heartbeat.yml`
accepts only an authenticated owner `issue_comment`, and forwards to the existing
recovery controller. A separate independently timed sender with the owner's
authorized credential is not yet available/certified. Do not call a
`workflow_dispatch` a native run or infer owner-manual from its event type.

`slot_claim_protocol.py` supplies an **isolated, executable, injectable**
GitHub Git-data CAS proposal for the future recovery controller. It is NOT
wired to any live workflow. Each UTC :00/:30 slot maps to exactly one ref
`refs/tags/paper-recovery-slot-v1/YYYYMMDDTHHMMZ`, independent of source SHA
and controller ID. A controller prepares a canonical annotated-tag payload
binding owner comment, controller run, ledger commit, source SHA, decision
digest, UTC slot and `native_schedule=false`. A future authorized adapter
would use GitHub Git-data endpoints to create the tag object, atomically
create the unique ref, and verify exact ref/tag readback before any writer
dispatch. Duplicate ref or ambiguous HTTP failure **blocks**. The isolated
implementation has no GitHub credentials, API calls, dispatch, scanner or
ledger writer. Its tests use an in-memory adapter.

The existing PAPER writer remains `paper-pipeline.yml`, with unchanged
`public-paper-proof-ledger-single-writer` and `cancel-in-progress: false`.
The existing mutex protects running jobs but the default pending queue can
replace pending jobs; optional `queue: max` requires GitHub-environment
compatibility testing and separate authorization. Neither mutex nor slot
tag ref proves global writer exclusivity or exactly-once completion.

## Critical crash/consistency limits

* Creating a tag object before creating its ref can leave an unreachable
  tag object; no slot has been claimed yet.
* A timeout after ref creation may have **claimed the slot**. Never retry
  dispatch automatically; reconcile GitHub ref, workflow runs and ledger.
* A crash after successful claim but before dispatch strands the slot.
  At-most-once cooperative admission is not at-least-once execution.
  An authorized owner must approve a separate recovery/reconciliation
  protocol; no automatic ref deletion, force push or lease expiry.
* A malicious or independently privileged actor can move/delete a tag ref.
  GitHub ruleset/permission review and ref readback are necessary. An
  annotated tag message is content-addressed, not an owner signature.
* Native/manual/recovery must eventually use the **same** durable slot claim
  and the same single writer, otherwise this does not prevent cross-path
  duplicates. GitHub's `workflow_dispatch` response does not include the
  eventual writer run ID; immutable request-to-run attribution remains
  a separate blocker.
* Owner-authenticated external comments require an actual independent
  clock and owner-authorized credential. GitHub Actions alone does not
  guarantee 30-minute trigger creation. No real owner-comment rehearsal
  can be safely run from a PR branch without touching default-branch
  event handling.

## Authorization gates

1. Exact-head offline adversarial tests, source SHA and green PR CI;
   no production writes in the rehearsal.
2. Independent audit certifies GitHub Git-data ref semantics, tag-ref
   protection, owner authentication, permissions, external clock, and
   a bounded, explicit **nonproduction** event route.
3. B implements shared UTC-slot admission for native, recovery and
   owner-manual; simultaneous and crash/retry tests show at most one
   ledger generation and scan ID per slot. Pending queue semantics tested.
4. C verifies no external Railway/Supabase/other writer and obtains a
   linked controller/dispatch/writer request receipt without guessing.
5. V certifies exchange-event quote age <=600s, full results delivery,
   retention invariants and independent audit. Then owner separately
   authorizes any live recovery. No main/cron/writer/scoring change here.

## Test commands

`python -m unittest paper_pov.test_slot_claim_protocol -v`
and the D provenance CI suite on exact PR head.
