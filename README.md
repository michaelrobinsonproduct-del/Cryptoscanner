# Cryptoscanner

Autonomous Kraken pre-surge research and execution-validation platform.

## Operating model

- `production-control`: the existing Kraken scanner remains live and unchanged.
- `challenger`: this repository contains the new system built and validated in parallel.
- Promotion is evidence-based and reversible; no challenger replaces production without prospective validation.

## Safety and reliability

- Market-data and scanner logic are deterministic software and do not require an LLM to run.
- AI/model providers are adapters above the scanner, not hard dependencies.
- No exchange withdrawal credentials belong in this repository or the iOS client.
- Production changes require tests, shadow evaluation, promotion criteria, and rollback support.
