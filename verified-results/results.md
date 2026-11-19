# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T15:15:21.232718+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44552562452
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** ef2bd815bd6affe268575fc8d68147b9a34e3e9f (atomic ledger/results publication)
**Ledger generation:** 799 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 23.069 | 105.003 | 94.150 | +6.45% | -0.83% | 2.98x | 11.7 | 2026-11-19T15:15:14.342141+00:00 | Not calibrated | STRONG 75/100 | HIGH 67/100 | Watch | WATCH |
| 2 | INJ/USD | 7.285 | 90.732 | 70.811 | +4.35% | +0.98% | 2.73x | 5.5 | 2026-11-19T15:15:14.342141+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | AKT/USD | 0.5531 | 87.211 | 71.035 | +6.78% | +0.24% | 2.92x | 10.9 | 2026-11-19T15:15:14.342141+00:00 | Not calibrated | STRONG 94/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | SENT/USD | 0.021787 | 86.754 | 72.487 | +5.74% | -0.15% | 3.05x | 2.8 | 2026-11-19T15:15:14.342141+00:00 | Not calibrated | STRONG 73/100 | HIGH 66/100 | Watch | WATCH |
| 5 | LIGHTER/USD | 2.962 | 72.258 | 74.032 | +9.14% | +0.34% | 0.65x | 13.6 | 2026-11-19T15:15:14.342141+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | ETH/USD | 1795.24 | 68.585 | 62.688 | +1.15% | +0.01% | 1.58x | 0.8 | 2026-11-19T15:15:14.342141+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 7 | PUMP/USD | 0.002734 | 68.360 | 76.321 | +5.32% | -0.18% | 0.30x | 7.4 | 2026-11-19T15:15:14.342141+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | ZEC/USD | 936.43 | 67.157 | 69.463 | +2.68% | +0.05% | 0.74x | 8.7 | 2026-11-19T15:15:14.342141+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | HYPE/USD | 68.64 | 64.941 | 72.692 | +2.63% | -0.43% | 0.44x | 1.5 | 2026-11-19T15:15:14.342141+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XRP/USD | 0.9841 | 63.201 | 67.183 | +1.83% | -0.08% | 0.64x | 1.3 | 2026-11-19T15:15:14.342141+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | GRASS/USD | 0.4475 | 62.457 | 68.757 | +10.44% | -0.84% | 0.79x | 20.2 | 2026-11-19T15:15:14.342141+00:00 | Not calibrated | WEAK 26/100 | EXTREME 85/100 | Do nothing | WATCH |
| 12 | XBT/USD | 63417.3 | 60.137 | 59.802 | +0.69% | -0.00% | 1.03x | 0.0 | 2026-11-19T15:15:14.342141+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 94.150 | 23.069 | -0.83% | 2.98x |
| 2 | PUMP/USD | 76.321 | 0.002734 | -0.18% | 0.30x |
| 3 | LIGHTER/USD | 74.032 | 2.962 | +0.34% | 0.65x |
| 4 | HYPE/USD | 72.692 | 68.64 | -0.43% | 0.44x |
| 5 | SENT/USD | 72.487 | 0.021787 | -0.15% | 3.05x |
| 6 | AKT/USD | 71.035 | 0.5531 | +0.24% | 2.92x |
| 7 | INJ/USD | 70.811 | 7.285 | +0.98% | 2.73x |
| 8 | ZEC/USD | 69.463 | 936.43 | +0.05% | 0.74x |
| 9 | GRASS/USD | 68.757 | 0.4475 | -0.84% | 0.79x |
| 10 | XRP/USD | 67.183 | 0.9841 | -0.08% | 0.64x |
| 11 | ETH/USD | 62.688 | 1795.24 | +0.01% | 1.58x |
| 12 | XBT/USD | 59.802 | 63417.3 | -0.00% | 1.03x |

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

- Persisted scans: 799; predictions: 6732; observations: 483240.
- Matured sampled outcomes across 1/6/24/48h: 6743; gap abstentions: 15174. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44552562452 · **Generation:** 799 · **Legacy run:** 44552562452
**Main quote time:** 2026-11-19T15:15:21.232718+00:00 · **Legacy report time:** 2026-11-19T15:16:15.216835+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 23.069 | 105.00 | -0.83% | 2.98x | STRONG 75/100 | HIGH 67/100 | Watch |
| 2 | INJ/USD ⭐ | 7.285 | 90.73 | +0.98% | 2.73x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | AKT/USD ⭐ | 0.5531 | 87.21 | +0.24% | 2.92x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 4 | SENT/USD | 0.021787 | 86.75 | -0.15% | 3.05x | STRONG 73/100 | HIGH 66/100 | Watch |
| 5 | LIGHTER/USD | 2.962 | 72.26 | +0.34% | 0.65x | MODERATE 61/100 | VERY_HIGH 81/100 | Watch |
| 6 | ETH/USD | 1795.24 | 68.59 | +0.01% | 1.58x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 7 | PUMP/USD | 0.002734 | 68.36 | -0.18% | 0.30x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 8 | ZEC/USD | 936.43 | 67.16 | +0.05% | 0.74x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 9 | HYPE/USD | 68.64 | 64.94 | -0.43% | 0.44x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 10 | XRP/USD | 0.9841 | 63.20 | -0.08% | 0.64x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 11 | GRASS/USD | 0.4475 | 62.46 | -0.84% | 0.79x | WEAK 26/100 | EXTREME 85/100 | Do nothing |
| 12 | XBT/USD | 63417.3 | 60.14 | -0.00% | 1.03x | WEAK 40/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 7.245 | 89.03 | +0.98% | 2.73x | 6532 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PYTH/USD | 0.05679 | 79.41 | +0.83% | 2.41x | 2645 | STRONG 90/100 | HIGH 66/100 | Consider small entry |
| 3 | AKT/USD ⭐ | 0.5522 | 79.28 | +0.24% | 2.92x | 3096 | STRONG 100/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** INJ/USD, AKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
