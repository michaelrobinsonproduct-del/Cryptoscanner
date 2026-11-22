# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T14:01:17.216599+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45030354509
**Source SHA:** 17af11513c515cf2dc9dda8017f091d9b1f13397
**Previous ledger commit:** 4b9eba2c71eb17a8d02662d98b407930e3abdfd6 (atomic ledger/results publication)
**Ledger generation:** 1292 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0252 | 100.124 | 87.200 | +4.81% | +0.16% | 2.21x | 3.0 | 2026-11-22T14:01:10.254572+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.0488 | 95.758 | 82.081 | +10.21% | +1.31% | 1.71x | 18.4 | 2026-11-22T14:01:10.254572+00:00 | Not calibrated | STRONG 88/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | STBL/USD | 0.017219 | 86.607 | 64.616 | +7.59% | +1.40% | 2.59x | 22.1 | 2026-11-22T14:01:10.254572+00:00 | Not calibrated | STRONG 88/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | TAO/USD | 190.9474 | 80.589 | 66.062 | +2.81% | -0.09% | 3.63x | 6.8 | 2026-11-22T14:01:10.254572+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ETH/USD | 1703.14 | 78.498 | 63.651 | +1.24% | -0.03% | 2.83x | 0.1 | 2026-11-22T14:01:10.254572+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 6 | LINK/USD | 8.7645 | 76.478 | 60.422 | +1.97% | +0.21% | 12.51x | 1.3 | 2026-11-22T14:01:10.254572+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | ZEC/USD | 790.1 | 68.772 | 64.405 | +1.53% | -0.41% | 1.64x | 2.7 | 2026-11-22T14:01:10.254572+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 8 | MNT/USD | 0.3966 | 66.212 | 70.704 | +7.07% | -0.08% | 0.59x | 10.1 | 2026-11-22T14:01:10.254572+00:00 | Not calibrated | WEAK 33/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | XBT/USD | 60710.8 | 64.587 | 62.225 | +1.03% | +0.04% | 1.21x | 0.0 | 2026-11-22T14:01:10.254572+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 10 | HYPE/USD | 62.48 | 63.595 | 67.573 | +2.02% | -0.10% | 0.65x | 3.2 | 2026-11-22T14:01:10.254572+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | SUI/USD | 0.6567 | 62.645 | 64.404 | +1.45% | -0.14% | 0.89x | 1.5 | 2026-11-22T14:01:10.254572+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 12 | ZBCN/USD | 0.001917 | 61.099 | 65.430 | +11.00% | -0.98% | 1.06x | 26.2 | 2026-11-22T14:01:10.254572+00:00 | Not calibrated | WEAK 31/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 87.200 | 3.0252 | +0.16% | 2.21x |
| 2 | NIGHT/USD | 82.081 | 0.0488 | +1.31% | 1.71x |
| 3 | MNT/USD | 70.704 | 0.3966 | -0.08% | 0.59x |
| 4 | HYPE/USD | 67.573 | 62.48 | -0.10% | 0.65x |
| 5 | TAO/USD | 66.062 | 190.9474 | -0.09% | 3.63x |
| 6 | ZBCN/USD | 65.430 | 0.001917 | -0.98% | 1.06x |
| 7 | STBL/USD | 64.616 | 0.017219 | +1.40% | 2.59x |
| 8 | ZEC/USD | 64.405 | 790.1 | -0.41% | 1.64x |
| 9 | SUI/USD | 64.404 | 0.6567 | -0.14% | 0.89x |
| 10 | ETH/USD | 63.651 | 1703.14 | -0.03% | 2.83x |
| 11 | XBT/USD | 62.225 | 60710.8 | +0.04% | 1.21x |
| 12 | LINK/USD | 60.422 | 8.7645 | +0.21% | 12.51x |

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

- Persisted scans: 1292; predictions: 10423; observations: 781937.
- Matured sampled outcomes across 1/6/24/48h: 15156; gap abstentions: 22268. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 60 (sampled only; not a success-rate estimate).
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

**Writer:** 45030354509 · **Generation:** 1292 · **Legacy run:** 45030354509
**Main quote time:** 2026-11-22T14:01:17.216599+00:00 · **Legacy report time:** 2026-11-22T14:02:16.018753+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.0252 | 100.12 | +0.16% | 2.21x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.0488 | 95.76 | +1.31% | 1.71x | STRONG 98/100 | HIGH 61/100 | Consider small entry |
| 3 | STBL/USD | 0.017219 | 86.61 | +1.40% | 2.59x | STRONG 88/100 | VERY_HIGH 79/100 | Watch |
| 4 | TAO/USD | 190.9474 | 80.59 | -0.09% | 3.63x | STRONG 70/100 | HIGH 61/100 | Watch |
| 5 | ETH/USD | 1703.14 | 78.50 | -0.03% | 2.83x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 6 | LINK/USD ⭐ | 8.7645 | 76.48 | +0.21% | 12.51x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | ZEC/USD | 790.1 | 68.77 | -0.41% | 1.64x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 8 | MNT/USD | 0.3966 | 66.21 | -0.08% | 0.59x | WEAK 33/100 | EXTREME 94/100 | Do nothing |
| 9 | XBT/USD | 60710.8 | 64.59 | +0.04% | 1.21x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 10 | HYPE/USD | 62.48 | 63.60 | -0.10% | 0.65x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 11 | SUI/USD | 0.6567 | 62.65 | -0.14% | 0.89x | WEAK 36/100 | HIGH 68/100 | Watch |
| 12 | ZBCN/USD | 0.001917 | 61.10 | -0.98% | 1.06x | WEAK 31/100 | EXTREME 85/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.37976 | 93.43 | +2.61% | 3.19x | 15352 | STRONG 92/100 | HIGH 67/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.027 | 90.33 | +0.16% | 2.21x | 13008 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.04883 | 86.53 | +1.31% | 1.71x | 9474 | STRONG 93/100 | HIGH 61/100 | Consider small entry |
| 4 | LINK/USD ⭐ | 8.77099 | 78.10 | +0.21% | 12.51x | 5557 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** NEAR/USD, NIGHT/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
