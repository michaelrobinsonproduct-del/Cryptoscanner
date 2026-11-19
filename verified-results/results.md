# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T01:30:22.328890+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44437293172
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 508684f7803e9d99a84c9ceb1aa5ebee7fb23c1b (atomic ledger/results publication)
**Ledger generation:** 719 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MEGA/USD | 0.05765 | 58.459 | 45.762 | +2.95% | +0.02% | 2.26x | 12.2 | 2026-11-19T01:30:15.940181+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | SENT/USD | 0.021151 | 51.381 | 46.431 | +2.65% | -0.71% | 1.85x | 7.1 | 2026-11-19T01:30:15.940181+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | TRX/USD | 0.310072 | 33.422 | 39.165 | +0.26% | -0.18% | 0.52x | 2.2 | 2026-11-19T01:30:15.940181+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | STABLE/USD | 0.02289 | 29.093 | 22.312 | +0.66% | +0.18% | 1.59x | 26.2 | 2026-11-19T01:30:15.940181+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | DRV/USD | 0.26656 | 26.465 | 29.090 | +0.71% | -0.31% | 0.89x | 18.0 | 2026-11-19T01:30:15.940181+00:00 | Not calibrated | WEAK 13/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 6 | BAT/USD | 0.09335 | 20.886 | 27.625 | +0.35% | -0.69% | 0.67x | 11.8 | 2026-11-19T01:30:15.940181+00:00 | Not calibrated | WEAK 10/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 46.431 | 0.021151 | -0.71% | 1.85x |
| 2 | MEGA/USD | 45.762 | 0.05765 | +0.02% | 2.26x |
| 3 | TRX/USD | 39.165 | 0.310072 | -0.18% | 0.52x |
| 4 | DRV/USD | 29.090 | 0.26656 | -0.31% | 0.89x |
| 5 | BAT/USD | 27.625 | 0.09335 | -0.69% | 0.67x |
| 6 | STABLE/USD | 22.312 | 0.02289 | +0.18% | 1.59x |

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

- Persisted scans: 719; predictions: 5835; observations: 434878.
- Matured sampled outcomes across 1/6/24/48h: 5732; gap abstentions: 13452. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44437293172 · **Generation:** 719 · **Legacy run:** 44437293172
**Main quote time:** 2026-11-19T01:30:22.328890+00:00 · **Legacy report time:** 2026-11-19T01:30:59.753890+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD | 0.05765 | 58.46 | +0.02% | 2.26x | MODERATE 69/100 | VERY_HIGH 73/100 | Watch |
| 2 | SENT/USD | 0.021151 | 51.38 | -0.71% | 1.85x | MODERATE 46/100 | VERY_HIGH 73/100 | Watch |
| 3 | TRX/USD | 0.310072 | 33.42 | -0.18% | 0.52x | WEAK 22/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | STABLE/USD ⭐ | 0.02289 | 29.09 | +0.18% | 1.59x | MODERATE 50/100 | VERY_HIGH 79/100 | Watch |
| 5 | DRV/USD | 0.26656 | 26.47 | -0.31% | 0.89x | WEAK 13/100 | VERY_HIGH 79/100 | Do nothing |
| 6 | BAT/USD | 0.09335 | 20.89 | -0.69% | 0.67x | WEAK 10/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | STABLE/USD ⭐ | 0.02289 | 29.64 | +0.18% | 1.59x | 2202 | MODERATE 50/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** STABLE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
