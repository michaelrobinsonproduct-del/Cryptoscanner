# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T16:00:33.326893+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44561013248
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 80e69866daa890be116008e1ce31d2e3dbab0773 (atomic ledger/results publication)
**Ledger generation:** 808 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 596; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BMT/USD | 0.02011 | 89.680 | 73.685 | +6.51% | +0.20% | 5.60x | 5.0 | 2026-11-19T16:00:24.182970+00:00 | Not calibrated | STRONG 90/100 | HIGH 67/100 | Watch | WATCH |
| 2 | SYRUP/USD | 0.10287 | 84.825 | 69.645 | +8.33% | +0.78% | 2.13x | 13.6 | 2026-11-19T16:00:24.182970+00:00 | Not calibrated | STRONG 92/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | PYTH/USD | 0.05653 | 83.959 | 71.882 | +7.15% | +0.82% | 1.80x | 10.6 | 2026-11-19T16:00:24.182970+00:00 | Not calibrated | STRONG 82/100 | HIGH 66/100 | Consider small entry | WATCH |
| 4 | VVV/USD | 22.537 | 80.600 | 79.870 | +4.00% | +0.82% | 0.66x | 6.2 | 2026-11-19T16:00:24.182970+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | USELESS/USD | 0.10114 | 80.004 | 64.360 | +5.84% | +0.13% | 3.48x | 27.8 | 2026-11-19T16:00:24.182970+00:00 | Not calibrated | STRONG 75/100 | HIGH 67/100 | Watch | WATCH |
| 6 | ZEC/USD | 922.27 | 74.170 | 62.867 | +1.13% | +0.11% | 2.08x | 0.1 | 2026-11-19T16:00:24.182970+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 7 | HYPE/USD | 67.91 | 72.677 | 63.571 | +1.54% | +0.15% | 1.84x | 4.4 | 2026-11-19T16:00:24.182970+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 8 | SKR/USD | 0.010558 | 68.464 | 62.223 | +9.60% | +1.81% | 0.72x | 27.6 | 2026-11-19T16:00:24.182970+00:00 | Not calibrated | MODERATE 54/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | AKT/USD | 0.5477 | 67.394 | 67.984 | +5.73% | -0.07% | 0.98x | 7.3 | 2026-11-19T16:00:24.182970+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 10 | ADA/USD | 0.152492 | 65.952 | 58.794 | +0.82% | +0.26% | 1.59x | 3.9 | 2026-11-19T16:00:24.182970+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 11 | INJ/USD | 7.09 | 63.084 | 52.131 | +1.56% | +0.18% | 2.00x | 4.2 | 2026-11-19T16:00:24.182970+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 12 | ETH/USD | 1780.08 | 62.366 | 57.070 | +0.30% | +0.34% | 1.36x | 0.1 | 2026-11-19T16:00:24.182970+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 79.870 | 22.537 | +0.82% | 0.66x |
| 2 | BMT/USD | 73.685 | 0.02011 | +0.20% | 5.60x |
| 3 | PYTH/USD | 71.882 | 0.05653 | +0.82% | 1.80x |
| 4 | SYRUP/USD | 69.645 | 0.10287 | +0.78% | 2.13x |
| 5 | AKT/USD | 67.984 | 0.5477 | -0.07% | 0.98x |
| 6 | USELESS/USD | 64.360 | 0.10114 | +0.13% | 3.48x |
| 7 | HYPE/USD | 63.571 | 67.91 | +0.15% | 1.84x |
| 8 | ZEC/USD | 62.867 | 922.27 | +0.11% | 2.08x |
| 9 | SKR/USD | 62.223 | 0.010558 | +1.81% | 0.72x |
| 10 | ADA/USD | 58.794 | 0.152492 | +0.26% | 1.59x |
| 11 | ETH/USD | 57.070 | 1780.08 | +0.34% | 1.36x |
| 12 | INJ/USD | 52.131 | 7.09 | +0.18% | 2.00x |

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

- Persisted scans: 808; predictions: 6840; observations: 488603.
- Matured sampled outcomes across 1/6/24/48h: 6839; gap abstentions: 15282. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44561013248 · **Generation:** 808 · **Legacy run:** 44561013248
**Main quote time:** 2026-11-19T16:00:33.326893+00:00 · **Legacy report time:** 2026-11-19T16:01:15.493414+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BMT/USD ⭐ | 0.02011 | 89.68 | +0.20% | 5.60x | STRONG 100/100 | HIGH 67/100 | Watch |
| 2 | SYRUP/USD ⭐ | 0.10287 | 84.83 | +0.78% | 2.13x | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 3 | PYTH/USD ⭐ | 0.05653 | 83.96 | +0.82% | 1.80x | STRONG 92/100 | HIGH 66/100 | Consider small entry |
| 4 | VVV/USD | 22.537 | 80.60 | +0.82% | 0.66x | STRONG 70/100 | VERY_HIGH 70/100 | Watch |
| 5 | USELESS/USD ⭐ | 0.10114 | 80.00 | +0.13% | 3.48x | STRONG 85/100 | HIGH 67/100 | Watch |
| 6 | ZEC/USD | 922.27 | 74.17 | +0.11% | 2.08x | STRONG 82/100 | HIGH 55/100 | Watch |
| 7 | HYPE/USD ⭐ | 67.91 | 72.68 | +0.15% | 1.84x | STRONG 81/100 | HIGH 55/100 | Watch |
| 8 | SKR/USD | 0.010558 | 68.46 | +1.81% | 0.72x | MODERATE 54/100 | EXTREME 94/100 | Do nothing |
| 9 | AKT/USD | 0.5477 | 67.39 | -0.07% | 0.98x | WEAK 39/100 | VERY_HIGH 80/100 | Watch |
| 10 | ADA/USD | 0.152492 | 65.95 | +0.26% | 1.59x | STRONG 78/100 | HIGH 55/100 | Watch |
| 11 | INJ/USD ⭐ | 7.09 | 63.08 | +0.18% | 2.00x | STRONG 87/100 | HIGH 55/100 | Watch |
| 12 | ETH/USD | 1780.08 | 62.37 | +0.34% | 1.36x | STRONG 76/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BMT/USD ⭐ | 0.0201 | 84.37 | +0.20% | 5.60x | 2932 | STRONG 97/100 | HIGH 67/100 | Watch |
| 2 | USELESS/USD ⭐ | 0.10114 | 82.79 | +0.13% | 3.48x | 3288 | STRONG 91/100 | HIGH 61/100 | Watch |
| 3 | PYTH/USD ⭐ | 0.05669 | 76.99 | +0.82% | 1.80x | 2721 | STRONG 88/100 | HIGH 66/100 | Consider small entry |
| 4 | SYRUP/USD ⭐ | 0.10287 | 71.26 | +0.78% | 2.13x | 1864 | STRONG 96/100 | VERY_HIGH 73/100 | Watch |
| 5 | HYPE/USD ⭐ | 67.85 | 67.29 | +0.15% | 1.84x | 13064 | STRONG 79/100 | HIGH 55/100 | Watch |
| 6 | INJ/USD ⭐ | 7.081 | 63.91 | +0.18% | 2.00x | 6830 | STRONG 87/100 | HIGH 55/100 | Watch |

**Same-run overlap:** BMT/USD, SYRUP/USD, PYTH/USD, USELESS/USD, HYPE/USD, INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
