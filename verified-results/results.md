# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T07:10:42.166664+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44692892986
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 3c844d69448de74367f936dba794798d5f3eeebe (atomic ledger/results publication)
**Ledger generation:** 946 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.4549 | 78.668 | 69.114 | +6.76% | -0.31% | 2.11x | 28.7 | 2026-11-20T07:10:34.790171+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | XLM/USD | 0.13378 | 56.910 | 60.660 | +0.81% | -0.30% | 0.77x | 0.1 | 2026-11-20T07:10:34.790171+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 3 | XRP/USD | 0.96689 | 52.503 | 60.213 | +0.80% | -0.27% | 0.36x | 0.7 | 2026-11-20T07:10:34.790171+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | SYRUP/USD | 0.09973 | 49.078 | 51.527 | +3.64% | -0.65% | 1.08x | 12.1 | 2026-11-20T07:10:34.790171+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 5 | PIEVERSE/USD | 2.9946 | 45.480 | 28.789 | +0.32% | +0.34% | 8.36x | 20.0 | 2026-11-20T07:10:34.790171+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | YB/USD | 0.0541 | 41.452 | 49.622 | +5.79% | -0.57% | 0.47x | 44.5 | 2026-11-20T07:10:34.790171+00:00 | Not calibrated | WEAK 11/100 | EXTREME 100/100 | Do nothing | WATCH |
| 7 | AUD/USD | 0.66768 | 39.611 | 41.048 | +0.33% | -0.00% | 0.86x | 0.4 | 2026-11-20T07:10:34.790171+00:00 | Not calibrated | WEAK 25/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | HBAR/USD | 0.05394 | 33.969 | 40.857 | +0.33% | -0.22% | 0.42x | 3.7 | 2026-11-20T07:10:34.790171+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | SKR/USD | 0.010201 | 33.638 | 37.089 | +1.54% | -0.32% | 0.82x | 9.8 | 2026-11-20T07:10:34.790171+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 10 | ATOM/USD | 1.265 | 26.305 | 31.340 | +0.28% | -0.13% | 0.56x | 6.3 | 2026-11-20T07:10:34.790171+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 69.114 | 0.4549 | -0.31% | 2.11x |
| 2 | XLM/USD | 60.660 | 0.13378 | -0.30% | 0.77x |
| 3 | XRP/USD | 60.213 | 0.96689 | -0.27% | 0.36x |
| 4 | SYRUP/USD | 51.527 | 0.09973 | -0.65% | 1.08x |
| 5 | YB/USD | 49.622 | 0.0541 | -0.57% | 0.47x |
| 6 | AUD/USD | 41.048 | 0.66768 | -0.00% | 0.86x |
| 7 | HBAR/USD | 40.857 | 0.05394 | -0.22% | 0.42x |
| 8 | SKR/USD | 37.089 | 0.010201 | -0.32% | 0.82x |
| 9 | ATOM/USD | 31.340 | 1.265 | -0.13% | 0.56x |
| 10 | PIEVERSE/USD | 28.789 | 2.9946 | +0.34% | 8.36x |

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

- Persisted scans: 946; predictions: 8031; observations: 571601.
- Matured sampled outcomes across 1/6/24/48h: 9439; gap abstentions: 17373. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44692892986 · **Generation:** 946 · **Legacy run:** 44692892986
**Main quote time:** 2026-11-20T07:10:42.166664+00:00 · **Legacy report time:** 2026-11-20T07:11:48.853443+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD | 0.4549 | 78.67 | -0.31% | 2.11x | MODERATE 59/100 | VERY_HIGH 73/100 | Watch |
| 2 | XLM/USD | 0.13378 | 56.91 | -0.30% | 0.77x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 3 | XRP/USD | 0.96689 | 52.50 | -0.27% | 0.36x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | SYRUP/USD | 0.09973 | 49.08 | -0.65% | 1.08x | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing |
| 5 | PIEVERSE/USD ⭐ | 2.9946 | 45.48 | +0.34% | 8.36x | STRONG 78/100 | VERY_HIGH 72/100 | Watch |
| 6 | YB/USD | 0.0541 | 41.45 | -0.57% | 0.47x | WEAK 11/100 | EXTREME 100/100 | Do nothing |
| 7 | AUD/USD | 0.66768 | 39.61 | -0.00% | 0.86x | WEAK 25/100 | HIGH 68/100 | Do nothing |
| 8 | HBAR/USD | 0.05394 | 33.97 | -0.22% | 0.42x | WEAK 22/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | SKR/USD | 0.010201 | 33.64 | -0.32% | 0.82x | WEAK 22/100 | VERY_HIGH 80/100 | Do nothing |
| 10 | ATOM/USD | 1.265 | 26.30 | -0.13% | 0.56x | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD ⭐ | 2.9952 | 38.99 | +0.34% | 8.36x | 3408 | STRONG 74/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** PIEVERSE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
