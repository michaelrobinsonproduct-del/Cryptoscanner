# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T07:02:11.204298+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45344538933
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 23a9d32c4981029b0d00b515e835bc987bcbff95 (atomic ledger/results publication)
**Ledger generation:** 1541 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.558 | 100.226 | 81.890 | +4.54% | +0.67% | 4.20x | 9.8 | 2026-11-24T07:02:03.139932+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | BABY/USD | 0.00898 | 83.243 | 65.738 | +5.65% | +1.34% | 2.08x | 11.1 | 2026-11-24T07:02:03.139932+00:00 | Not calibrated | STRONG 92/100 | HIGH 66/100 | Consider small entry | WATCH |
| 3 | HYPE/USD | 64.19 | 75.331 | 59.492 | +0.86% | +0.31% | 2.43x | 3.1 | 2026-11-24T07:02:03.139932+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | LINK/USD | 9.0842 | 70.316 | 58.377 | +0.88% | +0.06% | 2.16x | 5.6 | 2026-11-24T07:02:03.139932+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 5 | AI/USD | 0.01669 | 67.409 | 72.845 | +9.59% | +0.48% | 0.22x | 6.0 | 2026-11-24T07:02:03.139932+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | XMR/USD | 497.54 | 63.440 | 65.858 | +2.37% | +0.27% | 0.62x | 11.5 | 2026-11-24T07:02:03.139932+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.521e-06 | 61.530 | 69.352 | +2.89% | -0.31% | 0.37x | 2.8 | 2026-11-24T07:02:03.139932+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XRP/USD | 0.948 | 59.809 | 60.888 | +0.92% | +0.14% | 0.82x | 1.1 | 2026-11-24T07:02:03.139932+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 9 | NEAR/USD | 3.0244 | 59.281 | 62.664 | +1.45% | +0.23% | 0.55x | 5.0 | 2026-11-24T07:02:03.139932+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | LTC/USD | 41.73 | 57.986 | 59.041 | +0.75% | +0.12% | 0.83x | 2.4 | 2026-11-24T07:02:03.139932+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 11 | TIA/USD | 0.3422 | 40.474 | 43.831 | +1.91% | -0.09% | 0.71x | 2.9 | 2026-11-24T07:02:03.139932+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 12 | DOT/USD | 0.6828 | 33.213 | 41.494 | +1.08% | +0.01% | 0.16x | 1.5 | 2026-11-24T07:02:03.139932+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 81.890 | 25.558 | +0.67% | 4.20x |
| 2 | AI/USD | 72.845 | 0.01669 | +0.48% | 0.22x |
| 3 | PEPE/USD | 69.352 | 3.521e-06 | -0.31% | 0.37x |
| 4 | XMR/USD | 65.858 | 497.54 | +0.27% | 0.62x |
| 5 | BABY/USD | 65.738 | 0.00898 | +1.34% | 2.08x |
| 6 | NEAR/USD | 62.664 | 3.0244 | +0.23% | 0.55x |
| 7 | XRP/USD | 60.888 | 0.948 | +0.14% | 0.82x |
| 8 | HYPE/USD | 59.492 | 64.19 | +0.31% | 2.43x |
| 9 | LTC/USD | 59.041 | 41.73 | +0.12% | 0.83x |
| 10 | LINK/USD | 58.377 | 9.0842 | +0.06% | 2.16x |
| 11 | TIA/USD | 43.831 | 0.3422 | -0.09% | 0.71x |
| 12 | DOT/USD | 41.494 | 0.6828 | +0.01% | 0.16x |

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

- Persisted scans: 1541; predictions: 13225; observations: 933567.
- Matured sampled outcomes across 1/6/24/48h: 24847; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 139 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45344538933 · **Generation:** 1541 · **Legacy run:** 45344538933
**Main quote time:** 2026-11-24T07:02:11.204298+00:00 · **Legacy report time:** 2026-11-24T07:03:19.622130+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.558 | 100.23 | +0.67% | 4.20x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | BABY/USD ⭐ | 0.00898 | 83.24 | +1.34% | 2.08x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | HYPE/USD ⭐ | 64.19 | 75.33 | +0.31% | 2.43x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | LINK/USD | 9.0842 | 70.32 | +0.06% | 2.16x | STRONG 80/100 | HIGH 55/100 | Watch |
| 5 | AI/USD | 0.01669 | 67.41 | +0.48% | 0.22x | MODERATE 64/100 | VERY_HIGH 82/100 | Watch |
| 6 | XMR/USD | 497.54 | 63.44 | +0.27% | 0.62x | MODERATE 57/100 | VERY_HIGH 76/100 | Watch |
| 7 | PEPE/USD | 3.521e-06 | 61.53 | -0.31% | 0.37x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 8 | XRP/USD | 0.948 | 59.81 | +0.14% | 0.82x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 9 | NEAR/USD | 3.0244 | 59.28 | +0.23% | 0.55x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 10 | LTC/USD | 41.73 | 57.99 | +0.12% | 0.83x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 11 | TIA/USD | 0.3422 | 40.47 | -0.09% | 0.71x | WEAK 25/100 | VERY_HIGH 81/100 | Do nothing |
| 12 | DOT/USD | 0.6828 | 33.21 | +0.01% | 0.16x | WEAK 37/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.561 | 96.70 | +0.67% | 4.20x | 12778 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | BABY/USD ⭐ | 0.00901 | 79.41 | +1.34% | 2.08x | 3501 | STRONG 90/100 | VERY_HIGH 82/100 | Watch |
| 3 | HYPE/USD ⭐ | 64.26 | 64.12 | +0.31% | 2.43x | 30175 | STRONG 97/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** VVV/USD, BABY/USD, HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
