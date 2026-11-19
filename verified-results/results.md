# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T05:05:21.841099+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44462621912
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** e23a8c4424877480d97d95cff078b57d1fb0b9ab (atomic ledger/results publication)
**Ledger generation:** 762 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.383 | 80.717 | 74.008 | +3.29% | -1.21% | 2.28x | 5.8 | 2026-11-19T05:05:14.242943+00:00 | Not calibrated | STRONG 70/100 | HIGH 65/100 | Do nothing | WATCH |
| 2 | NEAR/USD | 3.4129 | 73.561 | 77.616 | +3.50% | +0.54% | 0.33x | 3.8 | 2026-11-19T05:05:14.242943+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | HYPE/USD | 67.52 | 70.198 | 60.958 | +0.96% | -0.38% | 2.12x | 1.5 | 2026-11-19T05:05:14.242943+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ADA/USD | 0.152622 | 69.168 | 59.758 | +0.90% | -0.28% | 2.08x | 3.1 | 2026-11-19T05:05:14.242943+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ZEC/USD | 932.76 | 67.884 | 70.491 | +2.28% | +0.01% | 0.73x | 1.0 | 2026-11-19T05:05:14.242943+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | SOL/USD | 74.5 | 64.542 | 63.467 | +1.31% | -0.12% | 1.17x | 1.3 | 2026-11-19T05:05:14.242943+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 7 | ETH/USD | 1795.64 | 63.775 | 63.208 | +1.18% | -0.23% | 1.17x | 0.1 | 2026-11-19T05:05:14.242943+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 8 | TAO/USD | 195.0576 | 58.976 | 63.313 | +1.61% | -0.36% | 0.75x | 6.0 | 2026-11-19T05:05:14.242943+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | XBT/USD | 63417.9 | 57.258 | 59.809 | +0.69% | -0.21% | 0.85x | 0.0 | 2026-11-19T05:05:14.242943+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 10 | LINK/USD | 9.11601 | 53.440 | 57.051 | +0.48% | -0.36% | 0.82x | 2.6 | 2026-11-19T05:05:14.242943+00:00 | Not calibrated | WEAK 32/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | XRP/USD | 0.97396 | 51.270 | 60.447 | +0.79% | -0.19% | 0.18x | 0.1 | 2026-11-19T05:05:14.242943+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | LTC/USD | 44.43 | 51.055 | 57.148 | +0.95% | -0.25% | 0.51x | 2.3 | 2026-11-19T05:05:14.242943+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 77.616 | 3.4129 | +0.54% | 0.33x |
| 2 | VVV/USD | 74.008 | 22.383 | -1.21% | 2.28x |
| 3 | ZEC/USD | 70.491 | 932.76 | +0.01% | 0.73x |
| 4 | SOL/USD | 63.467 | 74.5 | -0.12% | 1.17x |
| 5 | TAO/USD | 63.313 | 195.0576 | -0.36% | 0.75x |
| 6 | ETH/USD | 63.208 | 1795.64 | -0.23% | 1.17x |
| 7 | HYPE/USD | 60.958 | 67.52 | -0.38% | 2.12x |
| 8 | XRP/USD | 60.447 | 0.97396 | -0.19% | 0.18x |
| 9 | XBT/USD | 59.809 | 63417.9 | -0.21% | 0.85x |
| 10 | ADA/USD | 59.758 | 0.152622 | -0.28% | 2.08x |
| 11 | LTC/USD | 57.148 | 44.43 | -0.25% | 0.51x |
| 12 | LINK/USD | 57.051 | 9.11601 | -0.36% | 0.82x |

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

- Persisted scans: 762; predictions: 6288; observations: 461064.
- Matured sampled outcomes across 1/6/24/48h: 6274; gap abstentions: 13716. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44462621912 · **Generation:** 762 · **Legacy run:** 44462621912
**Main quote time:** 2026-11-19T05:05:21.841099+00:00 · **Legacy report time:** 2026-11-19T05:05:55.294885+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.383 | 80.72 | -1.21% | 2.28x | STRONG 70/100 | HIGH 65/100 | Do nothing |
| 2 | NEAR/USD | 3.4129 | 73.56 | +0.54% | 0.33x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 3 | HYPE/USD | 67.52 | 70.20 | -0.38% | 2.12x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | ADA/USD | 0.152622 | 69.17 | -0.28% | 2.08x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 5 | ZEC/USD | 932.76 | 67.88 | +0.01% | 0.73x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 6 | SOL/USD | 74.5 | 64.54 | -0.12% | 1.17x | WEAK 42/100 | HIGH 68/100 | Watch |
| 7 | ETH/USD | 1795.64 | 63.77 | -0.23% | 1.17x | WEAK 42/100 | HIGH 68/100 | Watch |
| 8 | TAO/USD | 195.0576 | 58.98 | -0.36% | 0.75x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | XBT/USD | 63417.9 | 57.26 | -0.21% | 0.85x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 10 | LINK/USD | 9.11601 | 53.44 | -0.36% | 0.82x | WEAK 32/100 | HIGH 68/100 | Do nothing |
| 11 | XRP/USD | 0.97396 | 51.27 | -0.19% | 0.18x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | LTC/USD | 44.43 | 51.06 | -0.25% | 0.51x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
