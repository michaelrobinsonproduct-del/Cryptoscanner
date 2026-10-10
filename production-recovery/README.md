# Isolated production recovery workspace

Production Railway runner and collector currently use base64-encoded Bun programs in their start commands. Their exact contents must **not** be pasted into GitHub until reviewed for secrets, sensitive endpoints, licensing, and deployment-specific values.

## Safe recovery sequence

1. Export each service's current Railway configuration into a restricted local backup, including deployment ID, timestamp, start-command checksum and environment name. Never print credentials or commit raw environment variables.
2. Decode the single base64 argument following `./run.sh` into separate `runner.ts` and `collector.ts` files in a private workspace. Compare a SHA-256 hash of each decoded source against the source recovered from the same Railway configuration twice.
3. Perform secret scanning and manual review. Replace sensitive literals with environment-variable references; keep secrets in Railway. Do not publish unreviewed recovered source.
4. Verify that the recovered programs compile and start with the same Bun runtime as production, using stubbed credentials and network responses.
5. Build deterministic tests for WebSocket timeouts/quarantine, Kraken REST fallback, stale trades/radar, historical-data outages, duplicate cycle IDs, and no actionable signals on stale inputs.
6. Deploy an isolated shadow service with no production alerting, scheduling, or writes until explicitly enabled; compare scans and only promote after the acceptance gates in `docs/production-source-migration.md` pass.

## Triple verification requirements

- **Source integrity:** compare decoded hashes from two independent configuration reads.
- **Behavior:** compile and execute automated tests against mocked healthy and failed market-data inputs.
- **Operations:** prove live shadow deployment revision, fresh end-to-end scan, persistence, and rollback before production cutover.

Current status: production source was decoded during investigation, but source files have not been committed; shadow deployment and tests remain pending. This directory intentionally contains no production code or secrets.
