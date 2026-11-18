# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T23:50:21.829237+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44423996474
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 25aec72a67020473da15fa2b58a591ebbae06230 (atomic ledger/results publication)
**Ledger generation:** 699 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.020806 | 84.838 | 74.632 | +11.45% | +1.82% | 1.11x | 3.4 | 2026-11-18T23:50:15.962988+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | MEGA/USD | 0.05601 | 65.457 | 67.323 | +8.46% | +1.12% | 0.25x | 17.8 | 2026-11-18T23:50:15.962988+00:00 | Not calibrated | MODERATE 58/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | TRX/USD | 0.309923 | 60.522 | 44.471 | +0.66% | +0.21% | 4.28x | 0.0 | 2026-11-18T23:50:15.962988+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 4 | AKE/USD | 0.01034772 | 56.935 | 46.136 | +3.64% | +1.64% | 1.26x | 27.8 | 2026-11-18T23:50:15.962988+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5203 | 39.094 | 42.035 | +2.16% | +1.15% | 0.13x | 9.6 | 2026-11-18T23:50:15.962988+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.04526 | 38.233 | 43.061 | +0.82% | -0.15% | 0.59x | 13.3 | 2026-11-18T23:50:15.962988+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 74.632 | 0.020806 | +1.82% | 1.11x |
| 2 | MEGA/USD | 67.323 | 0.05601 | +1.12% | 0.25x |
| 3 | AKE/USD | 46.136 | 0.01034772 | +1.64% | 1.26x |
| 4 | TRX/USD | 44.471 | 0.309923 | +0.21% | 4.28x |
| 5 | NIGHT/USD | 43.061 | 0.04526 | -0.15% | 0.59x |
| 6 | AKT/USD | 42.035 | 0.5203 | +1.15% | 0.13x |

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

- Persisted scans: 699; predictions: 5650; observations: 422698.
- Matured sampled outcomes across 1/6/24/48h: 5514; gap abstentions: 13290. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44423996474 · **Generation:** 699 · **Legacy run:** 44423996474
**Main quote time:** 2026-11-18T23:50:21.829237+00:00 · **Legacy report time:** 2026-11-18T23:50:58.203252+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.020806 | 84.84 | +1.82% | 1.11x | STRONG 87/100 | VERY_HIGH 74/100 | Watch |
| 2 | MEGA/USD | 0.05601 | 65.46 | +1.12% | 0.25x | MODERATE 58/100 | EXTREME 88/100 | Do nothing |
| 3 | TRX/USD ⭐ | 0.309923 | 60.52 | +0.21% | 4.28x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 4 | AKE/USD ⭐ | 0.01034772 | 56.93 | +1.64% | 1.26x | MODERATE 63/100 | VERY_HIGH 72/100 | Watch |
| 5 | AKT/USD | 0.5203 | 39.09 | +1.15% | 0.13x | MODERATE 50/100 | VERY_HIGH 75/100 | Watch |
| 6 | NIGHT/USD | 0.04526 | 38.23 | -0.15% | 0.59x | WEAK 19/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.020834 | 76.69 | +1.82% | 1.11x | 6716 | STRONG 78/100 | VERY_HIGH 80/100 | Watch |
| 2 | AKE/USD ⭐ | 0.01034772 | 74.38 | +1.64% | 1.26x | 3400 | STRONG 77/100 | HIGH 66/100 | Watch |
| 3 | TRX/USD ⭐ | 0.310009 | 59.72 | +0.21% | 4.28x | 4051 | STRONG 95/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** SENT/USD, TRX/USD, AKE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
