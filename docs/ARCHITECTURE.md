# Architecture

## Control plane
The existing Railway/Supabase/:00/:15/:30/:45 scanner remains the production control. This repository is a parallel challenger and must not mutate or disable the control during buildout.

## Challenger data path
Kraken WS v2 + official REST -> collectors -> normalized observations -> features -> discovery ranking -> independent acceptance verifier -> second still-early refresh -> decision ledger -> alerts/iOS.

## Promotion invariants
An actionable promotion requires: candidate-specific WS success; current two-sided book; executable BBO; recent trade confirmation; independent official REST confirmation; second refresh; displacement/extension still early relative to the original discovery baseline; and timestamp-comparable cross-venue evidence when used.

Discovery and execution are separate: poor execution may downgrade a candidate to WATCH but must not erase discovery evidence.

## Autonomous improvement
Miss census -> diagnosis -> challenger change -> deterministic tests/backtest -> prospective shadow -> control/challenger comparison -> promotion controller -> immutable release -> rollback. LLM/model providers may propose/review changes but never directly overwrite production.
