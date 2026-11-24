# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T02:11:41.446933+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45310310996
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1030ea09d8b2c198d54428170dba60b7daf8d324 (atomic ledger/results publication)
**Ledger generation:** 1511 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AI/USD | 0.01608 | 77.577 | 67.095 | +5.58% | +1.59% | 1.25x | 6.2 | 2026-11-24T02:11:32.675445+00:00 | Not calibrated | STRONG 74/100 | HIGH 67/100 | Watch | WATCH |
| 2 | LINK/USD | 9.07792 | 73.106 | 58.875 | +0.81% | -0.15% | 3.15x | 3.6 | 2026-11-24T02:11:32.675445+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 3 | PEPE/USD | 3.476e-06 | 69.409 | 56.700 | +1.58% | -0.46% | 3.79x | 5.8 | 2026-11-24T02:11:32.675445+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | PAXG/USD | 3643.48 | 66.281 | 52.579 | +0.62% | -0.26% | 2.55x | 0.4 | 2026-11-24T02:11:32.675445+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 5 | UNI/USD | 4.8635 | 63.596 | 51.306 | +0.53% | -0.54% | 4.12x | 7.0 | 2026-11-24T02:11:32.675445+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XRP/USD | 0.94552 | 61.678 | 58.880 | +0.65% | -0.09% | 1.32x | 1.4 | 2026-11-24T02:11:32.675445+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ADA/USD | 0.149595 | 56.584 | 58.069 | +0.77% | -0.15% | 0.93x | 4.7 | 2026-11-24T02:11:32.675445+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | XDG/USD | 0.0567036 | 56.222 | 57.044 | +0.71% | -0.05% | 0.94x | 5.8 | 2026-11-24T02:11:32.675445+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 9 | BLESS/USD | 0.014665 | 54.165 | 61.927 | +8.87% | -1.26% | 0.86x | 41.0 | 2026-11-24T02:11:32.675445+00:00 | Not calibrated | WEAK 17/100 | EXTREME 94/100 | Do nothing | WATCH |
| 10 | XLM/USD | 0.13145 | 54.086 | 60.594 | +1.12% | +0.16% | 0.27x | 4.5 | 2026-11-24T02:11:32.675445+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | VVV/USD | 24.626 | 52.167 | 55.208 | +0.73% | -0.42% | 0.90x | 9.8 | 2026-11-24T02:11:32.675445+00:00 | Not calibrated | WEAK 31/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | XAUT/USD | 3639.1 | 50.161 | 36.749 | +0.55% | -0.32% | 3.27x | 0.8 | 2026-11-24T02:11:32.675445+00:00 | Not calibrated | MODERATE 55/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AI/USD | 67.095 | 0.01608 | +1.59% | 1.25x |
| 2 | BLESS/USD | 61.927 | 0.014665 | -1.26% | 0.86x |
| 3 | XLM/USD | 60.594 | 0.13145 | +0.16% | 0.27x |
| 4 | XRP/USD | 58.880 | 0.94552 | -0.09% | 1.32x |
| 5 | LINK/USD | 58.875 | 9.07792 | -0.15% | 3.15x |
| 6 | ADA/USD | 58.069 | 0.149595 | -0.15% | 0.93x |
| 7 | XDG/USD | 57.044 | 0.0567036 | -0.05% | 0.94x |
| 8 | PEPE/USD | 56.700 | 3.476e-06 | -0.46% | 3.79x |
| 9 | VVV/USD | 55.208 | 24.626 | -0.42% | 0.90x |
| 10 | PAXG/USD | 52.579 | 3643.48 | -0.26% | 2.55x |
| 11 | UNI/USD | 51.306 | 4.8635 | -0.54% | 4.12x |
| 12 | XAUT/USD | 36.749 | 3639.1 | -0.32% | 3.27x |

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

- Persisted scans: 1511; predictions: 12889; observations: 915300.
- Matured sampled outcomes across 1/6/24/48h: 23789; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
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

**Writer:** 45310310996 · **Generation:** 1511 · **Legacy run:** 45310310996
**Main quote time:** 2026-11-24T02:11:41.446933+00:00 · **Legacy report time:** 2026-11-24T02:12:33.114306+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AI/USD ⭐ | 0.01608 | 77.58 | +1.59% | 1.25x | STRONG 84/100 | HIGH 67/100 | Watch |
| 2 | LINK/USD | 9.07792 | 73.11 | -0.15% | 3.15x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 3 | PEPE/USD | 3.476e-06 | 69.41 | -0.46% | 3.79x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | PAXG/USD | 3643.48 | 66.28 | -0.26% | 2.55x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 5 | UNI/USD | 4.8635 | 63.60 | -0.54% | 4.12x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 6 | XRP/USD | 0.94552 | 61.68 | -0.09% | 1.32x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 7 | ADA/USD | 0.149595 | 56.58 | -0.15% | 0.93x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 8 | XDG/USD | 0.0567036 | 56.22 | -0.05% | 0.94x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 9 | BLESS/USD | 0.014665 | 54.17 | -1.26% | 0.86x | WEAK 17/100 | EXTREME 94/100 | Do nothing |
| 10 | XLM/USD | 0.13145 | 54.09 | +0.16% | 0.27x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 11 | VVV/USD | 24.626 | 52.17 | -0.42% | 0.90x | WEAK 31/100 | HIGH 68/100 | Do nothing |
| 12 | XAUT/USD | 3639.1 | 50.16 | -0.32% | 3.27x | MODERATE 55/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AI/USD ⭐ | 0.01608 | 79.04 | +1.59% | 1.25x | 2689 | STRONG 85/100 | HIGH 67/100 | Watch |
| 2 | MON/USD | 0.01185 | 73.87 | +1.63% | 8.01x | 6851 | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 3 | BAT/USD | 0.07908 | 56.86 | +0.18% | 1.86x | 2857 | MODERATE 53/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** AI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
