-- Read-only index usage verification; do not reset PostgreSQL statistics.
SELECT indexrelname,idx_scan,idx_tup_read,idx_tup_fetch
FROM pg_stat_user_indexes
WHERE relname='kraken_candidate_observations'
AND indexrelname='kraken_candidate_observations_labeler_time_idx';
-- Observed 2026-10-11: idx_scan=0, idx_tup_read=0, idx_tup_fetch=0.
-- Cumulative since last statistics reset; not proof of why planner avoided it.
