# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T12:21:01.375667+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45818587718
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 68be79ddd484ec848f4b47050858d119203df7f6 (atomic ledger/results publication)
**Ledger generation:** 1860 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 588; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKY/USD | 0.04621 | 100.489 | 78.189 | +10.34% | +1.46% | 6.52x | 2.2 | 2026-11-26T12:20:53.508671+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | LINK/USD | 9.24807 | 84.571 | 68.617 | +2.25% | +0.19% | 6.47x | 4.3 | 2026-11-26T12:20:53.508671+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 3 | FET/USD | 0.1151 | 81.074 | 72.082 | +6.08% | -1.20% | 5.39x | 8.7 | 2026-11-26T12:20:53.508671+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 4 | XRP/USD | 0.95008 | 77.390 | 64.684 | +1.44% | -0.46% | 3.75x | 0.8 | 2026-11-26T12:20:53.508671+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 5 | INJ/USD | 6.183 | 77.108 | 67.069 | +3.85% | -0.99% | 5.85x | 6.5 | 2026-11-26T12:20:53.508671+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 6 | ETH/USD | 1701.52 | 73.287 | 59.395 | +0.66% | -0.22% | 6.61x | 0.4 | 2026-11-26T12:20:53.508671+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 7 | NEAR/USD | 3.0792 | 72.483 | 61.562 | +0.96% | -0.82% | 3.05x | 0.3 | 2026-11-26T12:20:53.508671+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 8 | SOL/USD | 70.76 | 71.002 | 57.973 | +0.53% | -0.39% | 9.10x | 1.4 | 2026-11-26T12:20:53.508671+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 9 | ADA/USD | 0.148816 | 70.695 | 68.015 | +2.09% | -0.40% | 1.47x | 3.2 | 2026-11-26T12:20:53.508671+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 10 | SYRUP/USD | 0.07204 | 70.008 | 64.775 | +8.71% | +0.28% | 1.38x | 25.0 | 2026-11-26T12:20:53.508671+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 11 | LTC/USD | 43.41 | 66.008 | 65.321 | +1.64% | -0.41% | 1.28x | 2.3 | 2026-11-26T12:20:53.508671+00:00 | Not calibrated | WEAK 43/100 | HIGH 61/100 | Watch | WATCH |
| 12 | QNT/USD | 149.05 | 64.261 | 66.358 | +2.94% | -0.03% | 0.81x | 5.4 | 2026-11-26T12:20:53.508671+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 78.189 | 0.04621 | +1.46% | 6.52x |
| 2 | FET/USD | 72.082 | 0.1151 | -1.20% | 5.39x |
| 3 | LINK/USD | 68.617 | 9.24807 | +0.19% | 6.47x |
| 4 | ADA/USD | 68.015 | 0.148816 | -0.40% | 1.47x |
| 5 | INJ/USD | 67.069 | 6.183 | -0.99% | 5.85x |
| 6 | QNT/USD | 66.358 | 149.05 | -0.03% | 0.81x |
| 7 | LTC/USD | 65.321 | 43.41 | -0.41% | 1.28x |
| 8 | SYRUP/USD | 64.775 | 0.07204 | +0.28% | 1.38x |
| 9 | XRP/USD | 64.684 | 0.95008 | -0.46% | 3.75x |
| 10 | NEAR/USD | 61.562 | 3.0792 | -0.82% | 3.05x |
| 11 | ETH/USD | 59.395 | 1701.52 | -0.22% | 6.61x |
| 12 | SOL/USD | 57.973 | 70.76 | -0.39% | 9.10x |

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

- Persisted scans: 1860; predictions: 16055; observations: 1127361.
- Matured sampled outcomes across 1/6/24/48h: 34730; gap abstentions: 24728. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45818587718 · **Generation:** 1860 · **Legacy run:** 45818587718
**Main quote time:** 2026-11-26T12:21:01.375667+00:00 · **Legacy report time:** 2026-11-26T12:22:00.626277+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04621 | 100.49 | +1.46% | 6.52x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | LINK/USD ⭐ | 9.24807 | 84.57 | +0.19% | 6.47x | STRONG 97/100 | HIGH 55/100 | Watch |
| 3 | FET/USD | 0.1151 | 81.07 | -1.20% | 5.39x | STRONG 71/100 | VERY_HIGH 70/100 | Do nothing |
| 4 | XRP/USD | 0.95008 | 77.39 | -0.46% | 3.75x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 5 | INJ/USD | 6.183 | 77.11 | -0.99% | 5.85x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 6 | ETH/USD | 1701.52 | 73.29 | -0.22% | 6.61x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 7 | NEAR/USD | 3.0792 | 72.48 | -0.82% | 3.05x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 8 | SOL/USD | 70.76 | 71.00 | -0.39% | 9.10x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 9 | ADA/USD | 0.148816 | 70.69 | -0.40% | 1.47x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 10 | SYRUP/USD ⭐ | 0.07204 | 70.01 | +0.28% | 1.38x | STRONG 80/100 | VERY_HIGH 72/100 | Watch |
| 11 | LTC/USD | 43.41 | 66.01 | -0.41% | 1.28x | WEAK 43/100 | HIGH 61/100 | Watch |
| 12 | QNT/USD | 149.05 | 64.26 | -0.03% | 0.81x | WEAK 37/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.0465 | 84.97 | +1.46% | 6.52x | 4694 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | LINK/USD ⭐ | 9.24136 | 79.37 | +0.19% | 6.47x | 9186 | STRONG 95/100 | HIGH 55/100 | Watch |
| 3 | SYRUP/USD ⭐ | 0.07204 | 73.72 | +0.28% | 1.38x | 3860 | STRONG 82/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** SKY/USD, LINK/USD, SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
