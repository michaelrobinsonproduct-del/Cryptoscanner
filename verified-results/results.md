# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T08:21:53.180743+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45964784941
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f1bf50adb7821b6b64d266aeef9c86a5d392c637 (atomic ledger/results publication)
**Ledger generation:** 1982 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 749.48 | 95.189 | 96.060 | +9.95% | +1.11% | 0.36x | 7.9 | 2026-11-27T08:21:47.003361+00:00 | Not calibrated | STRONG 78/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | ADA/USD | 0.153478 | 90.310 | 73.833 | +3.38% | +0.30% | 2.90x | 4.2 | 2026-11-27T08:21:47.003361+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | HYPE/USD | 65.75 | 88.691 | 93.953 | +5.67% | +0.41% | 0.27x | 1.5 | 2026-11-27T08:21:47.003361+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | XBT/USD | 61893.1 | 86.760 | 71.134 | +2.31% | +0.49% | 2.32x | 0.0 | 2026-11-27T08:21:47.003361+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | XRP/USD | 0.98322 | 86.453 | 84.999 | +4.29% | +0.76% | 0.77x | 0.1 | 2026-11-27T08:21:47.003361+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 6 | SOL/USD | 73.4 | 85.633 | 77.911 | +3.47% | +0.25% | 1.65x | 2.7 | 2026-11-27T08:21:47.003361+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | XDG/USD | 0.0583683 | 82.563 | 70.546 | +3.54% | +0.51% | 1.95x | 2.3 | 2026-11-27T08:21:47.003361+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | LINK/USD | 9.62634 | 82.081 | 79.210 | +3.86% | +0.29% | 1.14x | 5.6 | 2026-11-27T08:21:47.003361+00:00 | Not calibrated | STRONG 76/100 | HIGH 62/100 | Watch | WATCH |
| 9 | W/USD | 0.00965 | 80.425 | 73.588 | +9.53% | +2.30% | 0.54x | 10.4 | 2026-11-27T08:21:47.003361+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | UNI/USD | 4.9101 | 78.421 | 80.966 | +5.59% | +0.64% | 0.43x | 5.3 | 2026-11-27T08:21:47.003361+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | PAXG/USD | 3662.12 | 76.557 | 59.856 | +2.96% | +0.34% | 16.49x | 1.2 | 2026-11-27T08:21:47.003361+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 12 | ETH/USD | 1736.33 | 74.108 | 75.150 | +2.88% | +0.36% | 0.72x | 0.1 | 2026-11-27T08:21:47.003361+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.060 | 749.48 | +1.11% | 0.36x |
| 2 | HYPE/USD | 93.953 | 65.75 | +0.41% | 0.27x |
| 3 | XRP/USD | 84.999 | 0.98322 | +0.76% | 0.77x |
| 4 | UNI/USD | 80.966 | 4.9101 | +0.64% | 0.43x |
| 5 | LINK/USD | 79.210 | 9.62634 | +0.29% | 1.14x |
| 6 | SOL/USD | 77.911 | 73.4 | +0.25% | 1.65x |
| 7 | ETH/USD | 75.150 | 1736.33 | +0.36% | 0.72x |
| 8 | ADA/USD | 73.833 | 0.153478 | +0.30% | 2.90x |
| 9 | W/USD | 73.588 | 0.00965 | +2.30% | 0.54x |
| 10 | XBT/USD | 71.134 | 61893.1 | +0.49% | 2.32x |
| 11 | XDG/USD | 70.546 | 0.0583683 | +0.51% | 1.95x |
| 12 | PAXG/USD | 59.856 | 3662.12 | +0.34% | 16.49x |

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

- Persisted scans: 1982; predictions: 17486; observations: 1200299.
- Matured sampled outcomes across 1/6/24/48h: 38693; gap abstentions: 25676. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45964784941 · **Generation:** 1982 · **Legacy run:** 45964784941
**Main quote time:** 2026-11-27T08:21:53.180743+00:00 · **Legacy report time:** 2026-11-27T08:22:45.443688+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 749.48 | 95.19 | +1.11% | 0.36x | STRONG 78/100 | VERY_HIGH 70/100 | Watch |
| 2 | ADA/USD ⭐ | 0.153478 | 90.31 | +0.30% | 2.90x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | HYPE/USD | 65.75 | 88.69 | +0.41% | 0.27x | STRONG 74/100 | VERY_HIGH 70/100 | Watch |
| 4 | XBT/USD ⭐ | 61893.1 | 86.76 | +0.49% | 2.32x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | XRP/USD | 0.98322 | 86.45 | +0.76% | 0.77x | STRONG 73/100 | HIGH 62/100 | Watch |
| 6 | SOL/USD ⭐ | 73.4 | 85.63 | +0.25% | 1.65x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 7 | XDG/USD ⭐ | 0.0583683 | 82.56 | +0.51% | 1.95x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 8 | LINK/USD ⭐ | 9.62634 | 82.08 | +0.29% | 1.14x | STRONG 86/100 | HIGH 62/100 | Watch |
| 9 | W/USD | 0.00965 | 80.43 | +2.30% | 0.54x | MODERATE 65/100 | VERY_HIGH 81/100 | Watch |
| 10 | UNI/USD | 4.9101 | 78.42 | +0.64% | 0.43x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 11 | PAXG/USD | 3662.12 | 76.56 | +0.34% | 16.49x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 12 | ETH/USD | 1736.33 | 74.11 | +0.36% | 0.72x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.153478 | 99.28 | +0.30% | 2.90x | 9773 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 73.38 | 93.88 | +0.25% | 1.65x | 33763 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XDG/USD ⭐ | 0.058346 | 93.75 | +0.51% | 1.95x | 5955 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | LINK/USD ⭐ | 9.62818 | 93.26 | +0.29% | 1.14x | 8045 | STRONG 92/100 | HIGH 62/100 | Watch |
| 5 | XBT/USD ⭐ | 61904.7 | 86.61 | +0.49% | 2.32x | 139006 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | INJ/USD | 6.48 | 86.15 | +0.84% | 1.03x | 5043 | STRONG 78/100 | HIGH 62/100 | Watch |
| 7 | PEPE/USD | 3.63e-06 | 84.93 | +0.83% | 1.13x | 5253 | STRONG 77/100 | HIGH 62/100 | Watch |
| 8 | TAO/USD | 188.7756 | 77.28 | +0.44% | 1.47x | 5850 | STRONG 84/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ADA/USD, XBT/USD, SOL/USD, XDG/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
