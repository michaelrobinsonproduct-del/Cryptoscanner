# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T14:01:08.139541+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45834511823
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 8ccd7116c80bd0d897207c453f19dfc46e55f743 (atomic ledger/results publication)
**Ledger generation:** 1870 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 589; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZRO/USD | 1.112 | 90.352 | 75.875 | +8.59% | +0.18% | 2.36x | 18.0 | 2026-11-26T14:00:59.479684+00:00 | Not calibrated | STRONG 85/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XRP/USD | 0.94961 | 79.449 | 64.701 | +1.39% | -0.05% | 2.79x | 0.1 | 2026-11-26T14:00:59.479684+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | QNT/USD | 151.63 | 71.723 | 76.916 | +4.72% | +0.36% | 0.30x | 7.3 | 2026-11-26T14:00:59.479684+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | LTC/USD | 43.76 | 68.815 | 71.067 | +2.46% | +0.27% | 0.64x | 2.3 | 2026-11-26T14:00:59.479684+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | INJ/USD | 6.195 | 67.183 | 69.199 | +4.05% | +0.26% | 0.67x | 4.8 | 2026-11-26T14:00:59.479684+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | SOL/USD | 71.11 | 67.128 | 61.457 | +1.02% | +0.31% | 1.41x | 1.4 | 2026-11-26T14:00:59.479684+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 7 | LINK/USD | 9.23695 | 64.811 | 67.898 | +2.13% | +0.07% | 0.66x | 3.0 | 2026-11-26T14:00:59.479684+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ADA/USD | 0.148954 | 63.516 | 68.343 | +2.18% | +0.08% | 0.48x | 3.9 | 2026-11-26T14:00:59.479684+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | FET/USD | 0.1155 | 62.459 | 69.714 | +6.45% | +0.43% | 0.06x | 17.4 | 2026-11-26T14:00:59.479684+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0568637 | 60.337 | 60.541 | +1.62% | +0.11% | 0.92x | 0.0 | 2026-11-26T14:00:59.479684+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XBT/USD | 60770.5 | 56.258 | 59.652 | +0.67% | -0.04% | 0.68x | 0.0 | 2026-11-26T14:00:59.479684+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | ETH/USD | 1700.74 | 54.750 | 59.248 | +0.61% | +0.00% | 0.55x | 0.1 | 2026-11-26T14:00:59.479684+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 76.916 | 151.63 | +0.36% | 0.30x |
| 2 | ZRO/USD | 75.875 | 1.112 | +0.18% | 2.36x |
| 3 | LTC/USD | 71.067 | 43.76 | +0.27% | 0.64x |
| 4 | FET/USD | 69.714 | 0.1155 | +0.43% | 0.06x |
| 5 | INJ/USD | 69.199 | 6.195 | +0.26% | 0.67x |
| 6 | ADA/USD | 68.343 | 0.148954 | +0.08% | 0.48x |
| 7 | LINK/USD | 67.898 | 9.23695 | +0.07% | 0.66x |
| 8 | XRP/USD | 64.701 | 0.94961 | -0.05% | 2.79x |
| 9 | SOL/USD | 61.457 | 71.11 | +0.31% | 1.41x |
| 10 | XDG/USD | 60.541 | 0.0568637 | +0.11% | 0.92x |
| 11 | XBT/USD | 59.652 | 60770.5 | -0.04% | 0.68x |
| 12 | ETH/USD | 59.248 | 1700.74 | +0.00% | 0.55x |

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

- Persisted scans: 1870; predictions: 16175; observations: 1133243.
- Matured sampled outcomes across 1/6/24/48h: 34982; gap abstentions: 24877. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45834511823 · **Generation:** 1870 · **Legacy run:** 45834511823
**Main quote time:** 2026-11-26T14:01:08.139541+00:00 · **Legacy report time:** 2026-11-26T14:02:03.256470+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD ⭐ | 1.112 | 90.35 | +0.18% | 2.36x | STRONG 95/100 | HIGH 61/100 | Watch |
| 2 | XRP/USD | 0.94961 | 79.45 | -0.05% | 2.79x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | QNT/USD | 151.63 | 71.72 | +0.36% | 0.30x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 4 | LTC/USD | 43.76 | 68.81 | +0.27% | 0.64x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 5 | INJ/USD | 6.195 | 67.18 | +0.26% | 0.67x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 6 | SOL/USD | 71.11 | 67.13 | +0.31% | 1.41x | STRONG 79/100 | HIGH 55/100 | Watch |
| 7 | LINK/USD | 9.23695 | 64.81 | +0.07% | 0.66x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 8 | ADA/USD | 0.148954 | 63.52 | +0.08% | 0.48x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 9 | FET/USD | 0.1155 | 62.46 | +0.43% | 0.06x | MODERATE 56/100 | VERY_HIGH 81/100 | Watch |
| 10 | XDG/USD | 0.0568637 | 60.34 | +0.11% | 0.92x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 11 | XBT/USD | 60770.5 | 56.26 | -0.04% | 0.68x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | ETH/USD | 1700.74 | 54.75 | +0.00% | 0.55x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZRO/USD ⭐ | 1.111 | 81.90 | +0.18% | 2.36x | 3320 | STRONG 96/100 | HIGH 55/100 | Watch |
| 2 | SEI/USD | 0.03708 | 81.57 | +2.32% | 1.66x | 3886 | STRONG 81/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** ZRO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
