# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T06:06:00.700065+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45765693929
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f2df4da8dce474afea2f3962b9b504f51ae0e425 (atomic ledger/results publication)
**Ledger generation:** 1822 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ADA/USD | 0.148729 | 80.575 | 67.428 | +2.03% | -0.37% | 8.95x | 3.6 | 2026-11-26T06:05:51.905370+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 2 | LTC/USD | 43.51 | 80.009 | 65.813 | +1.87% | -0.16% | 3.82x | 4.6 | 2026-11-26T06:05:51.905370+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LINK/USD | 9.18459 | 75.124 | 62.264 | +1.55% | -0.43% | 4.52x | 2.7 | 2026-11-26T06:05:51.905370+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 4 | QNT/USD | 147.6 | 74.933 | 59.661 | +1.93% | +0.05% | 4.48x | 7.5 | 2026-11-26T06:05:51.905370+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 5 | XRP/USD | 0.95517 | 68.946 | 68.648 | +1.99% | -0.51% | 1.28x | 0.5 | 2026-11-26T06:05:51.905370+00:00 | Not calibrated | WEAK 44/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SYRUP/USD | 0.07083 | 67.002 | 71.491 | +6.88% | +0.55% | 0.27x | 11.3 | 2026-11-26T06:05:51.905370+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | SOL/USD | 70.74 | 66.659 | 57.774 | +0.50% | -0.58% | 2.18x | 1.4 | 2026-11-26T06:05:51.905370+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0565587 | 62.796 | 57.339 | +1.07% | -0.36% | 1.73x | 1.1 | 2026-11-26T06:05:51.905370+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 9 | PEPE/USD | 3.535e-06 | 61.253 | 54.271 | +1.46% | -0.87% | 2.13x | 2.8 | 2026-11-26T06:05:51.905370+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XBT/USD | 60574 | 59.944 | 57.373 | +0.34% | -0.37% | 1.44x | 0.0 | 2026-11-26T06:05:51.905370+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 11 | INJ/USD | 6.128 | 54.581 | 60.269 | +2.92% | -0.49% | 0.68x | 4.9 | 2026-11-26T06:05:51.905370+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | PIEVERSE/USD | 3.9015 | 53.686 | 64.304 | +10.18% | -1.08% | 0.48x | 36.1 | 2026-11-26T06:05:51.905370+00:00 | Not calibrated | WEAK 17/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SYRUP/USD | 71.491 | 0.07083 | +0.55% | 0.27x |
| 2 | XRP/USD | 68.648 | 0.95517 | -0.51% | 1.28x |
| 3 | ADA/USD | 67.428 | 0.148729 | -0.37% | 8.95x |
| 4 | LTC/USD | 65.813 | 43.51 | -0.16% | 3.82x |
| 5 | PIEVERSE/USD | 64.304 | 3.9015 | -1.08% | 0.48x |
| 6 | LINK/USD | 62.264 | 9.18459 | -0.43% | 4.52x |
| 7 | INJ/USD | 60.269 | 6.128 | -0.49% | 0.68x |
| 8 | QNT/USD | 59.661 | 147.6 | +0.05% | 4.48x |
| 9 | SOL/USD | 57.774 | 70.74 | -0.58% | 2.18x |
| 10 | XBT/USD | 57.373 | 60574 | -0.37% | 1.44x |
| 11 | XDG/USD | 57.339 | 0.0565587 | -0.36% | 1.73x |
| 12 | PEPE/USD | 54.271 | 3.535e-06 | -0.87% | 2.13x |

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

- Persisted scans: 1822; predictions: 15599; observations: 1104642.
- Matured sampled outcomes across 1/6/24/48h: 33839; gap abstentions: 24030. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45765693929 · **Generation:** 1822 · **Legacy run:** 45765693929
**Main quote time:** 2026-11-26T06:06:00.700065+00:00 · **Legacy report time:** 2026-11-26T06:06:52.039690+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD | 0.148729 | 80.58 | -0.37% | 8.95x | STRONG 70/100 | HIGH 61/100 | Watch |
| 2 | LTC/USD | 43.51 | 80.01 | -0.16% | 3.82x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | LINK/USD | 9.18459 | 75.12 | -0.43% | 4.52x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 4 | QNT/USD ⭐ | 147.6 | 74.93 | +0.05% | 4.48x | STRONG 92/100 | HIGH 55/100 | Watch |
| 5 | XRP/USD | 0.95517 | 68.95 | -0.51% | 1.28x | WEAK 44/100 | HIGH 61/100 | Watch |
| 6 | SYRUP/USD | 0.07083 | 67.00 | +0.55% | 0.27x | MODERATE 59/100 | VERY_HIGH 81/100 | Watch |
| 7 | SOL/USD | 70.74 | 66.66 | -0.58% | 2.18x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 8 | XDG/USD | 0.0565587 | 62.80 | -0.36% | 1.73x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 9 | PEPE/USD | 3.535e-06 | 61.25 | -0.87% | 2.13x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 10 | XBT/USD | 60574 | 59.94 | -0.37% | 1.44x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 11 | INJ/USD | 6.128 | 54.58 | -0.49% | 0.68x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | PIEVERSE/USD | 3.9015 | 53.69 | -1.08% | 0.48x | WEAK 17/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 147.68 | 72.83 | +0.05% | 4.48x | 9198 | STRONG 91/100 | HIGH 55/100 | Watch |

**Same-run overlap:** QNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
