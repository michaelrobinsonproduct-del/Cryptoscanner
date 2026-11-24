# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T06:51:51.903763+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45343332242
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** fce7b41ef6cd6132eb87aa5a3bf36ca0c55cdd5c (atomic ledger/results publication)
**Ledger generation:** 1540 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.493 | 89.610 | 82.959 | +4.27% | +0.41% | 1.46x | 3.9 | 2026-11-24T06:51:45.428070+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 2 | AI/USD | 0.01674 | 78.868 | 72.854 | +9.91% | +1.21% | 1.00x | 6.0 | 2026-11-24T06:51:45.428070+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | LINK/USD | 9.10255 | 75.980 | 60.947 | +1.08% | +0.01% | 2.60x | 3.3 | 2026-11-24T06:51:45.428070+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 4 | HYPE/USD | 64.26 | 75.808 | 61.042 | +0.97% | -0.05% | 3.86x | 1.6 | 2026-11-24T06:51:45.428070+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XMR/USD | 496.97 | 75.619 | 68.456 | +2.25% | +0.08% | 1.68x | 4.6 | 2026-11-24T06:51:45.428070+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.542e-06 | 65.467 | 73.684 | +3.51% | -0.11% | 0.23x | 2.8 | 2026-11-24T06:51:45.428070+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | ADA/USD | 0.149051 | 61.523 | 56.036 | +0.41% | +0.07% | 1.52x | 3.6 | 2026-11-24T06:51:45.428070+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0565171 | 61.512 | 57.627 | +0.38% | +0.16% | 1.31x | 0.0 | 2026-11-24T06:51:45.428070+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 9 | NEAR/USD | 3.0339 | 60.711 | 67.209 | +1.77% | +0.03% | 0.34x | 0.3 | 2026-11-24T06:51:45.428070+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XRP/USD | 0.95069 | 60.191 | 63.157 | +1.20% | -0.09% | 0.75x | 0.5 | 2026-11-24T06:51:45.428070+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 11 | LTC/USD | 41.79 | 56.254 | 60.058 | +0.89% | +0.05% | 0.60x | 2.4 | 2026-11-24T06:51:45.428070+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | TON/USD | 0.991 | 31.496 | 30.050 | +0.30% | +0.00% | 1.14x | 10.1 | 2026-11-24T06:51:45.428070+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 73/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 82.959 | 25.493 | +0.41% | 1.46x |
| 2 | PEPE/USD | 73.684 | 3.542e-06 | -0.11% | 0.23x |
| 3 | AI/USD | 72.854 | 0.01674 | +1.21% | 1.00x |
| 4 | XMR/USD | 68.456 | 496.97 | +0.08% | 1.68x |
| 5 | NEAR/USD | 67.209 | 3.0339 | +0.03% | 0.34x |
| 6 | XRP/USD | 63.157 | 0.95069 | -0.09% | 0.75x |
| 7 | HYPE/USD | 61.042 | 64.26 | -0.05% | 3.86x |
| 8 | LINK/USD | 60.947 | 9.10255 | +0.01% | 2.60x |
| 9 | LTC/USD | 60.058 | 41.79 | +0.05% | 0.60x |
| 10 | XDG/USD | 57.627 | 0.0565171 | +0.16% | 1.31x |
| 11 | ADA/USD | 56.036 | 0.149051 | +0.07% | 1.52x |
| 12 | TON/USD | 30.050 | 0.991 | +0.00% | 1.14x |

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

- Persisted scans: 1540; predictions: 13213; observations: 932958.
- Matured sampled outcomes across 1/6/24/48h: 24819; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 139 (sampled only; not a success-rate estimate).
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

**Writer:** 45343332242 · **Generation:** 1540 · **Legacy run:** 45343332242
**Main quote time:** 2026-11-24T06:51:51.903763+00:00 · **Legacy report time:** 2026-11-24T06:52:54.675544+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.493 | 89.61 | +0.41% | 1.46x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | AI/USD | 0.01674 | 78.87 | +1.21% | 1.00x | MODERATE 69/100 | VERY_HIGH 74/100 | Watch |
| 3 | LINK/USD | 9.10255 | 75.98 | +0.01% | 2.60x | STRONG 83/100 | HIGH 55/100 | Watch |
| 4 | HYPE/USD | 64.26 | 75.81 | -0.05% | 3.86x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 5 | XMR/USD ⭐ | 496.97 | 75.62 | +0.08% | 1.68x | STRONG 83/100 | HIGH 55/100 | Watch |
| 6 | PEPE/USD | 3.542e-06 | 65.47 | -0.11% | 0.23x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 7 | ADA/USD | 0.149051 | 61.52 | +0.07% | 1.52x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 8 | XDG/USD | 0.0565171 | 61.51 | +0.16% | 1.31x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 9 | NEAR/USD | 3.0339 | 60.71 | +0.03% | 0.34x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 10 | XRP/USD | 0.95069 | 60.19 | -0.09% | 0.75x | WEAK 35/100 | HIGH 68/100 | Watch |
| 11 | LTC/USD | 41.79 | 56.25 | +0.05% | 0.60x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 12 | TON/USD | 0.991 | 31.50 | +0.00% | 1.14x | WEAK 36/100 | VERY_HIGH 73/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.669 | 88.07 | +0.41% | 1.46x | 12640 | STRONG 99/100 | HIGH 55/100 | Watch |
| 2 | BABY/USD | 0.00905 | 83.81 | +1.58% | 4.68x | 3303 | STRONG 87/100 | VERY_HIGH 72/100 | Watch |
| 3 | XMR/USD ⭐ | 496.8 | 72.30 | +0.08% | 1.68x | 11732 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
