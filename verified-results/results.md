# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T02:20:24.663032+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44443473169
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 3a017155fa6bfd20f60212f0a334498a9bb96497 (atomic ledger/results publication)
**Ledger generation:** 729 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021914 | 80.424 | 75.315 | +6.35% | +0.07% | 1.48x | 1.4 | 2026-11-19T02:20:15.792378+00:00 | Not calibrated | STRONG 75/100 | HIGH 67/100 | Watch | WATCH |
| 2 | VVV/USD | 21.976 | 73.426 | 54.029 | +1.41% | +0.88% | 2.53x | 8.6 | 2026-11-19T02:20:15.792378+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ICP/USD | 2.242 | 52.845 | 56.235 | +2.94% | +0.63% | 0.35x | 4.5 | 2026-11-19T02:20:15.792378+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.307 | 47.206 | 55.379 | +0.29% | -0.04% | 0.20x | 3.3 | 2026-11-19T02:20:15.792378+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | PAXG/USD | 3741.65 | 43.618 | 42.614 | +0.28% | +0.02% | 1.09x | 1.8 | 2026-11-19T02:20:15.792378+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |
| 6 | TRX/USD | 0.310169 | 42.284 | 41.939 | +0.29% | +0.01% | 1.03x | 0.3 | 2026-11-19T02:20:15.792378+00:00 | Not calibrated | MODERATE 46/100 | HIGH 62/100 | Watch | WATCH |
| 7 | UAI/USD | 0.03371 | 33.100 | 37.629 | +1.81% | +0.24% | 0.43x | 11.9 | 2026-11-19T02:20:15.792378+00:00 | Not calibrated | WEAK 42/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | DRV/USD | 0.26631 | 25.832 | 33.447 | +0.61% | -0.02% | 0.25x | 8.3 | 2026-11-19T02:20:15.792378+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | TRUMP/USD | 0.948 | 24.828 | 31.770 | +0.32% | -0.11% | 0.36x | 10.5 | 2026-11-19T02:20:15.792378+00:00 | Not calibrated | WEAK 12/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | W/USD | 0.00894 | 21.668 | 22.266 | +0.34% | +0.45% | 0.72x | 22.4 | 2026-11-19T02:20:15.792378+00:00 | Not calibrated | WEAK 31/100 | EXTREME 94/100 | Do nothing | WATCH |
| 11 | LIGHTER/USD | 2.723 | 20.084 | 26.954 | +0.33% | -0.04% | 0.33x | 22.1 | 2026-11-19T02:20:15.792378+00:00 | Not calibrated | WEAK 5/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 75.315 | 0.021914 | +0.07% | 1.48x |
| 2 | ICP/USD | 56.235 | 2.242 | +0.63% | 0.35x |
| 3 | NEAR/USD | 55.379 | 3.307 | -0.04% | 0.20x |
| 4 | VVV/USD | 54.029 | 21.976 | +0.88% | 2.53x |
| 5 | PAXG/USD | 42.614 | 3741.65 | +0.02% | 1.09x |
| 6 | TRX/USD | 41.939 | 0.310169 | +0.01% | 1.03x |
| 7 | UAI/USD | 37.629 | 0.03371 | +0.24% | 0.43x |
| 8 | DRV/USD | 33.447 | 0.26631 | -0.02% | 0.25x |
| 9 | TRUMP/USD | 31.770 | 0.948 | -0.11% | 0.36x |
| 10 | LIGHTER/USD | 26.954 | 2.723 | -0.04% | 0.33x |
| 11 | W/USD | 22.266 | 0.00894 | +0.45% | 0.72x |

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

- Persisted scans: 729; predictions: 5924; observations: 440968.
- Matured sampled outcomes across 1/6/24/48h: 5857; gap abstentions: 13487. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44443473169 · **Generation:** 729 · **Legacy run:** 44443473169
**Main quote time:** 2026-11-19T02:20:24.663032+00:00 · **Legacy report time:** 2026-11-19T02:21:12.046145+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.021914 | 80.42 | +0.07% | 1.48x | STRONG 75/100 | HIGH 67/100 | Watch |
| 2 | VVV/USD ⭐ | 21.976 | 73.43 | +0.88% | 2.53x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ICP/USD | 2.242 | 52.84 | +0.63% | 0.35x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 4 | NEAR/USD | 3.307 | 47.21 | -0.04% | 0.20x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | PAXG/USD | 3741.65 | 43.62 | +0.02% | 1.09x | MODERATE 47/100 | HIGH 62/100 | Watch |
| 6 | TRX/USD | 0.310169 | 42.28 | +0.01% | 1.03x | MODERATE 46/100 | HIGH 62/100 | Watch |
| 7 | UAI/USD | 0.03371 | 33.10 | +0.24% | 0.43x | WEAK 42/100 | EXTREME 88/100 | Do nothing |
| 8 | DRV/USD | 0.26631 | 25.83 | -0.02% | 0.25x | WEAK 18/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | TRUMP/USD | 0.948 | 24.83 | -0.11% | 0.36x | WEAK 12/100 | EXTREME 87/100 | Do nothing |
| 10 | W/USD | 0.00894 | 21.67 | +0.45% | 0.72x | WEAK 31/100 | EXTREME 94/100 | Do nothing |
| 11 | LIGHTER/USD | 2.723 | 20.08 | -0.04% | 0.33x | WEAK 5/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.976 | 60.99 | +0.88% | 2.53x | 7980 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 2 | AKE/USD | 0.01051485 | 43.39 | +1.40% | 1.04x | 3439 | MODERATE 47/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
