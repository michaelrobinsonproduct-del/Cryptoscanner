# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T21:41:03.532112+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45899642376
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9c8a64a96df14b7c6e12c7529a4eaa42a710f1ba (atomic ledger/results publication)
**Ledger generation:** 1917 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.36926 | 94.466 | 77.775 | +3.59% | +0.34% | 42.33x | 4.7 | 2026-11-26T21:40:55.776654+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | DRV/USD | 0.39188 | 86.245 | 80.089 | +9.52% | +0.42% | 1.41x | 4.9 | 2026-11-26T21:40:55.776654+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XRP/USD | 0.95323 | 83.259 | 67.407 | +1.78% | +0.17% | 9.42x | 0.1 | 2026-11-26T21:40:55.776654+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SOL/USD | 71.61 | 78.652 | 66.434 | +1.73% | +0.22% | 2.11x | 1.4 | 2026-11-26T21:40:55.776654+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | ETH/USD | 1705.62 | 77.001 | 61.269 | +0.90% | +0.15% | 2.53x | 0.1 | 2026-11-26T21:40:55.776654+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ADA/USD | 0.150317 | 76.963 | 74.274 | +3.12% | -0.34% | 1.44x | 5.1 | 2026-11-26T21:40:55.776654+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 7 | INJ/USD | 6.286 | 75.628 | 76.315 | +5.58% | -0.10% | 0.98x | 4.8 | 2026-11-26T21:40:55.776654+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 8 | WIF/USD | 0.1374 | 73.921 | 73.237 | +7.93% | +0.37% | 0.89x | 7.3 | 2026-11-26T21:40:55.776654+00:00 | Not calibrated | MODERATE 67/100 | HIGH 67/100 | Watch | WATCH |
| 9 | LTC/USD | 44.15 | 70.293 | 77.469 | +3.37% | +0.18% | 0.19x | 2.3 | 2026-11-26T21:40:55.776654+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | HBAR/USD | 0.05496 | 69.546 | 72.552 | +5.49% | +0.13% | 0.64x | 1.8 | 2026-11-26T21:40:55.776654+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | XBT/USD | 60844.7 | 68.798 | 60.512 | +0.79% | +0.04% | 1.81x | 0.0 | 2026-11-26T21:40:55.776654+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 12 | HYPE/USD | 63.19 | 66.854 | 72.044 | +2.55% | -0.25% | 0.61x | 1.6 | 2026-11-26T21:40:55.776654+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 80.089 | 0.39188 | +0.42% | 1.41x |
| 2 | LINK/USD | 77.775 | 9.36926 | +0.34% | 42.33x |
| 3 | LTC/USD | 77.469 | 44.15 | +0.18% | 0.19x |
| 4 | INJ/USD | 76.315 | 6.286 | -0.10% | 0.98x |
| 5 | ADA/USD | 74.274 | 0.150317 | -0.34% | 1.44x |
| 6 | WIF/USD | 73.237 | 0.1374 | +0.37% | 0.89x |
| 7 | HBAR/USD | 72.552 | 0.05496 | +0.13% | 0.64x |
| 8 | HYPE/USD | 72.044 | 63.19 | -0.25% | 0.61x |
| 9 | XRP/USD | 67.407 | 0.95323 | +0.17% | 9.42x |
| 10 | SOL/USD | 66.434 | 71.61 | +0.22% | 2.11x |
| 11 | ETH/USD | 61.269 | 1705.62 | +0.15% | 2.53x |
| 12 | XBT/USD | 60.512 | 60844.7 | +0.04% | 1.81x |

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

- Persisted scans: 1917; predictions: 16739; observations: 1161217.
- Matured sampled outcomes across 1/6/24/48h: 36404; gap abstentions: 25280. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45899642376 · **Generation:** 1917 · **Legacy run:** 45899642376
**Main quote time:** 2026-11-26T21:41:03.532112+00:00 · **Legacy report time:** 2026-11-26T21:41:44.691723+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.36926 | 94.47 | +0.34% | 42.33x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | DRV/USD ⭐ | 0.39188 | 86.25 | +0.42% | 1.41x | STRONG 98/100 | HIGH 55/100 | Watch |
| 3 | XRP/USD ⭐ | 0.95323 | 83.26 | +0.17% | 9.42x | STRONG 97/100 | HIGH 55/100 | Watch |
| 4 | SOL/USD | 71.61 | 78.65 | +0.22% | 2.11x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 5 | ETH/USD | 1705.62 | 77.00 | +0.15% | 2.53x | STRONG 84/100 | HIGH 55/100 | Watch |
| 6 | ADA/USD | 0.150317 | 76.96 | -0.34% | 1.44x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 7 | INJ/USD | 6.286 | 75.63 | -0.10% | 0.98x | WEAK 43/100 | HIGH 68/100 | Watch |
| 8 | WIF/USD | 0.1374 | 73.92 | +0.37% | 0.89x | MODERATE 67/100 | HIGH 67/100 | Watch |
| 9 | LTC/USD | 44.15 | 70.29 | +0.18% | 0.19x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 10 | HBAR/USD | 0.05496 | 69.55 | +0.13% | 0.64x | MODERATE 55/100 | VERY_HIGH 75/100 | Watch |
| 11 | XBT/USD | 60844.7 | 68.80 | +0.04% | 1.81x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 12 | HYPE/USD | 63.19 | 66.85 | -0.25% | 0.61x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.37768 | 98.84 | +0.34% | 42.33x | 6763 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.95323 | 81.66 | +0.17% | 9.42x | 22299 | STRONG 96/100 | HIGH 55/100 | Watch |
| 3 | DRV/USD ⭐ | 0.39188 | 79.62 | +0.42% | 1.41x | 8088 | STRONG 95/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LINK/USD, DRV/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
