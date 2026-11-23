# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T13:41:56.028907+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45186099965
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c9909fff31bf0b8aefa9d4c9d58fabcf0a8d56c0 (atomic ledger/results publication)
**Ledger generation:** 1437 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ALGO/USD | 0.08448 | 92.547 | 76.956 | +12.00% | +0.12% | 4.56x | 9.5 | 2026-11-23T13:41:48.174491+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 2 | QNT/USD | 157.53 | 85.692 | 89.694 | +9.82% | +0.68% | 0.26x | 7.0 | 2026-11-23T13:41:48.174491+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | HYPE/USD | 64.03 | 79.439 | 64.986 | +1.54% | -0.11% | 4.78x | 1.6 | 2026-11-23T13:41:48.174491+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 4 | CCD/USD | 0.00294 | 74.879 | 72.540 | +10.53% | +1.03% | 0.72x | 6.8 | 2026-11-23T13:41:48.174491+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | NEAR/USD | 2.9949 | 70.928 | 56.262 | +0.44% | -0.07% | 2.52x | 3.7 | 2026-11-23T13:41:48.174491+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 6 | SOL/USD | 72.47 | 70.089 | 72.546 | +2.61% | -0.01% | 0.76x | 1.4 | 2026-11-23T13:41:48.174491+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 7 | LTC/USD | 40.78 | 65.162 | 51.993 | +1.54% | -0.37% | 3.52x | 2.5 | 2026-11-23T13:41:48.174491+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 8 | XRP/USD | 0.94035 | 64.976 | 64.348 | +1.38% | -0.25% | 1.19x | 0.6 | 2026-11-23T13:41:48.174491+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 9 | PAXG/USD | 3605.85 | 63.406 | 49.761 | +0.94% | -0.27% | 20.54x | 1.7 | 2026-11-23T13:41:48.174491+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6691 | 62.835 | 68.558 | +2.04% | +0.06% | 0.40x | 1.5 | 2026-11-23T13:41:48.174491+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XDG/USD | 0.055589 | 60.654 | 50.159 | +0.55% | -0.15% | 2.13x | 0.4 | 2026-11-23T13:41:48.174491+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 12 | GRT/USD | 0.01689 | 56.202 | 64.222 | +5.63% | -0.24% | 0.32x | 11.8 | 2026-11-23T13:41:48.174491+00:00 | Not calibrated | WEAK 28/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 89.694 | 157.53 | +0.68% | 0.26x |
| 2 | ALGO/USD | 76.956 | 0.08448 | +0.12% | 4.56x |
| 3 | SOL/USD | 72.546 | 72.47 | -0.01% | 0.76x |
| 4 | CCD/USD | 72.540 | 0.00294 | +1.03% | 0.72x |
| 5 | SUI/USD | 68.558 | 0.6691 | +0.06% | 0.40x |
| 6 | HYPE/USD | 64.986 | 64.03 | -0.11% | 4.78x |
| 7 | XRP/USD | 64.348 | 0.94035 | -0.25% | 1.19x |
| 8 | GRT/USD | 64.222 | 0.01689 | -0.24% | 0.32x |
| 9 | NEAR/USD | 56.262 | 2.9949 | -0.07% | 2.52x |
| 10 | LTC/USD | 51.993 | 40.78 | -0.37% | 3.52x |
| 11 | XDG/USD | 50.159 | 0.055589 | -0.15% | 2.13x |
| 12 | PAXG/USD | 49.761 | 3605.85 | -0.27% | 20.54x |

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

- Persisted scans: 1437; predictions: 12011; observations: 870235.
- Matured sampled outcomes across 1/6/24/48h: 20287; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45186099965 · **Generation:** 1437 · **Legacy run:** 45186099965
**Main quote time:** 2026-11-23T13:41:56.028907+00:00 · **Legacy report time:** 2026-11-23T13:43:06.567649+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD ⭐ | 0.08448 | 92.55 | +0.12% | 4.56x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | QNT/USD | 157.53 | 85.69 | +0.68% | 0.26x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 3 | HYPE/USD | 64.03 | 79.44 | -0.11% | 4.78x | STRONG 70/100 | HIGH 61/100 | Watch |
| 4 | CCD/USD | 0.00294 | 74.88 | +1.03% | 0.72x | MODERATE 67/100 | VERY_HIGH 82/100 | Watch |
| 5 | NEAR/USD | 2.9949 | 70.93 | -0.07% | 2.52x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 6 | SOL/USD | 72.47 | 70.09 | -0.01% | 0.76x | WEAK 40/100 | HIGH 68/100 | Watch |
| 7 | LTC/USD | 40.78 | 65.16 | -0.37% | 3.52x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 8 | XRP/USD | 0.94035 | 64.98 | -0.25% | 1.19x | WEAK 42/100 | HIGH 68/100 | Watch |
| 9 | PAXG/USD | 3605.85 | 63.41 | -0.27% | 20.54x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 10 | SUI/USD | 0.6691 | 62.84 | +0.06% | 0.40x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 11 | XDG/USD | 0.055589 | 60.65 | -0.15% | 2.13x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 12 | GRT/USD | 0.01689 | 56.20 | -0.24% | 0.32x | WEAK 28/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD ⭐ | 0.0846 | 83.18 | +0.12% | 4.56x | 4628 | STRONG 97/100 | HIGH 55/100 | Watch |

**Same-run overlap:** ALGO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
