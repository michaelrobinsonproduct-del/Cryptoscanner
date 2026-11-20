# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T00:35:28.918667+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44646957443
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 07e302dab5e8e4ad5fde311c33fca6c0e4755050 (atomic ledger/results publication)
**Ledger generation:** 888 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 500.93 | 71.814 | 56.554 | +0.69% | +0.05% | 3.58x | 6.6 | 2026-11-20T00:35:23.696754+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XLM/USD | 0.133337 | 50.316 | 55.698 | +0.48% | -0.03% | 0.48x | 5.3 | 2026-11-20T00:35:23.696754+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 3 | ICNT/USD | 0.4275 | 41.804 | 29.241 | +0.33% | -0.49% | 3.09x | 21.1 | 2026-11-20T00:35:23.696754+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | BLESS/USD | 0.012435 | 37.273 | 31.822 | +2.01% | +1.48% | 0.81x | 29.2 | 2026-11-20T00:35:23.696754+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | MEGA/USD | 0.05923 | 29.562 | 32.052 | +1.67% | +0.92% | 0.29x | 23.7 | 2026-11-20T00:35:23.696754+00:00 | Not calibrated | WEAK 35/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | STRK/USD | 0.03186 | 25.367 | 34.628 | +0.54% | -0.59% | 0.37x | 9.4 | 2026-11-20T00:35:23.696754+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 7 | CAP/USD | 0.096871 | 23.291 | 23.127 | +0.26% | -0.78% | 1.41x | 26.6 | 2026-11-20T00:35:23.696754+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 78/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 56.554 | 500.93 | +0.05% | 3.58x |
| 2 | XLM/USD | 55.698 | 0.133337 | -0.03% | 0.48x |
| 3 | STRK/USD | 34.628 | 0.03186 | -0.59% | 0.37x |
| 4 | MEGA/USD | 32.052 | 0.05923 | +0.92% | 0.29x |
| 5 | BLESS/USD | 31.822 | 0.012435 | +1.48% | 0.81x |
| 6 | ICNT/USD | 29.241 | 0.4275 | -0.49% | 3.09x |
| 7 | CAP/USD | 23.127 | 0.096871 | -0.78% | 1.41x |

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

- Persisted scans: 888; predictions: 7750; observations: 536589.
- Matured sampled outcomes across 1/6/24/48h: 8446; gap abstentions: 16072. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44646957443 · **Generation:** 888 · **Legacy run:** 44646957443
**Main quote time:** 2026-11-20T00:35:28.918667+00:00 · **Legacy report time:** 2026-11-20T00:36:33.516767+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 500.93 | 71.81 | +0.05% | 3.58x | STRONG 91/100 | HIGH 55/100 | Watch |
| 2 | XLM/USD | 0.133337 | 50.32 | -0.03% | 0.48x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 3 | ICNT/USD | 0.4275 | 41.80 | -0.49% | 3.09x | WEAK 41/100 | VERY_HIGH 73/100 | Watch |
| 4 | BLESS/USD | 0.012435 | 37.27 | +1.48% | 0.81x | WEAK 39/100 | VERY_HIGH 79/100 | Watch |
| 5 | MEGA/USD | 0.05923 | 29.56 | +0.92% | 0.29x | WEAK 35/100 | EXTREME 87/100 | Do nothing |
| 6 | STRK/USD | 0.03186 | 25.37 | -0.59% | 0.37x | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing |
| 7 | CAP/USD | 0.096871 | 23.29 | -0.78% | 1.41x | WEAK 22/100 | VERY_HIGH 78/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 499.66 | 51.81 | +0.05% | 3.58x | 7845 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
