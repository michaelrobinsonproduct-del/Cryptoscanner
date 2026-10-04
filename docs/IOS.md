# Kraken Edge iOS

The native app is a cockpit, not the autonomous runtime. It shows scanner state, candidate decisions, alerts, experiments and system health. No service-role, exchange, model-provider or signing secret is embedded in the client. Market/scanner logic remains server-side so it can evolve without downloading self-modifying native code.

A signed device/TestFlight build requires Apple signing authorization at the final distribution step. Simulator compilation remains part of CI before that step.
