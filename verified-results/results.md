# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T08:11:42.995208+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45353691853
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ae1d3bdececb0561bcd3afee198cfdb07d04dfae (atomic ledger/results publication)
**Ledger generation:** 1548 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.298 | 71.025 | 75.190 | +3.48% | -0.04% | 0.60x | 8.3 | 2026-11-24T08:11:35.315528+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | LINK/USD | 9.02938 | 68.917 | 54.958 | +0.27% | -0.21% | 3.29x | 3.9 | 2026-11-24T08:11:35.315528+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 3 | BABY/USD | 0.00898 | 63.814 | 65.836 | +5.65% | -0.99% | 1.29x | 11.1 | 2026-11-24T08:11:35.315528+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.529e-06 | 63.056 | 69.624 | +3.13% | -0.03% | 0.36x | 5.7 | 2026-11-24T08:11:35.315528+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | XMR/USD | 498.24 | 57.460 | 65.573 | +2.51% | -0.32% | 0.35x | 14.1 | 2026-11-24T08:11:35.315528+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 6 | LUNA/USD | 4.537e-05 | 53.000 | 52.809 | +4.37% | +0.27% | 0.89x | 19.8 | 2026-11-24T08:11:35.315528+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | NEAR/USD | 2.9981 | 51.682 | 56.801 | +0.57% | -0.27% | 0.62x | 4.3 | 2026-11-24T08:11:35.315528+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | ICNT/USD | 0.3214 | 50.331 | 49.392 | +3.98% | -2.81% | 3.07x | 21.8 | 2026-11-24T08:11:35.315528+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 9 | XRP/USD | 0.94175 | 49.124 | 56.281 | +0.25% | -0.27% | 0.42x | 1.0 | 2026-11-24T08:11:35.315528+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | TIA/USD | 0.3407 | 43.560 | 40.707 | +1.46% | -0.32% | 1.45x | 2.9 | 2026-11-24T08:11:35.315528+00:00 | Not calibrated | WEAK 42/100 | HIGH 66/100 | Watch | WATCH |
| 11 | WLD/USD | 0.2409 | 36.298 | 40.931 | +1.09% | -0.12% | 0.60x | 4.2 | 2026-11-24T08:11:35.315528+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 12 | NIGHT/USD | 0.04844 | 36.239 | 48.234 | +0.60% | -0.96% | 0.28x | 10.3 | 2026-11-24T08:11:35.315528+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 75.190 | 25.298 | -0.04% | 0.60x |
| 2 | PEPE/USD | 69.624 | 3.529e-06 | -0.03% | 0.36x |
| 3 | BABY/USD | 65.836 | 0.00898 | -0.99% | 1.29x |
| 4 | XMR/USD | 65.573 | 498.24 | -0.32% | 0.35x |
| 5 | NEAR/USD | 56.801 | 2.9981 | -0.27% | 0.62x |
| 6 | XRP/USD | 56.281 | 0.94175 | -0.27% | 0.42x |
| 7 | LINK/USD | 54.958 | 9.02938 | -0.21% | 3.29x |
| 8 | LUNA/USD | 52.809 | 4.537e-05 | +0.27% | 0.89x |
| 9 | ICNT/USD | 49.392 | 0.3214 | -2.81% | 3.07x |
| 10 | NIGHT/USD | 48.234 | 0.04844 | -0.96% | 0.28x |
| 11 | WLD/USD | 40.931 | 0.2409 | -0.12% | 0.60x |
| 12 | TIA/USD | 40.707 | 0.3407 | -0.32% | 1.45x |

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

- Persisted scans: 1548; predictions: 13309; observations: 937830.
- Matured sampled outcomes across 1/6/24/48h: 25139; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 139 (sampled only; not a success-rate estimate).
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

**Writer:** 45353691853 · **Generation:** 1548 · **Legacy run:** 45353691853
**Main quote time:** 2026-11-24T08:11:42.995208+00:00 · **Legacy report time:** 2026-11-24T08:12:54.744524+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.298 | 71.03 | -0.04% | 0.60x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 2 | LINK/USD | 9.02938 | 68.92 | -0.21% | 3.29x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 3 | BABY/USD | 0.00898 | 63.81 | -0.99% | 1.29x | WEAK 37/100 | VERY_HIGH 72/100 | Watch |
| 4 | PEPE/USD | 3.529e-06 | 63.06 | -0.03% | 0.36x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 5 | XMR/USD | 498.24 | 57.46 | -0.32% | 0.35x | WEAK 29/100 | VERY_HIGH 82/100 | Do nothing |
| 6 | LUNA/USD | 4.537e-05 | 53.00 | +0.27% | 0.89x | MODERATE 52/100 | VERY_HIGH 73/100 | Watch |
| 7 | NEAR/USD | 2.9981 | 51.68 | -0.27% | 0.62x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | ICNT/USD | 0.3214 | 50.33 | -2.81% | 3.07x | MODERATE 45/100 | VERY_HIGH 82/100 | Do nothing |
| 9 | XRP/USD | 0.94175 | 49.12 | -0.27% | 0.42x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | TIA/USD | 0.3407 | 43.56 | -0.32% | 1.45x | WEAK 42/100 | HIGH 66/100 | Watch |
| 11 | WLD/USD | 0.2409 | 36.30 | -0.12% | 0.60x | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing |
| 12 | NIGHT/USD | 0.04844 | 36.24 | -0.96% | 0.28x | WEAK 18/100 | VERY_HIGH 82/100 | Do nothing |

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
