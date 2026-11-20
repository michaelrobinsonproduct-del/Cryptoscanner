# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T00:40:37.137896+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44647608801
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** fe46503f01e53a16d27b4116dcb11634011e5655 (atomic ledger/results publication)
**Ledger generation:** 889 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 500.97 | 70.816 | 56.812 | +0.70% | -0.20% | 6.49x | 6.2 | 2026-11-20T00:40:29.933353+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XLM/USD | 0.133235 | 50.631 | 56.434 | +0.40% | -0.13% | 0.48x | 2.8 | 2026-11-20T00:40:29.933353+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 3 | MEGA/USD | 0.05959 | 42.177 | 38.996 | +2.28% | +2.02% | 0.31x | 18.5 | 2026-11-20T00:40:29.933353+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.4275 | 37.220 | 29.260 | +0.33% | -0.19% | 1.89x | 21.1 | 2026-11-20T00:40:29.933353+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 5 | USELESS/USD | 0.0995 | 26.295 | 31.990 | +0.25% | -0.30% | 0.58x | 22.2 | 2026-11-20T00:40:29.933353+00:00 | Not calibrated | WEAK 8/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | RARE/USD | 0.01336 | 23.930 | 21.407 | +0.75% | +1.37% | 0.57x | 30.1 | 2026-11-20T00:40:29.933353+00:00 | Not calibrated | WEAK 32/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | STRK/USD | 0.03177 | 21.105 | 31.045 | +0.25% | -0.84% | 0.43x | 12.6 | 2026-11-20T00:40:29.933353+00:00 | Not calibrated | WEAK 11/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | BLESS/USD | 0.012286 | 8.217 | 20.716 | +0.79% | -1.71% | 0.61x | 34.2 | 2026-11-20T00:40:29.933353+00:00 | Not calibrated | WEAK 0/100 | EXTREME 97/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 56.812 | 500.97 | -0.20% | 6.49x |
| 2 | XLM/USD | 56.434 | 0.133235 | -0.13% | 0.48x |
| 3 | MEGA/USD | 38.996 | 0.05959 | +2.02% | 0.31x |
| 4 | USELESS/USD | 31.990 | 0.0995 | -0.30% | 0.58x |
| 5 | STRK/USD | 31.045 | 0.03177 | -0.84% | 0.43x |
| 6 | ICNT/USD | 29.260 | 0.4275 | -0.19% | 1.89x |
| 7 | RARE/USD | 21.407 | 0.01336 | +1.37% | 0.57x |
| 8 | BLESS/USD | 20.716 | 0.012286 | -1.71% | 0.61x |

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

- Persisted scans: 889; predictions: 7758; observations: 537192.
- Matured sampled outcomes across 1/6/24/48h: 8469; gap abstentions: 16092. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44647608801 · **Generation:** 889 · **Legacy run:** 44647608801
**Main quote time:** 2026-11-20T00:40:37.137896+00:00 · **Legacy report time:** 2026-11-20T00:41:35.629157+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 500.97 | 70.82 | -0.20% | 6.49x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 2 | XLM/USD | 0.133235 | 50.63 | -0.13% | 0.48x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 3 | MEGA/USD | 0.05959 | 42.18 | +2.02% | 0.31x | MODERATE 46/100 | VERY_HIGH 81/100 | Watch |
| 4 | ICNT/USD | 0.4275 | 37.22 | -0.19% | 1.89x | WEAK 29/100 | VERY_HIGH 73/100 | Do nothing |
| 5 | USELESS/USD | 0.0995 | 26.30 | -0.30% | 0.58x | WEAK 8/100 | EXTREME 88/100 | Do nothing |
| 6 | RARE/USD | 0.01336 | 23.93 | +1.37% | 0.57x | WEAK 32/100 | EXTREME 94/100 | Do nothing |
| 7 | STRK/USD | 0.03177 | 21.10 | -0.84% | 0.43x | WEAK 11/100 | EXTREME 87/100 | Do nothing |
| 8 | BLESS/USD | 0.012286 | 8.22 | -1.71% | 0.61x | WEAK 0/100 | EXTREME 97/100 | Do nothing |

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
