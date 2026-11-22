# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T20:41:12.946388+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45067668802
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** a069f4cba29807facd52efa739ad20e85554c608 (atomic ledger/results publication)
**Ledger generation:** 1333 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.0484 | 89.025 | 91.759 | +9.30% | +0.21% | 0.62x | 2.1 | 2026-11-22T20:41:06.019570+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | VVV/USD | 26.114 | 88.886 | 85.301 | +4.88% | -0.48% | 1.60x | 7.7 | 2026-11-22T20:41:06.019570+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 3 | PUMP/USD | 0.002559 | 78.120 | 82.478 | +9.17% | +0.43% | 0.35x | 7.8 | 2026-11-22T20:41:06.019570+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ZEC/USD | 786.9 | 76.880 | 61.835 | +1.12% | +0.01% | 8.92x | 2.0 | 2026-11-22T20:41:06.019570+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NEAR/USD | 2.9614 | 74.885 | 71.356 | +2.60% | +0.15% | 1.28x | 3.7 | 2026-11-22T20:41:06.019570+00:00 | Not calibrated | MODERATE 62/100 | HIGH 55/100 | Watch | WATCH |
| 6 | DRV/USD | 0.37292 | 74.177 | 83.552 | +11.25% | -1.03% | 0.58x | 11.3 | 2026-11-22T20:41:06.019570+00:00 | Not calibrated | WEAK 37/100 | EXTREME 86/100 | Do nothing | WATCH |
| 7 | XBT/USD | 60552.8 | 72.839 | 60.384 | +0.77% | +0.09% | 2.20x | 0.0 | 2026-11-22T20:41:06.019570+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 8 | PYTH/USD | 0.05171 | 71.091 | 66.340 | +5.81% | +0.47% | 1.24x | 11.6 | 2026-11-22T20:41:06.019570+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 9 | ETH/USD | 1712.94 | 66.862 | 67.728 | +1.82% | +0.21% | 0.81x | 0.1 | 2026-11-22T20:41:06.019570+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 10 | LINK/USD | 8.79238 | 62.434 | 58.145 | +2.30% | +0.24% | 1.31x | 2.3 | 2026-11-22T20:41:06.019570+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 11 | HYPE/USD | 62.48 | 61.052 | 68.373 | +2.02% | +0.42% | 0.06x | 1.6 | 2026-11-22T20:41:06.019570+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | WLD/USD | 0.2388 | 59.026 | 65.939 | +4.87% | +0.55% | 0.04x | 4.2 | 2026-11-22T20:41:06.019570+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 91.759 | 0.0484 | +0.21% | 0.62x |
| 2 | VVV/USD | 85.301 | 26.114 | -0.48% | 1.60x |
| 3 | DRV/USD | 83.552 | 0.37292 | -1.03% | 0.58x |
| 4 | PUMP/USD | 82.478 | 0.002559 | +0.43% | 0.35x |
| 5 | NEAR/USD | 71.356 | 2.9614 | +0.15% | 1.28x |
| 6 | HYPE/USD | 68.373 | 62.48 | +0.42% | 0.06x |
| 7 | ETH/USD | 67.728 | 1712.94 | +0.21% | 0.81x |
| 8 | PYTH/USD | 66.340 | 0.05171 | +0.47% | 1.24x |
| 9 | WLD/USD | 65.939 | 0.2388 | +0.55% | 0.04x |
| 10 | ZEC/USD | 61.835 | 786.9 | +0.01% | 8.92x |
| 11 | XBT/USD | 60.384 | 60552.8 | +0.09% | 2.20x |
| 12 | LINK/USD | 58.145 | 8.79238 | +0.24% | 1.31x |

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

- Persisted scans: 1333; predictions: 10915; observations: 806905.
- Matured sampled outcomes across 1/6/24/48h: 16593; gap abstentions: 22352. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45067668802 · **Generation:** 1333 · **Legacy run:** 45067668802
**Main quote time:** 2026-11-22T20:41:12.946388+00:00 · **Legacy report time:** 2026-11-22T20:42:18.655282+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.0484 | 89.02 | +0.21% | 0.62x | STRONG 75/100 | VERY_HIGH 70/100 | Watch |
| 2 | VVV/USD | 26.114 | 88.89 | -0.48% | 1.60x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 3 | PUMP/USD | 0.002559 | 78.12 | +0.43% | 0.35x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 4 | ZEC/USD | 786.9 | 76.88 | +0.01% | 8.92x | STRONG 83/100 | HIGH 55/100 | Watch |
| 5 | NEAR/USD ⭐ | 2.9614 | 74.88 | +0.15% | 1.28x | STRONG 72/100 | HIGH 55/100 | Watch |
| 6 | DRV/USD | 0.37292 | 74.18 | -1.03% | 0.58x | WEAK 37/100 | EXTREME 86/100 | Do nothing |
| 7 | XBT/USD | 60552.8 | 72.84 | +0.09% | 2.20x | STRONG 81/100 | HIGH 55/100 | Watch |
| 8 | PYTH/USD | 0.05171 | 71.09 | +0.47% | 1.24x | MODERATE 66/100 | VERY_HIGH 80/100 | Watch |
| 9 | ETH/USD | 1712.94 | 66.86 | +0.21% | 0.81x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 10 | LINK/USD ⭐ | 8.79238 | 62.43 | +0.24% | 1.31x | STRONG 86/100 | HIGH 55/100 | Watch |
| 11 | HYPE/USD | 62.48 | 61.05 | +0.42% | 0.06x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 12 | WLD/USD | 0.2388 | 59.03 | +0.55% | 0.04x | MODERATE 60/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 2.9611 | 78.58 | +0.15% | 1.28x | 12654 | STRONG 74/100 | HIGH 55/100 | Watch |
| 2 | LINK/USD ⭐ | 8.79238 | 72.28 | +0.24% | 1.31x | 4532 | STRONG 91/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NEAR/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
