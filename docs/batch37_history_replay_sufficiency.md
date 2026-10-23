# Batch 37 — Historical schema, outcome joins and scoring replay sufficiency

Scope: read-only review of `simple_scanner/history.py`, `scan.py`, `offline_replay.py`, `offline_scoring_comparison.py`. No code or CI changes.

## Actual SQLite schema

- `snapshots(run_at,pair,price,score)`: selected watch candidates only, keyed by run and pair.
- `candidate_features(run_at,pair,base_score,early_signal_score,move_15m_pct,volume_accel,research_rank,base_rank)`: selected watch candidates only; several nullable fields; `base_rank` added by migration.
- `market_observations(run_at,pair,price)`: observed market prices, all reported pairs when `market_prices` is available, else watchlist only.
- `market_signals(run_at,pair,move24_pct,spread_bps,notional_24h_usd)`: all valid reported pairs with matching market prices.
- `outcomes(run_at,pair,horizon_hours,evaluated_at,return_pct)`: selected snapshot returns for 1, 3, 6 and 24 hours.

All candidate/outcome joins require **both** `run_at` and `pair`; outcomes additionally distinguish `horizon_hours`. `evaluated_at` is the actual observation timestamp, not necessarily the target horizon. Outcomes use the earliest observation in `[run_at+horizon,run_at+horizon+1h)`; absent observations remain missing rather than using later prices. Comparing only rows with outcomes introduces survivor/coverage bias unless missingness is explicitly measured.

## Retention and replay caveats

`history.persist` removes `market_observations` and `market_signals` older than 24h when the timestamp minute is >=15, retaining hourly-anchor records. Selected snapshots, features and outcomes are not targeted by that deletion. Therefore original 15-minute/5-minute source granularity and intermediate screen results cannot be recovered from this database alone. The code comment describing one-year history is not a verified retention bound; the shown SQL has no one-year cutoff.

`offline_replay.replay_feasibility` only counts signals, distinct timestamps and observations. `cohort_split` can embargo chronological cohorts but cannot supply missing raw features or establish point-in-time availability. `offline_scoring_comparison.compare_cohorts` uses supplied feature tuples and a caller-provided challenger score; it does not run actual pinned legacy and production scoring implementations.

## Minimum immutable export

1. **Provenance:** approved read-only source identity, export timestamp, SHA-256 manifest, table schema/migrations, row counts, min/max timestamps, time zones, retention rules, run IDs, scanner versions and configuration hashes; preserve an immutable copy.
2. **Existing database:** full `snapshots`, `candidate_features`, `market_signals`, `market_observations`, `outcomes`, plus missing/outcome coverage and source freshness diagnostics. Join on `(run_at,pair)`, and `horizon_hours` for outcomes.
3. **Historical decision reconstruction (not stored in DB):** each scan's complete eligible pair universe, asset metadata/eligibility, Kraken ticker bid/ask/open/last/volume, raw precision and source timestamps, screening failures and reasons, preselection rank, diversified selection order, all completed five-minute OHLC close/volume bars used, OHLC freshness and failed validations, source availability and errors, exact score/rank/tie-break semantics.
4. **Actual parity:** immutable versioned source/config/weights for both legacy and production implementations, historical feature snapshots that were available **at decision time**, original watchlists, per-pair scores and candidate selection decisions. If the legacy implementation or point-in-time inputs are unavailable, parity is **not demonstrable**.
5. **Unbiased outcomes:** full market observation provenance, exact first eligible observation per horizon, missingness and outage coverage for selected **and unselected** pairs; embargoed chronological holdout and explicit selection-budget matching. Missing outcomes must not be filled with hindsight prices.

## Sufficiency decision

- **Partial historical watchlist evaluation:** potentially feasible from an independently authenticated immutable copy of existing SQLite, subject to integrity, completeness and missingness audit.
- **Full historical scanner replay and genuine legacy-vs-production parity:** **not feasible from the currently defined SQLite tables alone**; needs point-in-time raw ticker/OHLC and versioned implementation evidence from independently verified historical sources.
- **No safe correction to `history.py` justified now:** changing retention, score logic or schema before real data and parity evidence risks regression. No new fixture tests or infrastructure.

**Release gates BLOCKED:** independent live backup, genuine historical replay, actual scoring parity, authenticated delivery integration, live rollback, scheduled reliability. No merge, deployment, production access, history deletion, model promotion or release-gate weakening.
