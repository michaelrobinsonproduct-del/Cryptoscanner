# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T01:55:18.760193+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44440400784
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 2e66b65e1d83b2b8bcde996bfae64d1ea79cd729 (atomic ledger/results publication)
**Ledger generation:** 724 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LUNA/USD | 4.55e-05 | 68.683 | 62.584 | +4.50% | +2.48% | 0.37x | 2.2 | 2026-11-19T01:55:11.873966+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 2 | SENT/USD | 0.021671 | 59.904 | 63.543 | +5.17% | +0.57% | 0.35x | 8.3 | 2026-11-19T01:55:11.873966+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | TRX/USD | 0.310263 | 56.205 | 40.770 | +0.32% | +0.09% | 6.57x | 1.5 | 2026-11-19T01:55:11.873966+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 4 | DRV/USD | 0.26623 | 47.535 | 32.103 | +0.58% | +0.09% | 4.20x | 10.5 | 2026-11-19T01:55:11.873966+00:00 | Not calibrated | MODERATE 64/100 | HIGH 66/100 | Watch | WATCH |
| 5 | PYTH/USD | 0.05362 | 39.504 | 38.462 | +1.63% | +0.47% | 0.87x | 9.4 | 2026-11-19T01:55:11.873966+00:00 | Not calibrated | MODERATE 50/100 | HIGH 67/100 | Watch | WATCH |
| 6 | PAXG/USD | 3743.07 | 35.672 | 43.943 | +0.32% | +0.17% | 0.09x | 1.1 | 2026-11-19T01:55:11.873966+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | MEGA/USD | 0.05725 | 33.911 | 40.753 | +2.23% | -0.75% | 0.69x | 12.2 | 2026-11-19T01:55:11.873966+00:00 | Not calibrated | WEAK 17/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 63.543 | 0.021671 | +0.57% | 0.35x |
| 2 | LUNA/USD | 62.584 | 4.55e-05 | +2.48% | 0.37x |
| 3 | PAXG/USD | 43.943 | 3743.07 | +0.17% | 0.09x |
| 4 | TRX/USD | 40.770 | 0.310263 | +0.09% | 6.57x |
| 5 | MEGA/USD | 40.753 | 0.05725 | -0.75% | 0.69x |
| 6 | PYTH/USD | 38.462 | 0.05362 | +0.47% | 0.87x |
| 7 | DRV/USD | 32.103 | 0.26623 | +0.09% | 4.20x |

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

- Persisted scans: 724; predictions: 5871; observations: 437923.
- Matured sampled outcomes across 1/6/24/48h: 5787; gap abstentions: 13466. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 17; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44440400784 · **Generation:** 724 · **Legacy run:** 44440400784
**Main quote time:** 2026-11-19T01:55:18.760193+00:00 · **Legacy report time:** 2026-11-19T01:55:55.667724+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD | 4.55e-05 | 68.68 | +2.48% | 0.37x | MODERATE 64/100 | VERY_HIGH 75/100 | Watch |
| 2 | SENT/USD | 0.021671 | 59.90 | +0.57% | 0.35x | MODERATE 60/100 | VERY_HIGH 82/100 | Watch |
| 3 | TRX/USD ⭐ | 0.310263 | 56.20 | +0.09% | 6.57x | STRONG 83/100 | HIGH 55/100 | Watch |
| 4 | DRV/USD ⭐ | 0.26623 | 47.53 | +0.09% | 4.20x | STRONG 74/100 | HIGH 66/100 | Watch |
| 5 | PYTH/USD | 0.05362 | 39.50 | +0.47% | 0.87x | MODERATE 50/100 | HIGH 67/100 | Watch |
| 6 | PAXG/USD | 3743.07 | 35.67 | +0.17% | 0.09x | WEAK 38/100 | VERY_HIGH 70/100 | Watch |
| 7 | MEGA/USD | 0.05725 | 33.91 | -0.75% | 0.69x | WEAK 17/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRX/USD ⭐ | 0.310042 | 51.27 | +0.09% | 6.57x | 4173 | STRONG 81/100 | HIGH 55/100 | Watch |
| 2 | LTC/USD | 44.08 | 44.41 | +0.16% | 2.08x | 11731 | MODERATE 67/100 | HIGH 55/100 | Watch |
| 3 | DRV/USD ⭐ | 0.26623 | 39.09 | +0.09% | 4.20x | 2625 | STRONG 70/100 | HIGH 66/100 | Watch |

**Same-run overlap:** TRX/USD, DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
