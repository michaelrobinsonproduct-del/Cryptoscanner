# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T09:32:17.545648+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45365697811
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 073234b1392992dffdff9ad047f537784cafe21d (atomic ledger/results publication)
**Ledger generation:** 1556 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 24.881 | 77.516 | 64.381 | +1.77% | +0.29% | 2.17x | 6.0 | 2026-11-24T09:32:09.219555+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | MON/USD | 0.01262 | 74.785 | 82.629 | +9.55% | -1.86% | 1.15x | 7.9 | 2026-11-24T09:32:09.219555+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 3 | PEPE/USD | 3.492e-06 | 63.275 | 63.453 | +2.05% | -0.11% | 1.04x | 2.9 | 2026-11-24T09:32:09.219555+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 4 | XMR/USD | 497.59 | 61.244 | 66.239 | +2.38% | +0.33% | 0.34x | 10.9 | 2026-11-24T09:32:09.219555+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | LINK/USD | 9.03783 | 60.216 | 55.133 | +0.37% | +0.16% | 1.43x | 4.8 | 2026-11-24T09:32:09.219555+00:00 | Not calibrated | MODERATE 65/100 | HIGH 55/100 | Watch | WATCH |
| 6 | 2Z/USD | 0.01623 | 56.852 | 53.584 | +3.71% | +0.00% | 1.33x | 6.2 | 2026-11-24T09:32:09.219555+00:00 | Not calibrated | MODERATE 63/100 | HIGH 67/100 | Watch | WATCH |
| 7 | LUNA/USD | 4.636e-05 | 49.571 | 55.529 | +6.65% | -0.39% | 0.60x | 43.1 | 2026-11-24T09:32:09.219555+00:00 | Not calibrated | WEAK 15/100 | EXTREME 100/100 | Do nothing | WATCH |
| 8 | INX/USD | 0.004079 | 48.123 | 54.446 | +4.64% | -0.73% | 0.73x | 19.6 | 2026-11-24T09:32:09.219555+00:00 | Not calibrated | WEAK 24/100 | EXTREME 87/100 | Do nothing | WATCH |
| 9 | BABY/USD | 0.00895 | 42.263 | 58.543 | +5.29% | -1.55% | 0.15x | 22.4 | 2026-11-24T09:32:09.219555+00:00 | Not calibrated | WEAK 16/100 | EXTREME 97/100 | Do nothing | WATCH |
| 10 | ATOM/USD | 1.2958 | 30.547 | 34.884 | +1.06% | +0.00% | 0.57x | 11.6 | 2026-11-24T09:32:09.219555+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 11 | XDC/USD | 0.02623 | 28.571 | 34.282 | +0.96% | +0.08% | 0.39x | 15.3 | 2026-11-24T09:32:09.219555+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 82.629 | 0.01262 | -1.86% | 1.15x |
| 2 | XMR/USD | 66.239 | 497.59 | +0.33% | 0.34x |
| 3 | VVV/USD | 64.381 | 24.881 | +0.29% | 2.17x |
| 4 | PEPE/USD | 63.453 | 3.492e-06 | -0.11% | 1.04x |
| 5 | BABY/USD | 58.543 | 0.00895 | -1.55% | 0.15x |
| 6 | LUNA/USD | 55.529 | 4.636e-05 | -0.39% | 0.60x |
| 7 | LINK/USD | 55.133 | 9.03783 | +0.16% | 1.43x |
| 8 | INX/USD | 54.446 | 0.004079 | -0.73% | 0.73x |
| 9 | 2Z/USD | 53.584 | 0.01623 | +0.00% | 1.33x |
| 10 | ATOM/USD | 34.884 | 1.2958 | +0.00% | 0.57x |
| 11 | XDC/USD | 34.282 | 0.02623 | +0.08% | 0.39x |

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

- Persisted scans: 1556; predictions: 13397; observations: 942702.
- Matured sampled outcomes across 1/6/24/48h: 25491; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 142 (sampled only; not a success-rate estimate).
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

**Writer:** 45365697811 · **Generation:** 1556 · **Legacy run:** 45365697811
**Main quote time:** 2026-11-24T09:32:17.545648+00:00 · **Legacy report time:** 2026-11-24T09:33:19.823923+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 24.881 | 77.52 | +0.29% | 2.17x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | MON/USD | 0.01262 | 74.78 | -1.86% | 1.15x | MODERATE 47/100 | VERY_HIGH 72/100 | Do nothing |
| 3 | PEPE/USD | 3.492e-06 | 63.27 | -0.11% | 1.04x | WEAK 42/100 | HIGH 68/100 | Watch |
| 4 | XMR/USD | 497.59 | 61.24 | +0.33% | 0.34x | MODERATE 56/100 | VERY_HIGH 76/100 | Watch |
| 5 | LINK/USD ⭐ | 9.03783 | 60.22 | +0.16% | 1.43x | STRONG 75/100 | HIGH 55/100 | Watch |
| 6 | 2Z/USD | 0.01623 | 56.85 | +0.00% | 1.33x | MODERATE 63/100 | HIGH 67/100 | Watch |
| 7 | LUNA/USD | 4.636e-05 | 49.57 | -0.39% | 0.60x | WEAK 15/100 | EXTREME 100/100 | Do nothing |
| 8 | INX/USD | 0.004079 | 48.12 | -0.73% | 0.73x | WEAK 24/100 | EXTREME 87/100 | Do nothing |
| 9 | BABY/USD | 0.00895 | 42.26 | -1.55% | 0.15x | WEAK 16/100 | EXTREME 97/100 | Do nothing |
| 10 | ATOM/USD | 1.2958 | 30.55 | +0.00% | 0.57x | WEAK 30/100 | VERY_HIGH 81/100 | Do nothing |
| 11 | XDC/USD | 0.02623 | 28.57 | +0.08% | 0.39x | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 24.848 | 62.18 | +0.29% | 2.17x | 13177 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 2 | LINK/USD ⭐ | 9.0342 | 47.93 | +0.16% | 1.43x | 8621 | MODERATE 69/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
