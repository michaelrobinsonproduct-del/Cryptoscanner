# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T00:20:20.671783+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44428087320
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 42af48f074c303f489fa0d35a33a40e3c9962f58 (atomic ledger/results publication)
**Ledger generation:** 705 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BAT/USD | 0.09355 | 50.059 | 32.318 | +0.57% | +0.55% | 2.92x | 5.3 | 2026-11-19T00:20:15.983878+00:00 | Not calibrated | STRONG 80/100 | HIGH 67/100 | Watch | WATCH |
| 2 | ATOM/USD | 1.3046 | 49.927 | 33.042 | +0.46% | +0.38% | 2.95x | 7.7 | 2026-11-19T00:20:15.983878+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.0456 | 47.539 | 43.455 | +0.40% | +0.31% | 1.25x | 6.6 | 2026-11-19T00:20:15.983878+00:00 | Not calibrated | MODERATE 59/100 | HIGH 55/100 | Watch | WATCH |
| 4 | UAI/USD | 0.03327 | 44.871 | 28.213 | +0.48% | +0.33% | 2.52x | 12.0 | 2026-11-19T00:20:15.983878+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | USELESS/USD | 0.09628 | 33.423 | 37.265 | +0.75% | +0.87% | 0.18x | 12.5 | 2026-11-19T00:20:15.983878+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | ICP/USD | 2.186 | 28.227 | 37.084 | +0.37% | +0.09% | 0.07x | 4.6 | 2026-11-19T00:20:15.983878+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 7 | W/USD | 0.00895 | 27.101 | 23.050 | +0.45% | +0.00% | 1.41x | 22.4 | 2026-11-19T00:20:15.983878+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 8 | MEGA/USD | 0.05632 | 23.981 | 22.757 | +0.57% | +1.09% | 0.57x | 24.9 | 2026-11-19T00:20:15.983878+00:00 | Not calibrated | WEAK 32/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 43.455 | 0.0456 | +0.31% | 1.25x |
| 2 | USELESS/USD | 37.265 | 0.09628 | +0.87% | 0.18x |
| 3 | ICP/USD | 37.084 | 2.186 | +0.09% | 0.07x |
| 4 | ATOM/USD | 33.042 | 1.3046 | +0.38% | 2.95x |
| 5 | BAT/USD | 32.318 | 0.09355 | +0.55% | 2.92x |
| 6 | UAI/USD | 28.213 | 0.03327 | +0.33% | 2.52x |
| 7 | W/USD | 23.050 | 0.00895 | +0.00% | 1.41x |
| 8 | MEGA/USD | 22.757 | 0.05632 | +1.09% | 0.57x |

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

- Persisted scans: 705; predictions: 5693; observations: 426352.
- Matured sampled outcomes across 1/6/24/48h: 5585; gap abstentions: 13362. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44428087320 · **Generation:** 705 · **Legacy run:** 44428087320
**Main quote time:** 2026-11-19T00:20:20.671783+00:00 · **Legacy report time:** 2026-11-19T00:20:53.996878+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BAT/USD ⭐ | 0.09355 | 50.06 | +0.55% | 2.92x | STRONG 90/100 | HIGH 67/100 | Consider small entry |
| 2 | ATOM/USD ⭐ | 1.3046 | 49.93 | +0.38% | 2.95x | STRONG 90/100 | HIGH 60/100 | Consider small entry |
| 3 | NIGHT/USD ⭐ | 0.0456 | 47.54 | +0.31% | 1.25x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 4 | UAI/USD ⭐ | 0.03327 | 44.87 | +0.33% | 2.52x | STRONG 82/100 | VERY_HIGH 73/100 | Watch |
| 5 | USELESS/USD | 0.09628 | 33.42 | +0.87% | 0.18x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 6 | ICP/USD | 2.186 | 28.23 | +0.09% | 0.07x | WEAK 34/100 | VERY_HIGH 70/100 | Do nothing |
| 7 | W/USD | 0.00895 | 27.10 | +0.00% | 1.41x | WEAK 39/100 | VERY_HIGH 79/100 | Watch |
| 8 | MEGA/USD | 0.05632 | 23.98 | +1.09% | 0.57x | WEAK 32/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ATOM/USD ⭐ | 1.3046 | 38.66 | +0.38% | 2.95x | 2738 | STRONG 84/100 | HIGH 60/100 | Consider small entry |
| 2 | BAT/USD ⭐ | 0.09355 | 37.51 | +0.55% | 2.92x | 1971 | STRONG 84/100 | HIGH 67/100 | Consider small entry |
| 3 | NIGHT/USD ⭐ | 0.0456 | 37.08 | +0.31% | 1.25x | 10884 | MODERATE 64/100 | HIGH 55/100 | Watch |
| 4 | UAI/USD ⭐ | 0.03327 | 29.88 | +0.33% | 2.52x | 1980 | STRONG 75/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** BAT/USD, ATOM/USD, NIGHT/USD, UAI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
