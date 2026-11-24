# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T10:51:44.619018+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45378429440
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 162cc9ecc3c61f2dc92439960e19631053971e74 (atomic ledger/results publication)
**Ledger generation:** 1564 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01252 | 83.034 | 78.364 | +8.68% | +0.00% | 1.47x | 16.0 | 2026-11-24T10:51:38.639863+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 494.25 | 73.459 | 60.683 | +1.69% | -0.44% | 2.85x | 12.3 | 2026-11-24T10:51:38.639863+00:00 | Not calibrated | MODERATE 62/100 | HIGH 67/100 | Watch | WATCH |
| 3 | VVV/USD | 25.109 | 62.864 | 69.746 | +2.70% | -0.42% | 0.52x | 8.4 | 2026-11-24T10:51:38.639863+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | DBR/USD | 0.01438 | 53.130 | 62.237 | +7.15% | -0.69% | 0.43x | 27.8 | 2026-11-24T10:51:38.639863+00:00 | Not calibrated | WEAK 22/100 | EXTREME 100/100 | Do nothing | WATCH |
| 5 | INX/USD | 0.003982 | 52.152 | 29.256 | +2.15% | +1.58% | 4.35x | 35.1 | 2026-11-24T10:51:38.639863+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | GBP/USD | 1.30679 | 50.157 | 56.825 | +0.27% | +0.03% | 0.32x | 0.2 | 2026-11-24T10:51:38.639863+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.448e-06 | 48.080 | 53.190 | +0.76% | -0.38% | 0.68x | 5.8 | 2026-11-24T10:51:38.639863+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | XDC/USD | 0.02624 | 41.237 | 34.527 | +1.00% | -0.61% | 1.97x | 15.3 | 2026-11-24T10:51:38.639863+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 9 | 2Z/USD | 0.01606 | 40.686 | 45.926 | +2.62% | -0.50% | 0.72x | 6.2 | 2026-11-24T10:51:38.639863+00:00 | Not calibrated | WEAK 25/100 | EXTREME 88/100 | Do nothing | WATCH |
| 10 | BAT/USD | 0.0779 | 26.880 | 32.591 | +0.95% | -0.04% | 0.45x | 12.8 | 2026-11-24T10:51:38.639863+00:00 | Not calibrated | WEAK 13/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 78.364 | 0.01252 | +0.00% | 1.47x |
| 2 | VVV/USD | 69.746 | 25.109 | -0.42% | 0.52x |
| 3 | DBR/USD | 62.237 | 0.01438 | -0.69% | 0.43x |
| 4 | XMR/USD | 60.683 | 494.25 | -0.44% | 2.85x |
| 5 | GBP/USD | 56.825 | 1.30679 | +0.03% | 0.32x |
| 6 | PEPE/USD | 53.190 | 3.448e-06 | -0.38% | 0.68x |
| 7 | 2Z/USD | 45.926 | 0.01606 | -0.50% | 0.72x |
| 8 | XDC/USD | 34.527 | 0.02624 | -0.61% | 1.97x |
| 9 | BAT/USD | 32.591 | 0.0779 | -0.04% | 0.45x |
| 10 | INX/USD | 29.256 | 0.003982 | +1.58% | 4.35x |

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

- Persisted scans: 1564; predictions: 13475; observations: 947574.
- Matured sampled outcomes across 1/6/24/48h: 25853; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45378429440 · **Generation:** 1564 · **Legacy run:** 45378429440
**Main quote time:** 2026-11-24T10:51:44.619018+00:00 · **Legacy report time:** 2026-11-24T10:52:35.007551+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.01252 | 83.03 | +0.00% | 1.47x | STRONG 72/100 | HIGH 61/100 | Watch |
| 2 | XMR/USD | 494.25 | 73.46 | -0.44% | 2.85x | MODERATE 62/100 | HIGH 67/100 | Watch |
| 3 | VVV/USD | 25.109 | 62.86 | -0.42% | 0.52x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 4 | DBR/USD | 0.01438 | 53.13 | -0.69% | 0.43x | WEAK 22/100 | EXTREME 100/100 | Do nothing |
| 5 | INX/USD ⭐ | 0.003982 | 52.15 | +1.58% | 4.35x | STRONG 76/100 | VERY_HIGH 72/100 | Watch |
| 6 | GBP/USD | 1.30679 | 50.16 | +0.03% | 0.32x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 7 | PEPE/USD | 3.448e-06 | 48.08 | -0.38% | 0.68x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | XDC/USD | 0.02624 | 41.24 | -0.61% | 1.97x | WEAK 36/100 | VERY_HIGH 72/100 | Watch |
| 9 | 2Z/USD | 0.01606 | 40.69 | -0.50% | 0.72x | WEAK 25/100 | EXTREME 88/100 | Do nothing |
| 10 | BAT/USD | 0.0779 | 26.88 | -0.04% | 0.45x | WEAK 13/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INX/USD ⭐ | 0.003979 | 60.71 | +1.58% | 4.35x | 4439 | STRONG 85/100 | VERY_HIGH 72/100 | Watch |
| 2 | NIGHT/USD | 0.04821 | 45.31 | +0.35% | 1.70x | 12298 | MODERATE 68/100 | HIGH 55/100 | Watch |

**Same-run overlap:** INX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
