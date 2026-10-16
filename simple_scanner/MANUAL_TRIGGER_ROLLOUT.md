# Manual scan rollout gate (development only)

## Verified current production configuration
- Railway service: `kraken-simple-validation`.
- Schedule: `*/15 * * * *`.
- Durable volume: `/data`.
- No service domain, no TCP proxy.
- Start command directly executes scan -> history -> shadow learning -> DEX guard.
- Docker CMD is overridden by Railway's configured start command.

## Blocking constraint
The optional `manual_trigger.py` is loopback-only and **not running**.
A Railway cron job starts for scheduled execution; it is not an always-on HTTP
server. Adding a listener file or changing Docker CMD alone does not provide
an external chat invocation path. GitHub Actions and the other Railway
services cannot directly share this service's mounted volume. Never launch
a parallel writer to its SQLite history.

## Non-negotiable acceptance gates
1. Select a supported, authenticated command path that executes **inside this
   same Railway service and mounted volume**, or explicitly approve a migration
   from Railway cron to a continuously running service with an internal
   scheduler. Neither option is implemented.
2. Ensure scheduled and manual invocations both use
   `python -m simple_scanner.execute_once cron|manual` and the same lock.
   The production Railway start-command override must be accounted for.
3. Verify no duplicate scans at overlapping cron/manual times, preserved
   SQLite integrity, DEX freshness, research-only approval, shadow-only
   learning, and expected scan results.
4. Prove authentication, replay/abuse limits, failure handling, and an
   operational rollback. Do not expose the loopback prototype publicly.
5. Verify the latest development CI is green and capture before/after
   production scheduled-run evidence. Deploy only after all gates pass.

## Rollback
Preserve the current production start command, schedule, mounted volume, and
deployed revision. Do not modify these for an unproven trigger. If a future
approved deployment fails, revert its service configuration and revision,
without deleting or recreating the volume.

## Notification policy
Do not create scanner-health email or push notifications. Only scan-result
notifications are in scope.
