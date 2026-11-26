# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T18:01:18.807061+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45872288488
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d572b9dc09ff1d2641b2dc73141b29db1e94b756 (atomic ledger/results publication)
**Ledger generation:** 1894 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKY/USD | 0.04578 | 90.803 | 75.474 | +9.31% | +0.07% | 3.33x | 8.8 | 2026-11-26T18:01:12.436122+00:00 | Not calibrated | STRONG 90/100 | HIGH 60/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0702 | 73.975 | 59.008 | +0.67% | -0.01% | 2.69x | 1.3 | 2026-11-26T18:01:12.436122+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ADA/USD | 0.149136 | 73.094 | 69.320 | +2.31% | +0.18% | 1.29x | 3.7 | 2026-11-26T18:01:12.436122+00:00 | Not calibrated | MODERATE 62/100 | HIGH 55/100 | Watch | WATCH |
| 4 | WIF/USD | 0.1397 | 67.769 | 69.382 | +9.74% | +0.95% | 0.36x | 14.3 | 2026-11-26T18:01:12.436122+00:00 | Not calibrated | MODERATE 59/100 | EXTREME 88/100 | Do nothing | WATCH |
| 5 | DRV/USD | 0.37852 | 66.808 | 66.215 | +5.79% | +0.48% | 0.82x | 20.4 | 2026-11-26T18:01:12.436122+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | XRP/USD | 0.95177 | 66.116 | 66.211 | +1.62% | +0.35% | 0.81x | 0.3 | 2026-11-26T18:01:12.436122+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 7 | SOL/USD | 71.08 | 64.073 | 61.158 | +0.98% | +0.33% | 1.13x | 1.4 | 2026-11-26T18:01:12.436122+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 8 | 2Z/USD | 0.01755 | 63.581 | 63.975 | +6.23% | +0.23% | 0.85x | 22.8 | 2026-11-26T18:01:12.436122+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 9 | STBL/USD | 0.020203 | 62.387 | 66.092 | +6.97% | -0.17% | 0.71x | 19.8 | 2026-11-26T18:01:12.436122+00:00 | Not calibrated | WEAK 31/100 | EXTREME 94/100 | Do nothing | WATCH |
| 10 | XDG/USD | 0.0568687 | 61.624 | 56.429 | +1.63% | +0.32% | 1.36x | 0.1 | 2026-11-26T18:01:12.436122+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 11 | FET/USD | 0.1164 | 61.481 | 65.455 | +7.28% | +0.35% | 0.43x | 25.8 | 2026-11-26T18:01:12.436122+00:00 | Not calibrated | MODERATE 51/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | LINK/USD | 9.22472 | 58.590 | 66.501 | +1.99% | +0.31% | 0.05x | 4.9 | 2026-11-26T18:01:12.436122+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 75.474 | 0.04578 | +0.07% | 3.33x |
| 2 | WIF/USD | 69.382 | 0.1397 | +0.95% | 0.36x |
| 3 | ADA/USD | 69.320 | 0.149136 | +0.18% | 1.29x |
| 4 | LINK/USD | 66.501 | 9.22472 | +0.31% | 0.05x |
| 5 | DRV/USD | 66.215 | 0.37852 | +0.48% | 0.82x |
| 6 | XRP/USD | 66.211 | 0.95177 | +0.35% | 0.81x |
| 7 | STBL/USD | 66.092 | 0.020203 | -0.17% | 0.71x |
| 8 | FET/USD | 65.455 | 0.1164 | +0.35% | 0.43x |
| 9 | 2Z/USD | 63.975 | 0.01755 | +0.23% | 0.85x |
| 10 | SOL/USD | 61.158 | 71.08 | +0.33% | 1.13x |
| 11 | NEAR/USD | 59.008 | 3.0702 | -0.01% | 2.69x |
| 12 | XDG/USD | 56.429 | 0.0568687 | +0.32% | 1.36x |

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

- Persisted scans: 1894; predictions: 16463; observations: 1147465.
- Matured sampled outcomes across 1/6/24/48h: 35589; gap abstentions: 25118. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45872288488 · **Generation:** 1894 · **Legacy run:** 45872288488
**Main quote time:** 2026-11-26T18:01:18.807061+00:00 · **Legacy report time:** 2026-11-26T18:02:08.958897+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04578 | 90.80 | +0.07% | 3.33x | STRONG 100/100 | HIGH 60/100 | Watch |
| 2 | NEAR/USD | 3.0702 | 73.98 | -0.01% | 2.69x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 3 | ADA/USD ⭐ | 0.149136 | 73.09 | +0.18% | 1.29x | STRONG 72/100 | HIGH 55/100 | Watch |
| 4 | WIF/USD | 0.1397 | 67.77 | +0.95% | 0.36x | MODERATE 59/100 | EXTREME 88/100 | Do nothing |
| 5 | DRV/USD | 0.37852 | 66.81 | +0.48% | 0.82x | MODERATE 53/100 | VERY_HIGH 79/100 | Watch |
| 6 | XRP/USD | 0.95177 | 66.12 | +0.35% | 0.81x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 7 | SOL/USD | 71.08 | 64.07 | +0.33% | 1.13x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 8 | 2Z/USD | 0.01755 | 63.58 | +0.23% | 0.85x | MODERATE 52/100 | VERY_HIGH 79/100 | Watch |
| 9 | STBL/USD | 0.020203 | 62.39 | -0.17% | 0.71x | WEAK 31/100 | EXTREME 94/100 | Do nothing |
| 10 | XDG/USD | 0.0568687 | 61.62 | +0.32% | 1.36x | STRONG 76/100 | HIGH 55/100 | Watch |
| 11 | FET/USD | 0.1164 | 61.48 | +0.35% | 0.43x | MODERATE 51/100 | EXTREME 87/100 | Do nothing |
| 12 | LINK/USD | 9.22472 | 58.59 | +0.31% | 0.05x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04578 | 87.35 | +0.07% | 3.33x | 6514 | STRONG 99/100 | HIGH 60/100 | Watch |
| 2 | HBAR/USD | 0.05414 | 81.60 | +0.43% | 1.11x | 5139 | STRONG 76/100 | HIGH 67/100 | Watch |
| 3 | ADA/USD ⭐ | 0.149191 | 74.87 | +0.18% | 1.29x | 10472 | STRONG 72/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SKY/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
