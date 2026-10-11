-- Read-only labeler performance audit. No production changes.
EXPLAIN SELECT c.id FROM public.kraken_candidate_observations c
WHERE c.observed_at < now()-interval '25 hours'
AND c.observed_at > now()-interval '7 days'
AND c.observed_price > 0 AND c.pair IS NOT NULL
ORDER BY c.observed_at,c.id LIMIT 20;
