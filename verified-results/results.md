# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T15:01:59.879328+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45200172714
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** be20691da357bb082d66cbc2104f6551ae25923a (atomic ledger/results publication)
**Ledger generation:** 1445 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 43.12 | 99.261 | 97.241 | +7.37% | -0.23% | 1.32x | 2.3 | 2026-11-23T15:01:51.952581+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 2 | HYPE/USD | 67.52 | 96.506 | 97.779 | +7.07% | -1.33% | 1.54x | 4.4 | 2026-11-23T15:01:51.952581+00:00 | Not calibrated | MODERATE 68/100 | HIGH 65/100 | Do nothing | WATCH |
| 3 | SOL/USD | 76.6 | 95.181 | 99.347 | +8.45% | -0.48% | 0.82x | 1.3 | 2026-11-23T15:01:51.952581+00:00 | Not calibrated | MODERATE 53/100 | HIGH 68/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0590643 | 93.870 | 99.585 | +6.84% | -0.32% | 0.59x | 0.8 | 2026-11-23T15:01:51.952581+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | SUI/USD | 0.7142 | 93.117 | 99.299 | +8.92% | -0.60% | 0.68x | 1.4 | 2026-11-23T15:01:51.952581+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | XRP/USD | 0.99309 | 92.690 | 99.043 | +7.07% | -0.63% | 0.68x | 1.9 | 2026-11-23T15:01:51.952581+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | ADA/USD | 0.154034 | 90.876 | 97.306 | +6.52% | -0.52% | 0.62x | 5.4 | 2026-11-23T15:01:51.952581+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | NEAR/USD | 3.1721 | 90.460 | 95.915 | +6.39% | -1.37% | 1.14x | 7.6 | 2026-11-23T15:01:51.952581+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 9 | XLM/USD | 0.135457 | 86.616 | 94.681 | +6.22% | -0.48% | 0.43x | 7.7 | 2026-11-23T15:01:51.952581+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | ZEC/USD | 865.29 | 84.919 | 94.964 | +8.50% | -1.41% | 0.70x | 10.1 | 2026-11-23T15:01:51.952581+00:00 | Not calibrated | WEAK 42/100 | EXTREME 86/100 | Do nothing | WATCH |
| 11 | UNI/USD | 5.1536 | 82.275 | 89.771 | +10.09% | -0.94% | 0.72x | 11.7 | 2026-11-23T15:01:51.952581+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 12 | INJ/USD | 6.854 | 76.893 | 90.376 | +10.05% | -1.63% | 0.47x | 8.8 | 2026-11-23T15:01:51.952581+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 80/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XDG/USD | 99.585 | 0.0590643 | -0.32% | 0.59x |
| 2 | SOL/USD | 99.347 | 76.6 | -0.48% | 0.82x |
| 3 | SUI/USD | 99.299 | 0.7142 | -0.60% | 0.68x |
| 4 | XRP/USD | 99.043 | 0.99309 | -0.63% | 0.68x |
| 5 | HYPE/USD | 97.779 | 67.52 | -1.33% | 1.54x |
| 6 | ADA/USD | 97.306 | 0.154034 | -0.52% | 0.62x |
| 7 | LTC/USD | 97.241 | 43.12 | -0.23% | 1.32x |
| 8 | NEAR/USD | 95.915 | 3.1721 | -1.37% | 1.14x |
| 9 | ZEC/USD | 94.964 | 865.29 | -1.41% | 0.70x |
| 10 | XLM/USD | 94.681 | 0.135457 | -0.48% | 0.43x |
| 11 | INJ/USD | 90.376 | 6.854 | -1.63% | 0.47x |
| 12 | UNI/USD | 89.771 | 5.1536 | -0.94% | 0.72x |

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

- Persisted scans: 1445; predictions: 12107; observations: 875107.
- Matured sampled outcomes across 1/6/24/48h: 20668; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45200172714 · **Generation:** 1445 · **Legacy run:** 45200172714
**Main quote time:** 2026-11-23T15:01:59.879328+00:00 · **Legacy report time:** 2026-11-23T15:03:08.310695+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD | 43.12 | 99.26 | -0.23% | 1.32x | STRONG 70/100 | HIGH 61/100 | Watch |
| 2 | HYPE/USD | 67.52 | 96.51 | -1.33% | 1.54x | MODERATE 68/100 | HIGH 65/100 | Do nothing |
| 3 | SOL/USD | 76.6 | 95.18 | -0.48% | 0.82x | MODERATE 53/100 | HIGH 68/100 | Watch |
| 4 | XDG/USD | 0.0590643 | 93.87 | -0.32% | 0.59x | MODERATE 52/100 | VERY_HIGH 76/100 | Watch |
| 5 | SUI/USD | 0.7142 | 93.12 | -0.60% | 0.68x | MODERATE 52/100 | VERY_HIGH 76/100 | Watch |
| 6 | XRP/USD | 0.99309 | 92.69 | -0.63% | 0.68x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 7 | ADA/USD | 0.154034 | 90.88 | -0.52% | 0.62x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 8 | NEAR/USD | 3.1721 | 90.46 | -1.37% | 1.14x | MODERATE 55/100 | VERY_HIGH 72/100 | Do nothing |
| 9 | XLM/USD | 0.135457 | 86.62 | -0.48% | 0.43x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 10 | ZEC/USD | 865.29 | 84.92 | -1.41% | 0.70x | WEAK 42/100 | EXTREME 86/100 | Do nothing |
| 11 | UNI/USD | 5.1536 | 82.27 | -0.94% | 0.72x | WEAK 41/100 | VERY_HIGH 82/100 | Watch |
| 12 | INJ/USD | 6.854 | 76.89 | -1.63% | 0.47x | WEAK 43/100 | VERY_HIGH 80/100 | Do nothing |

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
