# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T07:00:41.918686+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44691676903
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 1adfc1b9d22a73ca9afbfe6cae2d74c26faa0b6b (atomic ledger/results publication)
**Ledger generation:** 945 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.4497 | 87.122 | 72.665 | +5.54% | +1.86% | 1.51x | 8.9 | 2026-11-20T07:00:35.556932+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XRP/USD | 0.97138 | 60.346 | 63.800 | +1.26% | +0.69% | 0.31x | 0.1 | 2026-11-20T07:00:35.556932+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | XLM/USD | 0.134381 | 59.626 | 62.751 | +1.27% | +0.50% | 0.44x | 2.2 | 2026-11-20T07:00:35.556932+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | AUD/USD | 0.66797 | 56.900 | 41.570 | +0.37% | +0.07% | 4.07x | 0.1 | 2026-11-20T07:00:35.556932+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SYRUP/USD | 0.10023 | 55.096 | 54.202 | +4.16% | +0.51% | 0.83x | 14.0 | 2026-11-20T07:00:35.556932+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | PIEVERSE/USD | 3.0322 | 43.175 | 30.726 | +1.58% | +0.62% | 1.93x | 34.0 | 2026-11-20T07:00:35.556932+00:00 | Not calibrated | MODERATE 57/100 | HIGH 67/100 | Watch | WATCH |
| 7 | HBAR/USD | 0.05411 | 39.023 | 43.114 | +0.65% | +0.37% | 0.41x | 3.7 | 2026-11-20T07:00:35.556932+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SKR/USD | 0.010203 | 35.330 | 37.703 | +1.56% | -0.31% | 0.92x | 8.8 | 2026-11-20T07:00:35.556932+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 9 | ATOM/USD | 1.2691 | 28.081 | 32.825 | +0.60% | +0.59% | 0.23x | 7.9 | 2026-11-20T07:00:35.556932+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 72.665 | 0.4497 | +1.86% | 1.51x |
| 2 | XRP/USD | 63.800 | 0.97138 | +0.69% | 0.31x |
| 3 | XLM/USD | 62.751 | 0.134381 | +0.50% | 0.44x |
| 4 | SYRUP/USD | 54.202 | 0.10023 | +0.51% | 0.83x |
| 5 | HBAR/USD | 43.114 | 0.05411 | +0.37% | 0.41x |
| 6 | AUD/USD | 41.570 | 0.66797 | +0.07% | 4.07x |
| 7 | SKR/USD | 37.703 | 0.010203 | -0.31% | 0.92x |
| 8 | ATOM/USD | 32.825 | 1.2691 | +0.59% | 0.23x |
| 9 | PIEVERSE/USD | 30.726 | 3.0322 | +0.62% | 1.93x |

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

- Persisted scans: 945; predictions: 8021; observations: 570996.
- Matured sampled outcomes across 1/6/24/48h: 9410; gap abstentions: 17333. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44691676903 · **Generation:** 945 · **Legacy run:** 44691676903
**Main quote time:** 2026-11-20T07:00:41.918686+00:00 · **Legacy report time:** 2026-11-20T07:01:48.029717+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.4497 | 87.12 | +1.86% | 1.51x | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD | 0.97138 | 60.35 | +0.69% | 0.31x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 3 | XLM/USD | 0.134381 | 59.63 | +0.50% | 0.44x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 4 | AUD/USD ⭐ | 0.66797 | 56.90 | +0.07% | 4.07x | STRONG 83/100 | HIGH 55/100 | Watch |
| 5 | SYRUP/USD | 0.10023 | 55.10 | +0.51% | 0.83x | MODERATE 53/100 | VERY_HIGH 73/100 | Watch |
| 6 | PIEVERSE/USD ⭐ | 3.0322 | 43.18 | +0.62% | 1.93x | MODERATE 67/100 | HIGH 67/100 | Watch |
| 7 | HBAR/USD | 0.05411 | 39.02 | +0.37% | 0.41x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 8 | SKR/USD | 0.010203 | 35.33 | -0.31% | 0.92x | WEAK 23/100 | VERY_HIGH 80/100 | Do nothing |
| 9 | ATOM/USD | 1.2691 | 28.08 | +0.59% | 0.23x | WEAK 44/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.45 | 82.66 | +1.86% | 1.51x | 7708 | STRONG 86/100 | HIGH 67/100 | Consider small entry |
| 2 | PIEVERSE/USD ⭐ | 3.0565 | 60.35 | +0.62% | 1.93x | 3426 | STRONG 75/100 | HIGH 67/100 | Consider small entry |
| 3 | AUD/USD ⭐ | 0.66797 | 54.19 | +0.07% | 4.07x | 3954 | STRONG 82/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ICNT/USD, AUD/USD, PIEVERSE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
