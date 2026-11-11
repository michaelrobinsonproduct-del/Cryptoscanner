-- Read-only prospective source extract. No future outcome is exposed as an input feature.
-- A challenger decision MUST be separately recorded at observation time before comparison.
-- Run via read-only SQL access; this does not create or alter production tables.
WITH first_seen AS (
 SELECT DISTINCT ON (pair, date_trunc('day', observed_at))
   id AS observation_id, pair, observed_at, scan_fetched_at,
   score, status, confidence, risk, displacement_pct,
   live_validation_success, observed_price,
   discovery_payload->>'model' AS recorded_model
 FROM public.kraken_candidate_observations
 WHERE observed_at IS NOT NULL
   AND observed_at <= now() - interval '24 hours'
   AND coalesce(discovery_payload->>'prospective','false') = 'true'
 ORDER BY pair, date_trunc('day', observed_at), observed_at, id
)
SELECT f.observation_id, f.pair, f.observed_at, f.scan_fetched_at,
 f.score, f.status, f.confidence, f.risk, f.displacement_pct,
 f.live_validation_success, f.observed_price, f.recorded_model,
 o.evaluated_at, o.source AS outcome_source, o.return_24h_pct,
 o.max_return_24h_pct,
 CASE WHEN o.evaluated_at >= f.observed_at + interval '24 hours'
   AND o.max_return_24h_pct IS NOT NULL THEN 'mature_labeled'
   ELSE 'missing_or_immature' END AS label_status
FROM first_seen f
LEFT JOIN public.kraken_candidate_outcomes o ON o.observation_id=f.observation_id
ORDER BY f.observed_at DESC, f.pair
LIMIT 1000;
