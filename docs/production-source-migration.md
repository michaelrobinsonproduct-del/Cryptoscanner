# Production source migration (non-disruptive)

## Verified current deployment topology (2026-10-10)

- Railway runner service `kraken-autonomous-runner` (`fb4dd6e4-5512-4f69-8351-cf042b7038ab`) runs the `ghcr.io/railwayapp/function-bun:1.4.0` image with an embedded start-command payload.
- Railway collector service (`92c5219d-e453-44d0-92c4-86f0705693f4`) uses the same image pattern and has a `/health` healthcheck.
- Neither service is sourced from this GitHub repository. Commits to GitHub do **not** deploy the production services.

## Migration acceptance gates

1. Export the *exact* currently deployed runner and collector source into private version-controlled files. Inspect for credentials, tokens, and sensitive endpoints before committing; move secrets to Railway variables. Preserve original source and deployment identifiers for rollback.
2. Reconstruct the Bun startup/build contract and test it locally. Require static type checks, mocked Kraken HTTP/WebSocket failure tests, stale trade and stale radar tests, timeout/quarantine expiry tests, and no false actionable signals on source failures.
3. Deploy new GitHub-sourced services **in parallel** (shadow mode), without touching production routing, production schedules, or user alerts. Use identical inputs and compare universe coverage, freshness, latency, candidates, persistence, and error counts across consecutive cycles.
4. Require three independent confirmations before promotion: source revision matches deployed commit; automated tests and healthchecks pass; observed end-to-end scans publish fresh verified results with no duplicate cycle IDs. Validate rollback before switching traffic.
5. Promote gradually only after reliability thresholds and 24-hour observation are met. Keep original Railway service configurations available for immediate rollback.

## Safety invariants

- Never turn a stale, unvalidated, or partially confirmed market into an actionable buy candidate.
- WebSocket failure may degrade a market to WATCH/DISCOVERY, but must not silently satisfy freshness requirements.
- Recovery must be idempotent by scan cycle ID; do not equate an unrelated manual dispatch with a recovered scheduled cycle.
- A successful deployment alone is not proof of healthy market data, learning effectiveness, or notification delivery.

## Remaining verification

Source extraction, secret review, test suite, shadow deployment, cycle comparison, live watchdog evidence, DEX coverage, learning effectiveness, and notification delivery are pending. This document is a migration gate, not a claim of completion.
