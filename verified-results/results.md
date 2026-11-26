# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T09:16:10.830067+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45790143204
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 90768b3c2a9d67e6522141df37909b0d3fba74fb (atomic ledger/results publication)
**Ledger generation:** 1841 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 6.26 | 91.702 | 76.061 | +5.14% | +0.13% | 3.05x | 6.4 | 2026-11-26T09:16:04.131041+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 2 | LINK/USD | 9.24353 | 84.443 | 69.201 | +2.20% | +0.05% | 6.49x | 2.4 | 2026-11-26T09:16:04.131041+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XRP/USD | 0.95364 | 81.740 | 67.713 | +1.82% | -0.19% | 2.82x | 0.1 | 2026-11-26T09:16:04.131041+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SOL/USD | 70.96 | 75.034 | 59.964 | +0.81% | +0.01% | 3.82x | 1.4 | 2026-11-26T09:16:04.131041+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 5 | ETH/USD | 1698.3 | 73.517 | 58.238 | +0.47% | +0.06% | 4.50x | 0.1 | 2026-11-26T09:16:04.131041+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0566178 | 73.142 | 58.347 | +1.18% | -0.04% | 3.92x | 0.5 | 2026-11-26T09:16:04.131041+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ADA/USD | 0.148736 | 71.828 | 67.629 | +2.03% | +0.14% | 1.35x | 3.2 | 2026-11-26T09:16:04.131041+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6694 | 71.017 | 56.763 | +0.47% | -0.15% | 4.92x | 3.0 | 2026-11-26T09:16:04.131041+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 9 | LTC/USD | 43.72 | 69.682 | 70.410 | +2.36% | +0.39% | 0.73x | 2.3 | 2026-11-26T09:16:04.131041+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SEI/USD | 0.03575 | 68.587 | 71.543 | +7.33% | +0.37% | 0.52x | 11.2 | 2026-11-26T09:16:04.131041+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | SKY/USD | 0.04387 | 66.319 | 63.553 | +4.75% | +0.43% | 1.06x | 6.8 | 2026-11-26T09:16:04.131041+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 12 | ME/USD | 0.0396 | 64.379 | 64.077 | +7.32% | +0.00% | 1.03x | 25.3 | 2026-11-26T09:16:04.131041+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 79/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 76.061 | 6.26 | +0.13% | 3.05x |
| 2 | SEI/USD | 71.543 | 0.03575 | +0.37% | 0.52x |
| 3 | LTC/USD | 70.410 | 43.72 | +0.39% | 0.73x |
| 4 | LINK/USD | 69.201 | 9.24353 | +0.05% | 6.49x |
| 5 | XRP/USD | 67.713 | 0.95364 | -0.19% | 2.82x |
| 6 | ADA/USD | 67.629 | 0.148736 | +0.14% | 1.35x |
| 7 | ME/USD | 64.077 | 0.0396 | +0.00% | 1.03x |
| 8 | SKY/USD | 63.553 | 0.04387 | +0.43% | 1.06x |
| 9 | SOL/USD | 59.964 | 70.96 | +0.01% | 3.82x |
| 10 | XDG/USD | 58.347 | 0.0566178 | -0.04% | 3.92x |
| 11 | ETH/USD | 58.238 | 1698.3 | +0.06% | 4.50x |
| 12 | SUI/USD | 56.763 | 0.6694 | -0.15% | 4.92x |

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

- Persisted scans: 1841; predictions: 15827; observations: 1116211.
- Matured sampled outcomes across 1/6/24/48h: 34286; gap abstentions: 24427. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45790143204 · **Generation:** 1841 · **Legacy run:** 45790143204
**Main quote time:** 2026-11-26T09:16:10.830067+00:00 · **Legacy report time:** 2026-11-26T09:17:14.851904+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.26 | 91.70 | +0.13% | 3.05x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | LINK/USD | 9.24353 | 84.44 | +0.05% | 6.49x | STRONG 87/100 | HIGH 55/100 | Watch |
| 3 | XRP/USD | 0.95364 | 81.74 | -0.19% | 2.82x | STRONG 71/100 | HIGH 61/100 | Watch |
| 4 | SOL/USD | 70.96 | 75.03 | +0.01% | 3.82x | STRONG 83/100 | HIGH 55/100 | Watch |
| 5 | ETH/USD | 1698.3 | 73.52 | +0.06% | 4.50x | STRONG 82/100 | HIGH 55/100 | Watch |
| 6 | XDG/USD | 0.0566178 | 73.14 | -0.04% | 3.92x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 7 | ADA/USD ⭐ | 0.148736 | 71.83 | +0.14% | 1.35x | STRONG 81/100 | HIGH 55/100 | Watch |
| 8 | SUI/USD | 0.6694 | 71.02 | -0.15% | 4.92x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 9 | LTC/USD | 43.72 | 69.68 | +0.39% | 0.73x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 10 | SEI/USD | 0.03575 | 68.59 | +0.37% | 0.52x | MODERATE 59/100 | VERY_HIGH 81/100 | Watch |
| 11 | SKY/USD ⭐ | 0.04387 | 66.32 | +0.43% | 1.06x | STRONG 78/100 | HIGH 67/100 | Watch |
| 12 | ME/USD | 0.0396 | 64.38 | +0.00% | 1.03x | MODERATE 47/100 | VERY_HIGH 79/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.253 | 86.35 | +0.13% | 3.05x | 6926 | STRONG 98/100 | HIGH 55/100 | Watch |
| 2 | SKY/USD ⭐ | 0.0439 | 75.07 | +0.43% | 1.06x | 4146 | STRONG 83/100 | HIGH 67/100 | Watch |
| 3 | ADA/USD ⭐ | 0.148848 | 69.61 | +0.14% | 1.35x | 12522 | STRONG 80/100 | HIGH 55/100 | Watch |

**Same-run overlap:** INJ/USD, ADA/USD, SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
