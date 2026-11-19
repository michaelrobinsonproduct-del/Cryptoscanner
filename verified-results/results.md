# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T01:20:19.811773+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44436038771
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 576ae5170d9f34a998db3c61a606e8bbcd1bba69 (atomic ledger/results publication)
**Ledger generation:** 717 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.0213 | 62.566 | 51.049 | +3.37% | +0.99% | 1.66x | 8.0 | 2026-11-19T01:20:12.042690+00:00 | Not calibrated | STRONG 76/100 | HIGH 67/100 | Watch | WATCH |
| 2 | MEGA/USD | 0.05773 | 53.917 | 45.942 | +3.09% | +0.68% | 1.46x | 13.9 | 2026-11-19T01:20:12.042690+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | LTC/USD | 44.13 | 45.775 | 45.700 | +0.27% | -0.25% | 1.13x | 4.5 | 2026-11-19T01:20:12.042690+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 4 | DRV/USD | 0.26743 | 35.260 | 37.212 | +1.04% | +0.07% | 0.77x | 6.4 | 2026-11-19T01:20:12.042690+00:00 | Not calibrated | WEAK 38/100 | HIGH 67/100 | Watch | WATCH |
| 5 | TRX/USD | 0.310179 | 34.606 | 40.472 | +0.29% | -0.08% | 0.45x | 0.0 | 2026-11-19T01:20:12.042690+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | TON/USD | 1.024 | 29.080 | 31.672 | +0.29% | +0.39% | 0.54x | 9.8 | 2026-11-19T01:20:12.042690+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | TRUMP/USD | 0.949 | 27.154 | 32.410 | +0.42% | -0.21% | 0.58x | 10.5 | 2026-11-19T01:20:12.042690+00:00 | Not calibrated | WEAK 14/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | W/USD | 0.00895 | 25.983 | 28.643 | +0.45% | -0.56% | 1.01x | 11.2 | 2026-11-19T01:20:12.042690+00:00 | Not calibrated | WEAK 18/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 51.049 | 0.0213 | +0.99% | 1.66x |
| 2 | MEGA/USD | 45.942 | 0.05773 | +0.68% | 1.46x |
| 3 | LTC/USD | 45.700 | 44.13 | -0.25% | 1.13x |
| 4 | TRX/USD | 40.472 | 0.310179 | -0.08% | 0.45x |
| 5 | DRV/USD | 37.212 | 0.26743 | +0.07% | 0.77x |
| 6 | TRUMP/USD | 32.410 | 0.949 | -0.21% | 0.58x |
| 7 | TON/USD | 31.672 | 1.024 | +0.39% | 0.54x |
| 8 | W/USD | 28.643 | 0.00895 | -0.56% | 1.01x |

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

- Persisted scans: 717; predictions: 5825; observations: 433660.
- Matured sampled outcomes across 1/6/24/48h: 5699; gap abstentions: 13443. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44436038771 · **Generation:** 717 · **Legacy run:** 44436038771
**Main quote time:** 2026-11-19T01:20:19.811773+00:00 · **Legacy report time:** 2026-11-19T01:20:57.553233+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.0213 | 62.57 | +0.99% | 1.66x | STRONG 86/100 | HIGH 67/100 | Consider small entry |
| 2 | MEGA/USD ⭐ | 0.05773 | 53.92 | +0.68% | 1.46x | STRONG 77/100 | VERY_HIGH 73/100 | Watch |
| 3 | LTC/USD | 44.13 | 45.78 | -0.25% | 1.13x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 4 | DRV/USD | 0.26743 | 35.26 | +0.07% | 0.77x | WEAK 38/100 | HIGH 67/100 | Watch |
| 5 | TRX/USD | 0.310179 | 34.61 | -0.08% | 0.45x | WEAK 22/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | TON/USD | 1.024 | 29.08 | +0.39% | 0.54x | MODERATE 45/100 | VERY_HIGH 75/100 | Watch |
| 7 | TRUMP/USD | 0.949 | 27.15 | -0.21% | 0.58x | WEAK 14/100 | EXTREME 87/100 | Do nothing |
| 8 | W/USD | 0.00895 | 25.98 | -0.56% | 1.01x | WEAK 18/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.021218 | 64.15 | +0.99% | 1.66x | 7357 | STRONG 77/100 | VERY_HIGH 79/100 | Watch |
| 2 | MEGA/USD ⭐ | 0.05773 | 52.93 | +0.68% | 1.46x | 1349 | STRONG 76/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** SENT/USD, MEGA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
