# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T13:52:39.123036+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45407440223
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 01286a0874e84ea3a6c418465fd17e91ba7f13c2 (atomic ledger/results publication)
**Ledger generation:** 1582 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.553 | 77.386 | 83.107 | +4.52% | +0.06% | 0.40x | 7.1 | 2026-11-24T13:52:33.969576+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | MON/USD | 0.01232 | 73.522 | 79.092 | +6.94% | +0.00% | 0.44x | 16.3 | 2026-11-24T13:52:33.969576+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | LUNA/USD | 4.598e-05 | 73.464 | 50.410 | +5.77% | +1.61% | 6.23x | 43.7 | 2026-11-24T13:52:33.969576+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | XMR/USD | 496.89 | 63.605 | 67.029 | +2.24% | +0.26% | 0.53x | 7.3 | 2026-11-24T13:52:33.969576+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | DBR/USD | 0.01433 | 52.482 | 55.414 | +6.78% | +0.07% | 0.67x | 42.0 | 2026-11-24T13:52:33.969576+00:00 | Not calibrated | WEAK 31/100 | EXTREME 100/100 | Do nothing | WATCH |
| 6 | GBP/USD | 1.30954 | 50.069 | 58.188 | +0.48% | +0.05% | 0.16x | 0.4 | 2026-11-24T13:52:33.969576+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | INX/USD | 0.003951 | 50.024 | 29.666 | +1.36% | +2.20% | 1.94x | 22.8 | 2026-11-24T13:52:33.969576+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 8 | NIGHT/USD | 0.04841 | 46.578 | 46.624 | +0.54% | +0.29% | 0.85x | 10.3 | 2026-11-24T13:52:33.969576+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 9 | 2Z/USD | 0.01601 | 43.399 | 43.742 | +2.30% | +0.69% | 0.62x | 6.2 | 2026-11-24T13:52:33.969576+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 10 | Q/USD | 0.026766 | 34.020 | 40.377 | +3.47% | +0.24% | 0.24x | 29.2 | 2026-11-24T13:52:33.969576+00:00 | Not calibrated | WEAK 37/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 83.107 | 25.553 | +0.06% | 0.40x |
| 2 | MON/USD | 79.092 | 0.01232 | +0.00% | 0.44x |
| 3 | XMR/USD | 67.029 | 496.89 | +0.26% | 0.53x |
| 4 | GBP/USD | 58.188 | 1.30954 | +0.05% | 0.16x |
| 5 | DBR/USD | 55.414 | 0.01433 | +0.07% | 0.67x |
| 6 | LUNA/USD | 50.410 | 4.598e-05 | +1.61% | 6.23x |
| 7 | NIGHT/USD | 46.624 | 0.04841 | +0.29% | 0.85x |
| 8 | 2Z/USD | 43.742 | 0.01601 | +0.69% | 0.62x |
| 9 | Q/USD | 40.377 | 0.026766 | +0.24% | 0.24x |
| 10 | INX/USD | 29.666 | 0.003951 | +2.20% | 1.94x |

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

- Persisted scans: 1582; predictions: 13643; observations: 958535.
- Matured sampled outcomes across 1/6/24/48h: 26719; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45407440223 · **Generation:** 1582 · **Legacy run:** 45407440223
**Main quote time:** 2026-11-24T13:52:39.123036+00:00 · **Legacy report time:** 2026-11-24T13:53:52.127077+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.553 | 77.39 | +0.06% | 0.40x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 2 | MON/USD | 0.01232 | 73.52 | +0.00% | 0.44x | MODERATE 52/100 | VERY_HIGH 76/100 | Watch |
| 3 | LUNA/USD ⭐ | 4.598e-05 | 73.46 | +1.61% | 6.23x | STRONG 87/100 | VERY_HIGH 82/100 | Watch |
| 4 | XMR/USD | 496.89 | 63.60 | +0.26% | 0.53x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 5 | DBR/USD | 0.01433 | 52.48 | +0.07% | 0.67x | WEAK 31/100 | EXTREME 100/100 | Do nothing |
| 6 | GBP/USD | 1.30954 | 50.07 | +0.05% | 0.16x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 7 | INX/USD ⭐ | 0.003951 | 50.02 | +2.20% | 1.94x | STRONG 70/100 | VERY_HIGH 79/100 | Watch |
| 8 | NIGHT/USD | 0.04841 | 46.58 | +0.29% | 0.85x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 9 | 2Z/USD | 0.01601 | 43.40 | +0.69% | 0.62x | MODERATE 52/100 | VERY_HIGH 82/100 | Watch |
| 10 | Q/USD | 0.026766 | 34.02 | +0.24% | 0.24x | WEAK 37/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.598e-05 | 76.60 | +1.61% | 6.23x | 1758 | STRONG 93/100 | VERY_HIGH 72/100 | Watch |
| 2 | INX/USD ⭐ | 0.003932 | 43.73 | +2.20% | 1.94x | 4273 | MODERATE 67/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** LUNA/USD, INX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
