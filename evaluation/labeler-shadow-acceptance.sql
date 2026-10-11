-- Run ONLY after shadow function is installed in a disposable test database.
-- Baseline and shadow must return identical ordered tuples for valid batch sizes.
-- Fixed time boundaries are desirable for repeatability: execute in one transaction.
BEGIN READ ONLY;
WITH sizes(n) AS (VALUES (1),(2),(30),(100)),
comparison AS (
 SELECT n,
 (SELECT jsonb_agg(to_jsonb(x) ORDER BY x.observed_at,x.observation_id) FROM public.kraken_labeler_next_batch(n) x) AS baseline,
 (SELECT jsonb_agg(to_jsonb(x) ORDER BY x.observed_at,x.observation_id) FROM public.kraken_labeler_next_batch_shadow(n) x) AS shadow
 FROM sizes
)
SELECT n,baseline IS NOT DISTINCT FROM shadow AS equivalent,
 jsonb_array_length(COALESCE(baseline,'[]'::jsonb)) AS baseline_count,
 jsonb_array_length(COALESCE(shadow,'[]'::jsonb)) AS shadow_count
FROM comparison;
ROLLBACK;
-- REQUIRE all equivalent=true; verify NULL failure timestamp semantics.
-- Also test invalid batch sizes: baseline raises batch_size_out_of_range;
-- current shadow candidate DOES NOT yet match this behavior and must not replace baseline.
-- Measure EXPLAIN (ANALYZE, BUFFERS) on representative nonproduction data.
-- Ensure repeated scheduled calls stop timing out before production promotion.
