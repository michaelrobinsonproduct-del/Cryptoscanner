# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T18:01:47.402306+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45454601678
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ae95312b42c8fcc3e5f69195908c1a2d2da736b0 (atomic ledger/results publication)
**Ledger generation:** 1608 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 503.66 | 88.587 | 73.557 | +3.63% | +0.01% | 5.84x | 13.7 | 2026-11-24T18:01:42.431660+00:00 | Not calibrated | STRONG 84/100 | HIGH 61/100 | Watch | WATCH |
| 2 | LUNA/USD | 4.832e-05 | 79.212 | 71.614 | +11.16% | -0.37% | 1.95x | 10.4 | 2026-11-24T18:01:42.431660+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | GBP/USD | 1.31199 | 74.679 | 59.504 | +0.67% | +0.04% | 3.62x | 0.4 | 2026-11-24T18:01:42.431660+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 4 | VVV/USD | 25.13 | 70.077 | 69.959 | +2.79% | -0.59% | 1.31x | 9.1 | 2026-11-24T18:01:42.431660+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 5 | 2Z/USD | 0.01633 | 60.302 | 42.845 | +4.34% | +0.49% | 3.84x | 36.7 | 2026-11-24T18:01:42.431660+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | AUD/USD | 0.66461 | 53.827 | 44.105 | +0.30% | -0.00% | 1.97x | 2.0 | 2026-11-24T18:01:42.431660+00:00 | Not calibrated | MODERATE 47/100 | HIGH 61/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.448e-06 | 50.265 | 46.532 | +0.76% | +0.67% | 1.04x | 5.8 | 2026-11-24T18:01:42.431660+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 8 | NIGHT/USD | 0.04838 | 47.571 | 38.088 | +0.48% | +1.15% | 1.37x | 12.4 | 2026-11-24T18:01:42.431660+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 9 | DBR/USD | 0.01363 | 35.021 | 35.215 | +1.56% | -0.59% | 1.27x | 14.7 | 2026-11-24T18:01:42.431660+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 73.557 | 503.66 | +0.01% | 5.84x |
| 2 | LUNA/USD | 71.614 | 4.832e-05 | -0.37% | 1.95x |
| 3 | VVV/USD | 69.959 | 25.13 | -0.59% | 1.31x |
| 4 | GBP/USD | 59.504 | 1.31199 | +0.04% | 3.62x |
| 5 | PEPE/USD | 46.532 | 3.448e-06 | +0.67% | 1.04x |
| 6 | AUD/USD | 44.105 | 0.66461 | -0.00% | 1.97x |
| 7 | 2Z/USD | 42.845 | 0.01633 | +0.49% | 3.84x |
| 8 | NIGHT/USD | 38.088 | 0.04838 | +1.15% | 1.37x |
| 9 | DBR/USD | 35.215 | 0.01363 | -0.59% | 1.27x |

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

- Persisted scans: 1608; predictions: 13813; observations: 974364.
- Matured sampled outcomes across 1/6/24/48h: 27785; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45454601678 · **Generation:** 1608 · **Legacy run:** 45454601678
**Main quote time:** 2026-11-24T18:01:47.402306+00:00 · **Legacy report time:** 2026-11-24T18:02:37.832477+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 503.66 | 88.59 | +0.01% | 5.84x | STRONG 84/100 | HIGH 61/100 | Watch |
| 2 | LUNA/USD | 4.832e-05 | 79.21 | -0.37% | 1.95x | MODERATE 55/100 | VERY_HIGH 72/100 | Watch |
| 3 | GBP/USD | 1.31199 | 74.68 | +0.04% | 3.62x | STRONG 82/100 | HIGH 55/100 | Watch |
| 4 | VVV/USD | 25.13 | 70.08 | -0.59% | 1.31x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 5 | 2Z/USD ⭐ | 0.01633 | 60.30 | +0.49% | 3.84x | STRONG 80/100 | VERY_HIGH 79/100 | Watch |
| 6 | AUD/USD | 0.66461 | 53.83 | -0.00% | 1.97x | MODERATE 47/100 | HIGH 61/100 | Watch |
| 7 | PEPE/USD ⭐ | 3.448e-06 | 50.27 | +0.67% | 1.04x | STRONG 70/100 | HIGH 62/100 | Watch |
| 8 | NIGHT/USD ⭐ | 0.04838 | 47.57 | +1.15% | 1.37x | STRONG 74/100 | HIGH 61/100 | Watch |
| 9 | DBR/USD | 0.01363 | 35.02 | -0.59% | 1.27x | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | 2Z/USD ⭐ | 0.01633 | 69.93 | +0.49% | 3.84x | 1438 | STRONG 95/100 | VERY_HIGH 73/100 | Watch |
| 2 | PEPE/USD ⭐ | 3.442e-06 | 43.03 | +0.67% | 1.04x | 6849 | MODERATE 67/100 | HIGH 62/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.04829 | 36.99 | +1.15% | 1.37x | 9224 | MODERATE 68/100 | HIGH 61/100 | Watch |

**Same-run overlap:** 2Z/USD, PEPE/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
