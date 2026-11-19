# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T05:10:26.424518+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44463204734
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 9b1745f7ad7e5514eb4d7d82407b69d576a4cd38 (atomic ledger/results publication)
**Ledger generation:** 763 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 67.57 | 75.154 | 61.482 | +1.03% | -0.27% | 2.54x | 1.5 | 2026-11-19T05:10:19.923154+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 2 | VVV/USD | 22.517 | 74.669 | 77.579 | +3.90% | -0.22% | 0.82x | 8.0 | 2026-11-19T05:10:19.923154+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 3 | NEAR/USD | 3.4173 | 72.714 | 78.258 | +3.64% | -0.15% | 0.52x | 4.4 | 2026-11-19T05:10:19.923154+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | ZEC/USD | 935.1 | 71.424 | 70.738 | +2.54% | +0.14% | 1.00x | 4.1 | 2026-11-19T05:10:19.923154+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 5 | ETH/USD | 1798.52 | 68.173 | 64.344 | +1.34% | -0.01% | 1.39x | 0.1 | 2026-11-19T05:10:19.923154+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SOL/USD | 74.54 | 61.610 | 63.848 | +1.36% | -0.01% | 0.78x | 1.3 | 2026-11-19T05:10:19.923154+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 7 | XBT/USD | 63494.3 | 59.940 | 60.658 | +0.81% | -0.07% | 0.96x | 0.0 | 2026-11-19T05:10:19.923154+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 8 | TAO/USD | 194.5131 | 54.491 | 61.273 | +1.33% | -0.34% | 0.49x | 6.1 | 2026-11-19T05:10:19.923154+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | XRP/USD | 0.97395 | 51.056 | 60.439 | +0.78% | -0.16% | 0.14x | 0.1 | 2026-11-19T05:10:19.923154+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | SUI/USD | 0.7233 | 50.150 | 58.593 | +0.61% | -0.15% | 0.23x | 1.4 | 2026-11-19T05:10:19.923154+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XDG/USD | 0.0590504 | 48.818 | 53.072 | +0.59% | -0.19% | 0.67x | 1.2 | 2026-11-19T05:10:19.923154+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | LTC/USD | 44.43 | 48.326 | 57.149 | +0.95% | -0.27% | 0.25x | 2.3 | 2026-11-19T05:10:19.923154+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 78.258 | 3.4173 | -0.15% | 0.52x |
| 2 | VVV/USD | 77.579 | 22.517 | -0.22% | 0.82x |
| 3 | ZEC/USD | 70.738 | 935.1 | +0.14% | 1.00x |
| 4 | ETH/USD | 64.344 | 1798.52 | -0.01% | 1.39x |
| 5 | SOL/USD | 63.848 | 74.54 | -0.01% | 0.78x |
| 6 | HYPE/USD | 61.482 | 67.57 | -0.27% | 2.54x |
| 7 | TAO/USD | 61.273 | 194.5131 | -0.34% | 0.49x |
| 8 | XBT/USD | 60.658 | 63494.3 | -0.07% | 0.96x |
| 9 | XRP/USD | 60.439 | 0.97395 | -0.16% | 0.14x |
| 10 | SUI/USD | 58.593 | 0.7233 | -0.15% | 0.23x |
| 11 | LTC/USD | 57.149 | 44.43 | -0.27% | 0.25x |
| 12 | XDG/USD | 53.072 | 0.0590504 | -0.19% | 0.67x |

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

- Persisted scans: 763; predictions: 6300; observations: 461673.
- Matured sampled outcomes across 1/6/24/48h: 6298; gap abstentions: 13723. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44463204734 · **Generation:** 763 · **Legacy run:** 44463204734
**Main quote time:** 2026-11-19T05:10:26.424518+00:00 · **Legacy report time:** 2026-11-19T05:11:09.976148+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 67.57 | 75.15 | -0.27% | 2.54x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 2 | VVV/USD | 22.517 | 74.67 | -0.22% | 0.82x | WEAK 42/100 | HIGH 68/100 | Watch |
| 3 | NEAR/USD | 3.4173 | 72.71 | -0.15% | 0.52x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 4 | ZEC/USD | 935.1 | 71.42 | +0.14% | 1.00x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 5 | ETH/USD | 1798.52 | 68.17 | -0.01% | 1.39x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 6 | SOL/USD | 74.54 | 61.61 | -0.01% | 0.78x | WEAK 36/100 | HIGH 68/100 | Watch |
| 7 | XBT/USD | 63494.3 | 59.94 | -0.07% | 0.96x | WEAK 35/100 | HIGH 68/100 | Watch |
| 8 | TAO/USD | 194.5131 | 54.49 | -0.34% | 0.49x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | XRP/USD | 0.97395 | 51.06 | -0.16% | 0.14x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | SUI/USD | 0.7233 | 50.15 | -0.15% | 0.23x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XDG/USD | 0.0590504 | 48.82 | -0.19% | 0.67x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | LTC/USD | 44.43 | 48.33 | -0.27% | 0.25x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |

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
