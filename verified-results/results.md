# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T19:01:26.919568+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45058163023
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 2178ea33d12d25632faf674d9df44f133fdaf350 (atomic ledger/results publication)
**Ledger generation:** 1323 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04891 | 98.812 | 86.454 | +10.46% | -0.53% | 2.57x | 12.3 | 2026-11-22T19:01:20.173729+00:00 | Not calibrated | STRONG 74/100 | HIGH 67/100 | Watch | WATCH |
| 2 | DRV/USD | 0.37066 | 80.250 | 80.680 | +10.58% | +0.18% | 0.87x | 17.0 | 2026-11-22T19:01:20.173729+00:00 | Not calibrated | MODERATE 55/100 | HIGH 68/100 | Watch | WATCH |
| 3 | NEAR/USD | 2.9967 | 75.261 | 78.936 | +3.83% | +0.19% | 0.54x | 5.7 | 2026-11-22T19:01:20.173729+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | PUMP/USD | 0.002544 | 73.055 | 80.052 | +8.53% | -0.20% | 0.40x | 11.8 | 2026-11-22T19:01:20.173729+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | VVV/USD | 25.875 | 71.937 | 80.283 | +3.92% | -0.65% | 0.49x | 4.3 | 2026-11-22T19:01:20.173729+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | LINK/USD | 8.8 | 70.215 | 58.627 | +2.39% | -0.05% | 2.19x | 4.2 | 2026-11-22T19:01:20.173729+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ETH/USD | 1712.1 | 65.564 | 67.379 | +1.77% | -0.03% | 0.83x | 0.1 | 2026-11-22T19:01:20.173729+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6565 | 64.287 | 64.186 | +1.42% | +0.02% | 1.00x | 1.5 | 2026-11-22T19:01:20.173729+00:00 | Not calibrated | MODERATE 57/100 | HIGH 62/100 | Watch | WATCH |
| 9 | HYPE/USD | 62.46 | 60.273 | 67.344 | +1.99% | -0.03% | 0.31x | 3.2 | 2026-11-22T19:01:20.173729+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | ZEC/USD | 788.36 | 59.270 | 61.883 | +1.31% | +0.18% | 0.65x | 4.6 | 2026-11-22T19:01:20.173729+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XBT/USD | 60656.7 | 58.705 | 61.594 | +0.94% | +0.09% | 0.67x | 0.0 | 2026-11-22T19:01:20.173729+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | BNB/USD | 557.6 | 48.447 | 49.174 | +1.86% | +0.06% | 0.90x | 1.3 | 2026-11-22T19:01:20.173729+00:00 | Not calibrated | WEAK 44/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 86.454 | 0.04891 | -0.53% | 2.57x |
| 2 | DRV/USD | 80.680 | 0.37066 | +0.18% | 0.87x |
| 3 | VVV/USD | 80.283 | 25.875 | -0.65% | 0.49x |
| 4 | PUMP/USD | 80.052 | 0.002544 | -0.20% | 0.40x |
| 5 | NEAR/USD | 78.936 | 2.9967 | +0.19% | 0.54x |
| 6 | ETH/USD | 67.379 | 1712.1 | -0.03% | 0.83x |
| 7 | HYPE/USD | 67.344 | 62.46 | -0.03% | 0.31x |
| 8 | SUI/USD | 64.186 | 0.6565 | +0.02% | 1.00x |
| 9 | ZEC/USD | 61.883 | 788.36 | +0.18% | 0.65x |
| 10 | XBT/USD | 61.594 | 60656.7 | +0.09% | 0.67x |
| 11 | LINK/USD | 58.627 | 8.8 | -0.05% | 2.19x |
| 12 | BNB/USD | 49.174 | 557.6 | +0.06% | 0.90x |

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

- Persisted scans: 1323; predictions: 10795; observations: 800815.
- Matured sampled outcomes across 1/6/24/48h: 16234; gap abstentions: 22342. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45058163023 · **Generation:** 1323 · **Legacy run:** 45058163023
**Main quote time:** 2026-11-22T19:01:26.919568+00:00 · **Legacy report time:** 2026-11-22T19:02:24.335435+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04891 | 98.81 | -0.53% | 2.57x | STRONG 74/100 | HIGH 67/100 | Watch |
| 2 | DRV/USD | 0.37066 | 80.25 | +0.18% | 0.87x | MODERATE 55/100 | HIGH 68/100 | Watch |
| 3 | NEAR/USD | 2.9967 | 75.26 | +0.19% | 0.54x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 4 | PUMP/USD | 0.002544 | 73.05 | -0.20% | 0.40x | WEAK 37/100 | VERY_HIGH 82/100 | Watch |
| 5 | VVV/USD | 25.875 | 71.94 | -0.65% | 0.49x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 6 | LINK/USD | 8.8 | 70.22 | -0.05% | 2.19x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 7 | ETH/USD | 1712.1 | 65.56 | -0.03% | 0.83x | WEAK 38/100 | HIGH 68/100 | Watch |
| 8 | SUI/USD | 0.6565 | 64.29 | +0.02% | 1.00x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 9 | HYPE/USD | 62.46 | 60.27 | -0.03% | 0.31x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | ZEC/USD | 788.36 | 59.27 | +0.18% | 0.65x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 11 | XBT/USD | 60656.7 | 58.70 | +0.09% | 0.67x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 12 | BNB/USD | 557.6 | 48.45 | +0.06% | 0.90x | WEAK 44/100 | HIGH 62/100 | Watch |

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
