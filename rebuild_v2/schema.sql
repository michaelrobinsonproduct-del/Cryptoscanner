-- Run only in a dedicated private schema or secured project.
-- Exposed public schema: enforce RLS and no anon/authenticated policies.
CREATE TABLE IF NOT EXISTS public.kraken_rebuild_runs (
 run_id text PRIMARY KEY,
 recorded_at timestamptz NOT NULL,
 payload jsonb NOT NULL
);
ALTER TABLE public.kraken_rebuild_runs ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON public.kraken_rebuild_runs FROM anon, authenticated;
CREATE INDEX IF NOT EXISTS kraken_rebuild_runs_recorded_at_idx ON public.kraken_rebuild_runs (recorded_at DESC);
