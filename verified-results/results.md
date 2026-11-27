# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T08:01:49.650020+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45962273390
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c22cf158c5150d5e2a62cd29b45e14c6fd43521f (atomic ledger/results publication)
**Ledger generation:** 1980 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 742.4 | 103.310 | 96.564 | +8.91% | +0.50% | 1.43x | 6.9 | 2026-11-27T08:01:43.509575+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XRP/USD | 0.97481 | 95.731 | 78.754 | +3.40% | +0.40% | 3.41x | 0.1 | 2026-11-27T08:01:43.509575+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | LINK/USD | 9.60514 | 95.206 | 78.451 | +3.63% | +0.35% | 5.68x | 4.0 | 2026-11-27T08:01:43.509575+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | HYPE/USD | 65.55 | 94.913 | 90.937 | +5.35% | +0.09% | 1.35x | 3.1 | 2026-11-27T08:01:43.509575+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 5 | UNI/USD | 4.8875 | 93.519 | 78.734 | +5.11% | -0.04% | 3.35x | 2.5 | 2026-11-27T08:01:43.509575+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SOL/USD | 73.21 | 91.126 | 76.716 | +3.20% | +0.54% | 2.17x | 1.4 | 2026-11-27T08:01:43.509575+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | ETH/USD | 1732.73 | 85.332 | 73.656 | +2.67% | +0.43% | 1.95x | 0.1 | 2026-11-27T08:01:43.509575+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | VVV/USD | 27.14 | 74.463 | 75.803 | +3.65% | +0.33% | 0.70x | 9.6 | 2026-11-27T08:01:43.509575+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XBT/USD | 61608 | 73.834 | 67.835 | +1.83% | +0.23% | 1.48x | 0.0 | 2026-11-27T08:01:43.509575+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 10 | ADA/USD | 0.152975 | 72.662 | 71.195 | +3.04% | +0.29% | 1.00x | 2.9 | 2026-11-27T08:01:43.509575+00:00 | Not calibrated | STRONG 71/100 | HIGH 62/100 | Watch | WATCH |
| 11 | LTC/USD | 44.38 | 68.862 | 64.116 | +1.46% | +0.27% | 1.34x | 2.3 | 2026-11-27T08:01:43.509575+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 12 | BIGTIME/USD | 0.006286 | 68.573 | 70.470 | +8.03% | -0.48% | 1.05x | 11.1 | 2026-11-27T08:01:43.509575+00:00 | Not calibrated | WEAK 39/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.564 | 742.4 | +0.50% | 1.43x |
| 2 | HYPE/USD | 90.937 | 65.55 | +0.09% | 1.35x |
| 3 | XRP/USD | 78.754 | 0.97481 | +0.40% | 3.41x |
| 4 | UNI/USD | 78.734 | 4.8875 | -0.04% | 3.35x |
| 5 | LINK/USD | 78.451 | 9.60514 | +0.35% | 5.68x |
| 6 | SOL/USD | 76.716 | 73.21 | +0.54% | 2.17x |
| 7 | VVV/USD | 75.803 | 27.14 | +0.33% | 0.70x |
| 8 | ETH/USD | 73.656 | 1732.73 | +0.43% | 1.95x |
| 9 | ADA/USD | 71.195 | 0.152975 | +0.29% | 1.00x |
| 10 | BIGTIME/USD | 70.470 | 0.006286 | -0.48% | 1.05x |
| 11 | XBT/USD | 67.835 | 61608 | +0.23% | 1.48x |
| 12 | LTC/USD | 64.116 | 44.38 | +0.27% | 1.34x |

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

- Persisted scans: 1980; predictions: 17462; observations: 1199093.
- Matured sampled outcomes across 1/6/24/48h: 38621; gap abstentions: 25659. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45962273390 · **Generation:** 1980 · **Legacy run:** 45962273390
**Main quote time:** 2026-11-27T08:01:49.650020+00:00 · **Legacy report time:** 2026-11-27T08:02:42.812450+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 742.4 | 103.31 | +0.50% | 1.43x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | XRP/USD ⭐ | 0.97481 | 95.73 | +0.40% | 3.41x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | LINK/USD ⭐ | 9.60514 | 95.21 | +0.35% | 5.68x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | HYPE/USD ⭐ | 65.55 | 94.91 | +0.09% | 1.35x | STRONG 92/100 | HIGH 55/100 | Watch |
| 5 | UNI/USD | 4.8875 | 93.52 | -0.04% | 3.35x | STRONG 77/100 | HIGH 61/100 | Watch |
| 6 | SOL/USD ⭐ | 73.21 | 91.13 | +0.54% | 2.17x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | ETH/USD ⭐ | 1732.73 | 85.33 | +0.43% | 1.95x | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 8 | VVV/USD | 27.14 | 74.46 | +0.33% | 0.70x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 9 | XBT/USD ⭐ | 61608 | 73.83 | +0.23% | 1.48x | STRONG 92/100 | HIGH 55/100 | Watch |
| 10 | ADA/USD ⭐ | 0.152975 | 72.66 | +0.29% | 1.00x | STRONG 81/100 | HIGH 62/100 | Watch |
| 11 | LTC/USD | 44.38 | 68.86 | +0.27% | 1.34x | STRONG 79/100 | HIGH 55/100 | Watch |
| 12 | BIGTIME/USD | 0.006286 | 68.57 | -0.48% | 1.05x | WEAK 39/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.97439 | 100.00 | +0.40% | 3.41x | 22809 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LINK/USD ⭐ | 9.60514 | 97.98 | +0.35% | 5.68x | 7824 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | HYPE/USD ⭐ | 65.62 | 95.59 | +0.09% | 1.35x | 16106 | STRONG 93/100 | HIGH 55/100 | Watch |
| 4 | SOL/USD ⭐ | 73.27 | 94.98 | +0.54% | 2.17x | 33433 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | ZEC/USD ⭐ | 741 | 93.21 | +0.50% | 1.43x | 39891 | STRONG 100/100 | HIGH 55/100 | Watch |
| 6 | PEPE/USD | 3.599e-06 | 90.37 | +0.45% | 6.55x | 5218 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | ETH/USD ⭐ | 1732.12 | 88.58 | +0.43% | 1.95x | 34282 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 8 | ADA/USD ⭐ | 0.153242 | 82.71 | +0.29% | 1.00x | 9588 | STRONG 86/100 | HIGH 62/100 | Watch |
| 9 | XBT/USD ⭐ | 61646.6 | 77.38 | +0.23% | 1.48x | 137005 | STRONG 94/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ZEC/USD, XRP/USD, LINK/USD, HYPE/USD, SOL/USD, ETH/USD, XBT/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
