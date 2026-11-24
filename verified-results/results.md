# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T20:17:01.957349+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45478722740
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 11ab8188dcc5114ac01d1ccd49f3e51056403494 (atomic ledger/results publication)
**Ledger generation:** 1621 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 500.09 | 76.138 | 69.757 | +2.89% | -0.05% | 1.66x | 11.0 | 2026-11-24T20:16:58.547185+00:00 | Not calibrated | MODERATE 53/100 | HIGH 67/100 | Watch | WATCH |
| 2 | GBP/USD | 1.31143 | 61.950 | 59.241 | +0.63% | +0.01% | 1.26x | 0.3 | 2026-11-24T20:16:58.547185+00:00 | Not calibrated | MODERATE 56/100 | HIGH 55/100 | Watch | WATCH |
| 3 | 2Z/USD | 0.01626 | 59.263 | 45.794 | +3.90% | -0.31% | 2.58x | 24.6 | 2026-11-24T20:16:58.547185+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 85/100 | Do nothing | WATCH |
| 4 | AUD/USD | 0.66479 | 57.946 | 42.878 | +0.33% | +0.01% | 15.30x | 5.9 | 2026-11-24T20:16:58.547185+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ZEUS/USD | 0.00465 | 57.669 | 53.221 | +6.16% | +2.20% | 0.35x | 43.1 | 2026-11-24T20:16:58.547185+00:00 | Not calibrated | WEAK 44/100 | EXTREME 100/100 | Do nothing | WATCH |
| 6 | NIGHT/USD | 0.04872 | 53.350 | 47.893 | +1.18% | +0.23% | 1.43x | 2.1 | 2026-11-24T20:16:58.547185+00:00 | Not calibrated | STRONG 72/100 | HIGH 55/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.447e-06 | 45.158 | 45.490 | +0.73% | +0.29% | 0.82x | 5.8 | 2026-11-24T20:16:58.547185+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 69.757 | 500.09 | -0.05% | 1.66x |
| 2 | GBP/USD | 59.241 | 1.31143 | +0.01% | 1.26x |
| 3 | ZEUS/USD | 53.221 | 0.00465 | +2.20% | 0.35x |
| 4 | NIGHT/USD | 47.893 | 0.04872 | +0.23% | 1.43x |
| 5 | 2Z/USD | 45.794 | 0.01626 | -0.31% | 2.58x |
| 6 | PEPE/USD | 45.490 | 3.447e-06 | +0.29% | 0.82x |
| 7 | AUD/USD | 42.878 | 0.66479 | +0.01% | 15.30x |

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

- Persisted scans: 1621; predictions: 13910; observations: 982281.
- Matured sampled outcomes across 1/6/24/48h: 28347; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45478722740 · **Generation:** 1621 · **Legacy run:** 45478722740
**Main quote time:** 2026-11-24T20:17:01.957349+00:00 · **Legacy report time:** 2026-11-24T20:18:12.178512+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 500.09 | 76.14 | -0.05% | 1.66x | MODERATE 53/100 | HIGH 67/100 | Watch |
| 2 | GBP/USD | 1.31143 | 61.95 | +0.01% | 1.26x | MODERATE 56/100 | HIGH 55/100 | Watch |
| 3 | 2Z/USD | 0.01626 | 59.26 | -0.31% | 2.58x | MODERATE 50/100 | EXTREME 85/100 | Do nothing |
| 4 | AUD/USD | 0.66479 | 57.95 | +0.01% | 15.30x | STRONG 74/100 | HIGH 55/100 | Watch |
| 5 | ZEUS/USD | 0.00465 | 57.67 | +2.20% | 0.35x | WEAK 44/100 | EXTREME 100/100 | Do nothing |
| 6 | NIGHT/USD ⭐ | 0.04872 | 53.35 | +0.23% | 1.43x | STRONG 82/100 | HIGH 55/100 | Watch |
| 7 | PEPE/USD | 3.447e-06 | 45.16 | +0.29% | 0.82x | MODERATE 53/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04872 | 51.78 | +0.23% | 1.43x | 9301 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
