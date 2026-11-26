# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T23:31:18.335793+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45911240600
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8349bd258a06fa80e89631d673eb6a0bbe08dfa8 (atomic ledger/results publication)
**Ledger generation:** 1928 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LINK/USD | 9.24922 | 74.734 | 69.383 | +2.26% | -0.13% | 1.60x | 2.9 | 2026-11-26T23:31:10.268200+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ZRO/USD | 1.126 | 69.829 | 71.723 | +9.96% | +0.54% | 0.54x | 17.8 | 2026-11-26T23:31:10.268200+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 3 | FET/USD | 0.1195 | 67.887 | 66.219 | +10.14% | +0.25% | 1.04x | 25.1 | 2026-11-26T23:31:10.268200+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | LTC/USD | 43.8 | 66.012 | 70.581 | +2.55% | +0.05% | 0.52x | 4.6 | 2026-11-26T23:31:10.268200+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | HYPE/USD | 62.01 | 62.257 | 58.624 | +0.63% | +0.00% | 1.36x | 1.6 | 2026-11-26T23:31:10.268200+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 6 | SOL/USD | 70.89 | 60.395 | 59.267 | +0.71% | -0.03% | 1.13x | 1.4 | 2026-11-26T23:31:10.268200+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0563165 | 58.771 | 46.806 | +0.64% | +0.04% | 2.18x | 0.7 | 2026-11-26T23:31:10.268200+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 8 | ONDO/USD | 0.28627 | 56.405 | 41.754 | +1.33% | -0.07% | 5.23x | 0.3 | 2026-11-26T23:31:10.268200+00:00 | Not calibrated | MODERATE 58/100 | HIGH 66/100 | Watch | WATCH |
| 9 | XRP/USD | 0.94178 | 56.325 | 58.848 | +0.56% | -0.12% | 0.81x | 0.1 | 2026-11-26T23:31:10.268200+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 10 | DOT/USD | 0.6698 | 35.977 | 44.003 | +1.75% | -0.03% | 0.21x | 1.5 | 2026-11-26T23:31:10.268200+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZRO/USD | 71.723 | 1.126 | +0.54% | 0.54x |
| 2 | LTC/USD | 70.581 | 43.8 | +0.05% | 0.52x |
| 3 | LINK/USD | 69.383 | 9.24922 | -0.13% | 1.60x |
| 4 | FET/USD | 66.219 | 0.1195 | +0.25% | 1.04x |
| 5 | SOL/USD | 59.267 | 70.89 | -0.03% | 1.13x |
| 6 | XRP/USD | 58.848 | 0.94178 | -0.12% | 0.81x |
| 7 | HYPE/USD | 58.624 | 62.01 | +0.00% | 1.36x |
| 8 | XDG/USD | 46.806 | 0.0563165 | +0.04% | 2.18x |
| 9 | DOT/USD | 44.003 | 0.6698 | -0.03% | 0.21x |
| 10 | ONDO/USD | 41.754 | 0.28627 | -0.07% | 5.23x |

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

- Persisted scans: 1928; predictions: 16866; observations: 1167813.
- Matured sampled outcomes across 1/6/24/48h: 36824; gap abstentions: 25352. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 149 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45911240600 · **Generation:** 1928 · **Legacy run:** 45911240600
**Main quote time:** 2026-11-26T23:31:18.335793+00:00 · **Legacy report time:** 2026-11-26T23:32:10.187448+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD | 9.24922 | 74.73 | -0.13% | 1.60x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 2 | ZRO/USD | 1.126 | 69.83 | +0.54% | 0.54x | MODERATE 60/100 | VERY_HIGH 81/100 | Watch |
| 3 | FET/USD ⭐ | 0.1195 | 67.89 | +0.25% | 1.04x | MODERATE 69/100 | VERY_HIGH 79/100 | Watch |
| 4 | LTC/USD | 43.8 | 66.01 | +0.05% | 0.52x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 5 | HYPE/USD | 62.01 | 62.26 | +0.00% | 1.36x | MODERATE 66/100 | HIGH 55/100 | Watch |
| 6 | SOL/USD | 70.89 | 60.39 | -0.03% | 1.13x | WEAK 40/100 | HIGH 68/100 | Watch |
| 7 | XDG/USD | 0.0563165 | 58.77 | +0.04% | 2.18x | STRONG 74/100 | HIGH 55/100 | Watch |
| 8 | ONDO/USD | 0.28627 | 56.41 | -0.07% | 5.23x | MODERATE 58/100 | HIGH 66/100 | Watch |
| 9 | XRP/USD | 0.94178 | 56.32 | -0.12% | 0.81x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 10 | DOT/USD | 0.6698 | 35.98 | -0.03% | 0.21x | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ME/USD | 0.0422 | 75.19 | +0.96% | 1.20x | 4808 | MODERATE 58/100 | EXTREME 89/100 | Do nothing |
| 2 | FET/USD ⭐ | 0.1195 | 71.34 | +0.25% | 1.04x | 2420 | STRONG 71/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** FET/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
