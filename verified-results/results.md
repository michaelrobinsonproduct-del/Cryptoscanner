# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T01:51:21.592540+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45307886313
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8e3ca95e2c0d48bc09a2fa56a517d0649999c56e (atomic ledger/results publication)
**Ledger generation:** 1509 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XLM/USD | 0.131303 | 75.419 | 62.011 | +1.01% | -0.32% | 2.56x | 0.1 | 2026-11-24T01:51:14.763928+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 2 | LINK/USD | 9.06993 | 71.504 | 58.235 | +0.72% | -0.35% | 2.88x | 3.6 | 2026-11-24T01:51:14.763928+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XRP/USD | 0.94521 | 71.177 | 58.544 | +0.62% | -0.47% | 2.54x | 1.6 | 2026-11-24T01:51:14.763928+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LTC/USD | 41.63 | 69.112 | 56.144 | +0.51% | -0.41% | 3.72x | 4.8 | 2026-11-24T01:51:14.763928+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 5 | PEPE/USD | 3.482e-06 | 59.488 | 57.641 | +1.75% | -0.09% | 1.23x | 5.7 | 2026-11-24T01:51:14.763928+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 6 | ADA/USD | 0.149456 | 58.364 | 57.885 | +0.68% | -0.31% | 1.20x | 3.7 | 2026-11-24T01:51:14.763928+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.04878 | 53.336 | 55.683 | +1.31% | -0.59% | 1.06x | 6.2 | 2026-11-24T01:51:14.763928+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 8 | BLESS/USD | 0.015005 | 52.703 | 62.851 | +11.40% | -1.11% | 0.54x | 39.6 | 2026-11-24T01:51:14.763928+00:00 | Not calibrated | WEAK 16/100 | EXTREME 92/100 | Do nothing | WATCH |
| 9 | XDG/USD | 0.0566635 | 52.562 | 59.447 | +0.64% | -0.42% | 0.52x | 0.0 | 2026-11-24T01:51:14.763928+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | VVV/USD | 24.694 | 51.708 | 57.788 | +1.01% | -0.11% | 0.45x | 8.5 | 2026-11-24T01:51:14.763928+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | DOT/USD | 0.6785 | 48.368 | 36.075 | +0.44% | -0.54% | 8.02x | 4.4 | 2026-11-24T01:51:14.763928+00:00 | Not calibrated | MODERATE 54/100 | HIGH 66/100 | Watch | WATCH |
| 12 | PAXG/USD | 3652.49 | 47.189 | 53.740 | +0.87% | -0.08% | 0.39x | 1.1 | 2026-11-24T01:51:14.763928+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BLESS/USD | 62.851 | 0.015005 | -1.11% | 0.54x |
| 2 | XLM/USD | 62.011 | 0.131303 | -0.32% | 2.56x |
| 3 | XDG/USD | 59.447 | 0.0566635 | -0.42% | 0.52x |
| 4 | XRP/USD | 58.544 | 0.94521 | -0.47% | 2.54x |
| 5 | LINK/USD | 58.235 | 9.06993 | -0.35% | 2.88x |
| 6 | ADA/USD | 57.885 | 0.149456 | -0.31% | 1.20x |
| 7 | VVV/USD | 57.788 | 24.694 | -0.11% | 0.45x |
| 8 | PEPE/USD | 57.641 | 3.482e-06 | -0.09% | 1.23x |
| 9 | LTC/USD | 56.144 | 41.63 | -0.41% | 3.72x |
| 10 | NIGHT/USD | 55.683 | 0.04878 | -0.59% | 1.06x |
| 11 | PAXG/USD | 53.740 | 3652.49 | -0.08% | 0.39x |
| 12 | DOT/USD | 36.075 | 0.6785 | -0.54% | 8.02x |

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

- Persisted scans: 1509; predictions: 12865; observations: 914082.
- Matured sampled outcomes across 1/6/24/48h: 23725; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45307886313 · **Generation:** 1509 · **Legacy run:** 45307886313
**Main quote time:** 2026-11-24T01:51:21.592540+00:00 · **Legacy report time:** 2026-11-24T01:52:30.775674+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD | 0.131303 | 75.42 | -0.32% | 2.56x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 2 | LINK/USD | 9.06993 | 71.50 | -0.35% | 2.88x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 3 | XRP/USD | 0.94521 | 71.18 | -0.47% | 2.54x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 4 | LTC/USD | 41.63 | 69.11 | -0.41% | 3.72x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 5 | PEPE/USD | 3.482e-06 | 59.49 | -0.09% | 1.23x | WEAK 40/100 | HIGH 68/100 | Watch |
| 6 | ADA/USD | 0.149456 | 58.36 | -0.31% | 1.20x | WEAK 39/100 | HIGH 68/100 | Watch |
| 7 | NIGHT/USD | 0.04878 | 53.34 | -0.59% | 1.06x | WEAK 37/100 | HIGH 68/100 | Watch |
| 8 | BLESS/USD | 0.015005 | 52.70 | -1.11% | 0.54x | WEAK 16/100 | EXTREME 92/100 | Do nothing |
| 9 | XDG/USD | 0.0566635 | 52.56 | -0.42% | 0.52x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | VVV/USD | 24.694 | 51.71 | -0.11% | 0.45x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | DOT/USD | 0.6785 | 48.37 | -0.54% | 8.02x | MODERATE 54/100 | HIGH 66/100 | Watch |
| 12 | PAXG/USD | 3652.49 | 47.19 | -0.08% | 0.39x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |

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
