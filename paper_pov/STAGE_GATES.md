# Paper proof-of-value: stage 1 execution gate

**State:** research/paper-only. This document does not authorize production trading, deployment, scoring changes, paid services, or a second ledger writer.

## Current stage

- Exactly **one** GitHub-native scheduled paper execution per hour, at minute 9 UTC, using `.github/workflows/paper-pipeline.yml`.
- One repository-wide non-cancelling concurrency group serializes manual and scheduled attempts. The existing `paper-proof-ledger` branch is the sole persistent writer.
- Restore and validate the existing checksum-sealed ledger before any market request; abort on missing/corrupt history, unexpected branch movement, failed tests, stale quotes, or missing artifact. Publish with non-force Git push and remote byte-for-byte readback.
- Only real, timestamped, fresh public Kraken observations and immutable as-of paper predictions count. No actual orders.
- The **45-minute maximum observation gap remains unchanged**. Hourly-only scans normally cannot establish contiguous 1/6/24/48-hour observed outcomes; such horizons must abstain, not be counted as zero hits or failed predictions. The stage-1 cadence is a deliberate temporary safety restriction, **not evidence of predictive success**.

## Stage 2 gate (not authorized by green tests alone)

Before enabling the second scheduled execution per hour (target minutes :00 and :30), independent verification must demonstrate multiple genuine unattended schedule-triggered scans on accepted code, exact remote ledger continuity, integrity under failure/concurrency, durable 30-day artifact recovery, and an accepted reporting path. Record linked run IDs, source SHAs, ledger generations, artifacts, and any gaps in issue #34. Re-run exact-head tests and independent review before editing the cron. Keep a single workflow and single writer, never add a second scanner task/writer.

Matured 1/6/24/48-hour labels, missed-mover audit, same-cohort baseline/challenger comparison and unbiased held-out lift are **separate later gates**. No production promotion is automatic.
