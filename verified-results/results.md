# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T19:12:52.321077+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45881510943
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2aa224a1b4d03e802c086f911ce60b47917fcff5 (atomic ledger/results publication)
**Ledger generation:** 1901 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 597; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZRO/USD | 1.125 | 98.501 | 72.799 | +9.86% | +2.19% | 2.48x | 17.8 | 2026-11-26T19:12:44.365845+00:00 | Not calibrated | STRONG 99/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | FET/USD | 0.1209 | 92.023 | 70.295 | +11.43% | +1.35% | 4.47x | 16.6 | 2026-11-26T19:12:44.365845+00:00 | Not calibrated | STRONG 96/100 | HIGH 66/100 | Consider small entry | WATCH |
| 3 | ADA/USD | 0.150401 | 89.045 | 75.409 | +3.18% | +0.06% | 2.33x | 3.7 | 2026-11-26T19:12:44.365845+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 4 | AKT/USD | 0.5059 | 88.505 | 73.110 | +6.93% | +0.08% | 3.50x | 9.9 | 2026-11-26T19:12:44.365845+00:00 | Not calibrated | STRONG 89/100 | HIGH 60/100 | Watch | WATCH |
| 5 | INJ/USD | 6.258 | 83.739 | 72.543 | +5.11% | +0.99% | 1.63x | 6.4 | 2026-11-26T19:12:44.365845+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | DRV/USD | 0.39732 | 75.826 | 72.112 | +11.05% | +0.87% | 0.94x | 19.4 | 2026-11-26T19:12:44.365845+00:00 | Not calibrated | MODERATE 63/100 | HIGH 68/100 | Watch | WATCH |
| 7 | WIF/USD | 0.1403 | 72.728 | 73.197 | +10.21% | -0.64% | 1.27x | 7.1 | 2026-11-26T19:12:44.365845+00:00 | Not calibrated | MODERATE 46/100 | HIGH 66/100 | Watch | WATCH |
| 8 | HYPE/USD | 62.02 | 72.586 | 58.737 | +0.65% | +1.14% | 1.81x | 1.6 | 2026-11-26T19:12:44.365845+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | SKY/USD | 0.0452 | 68.718 | 74.225 | +7.93% | -0.92% | 0.91x | 11.1 | 2026-11-26T19:12:44.365845+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 10 | LINK/USD | 9.26288 | 68.218 | 69.283 | +2.41% | +0.15% | 0.82x | 2.7 | 2026-11-26T19:12:44.365845+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 11 | SOL/USD | 71.31 | 62.578 | 63.448 | +1.31% | +0.04% | 0.89x | 1.4 | 2026-11-26T19:12:44.365845+00:00 | Not calibrated | MODERATE 51/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XRP/USD | 0.95359 | 60.924 | 67.466 | +1.82% | -0.04% | 0.37x | 0.5 | 2026-11-26T19:12:44.365845+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ADA/USD | 75.409 | 0.150401 | +0.06% | 2.33x |
| 2 | SKY/USD | 74.225 | 0.0452 | -0.92% | 0.91x |
| 3 | WIF/USD | 73.197 | 0.1403 | -0.64% | 1.27x |
| 4 | AKT/USD | 73.110 | 0.5059 | +0.08% | 3.50x |
| 5 | ZRO/USD | 72.799 | 1.125 | +2.19% | 2.48x |
| 6 | INJ/USD | 72.543 | 6.258 | +0.99% | 1.63x |
| 7 | DRV/USD | 72.112 | 0.39732 | +0.87% | 0.94x |
| 8 | FET/USD | 70.295 | 0.1209 | +1.35% | 4.47x |
| 9 | LINK/USD | 69.283 | 9.26288 | +0.15% | 0.82x |
| 10 | XRP/USD | 67.466 | 0.95359 | -0.04% | 0.37x |
| 11 | SOL/USD | 63.448 | 71.31 | +0.04% | 0.89x |
| 12 | HYPE/USD | 58.737 | 62.02 | +1.14% | 1.81x |

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

- Persisted scans: 1901; predictions: 16547; observations: 1151638.
- Matured sampled outcomes across 1/6/24/48h: 35864; gap abstentions: 25180. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45881510943 · **Generation:** 1901 · **Legacy run:** 45881510943
**Main quote time:** 2026-11-26T19:12:52.321077+00:00 · **Legacy report time:** 2026-11-26T19:13:43.640341+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD ⭐ | 1.125 | 98.50 | +2.19% | 2.48x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | FET/USD | 0.1209 | 92.02 | +1.35% | 4.47x | STRONG 96/100 | HIGH 66/100 | Consider small entry |
| 3 | ADA/USD ⭐ | 0.150401 | 89.04 | +0.06% | 2.33x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | AKT/USD ⭐ | 0.5059 | 88.51 | +0.08% | 3.50x | STRONG 99/100 | HIGH 60/100 | Watch |
| 5 | INJ/USD ⭐ | 6.258 | 83.74 | +0.99% | 1.63x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 6 | DRV/USD | 0.39732 | 75.83 | +0.87% | 0.94x | MODERATE 63/100 | HIGH 68/100 | Watch |
| 7 | WIF/USD | 0.1403 | 72.73 | -0.64% | 1.27x | MODERATE 46/100 | HIGH 66/100 | Watch |
| 8 | HYPE/USD | 62.02 | 72.59 | +1.14% | 1.81x | STRONG 81/100 | HIGH 55/100 | Consider small entry |
| 9 | SKY/USD | 0.0452 | 68.72 | -0.92% | 0.91x | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing |
| 10 | LINK/USD | 9.26288 | 68.22 | +0.15% | 0.82x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 11 | SOL/USD | 71.31 | 62.58 | +0.04% | 0.89x | MODERATE 51/100 | HIGH 62/100 | Watch |
| 12 | XRP/USD | 0.95359 | 60.92 | -0.04% | 0.37x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD ⭐ | 0.5068 | 91.12 | +0.08% | 3.50x | 2693 | STRONG 100/100 | HIGH 60/100 | Watch |
| 2 | ADA/USD ⭐ | 0.150319 | 85.65 | +0.06% | 2.33x | 10545 | STRONG 98/100 | HIGH 55/100 | Watch |
| 3 | INJ/USD ⭐ | 6.258 | 83.66 | +0.99% | 1.63x | 5566 | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 4 | ZRO/USD ⭐ | 1.121 | 83.16 | +2.19% | 2.48x | 2242 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZRO/USD, ADA/USD, AKT/USD, INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
