# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T00:50:21.766777+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44648915565
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 452bdf5832a472d1ea9610300dd147421306e21d (atomic ledger/results publication)
**Ledger generation:** 890 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | RARE/USD | 0.014 | 76.928 | 55.986 | +5.58% | +5.26% | 0.59x | 28.7 | 2026-11-20T00:50:17.079343+00:00 | Not calibrated | MODERATE 58/100 | EXTREME 100/100 | Do nothing | WATCH |
| 2 | XMR/USD | 499.31 | 69.866 | 56.273 | +0.37% | -0.28% | 3.11x | 2.6 | 2026-11-20T00:50:17.079343+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XLM/USD | 0.133182 | 63.446 | 55.589 | +0.36% | -0.15% | 1.86x | 3.9 | 2026-11-20T00:50:17.079343+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 4 | MEGA/USD | 0.05881 | 40.992 | 29.537 | +0.94% | -0.71% | 4.77x | 18.7 | 2026-11-20T00:50:17.079343+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | CAP/USD | 0.097153 | 36.402 | 31.833 | +0.55% | +0.21% | 1.35x | 13.2 | 2026-11-20T00:50:17.079343+00:00 | Not calibrated | MODERATE 58/100 | HIGH 66/100 | Watch | WATCH |
| 6 | SYRUP/USD | 0.09742 | 32.444 | 34.711 | +1.24% | +0.43% | 0.56x | 11.3 | 2026-11-20T00:50:17.079343+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 56.273 | 499.31 | -0.28% | 3.11x |
| 2 | RARE/USD | 55.986 | 0.014 | +5.26% | 0.59x |
| 3 | XLM/USD | 55.589 | 0.133182 | -0.15% | 1.86x |
| 4 | SYRUP/USD | 34.711 | 0.09742 | +0.43% | 0.56x |
| 5 | CAP/USD | 31.833 | 0.097153 | +0.21% | 1.35x |
| 6 | MEGA/USD | 29.537 | 0.05881 | -0.71% | 4.77x |

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

- Persisted scans: 890; predictions: 7764; observations: 537795.
- Matured sampled outcomes across 1/6/24/48h: 8489; gap abstentions: 16114. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44648915565 · **Generation:** 890 · **Legacy run:** 44648915565
**Main quote time:** 2026-11-20T00:50:21.766777+00:00 · **Legacy report time:** 2026-11-20T00:51:14.227295+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | RARE/USD | 0.014 | 76.93 | +5.26% | 0.59x | MODERATE 58/100 | EXTREME 100/100 | Do nothing |
| 2 | XMR/USD | 499.31 | 69.87 | -0.28% | 3.11x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 3 | XLM/USD | 0.133182 | 63.45 | -0.15% | 1.86x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 4 | MEGA/USD | 0.05881 | 40.99 | -0.71% | 4.77x | MODERATE 45/100 | VERY_HIGH 72/100 | Watch |
| 5 | CAP/USD ⭐ | 0.097153 | 36.40 | +0.21% | 1.35x | MODERATE 68/100 | HIGH 66/100 | Watch |
| 6 | SYRUP/USD | 0.09742 | 32.44 | +0.43% | 0.56x | WEAK 41/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD ⭐ | 0.097153 | 33.42 | +0.21% | 1.35x | 8194 | MODERATE 67/100 | HIGH 66/100 | Watch |

**Same-run overlap:** CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
