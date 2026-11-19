# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T00:30:20.290077+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44429417200
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 650d498077ec44a819fc8eaed14b1d0519b6e686 (atomic ledger/results publication)
**Ledger generation:** 707 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.745 | 62.537 | 47.082 | +0.34% | +0.18% | 2.46x | 6.9 | 2026-11-19T00:30:13.694781+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04584 | 52.904 | 45.057 | +0.92% | +0.35% | 1.61x | 10.9 | 2026-11-19T00:30:13.694781+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | INJ/USD | 7.015 | 52.267 | 43.074 | +0.49% | -0.03% | 1.93x | 2.9 | 2026-11-19T00:30:13.694781+00:00 | Not calibrated | MODERATE 46/100 | HIGH 61/100 | Watch | WATCH |
| 4 | UAI/USD | 0.03331 | 48.424 | 32.070 | +0.60% | +0.27% | 3.72x | 6.0 | 2026-11-19T00:30:13.694781+00:00 | Not calibrated | STRONG 79/100 | HIGH 67/100 | Watch | WATCH |
| 5 | W/USD | 0.00898 | 43.237 | 25.438 | +0.79% | +0.56% | 2.70x | 22.3 | 2026-11-19T00:30:13.694781+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | AAVE/USD | 109.53 | 33.429 | 37.344 | +0.27% | +0.58% | 0.32x | 5.5 | 2026-11-19T00:30:13.694781+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | BAT/USD | 0.09354 | 31.821 | 27.434 | +0.56% | +0.07% | 1.40x | 15.0 | 2026-11-19T00:30:13.694781+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | ICP/USD | 2.195 | 29.189 | 35.482 | +0.78% | +0.50% | 0.12x | 13.7 | 2026-11-19T00:30:13.694781+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | USELESS/USD | 0.09612 | 27.618 | 32.339 | +0.59% | +0.22% | 0.42x | 19.8 | 2026-11-19T00:30:13.694781+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | PROS/USD | 0.672 | 26.261 | 14.458 | +0.33% | +1.51% | 1.43x | 38.8 | 2026-11-19T00:30:13.694781+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 11 | LUNA/USD | 4.368e-05 | 25.962 | 23.878 | +0.32% | +1.77% | 0.32x | 20.7 | 2026-11-19T00:30:13.694781+00:00 | Not calibrated | WEAK 33/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | SYRUP/USD | 0.09532 | 22.948 | 26.839 | +0.38% | +0.22% | 0.50x | 14.7 | 2026-11-19T00:30:13.694781+00:00 | Not calibrated | WEAK 36/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 47.082 | 21.745 | +0.18% | 2.46x |
| 2 | NIGHT/USD | 45.057 | 0.04584 | +0.35% | 1.61x |
| 3 | INJ/USD | 43.074 | 7.015 | -0.03% | 1.93x |
| 4 | AAVE/USD | 37.344 | 109.53 | +0.58% | 0.32x |
| 5 | ICP/USD | 35.482 | 2.195 | +0.50% | 0.12x |
| 6 | USELESS/USD | 32.339 | 0.09612 | +0.22% | 0.42x |
| 7 | UAI/USD | 32.070 | 0.03331 | +0.27% | 3.72x |
| 8 | BAT/USD | 27.434 | 0.09354 | +0.07% | 1.40x |
| 9 | SYRUP/USD | 26.839 | 0.09532 | +0.22% | 0.50x |
| 10 | W/USD | 25.438 | 0.00898 | +0.56% | 2.70x |
| 11 | LUNA/USD | 23.878 | 4.368e-05 | +1.77% | 0.32x |
| 12 | PROS/USD | 14.458 | 0.672 | +1.51% | 1.43x |

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

- Persisted scans: 707; predictions: 5709; observations: 427570.
- Matured sampled outcomes across 1/6/24/48h: 5612; gap abstentions: 13386. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44429417200 · **Generation:** 707 · **Legacy run:** 44429417200
**Main quote time:** 2026-11-19T00:30:20.290077+00:00 · **Legacy report time:** 2026-11-19T00:30:53.898117+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.745 | 62.54 | +0.18% | 2.46x | STRONG 86/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04584 | 52.90 | +0.35% | 1.61x | STRONG 76/100 | HIGH 61/100 | Consider small entry |
| 3 | INJ/USD | 7.015 | 52.27 | -0.03% | 1.93x | MODERATE 46/100 | HIGH 61/100 | Watch |
| 4 | UAI/USD | 0.03331 | 48.42 | +0.27% | 3.72x | STRONG 79/100 | HIGH 67/100 | Watch |
| 5 | W/USD | 0.00898 | 43.24 | +0.56% | 2.70x | MODERATE 67/100 | VERY_HIGH 79/100 | Watch |
| 6 | AAVE/USD | 109.53 | 33.43 | +0.58% | 0.32x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 7 | BAT/USD | 0.09354 | 31.82 | +0.07% | 1.40x | MODERATE 46/100 | VERY_HIGH 73/100 | Watch |
| 8 | ICP/USD | 2.195 | 29.19 | +0.50% | 0.12x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 9 | USELESS/USD | 0.09612 | 27.62 | +0.22% | 0.42x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 10 | PROS/USD | 0.672 | 26.26 | +1.51% | 1.43x | WEAK 43/100 | VERY_HIGH 79/100 | Watch |
| 11 | LUNA/USD | 4.368e-05 | 25.96 | +1.77% | 0.32x | WEAK 33/100 | EXTREME 87/100 | Do nothing |
| 12 | SYRUP/USD | 0.09532 | 22.95 | +0.22% | 0.50x | WEAK 36/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.775 | 47.16 | +0.18% | 2.46x | 7544 | STRONG 79/100 | HIGH 55/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04584 | 45.01 | +0.35% | 1.61x | 10804 | STRONG 73/100 | HIGH 61/100 | Watch |

**Same-run overlap:** VVV/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
