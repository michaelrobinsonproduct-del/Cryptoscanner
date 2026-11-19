# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T06:15:23.100235+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44470729824
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 60a44b28362495bb69a184a5400cd0889e667d13 (atomic ledger/results publication)
**Ledger generation:** 774 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LIGHTER/USD | 2.917 | 98.075 | 73.037 | +7.48% | +3.07% | 1.97x | 17.2 | 2026-11-19T06:15:17.185593+00:00 | Not calibrated | STRONG 89/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | VVV/USD | 23.023 | 88.493 | 89.085 | +6.24% | +0.89% | 0.50x | 18.7 | 2026-11-19T06:15:17.185593+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | ZEC/USD | 941 | 80.980 | 75.496 | +3.19% | +0.23% | 1.43x | 3.6 | 2026-11-19T06:15:17.185593+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.3926 | 69.621 | 72.119 | +2.89% | +0.44% | 0.53x | 6.2 | 2026-11-19T06:15:17.185593+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ETH/USD | 1801.14 | 68.489 | 65.377 | +1.49% | +0.15% | 1.23x | 0.1 | 2026-11-19T06:15:17.185593+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 6 | INJ/USD | 7.121 | 68.318 | 55.060 | +2.01% | +1.45% | 1.60x | 1.4 | 2026-11-19T06:15:17.185593+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SOL/USD | 74.8 | 68.241 | 66.325 | +1.71% | +0.20% | 1.09x | 1.3 | 2026-11-19T06:15:17.185593+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 8 | INFI/USD | 0.1209 | 66.763 | 66.411 | +6.24% | -0.08% | 1.08x | 16.6 | 2026-11-19T06:15:17.185593+00:00 | Not calibrated | WEAK 38/100 | EXTREME 86/100 | Do nothing | WATCH |
| 9 | TRX/USD | 0.312557 | 64.678 | 49.030 | +1.06% | +0.13% | 32.54x | 0.0 | 2026-11-19T06:15:17.185593+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 10 | HYPE/USD | 68.06 | 59.620 | 65.881 | +1.76% | -0.03% | 0.39x | 2.9 | 2026-11-19T06:15:17.185593+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | XRP/USD | 0.9758 | 58.127 | 61.779 | +0.98% | +0.23% | 0.52x | 0.1 | 2026-11-19T06:15:17.185593+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XBT/USD | 63418.6 | 54.728 | 59.817 | +0.69% | +0.17% | 0.41x | 0.0 | 2026-11-19T06:15:17.185593+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 89.085 | 23.023 | +0.89% | 0.50x |
| 2 | ZEC/USD | 75.496 | 941 | +0.23% | 1.43x |
| 3 | LIGHTER/USD | 73.037 | 2.917 | +3.07% | 1.97x |
| 4 | NEAR/USD | 72.119 | 3.3926 | +0.44% | 0.53x |
| 5 | INFI/USD | 66.411 | 0.1209 | -0.08% | 1.08x |
| 6 | SOL/USD | 66.325 | 74.8 | +0.20% | 1.09x |
| 7 | HYPE/USD | 65.881 | 68.06 | -0.03% | 0.39x |
| 8 | ETH/USD | 65.377 | 1801.14 | +0.15% | 1.23x |
| 9 | XRP/USD | 61.779 | 0.9758 | +0.23% | 0.52x |
| 10 | XBT/USD | 59.817 | 63418.6 | +0.17% | 0.41x |
| 11 | INJ/USD | 55.060 | 7.121 | +1.45% | 1.60x |
| 12 | TRX/USD | 49.030 | 0.312557 | +0.13% | 32.54x |

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

- Persisted scans: 774; predictions: 6432; observations: 468372.
- Matured sampled outcomes across 1/6/24/48h: 6488; gap abstentions: 13827. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44470729824 · **Generation:** 774 · **Legacy run:** 44470729824
**Main quote time:** 2026-11-19T06:15:23.100235+00:00 · **Legacy report time:** 2026-11-19T06:16:14.530592+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LIGHTER/USD ⭐ | 2.917 | 98.08 | +3.07% | 1.97x | STRONG 99/100 | VERY_HIGH 76/100 | Watch |
| 2 | VVV/USD | 23.023 | 88.49 | +0.89% | 0.50x | MODERATE 69/100 | VERY_HIGH 76/100 | Watch |
| 3 | ZEC/USD ⭐ | 941 | 80.98 | +0.23% | 1.43x | STRONG 95/100 | HIGH 55/100 | Watch |
| 4 | NEAR/USD | 3.3926 | 69.62 | +0.44% | 0.53x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 5 | ETH/USD ⭐ | 1801.14 | 68.49 | +0.15% | 1.23x | MODERATE 69/100 | HIGH 62/100 | Watch |
| 6 | INJ/USD | 7.121 | 68.32 | +1.45% | 1.60x | STRONG 79/100 | HIGH 55/100 | Watch |
| 7 | SOL/USD ⭐ | 74.8 | 68.24 | +0.20% | 1.09x | STRONG 79/100 | HIGH 62/100 | Watch |
| 8 | INFI/USD | 0.1209 | 66.76 | -0.08% | 1.08x | WEAK 38/100 | EXTREME 86/100 | Do nothing |
| 9 | TRX/USD | 0.312557 | 64.68 | +0.13% | 32.54x | STRONG 77/100 | HIGH 55/100 | Watch |
| 10 | HYPE/USD | 68.06 | 59.62 | -0.03% | 0.39x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 11 | XRP/USD | 0.9758 | 58.13 | +0.23% | 0.52x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 12 | XBT/USD | 63418.6 | 54.73 | +0.17% | 0.41x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 943.31 | 90.17 | +0.23% | 1.43x | 22461 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | LIGHTER/USD ⭐ | 2.912 | 85.83 | +3.07% | 1.97x | 4208 | STRONG 88/100 | VERY_HIGH 82/100 | Watch |
| 3 | AKT/USD | 0.5389 | 79.39 | +0.09% | 3.47x | 3452 | STRONG 85/100 | HIGH 67/100 | Watch |
| 4 | SOL/USD ⭐ | 74.82 | 71.18 | +0.20% | 1.09x | 35227 | STRONG 81/100 | HIGH 62/100 | Watch |
| 5 | ETH/USD ⭐ | 1801.09 | 71.09 | +0.15% | 1.23x | 58317 | STRONG 71/100 | HIGH 62/100 | Watch |

**Same-run overlap:** LIGHTER/USD, ZEC/USD, ETH/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
