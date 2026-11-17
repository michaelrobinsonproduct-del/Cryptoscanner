# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T21:11:33.214259+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44177071164
**Source SHA:** 19d4b4203812bcae29aa50a9444ca1bb8d9760d3
**Previous ledger commit:** 8a9890dd68c57c137cbecbe41f5a92b37c9a0007 (atomic ledger/results publication)
**Ledger generation:** 456 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 7.125 | 76.857 | 75.825 | +3.28% | +0.38% | 0.91x | 4.2 | 2026-11-17T21:11:24.380139+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 2 | ADA/USD | 0.153706 | 73.240 | 56.109 | +0.46% | +0.43% | 2.96x | 4.2 | 2026-11-17T21:11:24.380139+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ZEC/USD | 921.28 | 71.944 | 68.476 | +1.93% | -0.10% | 1.39x | 0.1 | 2026-11-17T21:11:24.380139+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SOL/USD | 73.13 | 69.113 | 70.074 | +2.25% | +0.26% | 0.77x | 1.4 | 2026-11-17T21:11:24.380139+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 5 | ICNT/USD | 0.2458 | 68.708 | 66.118 | +8.23% | -2.48% | 13.92x | 20.4 | 2026-11-17T21:11:24.380139+00:00 | Not calibrated | MODERATE 54/100 | EXTREME 89/100 | Do nothing | WATCH |
| 6 | NEAR/USD | 3.2479 | 66.921 | 74.510 | +2.85% | +0.17% | 0.15x | 0.9 | 2026-11-17T21:11:24.380139+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | XRP/USD | 0.9699 | 65.889 | 65.842 | +1.59% | +0.56% | 0.73x | 0.5 | 2026-11-17T21:11:24.380139+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | AAVE/USD | 110.18 | 64.975 | 50.338 | +1.57% | -0.07% | 11.38x | 5.4 | 2026-11-17T21:11:24.380139+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 9 | SUI/USD | 0.7246 | 59.671 | 59.370 | +0.72% | +0.29% | 0.88x | 1.4 | 2026-11-17T21:11:24.380139+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 10 | XMR/USD | 503.48 | 59.625 | 63.479 | +2.01% | -0.79% | 1.01x | 11.1 | 2026-11-17T21:11:24.380139+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 11 | TRUST/USD | 0.04639 | 58.999 | 62.661 | +7.86% | +0.15% | 0.56x | 30.2 | 2026-11-17T21:11:24.380139+00:00 | Not calibrated | WEAK 39/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | UNI/USD | 5.2747 | 54.559 | 56.787 | +2.20% | +0.03% | 0.76x | 4.2 | 2026-11-17T21:11:24.380139+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 75.825 | 7.125 | +0.38% | 0.91x |
| 2 | NEAR/USD | 74.510 | 3.2479 | +0.17% | 0.15x |
| 3 | SOL/USD | 70.074 | 73.13 | +0.26% | 0.77x |
| 4 | ZEC/USD | 68.476 | 921.28 | -0.10% | 1.39x |
| 5 | ICNT/USD | 66.118 | 0.2458 | -2.48% | 13.92x |
| 6 | XRP/USD | 65.842 | 0.9699 | +0.56% | 0.73x |
| 7 | XMR/USD | 63.479 | 503.48 | -0.79% | 1.01x |
| 8 | TRUST/USD | 62.661 | 0.04639 | +0.15% | 0.56x |
| 9 | SUI/USD | 59.370 | 0.7246 | +0.29% | 0.88x |
| 10 | UNI/USD | 56.787 | 5.2747 | +0.03% | 0.76x |
| 11 | ADA/USD | 56.109 | 0.153706 | +0.43% | 2.96x |
| 12 | AAVE/USD | 50.338 | 110.18 | -0.07% | 11.38x |

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

- Persisted scans: 456; predictions: 3953; observations: 274711.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12353. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44177071164 · **Generation:** 456 · **Legacy run:** 44177071164
**Main quote time:** 2026-11-17T21:11:33.214259+00:00 · **Legacy report time:** 2026-11-17T21:11:43.915561+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 7.125 | 76.86 | +0.38% | 0.91x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 2 | ADA/USD | 0.153706 | 73.24 | +0.43% | 2.96x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 3 | ZEC/USD | 921.28 | 71.94 | -0.10% | 1.39x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 4 | SOL/USD | 73.13 | 69.11 | +0.26% | 0.77x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 5 | ICNT/USD | 0.2458 | 68.71 | -2.48% | 13.92x | MODERATE 54/100 | EXTREME 89/100 | Do nothing |
| 6 | NEAR/USD | 3.2479 | 66.92 | +0.17% | 0.15x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 7 | XRP/USD | 0.9699 | 65.89 | +0.56% | 0.73x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 8 | AAVE/USD | 110.18 | 64.97 | -0.07% | 11.38x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 9 | SUI/USD | 0.7246 | 59.67 | +0.29% | 0.88x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 10 | XMR/USD | 503.48 | 59.62 | -0.79% | 1.01x | WEAK 35/100 | VERY_HIGH 74/100 | Watch |
| 11 | TRUST/USD | 0.04639 | 59.00 | +0.15% | 0.56x | WEAK 39/100 | EXTREME 87/100 | Do nothing |
| 12 | UNI/USD | 5.2747 | 54.56 | +0.03% | 0.76x | MODERATE 47/100 | HIGH 62/100 | Watch |

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
