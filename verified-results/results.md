# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T13:45:10.783797+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44316804112
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 405a0755761877abbd7b6390ff5c5751b2163bee (atomic ledger/results publication)
**Ledger generation:** 580 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.389 | 70.165 | 54.674 | +1.73% | +0.10% | 5.66x | 11.7 | 2026-11-18T13:45:02.608373+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04657 | 62.420 | 68.281 | +3.74% | +0.52% | 0.15x | 12.9 | 2026-11-18T13:45:02.608373+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | XRP/USD | 0.98624 | 55.252 | 57.593 | +0.38% | +0.23% | 0.65x | 0.1 | 2026-11-18T13:45:02.608373+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | TRX/USD | 0.30962 | 48.803 | 45.322 | +0.56% | -0.01% | 1.35x | 0.5 | 2026-11-18T13:45:02.608373+00:00 | Not calibrated | WEAK 44/100 | HIGH 61/100 | Watch | WATCH |
| 5 | AKT/USD | 0.523 | 46.056 | 48.473 | +2.69% | +0.10% | 0.71x | 5.7 | 2026-11-18T13:45:02.608373+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | PEARL/USD | 1.8213 | 41.764 | 42.158 | +0.60% | +0.70% | 0.61x | 0.5 | 2026-11-18T13:45:02.608373+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | W/USD | 0.00911 | 41.742 | 40.336 | +2.02% | +0.55% | 0.86x | 11.0 | 2026-11-18T13:45:02.608373+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | SENT/USD | 0.019186 | 41.449 | 46.248 | +2.77% | -1.33% | 1.18x | 8.3 | 2026-11-18T13:45:02.608373+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 84/100 | Do nothing | WATCH |
| 9 | USELESS/USD | 0.1001 | 41.126 | 49.913 | +2.58% | -0.30% | 0.27x | 20.0 | 2026-11-18T13:45:02.608373+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 10 | CAP/USD | 0.101846 | 41.049 | 25.970 | +0.86% | +0.02% | 3.93x | 22.8 | 2026-11-18T13:45:02.608373+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 11 | AKE/USD | 0.01017676 | 40.207 | 38.555 | +1.93% | +0.53% | 0.90x | 17.0 | 2026-11-18T13:45:02.608373+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 12 | CC/USD | 0.08316 | 32.057 | 40.023 | +1.25% | -0.22% | 0.31x | 8.4 | 2026-11-18T13:45:02.608373+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 68.281 | 0.04657 | +0.52% | 0.15x |
| 2 | XRP/USD | 57.593 | 0.98624 | +0.23% | 0.65x |
| 3 | VVV/USD | 54.674 | 21.389 | +0.10% | 5.66x |
| 4 | USELESS/USD | 49.913 | 0.1001 | -0.30% | 0.27x |
| 5 | AKT/USD | 48.473 | 0.523 | +0.10% | 0.71x |
| 6 | SENT/USD | 46.248 | 0.019186 | -1.33% | 1.18x |
| 7 | TRX/USD | 45.322 | 0.30962 | -0.01% | 1.35x |
| 8 | PEARL/USD | 42.158 | 1.8213 | +0.70% | 0.61x |
| 9 | W/USD | 40.336 | 0.00911 | +0.55% | 0.86x |
| 10 | CC/USD | 40.023 | 0.08316 | -0.22% | 0.31x |
| 11 | AKE/USD | 38.555 | 0.01017676 | +0.53% | 0.90x |
| 12 | CAP/USD | 25.970 | 0.101846 | +0.02% | 3.93x |

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

- Persisted scans: 580; predictions: 4915; observations: 350227.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 13072. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44316804112 · **Generation:** 580 · **Legacy run:** 44316804112
**Main quote time:** 2026-11-18T13:45:10.783797+00:00 · **Legacy report time:** 2026-11-18T13:45:30.153064+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.389 | 70.17 | +0.10% | 5.66x | STRONG 85/100 | HIGH 61/100 | Watch |
| 2 | NIGHT/USD | 0.04657 | 62.42 | +0.52% | 0.15x | MODERATE 56/100 | VERY_HIGH 76/100 | Watch |
| 3 | XRP/USD | 0.98624 | 55.25 | +0.23% | 0.65x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 4 | TRX/USD | 0.30962 | 48.80 | -0.01% | 1.35x | WEAK 44/100 | HIGH 61/100 | Watch |
| 5 | AKT/USD | 0.523 | 46.06 | +0.10% | 0.71x | WEAK 43/100 | VERY_HIGH 75/100 | Watch |
| 6 | PEARL/USD | 1.8213 | 41.76 | +0.70% | 0.61x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 7 | W/USD | 0.00911 | 41.74 | +0.55% | 0.86x | MODERATE 46/100 | VERY_HIGH 73/100 | Watch |
| 8 | SENT/USD | 0.019186 | 41.45 | -1.33% | 1.18x | WEAK 31/100 | VERY_HIGH 84/100 | Do nothing |
| 9 | USELESS/USD | 0.1001 | 41.13 | -0.30% | 0.27x | WEAK 21/100 | VERY_HIGH 82/100 | Do nothing |
| 10 | CAP/USD | 0.101846 | 41.05 | +0.02% | 3.93x | MODERATE 56/100 | VERY_HIGH 79/100 | Watch |
| 11 | AKE/USD | 0.01017676 | 40.21 | +0.53% | 0.90x | MODERATE 45/100 | VERY_HIGH 73/100 | Watch |
| 12 | CC/USD | 0.08316 | 32.06 | -0.22% | 0.31x | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.389 | 62.08 | +0.10% | 5.66x | 7078 | STRONG 81/100 | HIGH 61/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
