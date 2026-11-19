# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T03:15:14.757275+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44450044167
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 55eddb535aaecf5541b23e756e53617d5684a3fc (atomic ledger/results publication)
**Ledger generation:** 740 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.022261 | 80.574 | 75.057 | +8.04% | +0.65% | 1.23x | 3.1 | 2026-11-19T03:15:08.539018+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | BMT/USD | 0.0195 | 54.497 | 48.608 | +3.28% | +0.67% | 1.25x | 10.3 | 2026-11-19T03:15:08.539018+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | NEAR/USD | 3.3275 | 52.859 | 59.583 | +0.91% | -0.15% | 0.40x | 3.6 | 2026-11-19T03:15:08.539018+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | VVV/USD | 21.935 | 46.609 | 55.392 | +1.22% | -0.17% | 0.21x | 4.6 | 2026-11-19T03:15:08.539018+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | ICP/USD | 2.234 | 37.513 | 49.276 | +2.57% | -0.67% | 0.16x | 13.4 | 2026-11-19T03:15:08.539018+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 6 | DRV/USD | 0.26608 | 32.196 | 33.049 | +0.53% | +0.08% | 0.88x | 7.9 | 2026-11-19T03:15:08.539018+00:00 | Not calibrated | WEAK 36/100 | HIGH 67/100 | Watch | WATCH |
| 7 | AKE/USD | 0.01044746 | 27.128 | 34.272 | +0.54% | -0.27% | 0.42x | 8.2 | 2026-11-19T03:15:08.539018+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 75.057 | 0.022261 | +0.65% | 1.23x |
| 2 | NEAR/USD | 59.583 | 3.3275 | -0.15% | 0.40x |
| 3 | VVV/USD | 55.392 | 21.935 | -0.17% | 0.21x |
| 4 | ICP/USD | 49.276 | 2.234 | -0.67% | 0.16x |
| 5 | BMT/USD | 48.608 | 0.0195 | +0.67% | 1.25x |
| 6 | AKE/USD | 34.272 | 0.01044746 | -0.27% | 0.42x |
| 7 | DRV/USD | 33.049 | 0.26608 | +0.08% | 0.88x |

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

- Persisted scans: 740; predictions: 6036; observations: 447667.
- Matured sampled outcomes across 1/6/24/48h: 5991; gap abstentions: 13535. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44450044167 · **Generation:** 740 · **Legacy run:** 44450044167
**Main quote time:** 2026-11-19T03:15:14.757275+00:00 · **Legacy report time:** 2026-11-19T03:15:48.036815+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022261 | 80.57 | +0.65% | 1.23x | STRONG 85/100 | VERY_HIGH 74/100 | Watch |
| 2 | BMT/USD ⭐ | 0.0195 | 54.50 | +0.67% | 1.25x | MODERATE 67/100 | VERY_HIGH 73/100 | Watch |
| 3 | NEAR/USD | 3.3275 | 52.86 | -0.15% | 0.40x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | VVV/USD | 21.935 | 46.61 | -0.17% | 0.21x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | ICP/USD | 2.234 | 37.51 | -0.67% | 0.16x | WEAK 19/100 | VERY_HIGH 82/100 | Do nothing |
| 6 | DRV/USD | 0.26608 | 32.20 | +0.08% | 0.88x | WEAK 36/100 | HIGH 67/100 | Watch |
| 7 | AKE/USD | 0.01044746 | 27.13 | -0.27% | 0.42x | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022337 | 78.99 | +0.65% | 1.23x | 8079 | STRONG 84/100 | VERY_HIGH 74/100 | Watch |
| 2 | BMT/USD ⭐ | 0.0195 | 56.21 | +0.67% | 1.25x | 1599 | MODERATE 68/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** SENT/USD, BMT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
