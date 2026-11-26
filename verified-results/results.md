# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T21:51:14.933800+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45900745254
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 867b67908537733e45fd1a7d9d66973132946f09 (atomic ledger/results publication)
**Ledger generation:** 1918 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.40778 | 97.329 | 81.195 | +4.02% | +0.23% | 9.71x | 3.8 | 2026-11-26T21:51:06.714011+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | HYPE/USD | 63.26 | 84.638 | 72.048 | +2.66% | -0.28% | 2.40x | 3.2 | 2026-11-26T21:51:06.714011+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XRP/USD | 0.95432 | 82.881 | 67.645 | +1.90% | +0.05% | 10.36x | 1.3 | 2026-11-26T21:51:06.714011+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ADA/USD | 0.150519 | 76.485 | 75.512 | +3.26% | -0.22% | 1.21x | 4.6 | 2026-11-26T21:51:06.714011+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 5 | DRV/USD | 0.39383 | 75.026 | 75.277 | +10.07% | +0.62% | 0.66x | 14.7 | 2026-11-26T21:51:06.714011+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | SOL/USD | 71.67 | 74.565 | 67.031 | +1.82% | -0.06% | 1.78x | 1.4 | 2026-11-26T21:51:06.714011+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 7 | INJ/USD | 6.262 | 73.124 | 73.427 | +5.17% | -0.08% | 1.01x | 4.8 | 2026-11-26T21:51:06.714011+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 8 | AKT/USD | 0.5061 | 70.167 | 76.924 | +6.98% | -0.35% | 0.50x | 2.0 | 2026-11-26T21:51:06.714011+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | LTC/USD | 44.14 | 68.915 | 77.304 | +3.35% | -0.02% | 0.17x | 2.3 | 2026-11-26T21:51:06.714011+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | ETH/USD | 1707.62 | 64.910 | 62.097 | +1.02% | -0.02% | 1.29x | 0.1 | 2026-11-26T21:51:06.714011+00:00 | Not calibrated | WEAK 42/100 | HIGH 61/100 | Watch | WATCH |
| 11 | W/USD | 0.00889 | 64.778 | 71.820 | +7.11% | +0.00% | 0.30x | 11.3 | 2026-11-26T21:51:06.714011+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 12 | XBT/USD | 60843.4 | 60.274 | 60.497 | +0.79% | -0.10% | 1.03x | 0.0 | 2026-11-26T21:51:06.714011+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LINK/USD | 81.195 | 9.40778 | +0.23% | 9.71x |
| 2 | LTC/USD | 77.304 | 44.14 | -0.02% | 0.17x |
| 3 | AKT/USD | 76.924 | 0.5061 | -0.35% | 0.50x |
| 4 | ADA/USD | 75.512 | 0.150519 | -0.22% | 1.21x |
| 5 | DRV/USD | 75.277 | 0.39383 | +0.62% | 0.66x |
| 6 | INJ/USD | 73.427 | 6.262 | -0.08% | 1.01x |
| 7 | HYPE/USD | 72.048 | 63.26 | -0.28% | 2.40x |
| 8 | W/USD | 71.820 | 0.00889 | +0.00% | 0.30x |
| 9 | XRP/USD | 67.645 | 0.95432 | +0.05% | 10.36x |
| 10 | SOL/USD | 67.031 | 71.67 | -0.06% | 1.78x |
| 11 | ETH/USD | 62.097 | 1707.62 | -0.02% | 1.29x |
| 12 | XBT/USD | 60.497 | 60843.4 | -0.10% | 1.03x |

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

- Persisted scans: 1918; predictions: 16751; observations: 1161816.
- Matured sampled outcomes across 1/6/24/48h: 36452; gap abstentions: 25288. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45900745254 · **Generation:** 1918 · **Legacy run:** 45900745254
**Main quote time:** 2026-11-26T21:51:14.933800+00:00 · **Legacy report time:** 2026-11-26T21:51:57.228559+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.40778 | 97.33 | +0.23% | 9.71x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | HYPE/USD | 63.26 | 84.64 | -0.28% | 2.40x | STRONG 72/100 | HIGH 61/100 | Watch |
| 3 | XRP/USD | 0.95432 | 82.88 | +0.05% | 10.36x | STRONG 86/100 | HIGH 55/100 | Watch |
| 4 | ADA/USD | 0.150519 | 76.48 | -0.22% | 1.21x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 5 | DRV/USD | 0.39383 | 75.03 | +0.62% | 0.66x | MODERATE 63/100 | VERY_HIGH 76/100 | Watch |
| 6 | SOL/USD | 71.67 | 74.56 | -0.06% | 1.78x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 7 | INJ/USD | 6.262 | 73.12 | -0.08% | 1.01x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 8 | AKT/USD | 0.5061 | 70.17 | -0.35% | 0.50x | WEAK 40/100 | VERY_HIGH 81/100 | Watch |
| 9 | LTC/USD | 44.14 | 68.92 | -0.02% | 0.17x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 10 | ETH/USD | 1707.62 | 64.91 | -0.02% | 1.29x | WEAK 42/100 | HIGH 61/100 | Watch |
| 11 | W/USD | 0.00889 | 64.78 | +0.00% | 0.30x | MODERATE 47/100 | VERY_HIGH 81/100 | Watch |
| 12 | XBT/USD | 60843.4 | 60.27 | -0.10% | 1.03x | WEAK 40/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.39671 | 100.00 | +0.23% | 9.71x | 6816 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SYRUP/USD | 0.07147 | 73.34 | +0.42% | 1.24x | 3163 | MODERATE 67/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
