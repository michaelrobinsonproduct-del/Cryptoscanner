-- SHADOW ONLY. Do not apply to production without equivalence and latency tests.
-- Returns the same columns and oldest/newest split as the existing labeler.
-- Uses NOT EXISTS to avoid OR predicates on LEFT JOIN outputs.
-- Important: NULL last_failed_at is NOT eligible when a failure row exists.
CREATE OR REPLACE FUNCTION public.kraken_labeler_next_batch_shadow(batch_size integer DEFAULT 30)
RETURNS TABLE(observation_id bigint,pair text,observed_at timestamptz,observed_price numeric)
LANGUAGE sql STABLE
SET search_path TO 'public','pg_catalog'
AS $function$
WITH params AS (SELECT CASE WHEN batch_size BETWEEN 1 AND 100 THEN batch_size ELSE NULL END AS n),
oldest AS MATERIALIZED (
 SELECT c.id,c.pair,c.observed_at,c.observed_price
 FROM public.kraken_candidate_observations c
 WHERE c.observed_at < now()-interval '25 hours' AND c.observed_at > now()-interval '7 days'
 AND c.observed_price > 0 AND c.pair IS NOT NULL
 AND NOT EXISTS (SELECT 1 FROM public.kraken_candidate_outcomes o WHERE o.observation_id=c.id AND o.max_return_24h_pct IS NOT NULL)
 AND NOT EXISTS (SELECT 1 FROM public.kraken_labeler_failures f WHERE f.observation_id=c.id AND (f.attempts >= 5 OR f.last_failed_at >= now()-interval '30 minutes' OR f.attempts IS NULL OR f.last_failed_at IS NULL))
 ORDER BY c.observed_at,c.id LIMIT (SELECT n/2 FROM params)
),
newest AS MATERIALIZED (
 SELECT c.id,c.pair,c.observed_at,c.observed_price
 FROM public.kraken_candidate_observations c
 WHERE c.observed_at < now()-interval '25 hours' AND c.observed_at > now()-interval '7 days'
 AND c.observed_price > 0 AND c.pair IS NOT NULL
 AND NOT EXISTS (SELECT 1 FROM public.kraken_candidate_outcomes o WHERE o.observation_id=c.id AND o.max_return_24h_pct IS NOT NULL)
 AND NOT EXISTS (SELECT 1 FROM public.kraken_labeler_failures f WHERE f.observation_id=c.id AND (f.attempts >= 5 OR f.last_failed_at >= now()-interval '30 minutes' OR f.attempts IS NULL OR f.last_failed_at IS NULL))
 ORDER BY c.observed_at DESC,c.id DESC LIMIT (SELECT n-n/2 FROM params)
)
SELECT x.id,x.pair,x.observed_at,x.observed_price FROM (SELECT * FROM oldest UNION SELECT * FROM newest) x ORDER BY x.observed_at,x.id;
$function$;
-- Rollback: DROP FUNCTION IF EXISTS public.kraken_labeler_next_batch_shadow(integer);
-- Note: invalid batch sizes currently yield zero rows here, unlike the original exception.
-- That behavior MUST be corrected before considering this production-compatible.
