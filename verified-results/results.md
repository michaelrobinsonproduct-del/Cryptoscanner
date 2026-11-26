# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T23:11:27.514474+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45909232183
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 34892ef00f1e795ed38039af37a049f39dc0a4b3 (atomic ledger/results publication)
**Ledger generation:** 1926 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 600; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.5021 | 80.263 | 67.839 | +6.13% | -0.52% | 2.76x | 15.9 | 2026-11-26T23:11:20.825659+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | LTC/USD | 43.89 | 65.039 | 72.061 | +2.76% | -0.32% | 0.46x | 4.6 | 2026-11-26T23:11:20.825659+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | XRP/USD | 0.94336 | 62.587 | 59.393 | +0.73% | -0.40% | 1.52x | 1.4 | 2026-11-26T23:11:20.825659+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ZRO/USD | 1.117 | 60.911 | 72.081 | +9.08% | -0.71% | 0.24x | 17.9 | 2026-11-26T23:11:20.825659+00:00 | Not calibrated | WEAK 30/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | SOL/USD | 70.94 | 60.460 | 59.764 | +0.78% | -0.10% | 1.12x | 1.4 | 2026-11-26T23:11:20.825659+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0562805 | 59.730 | 46.074 | +0.57% | -0.27% | 4.23x | 1.3 | 2026-11-26T23:11:20.825659+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 7 | LINK/USD | 9.26 | 57.576 | 70.376 | +2.38% | -0.70% | 0.07x | 2.6 | 2026-11-26T23:11:20.825659+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | HBAR/USD | 0.05398 | 52.557 | 59.133 | +3.61% | -0.20% | 0.44x | 1.9 | 2026-11-26T23:11:20.825659+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | ONDO/USD | 0.28686 | 42.187 | 43.184 | +1.54% | -0.59% | 1.20x | 0.3 | 2026-11-26T23:11:20.825659+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 10 | DOT/USD | 0.6697 | 33.373 | 43.911 | +1.73% | -0.59% | 0.24x | 1.5 | 2026-11-26T23:11:20.825659+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZRO/USD | 72.081 | 1.117 | -0.71% | 0.24x |
| 2 | LTC/USD | 72.061 | 43.89 | -0.32% | 0.46x |
| 3 | LINK/USD | 70.376 | 9.26 | -0.70% | 0.07x |
| 4 | AKT/USD | 67.839 | 0.5021 | -0.52% | 2.76x |
| 5 | SOL/USD | 59.764 | 70.94 | -0.10% | 1.12x |
| 6 | XRP/USD | 59.393 | 0.94336 | -0.40% | 1.52x |
| 7 | HBAR/USD | 59.133 | 0.05398 | -0.20% | 0.44x |
| 8 | XDG/USD | 46.074 | 0.0562805 | -0.27% | 4.23x |
| 9 | DOT/USD | 43.911 | 0.6697 | -0.59% | 0.24x |
| 10 | ONDO/USD | 43.184 | 0.28686 | -0.59% | 1.20x |

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

- Persisted scans: 1926; predictions: 16845; observations: 1166611.
- Matured sampled outcomes across 1/6/24/48h: 36752; gap abstentions: 25337. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 149 (sampled only; not a success-rate estimate).
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

**Writer:** 45909232183 · **Generation:** 1926 · **Legacy run:** 45909232183
**Main quote time:** 2026-11-26T23:11:27.514474+00:00 · **Legacy report time:** 2026-11-26T23:12:13.535691+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD | 0.5021 | 80.26 | -0.52% | 2.76x | MODERATE 65/100 | VERY_HIGH 72/100 | Watch |
| 2 | LTC/USD | 43.89 | 65.04 | -0.32% | 0.46x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 3 | XRP/USD | 0.94336 | 62.59 | -0.40% | 1.52x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 4 | ZRO/USD | 1.117 | 60.91 | -0.71% | 0.24x | WEAK 30/100 | EXTREME 87/100 | Do nothing |
| 5 | SOL/USD | 70.94 | 60.46 | -0.10% | 1.12x | WEAK 40/100 | HIGH 68/100 | Watch |
| 6 | XDG/USD | 0.0562805 | 59.73 | -0.27% | 4.23x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 7 | LINK/USD | 9.26 | 57.58 | -0.70% | 0.07x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | HBAR/USD | 0.05398 | 52.56 | -0.20% | 0.44x | WEAK 31/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | ONDO/USD | 0.28686 | 42.19 | -0.59% | 1.20x | WEAK 31/100 | VERY_HIGH 73/100 | Do nothing |
| 10 | DOT/USD | 0.6697 | 33.37 | -0.59% | 0.24x | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing |

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
