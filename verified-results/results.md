# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T19:51:04.504177+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45062934511
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 15c78916d583408e928b1ccb287e2ca18b02185b (atomic ledger/results publication)
**Ledger generation:** 1328 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04821 | 103.164 | 87.853 | +8.88% | +0.06% | 5.69x | 10.4 | 2026-11-22T19:50:58.322912+00:00 | Not calibrated | STRONG 90/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 26.072 | 89.611 | 84.687 | +4.71% | +0.86% | 1.06x | 6.5 | 2026-11-22T19:50:58.322912+00:00 | Not calibrated | STRONG 80/100 | HIGH 62/100 | Watch | WATCH |
| 3 | PUMP/USD | 0.002576 | 85.555 | 81.949 | +9.90% | +0.55% | 1.09x | 7.8 | 2026-11-22T19:50:58.322912+00:00 | Not calibrated | STRONG 78/100 | HIGH 62/100 | Watch | WATCH |
| 4 | HYPE/USD | 62.25 | 80.020 | 65.742 | +1.65% | -0.14% | 5.62x | 1.6 | 2026-11-22T19:50:58.322912+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NEAR/USD | 2.9817 | 76.891 | 75.957 | +3.31% | -0.19% | 1.19x | 4.4 | 2026-11-22T19:50:58.322912+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 6 | PYTH/USD | 0.05176 | 68.301 | 65.073 | +5.91% | -0.37% | 1.51x | 15.5 | 2026-11-22T19:50:58.322912+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 7 | ETH/USD | 1712.52 | 60.891 | 67.554 | +1.80% | +0.08% | 0.30x | 0.1 | 2026-11-22T19:50:58.322912+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XBT/USD | 60622.5 | 59.399 | 61.196 | +0.89% | -0.02% | 0.83x | 0.0 | 2026-11-22T19:50:58.322912+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6543 | 54.865 | 61.675 | +1.08% | +0.02% | 0.31x | 1.5 | 2026-11-22T19:50:58.322912+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | AVAX/USD | 6.685 | 47.128 | 53.371 | +1.86% | +0.18% | 0.29x | 3.0 | 2026-11-22T19:50:58.322912+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | BNB/USD | 555.39 | 42.000 | 45.959 | +1.46% | -0.08% | 0.64x | 1.8 | 2026-11-22T19:50:58.322912+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 12 | LTC/USD | 39.88 | 41.136 | 44.515 | +0.38% | +0.15% | 0.59x | 2.5 | 2026-11-22T19:50:58.322912+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 87.853 | 0.04821 | +0.06% | 5.69x |
| 2 | VVV/USD | 84.687 | 26.072 | +0.86% | 1.06x |
| 3 | PUMP/USD | 81.949 | 0.002576 | +0.55% | 1.09x |
| 4 | NEAR/USD | 75.957 | 2.9817 | -0.19% | 1.19x |
| 5 | ETH/USD | 67.554 | 1712.52 | +0.08% | 0.30x |
| 6 | HYPE/USD | 65.742 | 62.25 | -0.14% | 5.62x |
| 7 | PYTH/USD | 65.073 | 0.05176 | -0.37% | 1.51x |
| 8 | SUI/USD | 61.675 | 0.6543 | +0.02% | 0.31x |
| 9 | XBT/USD | 61.196 | 60622.5 | -0.02% | 0.83x |
| 10 | AVAX/USD | 53.371 | 6.685 | +0.18% | 0.29x |
| 11 | BNB/USD | 45.959 | 555.39 | -0.08% | 0.64x |
| 12 | LTC/USD | 44.515 | 39.88 | +0.15% | 0.59x |

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

- Persisted scans: 1328; predictions: 10855; observations: 803860.
- Matured sampled outcomes across 1/6/24/48h: 16414; gap abstentions: 22344. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45062934511 · **Generation:** 1328 · **Legacy run:** 45062934511
**Main quote time:** 2026-11-22T19:51:04.504177+00:00 · **Legacy report time:** 2026-11-22T19:51:51.801257+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04821 | 103.16 | +0.06% | 5.69x | STRONG 100/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD ⭐ | 26.072 | 89.61 | +0.86% | 1.06x | STRONG 90/100 | HIGH 62/100 | Watch |
| 3 | PUMP/USD ⭐ | 0.002576 | 85.55 | +0.55% | 1.09x | STRONG 88/100 | HIGH 62/100 | Watch |
| 4 | HYPE/USD | 62.25 | 80.02 | -0.14% | 5.62x | STRONG 70/100 | HIGH 61/100 | Watch |
| 5 | NEAR/USD | 2.9817 | 76.89 | -0.19% | 1.19x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 6 | PYTH/USD | 0.05176 | 68.30 | -0.37% | 1.51x | MODERATE 49/100 | VERY_HIGH 79/100 | Watch |
| 7 | ETH/USD | 1712.52 | 60.89 | +0.08% | 0.30x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 8 | XBT/USD | 60622.5 | 59.40 | -0.02% | 0.83x | WEAK 35/100 | HIGH 68/100 | Watch |
| 9 | SUI/USD | 0.6543 | 54.86 | +0.02% | 0.31x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 10 | AVAX/USD | 6.685 | 47.13 | +0.18% | 0.29x | WEAK 44/100 | VERY_HIGH 70/100 | Watch |
| 11 | BNB/USD | 555.39 | 42.00 | -0.08% | 0.64x | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing |
| 12 | LTC/USD | 39.88 | 41.14 | +0.15% | 0.59x | WEAK 41/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.085 | 89.03 | +0.86% | 1.06x | 11921 | STRONG 90/100 | HIGH 62/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.04821 | 89.00 | +0.06% | 5.69x | 9838 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | DRV/USD | 0.37725 | 88.74 | +0.65% | 4.36x | 18404 | STRONG 94/100 | HIGH 61/100 | Consider small entry |
| 4 | PUMP/USD ⭐ | 0.002576 | 78.49 | +0.55% | 1.09x | 4019 | STRONG 84/100 | HIGH 62/100 | Watch |

**Same-run overlap:** NIGHT/USD, VVV/USD, PUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
