# Zero-cost parallel runtime

Until a dedicated always-on challenger worker is justified, GitHub Actions provides scheduled shadow execution and CI at zero incremental hosting cost. The existing Railway production services remain the live control and are only read by the challenger.

This is a validation runtime, not a substitute for a future persistent WebSocket worker. A long-lived worker will be added only through a zero-cost option or after explicit approval for paid infrastructure.
