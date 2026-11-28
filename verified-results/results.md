# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T03:47:37.489148+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46104289478
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8cfb435c90bdd8b5d8f5d0b2c3d43a8d43360d4d (atomic ledger/results publication)
**Ledger generation:** 2101 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 419.07 | 69.512 | 68.593 | +2.90% | +0.86% | 0.66x | 13.4 | 2026-11-28T03:47:32.409119+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | HYPE/USD | 64.17 | 63.224 | 61.718 | +1.07% | +0.33% | 0.99x | 1.6 | 2026-11-28T03:47:32.409119+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 3 | ZEC/USD | 747.15 | 61.826 | 64.377 | +1.71% | +0.37% | 0.56x | 5.2 | 2026-11-28T03:47:32.409119+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | CC/USD | 0.07572 | 54.716 | 46.129 | +2.12% | +0.05% | 1.83x | 6.6 | 2026-11-28T03:47:32.409119+00:00 | Not calibrated | MODERATE 62/100 | HIGH 60/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.045 | 54.522 | 59.738 | +0.89% | +0.10% | 0.43x | 3.0 | 2026-11-28T03:47:32.409119+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | BCH/USD | 209.03 | 50.426 | 42.218 | +0.98% | +0.01% | 1.81x | 3.3 | 2026-11-28T03:47:32.409119+00:00 | Not calibrated | MODERATE 60/100 | HIGH 55/100 | Watch | WATCH |
| 7 | VVV/USD | 26.022 | 47.941 | 46.343 | +1.06% | -0.02% | 1.17x | 15.0 | 2026-11-28T03:47:32.409119+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 8 | SENT/USD | 0.024232 | 44.474 | 45.144 | +2.18% | +0.12% | 0.87x | 2.1 | 2026-11-28T03:47:32.409119+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 9 | SPX/USD | 0.2739 | 42.030 | 24.830 | +0.55% | +0.44% | 3.83x | 21.9 | 2026-11-28T03:47:32.409119+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 72/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 68.593 | 419.07 | +0.86% | 0.66x |
| 2 | ZEC/USD | 64.377 | 747.15 | +0.37% | 0.56x |
| 3 | HYPE/USD | 61.718 | 64.17 | +0.33% | 0.99x |
| 4 | NEAR/USD | 59.738 | 3.045 | +0.10% | 0.43x |
| 5 | VVV/USD | 46.343 | 26.022 | -0.02% | 1.17x |
| 6 | CC/USD | 46.129 | 0.07572 | +0.05% | 1.83x |
| 7 | SENT/USD | 45.144 | 0.024232 | +0.12% | 0.87x |
| 8 | BCH/USD | 42.218 | 209.03 | +0.01% | 1.81x |
| 9 | SPX/USD | 24.830 | 0.2739 | +0.44% | 3.83x |

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

- Persisted scans: 2101; predictions: 18864; observations: 1272252.
- Matured sampled outcomes across 1/6/24/48h: 43646; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46104289478 · **Generation:** 2101 · **Legacy run:** 46104289478
**Main quote time:** 2026-11-28T03:47:37.489148+00:00 · **Legacy report time:** 2026-11-28T03:48:35.189307+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 419.07 | 69.51 | +0.86% | 0.66x | MODERATE 60/100 | VERY_HIGH 76/100 | Watch |
| 2 | HYPE/USD | 64.17 | 63.22 | +0.33% | 0.99x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 3 | ZEC/USD | 747.15 | 61.83 | +0.37% | 0.56x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 4 | CC/USD ⭐ | 0.07572 | 54.72 | +0.05% | 1.83x | STRONG 72/100 | HIGH 60/100 | Watch |
| 5 | NEAR/USD | 3.045 | 54.52 | +0.10% | 0.43x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 6 | BCH/USD | 209.03 | 50.43 | +0.01% | 1.81x | MODERATE 60/100 | HIGH 55/100 | Watch |
| 7 | VVV/USD | 26.022 | 47.94 | -0.02% | 1.17x | WEAK 29/100 | VERY_HIGH 74/100 | Do nothing |
| 8 | SENT/USD | 0.024232 | 44.47 | +0.12% | 0.87x | WEAK 42/100 | VERY_HIGH 74/100 | Watch |
| 9 | SPX/USD | 0.2739 | 42.03 | +0.44% | 3.83x | MODERATE 66/100 | VERY_HIGH 72/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.07568 | 53.01 | +0.05% | 1.83x | 5304 | STRONG 72/100 | HIGH 60/100 | Watch |

**Same-run overlap:** CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
