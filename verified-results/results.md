# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T09:37:33.261553+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45586704399
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** aa92d25b81bafd4bb8f9770ab02287d4ecabcee4 (atomic ledger/results publication)
**Ledger generation:** 1700 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.0102 | 77.600 | 85.001 | +7.71% | -3.11% | 1.81x | 19.7 | 2026-11-25T09:37:26.754955+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 71/100 | Do nothing | WATCH |
| 2 | 2Z/USD | 0.01692 | 68.068 | 47.685 | +3.23% | +1.08% | 4.32x | 11.8 | 2026-11-25T09:37:26.754955+00:00 | Not calibrated | STRONG 84/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | BABY/USD | 0.00867 | 56.477 | 60.550 | +4.96% | +0.23% | 0.48x | 11.5 | 2026-11-25T09:37:26.754955+00:00 | Not calibrated | MODERATE 53/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | VVV/USD | 24.645 | 43.464 | 50.529 | +0.44% | -0.34% | 0.47x | 15.0 | 2026-11-25T09:37:26.754955+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 5 | SYRUP/USD | 0.07065 | 35.435 | 30.764 | +1.41% | -0.73% | 1.83x | 21.3 | 2026-11-25T09:37:26.754955+00:00 | Not calibrated | WEAK 28/100 | EXTREME 85/100 | Do nothing | WATCH |
| 6 | LUNA/USD | 4.758e-05 | 34.309 | 44.538 | +3.93% | -0.23% | 0.09x | 29.6 | 2026-11-25T09:37:26.754955+00:00 | Not calibrated | WEAK 12/100 | EXTREME 93/100 | Do nothing | WATCH |
| 7 | ATOM/USD | 1.251 | 20.078 | 27.352 | +0.45% | -0.44% | 0.49x | 16.0 | 2026-11-25T09:37:26.754955+00:00 | Not calibrated | WEAK 10/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 85.001 | 0.0102 | -3.11% | 1.81x |
| 2 | BABY/USD | 60.550 | 0.00867 | +0.23% | 0.48x |
| 3 | VVV/USD | 50.529 | 24.645 | -0.34% | 0.47x |
| 4 | 2Z/USD | 47.685 | 0.01692 | +1.08% | 4.32x |
| 5 | LUNA/USD | 44.538 | 4.758e-05 | -0.23% | 0.09x |
| 6 | SYRUP/USD | 30.764 | 0.07065 | -0.73% | 1.83x |
| 7 | ATOM/USD | 27.352 | 1.251 | -0.44% | 0.49x |

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

- Persisted scans: 1700; predictions: 14426; observations: 1030383.
- Matured sampled outcomes across 1/6/24/48h: 31111; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45586704399 · **Generation:** 1700 · **Legacy run:** 45586704399
**Main quote time:** 2026-11-25T09:37:33.261553+00:00 · **Legacy report time:** 2026-11-25T09:38:49.520552+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.0102 | 77.60 | -3.11% | 1.81x | MODERATE 54/100 | VERY_HIGH 71/100 | Do nothing |
| 2 | 2Z/USD ⭐ | 0.01692 | 68.07 | +1.08% | 4.32x | STRONG 94/100 | VERY_HIGH 73/100 | Watch |
| 3 | BABY/USD | 0.00867 | 56.48 | +0.23% | 0.48x | MODERATE 53/100 | EXTREME 88/100 | Do nothing |
| 4 | VVV/USD | 24.645 | 43.46 | -0.34% | 0.47x | WEAK 22/100 | VERY_HIGH 82/100 | Do nothing |
| 5 | SYRUP/USD | 0.07065 | 35.44 | -0.73% | 1.83x | WEAK 28/100 | EXTREME 85/100 | Do nothing |
| 6 | LUNA/USD | 4.758e-05 | 34.31 | -0.23% | 0.09x | WEAK 12/100 | EXTREME 93/100 | Do nothing |
| 7 | ATOM/USD | 1.251 | 20.08 | -0.44% | 0.49x | WEAK 10/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | 2Z/USD ⭐ | 0.01688 | 64.54 | +1.08% | 4.32x | 1641 | STRONG 97/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** 2Z/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
