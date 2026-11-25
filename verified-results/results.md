# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T17:57:36.815416+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45669655064
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0a51e71922e5e9b4408f3ce76338f17775b1ee6d (atomic ledger/results publication)
**Ledger generation:** 1747 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.069 | 85.979 | 92.533 | +6.24% | -1.06% | 0.88x | 12.3 | 2026-11-25T17:57:28.799393+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 2 | DRV/USD | 0.34292 | 85.905 | 80.142 | +9.11% | +0.50% | 1.33x | 7.3 | 2026-11-25T17:57:28.799393+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XPL/USD | 0.0479 | 73.094 | 71.067 | +8.86% | +1.49% | 0.46x | 20.9 | 2026-11-25T17:57:28.799393+00:00 | Not calibrated | MODERATE 57/100 | EXTREME 87/100 | Do nothing | WATCH |
| 4 | LTC/USD | 41.89 | 69.832 | 70.432 | +2.55% | +0.55% | 0.66x | 4.8 | 2026-11-25T17:57:28.799393+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6493 | 53.031 | 55.405 | +0.28% | +0.14% | 0.69x | 3.1 | 2026-11-25T17:57:28.799393+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XLM/USD | 0.12572 | 52.010 | 52.626 | +1.34% | +0.39% | 0.75x | 1.0 | 2026-11-25T17:57:28.799393+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | INJ/USD | 5.923 | 51.665 | 44.276 | +1.28% | -0.66% | 2.07x | 6.8 | 2026-11-25T17:57:28.799393+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 8 | SHX/USD | 0.003441 | 48.493 | 33.613 | +0.82% | +1.12% | 1.93x | 5.8 | 2026-11-25T17:57:28.799393+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 9 | XMR/USD | 513.11 | 46.638 | 53.093 | +0.69% | +0.49% | 0.11x | 13.5 | 2026-11-25T17:57:28.799393+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | BCH/USD | 201.12 | 44.117 | 45.556 | +2.00% | +0.42% | 0.65x | 4.0 | 2026-11-25T17:57:28.799393+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | AAVE/USD | 94.31 | 39.812 | 39.734 | +0.44% | +0.18% | 0.92x | 6.4 | 2026-11-25T17:57:28.799393+00:00 | Not calibrated | WEAK 40/100 | HIGH 62/100 | Watch | WATCH |
| 12 | ASTER/USD | 0.49138 | 38.788 | 45.843 | +2.20% | +0.04% | 0.28x | 4.5 | 2026-11-25T17:57:28.799393+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 92.533 | 26.069 | -1.06% | 0.88x |
| 2 | DRV/USD | 80.142 | 0.34292 | +0.50% | 1.33x |
| 3 | XPL/USD | 71.067 | 0.0479 | +1.49% | 0.46x |
| 4 | LTC/USD | 70.432 | 41.89 | +0.55% | 0.66x |
| 5 | SUI/USD | 55.405 | 0.6493 | +0.14% | 0.69x |
| 6 | XMR/USD | 53.093 | 513.11 | +0.49% | 0.11x |
| 7 | XLM/USD | 52.626 | 0.12572 | +0.39% | 0.75x |
| 8 | ASTER/USD | 45.843 | 0.49138 | +0.04% | 0.28x |
| 9 | BCH/USD | 45.556 | 201.12 | +0.42% | 0.65x |
| 10 | INJ/USD | 44.276 | 5.923 | -0.66% | 2.07x |
| 11 | AAVE/USD | 39.734 | 94.31 | +0.18% | 0.92x |
| 12 | SHX/USD | 33.613 | 0.003441 | +1.12% | 1.93x |

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

- Persisted scans: 1747; predictions: 14708; observations: 1058967.
- Matured sampled outcomes across 1/6/24/48h: 32504; gap abstentions: 22614. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45669655064 · **Generation:** 1747 · **Legacy run:** 45669655064
**Main quote time:** 2026-11-25T17:57:36.815416+00:00 · **Legacy report time:** 2026-11-25T17:58:32.890106+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 26.069 | 85.98 | -1.06% | 0.88x | WEAK 43/100 | VERY_HIGH 78/100 | Watch |
| 2 | DRV/USD ⭐ | 0.34292 | 85.91 | +0.50% | 1.33x | STRONG 98/100 | HIGH 55/100 | Watch |
| 3 | XPL/USD | 0.0479 | 73.09 | +1.49% | 0.46x | MODERATE 57/100 | EXTREME 87/100 | Do nothing |
| 4 | LTC/USD | 41.89 | 69.83 | +0.55% | 0.66x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 5 | SUI/USD | 0.6493 | 53.03 | +0.14% | 0.69x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 6 | XLM/USD | 0.12572 | 52.01 | +0.39% | 0.75x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 7 | INJ/USD | 5.923 | 51.66 | -0.66% | 2.07x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 8 | SHX/USD | 0.003441 | 48.49 | +1.12% | 1.93x | MODERATE 69/100 | HIGH 67/100 | Watch |
| 9 | XMR/USD | 513.11 | 46.64 | +0.49% | 0.11x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 10 | BCH/USD | 201.12 | 44.12 | +0.42% | 0.65x | MODERATE 52/100 | VERY_HIGH 75/100 | Watch |
| 11 | AAVE/USD | 94.31 | 39.81 | +0.18% | 0.92x | WEAK 40/100 | HIGH 62/100 | Watch |
| 12 | ASTER/USD | 0.49138 | 38.79 | +0.04% | 0.28x | WEAK 39/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.34198 | 78.06 | +0.50% | 1.33x | 11130 | STRONG 89/100 | HIGH 61/100 | Watch |

**Same-run overlap:** DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
