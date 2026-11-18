# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T15:30:17.426179+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44336245666
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 331838b34aff966f4b69b2432cd6e8cc96bcc740 (atomic ledger/results publication)
**Ledger generation:** 601 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019856 | 76.480 | 71.272 | +6.36% | +1.29% | 0.88x | 8.6 | 2026-11-18T15:30:09.402845+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | CT/USD | 0.1229 | 73.760 | 67.891 | +8.76% | +0.00% | 1.59x | 16.3 | 2026-11-18T15:30:09.402845+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | STABLE/USD | 0.02303 | 67.404 | 62.958 | +9.41% | -0.13% | 1.51x | 26.1 | 2026-11-18T15:30:09.402845+00:00 | Not calibrated | WEAK 44/100 | EXTREME 85/100 | Do nothing | WATCH |
| 4 | AKE/USD | 0.01042278 | 54.161 | 48.377 | +4.39% | -1.40% | 2.28x | 31.9 | 2026-11-18T15:30:09.402845+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 5 | TRX/USD | 0.30999 | 50.626 | 45.325 | +0.68% | -0.03% | 1.55x | 0.9 | 2026-11-18T15:30:09.402845+00:00 | Not calibrated | MODERATE 45/100 | HIGH 61/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.0454 | 49.498 | 52.678 | +1.14% | +0.11% | 0.63x | 6.6 | 2026-11-18T15:30:09.402845+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | MNT/USD | 0.3859 | 44.721 | 51.428 | +3.38% | -0.08% | 0.37x | 10.4 | 2026-11-18T15:30:09.402845+00:00 | Not calibrated | WEAK 22/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | RE/USD | 0.24029 | 42.230 | 47.765 | +3.42% | +0.19% | 0.35x | 13.7 | 2026-11-18T15:30:09.402845+00:00 | Not calibrated | WEAK 36/100 | EXTREME 88/100 | Do nothing | WATCH |
| 9 | CAP/USD | 0.101649 | 39.410 | 30.999 | +0.67% | -0.55% | 2.12x | 10.0 | 2026-11-18T15:30:09.402845+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 10 | AKT/USD | 0.5134 | 37.090 | 35.976 | +0.81% | -0.48% | 1.35x | 3.9 | 2026-11-18T15:30:09.402845+00:00 | Not calibrated | WEAK 39/100 | HIGH 66/100 | Watch | WATCH |
| 11 | CC/USD | 0.08289 | 32.604 | 39.154 | +0.93% | -0.07% | 0.38x | 6.0 | 2026-11-18T15:30:09.402845+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 12 | ZAMA/USD | 0.0606 | 26.094 | 34.472 | +1.12% | +0.25% | 0.04x | 9.9 | 2026-11-18T15:30:09.402845+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 71.272 | 0.019856 | +1.29% | 0.88x |
| 2 | CT/USD | 67.891 | 0.1229 | +0.00% | 1.59x |
| 3 | STABLE/USD | 62.958 | 0.02303 | -0.13% | 1.51x |
| 4 | NIGHT/USD | 52.678 | 0.0454 | +0.11% | 0.63x |
| 5 | MNT/USD | 51.428 | 0.3859 | -0.08% | 0.37x |
| 6 | AKE/USD | 48.377 | 0.01042278 | -1.40% | 2.28x |
| 7 | RE/USD | 47.765 | 0.24029 | +0.19% | 0.35x |
| 8 | TRX/USD | 45.325 | 0.30999 | -0.03% | 1.55x |
| 9 | CC/USD | 39.154 | 0.08289 | -0.07% | 0.38x |
| 10 | AKT/USD | 35.976 | 0.5134 | -0.48% | 1.35x |
| 11 | ZAMA/USD | 34.472 | 0.0606 | +0.25% | 0.04x |
| 12 | CAP/USD | 30.999 | 0.101649 | -0.55% | 2.12x |

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

- Persisted scans: 601; predictions: 5148; observations: 363016.
- Matured sampled outcomes across 1/6/24/48h: 4359; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44336245666 · **Generation:** 601 · **Legacy run:** 44336245666
**Main quote time:** 2026-11-18T15:30:17.426179+00:00 · **Legacy report time:** 2026-11-18T15:30:46.696463+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019856 | 76.48 | +1.29% | 0.88x | MODERATE 68/100 | VERY_HIGH 74/100 | Watch |
| 2 | CT/USD | 0.1229 | 73.76 | +0.00% | 1.59x | MODERATE 67/100 | VERY_HIGH 73/100 | Watch |
| 3 | STABLE/USD | 0.02303 | 67.40 | -0.13% | 1.51x | WEAK 44/100 | EXTREME 85/100 | Do nothing |
| 4 | AKE/USD | 0.01042278 | 54.16 | -1.40% | 2.28x | MODERATE 47/100 | VERY_HIGH 82/100 | Do nothing |
| 5 | TRX/USD | 0.30999 | 50.63 | -0.03% | 1.55x | MODERATE 45/100 | HIGH 61/100 | Watch |
| 6 | NIGHT/USD | 0.0454 | 49.50 | +0.11% | 0.63x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 7 | MNT/USD | 0.3859 | 44.72 | -0.08% | 0.37x | WEAK 22/100 | EXTREME 87/100 | Do nothing |
| 8 | RE/USD | 0.24029 | 42.23 | +0.19% | 0.35x | WEAK 36/100 | EXTREME 88/100 | Do nothing |
| 9 | CAP/USD | 0.101649 | 39.41 | -0.55% | 2.12x | MODERATE 45/100 | VERY_HIGH 79/100 | Watch |
| 10 | AKT/USD | 0.5134 | 37.09 | -0.48% | 1.35x | WEAK 39/100 | HIGH 66/100 | Watch |
| 11 | CC/USD | 0.08289 | 32.60 | -0.07% | 0.38x | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing |
| 12 | ZAMA/USD | 0.0606 | 26.09 | +0.25% | 0.04x | WEAK 43/100 | VERY_HIGH 82/100 | Watch |

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
