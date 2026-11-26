# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T02:55:55.479997+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45745499949
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f5209272c8c3c28e142d67cf8c67f4889690bd44 (atomic ledger/results publication)
**Ledger generation:** 1803 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.12206 | 70.103 | 56.523 | +0.86% | -0.28% | 57.49x | 4.4 | 2026-11-26T02:55:48.558196+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XRP/USD | 0.95397 | 63.063 | 67.960 | +1.86% | +0.08% | 0.47x | 0.1 | 2026-11-26T02:55:48.558196+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | SUI/USD | 0.6723 | 62.050 | 60.560 | +0.90% | -0.15% | 1.22x | 1.5 | 2026-11-26T02:55:48.558196+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 4 | SYRUP/USD | 0.07033 | 61.911 | 65.682 | +6.13% | +0.24% | 0.50x | 18.5 | 2026-11-26T02:55:48.558196+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | TAO/USD | 184.6437 | 57.917 | 62.742 | +1.68% | +0.03% | 0.50x | 8.0 | 2026-11-26T02:55:48.558196+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XBT/USD | 60548.9 | 57.667 | 57.082 | +0.30% | -0.24% | 1.18x | 0.0 | 2026-11-26T02:55:48.558196+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 7 | SOL/USD | 70.98 | 56.392 | 60.163 | +0.84% | -0.10% | 0.67x | 1.4 | 2026-11-26T02:55:48.558196+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | LTC/USD | 43.35 | 55.553 | 64.336 | +1.50% | -0.41% | 0.33x | 2.3 | 2026-11-26T02:55:48.558196+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | INJ/USD | 6.1 | 53.927 | 55.150 | +2.45% | -0.73% | 1.24x | 8.2 | 2026-11-26T02:55:48.558196+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 10 | ADA/USD | 0.147819 | 53.583 | 63.047 | +1.41% | -0.11% | 0.11x | 3.6 | 2026-11-26T02:55:48.558196+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XDG/USD | 0.0565528 | 53.089 | 57.515 | +1.06% | +0.14% | 0.49x | 0.0 | 2026-11-26T02:55:48.558196+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | PEPE/USD | 3.534e-06 | 48.594 | 53.817 | +1.44% | -0.25% | 0.60x | 2.8 | 2026-11-26T02:55:48.558196+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 67.960 | 0.95397 | +0.08% | 0.47x |
| 2 | SYRUP/USD | 65.682 | 0.07033 | +0.24% | 0.50x |
| 3 | LTC/USD | 64.336 | 43.35 | -0.41% | 0.33x |
| 4 | ADA/USD | 63.047 | 0.147819 | -0.11% | 0.11x |
| 5 | TAO/USD | 62.742 | 184.6437 | +0.03% | 0.50x |
| 6 | SUI/USD | 60.560 | 0.6723 | -0.15% | 1.22x |
| 7 | SOL/USD | 60.163 | 70.98 | -0.10% | 0.67x |
| 8 | XDG/USD | 57.515 | 0.0565528 | +0.14% | 0.49x |
| 9 | XBT/USD | 57.082 | 60548.9 | -0.24% | 1.18x |
| 10 | LINK/USD | 56.523 | 9.12206 | -0.28% | 57.49x |
| 11 | INJ/USD | 55.150 | 6.1 | -0.73% | 1.24x |
| 12 | PEPE/USD | 53.817 | 3.534e-06 | -0.25% | 0.60x |

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

- Persisted scans: 1803; predictions: 15371; observations: 1093071.
- Matured sampled outcomes across 1/6/24/48h: 33371; gap abstentions: 23729. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45745499949 · **Generation:** 1803 · **Legacy run:** 45745499949
**Main quote time:** 2026-11-26T02:55:55.479997+00:00 · **Legacy report time:** 2026-11-26T02:56:58.463320+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD | 9.12206 | 70.10 | -0.28% | 57.49x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 2 | XRP/USD | 0.95397 | 63.06 | +0.08% | 0.47x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 3 | SUI/USD | 0.6723 | 62.05 | -0.15% | 1.22x | WEAK 41/100 | HIGH 68/100 | Watch |
| 4 | SYRUP/USD | 0.07033 | 61.91 | +0.24% | 0.50x | MODERATE 56/100 | VERY_HIGH 81/100 | Watch |
| 5 | TAO/USD | 184.6437 | 57.92 | +0.03% | 0.50x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 6 | XBT/USD | 60548.9 | 57.67 | -0.24% | 1.18x | WEAK 39/100 | HIGH 68/100 | Watch |
| 7 | SOL/USD | 70.98 | 56.39 | -0.10% | 0.67x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | LTC/USD | 43.35 | 55.55 | -0.41% | 0.33x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | INJ/USD | 6.1 | 53.93 | -0.73% | 1.24x | WEAK 37/100 | HIGH 68/100 | Watch |
| 10 | ADA/USD | 0.147819 | 53.58 | -0.11% | 0.11x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XDG/USD | 0.0565528 | 53.09 | +0.14% | 0.49x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 12 | PEPE/USD | 3.534e-06 | 48.59 | -0.25% | 0.60x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |

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
