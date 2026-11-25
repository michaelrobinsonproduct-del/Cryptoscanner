# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T18:58:54.229573+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45679886529
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9f927badfc303027ae1f0e1ae59e191b9a00d819 (atomic ledger/results publication)
**Ledger generation:** 1753 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.62 | 99.118 | 95.500 | +8.48% | +0.35% | 1.19x | 9.0 | 2026-11-25T18:58:46.325775+00:00 | Not calibrated | STRONG 85/100 | HIGH 62/100 | Watch | WATCH |
| 2 | ZEC/USD | 751.27 | 73.251 | 64.464 | +1.68% | +0.34% | 1.71x | 4.5 | 2026-11-25T18:58:46.325775+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | DRV/USD | 0.35071 | 71.026 | 72.134 | +11.59% | +0.50% | 0.64x | 24.0 | 2026-11-25T18:58:46.325775+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | LTC/USD | 42.09 | 69.528 | 75.061 | +3.04% | +0.57% | 0.16x | 2.4 | 2026-11-25T18:58:46.325775+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | XPL/USD | 0.0476 | 66.507 | 71.175 | +8.18% | -0.42% | 0.74x | 21.0 | 2026-11-25T18:58:46.325775+00:00 | Not calibrated | WEAK 28/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | XMR/USD | 514.37 | 64.479 | 59.121 | +0.94% | -0.38% | 1.72x | 4.9 | 2026-11-25T18:58:46.325775+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 7 | HYPE/USD | 60.48 | 61.745 | 60.479 | +1.02% | +0.38% | 0.94x | 3.3 | 2026-11-25T18:58:46.325775+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6557 | 60.839 | 62.340 | +1.27% | +0.58% | 0.56x | 3.0 | 2026-11-25T18:58:46.325775+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | BCH/USD | 202.29 | 59.099 | 50.881 | +2.60% | +0.65% | 1.50x | 3.5 | 2026-11-25T18:58:46.325775+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |
| 10 | NEAR/USD | 2.8931 | 56.453 | 55.531 | +0.30% | +0.75% | 0.72x | 3.1 | 2026-11-25T18:58:46.325775+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | LINK/USD | 8.99967 | 55.511 | 55.944 | +1.79% | +0.84% | 0.54x | 6.1 | 2026-11-25T18:58:46.325775+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XRP/USD | 0.92819 | 54.298 | 58.202 | +0.50% | +0.43% | 0.39x | 0.5 | 2026-11-25T18:58:46.325775+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 95.500 | 26.62 | +0.35% | 1.19x |
| 2 | LTC/USD | 75.061 | 42.09 | +0.57% | 0.16x |
| 3 | DRV/USD | 72.134 | 0.35071 | +0.50% | 0.64x |
| 4 | XPL/USD | 71.175 | 0.0476 | -0.42% | 0.74x |
| 5 | ZEC/USD | 64.464 | 751.27 | +0.34% | 1.71x |
| 6 | SUI/USD | 62.340 | 0.6557 | +0.58% | 0.56x |
| 7 | HYPE/USD | 60.479 | 60.48 | +0.38% | 0.94x |
| 8 | XMR/USD | 59.121 | 514.37 | -0.38% | 1.72x |
| 9 | XRP/USD | 58.202 | 0.92819 | +0.43% | 0.39x |
| 10 | LINK/USD | 55.944 | 8.99967 | +0.84% | 0.54x |
| 11 | NEAR/USD | 55.531 | 2.8931 | +0.75% | 0.72x |
| 12 | BCH/USD | 50.881 | 202.29 | +0.65% | 1.50x |

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

- Persisted scans: 1753; predictions: 14780; observations: 1062621.
- Matured sampled outcomes across 1/6/24/48h: 32535; gap abstentions: 22760. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45679886529 · **Generation:** 1753 · **Legacy run:** 45679886529
**Main quote time:** 2026-11-25T18:58:54.229573+00:00 · **Legacy report time:** 2026-11-25T19:00:10.628902+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.62 | 99.12 | +0.35% | 1.19x | STRONG 95/100 | HIGH 62/100 | Watch |
| 2 | ZEC/USD ⭐ | 751.27 | 73.25 | +0.34% | 1.71x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 3 | DRV/USD | 0.35071 | 71.03 | +0.50% | 0.64x | MODERATE 56/100 | VERY_HIGH 82/100 | Watch |
| 4 | LTC/USD | 42.09 | 69.53 | +0.57% | 0.16x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 5 | XPL/USD | 0.0476 | 66.51 | -0.42% | 0.74x | WEAK 28/100 | EXTREME 88/100 | Do nothing |
| 6 | XMR/USD | 514.37 | 64.48 | -0.38% | 1.72x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 7 | HYPE/USD | 60.48 | 61.74 | +0.38% | 0.94x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 8 | SUI/USD | 0.6557 | 60.84 | +0.58% | 0.56x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 9 | BCH/USD ⭐ | 202.29 | 59.10 | +0.65% | 1.50x | STRONG 85/100 | HIGH 60/100 | Watch |
| 10 | NEAR/USD | 2.8931 | 56.45 | +0.75% | 0.72x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 11 | LINK/USD | 8.99967 | 55.51 | +0.84% | 0.54x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 12 | XRP/USD | 0.92819 | 54.30 | +0.43% | 0.39x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.6 | 85.93 | +0.14% | 1.13x | 10915 | STRONG 78/100 | HIGH 62/100 | Watch |
| 2 | ZEC/USD ⭐ | 749.87 | 67.11 | +0.84% | 2.76x | 37482 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 3 | BCH/USD ⭐ | 202.29 | 64.09 | +0.54% | 1.48x | 2118 | STRONG 87/100 | HIGH 60/100 | Watch |

**Same-run overlap:** VVV/USD, ZEC/USD, BCH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
