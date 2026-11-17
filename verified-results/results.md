# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T22:25:04.318401+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44189765660
**Source SHA:** e9b1b6ee47d56a43a454042547735fcd1cdc45a9
**Previous ledger commit:** ae318f6825aaa5b9a0aab6c1c8520cd87288cf79 (atomic ledger/results publication)
**Ledger generation:** 458 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.3075 | 85.545 | 85.765 | +4.74% | +1.01% | 0.47x | 4.8 | 2026-11-17T22:24:55.892535+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | TAO/USD | 193.5892 | 79.133 | 61.334 | +1.25% | +0.56% | 2.55x | 4.8 | 2026-11-17T22:24:55.892535+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | INJ/USD | 7.201 | 78.515 | 82.866 | +4.38% | +0.69% | 0.22x | 5.6 | 2026-11-17T22:24:55.892535+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | LUNA/USD | 4.114e-05 | 77.341 | 64.523 | +10.29% | -0.44% | 3.62x | 26.8 | 2026-11-17T22:24:55.892535+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 5 | ADA/USD | 0.154196 | 73.952 | 59.235 | +0.78% | +0.45% | 2.25x | 2.5 | 2026-11-17T22:24:55.892535+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | ZEC/USD | 940 | 73.380 | 78.350 | +4.00% | +0.40% | 0.31x | 9.4 | 2026-11-17T22:24:55.892535+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | JUP/USD | 0.25704 | 72.402 | 72.489 | +6.85% | +0.74% | 0.62x | 11.3 | 2026-11-17T22:24:55.892535+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | SOL/USD | 73.76 | 72.015 | 75.568 | +3.13% | +0.35% | 0.47x | 2.7 | 2026-11-17T22:24:55.892535+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XRP/USD | 0.97034 | 69.224 | 65.805 | +1.63% | +0.31% | 1.19x | 1.2 | 2026-11-17T22:24:55.892535+00:00 | Not calibrated | STRONG 70/100 | HIGH 62/100 | Watch | WATCH |
| 10 | XMR/USD | 507.51 | 67.163 | 70.613 | +2.82% | +0.46% | 0.42x | 8.3 | 2026-11-17T22:24:55.892535+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | TRUST/USD | 0.04723 | 64.278 | 66.325 | +9.81% | +0.34% | 0.62x | 23.3 | 2026-11-17T22:24:55.892535+00:00 | Not calibrated | MODERATE 52/100 | EXTREME 87/100 | Do nothing | WATCH |
| 12 | AKT/USD | 0.4991 | 62.392 | 61.304 | +4.33% | +1.13% | 0.54x | 2.0 | 2026-11-17T22:24:55.892535+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 85.765 | 3.3075 | +1.01% | 0.47x |
| 2 | INJ/USD | 82.866 | 7.201 | +0.69% | 0.22x |
| 3 | ZEC/USD | 78.350 | 940 | +0.40% | 0.31x |
| 4 | SOL/USD | 75.568 | 73.76 | +0.35% | 0.47x |
| 5 | JUP/USD | 72.489 | 0.25704 | +0.74% | 0.62x |
| 6 | XMR/USD | 70.613 | 507.51 | +0.46% | 0.42x |
| 7 | TRUST/USD | 66.325 | 0.04723 | +0.34% | 0.62x |
| 8 | XRP/USD | 65.805 | 0.97034 | +0.31% | 1.19x |
| 9 | LUNA/USD | 64.523 | 4.114e-05 | -0.44% | 3.62x |
| 10 | TAO/USD | 61.334 | 193.5892 | +0.56% | 2.55x |
| 11 | AKT/USD | 61.304 | 0.4991 | +1.13% | 0.54x |
| 12 | ADA/USD | 59.235 | 0.154196 | +0.45% | 2.25x |

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

- Persisted scans: 458; predictions: 3977; observations: 275929.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12386. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44189765660 · **Generation:** 458 · **Legacy run:** 44189765660
**Main quote time:** 2026-11-17T22:25:04.318401+00:00 · **Legacy report time:** 2026-11-17T22:25:13.165583+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.3075 | 85.55 | +1.01% | 0.47x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 2 | TAO/USD | 193.5892 | 79.13 | +0.56% | 2.55x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 3 | INJ/USD | 7.201 | 78.52 | +0.69% | 0.22x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 4 | LUNA/USD | 4.114e-05 | 77.34 | -0.44% | 3.62x | MODERATE 59/100 | VERY_HIGH 78/100 | Watch |
| 5 | ADA/USD | 0.154196 | 73.95 | +0.45% | 2.25x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 6 | ZEC/USD | 940 | 73.38 | +0.40% | 0.31x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 7 | JUP/USD ⭐ | 0.25704 | 72.40 | +0.74% | 0.62x | STRONG 71/100 | VERY_HIGH 81/100 | Watch |
| 8 | SOL/USD | 73.76 | 72.02 | +0.35% | 0.47x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 9 | XRP/USD ⭐ | 0.97034 | 69.22 | +0.31% | 1.19x | STRONG 80/100 | HIGH 62/100 | Watch |
| 10 | XMR/USD | 507.51 | 67.16 | +0.46% | 0.42x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 11 | TRUST/USD | 0.04723 | 64.28 | +0.34% | 0.62x | MODERATE 52/100 | EXTREME 87/100 | Do nothing |
| 12 | AKT/USD | 0.4991 | 62.39 | +1.13% | 0.54x | MODERATE 61/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | RENDER/USD | 1.436 | 80.21 | +0.70% | 4.72x | 2385 | STRONG 90/100 | HIGH 66/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.97029 | 72.76 | +0.20% | 1.57x | 29745 | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 3 | JUP/USD ⭐ | 0.25704 | 70.40 | +0.82% | 1.07x | 2135 | STRONG 75/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** JUP/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
