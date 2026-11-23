# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T23:21:35.652673+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45287809357
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5317841ab364aa1bb0899ad8b2f5cbbd12796acf (atomic ledger/results publication)
**Ledger generation:** 1495 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 2.2716 | 102.583 | 98.239 | +10.57% | -1.60% | 2.23x | 3.5 | 2026-11-23T23:21:28.994841+00:00 | Not calibrated | STRONG 80/100 | HIGH 65/100 | Do nothing | WATCH |
| 2 | ALGO/USD | 0.08132 | 90.313 | 91.937 | +7.81% | -0.07% | 0.87x | 6.2 | 2026-11-23T23:21:28.994841+00:00 | Not calibrated | MODERATE 50/100 | HIGH 68/100 | Watch | WATCH |
| 3 | QNT/USD | 155.87 | 88.458 | 98.075 | +8.67% | -0.45% | 0.27x | 3.8 | 2026-11-23T23:21:28.994841+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | LTC/USD | 41.31 | 83.809 | 73.834 | +2.86% | +0.22% | 1.89x | 2.4 | 2026-11-23T23:21:28.994841+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | ATOM/USD | 1.266 | 77.754 | 72.247 | +8.02% | -0.56% | 1.83x | 11.8 | 2026-11-23T23:21:28.994841+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6705 | 70.579 | 70.054 | +2.26% | +0.09% | 1.01x | 1.5 | 2026-11-23T23:21:28.994841+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 7 | SHX/USD | 0.003597 | 70.111 | 70.788 | +6.58% | +0.00% | 0.93x | 11.1 | 2026-11-23T23:21:28.994841+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 8 | CAP/USD | 0.101154 | 67.878 | 76.460 | +8.10% | -1.59% | 0.94x | 5.4 | 2026-11-23T23:21:28.994841+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 9 | TRX/USD | 0.309399 | 65.873 | 50.731 | +1.38% | +0.03% | 3.05x | 1.0 | 2026-11-23T23:21:28.994841+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XRP/USD | 0.94177 | 64.878 | 65.686 | +1.53% | +0.20% | 0.82x | 0.1 | 2026-11-23T23:21:28.994841+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 11 | SOL/USD | 71.98 | 64.621 | 67.685 | +1.91% | -0.01% | 0.70x | 1.4 | 2026-11-23T23:21:28.994841+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0563066 | 63.216 | 67.755 | +1.85% | +0.13% | 0.48x | 0.4 | 2026-11-23T23:21:28.994841+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 98.239 | 2.2716 | -1.60% | 2.23x |
| 2 | QNT/USD | 98.075 | 155.87 | -0.45% | 0.27x |
| 3 | ALGO/USD | 91.937 | 0.08132 | -0.07% | 0.87x |
| 4 | CAP/USD | 76.460 | 0.101154 | -1.59% | 0.94x |
| 5 | LTC/USD | 73.834 | 41.31 | +0.22% | 1.89x |
| 6 | ATOM/USD | 72.247 | 1.266 | -0.56% | 1.83x |
| 7 | SHX/USD | 70.788 | 0.003597 | +0.00% | 0.93x |
| 8 | SUI/USD | 70.054 | 0.6705 | +0.09% | 1.01x |
| 9 | XDG/USD | 67.755 | 0.0563066 | +0.13% | 0.48x |
| 10 | SOL/USD | 67.685 | 71.98 | -0.01% | 0.70x |
| 11 | XRP/USD | 65.686 | 0.94177 | +0.20% | 0.82x |
| 12 | TRX/USD | 50.731 | 0.309399 | +0.03% | 3.05x |

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

- Persisted scans: 1495; predictions: 12707; observations: 905557.
- Matured sampled outcomes across 1/6/24/48h: 23116; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45287809357 · **Generation:** 1495 · **Legacy run:** 45287809357
**Main quote time:** 2026-11-23T23:21:35.652673+00:00 · **Legacy report time:** 2026-11-23T23:22:20.602390+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 2.2716 | 102.58 | -1.60% | 2.23x | STRONG 80/100 | HIGH 65/100 | Do nothing |
| 2 | ALGO/USD | 0.08132 | 90.31 | -0.07% | 0.87x | MODERATE 50/100 | HIGH 68/100 | Watch |
| 3 | QNT/USD | 155.87 | 88.46 | -0.45% | 0.27x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 4 | LTC/USD ⭐ | 41.31 | 83.81 | +0.22% | 1.89x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 5 | ATOM/USD | 1.266 | 77.75 | -0.56% | 1.83x | MODERATE 54/100 | VERY_HIGH 72/100 | Watch |
| 6 | SUI/USD ⭐ | 0.6705 | 70.58 | +0.09% | 1.01x | STRONG 70/100 | HIGH 62/100 | Watch |
| 7 | SHX/USD | 0.003597 | 70.11 | +0.00% | 0.93x | MODERATE 50/100 | VERY_HIGH 80/100 | Watch |
| 8 | CAP/USD | 0.101154 | 67.88 | -1.59% | 0.94x | WEAK 39/100 | VERY_HIGH 77/100 | Do nothing |
| 9 | TRX/USD | 0.309399 | 65.87 | +0.03% | 3.05x | STRONG 78/100 | HIGH 55/100 | Watch |
| 10 | XRP/USD | 0.94177 | 64.88 | +0.20% | 0.82x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 11 | SOL/USD | 71.98 | 64.62 | -0.01% | 0.70x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 12 | XDG/USD | 0.0563066 | 63.22 | +0.13% | 0.48x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD ⭐ | 41.31 | 80.88 | +0.22% | 1.89x | 12748 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 2 | SUI/USD ⭐ | 0.6705 | 73.41 | +0.09% | 1.01x | 12404 | STRONG 72/100 | HIGH 62/100 | Watch |

**Same-run overlap:** LTC/USD, SUI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
