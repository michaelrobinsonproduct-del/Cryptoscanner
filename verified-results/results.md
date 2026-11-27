# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T02:11:26.557409+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45926670735
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** af67f13a17f908d6ca7d6c37bff67def40c69492 (atomic ledger/results publication)
**Ledger generation:** 1944 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 718.18 | 111.981 | 85.401 | +5.36% | +3.26% | 2.03x | 14.2 | 2026-11-27T02:11:19.772639+00:00 | Not calibrated | STRONG 100/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0977 | 87.731 | 64.177 | +1.63% | +1.71% | 3.14x | 4.5 | 2026-11-27T02:11:19.772639+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ETH/USD | 1713.72 | 86.361 | 64.342 | +1.54% | +1.40% | 3.47x | 2.9 | 2026-11-27T02:11:19.772639+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SOL/USD | 72.09 | 81.292 | 65.654 | +1.62% | +1.46% | 1.83x | 1.4 | 2026-11-27T02:11:19.772639+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | XRP/USD | 0.95503 | 81.212 | 64.066 | +1.30% | +1.22% | 2.10x | 0.1 | 2026-11-27T02:11:19.772639+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | ADA/USD | 0.150488 | 80.548 | 59.902 | +1.37% | +1.13% | 3.77x | 4.7 | 2026-11-27T02:11:19.772639+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | HYPE/USD | 63.58 | 79.165 | 69.514 | +2.19% | +1.96% | 0.98x | 1.6 | 2026-11-27T02:11:19.772639+00:00 | Not calibrated | STRONG 70/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XMR/USD | 467.43 | 77.549 | 67.951 | +2.29% | +1.34% | 1.29x | 6.2 | 2026-11-27T02:11:19.772639+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 9 | XBT/USD | 61177.2 | 77.505 | 62.851 | +1.12% | +1.32% | 1.81x | 0.0 | 2026-11-27T02:11:19.772639+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | LINK/USD | 9.42532 | 71.625 | 65.045 | +1.69% | +1.40% | 0.96x | 3.6 | 2026-11-27T02:11:19.772639+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 11 | PAXG/USD | 3611.53 | 68.883 | 49.544 | +1.54% | +0.87% | 15.74x | 0.8 | 2026-11-27T02:11:19.772639+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 12 | LTC/USD | 44.36 | 67.076 | 61.626 | +1.42% | +0.98% | 1.06x | 4.5 | 2026-11-27T02:11:19.772639+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 85.401 | 718.18 | +3.26% | 2.03x |
| 2 | HYPE/USD | 69.514 | 63.58 | +1.96% | 0.98x |
| 3 | XMR/USD | 67.951 | 467.43 | +1.34% | 1.29x |
| 4 | SOL/USD | 65.654 | 72.09 | +1.46% | 1.83x |
| 5 | LINK/USD | 65.045 | 9.42532 | +1.40% | 0.96x |
| 6 | ETH/USD | 64.342 | 1713.72 | +1.40% | 3.47x |
| 7 | NEAR/USD | 64.177 | 3.0977 | +1.71% | 3.14x |
| 8 | XRP/USD | 64.066 | 0.95503 | +1.22% | 2.10x |
| 9 | XBT/USD | 62.851 | 61177.2 | +1.32% | 1.81x |
| 10 | LTC/USD | 61.626 | 44.36 | +0.98% | 1.06x |
| 11 | ADA/USD | 59.902 | 0.150488 | +1.13% | 3.77x |
| 12 | PAXG/USD | 49.544 | 3611.53 | +0.87% | 15.74x |

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

- Persisted scans: 1944; predictions: 17030; observations: 1177429.
- Matured sampled outcomes across 1/6/24/48h: 37361; gap abstentions: 25449. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45926670735 · **Generation:** 1944 · **Legacy run:** 45926670735
**Main quote time:** 2026-11-27T02:11:26.557409+00:00 · **Legacy report time:** 2026-11-27T02:12:19.307892+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 718.18 | 111.98 | +3.26% | 2.03x | STRONG 100/100 | VERY_HIGH 71/100 | Watch |
| 2 | NEAR/USD ⭐ | 3.0977 | 87.73 | +1.71% | 3.14x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ETH/USD ⭐ | 1713.72 | 86.36 | +1.40% | 3.47x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 72.09 | 81.29 | +1.46% | 1.83x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 5 | XRP/USD ⭐ | 0.95503 | 81.21 | +1.22% | 2.10x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | ADA/USD ⭐ | 0.150488 | 80.55 | +1.13% | 3.77x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | HYPE/USD | 63.58 | 79.16 | +1.96% | 0.98x | STRONG 70/100 | HIGH 62/100 | Watch |
| 8 | XMR/USD ⭐ | 467.43 | 77.55 | +1.34% | 1.29x | STRONG 84/100 | HIGH 55/100 | Watch |
| 9 | XBT/USD ⭐ | 61177.2 | 77.50 | +1.32% | 1.81x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 10 | LINK/USD | 9.42532 | 71.62 | +1.40% | 0.96x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 11 | PAXG/USD | 3611.53 | 68.88 | +0.87% | 15.74x | STRONG 89/100 | HIGH 55/100 | Watch |
| 12 | LTC/USD ⭐ | 44.36 | 67.08 | +0.98% | 1.06x | STRONG 79/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 721.02 | 97.12 | +3.26% | 2.03x | 34747 | STRONG 100/100 | HIGH 65/100 | Consider small entry |
| 2 | ETH/USD ⭐ | 1714.96 | 83.49 | +1.40% | 3.47x | 30132 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | PUMP/USD | 0.002648 | 78.66 | +2.40% | 5.76x | 4084 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 4 | SOL/USD ⭐ | 72.17 | 77.75 | +1.46% | 1.83x | 33100 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 5 | XRP/USD ⭐ | 0.95674 | 74.75 | +1.22% | 2.10x | 20743 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | XBT/USD ⭐ | 61272.7 | 74.51 | +1.32% | 1.81x | 130972 | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 7 | ADA/USD ⭐ | 0.150572 | 74.27 | +1.13% | 3.77x | 10010 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | NEAR/USD ⭐ | 3.101 | 73.78 | +1.71% | 3.14x | 13464 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | XMR/USD ⭐ | 467.43 | 69.71 | +1.34% | 1.29x | 18151 | STRONG 75/100 | HIGH 61/100 | Watch |
| 10 | LTC/USD ⭐ | 44.39 | 67.83 | +0.98% | 1.06x | 14204 | STRONG 79/100 | HIGH 62/100 | Watch |
| 11 | XDG/USD | 0.0572804 | 67.53 | +1.24% | 1.48x | 5120 | STRONG 79/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, NEAR/USD, ETH/USD, SOL/USD, XRP/USD, ADA/USD, XMR/USD, XBT/USD, LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
