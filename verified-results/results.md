# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T08:00:42.623909+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44699020981
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 97aa431d112701372a565aaf50cf7db094a4acd7 (atomic ledger/results publication)
**Ledger generation:** 951 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XLM/USD | 0.13401 | 66.658 | 59.485 | +0.99% | -0.27% | 1.85x | 4.9 | 2026-11-20T08:00:36.186172+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 2 | STRK/USD | 0.03212 | 54.917 | 37.563 | +1.36% | +0.47% | 5.26x | 12.4 | 2026-11-20T08:00:36.186172+00:00 | Not calibrated | STRONG 77/100 | HIGH 66/100 | Watch | WATCH |
| 3 | XRP/USD | 0.96454 | 51.687 | 58.809 | +0.55% | +0.02% | 0.28x | 0.1 | 2026-11-20T08:00:36.186172+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | SYRUP/USD | 0.09905 | 43.883 | 45.050 | +2.93% | -0.30% | 1.03x | 15.1 | 2026-11-20T08:00:36.186172+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 5 | ENA/USD | 0.1057 | 41.242 | 48.006 | +0.86% | +0.29% | 0.18x | 9.5 | 2026-11-20T08:00:36.186172+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | SKR/USD | 0.010328 | 40.923 | 45.075 | +2.81% | -0.60% | 0.88x | 11.6 | 2026-11-20T08:00:36.186172+00:00 | Not calibrated | WEAK 20/100 | EXTREME 86/100 | Do nothing | WATCH |
| 7 | AUD/USD | 0.66741 | 37.949 | 40.622 | +0.29% | -0.01% | 0.74x | 0.6 | 2026-11-20T08:00:36.186172+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | ATOM/USD | 1.2668 | 31.027 | 33.523 | +0.42% | -0.17% | 0.84x | 3.9 | 2026-11-20T08:00:36.186172+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 73/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XLM/USD | 59.485 | 0.13401 | -0.27% | 1.85x |
| 2 | XRP/USD | 58.809 | 0.96454 | +0.02% | 0.28x |
| 3 | ENA/USD | 48.006 | 0.1057 | +0.29% | 0.18x |
| 4 | SKR/USD | 45.075 | 0.010328 | -0.60% | 0.88x |
| 5 | SYRUP/USD | 45.050 | 0.09905 | -0.30% | 1.03x |
| 6 | AUD/USD | 40.622 | 0.66741 | -0.01% | 0.74x |
| 7 | STRK/USD | 37.563 | 0.03212 | +0.47% | 5.26x |
| 8 | ATOM/USD | 33.523 | 1.2668 | -0.17% | 0.84x |

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

- Persisted scans: 951; predictions: 8075; observations: 574626.
- Matured sampled outcomes across 1/6/24/48h: 9543; gap abstentions: 17453. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44699020981 · **Generation:** 951 · **Legacy run:** 44699020981
**Main quote time:** 2026-11-20T08:00:42.623909+00:00 · **Legacy report time:** 2026-11-20T08:01:29.827169+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD | 0.13401 | 66.66 | -0.27% | 1.85x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 2 | STRK/USD ⭐ | 0.03212 | 54.92 | +0.47% | 5.26x | STRONG 87/100 | HIGH 66/100 | Consider small entry |
| 3 | XRP/USD | 0.96454 | 51.69 | +0.02% | 0.28x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 4 | SYRUP/USD | 0.09905 | 43.88 | -0.30% | 1.03x | WEAK 27/100 | VERY_HIGH 79/100 | Do nothing |
| 5 | ENA/USD | 0.1057 | 41.24 | +0.29% | 0.18x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 6 | SKR/USD | 0.010328 | 40.92 | -0.60% | 0.88x | WEAK 20/100 | EXTREME 86/100 | Do nothing |
| 7 | AUD/USD | 0.66741 | 37.95 | -0.01% | 0.74x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | ATOM/USD | 1.2668 | 31.03 | -0.17% | 0.84x | WEAK 21/100 | VERY_HIGH 73/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | STRK/USD ⭐ | 0.03221 | 53.67 | +0.47% | 5.26x | 3337 | STRONG 92/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** STRK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
