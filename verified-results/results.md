# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T10:31:47.003096+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45375286145
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 40f81869941ed8e75bb4aebe339a84287d8f6209 (atomic ledger/results publication)
**Ledger generation:** 1562 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01254 | 95.993 | 78.496 | +8.85% | +2.11% | 1.70x | 15.9 | 2026-11-24T10:31:40.357053+00:00 | Not calibrated | STRONG 88/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 497.94 | 79.124 | 63.428 | +2.45% | +0.14% | 2.73x | 17.5 | 2026-11-24T10:31:40.357053+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 3 | VVV/USD | 25.23 | 67.792 | 73.226 | +3.20% | +0.13% | 0.39x | 8.3 | 2026-11-24T10:31:40.357053+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.458e-06 | 66.220 | 55.234 | +1.05% | -0.80% | 4.26x | 5.8 | 2026-11-24T10:31:40.357053+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 5 | DOS/USD | 0.1387 | 46.792 | 35.517 | +2.59% | +3.12% | 0.57x | 28.8 | 2026-11-24T10:31:40.357053+00:00 | Not calibrated | WEAK 43/100 | EXTREME 97/100 | Do nothing | WATCH |
| 6 | 2Z/USD | 0.01612 | 40.689 | 45.507 | +3.00% | +0.06% | 0.49x | 12.4 | 2026-11-24T10:31:40.357053+00:00 | Not calibrated | WEAK 35/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | ATOM/USD | 1.2878 | 27.802 | 32.056 | +0.44% | +0.27% | 0.44x | 8.5 | 2026-11-24T10:31:40.357053+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | BAT/USD | 0.07783 | 24.022 | 30.017 | +0.86% | -0.32% | 0.56x | 16.7 | 2026-11-24T10:31:40.357053+00:00 | Not calibrated | WEAK 12/100 | EXTREME 87/100 | Do nothing | WATCH |
| 9 | INX/USD | 0.003935 | 20.163 | 25.668 | +0.95% | -0.37% | 0.64x | 25.3 | 2026-11-24T10:31:40.357053+00:00 | Not calibrated | WEAK 5/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 78.496 | 0.01254 | +2.11% | 1.70x |
| 2 | VVV/USD | 73.226 | 25.23 | +0.13% | 0.39x |
| 3 | XMR/USD | 63.428 | 497.94 | +0.14% | 2.73x |
| 4 | PEPE/USD | 55.234 | 3.458e-06 | -0.80% | 4.26x |
| 5 | 2Z/USD | 45.507 | 0.01612 | +0.06% | 0.49x |
| 6 | DOS/USD | 35.517 | 0.1387 | +3.12% | 0.57x |
| 7 | ATOM/USD | 32.056 | 1.2878 | +0.27% | 0.44x |
| 8 | BAT/USD | 30.017 | 0.07783 | -0.32% | 0.56x |
| 9 | INX/USD | 25.668 | 0.003935 | -0.37% | 0.64x |

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

- Persisted scans: 1562; predictions: 13456; observations: 946356.
- Matured sampled outcomes across 1/6/24/48h: 25761; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45375286145 · **Generation:** 1562 · **Legacy run:** 45375286145
**Main quote time:** 2026-11-24T10:31:47.003096+00:00 · **Legacy report time:** 2026-11-24T10:32:34.369473+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01254 | 95.99 | +2.11% | 1.70x | STRONG 98/100 | HIGH 61/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 497.94 | 79.12 | +0.14% | 2.73x | STRONG 90/100 | HIGH 61/100 | Watch |
| 3 | VVV/USD | 25.23 | 67.79 | +0.13% | 0.39x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 4 | PEPE/USD | 3.458e-06 | 66.22 | -0.80% | 4.26x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 5 | DOS/USD | 0.1387 | 46.79 | +3.12% | 0.57x | WEAK 43/100 | EXTREME 97/100 | Do nothing |
| 6 | 2Z/USD | 0.01612 | 40.69 | +0.06% | 0.49x | WEAK 35/100 | EXTREME 88/100 | Do nothing |
| 7 | ATOM/USD | 1.2878 | 27.80 | +0.27% | 0.44x | WEAK 44/100 | VERY_HIGH 75/100 | Watch |
| 8 | BAT/USD | 0.07783 | 24.02 | -0.32% | 0.56x | WEAK 12/100 | EXTREME 87/100 | Do nothing |
| 9 | INX/USD | 0.003935 | 20.16 | -0.37% | 0.64x | WEAK 5/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01262 | 86.03 | +2.11% | 1.70x | 10322 | STRONG 93/100 | HIGH 61/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 498.4 | 74.92 | +0.14% | 2.73x | 10996 | STRONG 87/100 | HIGH 61/100 | Watch |

**Same-run overlap:** MON/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
