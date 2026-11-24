# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T08:01:29.469962+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45352277899
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1e97e4cfcb45486fcf54c7d6a56569098feb0717 (atomic ledger/results publication)
**Ledger generation:** 1547 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BABY/USD | 0.00912 | 77.553 | 71.391 | +7.29% | +0.78% | 1.23x | 11.0 | 2026-11-24T08:01:21.669775+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | VVV/USD | 25.201 | 75.525 | 72.996 | +3.08% | +0.23% | 1.14x | 7.1 | 2026-11-24T08:01:21.669775+00:00 | Not calibrated | STRONG 73/100 | HIGH 62/100 | Watch | WATCH |
| 3 | XMR/USD | 499.56 | 72.192 | 71.090 | +2.79% | +0.23% | 1.00x | 6.8 | 2026-11-24T08:01:21.669775+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 4 | LINK/USD | 9.04269 | 70.737 | 55.219 | +0.42% | +0.10% | 3.47x | 5.4 | 2026-11-24T08:01:21.669775+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 5 | PEPE/USD | 3.526e-06 | 61.102 | 68.996 | +3.04% | -0.06% | 0.24x | 5.7 | 2026-11-24T08:01:21.669775+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.0029 | 60.685 | 58.596 | +0.73% | -0.18% | 1.30x | 3.0 | 2026-11-24T08:01:21.669775+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 7 | LTC/USD | 41.53 | 56.399 | 55.654 | +0.27% | -0.14% | 1.15x | 2.4 | 2026-11-24T08:01:21.669775+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 8 | HYPE/USD | 63.82 | 51.262 | 55.413 | +0.28% | +0.05% | 0.56x | 3.1 | 2026-11-24T08:01:21.669775+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ICNT/USD | 0.325 | 50.946 | 54.565 | +5.14% | -3.37% | 2.32x | 27.8 | 2026-11-24T08:01:21.669775+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 10 | WLD/USD | 0.2414 | 49.171 | 42.380 | +1.30% | -0.04% | 1.70x | 4.1 | 2026-11-24T08:01:21.669775+00:00 | Not calibrated | MODERATE 45/100 | HIGH 66/100 | Watch | WATCH |
| 11 | XRP/USD | 0.94189 | 49.053 | 56.332 | +0.27% | -0.10% | 0.32x | 1.1 | 2026-11-24T08:01:21.669775+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | TIA/USD | 0.3413 | 39.620 | 40.505 | +1.64% | +0.06% | 0.88x | 5.9 | 2026-11-24T08:01:21.669775+00:00 | Not calibrated | WEAK 40/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 72.996 | 25.201 | +0.23% | 1.14x |
| 2 | BABY/USD | 71.391 | 0.00912 | +0.78% | 1.23x |
| 3 | XMR/USD | 71.090 | 499.56 | +0.23% | 1.00x |
| 4 | PEPE/USD | 68.996 | 3.526e-06 | -0.06% | 0.24x |
| 5 | NEAR/USD | 58.596 | 3.0029 | -0.18% | 1.30x |
| 6 | XRP/USD | 56.332 | 0.94189 | -0.10% | 0.32x |
| 7 | LTC/USD | 55.654 | 41.53 | -0.14% | 1.15x |
| 8 | HYPE/USD | 55.413 | 63.82 | +0.05% | 0.56x |
| 9 | LINK/USD | 55.219 | 9.04269 | +0.10% | 3.47x |
| 10 | ICNT/USD | 54.565 | 0.325 | -3.37% | 2.32x |
| 11 | WLD/USD | 42.380 | 0.2414 | -0.04% | 1.70x |
| 12 | TIA/USD | 40.505 | 0.3413 | +0.06% | 0.88x |

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

- Persisted scans: 1547; predictions: 13297; observations: 937221.
- Matured sampled outcomes across 1/6/24/48h: 25088; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 139 (sampled only; not a success-rate estimate).
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

**Writer:** 45352277899 · **Generation:** 1547 · **Legacy run:** 45352277899
**Main quote time:** 2026-11-24T08:01:29.469962+00:00 · **Legacy report time:** 2026-11-24T08:02:16.543436+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BABY/USD ⭐ | 0.00912 | 77.55 | +0.78% | 1.23x | STRONG 79/100 | VERY_HIGH 73/100 | Watch |
| 2 | VVV/USD ⭐ | 25.201 | 75.52 | +0.23% | 1.14x | STRONG 83/100 | HIGH 62/100 | Watch |
| 3 | XMR/USD | 499.56 | 72.19 | +0.23% | 1.00x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 4 | LINK/USD | 9.04269 | 70.74 | +0.10% | 3.47x | STRONG 80/100 | HIGH 55/100 | Watch |
| 5 | PEPE/USD | 3.526e-06 | 61.10 | -0.06% | 0.24x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 6 | NEAR/USD | 3.0029 | 60.68 | -0.18% | 1.30x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 7 | LTC/USD | 41.53 | 56.40 | -0.14% | 1.15x | WEAK 38/100 | HIGH 68/100 | Watch |
| 8 | HYPE/USD | 63.82 | 51.26 | +0.05% | 0.56x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 9 | ICNT/USD | 0.325 | 50.95 | -3.37% | 2.32x | MODERATE 45/100 | VERY_HIGH 82/100 | Do nothing |
| 10 | WLD/USD | 0.2414 | 49.17 | -0.04% | 1.70x | MODERATE 45/100 | HIGH 66/100 | Watch |
| 11 | XRP/USD | 0.94189 | 49.05 | -0.10% | 0.32x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | TIA/USD | 0.3413 | 39.62 | +0.06% | 0.88x | WEAK 40/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.288 | 79.47 | +0.23% | 1.14x | 12914 | STRONG 85/100 | HIGH 62/100 | Watch |
| 2 | BABY/USD ⭐ | 0.00912 | 74.36 | +0.78% | 1.23x | 3768 | STRONG 77/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** BABY/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
