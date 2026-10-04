# Zero-cost build plan

Production remains on the already-running Railway services. Incremental challenger validation uses the private GitHub repository, GitHub Actions scheduling/CI and existing data services, so no additional Railway service is required for this stage. A persistent second WebSocket worker is intentionally deferred until it can be hosted without incremental cost or consolidated safely without weakening the production control.
