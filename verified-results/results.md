# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T17:28:24.483202+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45664441071
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b49001441bcc4ea9717bc0824257ae5adf72b827 (atomic ledger/results publication)
**Ledger generation:** 1744 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.797 | 108.039 | 87.039 | +5.13% | +1.20% | 9.30x | 7.8 | 2026-11-25T17:28:15.273578+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | DRV/USD | 0.33643 | 102.477 | 80.555 | +7.05% | +1.38% | 7.47x | 5.6 | 2026-11-25T17:28:15.273578+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XPL/USD | 0.0469 | 89.891 | 70.590 | +6.59% | +0.86% | 3.25x | 21.4 | 2026-11-25T17:28:15.273578+00:00 | Not calibrated | STRONG 90/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | LTC/USD | 41.28 | 68.309 | 59.946 | +1.05% | +0.39% | 1.64x | 4.8 | 2026-11-25T17:28:15.273578+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 5 | INJ/USD | 5.863 | 53.139 | 35.565 | +0.26% | +0.51% | 7.17x | 8.5 | 2026-11-25T17:28:15.273578+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 6 | STRK/USD | 0.03017 | 51.457 | 36.291 | +1.14% | +0.03% | 4.83x | 6.7 | 2026-11-25T17:28:15.273578+00:00 | Not calibrated | STRONG 71/100 | HIGH 67/100 | Watch | WATCH |
| 7 | KAS/USD | 0.02649 | 50.541 | 34.029 | +1.42% | +0.30% | 4.64x | 18.9 | 2026-11-25T17:28:15.273578+00:00 | Not calibrated | STRONG 75/100 | HIGH 66/100 | Watch | WATCH |
| 8 | ASTER/USD | 0.48816 | 46.029 | 40.457 | +1.53% | +0.52% | 1.30x | 5.7 | 2026-11-25T17:28:15.273578+00:00 | Not calibrated | MODERATE 58/100 | HIGH 60/100 | Watch | WATCH |
| 9 | ATOM/USD | 1.251 | 40.377 | 27.497 | +0.45% | +0.92% | 1.83x | 16.9 | 2026-11-25T17:28:15.273578+00:00 | Not calibrated | MODERATE 60/100 | HIGH 66/100 | Watch | WATCH |
| 10 | XTZ/USD | 0.21245 | 36.842 | 29.795 | +0.53% | -0.14% | 1.78x | 9.4 | 2026-11-25T17:28:15.273578+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 11 | CAP/USD | 0.092679 | 25.933 | 30.337 | +0.28% | +0.45% | 0.33x | 6.2 | 2026-11-25T17:28:15.273578+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 87.039 | 25.797 | +1.20% | 9.30x |
| 2 | DRV/USD | 80.555 | 0.33643 | +1.38% | 7.47x |
| 3 | XPL/USD | 70.590 | 0.0469 | +0.86% | 3.25x |
| 4 | LTC/USD | 59.946 | 41.28 | +0.39% | 1.64x |
| 5 | ASTER/USD | 40.457 | 0.48816 | +0.52% | 1.30x |
| 6 | STRK/USD | 36.291 | 0.03017 | +0.03% | 4.83x |
| 7 | INJ/USD | 35.565 | 5.863 | +0.51% | 7.17x |
| 8 | KAS/USD | 34.029 | 0.02649 | +0.30% | 4.64x |
| 9 | CAP/USD | 30.337 | 0.092679 | +0.45% | 0.33x |
| 10 | XTZ/USD | 29.795 | 0.21245 | -0.14% | 1.78x |
| 11 | ATOM/USD | 27.497 | 1.251 | +0.92% | 1.83x |

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

- Persisted scans: 1744; predictions: 14672; observations: 1057140.
- Matured sampled outcomes across 1/6/24/48h: 32504; gap abstentions: 22547. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45664441071 · **Generation:** 1744 · **Legacy run:** 45664441071
**Main quote time:** 2026-11-25T17:28:24.483202+00:00 · **Legacy report time:** 2026-11-25T17:29:44.299053+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.797 | 108.04 | +1.20% | 9.30x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | DRV/USD ⭐ | 0.33643 | 102.48 | +1.38% | 7.47x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XPL/USD ⭐ | 0.0469 | 89.89 | +0.86% | 3.25x | STRONG 100/100 | VERY_HIGH 72/100 | Watch |
| 4 | LTC/USD ⭐ | 41.28 | 68.31 | +0.39% | 1.64x | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 5 | INJ/USD ⭐ | 5.863 | 53.14 | +0.51% | 7.17x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 6 | STRK/USD | 0.03017 | 51.46 | +0.03% | 4.83x | STRONG 71/100 | HIGH 67/100 | Watch |
| 7 | KAS/USD ⭐ | 0.02649 | 50.54 | +0.30% | 4.64x | STRONG 85/100 | HIGH 66/100 | Consider small entry |
| 8 | ASTER/USD ⭐ | 0.48816 | 46.03 | +0.52% | 1.30x | MODERATE 68/100 | HIGH 60/100 | Watch |
| 9 | ATOM/USD | 1.251 | 40.38 | +0.92% | 1.83x | MODERATE 60/100 | HIGH 66/100 | Watch |
| 10 | XTZ/USD | 0.21245 | 36.84 | -0.14% | 1.78x | WEAK 38/100 | VERY_HIGH 73/100 | Watch |
| 11 | CAP/USD | 0.092679 | 25.93 | +0.45% | 0.33x | WEAK 43/100 | VERY_HIGH 82/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.882 | 96.60 | +1.20% | 9.30x | 10225 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | DRV/USD ⭐ | 0.33748 | 87.20 | +1.38% | 7.47x | 10862 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | XPL/USD ⭐ | 0.0471 | 78.53 | +0.86% | 3.25x | 1940 | STRONG 94/100 | VERY_HIGH 72/100 | Watch |
| 4 | LTC/USD ⭐ | 41.38 | 66.47 | +0.39% | 1.64x | 12849 | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 5 | ASTER/USD ⭐ | 0.48943 | 57.11 | +0.52% | 1.30x | 2980 | STRONG 74/100 | HIGH 60/100 | Watch |
| 6 | KAS/USD ⭐ | 0.02649 | 48.87 | +0.30% | 4.64x | 2501 | STRONG 84/100 | HIGH 66/100 | Consider small entry |
| 7 | HBAR/USD | 0.05037 | 47.84 | +0.22% | 4.00x | 5431 | STRONG 79/100 | HIGH 60/100 | Watch |
| 8 | XLM/USD | 0.124232 | 41.63 | +0.40% | 1.40x | 7850 | MODERATE 66/100 | HIGH 55/100 | Watch |
| 9 | INJ/USD ⭐ | 5.855 | 37.79 | +0.51% | 7.17x | 6629 | STRONG 79/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** VVV/USD, DRV/USD, XPL/USD, LTC/USD, INJ/USD, KAS/USD, ASTER/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
