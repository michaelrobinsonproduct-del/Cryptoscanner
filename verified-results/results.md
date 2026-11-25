# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T17:08:22.356572+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45660807746
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 016244ccd0680393c712debad598948d6167a391 (atomic ledger/results publication)
**Ledger generation:** 1742 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.749 | 99.945 | 80.989 | +4.94% | +2.00% | 1.89x | 17.1 | 2026-11-25T17:08:18.071230+00:00 | Not calibrated | STRONG 90/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | DRV/USD | 0.33231 | 86.993 | 68.642 | +5.74% | +1.46% | 2.10x | 19.3 | 2026-11-25T17:08:18.071230+00:00 | Not calibrated | STRONG 93/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | XPL/USD | 0.0468 | 85.035 | 69.921 | +6.36% | +2.20% | 1.41x | 21.4 | 2026-11-25T17:08:18.071230+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | LTC/USD | 41.32 | 59.549 | 59.423 | +1.15% | +1.21% | 0.41x | 7.3 | 2026-11-25T17:08:18.071230+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ASTER/USD | 0.48616 | 47.664 | 36.952 | +1.11% | +0.52% | 1.81x | 6.6 | 2026-11-25T17:08:18.071230+00:00 | Not calibrated | MODERATE 69/100 | HIGH 60/100 | Watch | WATCH |
| 6 | STRK/USD | 0.03014 | 37.107 | 33.902 | +1.04% | +2.12% | 0.26x | 10.0 | 2026-11-25T17:08:18.071230+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 7 | XTZ/USD | 0.21264 | 35.456 | 28.293 | +0.62% | +1.77% | 0.83x | 13.7 | 2026-11-25T17:08:18.071230+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 8 | KAS/USD | 0.02638 | 32.299 | 27.142 | +1.00% | +1.16% | 0.94x | 26.5 | 2026-11-25T17:08:18.071230+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 9 | CT/USD | 0.1282 | 22.874 | 29.859 | +1.50% | +0.24% | 0.18x | 23.5 | 2026-11-25T17:08:18.071230+00:00 | Not calibrated | WEAK 31/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 80.989 | 25.749 | +2.00% | 1.89x |
| 2 | XPL/USD | 69.921 | 0.0468 | +2.20% | 1.41x |
| 3 | DRV/USD | 68.642 | 0.33231 | +1.46% | 2.10x |
| 4 | LTC/USD | 59.423 | 41.32 | +1.21% | 0.41x |
| 5 | ASTER/USD | 36.952 | 0.48616 | +0.52% | 1.81x |
| 6 | STRK/USD | 33.902 | 0.03014 | +2.12% | 0.26x |
| 7 | CT/USD | 29.859 | 0.1282 | +0.24% | 0.18x |
| 8 | XTZ/USD | 28.293 | 0.21264 | +1.77% | 0.83x |
| 9 | KAS/USD | 27.142 | 0.02638 | +1.16% | 0.94x |

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

- Persisted scans: 1742; predictions: 14649; observations: 1055922.
- Matured sampled outcomes across 1/6/24/48h: 32504; gap abstentions: 22488. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45660807746 · **Generation:** 1742 · **Legacy run:** 45660807746
**Main quote time:** 2026-11-25T17:08:22.356572+00:00 · **Legacy report time:** 2026-11-25T17:09:40.436918+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.749 | 99.94 | +2.00% | 1.89x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | DRV/USD ⭐ | 0.33231 | 86.99 | +1.46% | 2.10x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | XPL/USD ⭐ | 0.0468 | 85.04 | +2.20% | 1.41x | STRONG 88/100 | VERY_HIGH 72/100 | Watch |
| 4 | LTC/USD | 41.32 | 59.55 | +1.21% | 0.41x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 5 | ASTER/USD ⭐ | 0.48616 | 47.66 | +0.52% | 1.81x | STRONG 79/100 | HIGH 60/100 | Consider small entry |
| 6 | STRK/USD | 0.03014 | 37.11 | +2.12% | 0.26x | MODERATE 49/100 | VERY_HIGH 82/100 | Watch |
| 7 | XTZ/USD | 0.21264 | 35.46 | +1.77% | 0.83x | WEAK 43/100 | VERY_HIGH 80/100 | Watch |
| 8 | KAS/USD | 0.02638 | 32.30 | +1.16% | 0.94x | WEAK 36/100 | VERY_HIGH 79/100 | Watch |
| 9 | CT/USD | 0.1282 | 22.87 | +0.24% | 0.18x | WEAK 31/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.652 | 94.45 | +2.00% | 1.89x | 10502 | STRONG 97/100 | HIGH 61/100 | Consider small entry |
| 2 | DRV/USD ⭐ | 0.33231 | 83.68 | +1.46% | 2.10x | 10723 | STRONG 97/100 | HIGH 67/100 | Consider small entry |
| 3 | XPL/USD ⭐ | 0.0467 | 75.41 | +2.20% | 1.41x | 1860 | STRONG 78/100 | VERY_HIGH 82/100 | Watch |
| 4 | ASTER/USD ⭐ | 0.48615 | 43.83 | +0.52% | 1.81x | 2930 | STRONG 77/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** VVV/USD, DRV/USD, XPL/USD, ASTER/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
