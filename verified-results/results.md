# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T16:40:58.045134+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45860789181
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 246e37bb77c0603e8a8f2ba2c08dedd5a6038895 (atomic ledger/results publication)
**Ledger generation:** 1886 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 593; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKY/USD | 0.04595 | 69.864 | 75.259 | +9.72% | -1.03% | 0.98x | 8.7 | 2026-11-26T16:40:48.842271+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 2 | STBL/USD | 0.020383 | 67.985 | 65.918 | +7.93% | -0.05% | 1.23x | 20.2 | 2026-11-26T16:40:48.842271+00:00 | Not calibrated | WEAK 34/100 | EXTREME 92/100 | Do nothing | WATCH |
| 3 | DRV/USD | 0.36666 | 67.415 | 51.431 | +2.48% | +0.20% | 2.66x | 4.1 | 2026-11-26T16:40:48.842271+00:00 | Not calibrated | STRONG 79/100 | HIGH 60/100 | Watch | WATCH |
| 4 | ADA/USD | 0.148036 | 64.173 | 63.956 | +1.55% | -0.32% | 1.18x | 3.9 | 2026-11-26T16:40:48.842271+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 5 | LTC/USD | 43.43 | 62.169 | 64.498 | +1.69% | -0.12% | 0.82x | 4.6 | 2026-11-26T16:40:48.842271+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 6 | QNT/USD | 149.35 | 58.780 | 63.566 | +3.14% | +0.13% | 0.46x | 6.0 | 2026-11-26T16:40:48.842271+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | WIF/USD | 0.1351 | 58.740 | 66.853 | +6.13% | -0.74% | 0.56x | 14.8 | 2026-11-26T16:40:48.842271+00:00 | Not calibrated | WEAK 29/100 | EXTREME 94/100 | Do nothing | WATCH |
| 8 | SOL/USD | 70.79 | 58.457 | 58.272 | +0.57% | -0.27% | 1.15x | 1.4 | 2026-11-26T16:40:48.842271+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XRP/USD | 0.94893 | 54.660 | 63.877 | +1.32% | -0.13% | 0.14x | 0.7 | 2026-11-26T16:40:48.842271+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | HBAR/USD | 0.0535 | 46.438 | 53.046 | +2.69% | -0.37% | 0.53x | 3.7 | 2026-11-26T16:40:48.842271+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 11 | PUMP/USD | 0.002585 | 37.094 | 36.945 | +0.31% | -0.54% | 1.28x | 15.5 | 2026-11-26T16:40:48.842271+00:00 | Not calibrated | WEAK 24/100 | HIGH 67/100 | Do nothing | WATCH |
| 12 | ONDO/USD | 0.28545 | 31.304 | 41.037 | +1.04% | -0.43% | 0.24x | 0.4 | 2026-11-26T16:40:48.842271+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 75.259 | 0.04595 | -1.03% | 0.98x |
| 2 | WIF/USD | 66.853 | 0.1351 | -0.74% | 0.56x |
| 3 | STBL/USD | 65.918 | 0.020383 | -0.05% | 1.23x |
| 4 | LTC/USD | 64.498 | 43.43 | -0.12% | 0.82x |
| 5 | ADA/USD | 63.956 | 0.148036 | -0.32% | 1.18x |
| 6 | XRP/USD | 63.877 | 0.94893 | -0.13% | 0.14x |
| 7 | QNT/USD | 63.566 | 149.35 | +0.13% | 0.46x |
| 8 | SOL/USD | 58.272 | 70.79 | -0.27% | 1.15x |
| 9 | HBAR/USD | 53.046 | 0.0535 | -0.37% | 0.53x |
| 10 | DRV/USD | 51.431 | 0.36666 | +0.20% | 2.66x |
| 11 | ONDO/USD | 41.037 | 0.28545 | -0.43% | 0.24x |
| 12 | PUMP/USD | 36.945 | 0.002585 | -0.54% | 1.28x |

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

- Persisted scans: 1886; predictions: 16367; observations: 1142704.
- Matured sampled outcomes across 1/6/24/48h: 35366; gap abstentions: 25072. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45860789181 · **Generation:** 1886 · **Legacy run:** 45860789181
**Main quote time:** 2026-11-26T16:40:58.045134+00:00 · **Legacy report time:** 2026-11-26T16:41:31.272435+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD | 0.04595 | 69.86 | -1.03% | 0.98x | WEAK 40/100 | VERY_HIGH 77/100 | Watch |
| 2 | STBL/USD | 0.020383 | 67.98 | -0.05% | 1.23x | WEAK 34/100 | EXTREME 92/100 | Do nothing |
| 3 | DRV/USD ⭐ | 0.36666 | 67.42 | +0.20% | 2.66x | STRONG 89/100 | HIGH 60/100 | Watch |
| 4 | ADA/USD | 0.148036 | 64.17 | -0.32% | 1.18x | WEAK 42/100 | HIGH 68/100 | Watch |
| 5 | LTC/USD | 43.43 | 62.17 | -0.12% | 0.82x | WEAK 36/100 | HIGH 68/100 | Watch |
| 6 | QNT/USD | 149.35 | 58.78 | +0.13% | 0.46x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 7 | WIF/USD | 0.1351 | 58.74 | -0.74% | 0.56x | WEAK 29/100 | EXTREME 94/100 | Do nothing |
| 8 | SOL/USD | 70.79 | 58.46 | -0.27% | 1.15x | WEAK 39/100 | HIGH 68/100 | Watch |
| 9 | XRP/USD | 0.94893 | 54.66 | -0.13% | 0.14x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | HBAR/USD | 0.0535 | 46.44 | -0.37% | 0.53x | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing |
| 11 | PUMP/USD | 0.002585 | 37.09 | -0.54% | 1.28x | WEAK 24/100 | HIGH 67/100 | Do nothing |
| 12 | ONDO/USD | 0.28545 | 31.30 | -0.43% | 0.24x | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.36666 | 74.36 | +0.20% | 2.66x | 7758 | STRONG 92/100 | HIGH 60/100 | Watch |

**Same-run overlap:** DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
