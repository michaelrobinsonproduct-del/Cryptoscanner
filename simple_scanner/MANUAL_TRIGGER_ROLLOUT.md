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

## Proposed immediate manual-request architecture (isolated branch)
- `simple_scanner.daemon` is a single persistent process, replacing Railway cron **only after explicit acceptance**. It schedules the same scan/history/shadow/DEX pipeline at UTC quarter-hour boundaries and checks authenticated GitHub issue requests every 30 seconds.
- A request must be an open issue titled `MANUAL_SCAN_REQUEST` with label `manual-scan-request`, created within the preceding hour. A single manual scan can satisfy multiple requests; no request content is executed. Request results are posted back to the issue after verified completion.
- Cron and manual invocations both call `simple_scanner.execute_once`, using the same on-volume flock. Manual scans have a five-minute attempt cooldown. If GitHub is unavailable, scheduled scans continue.
- This design does not require a public HTTP endpoint, extra Railway service, or separate SQLite writer. It does require a narrowly scoped GitHub token in the existing service and a single persistent Railway replica.
- **Deployment prerequisites**: capture current service config, volume ID and deployment SHA; validate CI; set GitHub token securely; connect development commit; set start command `python -m simple_scanner.daemon`; remove Railway cron schedule; set appropriate restart policy; verify same /data mount and one replica. Never switch just the branch or just the start command.
- **Live acceptance**: scheduled quarter-hour run and manually created issue both produce same-run SCAN_SUMMARY, WATCH_SUMMARY, HISTORY_PERSISTED, SHADOW_LEARNING, DEX_SUMMARY/DEX_CACHE_REUSED, valid fresh receipt, no duplicate execution, and no historical DB corruption. Confirm 61-minute DEX cache expiry and shadow-only learning.
- **Rollback**: restore original branch `simplified-scanner-recovery-20261011`, original start command and `*/15 * * * *` Railway cron, restart policy NEVER, without recreating /data.
