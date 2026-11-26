# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T15:31:17.647786+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45849617666
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ad87e4d14100184a7aac30491cc7ad939757e58a (atomic ledger/results publication)
**Ledger generation:** 1879 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 592; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZRO/USD | 1.078 | 86.001 | 66.556 | +5.27% | +1.60% | 2.14x | 18.6 | 2026-11-26T15:31:08.985299+00:00 | Not calibrated | STRONG 93/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | LTC/USD | 43.22 | 76.855 | 61.044 | +1.19% | +0.16% | 4.20x | 4.6 | 2026-11-26T15:31:08.985299+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ADA/USD | 0.147277 | 76.320 | 59.860 | +1.03% | +0.29% | 13.01x | 4.8 | 2026-11-26T15:31:08.985299+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | XRP/USD | 0.94105 | 74.395 | 57.984 | +0.48% | +0.28% | 8.00x | 0.7 | 2026-11-26T15:31:08.985299+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | SKY/USD | 0.04624 | 73.382 | 76.281 | +10.41% | +0.48% | 0.47x | 6.5 | 2026-11-26T15:31:08.985299+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | HBAR/USD | 0.05326 | 66.873 | 50.179 | +2.23% | +0.34% | 2.59x | 3.8 | 2026-11-26T15:31:08.985299+00:00 | Not calibrated | STRONG 88/100 | HIGH 60/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0561971 | 65.966 | 50.034 | +0.43% | +0.19% | 6.21x | 0.5 | 2026-11-26T15:31:08.985299+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 8 | WIF/USD | 0.1333 | 64.282 | 60.508 | +4.71% | +0.53% | 1.11x | 7.5 | 2026-11-26T15:31:08.985299+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 9 | STBL/USD | 0.020439 | 61.075 | 64.889 | +8.22% | +0.43% | 0.40x | 22.0 | 2026-11-26T15:31:08.985299+00:00 | Not calibrated | MODERATE 51/100 | EXTREME 94/100 | Do nothing | WATCH |
| 10 | FET/USD | 0.1139 | 58.614 | 59.494 | +4.98% | +0.26% | 0.78x | 17.6 | 2026-11-26T15:31:08.985299+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 11 | DCR/USD | 10.593 | 51.936 | 37.219 | +0.98% | -0.06% | 5.07x | 0.9 | 2026-11-26T15:31:08.985299+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 12 | DRV/USD | 0.35906 | 49.585 | 32.584 | +0.35% | +0.40% | 12.06x | 11.7 | 2026-11-26T15:31:08.985299+00:00 | Not calibrated | STRONG 75/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 76.281 | 0.04624 | +0.48% | 0.47x |
| 2 | ZRO/USD | 66.556 | 1.078 | +1.60% | 2.14x |
| 3 | STBL/USD | 64.889 | 0.020439 | +0.43% | 0.40x |
| 4 | LTC/USD | 61.044 | 43.22 | +0.16% | 4.20x |
| 5 | WIF/USD | 60.508 | 0.1333 | +0.53% | 1.11x |
| 6 | ADA/USD | 59.860 | 0.147277 | +0.29% | 13.01x |
| 7 | FET/USD | 59.494 | 0.1139 | +0.26% | 0.78x |
| 8 | XRP/USD | 57.984 | 0.94105 | +0.28% | 8.00x |
| 9 | HBAR/USD | 50.179 | 0.05326 | +0.34% | 2.59x |
| 10 | XDG/USD | 50.034 | 0.0561971 | +0.19% | 6.21x |
| 11 | DCR/USD | 37.219 | 10.593 | -0.06% | 5.07x |
| 12 | DRV/USD | 32.584 | 0.35906 | +0.40% | 12.06x |

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

- Persisted scans: 1879; predictions: 16283; observations: 1138557.
- Matured sampled outcomes across 1/6/24/48h: 35210; gap abstentions: 24994. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45849617666 · **Generation:** 1879 · **Legacy run:** 45849617666
**Main quote time:** 2026-11-26T15:31:17.647786+00:00 · **Legacy report time:** 2026-11-26T15:32:28.763050+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD ⭐ | 1.078 | 86.00 | +1.60% | 2.14x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | LTC/USD | 43.22 | 76.85 | +0.16% | 4.20x | STRONG 83/100 | HIGH 55/100 | Watch |
| 3 | ADA/USD | 0.147277 | 76.32 | +0.29% | 13.01x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 4 | XRP/USD | 0.94105 | 74.40 | +0.28% | 8.00x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 5 | SKY/USD | 0.04624 | 73.38 | +0.48% | 0.47x | MODERATE 67/100 | VERY_HIGH 75/100 | Watch |
| 6 | HBAR/USD | 0.05326 | 66.87 | +0.34% | 2.59x | STRONG 88/100 | HIGH 60/100 | Watch |
| 7 | XDG/USD | 0.0561971 | 65.97 | +0.19% | 6.21x | STRONG 78/100 | HIGH 55/100 | Watch |
| 8 | WIF/USD ⭐ | 0.1333 | 64.28 | +0.53% | 1.11x | STRONG 77/100 | VERY_HIGH 74/100 | Watch |
| 9 | STBL/USD | 0.020439 | 61.07 | +0.43% | 0.40x | MODERATE 51/100 | EXTREME 94/100 | Do nothing |
| 10 | FET/USD | 0.1139 | 58.61 | +0.26% | 0.78x | MODERATE 54/100 | VERY_HIGH 73/100 | Watch |
| 11 | DCR/USD | 10.593 | 51.94 | -0.06% | 5.07x | MODERATE 56/100 | VERY_HIGH 73/100 | Watch |
| 12 | DRV/USD | 0.35906 | 49.59 | +0.40% | 12.06x | STRONG 75/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD ⭐ | 1.078 | 84.72 | +1.60% | 2.14x | 2992 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | AKT/USD | 0.4906 | 77.57 | +0.51% | 3.50x | 2978 | STRONG 89/100 | HIGH 66/100 | Consider small entry |
| 3 | SEI/USD | 0.03739 | 77.09 | +1.53% | 1.03x | 5089 | MODERATE 69/100 | VERY_HIGH 73/100 | Watch |
| 4 | WIF/USD ⭐ | 0.1331 | 61.77 | +0.53% | 1.11x | 1317 | STRONG 76/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** ZRO/USD, WIF/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
