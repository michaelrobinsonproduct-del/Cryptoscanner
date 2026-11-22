# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T08:11:08.065432+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45001483661
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 59bb6d10ab5b5cb754a59bfb579521c6bfc272a8 (atomic ledger/results publication)
**Ledger generation:** 1255 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.281 | 78.320 | 60.763 | +1.53% | +0.51% | 3.00x | 9.9 | 2026-11-22T08:11:00.389701+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | TAO/USD | 187.5494 | 68.561 | 58.296 | +0.98% | +0.27% | 1.89x | 7.1 | 2026-11-22T08:11:00.389701+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ZEC/USD | 786.81 | 54.451 | 60.672 | +1.11% | -0.03% | 0.39x | 4.2 | 2026-11-22T08:11:00.389701+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | ZBCN/USD | 0.001833 | 54.448 | 58.845 | +6.14% | +0.11% | 0.51x | 32.8 | 2026-11-22T08:11:00.389701+00:00 | Not calibrated | WEAK 37/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | INJ/USD | 6.006 | 46.685 | 38.525 | +0.55% | +0.93% | 1.35x | 10.0 | 2026-11-22T08:11:00.389701+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.04476 | 43.599 | 49.683 | +1.08% | +0.36% | 0.21x | 4.5 | 2026-11-22T08:11:00.389701+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | PEARL/USD | 1.9846 | 43.469 | 39.378 | +1.86% | +0.69% | 1.06x | 31.3 | 2026-11-22T08:11:00.389701+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 8 | ORCA/USD | 1.23 | 35.022 | 36.817 | +2.41% | -1.20% | 1.42x | 24.4 | 2026-11-22T08:11:00.389701+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 9 | TRUMP/USD | 0.889 | 30.271 | 25.048 | +0.34% | +0.57% | 1.24x | 22.5 | 2026-11-22T08:11:00.389701+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 79/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 60.763 | 25.281 | +0.51% | 3.00x |
| 2 | ZEC/USD | 60.672 | 786.81 | -0.03% | 0.39x |
| 3 | ZBCN/USD | 58.845 | 0.001833 | +0.11% | 0.51x |
| 4 | TAO/USD | 58.296 | 187.5494 | +0.27% | 1.89x |
| 5 | NIGHT/USD | 49.683 | 0.04476 | +0.36% | 0.21x |
| 6 | PEARL/USD | 39.378 | 1.9846 | +0.69% | 1.06x |
| 7 | INJ/USD | 38.525 | 6.006 | +0.93% | 1.35x |
| 8 | ORCA/USD | 36.817 | 1.23 | -1.20% | 1.42x |
| 9 | TRUMP/USD | 25.048 | 0.889 | +0.57% | 1.24x |

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

- Persisted scans: 1255; predictions: 9990; observations: 759405.
- Matured sampled outcomes across 1/6/24/48h: 14380; gap abstentions: 22086. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 59 (sampled only; not a success-rate estimate).
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

**Writer:** 45001483661 · **Generation:** 1255 · **Legacy run:** 45001483661
**Main quote time:** 2026-11-22T08:11:08.065432+00:00 · **Legacy report time:** 2026-11-22T08:12:00.321113+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.281 | 78.32 | +0.51% | 3.00x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | TAO/USD ⭐ | 187.5494 | 68.56 | +0.27% | 1.89x | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 3 | ZEC/USD | 786.81 | 54.45 | -0.03% | 0.39x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | ZBCN/USD | 0.001833 | 54.45 | +0.11% | 0.51x | WEAK 37/100 | EXTREME 87/100 | Do nothing |
| 5 | INJ/USD ⭐ | 6.006 | 46.69 | +0.93% | 1.35x | STRONG 78/100 | HIGH 55/100 | Watch |
| 6 | NIGHT/USD | 0.04476 | 43.60 | +0.36% | 0.21x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 7 | PEARL/USD | 1.9846 | 43.47 | +0.69% | 1.06x | MODERATE 47/100 | VERY_HIGH 74/100 | Watch |
| 8 | ORCA/USD | 1.23 | 35.02 | -1.20% | 1.42x | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing |
| 9 | TRUMP/USD ⭐ | 0.889 | 30.27 | +0.57% | 1.24x | MODERATE 50/100 | VERY_HIGH 79/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.285 | 75.34 | +0.51% | 3.00x | 13651 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | TAO/USD ⭐ | 187.2535 | 53.99 | +0.27% | 1.89x | 7090 | STRONG 82/100 | HIGH 55/100 | Consider small entry |
| 3 | INJ/USD ⭐ | 6.009 | 39.22 | +0.93% | 1.35x | 5919 | MODERATE 65/100 | HIGH 67/100 | Watch |
| 4 | TRUMP/USD ⭐ | 0.889 | 31.08 | +0.57% | 1.24x | 2925 | MODERATE 56/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** VVV/USD, TAO/USD, INJ/USD, TRUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
