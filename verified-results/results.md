# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T19:05:46.657805+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45681541275
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e9c68dfd39aa43f3aadee92b12ced087b0061e21 (atomic ledger/results publication)
**Ledger generation:** 1754 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.913 | 96.305 | 89.944 | +9.68% | +0.97% | 1.15x | 20.1 | 2026-11-25T19:05:38.429737+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | ZEC/USD | 754.07 | 87.713 | 67.524 | +2.05% | +1.04% | 3.10x | 3.7 | 2026-11-25T19:05:38.429737+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XMR/USD | 516.98 | 74.966 | 59.715 | +1.45% | +0.10% | 2.47x | 10.8 | 2026-11-25T19:05:38.429737+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LTC/USD | 42.29 | 74.505 | 78.493 | +3.53% | +0.67% | 0.27x | 2.4 | 2026-11-25T19:05:38.429737+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | XPL/USD | 0.0481 | 71.449 | 71.359 | +9.32% | +0.63% | 0.70x | 20.8 | 2026-11-25T19:05:38.429737+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | DRV/USD | 0.35041 | 70.625 | 74.450 | +11.50% | +0.24% | 0.50x | 19.4 | 2026-11-25T19:05:38.429737+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6582 | 64.604 | 65.048 | +1.65% | +0.40% | 0.76x | 3.0 | 2026-11-25T19:05:38.429737+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 8 | HYPE/USD | 60.71 | 61.250 | 63.174 | +1.40% | +0.15% | 0.73x | 3.3 | 2026-11-25T19:05:38.429737+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XRP/USD | 0.933 | 59.771 | 62.063 | +1.02% | +0.45% | 0.55x | 0.1 | 2026-11-25T19:05:38.429737+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | LINK/USD | 9.03153 | 58.383 | 59.168 | +2.15% | +0.29% | 0.78x | 4.8 | 2026-11-25T19:05:38.429737+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 11 | SOL/USD | 70.03 | 53.492 | 58.611 | +0.62% | +0.24% | 0.37x | 1.4 | 2026-11-25T19:05:38.429737+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ETH/USD | 1684.85 | 52.087 | 57.949 | +0.43% | +0.15% | 0.34x | 0.1 | 2026-11-25T19:05:38.429737+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 89.944 | 26.913 | +0.97% | 1.15x |
| 2 | LTC/USD | 78.493 | 42.29 | +0.67% | 0.27x |
| 3 | DRV/USD | 74.450 | 0.35041 | +0.24% | 0.50x |
| 4 | XPL/USD | 71.359 | 0.0481 | +0.63% | 0.70x |
| 5 | ZEC/USD | 67.524 | 754.07 | +1.04% | 3.10x |
| 6 | SUI/USD | 65.048 | 0.6582 | +0.40% | 0.76x |
| 7 | HYPE/USD | 63.174 | 60.71 | +0.15% | 0.73x |
| 8 | XRP/USD | 62.063 | 0.933 | +0.45% | 0.55x |
| 9 | XMR/USD | 59.715 | 516.98 | +0.10% | 2.47x |
| 10 | LINK/USD | 59.168 | 9.03153 | +0.29% | 0.78x |
| 11 | SOL/USD | 58.611 | 70.03 | +0.24% | 0.37x |
| 12 | ETH/USD | 57.949 | 1684.85 | +0.15% | 0.34x |

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

- Persisted scans: 1754; predictions: 14792; observations: 1063230.
- Matured sampled outcomes across 1/6/24/48h: 32547; gap abstentions: 22769. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45681541275 · **Generation:** 1754 · **Legacy run:** 45681541275
**Main quote time:** 2026-11-25T19:05:46.657805+00:00 · **Legacy report time:** 2026-11-25T19:06:46.886241+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.913 | 96.31 | +0.97% | 1.15x | STRONG 83/100 | VERY_HIGH 74/100 | Watch |
| 2 | ZEC/USD ⭐ | 754.07 | 87.71 | +1.04% | 3.10x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XMR/USD | 516.98 | 74.97 | +0.10% | 2.47x | STRONG 77/100 | HIGH 61/100 | Watch |
| 4 | LTC/USD | 42.29 | 74.50 | +0.67% | 0.27x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 5 | XPL/USD | 0.0481 | 71.45 | +0.63% | 0.70x | MODERATE 56/100 | VERY_HIGH 82/100 | Watch |
| 6 | DRV/USD | 0.35041 | 70.62 | +0.24% | 0.50x | MODERATE 60/100 | VERY_HIGH 76/100 | Watch |
| 7 | SUI/USD | 0.6582 | 64.60 | +0.40% | 0.76x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 8 | HYPE/USD | 60.71 | 61.25 | +0.15% | 0.73x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 9 | XRP/USD | 0.933 | 59.77 | +0.45% | 0.55x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 10 | LINK/USD | 9.03153 | 58.38 | +0.29% | 0.78x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 11 | SOL/USD | 70.03 | 53.49 | +0.24% | 0.37x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 12 | ETH/USD | 1684.85 | 52.09 | +0.15% | 0.34x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.907 | 88.52 | +0.97% | 1.15x | 10948 | STRONG 79/100 | VERY_HIGH 74/100 | Watch |
| 2 | ZEC/USD ⭐ | 754.39 | 73.29 | +1.04% | 3.10x | 37769 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | BCH/USD | 203.02 | 65.31 | +0.37% | 1.76x | 2133 | STRONG 78/100 | HIGH 60/100 | Watch |

**Same-run overlap:** VVV/USD, ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
