# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T14:31:20.331244+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45033092041
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** d50ebd3c1de30b3933d79d3e4f902be9a86dffcd (atomic ledger/results publication)
**Ledger generation:** 1295 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | STBL/USD | 0.017126 | 85.171 | 74.020 | +7.01% | -0.77% | 3.40x | 3.5 | 2026-11-22T14:31:13.337478+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04904 | 83.956 | 82.747 | +10.75% | -0.64% | 1.44x | 18.4 | 2026-11-22T14:31:13.337478+00:00 | Not calibrated | MODERATE 57/100 | HIGH 67/100 | Watch | WATCH |
| 3 | TAO/USD | 190.3182 | 73.959 | 63.247 | +2.47% | -0.44% | 2.29x | 7.1 | 2026-11-22T14:31:13.337478+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 4 | VVV/USD | 25.418 | 70.157 | 65.440 | +2.08% | -0.32% | 1.63x | 8.2 | 2026-11-22T14:31:13.337478+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.006 | 68.730 | 81.537 | +4.15% | -1.11% | 0.28x | 5.0 | 2026-11-22T14:31:13.337478+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 6 | MNT/USD | 0.3939 | 63.425 | 71.325 | +6.34% | -0.53% | 0.47x | 7.6 | 2026-11-22T14:31:13.337478+00:00 | Not calibrated | WEAK 37/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | SUI/USD | 0.6547 | 59.046 | 62.239 | +1.14% | -0.55% | 0.95x | 1.5 | 2026-11-22T14:31:13.337478+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 8 | HYPE/USD | 62.39 | 57.693 | 67.344 | +1.88% | -0.57% | 0.32x | 1.6 | 2026-11-22T14:31:13.337478+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | XBT/USD | 60562.4 | 55.423 | 60.496 | +0.79% | -0.18% | 0.58x | 0.0 | 2026-11-22T14:31:13.337478+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | ETH/USD | 1700.66 | 55.332 | 62.472 | +1.09% | -0.23% | 0.40x | 0.4 | 2026-11-22T14:31:13.337478+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | DOT/USD | 0.6592 | 46.746 | 38.075 | +0.95% | -0.47% | 2.10x | 1.5 | 2026-11-22T14:31:13.337478+00:00 | Not calibrated | MODERATE 53/100 | HIGH 66/100 | Watch | WATCH |
| 12 | LINK/USD | 8.74079 | 45.677 | 56.867 | +1.70% | -0.48% | 0.12x | 0.0 | 2026-11-22T14:31:13.337478+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 82.747 | 0.04904 | -0.64% | 1.44x |
| 2 | NEAR/USD | 81.537 | 3.006 | -1.11% | 0.28x |
| 3 | STBL/USD | 74.020 | 0.017126 | -0.77% | 3.40x |
| 4 | MNT/USD | 71.325 | 0.3939 | -0.53% | 0.47x |
| 5 | HYPE/USD | 67.344 | 62.39 | -0.57% | 0.32x |
| 6 | VVV/USD | 65.440 | 25.418 | -0.32% | 1.63x |
| 7 | TAO/USD | 63.247 | 190.3182 | -0.44% | 2.29x |
| 8 | ETH/USD | 62.472 | 1700.66 | -0.23% | 0.40x |
| 9 | SUI/USD | 62.239 | 0.6547 | -0.55% | 0.95x |
| 10 | XBT/USD | 60.496 | 60562.4 | -0.18% | 0.58x |
| 11 | LINK/USD | 56.867 | 8.74079 | -0.48% | 0.12x |
| 12 | DOT/USD | 38.075 | 0.6592 | -0.47% | 2.10x |

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

- Persisted scans: 1295; predictions: 10459; observations: 783764.
- Matured sampled outcomes across 1/6/24/48h: 15239; gap abstentions: 22277. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45033092041 · **Generation:** 1295 · **Legacy run:** 45033092041
**Main quote time:** 2026-11-22T14:31:20.331244+00:00 · **Legacy report time:** 2026-11-22T14:32:18.789375+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | STBL/USD | 0.017126 | 85.17 | -0.77% | 3.40x | STRONG 73/100 | VERY_HIGH 73/100 | Watch |
| 2 | NIGHT/USD | 0.04904 | 83.96 | -0.64% | 1.44x | MODERATE 57/100 | HIGH 67/100 | Watch |
| 3 | TAO/USD | 190.3182 | 73.96 | -0.44% | 2.29x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 4 | VVV/USD | 25.418 | 70.16 | -0.32% | 1.63x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 5 | NEAR/USD | 3.006 | 68.73 | -1.11% | 0.28x | WEAK 39/100 | VERY_HIGH 80/100 | Watch |
| 6 | MNT/USD | 0.3939 | 63.43 | -0.53% | 0.47x | WEAK 37/100 | EXTREME 88/100 | Do nothing |
| 7 | SUI/USD | 0.6547 | 59.05 | -0.55% | 0.95x | WEAK 35/100 | HIGH 68/100 | Watch |
| 8 | HYPE/USD | 62.39 | 57.69 | -0.57% | 0.32x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | XBT/USD | 60562.4 | 55.42 | -0.18% | 0.58x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | ETH/USD | 1700.66 | 55.33 | -0.23% | 0.40x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | DOT/USD | 0.6592 | 46.75 | -0.47% | 2.10x | MODERATE 53/100 | HIGH 66/100 | Watch |
| 12 | LINK/USD | 8.74079 | 45.68 | -0.48% | 0.12x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD | 3.6625 | 92.23 | +17.14% | 2.98x | 6046 | STRONG 86/100 | EXTREME 87/100 | Do nothing |
| 2 | RARE/USD | 0.01481 | 79.36 | +0.61% | 3.73x | 2522 | STRONG 85/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
