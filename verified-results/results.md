# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T15:05:23.450673+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44550689043
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 577c5d2b92f1b4881841dab59158f5a3e2b0dac7 (atomic ledger/results publication)
**Ledger generation:** 797 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 23.449 | 106.338 | 96.362 | +8.20% | -1.00% | 4.28x | 7.3 | 2026-11-19T15:05:15.638103+00:00 | Not calibrated | STRONG 80/100 | HIGH 65/100 | Watch | WATCH |
| 2 | HYPE/USD | 69.36 | 94.660 | 80.236 | +3.71% | -0.12% | 3.06x | 1.4 | 2026-11-19T15:05:15.638103+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SENT/USD | 0.021954 | 88.563 | 78.256 | +6.55% | -0.94% | 6.01x | 0.9 | 2026-11-19T15:05:15.638103+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 4 | ZEC/USD | 943.27 | 88.263 | 75.695 | +3.43% | -0.49% | 7.01x | 6.7 | 2026-11-19T15:05:15.638103+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 5 | INJ/USD | 7.279 | 84.448 | 70.829 | +4.27% | +0.14% | 2.29x | 4.1 | 2026-11-19T15:05:15.638103+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 6 | TAO/USD | 197.9592 | 80.873 | 72.843 | +3.13% | -0.40% | 2.00x | 8.1 | 2026-11-19T15:05:15.638103+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ETH/USD | 1808.47 | 74.367 | 67.522 | +1.90% | +0.15% | 1.61x | 1.5 | 2026-11-19T15:05:15.638103+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XRP/USD | 0.99091 | 70.837 | 72.019 | +2.54% | -0.16% | 0.96x | 1.5 | 2026-11-19T15:05:15.638103+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 9 | ADA/USD | 0.155117 | 70.470 | 71.588 | +2.55% | -0.07% | 0.92x | 2.6 | 2026-11-19T15:05:15.638103+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 10 | PUMP/USD | 0.002755 | 68.079 | 78.628 | +6.12% | -0.33% | 0.11x | 14.5 | 2026-11-19T15:05:15.638103+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 11 | LIGHTER/USD | 2.975 | 67.421 | 74.109 | +9.62% | -0.34% | 0.50x | 13.5 | 2026-11-19T15:05:15.638103+00:00 | Not calibrated | WEAK 34/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | XBT/USD | 63771.1 | 67.339 | 63.734 | +1.25% | -0.19% | 1.46x | 0.0 | 2026-11-19T15:05:15.638103+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 96.362 | 23.449 | -1.00% | 4.28x |
| 2 | HYPE/USD | 80.236 | 69.36 | -0.12% | 3.06x |
| 3 | PUMP/USD | 78.628 | 0.002755 | -0.33% | 0.11x |
| 4 | SENT/USD | 78.256 | 0.021954 | -0.94% | 6.01x |
| 5 | ZEC/USD | 75.695 | 943.27 | -0.49% | 7.01x |
| 6 | LIGHTER/USD | 74.109 | 2.975 | -0.34% | 0.50x |
| 7 | TAO/USD | 72.843 | 197.9592 | -0.40% | 2.00x |
| 8 | XRP/USD | 72.019 | 0.99091 | -0.16% | 0.96x |
| 9 | ADA/USD | 71.588 | 0.155117 | -0.07% | 0.92x |
| 10 | INJ/USD | 70.829 | 7.279 | +0.14% | 2.29x |
| 11 | ETH/USD | 67.522 | 1808.47 | +0.15% | 1.61x |
| 12 | XBT/USD | 63.734 | 63771.1 | -0.19% | 1.46x |

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

- Persisted scans: 797; predictions: 6708; observations: 482048.
- Matured sampled outcomes across 1/6/24/48h: 6719; gap abstentions: 15164. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44550689043 · **Generation:** 797 · **Legacy run:** 44550689043
**Main quote time:** 2026-11-19T15:05:23.450673+00:00 · **Legacy report time:** 2026-11-19T15:06:14.282806+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 23.449 | 106.34 | -1.00% | 4.28x | STRONG 80/100 | HIGH 65/100 | Watch |
| 2 | HYPE/USD | 69.36 | 94.66 | -0.12% | 3.06x | STRONG 77/100 | HIGH 61/100 | Watch |
| 3 | SENT/USD | 0.021954 | 88.56 | -0.94% | 6.01x | STRONG 74/100 | HIGH 66/100 | Watch |
| 4 | ZEC/USD | 943.27 | 88.26 | -0.49% | 7.01x | STRONG 74/100 | HIGH 61/100 | Watch |
| 5 | INJ/USD ⭐ | 7.279 | 84.45 | +0.14% | 2.29x | STRONG 97/100 | HIGH 55/100 | Watch |
| 6 | TAO/USD | 197.9592 | 80.87 | -0.40% | 2.00x | STRONG 70/100 | HIGH 61/100 | Watch |
| 7 | ETH/USD | 1808.47 | 74.37 | +0.15% | 1.61x | STRONG 72/100 | HIGH 55/100 | Watch |
| 8 | XRP/USD | 0.99091 | 70.84 | -0.16% | 0.96x | WEAK 40/100 | HIGH 68/100 | Watch |
| 9 | ADA/USD | 0.155117 | 70.47 | -0.07% | 0.92x | WEAK 40/100 | HIGH 68/100 | Watch |
| 10 | PUMP/USD | 0.002755 | 68.08 | -0.33% | 0.11x | WEAK 34/100 | VERY_HIGH 82/100 | Do nothing |
| 11 | LIGHTER/USD | 2.975 | 67.42 | -0.34% | 0.50x | WEAK 34/100 | EXTREME 87/100 | Do nothing |
| 12 | XBT/USD | 63771.1 | 67.34 | -0.19% | 1.46x | MODERATE 54/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 7.279 | 87.35 | +0.14% | 2.29x | 6516 | STRONG 99/100 | HIGH 55/100 | Watch |

**Same-run overlap:** INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
