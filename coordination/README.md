# Cryptoscanner engineering coordination

The canonical backlog is `coordination/workqueue.json` after this PR is reviewed and merged. Until then, use this branch as a proposed queue and issue #34 as the active coordination record.

## Per-run contract

1. Read latest main, issue #34, and queue; verify exact branch heads.
2. Select highest-priority unblocked item owned by your role. Never claim an item that another owner is implementing.
3. Work on an isolated branch; do not use this coordination branch for feature changes.
4. Execute multiple implement/test/repair cycles while runtime allows. If blocked, record the precise source and move to the next independent item.
5. At handoff, record work item ID, immutable commit SHA, exact tests and results, numerical evidence, artifacts, blocker and next executable step in issue #34.
6. Only the coordinator edits the queue, using the current GitHub blob SHA and optimistic conflict detection. Others propose changes in issue #34. Do not treat an advisory lease as authorization to overwrite concurrent changes.
7. Close items only after their acceptance criteria are evidenced. CI green alone is not evidence of predictive lift.

## Safety

No new production writers, live scoring/model promotion, cron edits, trading, Railway or Supabase changes, or merges without independently reviewed gates. Data provenance and point-in-time integrity are required; missing observations abstain. Avoid redundant audits and repeated testing when the exact commit and artifact are unchanged.

## Throughput measurements

Count substantive code commits, fixed defects, exact-head tests, historical pair-time samples with usable outcomes, missed +20/+30% movers, false positives, held-out challenger lift and runtime gaps. A scheduled task run is not an engineering deliverable.
