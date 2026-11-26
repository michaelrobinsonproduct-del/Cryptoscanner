# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T15:51:08.719896+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45852895535
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a2785bb499a39232927c17016b1ed0e69fbab20a (atomic ledger/results publication)
**Ledger generation:** 1881 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 592; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.4992 | 86.477 | 62.510 | +5.52% | +1.79% | 3.47x | 18.0 | 2026-11-26T15:51:02.549058+00:00 | Not calibrated | STRONG 93/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | KNTQ/USD | 0.16025 | 78.811 | 71.795 | +5.82% | +0.81% | 1.30x | 0.6 | 2026-11-26T15:51:02.549058+00:00 | Not calibrated | STRONG 74/100 | HIGH 67/100 | Watch | WATCH |
| 3 | STBL/USD | 0.021051 | 70.796 | 65.737 | +11.46% | +2.70% | 0.16x | 20.4 | 2026-11-26T15:51:02.549058+00:00 | Not calibrated | MODERATE 55/100 | EXTREME 94/100 | Do nothing | WATCH |
| 4 | WIF/USD | 0.1343 | 68.336 | 66.058 | +5.50% | +0.68% | 0.89x | 7.5 | 2026-11-26T15:51:02.549058+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 5 | SKY/USD | 0.04548 | 67.236 | 75.077 | +8.60% | -0.68% | 0.55x | 8.8 | 2026-11-26T15:51:02.549058+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | FET/USD | 0.1148 | 63.470 | 65.366 | +5.81% | +0.70% | 0.46x | 17.5 | 2026-11-26T15:51:02.549058+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | LTC/USD | 43.4 | 61.814 | 65.156 | +1.62% | +0.35% | 0.49x | 2.3 | 2026-11-26T15:51:02.549058+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ADA/USD | 0.148049 | 58.489 | 63.140 | +1.56% | +0.46% | 0.30x | 5.6 | 2026-11-26T15:51:02.549058+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XRP/USD | 0.94702 | 55.886 | 62.343 | +1.12% | +0.46% | 0.12x | 1.0 | 2026-11-26T15:51:02.549058+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | LINK/USD | 9.16503 | 55.389 | 61.713 | +1.33% | +0.41% | 0.16x | 5.2 | 2026-11-26T15:51:02.549058+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | SOL/USD | 70.85 | 52.922 | 58.869 | +0.65% | +0.33% | 0.24x | 1.4 | 2026-11-26T15:51:02.549058+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | HBAR/USD | 0.05356 | 52.590 | 53.963 | +2.80% | +0.45% | 0.64x | 3.7 | 2026-11-26T15:51:02.549058+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 75.077 | 0.04548 | -0.68% | 0.55x |
| 2 | KNTQ/USD | 71.795 | 0.16025 | +0.81% | 1.30x |
| 3 | WIF/USD | 66.058 | 0.1343 | +0.68% | 0.89x |
| 4 | STBL/USD | 65.737 | 0.021051 | +2.70% | 0.16x |
| 5 | FET/USD | 65.366 | 0.1148 | +0.70% | 0.46x |
| 6 | LTC/USD | 65.156 | 43.4 | +0.35% | 0.49x |
| 7 | ADA/USD | 63.140 | 0.148049 | +0.46% | 0.30x |
| 8 | AKT/USD | 62.510 | 0.4992 | +1.79% | 3.47x |
| 9 | XRP/USD | 62.343 | 0.94702 | +0.46% | 0.12x |
| 10 | LINK/USD | 61.713 | 9.16503 | +0.41% | 0.16x |
| 11 | SOL/USD | 58.869 | 70.85 | +0.33% | 0.24x |
| 12 | HBAR/USD | 53.963 | 0.05356 | +0.45% | 0.64x |

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

- Persisted scans: 1881; predictions: 16307; observations: 1139741.
- Matured sampled outcomes across 1/6/24/48h: 35246; gap abstentions: 25024. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45852895535 · **Generation:** 1881 · **Legacy run:** 45852895535
**Main quote time:** 2026-11-26T15:51:08.719896+00:00 · **Legacy report time:** 2026-11-26T15:51:57.847100+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.4992 | 86.48 | +1.79% | 3.47x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | KNTQ/USD ⭐ | 0.16025 | 78.81 | +0.81% | 1.30x | STRONG 84/100 | HIGH 67/100 | Watch |
| 3 | STBL/USD | 0.021051 | 70.80 | +2.70% | 0.16x | MODERATE 55/100 | EXTREME 94/100 | Do nothing |
| 4 | WIF/USD | 0.1343 | 68.34 | +0.68% | 0.89x | MODERATE 64/100 | VERY_HIGH 74/100 | Watch |
| 5 | SKY/USD | 0.04548 | 67.24 | -0.68% | 0.55x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |
| 6 | FET/USD | 0.1148 | 63.47 | +0.70% | 0.46x | MODERATE 57/100 | VERY_HIGH 81/100 | Watch |
| 7 | LTC/USD | 43.4 | 61.81 | +0.35% | 0.49x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 8 | ADA/USD | 0.148049 | 58.49 | +0.46% | 0.30x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 9 | XRP/USD | 0.94702 | 55.89 | +0.46% | 0.12x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 10 | LINK/USD | 9.16503 | 55.39 | +0.41% | 0.16x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 11 | SOL/USD | 70.85 | 52.92 | +0.33% | 0.24x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 12 | HBAR/USD | 0.05356 | 52.59 | +0.45% | 0.64x | MODERATE 56/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.4992 | 88.11 | +1.79% | 3.47x | 2972 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | KNTQ/USD ⭐ | 0.16043 | 78.90 | +0.81% | 1.30x | 1523 | STRONG 84/100 | HIGH 67/100 | Watch |
| 3 | SYRUP/USD | 0.06992 | 72.60 | +0.24% | 1.16x | 3668 | MODERATE 66/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** AKT/USD, KNTQ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
