# Recovery tests (isolated)
Run `bun test production-recovery/market-evidence.test.ts production-recovery/promotion-gate.test.ts` from repository root with Bun installed.
These tests protect a proposed replacement implementation. They are **not wired into the current Railway services** and do not prove production correctness.
The REST fallback flag must be set only after independent live REST ticker, order book and trade validation. A stale trade must never be relabeled fresh simply because the API response arrived recently.
Production cutover remains blocked until source review, CI execution, shadow scan comparison, persistence, alerting and rollback verification.
