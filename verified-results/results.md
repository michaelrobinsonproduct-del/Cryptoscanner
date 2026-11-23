# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T13:52:01.209324+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45187758864
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 65019d53bf9fc68a936b95f8ae8348b25272c8f9 (atomic ledger/results publication)
**Ledger generation:** 1438 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 155.52 | 91.344 | 87.514 | +8.42% | -0.87% | 1.82x | 12.9 | 2026-11-23T13:51:53.196070+00:00 | Not calibrated | MODERATE 61/100 | HIGH 67/100 | Watch | WATCH |
| 2 | ALGO/USD | 0.08414 | 91.219 | 77.524 | +11.55% | -0.26% | 2.79x | 8.3 | 2026-11-23T13:51:53.196070+00:00 | Not calibrated | STRONG 76/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SOL/USD | 72.37 | 73.792 | 71.554 | +2.46% | +0.10% | 1.18x | 1.4 | 2026-11-23T13:51:53.196070+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 4 | NEAR/USD | 2.9892 | 68.719 | 54.919 | +0.25% | -0.24% | 2.51x | 3.7 | 2026-11-23T13:51:53.196070+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 5 | HYPE/USD | 63.82 | 64.709 | 62.652 | +1.21% | -0.05% | 1.23x | 1.6 | 2026-11-23T13:51:53.196070+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XRP/USD | 0.93916 | 64.653 | 63.716 | +1.25% | -0.02% | 1.11x | 0.1 | 2026-11-23T13:51:53.196070+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 7 | LTC/USD | 40.73 | 64.066 | 51.144 | +1.42% | -0.42% | 3.26x | 2.5 | 2026-11-23T13:51:53.196070+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6672 | 58.643 | 66.527 | +1.75% | -0.13% | 0.28x | 1.5 | 2026-11-23T13:51:53.196070+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | CCD/USD | 0.002901 | 55.615 | 60.400 | +9.06% | -0.14% | 0.59x | 31.1 | 2026-11-23T13:51:53.196070+00:00 | Not calibrated | WEAK 23/100 | EXTREME 100/100 | Do nothing | WATCH |
| 10 | GRT/USD | 0.01693 | 55.394 | 60.086 | +5.88% | +0.12% | 0.47x | 23.7 | 2026-11-23T13:51:53.196070+00:00 | Not calibrated | WEAK 38/100 | EXTREME 94/100 | Do nothing | WATCH |
| 11 | XDG/USD | 0.0554849 | 52.081 | 47.601 | +0.36% | -0.15% | 1.52x | 0.8 | 2026-11-23T13:51:53.196070+00:00 | Not calibrated | MODERATE 46/100 | HIGH 61/100 | Watch | WATCH |
| 12 | XLM/USD | 0.127964 | 50.995 | 51.849 | +0.34% | -0.14% | 0.99x | 4.5 | 2026-11-23T13:51:53.196070+00:00 | Not calibrated | WEAK 30/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 87.514 | 155.52 | -0.87% | 1.82x |
| 2 | ALGO/USD | 77.524 | 0.08414 | -0.26% | 2.79x |
| 3 | SOL/USD | 71.554 | 72.37 | +0.10% | 1.18x |
| 4 | SUI/USD | 66.527 | 0.6672 | -0.13% | 0.28x |
| 5 | XRP/USD | 63.716 | 0.93916 | -0.02% | 1.11x |
| 6 | HYPE/USD | 62.652 | 63.82 | -0.05% | 1.23x |
| 7 | CCD/USD | 60.400 | 0.002901 | -0.14% | 0.59x |
| 8 | GRT/USD | 60.086 | 0.01693 | +0.12% | 0.47x |
| 9 | NEAR/USD | 54.919 | 2.9892 | -0.24% | 2.51x |
| 10 | XLM/USD | 51.849 | 0.127964 | -0.14% | 0.99x |
| 11 | LTC/USD | 51.144 | 40.73 | -0.42% | 3.26x |
| 12 | XDG/USD | 47.601 | 0.0554849 | -0.15% | 1.52x |

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

- Persisted scans: 1438; predictions: 12023; observations: 870844.
- Matured sampled outcomes across 1/6/24/48h: 20333; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45187758864 · **Generation:** 1438 · **Legacy run:** 45187758864
**Main quote time:** 2026-11-23T13:52:01.209324+00:00 · **Legacy report time:** 2026-11-23T13:53:02.718753+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 155.52 | 91.34 | -0.87% | 1.82x | MODERATE 61/100 | HIGH 67/100 | Watch |
| 2 | ALGO/USD | 0.08414 | 91.22 | -0.26% | 2.79x | STRONG 76/100 | HIGH 61/100 | Watch |
| 3 | SOL/USD ⭐ | 72.37 | 73.79 | +0.10% | 1.18x | STRONG 72/100 | HIGH 62/100 | Watch |
| 4 | NEAR/USD | 2.9892 | 68.72 | -0.24% | 2.51x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 5 | HYPE/USD | 63.82 | 64.71 | -0.05% | 1.23x | WEAK 42/100 | HIGH 68/100 | Watch |
| 6 | XRP/USD | 0.93916 | 64.65 | -0.02% | 1.11x | WEAK 42/100 | HIGH 68/100 | Watch |
| 7 | LTC/USD | 40.73 | 64.07 | -0.42% | 3.26x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 8 | SUI/USD | 0.6672 | 58.64 | -0.13% | 0.28x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | CCD/USD | 0.002901 | 55.61 | -0.14% | 0.59x | WEAK 23/100 | EXTREME 100/100 | Do nothing |
| 10 | GRT/USD | 0.01693 | 55.39 | +0.12% | 0.47x | WEAK 38/100 | EXTREME 94/100 | Do nothing |
| 11 | XDG/USD | 0.0554849 | 52.08 | -0.15% | 1.52x | MODERATE 46/100 | HIGH 61/100 | Watch |
| 12 | XLM/USD | 0.127964 | 50.99 | -0.14% | 0.99x | WEAK 30/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 72.31 | 78.77 | +0.10% | 1.18x | 29469 | STRONG 74/100 | HIGH 62/100 | Watch |

**Same-run overlap:** SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
