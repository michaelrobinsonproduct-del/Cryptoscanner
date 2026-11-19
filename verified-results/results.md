# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T02:45:25.139142+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44446507097
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 5c83eb3ae68ee3347e1432d7ce36f3b6b32292ea (atomic ledger/results publication)
**Ledger generation:** 734 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.022018 | 75.858 | 72.704 | +6.86% | +0.33% | 1.15x | 7.7 | 2026-11-19T02:45:18.326234+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.3058 | 67.052 | 54.817 | +0.25% | -0.55% | 4.51x | 3.9 | 2026-11-19T02:45:18.326234+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 3 | VVV/USD | 21.962 | 65.952 | 55.643 | +1.34% | -0.94% | 4.91x | 5.5 | 2026-11-19T02:45:18.326234+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ICP/USD | 2.24 | 51.188 | 48.988 | +2.85% | -0.44% | 1.44x | 17.9 | 2026-11-19T02:45:18.326234+00:00 | Not calibrated | WEAK 41/100 | HIGH 67/100 | Watch | WATCH |
| 5 | UAI/USD | 0.03368 | 49.297 | 35.482 | +1.72% | -0.24% | 6.60x | 14.9 | 2026-11-19T02:45:18.326234+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | BMT/USD | 0.01958 | 46.541 | 51.590 | +3.71% | -0.25% | 0.62x | 10.2 | 2026-11-19T02:45:18.326234+00:00 | Not calibrated | WEAK 23/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | AKE/USD | 0.01042315 | 42.059 | 29.342 | +0.31% | -0.46% | 4.25x | 14.8 | 2026-11-19T02:45:18.326234+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | TON/USD | 1.024 | 34.968 | 31.304 | +0.29% | -0.19% | 1.46x | 9.8 | 2026-11-19T02:45:18.326234+00:00 | Not calibrated | WEAK 37/100 | HIGH 66/100 | Watch | WATCH |
| 9 | MEGA/USD | 0.05684 | 33.485 | 33.877 | +1.50% | -1.71% | 1.82x | 15.8 | 2026-11-19T02:45:18.326234+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 10 | LIGHTER/USD | 2.722 | 26.138 | 28.628 | +0.29% | -0.87% | 1.19x | 18.4 | 2026-11-19T02:45:18.326234+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 72.704 | 0.022018 | +0.33% | 1.15x |
| 2 | VVV/USD | 55.643 | 21.962 | -0.94% | 4.91x |
| 3 | NEAR/USD | 54.817 | 3.3058 | -0.55% | 4.51x |
| 4 | BMT/USD | 51.590 | 0.01958 | -0.25% | 0.62x |
| 5 | ICP/USD | 48.988 | 2.24 | -0.44% | 1.44x |
| 6 | UAI/USD | 35.482 | 0.03368 | -0.24% | 6.60x |
| 7 | MEGA/USD | 33.877 | 0.05684 | -1.71% | 1.82x |
| 8 | TON/USD | 31.304 | 1.024 | -0.19% | 1.46x |
| 9 | AKE/USD | 29.342 | 0.01042315 | -0.46% | 4.25x |
| 10 | LIGHTER/USD | 28.628 | 2.722 | -0.87% | 1.19x |

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

- Persisted scans: 734; predictions: 5977; observations: 444013.
- Matured sampled outcomes across 1/6/24/48h: 5920; gap abstentions: 13501. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44446507097 · **Generation:** 734 · **Legacy run:** 44446507097
**Main quote time:** 2026-11-19T02:45:25.139142+00:00 · **Legacy report time:** 2026-11-19T02:46:07.169441+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022018 | 75.86 | +0.33% | 1.15x | STRONG 83/100 | VERY_HIGH 74/100 | Watch |
| 2 | NEAR/USD | 3.3058 | 67.05 | -0.55% | 4.51x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 3 | VVV/USD | 21.962 | 65.95 | -0.94% | 4.91x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 4 | ICP/USD | 2.24 | 51.19 | -0.44% | 1.44x | WEAK 41/100 | HIGH 67/100 | Watch |
| 5 | UAI/USD | 0.03368 | 49.30 | -0.24% | 6.60x | MODERATE 50/100 | VERY_HIGH 79/100 | Watch |
| 6 | BMT/USD | 0.01958 | 46.54 | -0.25% | 0.62x | WEAK 23/100 | EXTREME 94/100 | Do nothing |
| 7 | AKE/USD | 0.01042315 | 42.06 | -0.46% | 4.25x | MODERATE 46/100 | VERY_HIGH 72/100 | Watch |
| 8 | TON/USD | 1.024 | 34.97 | -0.19% | 1.46x | WEAK 37/100 | HIGH 66/100 | Watch |
| 9 | MEGA/USD | 0.05684 | 33.49 | -1.71% | 1.82x | WEAK 32/100 | VERY_HIGH 83/100 | Do nothing |
| 10 | LIGHTER/USD | 2.722 | 26.14 | -0.87% | 1.19x | WEAK 18/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022029 | 76.63 | +0.33% | 1.15x | 7885 | STRONG 83/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
