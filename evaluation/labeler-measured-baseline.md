# Labeler observation-query measured baseline

Measured on production database 2026-10-11 using read-only `EXPLAIN (ANALYZE, BUFFERS, TIMING OFF)` with `LIMIT 1`; this **executed the SELECT**, not a mutation.

- Execution Time: **8013.589 ms**; planning: 32.228 ms.
- Parallel Seq Scan of `kraken_candidate_observations`, 2 worker loops.
- Actual rows: 67,898 per loop (approximately 135,796 total qualifying rows).
- Shared buffers: 17,034 hits and 820 reads; scan itself: 16,988 hits, 820 reads.
- Gather Merge with top-N heapsort, even for one requested row.
- This is the **candidate-only** query, not the complete labeler function; do not extrapolate exact full-labeler latency.

## Acceptance
Benchmark the shadow and baseline on the same data/snapshot; compare exact candidate tuples and ordering, p50/p95 execution time and buffers. Do not promote until faster under representative load and no eligibility or retry regressions. No production changes were made by this benchmark.
