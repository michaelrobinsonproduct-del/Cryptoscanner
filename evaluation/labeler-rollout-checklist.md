# Outcome labeler performance recovery acceptance

## Evidence
- Production PostgREST calls to `public.kraken_labeler_next_batch(integer)` repeatedly hit SQL statement timeouts.
- Both oldest-first and newest-first candidate-only EXPLAIN plans use parallel sequential scans and sorting despite existing partial `(observed_at,id)` index.
- Production cron jobs #7 and #18 are disabled. Keep this issue separate from labeler performance.

## Required safe rollout
1. Capture baseline query plans, execution time, buffer reads, timeout counts, and exact ordered results on a fixed test snapshot for batch sizes 1, 2, 30 and 100.
2. Trial bounded/index-driven strategies on a shadow database. Reject any strategy that skips eligible observations or changes the oldest/newest split, failed-retry logic, or order.
3. Compare complete returned `(observation_id,pair,observed_at,observed_price)` tuples to original for every test batch. Verify NULL semantics of failure timestamps.
4. Test execution with representative large data, concurrency, and sustained scheduled runs; measure p50/p95 latency and errors, not just EXPLAIN cost.
5. Stage a reversible deployment with rollback SQL and keep live candidate approval fail-closed during rollout.
6. Reactivate health cron #7 and verify durable new system-health rows; then #18 and verify durable pipeline-health rows. Do not declare HEALTHY until the existing strict integrated health view does.
7. Confirm continuous-learning outcomes advance and no missing or duplicate labels. Document observed production results and commit IDs.

**Status:** checklist only. No production change or recovery claim.
