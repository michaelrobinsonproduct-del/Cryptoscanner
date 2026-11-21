# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T12:30:46.105565+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44904164656
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 22dd35d0d7bfb2867000538968f48280ee8694d1 (atomic ledger/results publication)
**Ledger generation:** 1133 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.287 | 103.667 | 97.982 | +7.46% | +0.67% | 1.23x | 4.0 | 2026-11-21T12:30:38.082906+00:00 | Not calibrated | STRONG 85/100 | HIGH 62/100 | Watch | WATCH |
| 2 | XMR/USD | 472.63 | 69.530 | 76.890 | +3.58% | -0.66% | 0.59x | 6.4 | 2026-11-21T12:30:38.082906+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | ETH/USD | 1655.5 | 65.660 | 70.610 | +2.23% | +0.25% | 0.38x | 0.1 | 2026-11-21T12:30:38.082906+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | SOL/USD | 68.96 | 60.067 | 56.822 | +0.36% | +0.10% | 1.27x | 1.5 | 2026-11-21T12:30:38.082906+00:00 | Not calibrated | MODERATE 55/100 | HIGH 55/100 | Watch | WATCH |
| 5 | AAVE/USD | 99.56 | 57.635 | 55.388 | +1.71% | +0.00% | 1.22x | 5.0 | 2026-11-21T12:30:38.082906+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 6 | SENT/USD | 0.021045 | 54.982 | 42.259 | +2.19% | -0.03% | 2.29x | 8.1 | 2026-11-21T12:30:38.082906+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | TAO/USD | 181.7383 | 53.319 | 57.056 | +0.68% | +0.64% | 0.30x | 5.4 | 2026-11-21T12:30:38.082906+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | UNI/USD | 4.49 | 52.393 | 57.013 | +0.51% | -0.18% | 0.63x | 3.1 | 2026-11-21T12:30:38.082906+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | TRX/USD | 0.302506 | 51.547 | 57.227 | +0.33% | -0.04% | 0.45x | 0.2 | 2026-11-21T12:30:38.082906+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | ZEC/USD | 764.93 | 51.277 | 59.390 | +0.93% | -0.27% | 0.32x | 4.2 | 2026-11-21T12:30:38.082906+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | SKY/USD | 0.04453 | 42.469 | 40.629 | +1.57% | -0.36% | 1.36x | 9.0 | 2026-11-21T12:30:38.082906+00:00 | Not calibrated | WEAK 41/100 | HIGH 66/100 | Watch | WATCH |
| 12 | ZAMA/USD | 0.05845 | 37.809 | 43.831 | +2.53% | +0.33% | 0.23x | 10.3 | 2026-11-21T12:30:38.082906+00:00 | Not calibrated | WEAK 44/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 97.982 | 22.287 | +0.67% | 1.23x |
| 2 | XMR/USD | 76.890 | 472.63 | -0.66% | 0.59x |
| 3 | ETH/USD | 70.610 | 1655.5 | +0.25% | 0.38x |
| 4 | ZEC/USD | 59.390 | 764.93 | -0.27% | 0.32x |
| 5 | TRX/USD | 57.227 | 0.302506 | -0.04% | 0.45x |
| 6 | TAO/USD | 57.056 | 181.7383 | +0.64% | 0.30x |
| 7 | UNI/USD | 57.013 | 4.49 | -0.18% | 0.63x |
| 8 | SOL/USD | 56.822 | 68.96 | +0.10% | 1.27x |
| 9 | AAVE/USD | 55.388 | 99.56 | +0.00% | 1.22x |
| 10 | ZAMA/USD | 43.831 | 0.05845 | +0.33% | 0.23x |
| 11 | SENT/USD | 42.259 | 0.021045 | -0.03% | 2.29x |
| 12 | SKY/USD | 40.629 | 0.04453 | -0.36% | 1.36x |

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

- Persisted scans: 1133; predictions: 8907; observations: 685223.
- Matured sampled outcomes across 1/6/24/48h: 11704; gap abstentions: 20375. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44904164656 · **Generation:** 1133 · **Legacy run:** 44904164656
**Main quote time:** 2026-11-21T12:30:46.105565+00:00 · **Legacy report time:** 2026-11-21T12:31:28.899059+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.287 | 103.67 | +0.67% | 1.23x | STRONG 95/100 | HIGH 62/100 | Watch |
| 2 | XMR/USD | 472.63 | 69.53 | -0.66% | 0.59x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 3 | ETH/USD | 1655.5 | 65.66 | +0.25% | 0.38x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 4 | SOL/USD ⭐ | 68.96 | 60.07 | +0.10% | 1.27x | MODERATE 65/100 | HIGH 55/100 | Watch |
| 5 | AAVE/USD | 99.56 | 57.63 | +0.00% | 1.22x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 6 | SENT/USD | 0.021045 | 54.98 | -0.03% | 2.29x | MODERATE 57/100 | VERY_HIGH 73/100 | Watch |
| 7 | TAO/USD | 181.7383 | 53.32 | +0.64% | 0.30x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 8 | UNI/USD | 4.49 | 52.39 | -0.18% | 0.63x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | TRX/USD | 0.302506 | 51.55 | -0.04% | 0.45x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | ZEC/USD | 764.93 | 51.28 | -0.27% | 0.32x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | SKY/USD | 0.04453 | 42.47 | -0.36% | 1.36x | WEAK 41/100 | HIGH 66/100 | Watch |
| 12 | ZAMA/USD | 0.05845 | 37.81 | +0.33% | 0.23x | WEAK 44/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 22.332 | 89.51 | +0.67% | 1.23x | 14278 | STRONG 90/100 | HIGH 62/100 | Watch |
| 2 | SOL/USD ⭐ | 69.02 | 55.92 | +0.10% | 1.27x | 57674 | MODERATE 63/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
