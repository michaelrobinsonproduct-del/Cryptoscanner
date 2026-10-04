# Failure recovery

For every market-data route: canonicalize symbol -> reconnect/resubscribe -> retry -> alternate collector -> official Kraken REST fallback. A candidate discovered before a validation failure remains WATCH rather than disappearing. Stale, one-sided, asynchronous, or non-executable data can never promote a candidate. Failures are recorded as evidence for diagnosis rather than silently converted into negative signals.
