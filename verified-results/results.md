# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T23:21:21.846660+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45082633715
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 623b2041e33429836ac151c8403b828ce6247259 (atomic ledger/results publication)
**Ledger generation:** 1349 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04949 | 103.420 | 93.009 | +11.77% | -0.48% | 2.28x | 4.0 | 2026-11-22T23:21:13.576581+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 26.421 | 96.122 | 91.774 | +6.11% | +0.41% | 1.23x | 9.5 | 2026-11-22T23:21:13.576581+00:00 | Not calibrated | STRONG 83/100 | HIGH 62/100 | Watch | WATCH |
| 3 | PUMP/USD | 0.002571 | 92.674 | 81.010 | +9.68% | -0.31% | 2.32x | 11.7 | 2026-11-22T23:21:13.576581+00:00 | Not calibrated | STRONG 71/100 | HIGH 67/100 | Watch | WATCH |
| 4 | DRV/USD | 0.37042 | 86.598 | 88.664 | +10.51% | +0.04% | 0.77x | 0.3 | 2026-11-22T23:21:13.576581+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 5 | PEARL/USD | 2.0571 | 84.904 | 79.121 | +5.58% | +0.48% | 1.34x | 0.5 | 2026-11-22T23:21:13.576581+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XBT/USD | 61014.7 | 75.019 | 65.765 | +1.54% | -0.15% | 2.00x | 0.0 | 2026-11-22T23:21:13.576581+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ETH/USD | 1722.21 | 73.041 | 71.586 | +2.37% | +0.07% | 1.11x | 0.1 | 2026-11-22T23:21:13.576581+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 8 | PIEVERSE/USD | 3.66 | 72.516 | 77.043 | +7.55% | +0.19% | 0.45x | 17.2 | 2026-11-22T23:21:13.576581+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XMR/USD | 494.22 | 69.566 | 54.607 | +0.49% | -0.01% | 3.78x | 7.7 | 2026-11-22T23:21:13.576581+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 10 | HYPE/USD | 62.74 | 68.710 | 70.551 | +2.45% | +0.14% | 0.74x | 3.2 | 2026-11-22T23:21:13.576581+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | NEAR/USD | 2.9749 | 64.600 | 74.637 | +3.07% | -0.21% | 0.10x | 3.7 | 2026-11-22T23:21:13.576581+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | PAXG/USD | 3574.89 | 64.013 | 47.920 | +0.78% | +0.22% | 26.00x | 1.5 | 2026-11-22T23:21:13.576581+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 93.009 | 0.04949 | -0.48% | 2.28x |
| 2 | VVV/USD | 91.774 | 26.421 | +0.41% | 1.23x |
| 3 | DRV/USD | 88.664 | 0.37042 | +0.04% | 0.77x |
| 4 | PUMP/USD | 81.010 | 0.002571 | -0.31% | 2.32x |
| 5 | PEARL/USD | 79.121 | 2.0571 | +0.48% | 1.34x |
| 6 | PIEVERSE/USD | 77.043 | 3.66 | +0.19% | 0.45x |
| 7 | NEAR/USD | 74.637 | 2.9749 | -0.21% | 0.10x |
| 8 | ETH/USD | 71.586 | 1722.21 | +0.07% | 1.11x |
| 9 | HYPE/USD | 70.551 | 62.74 | +0.14% | 0.74x |
| 10 | XBT/USD | 65.765 | 61014.7 | -0.15% | 2.00x |
| 11 | XMR/USD | 54.607 | 494.22 | -0.01% | 3.78x |
| 12 | PAXG/USD | 47.920 | 3574.89 | +0.22% | 26.00x |

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

- Persisted scans: 1349; predictions: 11107; observations: 816648.
- Matured sampled outcomes across 1/6/24/48h: 17182; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 62 (sampled only; not a success-rate estimate).
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

**Writer:** 45082633715 · **Generation:** 1349 · **Legacy run:** 45082633715
**Main quote time:** 2026-11-22T23:21:21.846660+00:00 · **Legacy report time:** 2026-11-22T23:22:29.284926+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04949 | 103.42 | -0.48% | 2.28x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD ⭐ | 26.421 | 96.12 | +0.41% | 1.23x | STRONG 93/100 | HIGH 62/100 | Watch |
| 3 | PUMP/USD | 0.002571 | 92.67 | -0.31% | 2.32x | STRONG 71/100 | HIGH 67/100 | Watch |
| 4 | DRV/USD | 0.37042 | 86.60 | +0.04% | 0.77x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 5 | PEARL/USD ⭐ | 2.0571 | 84.90 | +0.48% | 1.34x | STRONG 97/100 | HIGH 55/100 | Watch |
| 6 | XBT/USD | 61014.7 | 75.02 | -0.15% | 2.00x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 7 | ETH/USD ⭐ | 1722.21 | 73.04 | +0.07% | 1.11x | STRONG 72/100 | HIGH 62/100 | Watch |
| 8 | PIEVERSE/USD | 3.66 | 72.52 | +0.19% | 0.45x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 9 | XMR/USD | 494.22 | 69.57 | -0.01% | 3.78x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 10 | HYPE/USD | 62.74 | 68.71 | +0.14% | 0.74x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 11 | NEAR/USD | 2.9749 | 64.60 | -0.21% | 0.10x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 12 | PAXG/USD | 3574.89 | 64.01 | +0.22% | 26.00x | STRONG 87/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 2.0604 | 90.12 | +0.48% | 1.34x | 6118 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | VVV/USD ⭐ | 26.378 | 86.38 | +0.41% | 1.23x | 11511 | STRONG 88/100 | HIGH 62/100 | Watch |
| 3 | ETH/USD ⭐ | 1719.17 | 75.13 | +0.07% | 1.11x | 39928 | STRONG 73/100 | HIGH 62/100 | Watch |

**Same-run overlap:** VVV/USD, PEARL/USD, ETH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
