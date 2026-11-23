# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T08:51:27.488798+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45141745968
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d677c12431e2ee3cf72bb80a81a5d51317529250 (atomic ledger/results publication)
**Ledger generation:** 1407 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 2.1908 | 87.563 | 80.324 | +6.64% | -0.85% | 2.15x | 14.1 | 2026-11-23T08:51:19.151771+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 2 | QNT/USD | 148.05 | 81.779 | 64.025 | +3.21% | +0.55% | 4.25x | 5.4 | 2026-11-23T08:51:19.151771+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ALGO/USD | 0.07912 | 80.971 | 63.935 | +4.89% | +0.41% | 4.69x | 8.8 | 2026-11-23T08:51:19.151771+00:00 | Not calibrated | STRONG 95/100 | HIGH 60/100 | Consider small entry | WATCH |
| 4 | XRP/USD | 0.93981 | 78.505 | 62.983 | +1.32% | +0.10% | 3.07x | 2.6 | 2026-11-23T08:51:19.151771+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 5 | XMR/USD | 499.48 | 77.353 | 60.175 | +1.17% | +0.44% | 5.58x | 6.0 | 2026-11-23T08:51:19.151771+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | HYPE/USD | 63.54 | 75.094 | 59.541 | +0.76% | +0.11% | 4.42x | 1.6 | 2026-11-23T08:51:19.151771+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SOL/USD | 72.45 | 70.360 | 72.347 | +2.58% | +0.14% | 0.73x | 1.4 | 2026-11-23T08:51:19.151771+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | JUP/USD | 0.24304 | 69.737 | 76.759 | +8.22% | -0.65% | 0.62x | 6.2 | 2026-11-23T08:51:19.151771+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | XDG/USD | 0.0556457 | 68.035 | 52.575 | +0.65% | +0.09% | 11.28x | 0.4 | 2026-11-23T08:51:19.151771+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 10 | PENGU/USD | 0.00435 | 60.089 | 44.858 | +2.02% | +0.05% | 3.12x | 2.3 | 2026-11-23T08:51:19.151771+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |
| 11 | GBP/USD | 1.3135 | 59.770 | 57.205 | +0.34% | +0.07% | 1.22x | 0.4 | 2026-11-23T08:51:19.151771+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6681 | 59.586 | 66.741 | +1.89% | +0.18% | 0.19x | 3.0 | 2026-11-23T08:51:19.151771+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 80.324 | 2.1908 | -0.85% | 2.15x |
| 2 | JUP/USD | 76.759 | 0.24304 | -0.65% | 0.62x |
| 3 | SOL/USD | 72.347 | 72.45 | +0.14% | 0.73x |
| 4 | SUI/USD | 66.741 | 0.6681 | +0.18% | 0.19x |
| 5 | QNT/USD | 64.025 | 148.05 | +0.55% | 4.25x |
| 6 | ALGO/USD | 63.935 | 0.07912 | +0.41% | 4.69x |
| 7 | XRP/USD | 62.983 | 0.93981 | +0.10% | 3.07x |
| 8 | XMR/USD | 60.175 | 499.48 | +0.44% | 5.58x |
| 9 | HYPE/USD | 59.541 | 63.54 | +0.11% | 4.42x |
| 10 | GBP/USD | 57.205 | 1.3135 | +0.07% | 1.22x |
| 11 | XDG/USD | 52.575 | 0.0556457 | +0.09% | 11.28x |
| 12 | PENGU/USD | 44.858 | 0.00435 | +0.05% | 3.12x |

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

- Persisted scans: 1407; predictions: 11651; observations: 851966.
- Matured sampled outcomes across 1/6/24/48h: 19038; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 130 (sampled only; not a success-rate estimate).
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

**Writer:** 45141745968 · **Generation:** 1407 · **Legacy run:** 45141745968
**Main quote time:** 2026-11-23T08:51:27.488798+00:00 · **Legacy report time:** 2026-11-23T08:52:13.729752+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 2.1908 | 87.56 | -0.85% | 2.15x | MODERATE 69/100 | HIGH 67/100 | Watch |
| 2 | QNT/USD ⭐ | 148.05 | 81.78 | +0.55% | 4.25x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ALGO/USD ⭐ | 0.07912 | 80.97 | +0.41% | 4.69x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 4 | XRP/USD ⭐ | 0.93981 | 78.50 | +0.10% | 3.07x | STRONG 94/100 | HIGH 55/100 | Watch |
| 5 | XMR/USD | 499.48 | 77.35 | +0.44% | 5.58x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 6 | HYPE/USD | 63.54 | 75.09 | +0.11% | 4.42x | STRONG 83/100 | HIGH 55/100 | Watch |
| 7 | SOL/USD | 72.45 | 70.36 | +0.14% | 0.73x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 8 | JUP/USD | 0.24304 | 69.74 | -0.65% | 0.62x | WEAK 40/100 | VERY_HIGH 81/100 | Watch |
| 9 | XDG/USD | 0.0556457 | 68.04 | +0.09% | 11.28x | STRONG 79/100 | HIGH 55/100 | Watch |
| 10 | PENGU/USD | 0.00435 | 60.09 | +0.05% | 3.12x | STRONG 75/100 | HIGH 60/100 | Watch |
| 11 | GBP/USD | 1.3135 | 59.77 | +0.07% | 1.22x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 12 | SUI/USD | 0.6681 | 59.59 | +0.18% | 0.19x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 148.26 | 84.74 | +0.55% | 4.25x | 4628 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ALGO/USD ⭐ | 0.07927 | 79.25 | +0.41% | 4.69x | 2346 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 3 | XRP/USD ⭐ | 0.93997 | 73.42 | +0.10% | 3.07x | 20963 | STRONG 92/100 | HIGH 55/100 | Watch |

**Same-run overlap:** QNT/USD, ALGO/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
