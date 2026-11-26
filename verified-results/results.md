# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T12:40:54.835705+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45821706566
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7cd5f73c634b9edd11945625407330110dcf9f24 (atomic ledger/results publication)
**Ledger generation:** 1862 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 588; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 150.72 | 94.054 | 74.501 | +4.09% | +0.91% | 2.58x | 6.0 | 2026-11-26T12:40:48.291257+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SKY/USD | 0.04669 | 93.310 | 75.106 | +11.49% | +0.64% | 4.23x | 8.6 | 2026-11-26T12:40:48.291257+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 3 | LTC/USD | 43.57 | 83.873 | 66.799 | +2.01% | +0.41% | 5.93x | 4.6 | 2026-11-26T12:40:48.291257+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | LINK/USD | 9.22734 | 83.439 | 67.918 | +2.02% | +0.10% | 2.94x | 2.5 | 2026-11-26T12:40:48.291257+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.002654 | 82.325 | 64.674 | +2.99% | +0.53% | 3.59x | 3.8 | 2026-11-26T12:40:48.291257+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | ADA/USD | 0.149014 | 76.969 | 68.833 | +2.23% | +0.25% | 1.69x | 3.5 | 2026-11-26T12:40:48.291257+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | SUI/USD | 0.6684 | 73.109 | 56.458 | +0.32% | +0.33% | 4.52x | 1.5 | 2026-11-26T12:40:48.291257+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | HBAR/USD | 0.05405 | 68.530 | 62.141 | +3.74% | +0.46% | 1.41x | 1.9 | 2026-11-26T12:40:48.291257+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 9 | INJ/USD | 6.202 | 65.555 | 69.357 | +4.17% | +0.62% | 0.31x | 6.5 | 2026-11-26T12:40:48.291257+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SYRUP/USD | 0.07205 | 65.499 | 68.895 | +8.72% | -0.41% | 0.87x | 16.7 | 2026-11-26T12:40:48.291257+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 11 | XRP/USD | 0.95118 | 64.618 | 65.875 | +1.56% | +0.32% | 0.71x | 0.1 | 2026-11-26T12:40:48.291257+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XBT/USD | 60774.2 | 63.496 | 59.695 | +0.67% | +0.38% | 1.19x | 0.0 | 2026-11-26T12:40:48.291257+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 75.106 | 0.04669 | +0.64% | 4.23x |
| 2 | QNT/USD | 74.501 | 150.72 | +0.91% | 2.58x |
| 3 | INJ/USD | 69.357 | 6.202 | +0.62% | 0.31x |
| 4 | SYRUP/USD | 68.895 | 0.07205 | -0.41% | 0.87x |
| 5 | ADA/USD | 68.833 | 0.149014 | +0.25% | 1.69x |
| 6 | LINK/USD | 67.918 | 9.22734 | +0.10% | 2.94x |
| 7 | LTC/USD | 66.799 | 43.57 | +0.41% | 5.93x |
| 8 | XRP/USD | 65.875 | 0.95118 | +0.32% | 0.71x |
| 9 | PUMP/USD | 64.674 | 0.002654 | +0.53% | 3.59x |
| 10 | HBAR/USD | 62.141 | 0.05405 | +0.46% | 1.41x |
| 11 | XBT/USD | 59.695 | 60774.2 | +0.38% | 1.19x |
| 12 | SUI/USD | 56.458 | 0.6684 | +0.33% | 4.52x |

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

- Persisted scans: 1862; predictions: 16079; observations: 1128537.
- Matured sampled outcomes across 1/6/24/48h: 34778; gap abstentions: 24759. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45821706566 · **Generation:** 1862 · **Legacy run:** 45821706566
**Main quote time:** 2026-11-26T12:40:54.835705+00:00 · **Legacy report time:** 2026-11-26T12:41:48.727513+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 150.72 | 94.05 | +0.91% | 2.58x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SKY/USD ⭐ | 0.04669 | 93.31 | +0.64% | 4.23x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | LTC/USD ⭐ | 43.57 | 83.87 | +0.41% | 5.93x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | LINK/USD ⭐ | 9.22734 | 83.44 | +0.10% | 2.94x | STRONG 97/100 | HIGH 55/100 | Watch |
| 5 | PUMP/USD | 0.002654 | 82.33 | +0.53% | 3.59x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 6 | ADA/USD ⭐ | 0.149014 | 76.97 | +0.25% | 1.69x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 7 | SUI/USD | 0.6684 | 73.11 | +0.33% | 4.52x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 8 | HBAR/USD ⭐ | 0.05405 | 68.53 | +0.46% | 1.41x | STRONG 89/100 | HIGH 55/100 | Watch |
| 9 | INJ/USD | 6.202 | 65.56 | +0.62% | 0.31x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 10 | SYRUP/USD | 0.07205 | 65.50 | -0.41% | 0.87x | WEAK 33/100 | VERY_HIGH 79/100 | Do nothing |
| 11 | XRP/USD | 0.95118 | 64.62 | +0.32% | 0.71x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 12 | XBT/USD | 60774.2 | 63.50 | +0.38% | 1.19x | MODERATE 67/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 150.97 | 92.15 | +0.91% | 2.58x | 9191 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SKY/USD ⭐ | 0.04711 | 82.62 | +0.64% | 4.23x | 5011 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | LTC/USD ⭐ | 43.62 | 82.23 | +0.41% | 5.93x | 15676 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | HBAR/USD ⭐ | 0.05407 | 82.12 | +0.46% | 1.41x | 6096 | STRONG 96/100 | HIGH 55/100 | Watch |
| 5 | SEI/USD | 0.03751 | 79.20 | +0.13% | 2.73x | 3297 | STRONG 80/100 | HIGH 66/100 | Watch |
| 6 | ALGO/USD | 0.08069 | 78.43 | +0.15% | 3.55x | 5165 | STRONG 84/100 | HIGH 55/100 | Watch |
| 7 | LINK/USD ⭐ | 9.2429 | 77.93 | +0.10% | 2.94x | 9190 | STRONG 94/100 | HIGH 55/100 | Watch |
| 8 | ADA/USD ⭐ | 0.149317 | 77.06 | +0.25% | 1.69x | 12637 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 9 | DOT/USD | 0.6769 | 71.00 | +0.31% | 1.06x | 7622 | STRONG 70/100 | HIGH 67/100 | Watch |

**Same-run overlap:** QNT/USD, SKY/USD, LTC/USD, LINK/USD, ADA/USD, HBAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
