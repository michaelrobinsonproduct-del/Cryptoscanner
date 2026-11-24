# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T02:51:48.370859+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45315174956
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1cffb04fa9ad149ab8d5de032887532cb632b798 (atomic ledger/results publication)
**Ledger generation:** 1515 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.0123 | 90.132 | 79.555 | +6.77% | +1.80% | 1.16x | 8.1 | 2026-11-24T02:51:40.299186+00:00 | Not calibrated | STRONG 80/100 | HIGH 62/100 | Watch | WATCH |
| 2 | PEPE/USD | 3.438e-06 | 46.767 | 49.226 | +0.47% | -0.14% | 0.83x | 5.8 | 2026-11-24T02:51:40.299186+00:00 | Not calibrated | WEAK 28/100 | HIGH 68/100 | Do nothing | WATCH |
| 3 | NIGHT/USD | 0.04846 | 44.328 | 51.098 | +0.64% | -0.29% | 0.47x | 6.2 | 2026-11-24T02:51:40.299186+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | BAT/USD | 0.07806 | 43.299 | 39.423 | +1.15% | +0.19% | 1.29x | 1.3 | 2026-11-24T02:51:40.299186+00:00 | Not calibrated | MODERATE 47/100 | HIGH 60/100 | Watch | WATCH |
| 5 | BABY/USD | 0.00854 | 39.917 | 28.409 | +0.47% | -0.70% | 2.64x | 11.7 | 2026-11-24T02:51:40.299186+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | CC/USD | 0.07917 | 36.889 | 36.727 | +0.78% | -0.38% | 1.21x | 10.1 | 2026-11-24T02:51:40.299186+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 7 | XDC/USD | 0.02616 | 32.512 | 38.194 | +0.69% | +0.27% | 0.30x | 3.8 | 2026-11-24T02:51:40.299186+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | AI/USD | 0.01569 | 31.072 | 42.719 | +3.02% | -2.55% | 1.11x | 19.1 | 2026-11-24T02:51:40.299186+00:00 | Not calibrated | WEAK 21/100 | EXTREME 90/100 | Do nothing | WATCH |
| 9 | SPX/USD | 0.2805 | 21.244 | 28.991 | +0.32% | -0.18% | 0.31x | 10.7 | 2026-11-24T02:51:40.299186+00:00 | Not calibrated | WEAK 11/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 79.555 | 0.0123 | +1.80% | 1.16x |
| 2 | NIGHT/USD | 51.098 | 0.04846 | -0.29% | 0.47x |
| 3 | PEPE/USD | 49.226 | 3.438e-06 | -0.14% | 0.83x |
| 4 | AI/USD | 42.719 | 0.01569 | -2.55% | 1.11x |
| 5 | BAT/USD | 39.423 | 0.07806 | +0.19% | 1.29x |
| 6 | XDC/USD | 38.194 | 0.02616 | +0.27% | 0.30x |
| 7 | CC/USD | 36.727 | 0.07917 | -0.38% | 1.21x |
| 8 | SPX/USD | 28.991 | 0.2805 | -0.18% | 0.31x |
| 9 | BABY/USD | 28.409 | 0.00854 | -0.70% | 2.64x |

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

- Persisted scans: 1515; predictions: 12934; observations: 917736.
- Matured sampled outcomes across 1/6/24/48h: 23954; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45315174956 · **Generation:** 1515 · **Legacy run:** 45315174956
**Main quote time:** 2026-11-24T02:51:48.370859+00:00 · **Legacy report time:** 2026-11-24T02:52:40.397673+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.0123 | 90.13 | +1.80% | 1.16x | STRONG 90/100 | HIGH 62/100 | Watch |
| 2 | PEPE/USD | 3.438e-06 | 46.77 | -0.14% | 0.83x | WEAK 28/100 | HIGH 68/100 | Do nothing |
| 3 | NIGHT/USD | 0.04846 | 44.33 | -0.29% | 0.47x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | BAT/USD ⭐ | 0.07806 | 43.30 | +0.19% | 1.29x | MODERATE 57/100 | HIGH 60/100 | Watch |
| 5 | BABY/USD | 0.00854 | 39.92 | -0.70% | 2.64x | MODERATE 45/100 | VERY_HIGH 79/100 | Watch |
| 6 | CC/USD | 0.07917 | 36.89 | -0.38% | 1.21x | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing |
| 7 | XDC/USD | 0.02616 | 32.51 | +0.27% | 0.30x | MODERATE 46/100 | VERY_HIGH 75/100 | Watch |
| 8 | AI/USD | 0.01569 | 31.07 | -2.55% | 1.11x | WEAK 21/100 | EXTREME 90/100 | Do nothing |
| 9 | SPX/USD | 0.2805 | 21.24 | -0.18% | 0.31x | WEAK 11/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01217 | 81.17 | +1.80% | 1.16x | 7424 | STRONG 81/100 | HIGH 68/100 | Watch |
| 2 | BAT/USD ⭐ | 0.07808 | 39.09 | +0.19% | 1.29x | 2961 | MODERATE 45/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** MON/USD, BAT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
