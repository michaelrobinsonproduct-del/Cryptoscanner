# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T06:55:31.043324+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44691117759
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 8a9ce02fd7845eaec5e4acb630e181f57ea8ed0e (atomic ledger/results publication)
**Ledger generation:** 944 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.4528 | 84.318 | 66.793 | +6.27% | +2.61% | 1.45x | 30.9 | 2026-11-20T06:55:25.219044+00:00 | Not calibrated | STRONG 77/100 | HIGH 67/100 | Watch | WATCH |
| 2 | PROS/USD | 0.5866 | 69.537 | 63.071 | +8.89% | +0.17% | 1.56x | 25.6 | 2026-11-20T06:55:25.219044+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 3 | XLM/USD | 0.134438 | 63.997 | 64.019 | +1.31% | +0.54% | 0.73x | 0.3 | 2026-11-20T06:55:25.219044+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | XRP/USD | 0.96994 | 57.640 | 62.543 | +1.11% | +0.58% | 0.22x | 0.5 | 2026-11-20T06:55:25.219044+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | AUD/USD | 0.66772 | 56.242 | 40.987 | +0.34% | +0.05% | 5.31x | 0.9 | 2026-11-20T06:55:25.219044+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 6 | SYRUP/USD | 0.10038 | 55.985 | 54.320 | +4.31% | +0.82% | 0.75x | 16.0 | 2026-11-20T06:55:25.219044+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | SKR/USD | 0.010234 | 38.566 | 38.883 | +1.87% | +0.05% | 0.94x | 10.8 | 2026-11-20T06:55:25.219044+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 8 | HBAR/USD | 0.05405 | 37.042 | 42.341 | +0.54% | +0.54% | 0.20x | 3.7 | 2026-11-20T06:55:25.219044+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ATOM/USD | 1.2665 | 26.020 | 32.162 | +0.40% | +0.43% | 0.17x | 6.3 | 2026-11-20T06:55:25.219044+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 66.793 | 0.4528 | +2.61% | 1.45x |
| 2 | XLM/USD | 64.019 | 0.134438 | +0.54% | 0.73x |
| 3 | PROS/USD | 63.071 | 0.5866 | +0.17% | 1.56x |
| 4 | XRP/USD | 62.543 | 0.96994 | +0.58% | 0.22x |
| 5 | SYRUP/USD | 54.320 | 0.10038 | +0.82% | 0.75x |
| 6 | HBAR/USD | 42.341 | 0.05405 | +0.54% | 0.20x |
| 7 | AUD/USD | 40.987 | 0.66772 | +0.05% | 5.31x |
| 8 | SKR/USD | 38.883 | 0.010234 | +0.05% | 0.94x |
| 9 | ATOM/USD | 32.162 | 1.2665 | +0.43% | 0.17x |

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

- Persisted scans: 944; predictions: 8012; observations: 570391.
- Matured sampled outcomes across 1/6/24/48h: 9398; gap abstentions: 17313. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44691117759 · **Generation:** 944 · **Legacy run:** 44691117759
**Main quote time:** 2026-11-20T06:55:31.043324+00:00 · **Legacy report time:** 2026-11-20T06:56:12.353403+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.4528 | 84.32 | +2.61% | 1.45x | STRONG 87/100 | HIGH 67/100 | Watch |
| 2 | PROS/USD ⭐ | 0.5866 | 69.54 | +0.17% | 1.56x | STRONG 70/100 | VERY_HIGH 79/100 | Watch |
| 3 | XLM/USD | 0.134438 | 64.00 | +0.54% | 0.73x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 4 | XRP/USD | 0.96994 | 57.64 | +0.58% | 0.22x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 5 | AUD/USD ⭐ | 0.66772 | 56.24 | +0.05% | 5.31x | STRONG 83/100 | HIGH 55/100 | Watch |
| 6 | SYRUP/USD | 0.10038 | 55.98 | +0.82% | 0.75x | MODERATE 53/100 | VERY_HIGH 73/100 | Watch |
| 7 | SKR/USD | 0.010234 | 38.57 | +0.05% | 0.94x | WEAK 34/100 | VERY_HIGH 80/100 | Do nothing |
| 8 | HBAR/USD | 0.05405 | 37.04 | +0.54% | 0.20x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 9 | ATOM/USD | 1.2665 | 26.02 | +0.43% | 0.17x | WEAK 43/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.4526 | 84.66 | +2.61% | 1.45x | 7713 | STRONG 92/100 | HIGH 61/100 | Watch |
| 2 | PROS/USD ⭐ | 0.5866 | 59.96 | +0.17% | 1.56x | 1041 | MODERATE 65/100 | VERY_HIGH 79/100 | Watch |
| 3 | AUD/USD ⭐ | 0.66789 | 53.74 | +0.05% | 5.31x | 3972 | STRONG 82/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ICNT/USD, PROS/USD, AUD/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
