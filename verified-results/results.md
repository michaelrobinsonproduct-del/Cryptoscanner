# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T22:40:59.817307+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45906184802
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2f2bbe8ae1dfe26a91fb4d6977fabb106fd701c0 (atomic ledger/results publication)
**Ledger generation:** 1923 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.39049 | 93.596 | 72.282 | +9.14% | +1.26% | 4.14x | 22.5 | 2026-11-26T22:40:50.708215+00:00 | Not calibrated | STRONG 92/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | LTC/USD | 44.02 | 88.638 | 75.334 | +3.07% | -0.34% | 3.40x | 2.3 | 2026-11-26T22:40:50.708215+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ZRO/USD | 1.122 | 85.812 | 76.549 | +9.57% | -1.15% | 6.43x | 8.9 | 2026-11-26T22:40:50.708215+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | LINK/USD | 9.32207 | 68.704 | 75.242 | +3.07% | -0.32% | 0.50x | 2.5 | 2026-11-26T22:40:50.708215+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | ADA/USD | 0.149244 | 67.461 | 68.650 | +2.38% | -0.31% | 1.04x | 4.8 | 2026-11-26T22:40:50.708215+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 6 | PIEVERSE/USD | 3.8304 | 66.136 | 74.247 | +8.18% | -0.66% | 0.52x | 21.7 | 2026-11-26T22:40:50.708215+00:00 | Not calibrated | WEAK 28/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.5043 | 63.440 | 69.013 | +6.59% | -0.02% | 0.45x | 17.8 | 2026-11-26T22:40:50.708215+00:00 | Not calibrated | WEAK 32/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | XRP/USD | 0.94732 | 58.320 | 62.989 | +1.15% | -0.31% | 0.69x | 0.1 | 2026-11-26T22:40:50.708215+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | SOL/USD | 71.13 | 56.953 | 61.656 | +1.05% | -0.15% | 0.61x | 1.4 | 2026-11-26T22:40:50.708215+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | HYPE/USD | 62.33 | 55.327 | 62.263 | +1.15% | -0.10% | 0.35x | 1.6 | 2026-11-26T22:40:50.708215+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | ONDO/USD | 0.28869 | 52.207 | 47.746 | +2.19% | -0.31% | 1.60x | 0.3 | 2026-11-26T22:40:50.708215+00:00 | Not calibrated | MODERATE 46/100 | HIGH 66/100 | Watch | WATCH |
| 12 | TAO/USD | 183.9896 | 48.100 | 55.618 | +1.32% | -0.20% | 0.35x | 2.0 | 2026-11-26T22:40:50.708215+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZRO/USD | 76.549 | 1.122 | -1.15% | 6.43x |
| 2 | LTC/USD | 75.334 | 44.02 | -0.34% | 3.40x |
| 3 | LINK/USD | 75.242 | 9.32207 | -0.32% | 0.50x |
| 4 | PIEVERSE/USD | 74.247 | 3.8304 | -0.66% | 0.52x |
| 5 | DRV/USD | 72.282 | 0.39049 | +1.26% | 4.14x |
| 6 | AKT/USD | 69.013 | 0.5043 | -0.02% | 0.45x |
| 7 | ADA/USD | 68.650 | 0.149244 | -0.31% | 1.04x |
| 8 | XRP/USD | 62.989 | 0.94732 | -0.31% | 0.69x |
| 9 | HYPE/USD | 62.263 | 62.33 | -0.10% | 0.35x |
| 10 | SOL/USD | 61.656 | 71.13 | -0.15% | 0.61x |
| 11 | TAO/USD | 55.618 | 183.9896 | -0.20% | 0.35x |
| 12 | ONDO/USD | 47.746 | 0.28869 | -0.31% | 1.60x |

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

- Persisted scans: 1923; predictions: 16811; observations: 1164811.
- Matured sampled outcomes across 1/6/24/48h: 36632; gap abstentions: 25317. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 147 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45906184802 · **Generation:** 1923 · **Legacy run:** 45906184802
**Main quote time:** 2026-11-26T22:40:59.817307+00:00 · **Legacy report time:** 2026-11-26T22:41:34.209705+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.39049 | 93.60 | +1.26% | 4.14x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | LTC/USD | 44.02 | 88.64 | -0.34% | 3.40x | STRONG 74/100 | HIGH 61/100 | Watch |
| 3 | ZRO/USD | 1.122 | 85.81 | -1.15% | 6.43x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 4 | LINK/USD | 9.32207 | 68.70 | -0.32% | 0.50x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 5 | ADA/USD | 0.149244 | 67.46 | -0.31% | 1.04x | WEAK 44/100 | HIGH 68/100 | Watch |
| 6 | PIEVERSE/USD | 3.8304 | 66.14 | -0.66% | 0.52x | WEAK 28/100 | EXTREME 88/100 | Do nothing |
| 7 | AKT/USD | 0.5043 | 63.44 | -0.02% | 0.45x | WEAK 32/100 | EXTREME 87/100 | Do nothing |
| 8 | XRP/USD | 0.94732 | 58.32 | -0.31% | 0.69x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | SOL/USD | 71.13 | 56.95 | -0.15% | 0.61x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | HYPE/USD | 62.33 | 55.33 | -0.10% | 0.35x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | ONDO/USD | 0.28869 | 52.21 | -0.31% | 1.60x | MODERATE 46/100 | HIGH 66/100 | Watch |
| 12 | TAO/USD | 183.9896 | 48.10 | -0.20% | 0.35x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.39097 | 86.93 | +1.26% | 4.14x | 8676 | STRONG 98/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
