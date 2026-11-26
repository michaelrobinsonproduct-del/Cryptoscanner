# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T10:26:23.402824+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45801050933
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c70ab3505afaff66f269306f022440fc6c3572b3 (atomic ledger/results publication)
**Ledger generation:** 1848 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 585; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SYRUP/USD | 0.07084 | 81.349 | 66.772 | +6.90% | -0.08% | 4.84x | 21.2 | 2026-11-26T10:26:15.188867+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 2 | INJ/USD | 6.192 | 80.314 | 70.007 | +4.00% | -0.18% | 2.12x | 3.2 | 2026-11-26T10:26:15.188867+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XMR/USD | 525.72 | 79.859 | 64.783 | +1.70% | +0.02% | 6.10x | 4.2 | 2026-11-26T10:26:15.188867+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SEI/USD | 0.03583 | 70.444 | 71.706 | +7.57% | -0.47% | 1.11x | 11.2 | 2026-11-26T10:26:15.188867+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | ADA/USD | 0.148491 | 69.524 | 66.450 | +1.87% | -0.14% | 1.38x | 3.2 | 2026-11-26T10:26:15.188867+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 6 | LTC/USD | 43.57 | 68.401 | 66.799 | +2.01% | -0.18% | 1.25x | 4.6 | 2026-11-26T10:26:15.188867+00:00 | Not calibrated | WEAK 44/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XRP/USD | 0.95227 | 63.711 | 66.689 | +1.68% | -0.12% | 0.76x | 0.1 | 2026-11-26T10:26:15.188867+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 8 | LINK/USD | 9.23148 | 60.435 | 68.533 | +2.07% | -0.33% | 0.36x | 1.9 | 2026-11-26T10:26:15.188867+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | SOL/USD | 70.91 | 60.059 | 59.466 | +0.74% | -0.25% | 1.19x | 1.4 | 2026-11-26T10:26:15.188867+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 10 | AAVE/USD | 95.89 | 59.398 | 47.208 | +0.56% | -0.29% | 2.36x | 1.0 | 2026-11-26T10:26:15.188867+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 11 | XBT/USD | 60755.3 | 55.657 | 59.476 | +0.64% | -0.15% | 0.70x | 0.0 | 2026-11-26T10:26:15.188867+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XDG/USD | 0.0566224 | 53.954 | 58.459 | +1.19% | -0.05% | 0.58x | 0.3 | 2026-11-26T10:26:15.188867+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SEI/USD | 71.706 | 0.03583 | -0.47% | 1.11x |
| 2 | INJ/USD | 70.007 | 6.192 | -0.18% | 2.12x |
| 3 | LINK/USD | 68.533 | 9.23148 | -0.33% | 0.36x |
| 4 | LTC/USD | 66.799 | 43.57 | -0.18% | 1.25x |
| 5 | SYRUP/USD | 66.772 | 0.07084 | -0.08% | 4.84x |
| 6 | XRP/USD | 66.689 | 0.95227 | -0.12% | 0.76x |
| 7 | ADA/USD | 66.450 | 0.148491 | -0.14% | 1.38x |
| 8 | XMR/USD | 64.783 | 525.72 | +0.02% | 6.10x |
| 9 | XBT/USD | 59.476 | 60755.3 | -0.15% | 0.70x |
| 10 | SOL/USD | 59.466 | 70.91 | -0.25% | 1.19x |
| 11 | XDG/USD | 58.459 | 0.0566224 | -0.05% | 0.58x |
| 12 | AAVE/USD | 47.208 | 95.89 | -0.29% | 2.36x |

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

- Persisted scans: 1848; predictions: 15911; observations: 1120325.
- Matured sampled outcomes across 1/6/24/48h: 34466; gap abstentions: 24555. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45801050933 · **Generation:** 1848 · **Legacy run:** 45801050933
**Main quote time:** 2026-11-26T10:26:23.402824+00:00 · **Legacy report time:** 2026-11-26T10:27:37.139425+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD | 0.07084 | 81.35 | -0.08% | 4.84x | MODERATE 61/100 | VERY_HIGH 78/100 | Watch |
| 2 | INJ/USD | 6.192 | 80.31 | -0.18% | 2.12x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | XMR/USD | 525.72 | 79.86 | +0.02% | 6.10x | STRONG 85/100 | HIGH 55/100 | Watch |
| 4 | SEI/USD | 0.03583 | 70.44 | -0.47% | 1.11x | WEAK 40/100 | VERY_HIGH 79/100 | Watch |
| 5 | ADA/USD | 0.148491 | 69.52 | -0.14% | 1.38x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 6 | LTC/USD | 43.57 | 68.40 | -0.18% | 1.25x | WEAK 44/100 | HIGH 61/100 | Watch |
| 7 | XRP/USD | 0.95227 | 63.71 | -0.12% | 0.76x | WEAK 37/100 | HIGH 68/100 | Watch |
| 8 | LINK/USD | 9.23148 | 60.44 | -0.33% | 0.36x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 9 | SOL/USD | 70.91 | 60.06 | -0.25% | 1.19x | WEAK 40/100 | HIGH 68/100 | Watch |
| 10 | AAVE/USD | 95.89 | 59.40 | -0.29% | 2.36x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 11 | XBT/USD | 60755.3 | 55.66 | -0.15% | 0.70x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XDG/USD | 0.0566224 | 53.95 | -0.05% | 0.58x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD | 0.002659 | 72.86 | +0.42% | 1.66x | 6021 | STRONG 76/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
