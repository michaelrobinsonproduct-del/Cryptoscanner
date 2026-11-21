# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T19:41:08.128940+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44942102413
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 00b1c5fb1c8f9c7a99629a8001c9cda0b89f4915 (atomic ledger/results publication)
**Ledger generation:** 1177 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.93558 | 91.271 | 75.485 | +2.96% | +0.40% | 2.38x | 0.4 | 2026-11-21T19:40:59.679313+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | TAO/USD | 185.7175 | 88.819 | 72.790 | +2.89% | +0.21% | 4.21x | 4.8 | 2026-11-21T19:40:59.679313+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XMR/USD | 483.36 | 85.897 | 92.495 | +5.93% | -0.17% | 0.43x | 8.1 | 2026-11-21T19:40:59.679313+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | UNI/USD | 4.6899 | 84.431 | 88.084 | +4.99% | +0.20% | 0.54x | 3.6 | 2026-11-21T19:40:59.679313+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ZEC/USD | 791.08 | 82.790 | 84.055 | +4.38% | +0.47% | 0.64x | 3.2 | 2026-11-21T19:40:59.679313+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | ETH/USD | 1683.6 | 81.841 | 82.728 | +3.97% | +0.10% | 0.86x | 0.1 | 2026-11-21T19:40:59.679313+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.04527 | 75.116 | 86.853 | +7.22% | -1.25% | 0.45x | 13.3 | 2026-11-21T19:40:59.679313+00:00 | Not calibrated | WEAK 38/100 | EXTREME 86/100 | Do nothing | WATCH |
| 8 | SOL/USD | 70.68 | 72.351 | 74.362 | +2.87% | +0.20% | 0.70x | 1.4 | 2026-11-21T19:40:59.679313+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XBT/USD | 60246.2 | 65.830 | 72.130 | +2.45% | +0.09% | 0.32x | 0.0 | 2026-11-21T19:40:59.679313+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | HYPE/USD | 61.42 | 63.343 | 60.511 | +0.90% | +0.21% | 1.18x | 1.6 | 2026-11-21T19:40:59.679313+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0552077 | 62.421 | 67.020 | +1.72% | +0.17% | 0.45x | 0.0 | 2026-11-21T19:40:59.679313+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | TRX/USD | 0.304389 | 58.512 | 48.982 | +0.96% | +0.02% | 1.94x | 1.0 | 2026-11-21T19:40:59.679313+00:00 | Not calibrated | MODERATE 64/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 92.495 | 483.36 | -0.17% | 0.43x |
| 2 | UNI/USD | 88.084 | 4.6899 | +0.20% | 0.54x |
| 3 | NIGHT/USD | 86.853 | 0.04527 | -1.25% | 0.45x |
| 4 | ZEC/USD | 84.055 | 791.08 | +0.47% | 0.64x |
| 5 | ETH/USD | 82.728 | 1683.6 | +0.10% | 0.86x |
| 6 | XRP/USD | 75.485 | 0.93558 | +0.40% | 2.38x |
| 7 | SOL/USD | 74.362 | 70.68 | +0.20% | 0.70x |
| 8 | TAO/USD | 72.790 | 185.7175 | +0.21% | 4.21x |
| 9 | XBT/USD | 72.130 | 60246.2 | +0.09% | 0.32x |
| 10 | XDG/USD | 67.020 | 0.0552077 | +0.17% | 0.45x |
| 11 | HYPE/USD | 60.511 | 61.42 | +0.21% | 1.18x |
| 12 | TRX/USD | 48.982 | 0.304389 | +0.02% | 1.94x |

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

- Persisted scans: 1177; predictions: 9433; observations: 711975.
- Matured sampled outcomes across 1/6/24/48h: 12510; gap abstentions: 21231. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44942102413 · **Generation:** 1177 · **Legacy run:** 44942102413
**Main quote time:** 2026-11-21T19:41:08.128940+00:00 · **Legacy report time:** 2026-11-21T19:42:13.432797+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.93558 | 91.27 | +0.40% | 2.38x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | TAO/USD ⭐ | 185.7175 | 88.82 | +0.21% | 4.21x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XMR/USD | 483.36 | 85.90 | -0.17% | 0.43x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 4 | UNI/USD | 4.6899 | 84.43 | +0.20% | 0.54x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 5 | ZEC/USD | 791.08 | 82.79 | +0.47% | 0.64x | STRONG 71/100 | VERY_HIGH 70/100 | Watch |
| 6 | ETH/USD | 1683.6 | 81.84 | +0.10% | 0.86x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 7 | NIGHT/USD | 0.04527 | 75.12 | -1.25% | 0.45x | WEAK 38/100 | EXTREME 86/100 | Do nothing |
| 8 | SOL/USD | 70.68 | 72.35 | +0.20% | 0.70x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 9 | XBT/USD | 60246.2 | 65.83 | +0.09% | 0.32x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 10 | HYPE/USD | 61.42 | 63.34 | +0.21% | 1.18x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 11 | XDG/USD | 0.0552077 | 62.42 | +0.17% | 0.45x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 12 | TRX/USD | 0.304389 | 58.51 | +0.02% | 1.94x | MODERATE 64/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.93588 | 94.38 | +0.40% | 2.38x | 55210 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | TAO/USD ⭐ | 185.7175 | 83.59 | +0.21% | 4.21x | 12009 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SHX/USD | 0.00352 | 80.39 | +0.40% | 3.90x | 2703 | STRONG 90/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** XRP/USD, TAO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
