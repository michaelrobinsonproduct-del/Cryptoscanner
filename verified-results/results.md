# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T04:55:21.084931+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44461502556
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 51e83dafd523d4ae6322ce742ef312843c73ab45 (atomic ledger/results publication)
**Ledger generation:** 760 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.51 | 84.329 | 72.348 | +3.87% | -0.60% | 3.59x | 17.3 | 2026-11-19T04:55:13.468728+00:00 | Not calibrated | MODERATE 67/100 | HIGH 67/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.4226 | 77.592 | 79.679 | +3.80% | +0.29% | 0.64x | 3.8 | 2026-11-19T04:55:13.468728+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | LTC/USD | 44.55 | 74.496 | 59.046 | +1.23% | +0.09% | 26.16x | 2.2 | 2026-11-19T04:55:13.468728+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 4 | HYPE/USD | 67.75 | 70.753 | 62.629 | +1.30% | +0.37% | 1.63x | 3.0 | 2026-11-19T04:55:13.468728+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | ZEC/USD | 933.76 | 67.586 | 69.920 | +2.39% | +0.47% | 0.53x | 3.6 | 2026-11-19T04:55:13.468728+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | PEARL/USD | 2.3494 | 65.932 | 48.130 | +0.40% | +0.56% | 2.63x | 18.8 | 2026-11-19T04:55:13.468728+00:00 | Not calibrated | STRONG 83/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SOL/USD | 74.55 | 63.002 | 63.943 | +1.37% | -0.16% | 0.99x | 1.3 | 2026-11-19T04:55:13.468728+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XBT/USD | 63570.6 | 60.663 | 61.506 | +0.93% | +0.19% | 0.82x | 0.0 | 2026-11-19T04:55:13.468728+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 9 | TAO/USD | 195.1774 | 59.958 | 62.965 | +1.68% | -0.01% | 0.71x | 7.5 | 2026-11-19T04:55:13.468728+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XRP/USD | 0.97555 | 59.880 | 61.598 | +0.95% | +0.38% | 0.64x | 0.1 | 2026-11-19T04:55:13.468728+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ETH/USD | 1798.88 | 57.906 | 64.486 | +1.36% | +0.05% | 0.32x | 0.1 | 2026-11-19T04:55:13.468728+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ETHFI/USD | 0.52 | 57.206 | 65.039 | +6.14% | -0.63% | 0.53x | 17.4 | 2026-11-19T04:55:13.468728+00:00 | Not calibrated | WEAK 29/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 79.679 | 3.4226 | +0.29% | 0.64x |
| 2 | VVV/USD | 72.348 | 22.51 | -0.60% | 3.59x |
| 3 | ZEC/USD | 69.920 | 933.76 | +0.47% | 0.53x |
| 4 | ETHFI/USD | 65.039 | 0.52 | -0.63% | 0.53x |
| 5 | ETH/USD | 64.486 | 1798.88 | +0.05% | 0.32x |
| 6 | SOL/USD | 63.943 | 74.55 | -0.16% | 0.99x |
| 7 | TAO/USD | 62.965 | 195.1774 | -0.01% | 0.71x |
| 8 | HYPE/USD | 62.629 | 67.75 | +0.37% | 1.63x |
| 9 | XRP/USD | 61.598 | 0.97555 | +0.38% | 0.64x |
| 10 | XBT/USD | 61.506 | 63570.6 | +0.19% | 0.82x |
| 11 | LTC/USD | 59.046 | 44.55 | +0.09% | 26.16x |
| 12 | PEARL/USD | 48.130 | 2.3494 | +0.56% | 2.63x |

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

- Persisted scans: 760; predictions: 6264; observations: 459846.
- Matured sampled outcomes across 1/6/24/48h: 6247; gap abstentions: 13698. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44461502556 · **Generation:** 760 · **Legacy run:** 44461502556
**Main quote time:** 2026-11-19T04:55:21.084931+00:00 · **Legacy report time:** 2026-11-19T04:55:55.082219+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.51 | 84.33 | -0.60% | 3.59x | MODERATE 67/100 | HIGH 67/100 | Watch |
| 2 | NEAR/USD | 3.4226 | 77.59 | +0.29% | 0.64x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 3 | LTC/USD | 44.55 | 74.50 | +0.09% | 26.16x | STRONG 82/100 | HIGH 55/100 | Watch |
| 4 | HYPE/USD ⭐ | 67.75 | 70.75 | +0.37% | 1.63x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 5 | ZEC/USD | 933.76 | 67.59 | +0.47% | 0.53x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 6 | PEARL/USD | 2.3494 | 65.93 | +0.56% | 2.63x | STRONG 83/100 | HIGH 61/100 | Watch |
| 7 | SOL/USD | 74.55 | 63.00 | -0.16% | 0.99x | WEAK 37/100 | HIGH 68/100 | Watch |
| 8 | XBT/USD | 63570.6 | 60.66 | +0.19% | 0.82x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 9 | TAO/USD | 195.1774 | 59.96 | -0.01% | 0.71x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | XRP/USD | 0.97555 | 59.88 | +0.38% | 0.64x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 11 | ETH/USD | 1798.88 | 57.91 | +0.05% | 0.32x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 12 | ETHFI/USD | 0.52 | 57.21 | -0.63% | 0.53x | WEAK 29/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 67.73 | 67.92 | +0.37% | 1.63x | 14615 | STRONG 89/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
