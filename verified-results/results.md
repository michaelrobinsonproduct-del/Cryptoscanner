# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T02:02:30.848451+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46095820814
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2d577fa6cefa53c8395813cfd6d6fee89e5de872 (atomic ledger/results publication)
**Ledger generation:** 2090 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.061 | 71.085 | 62.964 | +1.42% | +0.22% | 1.70x | 3.9 | 2026-11-28T02:02:24.350101+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 757.2 | 68.322 | 74.650 | +3.08% | +0.18% | 0.28x | 3.8 | 2026-11-28T02:02:24.350101+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | HYPE/USD | 64.63 | 62.675 | 66.795 | +1.80% | +0.37% | 0.40x | 1.5 | 2026-11-28T02:02:24.350101+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | QNT/USD | 146.99 | 59.356 | 42.514 | +0.48% | +0.37% | 2.91x | 1.4 | 2026-11-28T02:02:24.350101+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 5 | PUMP/USD | 0.002629 | 59.099 | 45.239 | +1.15% | -0.23% | 18.34x | 3.8 | 2026-11-28T02:02:24.350101+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XBT/USD | 60106.3 | 58.893 | 57.827 | +0.41% | +0.02% | 1.10x | 0.0 | 2026-11-28T02:02:24.350101+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 7 | SOL/USD | 72.09 | 55.398 | 59.097 | +0.68% | +0.18% | 0.54x | 1.4 | 2026-11-28T02:02:24.350101+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XRP/USD | 0.95358 | 54.400 | 58.769 | +0.58% | +0.05% | 0.54x | 0.6 | 2026-11-28T02:02:24.350101+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XMR/USD | 410.15 | 54.392 | 53.358 | +0.71% | +0.98% | 0.61x | 13.2 | 2026-11-28T02:02:24.350101+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | ETH/USD | 1667.12 | 53.799 | 57.587 | +0.37% | +0.04% | 0.60x | 0.1 | 2026-11-28T02:02:24.350101+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | TAO/USD | 188.7115 | 52.736 | 58.873 | +0.94% | -0.24% | 0.51x | 5.4 | 2026-11-28T02:02:24.350101+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | SUI/USD | 0.6754 | 51.850 | 56.433 | +0.42% | +0.09% | 0.50x | 3.0 | 2026-11-28T02:02:24.350101+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 74.650 | 757.2 | +0.18% | 0.28x |
| 2 | HYPE/USD | 66.795 | 64.63 | +0.37% | 0.40x |
| 3 | NEAR/USD | 62.964 | 3.061 | +0.22% | 1.70x |
| 4 | SOL/USD | 59.097 | 72.09 | +0.18% | 0.54x |
| 5 | TAO/USD | 58.873 | 188.7115 | -0.24% | 0.51x |
| 6 | XRP/USD | 58.769 | 0.95358 | +0.05% | 0.54x |
| 7 | XBT/USD | 57.827 | 60106.3 | +0.02% | 1.10x |
| 8 | ETH/USD | 57.587 | 1667.12 | +0.04% | 0.60x |
| 9 | SUI/USD | 56.433 | 0.6754 | +0.09% | 0.50x |
| 10 | XMR/USD | 53.358 | 410.15 | +0.98% | 0.61x |
| 11 | PUMP/USD | 45.239 | 0.002629 | -0.23% | 18.34x |
| 12 | QNT/USD | 42.514 | 146.99 | +0.37% | 2.91x |

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

- Persisted scans: 2090; predictions: 18743; observations: 1265586.
- Matured sampled outcomes across 1/6/24/48h: 43141; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46095820814 · **Generation:** 2090 · **Legacy run:** 46095820814
**Main quote time:** 2026-11-28T02:02:30.848451+00:00 · **Legacy report time:** 2026-11-28T02:03:17.409705+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.061 | 71.09 | +0.22% | 1.70x | STRONG 91/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD | 757.2 | 68.32 | +0.18% | 0.28x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 3 | HYPE/USD | 64.63 | 62.68 | +0.37% | 0.40x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 4 | QNT/USD ⭐ | 146.99 | 59.36 | +0.37% | 2.91x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 5 | PUMP/USD | 0.002629 | 59.10 | -0.23% | 18.34x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 6 | XBT/USD | 60106.3 | 58.89 | +0.02% | 1.10x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 7 | SOL/USD | 72.09 | 55.40 | +0.18% | 0.54x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 8 | XRP/USD | 0.95358 | 54.40 | +0.05% | 0.54x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 9 | XMR/USD | 410.15 | 54.39 | +0.98% | 0.61x | MODERATE 52/100 | VERY_HIGH 76/100 | Watch |
| 10 | ETH/USD | 1667.12 | 53.80 | +0.04% | 0.60x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 11 | TAO/USD | 188.7115 | 52.74 | -0.24% | 0.51x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | SUI/USD | 0.6754 | 51.85 | +0.09% | 0.50x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.0577 | 63.98 | +0.22% | 1.70x | 14288 | STRONG 87/100 | HIGH 55/100 | Consider small entry |
| 2 | QNT/USD ⭐ | 146.99 | 56.02 | +0.37% | 2.91x | 6688 | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 3 | SENT/USD | 0.024147 | 48.21 | +0.47% | 1.60x | 3885 | MODERATE 69/100 | HIGH 67/100 | Watch |

**Same-run overlap:** NEAR/USD, QNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
