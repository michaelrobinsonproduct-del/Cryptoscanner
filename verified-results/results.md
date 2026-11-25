# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T23:15:44.777203+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45719809246
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c38ca49fd6bedd3ead750dfd83d55869d994e565 (atomic ledger/results publication)
**Ledger generation:** 1780 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 759.62 | 84.693 | 71.214 | +2.81% | +0.67% | 2.01x | 6.8 | 2026-11-25T23:15:38.141494+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 3.0254 | 83.733 | 87.541 | +4.88% | +0.11% | 0.57x | 3.3 | 2026-11-25T23:15:38.141494+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | XBT/USD | 60166.5 | 76.073 | 59.974 | +0.71% | +0.22% | 2.61x | 0.0 | 2026-11-25T23:15:38.141494+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | LTC/USD | 42.47 | 73.549 | 80.406 | +3.97% | -0.14% | 0.38x | 4.7 | 2026-11-25T23:15:38.141494+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | HYPE/USD | 61.31 | 72.753 | 71.021 | +2.41% | -0.33% | 1.34x | 1.6 | 2026-11-25T23:15:38.141494+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XMR/USD | 520.32 | 70.925 | 65.304 | +2.10% | -0.14% | 1.63x | 8.8 | 2026-11-25T23:15:38.141494+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6642 | 70.077 | 71.549 | +2.58% | +0.02% | 0.85x | 3.0 | 2026-11-25T23:15:38.141494+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 8 | PAXG/USD | 3565.82 | 65.639 | 59.421 | +0.68% | -0.45% | 1.85x | 0.6 | 2026-11-25T23:15:38.141494+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 9 | PUMP/USD | 0.00255 | 62.643 | 69.491 | +4.55% | +0.04% | 0.30x | 11.8 | 2026-11-25T23:15:38.141494+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XLM/USD | 0.127926 | 61.348 | 64.461 | +3.12% | +0.12% | 0.63x | 2.6 | 2026-11-25T23:15:38.141494+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ETH/USD | 1687.02 | 59.939 | 58.766 | +0.55% | +0.20% | 1.02x | 0.2 | 2026-11-25T23:15:38.141494+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 12 | PEPE/USD | 3.466e-06 | 58.209 | 44.073 | +0.38% | -0.17% | 4.66x | 5.8 | 2026-11-25T23:15:38.141494+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 87.541 | 3.0254 | +0.11% | 0.57x |
| 2 | LTC/USD | 80.406 | 42.47 | -0.14% | 0.38x |
| 3 | SUI/USD | 71.549 | 0.6642 | +0.02% | 0.85x |
| 4 | ZEC/USD | 71.214 | 759.62 | +0.67% | 2.01x |
| 5 | HYPE/USD | 71.021 | 61.31 | -0.33% | 1.34x |
| 6 | PUMP/USD | 69.491 | 0.00255 | +0.04% | 0.30x |
| 7 | XMR/USD | 65.304 | 520.32 | -0.14% | 1.63x |
| 8 | XLM/USD | 64.461 | 0.127926 | +0.12% | 0.63x |
| 9 | XBT/USD | 59.974 | 60166.5 | +0.22% | 2.61x |
| 10 | PAXG/USD | 59.421 | 3565.82 | -0.45% | 1.85x |
| 11 | ETH/USD | 58.766 | 1687.02 | +0.20% | 1.02x |
| 12 | PEPE/USD | 44.073 | 3.466e-06 | -0.17% | 4.66x |

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

- Persisted scans: 1780; predictions: 15104; observations: 1079064.
- Matured sampled outcomes across 1/6/24/48h: 32864; gap abstentions: 23354. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45719809246 · **Generation:** 1780 · **Legacy run:** 45719809246
**Main quote time:** 2026-11-25T23:15:44.777203+00:00 · **Legacy report time:** 2026-11-25T23:16:33.061876+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 759.62 | 84.69 | +0.67% | 2.01x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD | 3.0254 | 83.73 | +0.11% | 0.57x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 3 | XBT/USD | 60166.5 | 76.07 | +0.22% | 2.61x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 4 | LTC/USD | 42.47 | 73.55 | -0.14% | 0.38x | WEAK 42/100 | VERY_HIGH 76/100 | Watch |
| 5 | HYPE/USD | 61.31 | 72.75 | -0.33% | 1.34x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 6 | XMR/USD | 520.32 | 70.93 | -0.14% | 1.63x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 7 | SUI/USD | 0.6642 | 70.08 | +0.02% | 0.85x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 8 | PAXG/USD | 3565.82 | 65.64 | -0.45% | 1.85x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 9 | PUMP/USD | 0.00255 | 62.64 | +0.04% | 0.30x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 10 | XLM/USD | 0.127926 | 61.35 | +0.12% | 0.63x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 11 | ETH/USD | 1687.02 | 59.94 | +0.20% | 1.02x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 12 | PEPE/USD | 3.466e-06 | 58.21 | -0.17% | 4.66x | MODERATE 59/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 761 | 78.97 | +0.67% | 2.01x | 43210 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
