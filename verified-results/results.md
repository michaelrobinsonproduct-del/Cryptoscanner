# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T14:01:55.867014+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45409166679
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 24257f28a5a89c8d44f0eeae9875dac10a848fed (atomic ledger/results publication)
**Ledger generation:** 1583 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.516 | 71.130 | 79.703 | +4.37% | -0.44% | 0.36x | 11.8 | 2026-11-24T14:01:51.265721+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | LUNA/USD | 4.591e-05 | 59.564 | 49.222 | +5.61% | -0.93% | 7.97x | 43.8 | 2026-11-24T14:01:51.265721+00:00 | Not calibrated | MODERATE 45/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | MON/USD | 0.01208 | 53.623 | 67.618 | +4.86% | -2.11% | 0.65x | 16.6 | 2026-11-24T14:01:51.265721+00:00 | Not calibrated | WEAK 27/100 | EXTREME 86/100 | Do nothing | WATCH |
| 4 | XMR/USD | 495.53 | 53.013 | 61.633 | +1.96% | -0.40% | 0.34x | 14.1 | 2026-11-24T14:01:51.265721+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 5 | GBP/USD | 1.30974 | 51.440 | 58.219 | +0.50% | +0.03% | 0.31x | 0.5 | 2026-11-24T14:01:51.265721+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.04831 | 51.120 | 47.486 | +0.33% | -0.58% | 1.65x | 4.1 | 2026-11-24T14:01:51.265721+00:00 | Not calibrated | MODERATE 46/100 | HIGH 61/100 | Watch | WATCH |
| 7 | 2Z/USD | 0.01618 | 45.024 | 48.259 | +3.39% | +0.38% | 0.49x | 12.4 | 2026-11-24T14:01:51.265721+00:00 | Not calibrated | MODERATE 48/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | Q/USD | 0.026714 | 24.265 | 35.929 | +3.27% | -0.68% | 0.17x | 35.3 | 2026-11-24T14:01:51.265721+00:00 | Not calibrated | WEAK 2/100 | EXTREME 100/100 | Do nothing | WATCH |
| 9 | LCX/USD | 0.03184 | 19.623 | 19.874 | +0.32% | +0.00% | 0.97x | 28.3 | 2026-11-24T14:01:51.265721+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 10 | SPX/USD | 0.2805 | 11.022 | 22.169 | +0.32% | -0.36% | 0.07x | 25.1 | 2026-11-24T14:01:51.265721+00:00 | Not calibrated | WEAK 1/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 79.703 | 25.516 | -0.44% | 0.36x |
| 2 | MON/USD | 67.618 | 0.01208 | -2.11% | 0.65x |
| 3 | XMR/USD | 61.633 | 495.53 | -0.40% | 0.34x |
| 4 | GBP/USD | 58.219 | 1.30974 | +0.03% | 0.31x |
| 5 | LUNA/USD | 49.222 | 4.591e-05 | -0.93% | 7.97x |
| 6 | 2Z/USD | 48.259 | 0.01618 | +0.38% | 0.49x |
| 7 | NIGHT/USD | 47.486 | 0.04831 | -0.58% | 1.65x |
| 8 | Q/USD | 35.929 | 0.026714 | -0.68% | 0.17x |
| 9 | SPX/USD | 22.169 | 0.2805 | -0.36% | 0.07x |
| 10 | LCX/USD | 19.874 | 0.03184 | +0.00% | 0.97x |

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

- Persisted scans: 1583; predictions: 13653; observations: 959144.
- Matured sampled outcomes across 1/6/24/48h: 26766; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45409166679 · **Generation:** 1583 · **Legacy run:** 45409166679
**Main quote time:** 2026-11-24T14:01:55.867014+00:00 · **Legacy report time:** 2026-11-24T14:03:05.371418+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.516 | 71.13 | -0.44% | 0.36x | WEAK 36/100 | VERY_HIGH 82/100 | Watch |
| 2 | LUNA/USD | 4.591e-05 | 59.56 | -0.93% | 7.97x | MODERATE 45/100 | EXTREME 88/100 | Do nothing |
| 3 | MON/USD | 0.01208 | 53.62 | -2.11% | 0.65x | WEAK 27/100 | EXTREME 86/100 | Do nothing |
| 4 | XMR/USD | 495.53 | 53.01 | -0.40% | 0.34x | WEAK 27/100 | VERY_HIGH 82/100 | Do nothing |
| 5 | GBP/USD | 1.30974 | 51.44 | +0.03% | 0.31x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 6 | NIGHT/USD | 0.04831 | 51.12 | -0.58% | 1.65x | MODERATE 46/100 | HIGH 61/100 | Watch |
| 7 | 2Z/USD | 0.01618 | 45.02 | +0.38% | 0.49x | MODERATE 48/100 | EXTREME 88/100 | Do nothing |
| 8 | Q/USD | 0.026714 | 24.27 | -0.68% | 0.17x | WEAK 2/100 | EXTREME 100/100 | Do nothing |
| 9 | LCX/USD | 0.03184 | 19.62 | +0.00% | 0.97x | WEAK 20/100 | VERY_HIGH 79/100 | Do nothing |
| 10 | SPX/USD | 0.2805 | 11.02 | -0.36% | 0.07x | WEAK 1/100 | EXTREME 93/100 | Do nothing |

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
