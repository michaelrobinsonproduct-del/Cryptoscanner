# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T23:21:20.682917+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45910257251
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 13df63e7aa14332e402c15ca2e30ce158920542c (atomic ledger/results publication)
**Ledger generation:** 1927 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.24756 | 81.812 | 68.698 | +2.24% | -0.38% | 3.07x | 4.0 | 2026-11-26T23:21:12.467043+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ALGO/USD | 0.08103 | 72.637 | 59.483 | +3.76% | -0.37% | 5.47x | 3.7 | 2026-11-26T23:21:12.467043+00:00 | Not calibrated | MODERATE 66/100 | HIGH 66/100 | Watch | WATCH |
| 3 | SOL/USD | 70.81 | 66.142 | 58.471 | +0.60% | -0.44% | 1.99x | 1.4 | 2026-11-26T23:21:12.467043+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XRP/USD | 0.94143 | 65.313 | 58.587 | +0.52% | -0.48% | 1.91x | 0.1 | 2026-11-26T23:21:12.467043+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ZRO/USD | 1.121 | 62.313 | 71.707 | +9.47% | -0.27% | 0.19x | 17.9 | 2026-11-26T23:21:12.467043+00:00 | Not calibrated | WEAK 31/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | LTC/USD | 43.73 | 61.837 | 70.575 | +2.39% | -0.50% | 0.38x | 2.3 | 2026-11-26T23:21:12.467043+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | FET/USD | 0.1193 | 59.545 | 66.161 | +9.95% | -0.67% | 0.67x | 25.2 | 2026-11-26T23:21:12.467043+00:00 | Not calibrated | WEAK 25/100 | EXTREME 93/100 | Do nothing | WATCH |
| 8 | XDG/USD | 0.0562554 | 59.261 | 45.716 | +0.53% | -0.27% | 2.49x | 1.4 | 2026-11-26T23:21:12.467043+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 9 | ONDO/USD | 0.28608 | 54.238 | 40.926 | +1.27% | -0.34% | 4.90x | 1.0 | 2026-11-26T23:21:12.467043+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |
| 10 | HYPE/USD | 61.88 | 52.084 | 56.338 | +0.42% | -0.80% | 0.98x | 3.2 | 2026-11-26T23:21:12.467043+00:00 | Not calibrated | WEAK 31/100 | HIGH 68/100 | Do nothing | WATCH |
| 11 | DOT/USD | 0.6687 | 33.830 | 42.846 | +1.58% | -0.55% | 0.37x | 1.5 | 2026-11-26T23:21:12.467043+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZRO/USD | 71.707 | 1.121 | -0.27% | 0.19x |
| 2 | LTC/USD | 70.575 | 43.73 | -0.50% | 0.38x |
| 3 | LINK/USD | 68.698 | 9.24756 | -0.38% | 3.07x |
| 4 | FET/USD | 66.161 | 0.1193 | -0.67% | 0.67x |
| 5 | ALGO/USD | 59.483 | 0.08103 | -0.37% | 5.47x |
| 6 | XRP/USD | 58.587 | 0.94143 | -0.48% | 1.91x |
| 7 | SOL/USD | 58.471 | 70.81 | -0.44% | 1.99x |
| 8 | HYPE/USD | 56.338 | 61.88 | -0.80% | 0.98x |
| 9 | XDG/USD | 45.716 | 0.0562554 | -0.27% | 2.49x |
| 10 | DOT/USD | 42.846 | 0.6687 | -0.55% | 0.37x |
| 11 | ONDO/USD | 40.926 | 0.28608 | -0.34% | 4.90x |

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

- Persisted scans: 1927; predictions: 16856; observations: 1167212.
- Matured sampled outcomes across 1/6/24/48h: 36788; gap abstentions: 25344. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 149 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45910257251 · **Generation:** 1927 · **Legacy run:** 45910257251
**Main quote time:** 2026-11-26T23:21:20.682917+00:00 · **Legacy report time:** 2026-11-26T23:22:09.976254+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD | 9.24756 | 81.81 | -0.38% | 3.07x | STRONG 71/100 | HIGH 61/100 | Watch |
| 2 | ALGO/USD | 0.08103 | 72.64 | -0.37% | 5.47x | MODERATE 66/100 | HIGH 66/100 | Watch |
| 3 | SOL/USD | 70.81 | 66.14 | -0.44% | 1.99x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 4 | XRP/USD | 0.94143 | 65.31 | -0.48% | 1.91x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 5 | ZRO/USD | 1.121 | 62.31 | -0.27% | 0.19x | WEAK 31/100 | EXTREME 87/100 | Do nothing |
| 6 | LTC/USD | 43.73 | 61.84 | -0.50% | 0.38x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 7 | FET/USD | 0.1193 | 59.55 | -0.67% | 0.67x | WEAK 25/100 | EXTREME 93/100 | Do nothing |
| 8 | XDG/USD | 0.0562554 | 59.26 | -0.27% | 2.49x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 9 | ONDO/USD | 0.28608 | 54.24 | -0.34% | 4.90x | MODERATE 57/100 | HIGH 66/100 | Watch |
| 10 | HYPE/USD | 61.88 | 52.08 | -0.80% | 0.98x | WEAK 31/100 | HIGH 68/100 | Do nothing |
| 11 | DOT/USD | 0.6687 | 33.83 | -0.55% | 0.37x | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing |

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
