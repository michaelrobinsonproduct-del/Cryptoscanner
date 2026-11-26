# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T11:16:25.147087+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45808781006
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d14e6d17f05e810624edac6fc94db11d4bcc805d (atomic ledger/results publication)
**Ledger generation:** 1853 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 11s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 585; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SEI/USD | 0.03627 | 82.105 | 73.331 | +8.89% | +0.44% | 1.66x | 8.3 | 2026-11-26T11:16:14.117709+00:00 | Not calibrated | STRONG 86/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | ADA/USD | 0.14819 | 81.806 | 65.576 | +1.66% | +0.25% | 4.24x | 2.1 | 2026-11-26T11:16:14.117709+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | SKY/USD | 0.0444 | 73.529 | 72.621 | +6.02% | +0.27% | 0.96x | 6.8 | 2026-11-26T11:16:14.117709+00:00 | Not calibrated | MODERATE 67/100 | HIGH 67/100 | Watch | WATCH |
| 4 | BAT/USD | 0.08105 | 69.038 | 50.816 | +2.83% | +0.64% | 11.79x | 2.5 | 2026-11-26T11:16:14.117709+00:00 | Not calibrated | STRONG 90/100 | HIGH 60/100 | Watch | WATCH |
| 5 | LTC/USD | 43.53 | 66.334 | 66.141 | +1.92% | +0.30% | 0.87x | 4.6 | 2026-11-26T11:16:14.117709+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XMR/USD | 518.33 | 65.506 | 51.661 | +0.27% | -0.23% | 4.07x | 10.4 | 2026-11-26T11:16:14.117709+00:00 | Not calibrated | MODERATE 58/100 | HIGH 67/100 | Watch | WATCH |
| 7 | XRP/USD | 0.94931 | 65.274 | 64.477 | +1.36% | +0.05% | 1.06x | 0.1 | 2026-11-26T11:16:14.117709+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 8 | LINK/USD | 9.21365 | 64.654 | 66.652 | +1.87% | +0.24% | 0.68x | 2.9 | 2026-11-26T11:16:14.117709+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | SYRUP/USD | 0.07166 | 63.982 | 68.247 | +8.13% | +0.53% | 0.31x | 18.2 | 2026-11-26T11:16:14.117709+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | INJ/USD | 6.168 | 63.473 | 67.129 | +3.59% | +0.32% | 0.47x | 3.2 | 2026-11-26T11:16:14.117709+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | PENGU/USD | 0.004429 | 60.938 | 44.807 | +1.84% | +0.23% | 3.53x | 2.3 | 2026-11-26T11:16:14.117709+00:00 | Not calibrated | STRONG 85/100 | HIGH 60/100 | Watch | WATCH |
| 12 | FET/USD | 0.1141 | 59.148 | 65.141 | +5.16% | +0.26% | 0.27x | 8.8 | 2026-11-26T11:16:14.117709+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SEI/USD | 73.331 | 0.03627 | +0.44% | 1.66x |
| 2 | SKY/USD | 72.621 | 0.0444 | +0.27% | 0.96x |
| 3 | SYRUP/USD | 68.247 | 0.07166 | +0.53% | 0.31x |
| 4 | INJ/USD | 67.129 | 6.168 | +0.32% | 0.47x |
| 5 | LINK/USD | 66.652 | 9.21365 | +0.24% | 0.68x |
| 6 | LTC/USD | 66.141 | 43.53 | +0.30% | 0.87x |
| 7 | ADA/USD | 65.576 | 0.14819 | +0.25% | 4.24x |
| 8 | FET/USD | 65.141 | 0.1141 | +0.26% | 0.27x |
| 9 | XRP/USD | 64.477 | 0.94931 | +0.05% | 1.06x |
| 10 | XMR/USD | 51.661 | 518.33 | -0.23% | 4.07x |
| 11 | BAT/USD | 50.816 | 0.08105 | +0.64% | 11.79x |
| 12 | PENGU/USD | 44.807 | 0.004429 | +0.23% | 3.53x |

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

- Persisted scans: 1853; predictions: 15971; observations: 1123250.
- Matured sampled outcomes across 1/6/24/48h: 34586; gap abstentions: 24628. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45808781006 · **Generation:** 1853 · **Legacy run:** 45808781006
**Main quote time:** 2026-11-26T11:16:25.147087+00:00 · **Legacy report time:** 2026-11-26T11:17:36.691517+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SEI/USD ⭐ | 0.03627 | 82.10 | +0.44% | 1.66x | STRONG 96/100 | HIGH 60/100 | Consider small entry |
| 2 | ADA/USD ⭐ | 0.14819 | 81.81 | +0.25% | 4.24x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SKY/USD | 0.0444 | 73.53 | +0.27% | 0.96x | MODERATE 67/100 | HIGH 67/100 | Watch |
| 4 | BAT/USD | 0.08105 | 69.04 | +0.64% | 11.79x | STRONG 90/100 | HIGH 60/100 | Watch |
| 5 | LTC/USD | 43.53 | 66.33 | +0.30% | 0.87x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 6 | XMR/USD | 518.33 | 65.51 | -0.23% | 4.07x | MODERATE 58/100 | HIGH 67/100 | Watch |
| 7 | XRP/USD | 0.94931 | 65.27 | +0.05% | 1.06x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 8 | LINK/USD | 9.21365 | 64.65 | +0.24% | 0.68x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 9 | SYRUP/USD | 0.07166 | 63.98 | +0.53% | 0.31x | MODERATE 57/100 | VERY_HIGH 81/100 | Watch |
| 10 | INJ/USD | 6.168 | 63.47 | +0.32% | 0.47x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 11 | PENGU/USD | 0.004429 | 60.94 | +0.23% | 3.53x | STRONG 85/100 | HIGH 60/100 | Watch |
| 12 | FET/USD | 0.1141 | 59.15 | +0.26% | 0.27x | MODERATE 60/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.148336 | 77.55 | +0.25% | 4.24x | 12550 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SEI/USD ⭐ | 0.03622 | 74.93 | +0.44% | 1.66x | 2580 | STRONG 92/100 | HIGH 60/100 | Consider small entry |
| 3 | CC/USD | 0.07931 | 73.29 | +0.15% | 2.57x | 4788 | STRONG 82/100 | HIGH 60/100 | Watch |
| 4 | HBAR/USD | 0.05357 | 68.30 | +0.21% | 1.02x | 6187 | MODERATE 69/100 | HIGH 62/100 | Watch |

**Same-run overlap:** SEI/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
