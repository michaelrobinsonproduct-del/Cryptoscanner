# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T13:25:27.732775+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44533150403
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** f3342e7acd6576388ade0637ae20ae2b731e8195 (atomic ledger/results publication)
**Ledger generation:** 782 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 593; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LIGHTER/USD | 2.947 | 90.209 | 74.529 | +8.59% | +0.14% | 5.06x | 13.6 | 2026-11-19T13:25:21.050386+00:00 | Not calibrated | STRONG 85/100 | HIGH 66/100 | Watch | WATCH |
| 2 | PEPE/USD | 3.954e-06 | 85.374 | 74.264 | +5.55% | -0.78% | 2.51x | 10.1 | 2026-11-19T13:25:21.050386+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 3 | VVV/USD | 22.854 | 83.126 | 90.366 | +5.46% | -0.04% | 0.29x | 5.7 | 2026-11-19T13:25:21.050386+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | XRP/USD | 0.98614 | 82.769 | 69.270 | +2.05% | -0.30% | 5.06x | 0.1 | 2026-11-19T13:25:21.050386+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.3971 | 72.702 | 74.400 | +3.02% | -0.12% | 0.89x | 3.5 | 2026-11-19T13:25:21.050386+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 6 | ZEC/USD | 942.45 | 72.451 | 77.616 | +3.34% | -0.67% | 0.82x | 1.6 | 2026-11-19T13:25:21.050386+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 7 | LINK/USD | 9.20966 | 69.629 | 65.560 | +1.51% | -0.22% | 1.52x | 0.0 | 2026-11-19T13:25:21.050386+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ETH/USD | 1801.51 | 63.864 | 65.523 | +1.51% | -0.34% | 1.00x | 0.1 | 2026-11-19T13:25:21.050386+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 9 | SENT/USD | 0.021805 | 61.620 | 72.668 | +5.82% | -0.62% | 0.21x | 2.7 | 2026-11-19T13:25:21.050386+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | XBT/USD | 63644.2 | 60.468 | 62.324 | +1.05% | -0.27% | 0.95x | 0.0 | 2026-11-19T13:25:21.050386+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0595446 | 56.141 | 61.370 | +1.43% | -0.10% | 0.53x | 0.0 | 2026-11-19T13:25:21.050386+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | TRX/USD | 0.312328 | 38.452 | 47.253 | +0.99% | -0.05% | 0.15x | 0.2 | 2026-11-19T13:25:21.050386+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 90.366 | 22.854 | -0.04% | 0.29x |
| 2 | ZEC/USD | 77.616 | 942.45 | -0.67% | 0.82x |
| 3 | LIGHTER/USD | 74.529 | 2.947 | +0.14% | 5.06x |
| 4 | NEAR/USD | 74.400 | 3.3971 | -0.12% | 0.89x |
| 5 | PEPE/USD | 74.264 | 3.954e-06 | -0.78% | 2.51x |
| 6 | SENT/USD | 72.668 | 0.021805 | -0.62% | 0.21x |
| 7 | XRP/USD | 69.270 | 0.98614 | -0.30% | 5.06x |
| 8 | LINK/USD | 65.560 | 9.20966 | -0.22% | 1.52x |
| 9 | ETH/USD | 65.523 | 1801.51 | -0.34% | 1.00x |
| 10 | XBT/USD | 62.324 | 63644.2 | -0.27% | 0.95x |
| 11 | XDG/USD | 61.370 | 0.0595446 | -0.10% | 0.53x |
| 12 | TRX/USD | 47.253 | 0.312328 | -0.05% | 0.15x |

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

- Persisted scans: 782; predictions: 6528; observations: 473144.
- Matured sampled outcomes across 1/6/24/48h: 6671; gap abstentions: 14952. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44533150403 · **Generation:** 782 · **Legacy run:** 44533150403
**Main quote time:** 2026-11-19T13:25:27.732775+00:00 · **Legacy report time:** 2026-11-19T13:26:19.617509+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LIGHTER/USD ⭐ | 2.947 | 90.21 | +0.14% | 5.06x | STRONG 95/100 | HIGH 66/100 | Watch |
| 2 | PEPE/USD | 3.954e-06 | 85.37 | -0.78% | 2.51x | MODERATE 68/100 | HIGH 67/100 | Watch |
| 3 | VVV/USD | 22.854 | 83.13 | -0.04% | 0.29x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 4 | XRP/USD | 0.98614 | 82.77 | -0.30% | 5.06x | STRONG 71/100 | HIGH 61/100 | Watch |
| 5 | NEAR/USD | 3.3971 | 72.70 | -0.12% | 0.89x | WEAK 41/100 | HIGH 68/100 | Watch |
| 6 | ZEC/USD | 942.45 | 72.45 | -0.67% | 0.82x | WEAK 41/100 | HIGH 68/100 | Watch |
| 7 | LINK/USD | 9.20966 | 69.63 | -0.22% | 1.52x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 8 | ETH/USD | 1801.51 | 63.86 | -0.34% | 1.00x | WEAK 42/100 | HIGH 68/100 | Watch |
| 9 | SENT/USD | 0.021805 | 61.62 | -0.62% | 0.21x | WEAK 36/100 | VERY_HIGH 81/100 | Watch |
| 10 | XBT/USD | 63644.2 | 60.47 | -0.27% | 0.95x | WEAK 35/100 | HIGH 68/100 | Watch |
| 11 | XDG/USD | 0.0595446 | 56.14 | -0.10% | 0.53x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | TRX/USD | 0.312328 | 38.45 | -0.05% | 0.15x | WEAK 24/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LIGHTER/USD ⭐ | 2.944 | 83.62 | +0.14% | 5.06x | 3798 | STRONG 97/100 | HIGH 60/100 | Watch |
| 2 | ADA/USD | 0.155245 | 78.52 | +0.09% | 1.42x | 11938 | STRONG 74/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LIGHTER/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
