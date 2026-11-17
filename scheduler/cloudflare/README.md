# Independent API scheduler (Cloudflare Workers Free)

This is an independent clock, not another scanner or writer. It makes one bounded decision per five-minute slot. It never holds a GitHub runner open and does not trade. Existing GitHub cron/recovery remains backup until the independent path is proven. Do not restart the GitHub relay concurrently.

## One-time deployment (account owner)
1. In a Cloudflare Workers Free account, import this public GitHub repository as a Worker using the root directory `scheduler/cloudflare` (or run `npx wrangler deploy` in that directory). Keep the Free plan; the checked-in production configuration is enabled following the owner's activation approval. No public HTTP routes.
2. Create a fine-grained GitHub token restricted to this repository, Actions read/write and Contents read (metadata read is implicit). Add as encrypted Worker secret `GITHUB_TOKEN`, never in Git or chat. The repository sets `ENABLED=true` and uses `keep_vars=true` to retain additional dashboard variables. Check the first scheduled event; logs distinguish STOPPED, MISSING_GITHUB_TOKEN, TICK_STARTED and GitHub HTTP errors without exposing secrets. For CLI deployments use `npx wrangler secret put GITHUB_TOKEN`, and deploy with `--var ENABLED:true` or change the dashboard variable.
3. Confirm Worker log DISPATCH_ACCEPTED, GitHub exact writer run, next tick's VERIFIED receipt and fresh A/B delivery before changing backups. For a temporary stop turn ENABLED off or remove the Cron Trigger in the dashboard. For a persistent stop change the checked-in configuration before redeployment; the declared ENABLED value and triggers are managed by Wrangler. Do not reset the Durable Object while a dispatch is ambiguous.

A single SQLite Durable Object serializes ticks and durably stores the request before dispatch. The optional workflow input only sets a correlation title, not any scanner setting. If the API response is lost, the next invocation searches for that exact title; zero or multiple matches stop dispatch rather than guessing. An operator must inspect the exact attempt before retiring ambiguity. No paid infrastructure is required by design; actual account eligibility and deployment are not established. Keep the existing writer mutex and canonical checksum verification.

Local contract tests: `node --test scheduler/cloudflare/core.test.mjs`.

Policy: meaningful scanner runs only; no idle GitHub jobs, no quota circumvention. GitHub and Cloudflare quotas still apply. No five-minute delivery guarantee until measured.
