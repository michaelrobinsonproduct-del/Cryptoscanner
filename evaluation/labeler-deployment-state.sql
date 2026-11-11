-- Read-only acceptance query: inspect actual deployment state.
SELECT to_regprocedure('public.kraken_labeler_next_batch_shadow(integer)')::text AS shadow_function,
 (SELECT active FROM cron.job WHERE jobid=7) AS health_job_active,
 (SELECT active FROM cron.job WHERE jobid=18) AS pipeline_job_active;
-- Observed 2026-10-11: shadow_function NULL, both active FALSE.
-- Do not interpret GitHub branch commits as deployed production changes.
