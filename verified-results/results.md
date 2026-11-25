# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T20:25:49.450479+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45694678110
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 53d56de3d27db84f42d947eb44b8cf73751732e5 (atomic ledger/results publication)
**Ledger generation:** 1763 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.023 | 114.901 | 85.797 | +4.80% | +2.82% | 5.07x | 5.6 | 2026-11-25T20:25:41.780991+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | LTC/USD | 42.55 | 81.533 | 82.956 | +4.16% | +0.47% | 0.62x | 2.4 | 2026-11-25T20:25:41.780991+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | PUMP/USD | 0.002544 | 73.631 | 68.347 | +4.30% | +0.99% | 1.03x | 7.9 | 2026-11-25T20:25:41.780991+00:00 | Not calibrated | STRONG 72/100 | HIGH 62/100 | Watch | WATCH |
| 4 | DRV/USD | 0.3507 | 72.946 | 79.511 | +11.59% | -1.16% | 0.92x | 9.7 | 2026-11-25T20:25:41.780991+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | ZEC/USD | 759.98 | 71.611 | 73.007 | +2.85% | +0.75% | 0.49x | 3.9 | 2026-11-25T20:25:41.780991+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | HYPE/USD | 61.73 | 71.041 | 75.127 | +3.11% | +0.67% | 0.26x | 3.2 | 2026-11-25T20:25:41.780991+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SUI/USD | 0.664 | 69.398 | 71.332 | +2.55% | +0.50% | 0.56x | 3.0 | 2026-11-25T20:25:41.780991+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | AVAX/USD | 6.615 | 67.591 | 49.550 | +0.84% | +0.61% | 2.70x | 1.5 | 2026-11-25T20:25:41.780991+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 9 | CT/USD | 0.134 | 67.436 | 66.179 | +6.10% | -0.37% | 1.31x | 15.0 | 2026-11-25T20:25:41.780991+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 10 | LINK/USD | 9.10539 | 66.705 | 65.136 | +2.99% | +0.55% | 0.88x | 5.9 | 2026-11-25T20:25:41.780991+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XPL/USD | 0.0476 | 65.063 | 71.840 | +8.18% | -0.21% | 0.43x | 21.1 | 2026-11-25T20:25:41.780991+00:00 | Not calibrated | WEAK 28/100 | EXTREME 88/100 | Do nothing | WATCH |
| 12 | XRP/USD | 0.9393 | 61.543 | 66.466 | +1.70% | +0.31% | 0.35x | 0.9 | 2026-11-25T20:25:41.780991+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 85.797 | 3.023 | +2.82% | 5.07x |
| 2 | LTC/USD | 82.956 | 42.55 | +0.47% | 0.62x |
| 3 | DRV/USD | 79.511 | 0.3507 | -1.16% | 0.92x |
| 4 | HYPE/USD | 75.127 | 61.73 | +0.67% | 0.26x |
| 5 | ZEC/USD | 73.007 | 759.98 | +0.75% | 0.49x |
| 6 | XPL/USD | 71.840 | 0.0476 | -0.21% | 0.43x |
| 7 | SUI/USD | 71.332 | 0.664 | +0.50% | 0.56x |
| 8 | PUMP/USD | 68.347 | 0.002544 | +0.99% | 1.03x |
| 9 | XRP/USD | 66.466 | 0.9393 | +0.31% | 0.35x |
| 10 | CT/USD | 66.179 | 0.134 | -0.37% | 1.31x |
| 11 | LINK/USD | 65.136 | 9.10539 | +0.55% | 0.88x |
| 12 | AVAX/USD | 49.550 | 6.615 | +0.61% | 2.70x |

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

- Persisted scans: 1763; predictions: 14900; observations: 1068711.
- Matured sampled outcomes across 1/6/24/48h: 32642; gap abstentions: 22971. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45694678110 · **Generation:** 1763 · **Legacy run:** 45694678110
**Main quote time:** 2026-11-25T20:25:49.450479+00:00 · **Legacy report time:** 2026-11-25T20:26:43.459620+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.023 | 114.90 | +2.82% | 5.07x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | LTC/USD | 42.55 | 81.53 | +0.47% | 0.62x | STRONG 71/100 | VERY_HIGH 70/100 | Watch |
| 3 | PUMP/USD ⭐ | 0.002544 | 73.63 | +0.99% | 1.03x | STRONG 82/100 | HIGH 62/100 | Watch |
| 4 | DRV/USD | 0.3507 | 72.95 | -1.16% | 0.92x | WEAK 41/100 | VERY_HIGH 72/100 | Watch |
| 5 | ZEC/USD | 759.98 | 71.61 | +0.75% | 0.49x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 6 | HYPE/USD | 61.73 | 71.04 | +0.67% | 0.26x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 7 | SUI/USD | 0.664 | 69.40 | +0.50% | 0.56x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 8 | AVAX/USD | 6.615 | 67.59 | +0.61% | 2.70x | STRONG 89/100 | HIGH 55/100 | Watch |
| 9 | CT/USD | 0.134 | 67.44 | -0.37% | 1.31x | MODERATE 49/100 | VERY_HIGH 79/100 | Watch |
| 10 | LINK/USD | 9.10539 | 66.70 | +0.55% | 0.88x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 11 | XPL/USD | 0.0476 | 65.06 | -0.21% | 0.43x | WEAK 28/100 | EXTREME 88/100 | Do nothing |
| 12 | XRP/USD | 0.9393 | 61.54 | +0.31% | 0.35x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.0262 | 100.00 | +2.82% | 5.07x | 15267 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PUMP/USD ⭐ | 0.002535 | 79.60 | +0.99% | 1.03x | 5441 | STRONG 85/100 | HIGH 62/100 | Watch |
| 3 | BCH/USD | 204.62 | 76.50 | +0.75% | 1.18x | 2178 | STRONG 73/100 | HIGH 67/100 | Watch |
| 4 | INJ/USD | 6.051 | 75.58 | +1.66% | 1.22x | 6907 | STRONG 73/100 | HIGH 62/100 | Watch |

**Same-run overlap:** NEAR/USD, PUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
