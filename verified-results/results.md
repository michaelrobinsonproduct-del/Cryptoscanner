# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T14:21:37.306983+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45032198398
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 367fad076f1408a4e3f1195aaf1d8471a9c863df (atomic ledger/results publication)
**Ledger generation:** 1294 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04873 | 98.439 | 84.157 | +10.05% | -0.14% | 3.02x | 14.4 | 2026-11-22T14:21:29.057627+00:00 | Not calibrated | STRONG 74/100 | HIGH 67/100 | Watch | WATCH |
| 2 | STBL/USD | 0.017223 | 83.472 | 66.175 | +7.62% | +0.46% | 9.24x | 19.2 | 2026-11-22T14:21:29.057627+00:00 | Not calibrated | STRONG 92/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | VVV/USD | 25.546 | 83.359 | 70.030 | +2.59% | +1.40% | 1.63x | 6.3 | 2026-11-22T14:21:29.057627+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | TAO/USD | 190.8994 | 80.311 | 65.197 | +2.78% | +0.02% | 2.50x | 8.2 | 2026-11-22T14:21:29.057627+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.0203 | 76.886 | 84.353 | +4.64% | -0.20% | 0.35x | 6.3 | 2026-11-22T14:21:29.057627+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | HYPE/USD | 62.5 | 73.479 | 67.805 | +2.06% | -0.03% | 1.58x | 3.2 | 2026-11-22T14:21:29.057627+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ZEC/USD | 791.66 | 67.262 | 64.672 | +1.73% | -0.12% | 1.32x | 4.9 | 2026-11-22T14:21:29.057627+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ETH/USD | 1705.33 | 64.102 | 64.562 | +1.37% | +0.07% | 0.92x | 0.1 | 2026-11-22T14:21:29.057627+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 9 | MNT/USD | 0.3973 | 63.326 | 71.951 | +7.26% | -0.03% | 0.15x | 7.6 | 2026-11-22T14:21:29.057627+00:00 | Not calibrated | WEAK 37/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | XBT/USD | 60654 | 62.169 | 61.563 | +0.94% | -0.12% | 1.12x | 0.0 | 2026-11-22T14:21:29.057627+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 11 | LINK/USD | 8.77803 | 50.649 | 59.289 | +2.13% | +0.06% | 0.11x | 1.5 | 2026-11-22T14:21:29.057627+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | AVAX/USD | 6.658 | 46.456 | 50.303 | +1.45% | -0.15% | 0.69x | 3.0 | 2026-11-22T14:21:29.057627+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 84.353 | 3.0203 | -0.20% | 0.35x |
| 2 | NIGHT/USD | 84.157 | 0.04873 | -0.14% | 3.02x |
| 3 | MNT/USD | 71.951 | 0.3973 | -0.03% | 0.15x |
| 4 | VVV/USD | 70.030 | 25.546 | +1.40% | 1.63x |
| 5 | HYPE/USD | 67.805 | 62.5 | -0.03% | 1.58x |
| 6 | STBL/USD | 66.175 | 0.017223 | +0.46% | 9.24x |
| 7 | TAO/USD | 65.197 | 190.8994 | +0.02% | 2.50x |
| 8 | ZEC/USD | 64.672 | 791.66 | -0.12% | 1.32x |
| 9 | ETH/USD | 64.562 | 1705.33 | +0.07% | 0.92x |
| 10 | XBT/USD | 61.563 | 60654 | -0.12% | 1.12x |
| 11 | LINK/USD | 59.289 | 8.77803 | +0.06% | 0.11x |
| 12 | AVAX/USD | 50.303 | 6.658 | -0.15% | 0.69x |

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

- Persisted scans: 1294; predictions: 10447; observations: 783155.
- Matured sampled outcomes across 1/6/24/48h: 15210; gap abstentions: 22275. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45032198398 · **Generation:** 1294 · **Legacy run:** 45032198398
**Main quote time:** 2026-11-22T14:21:37.306983+00:00 · **Legacy report time:** 2026-11-22T14:22:19.502854+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04873 | 98.44 | -0.14% | 3.02x | STRONG 74/100 | HIGH 67/100 | Watch |
| 2 | STBL/USD | 0.017223 | 83.47 | +0.46% | 9.24x | STRONG 92/100 | VERY_HIGH 73/100 | Watch |
| 3 | VVV/USD ⭐ | 25.546 | 83.36 | +1.40% | 1.63x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 4 | TAO/USD | 190.8994 | 80.31 | +0.02% | 2.50x | STRONG 85/100 | HIGH 55/100 | Watch |
| 5 | NEAR/USD | 3.0203 | 76.89 | -0.20% | 0.35x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 6 | HYPE/USD | 62.5 | 73.48 | -0.03% | 1.58x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 7 | ZEC/USD | 791.66 | 67.26 | -0.12% | 1.32x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 8 | ETH/USD | 1705.33 | 64.10 | +0.07% | 0.92x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 9 | MNT/USD | 0.3973 | 63.33 | -0.03% | 0.15x | WEAK 37/100 | EXTREME 88/100 | Do nothing |
| 10 | XBT/USD | 60654 | 62.17 | -0.12% | 1.12x | WEAK 41/100 | HIGH 68/100 | Watch |
| 11 | LINK/USD | 8.77803 | 50.65 | +0.06% | 0.11x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 12 | AVAX/USD | 6.658 | 46.46 | -0.15% | 0.69x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.546 | 76.58 | +1.40% | 1.63x | 13444 | STRONG 93/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
