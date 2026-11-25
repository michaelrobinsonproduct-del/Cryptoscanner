# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T23:05:47.949576+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45718465008
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f8b7828755a83df3f236d9271330689adf8d38eb (atomic ledger/results publication)
**Ledger generation:** 1779 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0167 | 76.009 | 85.259 | +4.58% | -0.21% | 0.18x | 3.6 | 2026-11-25T23:05:40.258000+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | PAXG/USD | 3570.64 | 74.778 | 60.514 | +0.81% | -0.15% | 13.30x | 0.4 | 2026-11-25T23:05:40.258000+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XMR/USD | 518.93 | 72.941 | 63.380 | +1.83% | +0.03% | 1.94x | 8.9 | 2026-11-25T23:05:40.258000+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 4 | LTC/USD | 42.36 | 71.027 | 78.513 | +3.70% | -0.26% | 0.38x | 4.7 | 2026-11-25T23:05:40.258000+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | ZEC/USD | 752.93 | 66.192 | 67.571 | +1.90% | -0.27% | 1.00x | 1.5 | 2026-11-25T23:05:40.258000+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 6 | HYPE/USD | 61.18 | 65.016 | 69.499 | +2.19% | -0.57% | 0.84x | 1.6 | 2026-11-25T23:05:40.258000+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6615 | 60.212 | 68.623 | +2.16% | -0.18% | 0.25x | 3.0 | 2026-11-25T23:05:40.258000+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XBT/USD | 59918 | 59.665 | 57.062 | +0.30% | -0.30% | 1.41x | 0.0 | 2026-11-25T23:05:40.258000+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 9 | SOL/USD | 70.24 | 59.496 | 60.725 | +0.92% | -0.38% | 1.07x | 1.4 | 2026-11-25T23:05:40.258000+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 10 | PUMP/USD | 0.002536 | 56.007 | 65.380 | +3.98% | -0.67% | 0.40x | 11.8 | 2026-11-25T23:05:40.258000+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 11 | XRP/USD | 0.93267 | 55.337 | 61.384 | +0.98% | -0.43% | 0.61x | 1.0 | 2026-11-25T23:05:40.258000+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XDG/USD | 0.0556989 | 47.325 | 53.510 | +0.84% | -0.31% | 0.54x | 0.6 | 2026-11-25T23:05:40.258000+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 85.259 | 3.0167 | -0.21% | 0.18x |
| 2 | LTC/USD | 78.513 | 42.36 | -0.26% | 0.38x |
| 3 | HYPE/USD | 69.499 | 61.18 | -0.57% | 0.84x |
| 4 | SUI/USD | 68.623 | 0.6615 | -0.18% | 0.25x |
| 5 | ZEC/USD | 67.571 | 752.93 | -0.27% | 1.00x |
| 6 | PUMP/USD | 65.380 | 0.002536 | -0.67% | 0.40x |
| 7 | XMR/USD | 63.380 | 518.93 | +0.03% | 1.94x |
| 8 | XRP/USD | 61.384 | 0.93267 | -0.43% | 0.61x |
| 9 | SOL/USD | 60.725 | 70.24 | -0.38% | 1.07x |
| 10 | PAXG/USD | 60.514 | 3570.64 | -0.15% | 13.30x |
| 11 | XBT/USD | 57.062 | 59918 | -0.30% | 1.41x |
| 12 | XDG/USD | 53.510 | 0.0556989 | -0.31% | 0.54x |

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

- Persisted scans: 1779; predictions: 15092; observations: 1078455.
- Matured sampled outcomes across 1/6/24/48h: 32846; gap abstentions: 23335. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45718465008 · **Generation:** 1779 · **Legacy run:** 45718465008
**Main quote time:** 2026-11-25T23:05:47.949576+00:00 · **Legacy report time:** 2026-11-25T23:06:36.200591+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.0167 | 76.01 | -0.21% | 0.18x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 2 | PAXG/USD | 3570.64 | 74.78 | -0.15% | 13.30x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 3 | XMR/USD | 518.93 | 72.94 | +0.03% | 1.94x | STRONG 71/100 | HIGH 55/100 | Watch |
| 4 | LTC/USD | 42.36 | 71.03 | -0.26% | 0.38x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 5 | ZEC/USD | 752.93 | 66.19 | -0.27% | 1.00x | WEAK 38/100 | HIGH 68/100 | Watch |
| 6 | HYPE/USD | 61.18 | 65.02 | -0.57% | 0.84x | WEAK 38/100 | HIGH 68/100 | Watch |
| 7 | SUI/USD | 0.6615 | 60.21 | -0.18% | 0.25x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 8 | XBT/USD | 59918 | 59.67 | -0.30% | 1.41x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 9 | SOL/USD | 70.24 | 59.50 | -0.38% | 1.07x | WEAK 40/100 | HIGH 68/100 | Watch |
| 10 | PUMP/USD | 0.002536 | 56.01 | -0.67% | 0.40x | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing |
| 11 | XRP/USD | 0.93267 | 55.34 | -0.43% | 0.61x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XDG/USD | 0.0556989 | 47.33 | -0.31% | 0.54x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |

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
