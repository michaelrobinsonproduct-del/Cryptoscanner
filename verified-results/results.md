# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T21:16:19.974259+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45702510178
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 59853040e737f5f9e076de811dd70fe06f13bbfc (atomic ledger/results publication)
**Ledger generation:** 1768 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 42.41 | 86.273 | 79.373 | +3.82% | -0.12% | 1.75x | 4.7 | 2026-11-25T21:16:10.926244+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SUI/USD | 0.6633 | 85.875 | 71.327 | +2.44% | -0.09% | 2.79x | 1.5 | 2026-11-25T21:16:10.926244+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XMR/USD | 520.67 | 81.467 | 66.937 | +2.17% | -0.09% | 6.65x | 6.5 | 2026-11-25T21:16:10.926244+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XRP/USD | 0.94393 | 81.286 | 70.135 | +2.20% | +0.33% | 1.95x | 0.5 | 2026-11-25T21:16:10.926244+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | ADA/USD | 0.146957 | 80.370 | 65.411 | +1.80% | -0.01% | 3.93x | 4.4 | 2026-11-25T21:16:10.926244+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.0136 | 76.109 | 84.335 | +4.48% | -0.67% | 0.51x | 4.0 | 2026-11-25T21:16:10.926244+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0559521 | 71.721 | 56.347 | +1.29% | +0.07% | 7.91x | 0.1 | 2026-11-25T21:16:10.926244+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 8 | SOL/USD | 70.46 | 71.650 | 62.940 | +1.24% | -0.04% | 1.89x | 1.4 | 2026-11-25T21:16:10.926244+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 9 | PAXG/USD | 3567.03 | 71.440 | 59.337 | +0.71% | -0.11% | 2.26x | 1.3 | 2026-11-25T21:16:10.926244+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 10 | HYPE/USD | 61.76 | 70.054 | 76.288 | +3.16% | -0.05% | 0.40x | 1.6 | 2026-11-25T21:16:10.926244+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XLM/USD | 0.128145 | 68.126 | 65.705 | +3.30% | -0.09% | 1.29x | 2.7 | 2026-11-25T21:16:10.926244+00:00 | Not calibrated | WEAK 44/100 | HIGH 61/100 | Watch | WATCH |
| 12 | LINK/USD | 9.06872 | 64.938 | 64.521 | +2.57% | -0.37% | 1.22x | 3.7 | 2026-11-25T21:16:10.926244+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 84.335 | 3.0136 | -0.67% | 0.51x |
| 2 | LTC/USD | 79.373 | 42.41 | -0.12% | 1.75x |
| 3 | HYPE/USD | 76.288 | 61.76 | -0.05% | 0.40x |
| 4 | SUI/USD | 71.327 | 0.6633 | -0.09% | 2.79x |
| 5 | XRP/USD | 70.135 | 0.94393 | +0.33% | 1.95x |
| 6 | XMR/USD | 66.937 | 520.67 | -0.09% | 6.65x |
| 7 | XLM/USD | 65.705 | 0.128145 | -0.09% | 1.29x |
| 8 | ADA/USD | 65.411 | 0.146957 | -0.01% | 3.93x |
| 9 | LINK/USD | 64.521 | 9.06872 | -0.37% | 1.22x |
| 10 | SOL/USD | 62.940 | 70.46 | -0.04% | 1.89x |
| 11 | PAXG/USD | 59.337 | 3567.03 | -0.11% | 2.26x |
| 12 | XDG/USD | 56.347 | 0.0559521 | +0.07% | 7.91x |

The baseline ordering is over this same confirmed WATCH pool, not an independent full-market baseline scan.
The separate legacy-inspired scanner publishes its own WATCH signals in a later, read-only GitHub artifact linked by this paper run ID.

**30%+ in 48h probability:** NOT CALIBRATED. The separate signal-confidence index (0–100) expresses current setup strength, NOT odds of a gain. Risk varies by spread, momentum and volume; every candidate remains speculative. The action is a research consideration, not an executed or authorized trade. A more substantial entry requires independently qualified held-out calibration.

## Learning and coverage

| Forward horizon | Evidence status | Verified matured / hits |
|---|---|---|
| 1h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 6h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 24h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |
| 48h | PER HORIZON NOT INDEPENDENTLY VERIFIED | NOT VERIFIED |

- Persisted scans: 1768; predictions: 14960; observations: 1071756.
- Matured sampled outcomes across 1/6/24/48h: 32702; gap abstentions: 23091. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45702510178 · **Generation:** 1768 · **Legacy run:** 45702510178
**Main quote time:** 2026-11-25T21:16:19.974259+00:00 · **Legacy report time:** 2026-11-25T21:17:30.223289+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD | 42.41 | 86.27 | -0.12% | 1.75x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 2 | SUI/USD | 0.6633 | 85.88 | -0.09% | 2.79x | STRONG 73/100 | HIGH 61/100 | Watch |
| 3 | XMR/USD | 520.67 | 81.47 | -0.09% | 6.65x | STRONG 71/100 | HIGH 61/100 | Watch |
| 4 | XRP/USD ⭐ | 0.94393 | 81.29 | +0.33% | 1.95x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 5 | ADA/USD | 0.146957 | 80.37 | -0.01% | 3.93x | STRONG 70/100 | HIGH 61/100 | Watch |
| 6 | NEAR/USD | 3.0136 | 76.11 | -0.67% | 0.51x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 7 | XDG/USD | 0.0559521 | 71.72 | +0.07% | 7.91x | STRONG 81/100 | HIGH 55/100 | Watch |
| 8 | SOL/USD | 70.46 | 71.65 | -0.04% | 1.89x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 9 | PAXG/USD | 3567.03 | 71.44 | -0.11% | 2.26x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 10 | HYPE/USD | 61.76 | 70.05 | -0.05% | 0.40x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 11 | XLM/USD | 0.128145 | 68.13 | -0.09% | 1.29x | WEAK 44/100 | HIGH 61/100 | Watch |
| 12 | LINK/USD | 9.06872 | 64.94 | -0.37% | 1.22x | WEAK 42/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.9437 | 82.05 | +0.33% | 1.95x | 41673 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 2 | DRV/USD | 0.35709 | 79.65 | +0.98% | 1.23x | 12137 | STRONG 70/100 | HIGH 68/100 | Watch |
| 3 | PENGU/USD | 0.004339 | 77.68 | +0.09% | 4.25x | 3244 | STRONG 84/100 | HIGH 60/100 | Watch |
| 4 | BCH/USD | 204.24 | 69.97 | +0.10% | 1.31x | 2278 | STRONG 70/100 | HIGH 60/100 | Watch |

**Same-run overlap:** XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
