# Cryptoscanner

Autonomous Kraken pre-surge research and execution-validation platform.

## Operating model

- `production-control`: the existing Kraken scanner remains live and unchanged.
- `challenger`: this repository contains the new system built and validated in parallel.
- Promotion is evidence-based and reversible; no challenger replaces production without prospective validation.

## Safety and reliability

- Market-data and scanner logic are deterministic software and do not require an LLM to run.
- AI/model providers are adapters above the scanner, not hard dependencies.
- No exchange withdrawal credentials belong in this repository or the iOS client.
- Production changes require tests, shadow evaluation, promotion criteria, and rollback support.

## Current challenger capabilities

- Independent Kraken execution confirmation with second refresh.
- Discovery-baseline extension gate and stale/asynchronous quote rejection.
- Stateful microstructure and trajectory feature library.
- Prospective mover/miss accounting, lead-time and early-displacement metrics.
- Control-vs-challenger scorecards with deterministic promotion/rejection gates.
- Scheduled zero-incremental-cost shadow evaluation.
- Native SwiftUI Kraken Edge cockpit with scanner, alerts, experiments, health and settings.

## Validation

`bun test`, `bun run validate`, `bun run live-smoke`, and `bun run shadow` are wired into the repository. CI never mutates the production control.


## Current operating state

Production remains the unchanged control. The replacement engine runs as a shadow challenger on a free scheduled runtime and persists explicit cycle evidence. Promotion is fail-closed and requires independent fresh executable Kraken confirmation plus sufficient prospective evidence; historical backtests alone cannot authorize a production change.

