# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T08:31:41.429053+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45139040049
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 56322ad231cfc63dc15c8a52c9737c66f2872c1f (atomic ledger/results publication)
**Ledger generation:** 1405 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SOL/USD | 72.29 | 75.322 | 70.760 | +2.35% | +0.21% | 1.35x | 1.4 | 2026-11-23T08:31:32.837494+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0022 | 73.180 | 58.147 | +0.69% | +0.01% | 4.90x | 3.3 | 2026-11-23T08:31:32.837494+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 3 | JUP/USD | 0.24412 | 71.564 | 74.146 | +8.71% | +0.40% | 0.54x | 11.5 | 2026-11-23T08:31:32.837494+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0555455 | 66.851 | 51.735 | +0.47% | +0.02% | 18.47x | 0.0 | 2026-11-23T08:31:32.837494+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.05013 | 64.045 | 60.802 | +1.95% | +0.58% | 1.03x | 8.0 | 2026-11-23T08:31:32.837494+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XRP/USD | 0.93753 | 63.005 | 62.486 | +1.08% | +0.11% | 1.00x | 0.1 | 2026-11-23T08:31:32.837494+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 7 | GBP/USD | 1.31245 | 59.523 | 56.644 | +0.26% | +0.01% | 1.28x | 0.4 | 2026-11-23T08:31:32.837494+00:00 | Not calibrated | MODERATE 55/100 | HIGH 55/100 | Watch | WATCH |
| 8 | AUD/USD | 0.66468 | 57.657 | 43.290 | +0.47% | -0.01% | 2.44x | 0.6 | 2026-11-23T08:31:32.837494+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 9 | HYPE/USD | 63.23 | 56.989 | 56.097 | +0.27% | +0.03% | 1.07x | 1.6 | 2026-11-23T08:31:32.837494+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6648 | 56.754 | 63.963 | +1.39% | -0.09% | 0.32x | 1.5 | 2026-11-23T08:31:32.837494+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XLM/USD | 0.128532 | 56.713 | 59.340 | +0.79% | +0.03% | 0.72x | 1.6 | 2026-11-23T08:31:32.837494+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ALGO/USD | 0.07849 | 53.521 | 58.513 | +4.06% | +0.44% | 0.28x | 7.6 | 2026-11-23T08:31:32.837494+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | JUP/USD | 74.146 | 0.24412 | +0.40% | 0.54x |
| 2 | SOL/USD | 70.760 | 72.29 | +0.21% | 1.35x |
| 3 | SUI/USD | 63.963 | 0.6648 | -0.09% | 0.32x |
| 4 | XRP/USD | 62.486 | 0.93753 | +0.11% | 1.00x |
| 5 | NIGHT/USD | 60.802 | 0.05013 | +0.58% | 1.03x |
| 6 | XLM/USD | 59.340 | 0.128532 | +0.03% | 0.72x |
| 7 | ALGO/USD | 58.513 | 0.07849 | +0.44% | 0.28x |
| 8 | NEAR/USD | 58.147 | 3.0022 | +0.01% | 4.90x |
| 9 | GBP/USD | 56.644 | 1.31245 | +0.01% | 1.28x |
| 10 | HYPE/USD | 56.097 | 63.23 | +0.03% | 1.07x |
| 11 | XDG/USD | 51.735 | 0.0555455 | +0.02% | 18.47x |
| 12 | AUD/USD | 43.290 | 0.66468 | -0.01% | 2.44x |

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

- Persisted scans: 1405; predictions: 11627; observations: 850748.
- Matured sampled outcomes across 1/6/24/48h: 18976; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 129 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45139040049 · **Generation:** 1405 · **Legacy run:** 45139040049
**Main quote time:** 2026-11-23T08:31:41.429053+00:00 · **Legacy report time:** 2026-11-23T08:32:51.691878+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 72.29 | 75.32 | +0.21% | 1.35x | STRONG 93/100 | HIGH 55/100 | Watch |
| 2 | NEAR/USD | 3.0022 | 73.18 | +0.01% | 4.90x | STRONG 82/100 | HIGH 55/100 | Watch |
| 3 | JUP/USD | 0.24412 | 71.56 | +0.40% | 0.54x | MODERATE 61/100 | VERY_HIGH 81/100 | Watch |
| 4 | XDG/USD | 0.0555455 | 66.85 | +0.02% | 18.47x | STRONG 78/100 | HIGH 55/100 | Watch |
| 5 | NIGHT/USD ⭐ | 0.05013 | 64.04 | +0.58% | 1.03x | STRONG 77/100 | HIGH 62/100 | Watch |
| 6 | XRP/USD | 0.93753 | 63.01 | +0.11% | 1.00x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 7 | GBP/USD | 1.31245 | 59.52 | +0.01% | 1.28x | MODERATE 55/100 | HIGH 55/100 | Watch |
| 8 | AUD/USD | 0.66468 | 57.66 | -0.01% | 2.44x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 9 | HYPE/USD | 63.23 | 56.99 | +0.03% | 1.07x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 10 | SUI/USD | 0.6648 | 56.75 | -0.09% | 0.32x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XLM/USD | 0.128532 | 56.71 | +0.03% | 0.72x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 12 | ALGO/USD | 0.07849 | 53.52 | +0.44% | 0.28x | MODERATE 57/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 72.37 | 80.83 | +0.21% | 1.35x | 29796 | STRONG 95/100 | HIGH 55/100 | Watch |
| 2 | QNT/USD | 147.19 | 63.92 | +0.27% | 1.39x | 4615 | STRONG 77/100 | HIGH 55/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.05013 | 59.98 | +0.58% | 1.03x | 11296 | STRONG 70/100 | HIGH 68/100 | Watch |

**Same-run overlap:** SOL/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
