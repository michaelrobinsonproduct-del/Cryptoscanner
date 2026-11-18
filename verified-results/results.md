# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T12:50:11.421219+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44307617189
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** ea5d13c02e63d152c8025a70f61ffc13364dc20c (atomic ledger/results publication)
**Ledger generation:** 569 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04655 | 69.147 | 72.344 | +3.70% | +0.28% | 0.54x | 4.3 | 2026-11-18T12:50:03.968158+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | SENT/USD | 0.01961 | 68.213 | 62.503 | +5.04% | +0.61% | 1.27x | 7.7 | 2026-11-18T12:50:03.968158+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 3 | USELESS/USD | 0.10004 | 56.836 | 51.481 | +2.52% | +0.02% | 1.53x | 16.0 | 2026-11-18T12:50:03.968158+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 4 | STABLE/USD | 0.02308 | 55.053 | 65.122 | +9.64% | -1.87% | 0.93x | 21.7 | 2026-11-18T12:50:03.968158+00:00 | Not calibrated | WEAK 23/100 | EXTREME 96/100 | Do nothing | WATCH |
| 5 | MNT/USD | 0.3848 | 49.925 | 48.064 | +3.08% | -0.54% | 1.46x | 13.0 | 2026-11-18T12:50:03.968158+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | ME/USD | 0.0403 | 47.346 | 49.936 | +4.40% | +0.00% | 0.74x | 24.8 | 2026-11-18T12:50:03.968158+00:00 | Not calibrated | WEAK 34/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | CAP/USD | 0.101732 | 47.320 | 33.538 | +0.75% | +0.12% | 2.32x | 6.1 | 2026-11-18T12:50:03.968158+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 8 | TRX/USD | 0.309754 | 40.066 | 44.923 | +0.60% | +0.00% | 0.51x | 1.3 | 2026-11-18T12:50:03.968158+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | CC/USD | 0.08301 | 39.749 | 41.752 | +1.07% | -0.41% | 1.00x | 3.6 | 2026-11-18T12:50:03.968158+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 10 | AKT/USD | 0.5172 | 38.056 | 38.477 | +1.55% | -0.21% | 1.06x | 9.7 | 2026-11-18T12:50:03.968158+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 11 | VVV/USD | 21.109 | 27.436 | 37.576 | +0.39% | -0.75% | 0.36x | 26.6 | 2026-11-18T12:50:03.968158+00:00 | Not calibrated | WEAK 9/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 72.344 | 0.04655 | +0.28% | 0.54x |
| 2 | STABLE/USD | 65.122 | 0.02308 | -1.87% | 0.93x |
| 3 | SENT/USD | 62.503 | 0.01961 | +0.61% | 1.27x |
| 4 | USELESS/USD | 51.481 | 0.10004 | +0.02% | 1.53x |
| 5 | ME/USD | 49.936 | 0.0403 | +0.00% | 0.74x |
| 6 | MNT/USD | 48.064 | 0.3848 | -0.54% | 1.46x |
| 7 | TRX/USD | 44.923 | 0.309754 | +0.00% | 0.51x |
| 8 | CC/USD | 41.752 | 0.08301 | -0.41% | 1.00x |
| 9 | AKT/USD | 38.477 | 0.5172 | -0.21% | 1.06x |
| 10 | VVV/USD | 37.576 | 21.109 | -0.75% | 0.36x |
| 11 | CAP/USD | 33.538 | 0.101732 | +0.12% | 2.32x |

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

- Persisted scans: 569; predictions: 4802; observations: 343528.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 12965. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44307617189 · **Generation:** 569 · **Legacy run:** 44307617189
**Main quote time:** 2026-11-18T12:50:11.421219+00:00 · **Legacy report time:** 2026-11-18T12:50:30.408853+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04655 | 69.15 | +0.28% | 0.54x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 2 | SENT/USD ⭐ | 0.01961 | 68.21 | +0.61% | 1.27x | STRONG 79/100 | HIGH 67/100 | Watch |
| 3 | USELESS/USD | 0.10004 | 56.84 | +0.02% | 1.53x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 4 | STABLE/USD | 0.02308 | 55.05 | -1.87% | 0.93x | WEAK 23/100 | EXTREME 96/100 | Do nothing |
| 5 | MNT/USD | 0.3848 | 49.92 | -0.54% | 1.46x | WEAK 40/100 | VERY_HIGH 72/100 | Watch |
| 6 | ME/USD | 0.0403 | 47.35 | +0.00% | 0.74x | WEAK 34/100 | EXTREME 94/100 | Do nothing |
| 7 | CAP/USD ⭐ | 0.101732 | 47.32 | +0.12% | 2.32x | STRONG 79/100 | HIGH 67/100 | Watch |
| 8 | TRX/USD | 0.309754 | 40.07 | +0.00% | 0.51x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |
| 9 | CC/USD | 0.08301 | 39.75 | -0.41% | 1.00x | WEAK 30/100 | VERY_HIGH 73/100 | Do nothing |
| 10 | AKT/USD | 0.5172 | 38.06 | -0.21% | 1.06x | WEAK 29/100 | VERY_HIGH 73/100 | Do nothing |
| 11 | VVV/USD | 21.109 | 27.44 | -0.75% | 0.36x | WEAK 9/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019588 | 76.27 | +0.61% | 1.27x | 5606 | STRONG 83/100 | HIGH 67/100 | Watch |
| 2 | CAP/USD ⭐ | 0.101732 | 39.73 | +0.12% | 2.32x | 2578 | STRONG 75/100 | HIGH 67/100 | Watch |

**Same-run overlap:** SENT/USD, CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
