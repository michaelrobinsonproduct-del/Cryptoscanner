# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T14:35:16.870525+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44325762408
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** e057b33272b4d7e2e794fc5f44c0750191aa486c (atomic ledger/results publication)
**Ledger generation:** 590 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04671 | 72.049 | 68.335 | +4.05% | -0.15% | 1.45x | 17.1 | 2026-11-18T14:35:08.095166+00:00 | Not calibrated | MODERATE 51/100 | HIGH 67/100 | Watch | WATCH |
| 2 | XRP/USD | 0.98608 | 64.228 | 55.044 | +0.36% | -0.12% | 1.98x | 5.0 | 2026-11-18T14:35:08.095166+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 3 | CT/USD | 0.121 | 62.575 | 67.687 | +7.08% | -0.66% | 0.82x | 16.5 | 2026-11-18T14:35:08.095166+00:00 | Not calibrated | WEAK 31/100 | EXTREME 86/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.019577 | 58.848 | 61.027 | +4.86% | +0.75% | 0.41x | 8.2 | 2026-11-18T14:35:08.095166+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | VVV/USD | 21.278 | 57.685 | 51.138 | +1.20% | +0.04% | 1.64x | 11.3 | 2026-11-18T14:35:08.095166+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 6 | INFI/USD | 0.1357 | 48.858 | 61.729 | +6.85% | -5.76% | 2.21x | 29.5 | 2026-11-18T14:35:08.095166+00:00 | Not calibrated | WEAK 44/100 | EXTREME 89/100 | Do nothing | WATCH |
| 7 | STABLE/USD | 0.02314 | 48.519 | 58.668 | +9.93% | -0.30% | 0.14x | 34.7 | 2026-11-18T14:35:08.095166+00:00 | Not calibrated | WEAK 19/100 | EXTREME 100/100 | Do nothing | WATCH |
| 8 | CC/USD | 0.08311 | 44.361 | 37.714 | +1.19% | -0.08% | 1.71x | 12.1 | 2026-11-18T14:35:08.095166+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 9 | TRX/USD | 0.309493 | 36.822 | 44.696 | +0.52% | -0.05% | 0.24x | 1.0 | 2026-11-18T14:35:08.095166+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | AKT/USD | 0.52 | 34.950 | 41.359 | +2.10% | -0.31% | 0.51x | 11.5 | 2026-11-18T14:35:08.095166+00:00 | Not calibrated | WEAK 17/100 | EXTREME 87/100 | Do nothing | WATCH |
| 11 | ME/USD | 0.0393 | 29.441 | 31.423 | +1.81% | -0.25% | 0.93x | 25.4 | 2026-11-18T14:35:08.095166+00:00 | Not calibrated | WEAK 10/100 | EXTREME 92/100 | Do nothing | WATCH |
| 12 | W/USD | 0.00898 | 25.385 | 30.071 | +0.56% | -0.44% | 0.75x | 11.1 | 2026-11-18T14:35:08.095166+00:00 | Not calibrated | WEAK 13/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 68.335 | 0.04671 | -0.15% | 1.45x |
| 2 | CT/USD | 67.687 | 0.121 | -0.66% | 0.82x |
| 3 | INFI/USD | 61.729 | 0.1357 | -5.76% | 2.21x |
| 4 | SENT/USD | 61.027 | 0.019577 | +0.75% | 0.41x |
| 5 | STABLE/USD | 58.668 | 0.02314 | -0.30% | 0.14x |
| 6 | XRP/USD | 55.044 | 0.98608 | -0.12% | 1.98x |
| 7 | VVV/USD | 51.138 | 21.278 | +0.04% | 1.64x |
| 8 | TRX/USD | 44.696 | 0.309493 | -0.05% | 0.24x |
| 9 | AKT/USD | 41.359 | 0.52 | -0.31% | 0.51x |
| 10 | CC/USD | 37.714 | 0.08311 | -0.08% | 1.71x |
| 11 | ME/USD | 31.423 | 0.0393 | -0.25% | 0.93x |
| 12 | W/USD | 30.071 | 0.00898 | -0.44% | 0.75x |

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

- Persisted scans: 590; predictions: 5028; observations: 356317.
- Matured sampled outcomes across 1/6/24/48h: 4246; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44325762408 · **Generation:** 590 · **Legacy run:** 44325762408
**Main quote time:** 2026-11-18T14:35:16.870525+00:00 · **Legacy report time:** 2026-11-18T14:35:44.695454+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04671 | 72.05 | -0.15% | 1.45x | MODERATE 51/100 | HIGH 67/100 | Watch |
| 2 | XRP/USD | 0.98608 | 64.23 | -0.12% | 1.98x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 3 | CT/USD | 0.121 | 62.58 | -0.66% | 0.82x | WEAK 31/100 | EXTREME 86/100 | Do nothing |
| 4 | SENT/USD | 0.019577 | 58.85 | +0.75% | 0.41x | MODERATE 59/100 | VERY_HIGH 82/100 | Watch |
| 5 | VVV/USD | 21.278 | 57.69 | +0.04% | 1.64x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 6 | INFI/USD | 0.1357 | 48.86 | -5.76% | 2.21x | WEAK 44/100 | EXTREME 89/100 | Do nothing |
| 7 | STABLE/USD | 0.02314 | 48.52 | -0.30% | 0.14x | WEAK 19/100 | EXTREME 100/100 | Do nothing |
| 8 | CC/USD | 0.08311 | 44.36 | -0.08% | 1.71x | WEAK 37/100 | VERY_HIGH 72/100 | Watch |
| 9 | TRX/USD | 0.309493 | 36.82 | -0.05% | 0.24x | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | AKT/USD | 0.52 | 34.95 | -0.31% | 0.51x | WEAK 17/100 | EXTREME 87/100 | Do nothing |
| 11 | ME/USD | 0.0393 | 29.44 | -0.25% | 0.93x | WEAK 10/100 | EXTREME 92/100 | Do nothing |
| 12 | W/USD | 0.00898 | 25.38 | -0.44% | 0.75x | WEAK 13/100 | VERY_HIGH 79/100 | Do nothing |

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
