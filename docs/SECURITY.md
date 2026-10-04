# Security boundaries

The iOS application contains no exchange, model-provider, database service-role, signing, or deployment secrets. Public Kraken market data requires no trading key. Autonomous code changes are restricted to challenger paths and cannot directly mutate production, secrets, or iOS signing. A future execution feature must be separately authorized and use least-privilege credentials with withdrawals disabled.

Public expensive trigger endpoints should not be treated as trusted control surfaces. Production promotion/deployment must require server-side authorization and immutable release metadata.
