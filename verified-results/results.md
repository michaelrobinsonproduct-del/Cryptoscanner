# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T11:51:40.874493+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45387720286
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2d55ef7b2a8e8f96dffcf3ff57fe14dba2571877 (atomic ledger/results publication)
**Ledger generation:** 1570 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.984 | 102.005 | 97.054 | +6.28% | +1.35% | 0.82x | 3.9 | 2026-11-24T11:51:34.052855+00:00 | Not calibrated | STRONG 80/100 | HIGH 62/100 | Watch | WATCH |
| 2 | MON/USD | 0.01277 | 92.699 | 79.101 | +10.85% | +0.63% | 2.04x | 15.7 | 2026-11-24T11:51:34.052855+00:00 | Not calibrated | STRONG 96/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | GBP/USD | 1.30832 | 65.872 | 57.647 | +0.39% | +0.04% | 1.80x | 0.2 | 2026-11-24T11:51:34.052855+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XMR/USD | 498.6 | 65.000 | 70.210 | +2.59% | +0.28% | 0.34x | 5.8 | 2026-11-24T11:51:34.052855+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ICNT/USD | 0.3264 | 59.477 | 61.217 | +5.60% | -0.76% | 1.20x | 21.5 | 2026-11-24T11:51:34.052855+00:00 | Not calibrated | WEAK 30/100 | EXTREME 85/100 | Do nothing | WATCH |
| 6 | PEPE/USD | 3.478e-06 | 56.522 | 59.958 | +1.64% | +0.43% | 0.44x | 5.8 | 2026-11-24T11:51:34.052855+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.04892 | 49.066 | 53.880 | +1.60% | +0.56% | 0.24x | 12.3 | 2026-11-24T11:51:34.052855+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | BABY/USD | 0.00864 | 47.770 | 38.433 | +1.65% | +0.58% | 1.64x | 11.6 | 2026-11-24T11:51:34.052855+00:00 | Not calibrated | MODERATE 64/100 | HIGH 66/100 | Watch | WATCH |
| 9 | BAT/USD | 0.07803 | 23.063 | 29.954 | +1.11% | -0.23% | 0.43x | 20.5 | 2026-11-24T11:51:34.052855+00:00 | Not calibrated | WEAK 7/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 97.054 | 25.984 | +1.35% | 0.82x |
| 2 | MON/USD | 79.101 | 0.01277 | +0.63% | 2.04x |
| 3 | XMR/USD | 70.210 | 498.6 | +0.28% | 0.34x |
| 4 | ICNT/USD | 61.217 | 0.3264 | -0.76% | 1.20x |
| 5 | PEPE/USD | 59.958 | 3.478e-06 | +0.43% | 0.44x |
| 6 | GBP/USD | 57.647 | 1.30832 | +0.04% | 1.80x |
| 7 | NIGHT/USD | 53.880 | 0.04892 | +0.56% | 0.24x |
| 8 | BABY/USD | 38.433 | 0.00864 | +0.58% | 1.64x |
| 9 | BAT/USD | 29.954 | 0.07803 | -0.23% | 0.43x |

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

- Persisted scans: 1570; predictions: 13539; observations: 951228.
- Matured sampled outcomes across 1/6/24/48h: 26141; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45387720286 · **Generation:** 1570 · **Legacy run:** 45387720286
**Main quote time:** 2026-11-24T11:51:40.874493+00:00 · **Legacy report time:** 2026-11-24T11:52:27.942901+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.984 | 102.01 | +1.35% | 0.82x | STRONG 80/100 | HIGH 62/100 | Watch |
| 2 | MON/USD ⭐ | 0.01277 | 92.70 | +0.63% | 2.04x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | GBP/USD | 1.30832 | 65.87 | +0.04% | 1.80x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 4 | XMR/USD | 498.6 | 65.00 | +0.28% | 0.34x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 5 | ICNT/USD | 0.3264 | 59.48 | -0.76% | 1.20x | WEAK 30/100 | EXTREME 85/100 | Do nothing |
| 6 | PEPE/USD | 3.478e-06 | 56.52 | +0.43% | 0.44x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 7 | NIGHT/USD | 0.04892 | 49.07 | +0.56% | 0.24x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 8 | BABY/USD ⭐ | 0.00864 | 47.77 | +0.58% | 1.64x | STRONG 74/100 | HIGH 66/100 | Watch |
| 9 | BAT/USD | 0.07803 | 23.06 | -0.23% | 0.43x | WEAK 7/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01277 | 83.23 | +0.63% | 2.04x | 10470 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | BABY/USD ⭐ | 0.00862 | 44.87 | +0.58% | 1.64x | 5265 | STRONG 72/100 | HIGH 66/100 | Watch |

**Same-run overlap:** MON/USD, BABY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
