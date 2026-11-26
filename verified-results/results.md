# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T07:36:18.440433+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45776340870
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9a38b41654f811610ca0e4005f65017954da7b34 (atomic ledger/results publication)
**Ledger generation:** 1831 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ME/USD | 0.0392 | 71.833 | 62.539 | +6.23% | +0.77% | 1.54x | 25.5 | 2026-11-26T07:36:11.656396+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 2 | SYRUP/USD | 0.07174 | 71.525 | 59.044 | +8.25% | -0.50% | 3.69x | 36.4 | 2026-11-26T07:36:11.656396+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 3 | ZRO/USD | 1.072 | 69.184 | 63.815 | +4.69% | +0.00% | 1.54x | 18.6 | 2026-11-26T07:36:11.656396+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LTC/USD | 43.32 | 64.656 | 63.843 | +1.43% | -0.16% | 1.16x | 2.3 | 2026-11-26T07:36:11.656396+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 5 | INJ/USD | 6.096 | 59.718 | 57.394 | +2.38% | -0.18% | 1.32x | 3.3 | 2026-11-26T07:36:11.656396+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XRP/USD | 0.95119 | 58.960 | 65.462 | +1.56% | -0.03% | 0.37x | 0.9 | 2026-11-26T07:36:11.656396+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | ADA/USD | 0.147547 | 57.981 | 63.499 | +1.22% | -0.47% | 0.68x | 0.1 | 2026-11-26T07:36:11.656396+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | SKY/USD | 0.04385 | 56.449 | 63.103 | +4.70% | +0.05% | 0.31x | 6.8 | 2026-11-26T07:36:11.656396+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | SOL/USD | 70.84 | 54.993 | 58.769 | +0.64% | -0.10% | 0.67x | 1.4 | 2026-11-26T07:36:11.656396+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | TAO/USD | 183.3466 | 52.128 | 58.320 | +0.97% | +0.03% | 0.37x | 6.9 | 2026-11-26T07:36:11.656396+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | DOT/USD | 0.6639 | 51.440 | 37.567 | +0.85% | -0.23% | 8.63x | 3.0 | 2026-11-26T07:36:11.656396+00:00 | Not calibrated | MODERATE 56/100 | HIGH 66/100 | Watch | WATCH |
| 12 | LINK/USD | 9.14616 | 51.057 | 61.569 | +1.12% | -0.28% | 0.09x | 1.5 | 2026-11-26T07:36:11.656396+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 65.462 | 0.95119 | -0.03% | 0.37x |
| 2 | LTC/USD | 63.843 | 43.32 | -0.16% | 1.16x |
| 3 | ZRO/USD | 63.815 | 1.072 | +0.00% | 1.54x |
| 4 | ADA/USD | 63.499 | 0.147547 | -0.47% | 0.68x |
| 5 | SKY/USD | 63.103 | 0.04385 | +0.05% | 0.31x |
| 6 | ME/USD | 62.539 | 0.0392 | +0.77% | 1.54x |
| 7 | LINK/USD | 61.569 | 9.14616 | -0.28% | 0.09x |
| 8 | SYRUP/USD | 59.044 | 0.07174 | -0.50% | 3.69x |
| 9 | SOL/USD | 58.769 | 70.84 | -0.10% | 0.67x |
| 10 | TAO/USD | 58.320 | 183.3466 | +0.03% | 0.37x |
| 11 | INJ/USD | 57.394 | 6.096 | -0.18% | 1.32x |
| 12 | DOT/USD | 37.567 | 0.6639 | -0.23% | 8.63x |

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

- Persisted scans: 1831; predictions: 15707; observations: 1110123.
- Matured sampled outcomes across 1/6/24/48h: 34046; gap abstentions: 24226. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45776340870 · **Generation:** 1831 · **Legacy run:** 45776340870
**Main quote time:** 2026-11-26T07:36:18.440433+00:00 · **Legacy report time:** 2026-11-26T07:37:28.750572+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ME/USD | 0.0392 | 71.83 | +0.77% | 1.54x | STRONG 71/100 | VERY_HIGH 79/100 | Watch |
| 2 | SYRUP/USD | 0.07174 | 71.53 | -0.50% | 3.69x | MODERATE 51/100 | VERY_HIGH 78/100 | Watch |
| 3 | ZRO/USD | 1.072 | 69.18 | +0.00% | 1.54x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | LTC/USD | 43.32 | 64.66 | -0.16% | 1.16x | WEAK 42/100 | HIGH 68/100 | Watch |
| 5 | INJ/USD | 6.096 | 59.72 | -0.18% | 1.32x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 6 | XRP/USD | 0.95119 | 58.96 | -0.03% | 0.37x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | ADA/USD | 0.147547 | 57.98 | -0.47% | 0.68x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | SKY/USD | 0.04385 | 56.45 | +0.05% | 0.31x | MODERATE 48/100 | VERY_HIGH 75/100 | Watch |
| 9 | SOL/USD | 70.84 | 54.99 | -0.10% | 0.67x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | TAO/USD | 183.3466 | 52.13 | +0.03% | 0.37x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 11 | DOT/USD | 0.6639 | 51.44 | -0.23% | 8.63x | MODERATE 56/100 | HIGH 66/100 | Watch |
| 12 | LINK/USD | 9.14616 | 51.06 | -0.28% | 0.09x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
