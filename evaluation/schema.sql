-- Optional persistence schema for a provider-independent deployment.
create table if not exists challenger_cycles(id bigint generated always as identity primary key,created_at timestamptz not null default now(),source_commit text not null,mode text not null default 'shadow',control_untouched boolean not null default true,payload jsonb not null);
create table if not exists challenger_labels(id bigint generated always as identity primary key,created_at timestamptz not null default now(),pair text not null,discovered_at timestamptz,alerted_at timestamptz,threshold_20_at timestamptz,threshold_50_at timestamptz,threshold_100_at timestamptz,max_return_24h numeric,alert_displacement_pct numeric,payload jsonb not null default '{}'::jsonb);

-- Prospective observations retain both accepted and rejected signals; no synthetic prices.
create table if not exists challenger_observations (
  id bigint generated always as identity primary key,
  cycle_id text not null,
  pair text not null,
  observed_at timestamptz not null,
  decision text not null check (decision in ('WATCH','PROMOTION_ELIGIBLE')),
  baseline_ask numeric check (baseline_ask > 0),
  baseline_at timestamptz,
  baseline_status text not null check (baseline_status in ('observed','missing_baseline')),
  source_payload jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  unique(cycle_id,pair),
  check ((baseline_status='observed' and baseline_ask is not null and baseline_at is not null) or (baseline_status='missing_baseline' and baseline_ask is null))
);
create table if not exists challenger_forward_outcomes (
  observation_id bigint not null references challenger_observations(id),
  horizon_hours integer not null check (horizon_hours in (24,48,72)),
  due_at timestamptz not null,
  measured_at timestamptz,
  ask_at_horizon numeric check (ask_at_horizon > 0),
  return_pct numeric,
  status text not null check (status in ('pending','measured','missing_price')),
  primary key(observation_id,horizon_hours),
  check ((status='measured' and measured_at is not null and ask_at_horizon is not null and return_pct is not null) or (status<>'measured' and return_pct is null))
);
