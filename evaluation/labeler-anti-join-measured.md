# Anti-join labeler candidate benchmark

2026-10-11 production read-only `EXPLAIN (ANALYZE, BUFFERS, TIMING OFF)` for a `LIMIT 1` eligibility query with `NOT EXISTS` against labeled outcomes and blocked failure retries.

- Execution: **2771.643 ms**; planning **36.169 ms**.
- Shared buffers: **35,027 hits, 756 reads**.
- Still uses parallel sequential scan of observation rows, hash anti joins, and sorting.
- Candidate-only query measured separately earlier at 8013.589 ms, but these are **not comparable A/B tests**: different predicates and execution times, no repeat controls.
- This query is NOT the installed shadow function or full baseline function; no equivalence verified.

## Next gate
Run both baseline and shadow with fixed inputs on the same test snapshot, repeat under similar cache/load conditions, compare returned tuples and p50/p95 latency. Do not promote based on this one result.
