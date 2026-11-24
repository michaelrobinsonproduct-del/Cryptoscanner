# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T12:11:50.619780+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45390825020
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c8602a9d973ebcc039c4412628750a5483c21a60 (atomic ledger/results publication)
**Ledger generation:** 1572 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.825 | 81.883 | 91.328 | +5.63% | -0.47% | 0.29x | 6.2 | 2026-11-24T12:11:43.418149+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | ICNT/USD | 0.3311 | 67.997 | 65.654 | +7.12% | +1.19% | 0.64x | 24.2 | 2026-11-24T12:11:43.418149+00:00 | Not calibrated | MODERATE 54/100 | EXTREME 87/100 | Do nothing | WATCH |
| 3 | XMR/USD | 498.98 | 67.225 | 69.756 | +2.67% | -0.22% | 0.86x | 7.8 | 2026-11-24T12:11:43.418149+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.452e-06 | 65.524 | 53.824 | +0.88% | -0.66% | 25.97x | 8.7 | 2026-11-24T12:11:43.418149+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 5 | MON/USD | 0.01251 | 64.474 | 78.725 | +8.59% | -1.57% | 0.36x | 16.0 | 2026-11-24T12:11:43.418149+00:00 | Not calibrated | WEAK 32/100 | EXTREME 86/100 | Do nothing | WATCH |
| 6 | LUNA/USD | 4.579e-05 | 62.865 | 51.677 | +5.34% | -0.46% | 2.35x | 35.1 | 2026-11-24T12:11:43.418149+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 7 | GBP/USD | 1.30808 | 50.992 | 57.365 | +0.37% | -0.03% | 0.38x | 0.5 | 2026-11-24T12:11:43.418149+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | NIGHT/USD | 0.04837 | 37.101 | 48.726 | +0.46% | -1.31% | 0.49x | 6.2 | 2026-11-24T12:11:43.418149+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 9 | BABY/USD | 0.00871 | 34.205 | 32.682 | +2.47% | +0.58% | 0.86x | 34.7 | 2026-11-24T12:11:43.418149+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 10 | BAT/USD | 0.07781 | 26.351 | 27.309 | +0.83% | -0.19% | 1.00x | 21.9 | 2026-11-24T12:11:43.418149+00:00 | Not calibrated | WEAK 13/100 | EXTREME 85/100 | Do nothing | WATCH |
| 11 | KAVA/USD | 0.0243 | 17.429 | 13.120 | +0.41% | -0.41% | 1.64x | 41.3 | 2026-11-24T12:11:43.418149+00:00 | Not calibrated | WEAK 14/100 | EXTREME 95/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 91.328 | 25.825 | -0.47% | 0.29x |
| 2 | MON/USD | 78.725 | 0.01251 | -1.57% | 0.36x |
| 3 | XMR/USD | 69.756 | 498.98 | -0.22% | 0.86x |
| 4 | ICNT/USD | 65.654 | 0.3311 | +1.19% | 0.64x |
| 5 | GBP/USD | 57.365 | 1.30808 | -0.03% | 0.38x |
| 6 | PEPE/USD | 53.824 | 3.452e-06 | -0.66% | 25.97x |
| 7 | LUNA/USD | 51.677 | 4.579e-05 | -0.46% | 2.35x |
| 8 | NIGHT/USD | 48.726 | 0.04837 | -1.31% | 0.49x |
| 9 | BABY/USD | 32.682 | 0.00871 | +0.58% | 0.86x |
| 10 | BAT/USD | 27.309 | 0.07781 | -0.19% | 1.00x |
| 11 | KAVA/USD | 13.120 | 0.0243 | -0.41% | 1.64x |

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

- Persisted scans: 1572; predictions: 13560; observations: 952446.
- Matured sampled outcomes across 1/6/24/48h: 26233; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45390825020 · **Generation:** 1572 · **Legacy run:** 45390825020
**Main quote time:** 2026-11-24T12:11:50.619780+00:00 · **Legacy report time:** 2026-11-24T12:12:49.731536+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.825 | 81.88 | -0.47% | 0.29x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 2 | ICNT/USD | 0.3311 | 68.00 | +1.19% | 0.64x | MODERATE 54/100 | EXTREME 87/100 | Do nothing |
| 3 | XMR/USD | 498.98 | 67.23 | -0.22% | 0.86x | WEAK 39/100 | HIGH 68/100 | Watch |
| 4 | PEPE/USD | 3.452e-06 | 65.52 | -0.66% | 25.97x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 5 | MON/USD | 0.01251 | 64.47 | -1.57% | 0.36x | WEAK 32/100 | EXTREME 86/100 | Do nothing |
| 6 | LUNA/USD | 4.579e-05 | 62.87 | -0.46% | 2.35x | MODERATE 46/100 | VERY_HIGH 78/100 | Watch |
| 7 | GBP/USD | 1.30808 | 50.99 | -0.03% | 0.38x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | NIGHT/USD | 0.04837 | 37.10 | -1.31% | 0.49x | WEAK 24/100 | VERY_HIGH 80/100 | Do nothing |
| 9 | BABY/USD | 0.00871 | 34.20 | +0.58% | 0.86x | WEAK 37/100 | VERY_HIGH 79/100 | Watch |
| 10 | BAT/USD | 0.07781 | 26.35 | -0.19% | 1.00x | WEAK 13/100 | EXTREME 85/100 | Do nothing |
| 11 | KAVA/USD | 0.0243 | 17.43 | -0.41% | 1.64x | WEAK 14/100 | EXTREME 95/100 | Do nothing |

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
