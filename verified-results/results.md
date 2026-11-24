# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T06:11:34.598685+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45338361093
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a56e7200333dc1a3f4c4a0f59540f1073d0bbc9a (atomic ledger/results publication)
**Ledger generation:** 1535 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.466 | 83.954 | 79.624 | +4.16% | +0.64% | 1.11x | 9.0 | 2026-11-24T06:11:27.082259+00:00 | Not calibrated | STRONG 77/100 | HIGH 62/100 | Watch | WATCH |
| 2 | PEPE/USD | 3.555e-06 | 83.755 | 74.963 | +3.89% | -1.19% | 2.48x | 5.6 | 2026-11-24T06:11:27.082259+00:00 | Not calibrated | STRONG 72/100 | HIGH 65/100 | Watch | WATCH |
| 3 | NEAR/USD | 3.0346 | 77.924 | 65.726 | +1.79% | -0.56% | 3.47x | 3.6 | 2026-11-24T06:11:27.082259+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 4 | BAT/USD | 0.08057 | 72.144 | 60.541 | +4.41% | -0.68% | 7.69x | 5.0 | 2026-11-24T06:11:27.082259+00:00 | Not calibrated | MODERATE 66/100 | HIGH 66/100 | Watch | WATCH |
| 5 | LINK/USD | 9.10469 | 61.291 | 61.854 | +1.11% | -0.52% | 1.20x | 1.8 | 2026-11-24T06:11:27.082259+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 6 | ICNT/USD | 0.3332 | 56.477 | 68.341 | +7.80% | -0.75% | 0.19x | 18.1 | 2026-11-24T06:11:27.082259+00:00 | Not calibrated | WEAK 28/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | XRP/USD | 0.95265 | 55.949 | 64.513 | +1.41% | -0.58% | 0.43x | 0.7 | 2026-11-24T06:11:27.082259+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | XMR/USD | 494.79 | 55.089 | 62.474 | +1.80% | -0.27% | 0.40x | 10.3 | 2026-11-24T06:11:27.082259+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 9 | XDG/USD | 0.0566287 | 52.195 | 59.014 | +0.57% | -0.44% | 0.54x | 0.0 | 2026-11-24T06:11:27.082259+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | HYPE/USD | 64.16 | 48.132 | 59.941 | +0.82% | -0.50% | 0.07x | 1.6 | 2026-11-24T06:11:27.082259+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XLM/USD | 0.130623 | 46.351 | 57.736 | +0.48% | -0.46% | 0.09x | 1.3 | 2026-11-24T06:11:27.082259+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | TON/USD | 0.992 | 44.280 | 30.785 | +0.40% | -0.30% | 2.69x | 10.1 | 2026-11-24T06:11:27.082259+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 72/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 79.624 | 25.466 | +0.64% | 1.11x |
| 2 | PEPE/USD | 74.963 | 3.555e-06 | -1.19% | 2.48x |
| 3 | ICNT/USD | 68.341 | 0.3332 | -0.75% | 0.19x |
| 4 | NEAR/USD | 65.726 | 3.0346 | -0.56% | 3.47x |
| 5 | XRP/USD | 64.513 | 0.95265 | -0.58% | 0.43x |
| 6 | XMR/USD | 62.474 | 494.79 | -0.27% | 0.40x |
| 7 | LINK/USD | 61.854 | 9.10469 | -0.52% | 1.20x |
| 8 | BAT/USD | 60.541 | 0.08057 | -0.68% | 7.69x |
| 9 | HYPE/USD | 59.941 | 64.16 | -0.50% | 0.07x |
| 10 | XDG/USD | 59.014 | 0.0566287 | -0.44% | 0.54x |
| 11 | XLM/USD | 57.736 | 0.130623 | -0.46% | 0.09x |
| 12 | TON/USD | 30.785 | 0.992 | -0.30% | 2.69x |

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

- Persisted scans: 1535; predictions: 13153; observations: 929913.
- Matured sampled outcomes across 1/6/24/48h: 24679; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 137 (sampled only; not a success-rate estimate).
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

**Writer:** 45338361093 · **Generation:** 1535 · **Legacy run:** 45338361093
**Main quote time:** 2026-11-24T06:11:34.598685+00:00 · **Legacy report time:** 2026-11-24T06:12:45.995550+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.466 | 83.95 | +0.64% | 1.11x | STRONG 87/100 | HIGH 62/100 | Watch |
| 2 | PEPE/USD | 3.555e-06 | 83.76 | -1.19% | 2.48x | STRONG 72/100 | HIGH 65/100 | Watch |
| 3 | NEAR/USD | 3.0346 | 77.92 | -0.56% | 3.47x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 4 | BAT/USD | 0.08057 | 72.14 | -0.68% | 7.69x | MODERATE 66/100 | HIGH 66/100 | Watch |
| 5 | LINK/USD | 9.10469 | 61.29 | -0.52% | 1.20x | WEAK 41/100 | HIGH 68/100 | Watch |
| 6 | ICNT/USD | 0.3332 | 56.48 | -0.75% | 0.19x | WEAK 28/100 | EXTREME 87/100 | Do nothing |
| 7 | XRP/USD | 0.95265 | 55.95 | -0.58% | 0.43x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | XMR/USD | 494.79 | 55.09 | -0.27% | 0.40x | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing |
| 9 | XDG/USD | 0.0566287 | 52.20 | -0.44% | 0.54x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | HYPE/USD | 64.16 | 48.13 | -0.50% | 0.07x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XLM/USD | 0.130623 | 46.35 | -0.46% | 0.09x | WEAK 28/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | TON/USD | 0.992 | 44.28 | -0.30% | 2.69x | MODERATE 47/100 | VERY_HIGH 72/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.41 | 86.59 | +0.64% | 1.11x | 12384 | STRONG 88/100 | HIGH 62/100 | Watch |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
