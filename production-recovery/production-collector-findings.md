# Confirmed collector quarantine reporting mismatch

Production collector inspection on 2026-10-10:
- The WebSocket pair validation function enforces a 30-second cooldown after repeated failures.
- The health endpoint's quarantined-pair metric instead counts failures for 30 minutes.
- This causes overstated health metrics, not a 30-minute enforcement block.
- The resilient validation wrapper retries WebSocket checks but does not independently validate REST fallback.

The isolated recovery module `quarantine-health.ts` defines one 30-second constant for enforcement, reporting and expiry. `quarantine-health.test.ts` checks boundary behavior and reporting parity.

These files do not yet modify the live collector. Integrate only after reviewing the recovered production source, passing the test suite, and validating a shadow deployment. Do not treat unverified REST data as fresh.
