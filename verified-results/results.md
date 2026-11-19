# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T22:50:33.091751+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44632191739
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 0f08e97a243f548a821eb130ec4feb4cabecc02f (atomic ledger/results publication)
**Ledger generation:** 874 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 602; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 21.982 | 77.265 | 61.399 | +1.44% | +0.17% | 2.55x | 7.3 | 2026-11-19T22:50:26.979520+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 2 | MEGA/USD | 0.05998 | 76.080 | 70.558 | +7.11% | -0.88% | 1.99x | 13.3 | 2026-11-19T22:50:26.979520+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | ADA/USD | 0.151764 | 69.684 | 54.723 | +0.34% | -0.01% | 2.71x | 5.3 | 2026-11-19T22:50:26.979520+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | CT/USD | 0.1291 | 68.175 | 65.152 | +9.22% | +0.39% | 1.11x | 23.3 | 2026-11-19T22:50:26.979520+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | TRX/USD | 0.310406 | 59.901 | 44.775 | +0.36% | +0.03% | 12.40x | 0.1 | 2026-11-19T22:50:26.979520+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 6 | USELESS/USD | 0.09926 | 57.918 | 60.707 | +3.87% | -0.48% | 0.96x | 13.1 | 2026-11-19T22:50:26.979520+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 7 | SENT/USD | 0.021565 | 55.622 | 63.099 | +4.66% | +0.31% | 0.10x | 7.9 | 2026-11-19T22:50:26.979520+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | HYPE/USD | 67.11 | 52.041 | 55.917 | +0.34% | +0.27% | 0.48x | 3.0 | 2026-11-19T22:50:26.979520+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | AKT/USD | 0.5392 | 51.640 | 55.439 | +4.09% | +0.28% | 0.48x | 11.1 | 2026-11-19T22:50:26.979520+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | INJ/USD | 7.086 | 51.321 | 53.902 | +1.50% | +0.20% | 0.64x | 4.2 | 2026-11-19T22:50:26.979520+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | PYTH/USD | 0.05307 | 29.062 | 34.504 | +0.59% | -0.15% | 0.53x | 5.7 | 2026-11-19T22:50:26.979520+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MEGA/USD | 70.558 | 0.05998 | -0.88% | 1.99x |
| 2 | CT/USD | 65.152 | 0.1291 | +0.39% | 1.11x |
| 3 | SENT/USD | 63.099 | 0.021565 | +0.31% | 0.10x |
| 4 | VVV/USD | 61.399 | 21.982 | +0.17% | 2.55x |
| 5 | USELESS/USD | 60.707 | 0.09926 | -0.48% | 0.96x |
| 6 | HYPE/USD | 55.917 | 67.11 | +0.27% | 0.48x |
| 7 | AKT/USD | 55.439 | 0.5392 | +0.28% | 0.48x |
| 8 | ADA/USD | 54.723 | 0.151764 | -0.01% | 2.71x |
| 9 | INJ/USD | 53.902 | 7.086 | +0.20% | 0.64x |
| 10 | TRX/USD | 44.775 | 0.310406 | +0.03% | 12.40x |
| 11 | PYTH/USD | 34.504 | 0.05307 | -0.15% | 0.53x |

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

- Persisted scans: 874; predictions: 7606; observations: 528150.
- Matured sampled outcomes across 1/6/24/48h: 8034; gap abstentions: 15760. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44632191739 · **Generation:** 874 · **Legacy run:** 44632191739
**Main quote time:** 2026-11-19T22:50:33.091751+00:00 · **Legacy report time:** 2026-11-19T22:51:20.125561+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.982 | 77.26 | +0.17% | 2.55x | STRONG 94/100 | HIGH 55/100 | Watch |
| 2 | MEGA/USD | 0.05998 | 76.08 | -0.88% | 1.99x | MODERATE 53/100 | VERY_HIGH 72/100 | Watch |
| 3 | ADA/USD | 0.151764 | 69.68 | -0.01% | 2.71x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | CT/USD ⭐ | 0.1291 | 68.18 | +0.39% | 1.11x | MODERATE 69/100 | VERY_HIGH 79/100 | Watch |
| 5 | TRX/USD | 0.310406 | 59.90 | +0.03% | 12.40x | STRONG 75/100 | HIGH 55/100 | Watch |
| 6 | USELESS/USD | 0.09926 | 57.92 | -0.48% | 0.96x | WEAK 29/100 | VERY_HIGH 74/100 | Do nothing |
| 7 | SENT/USD | 0.021565 | 55.62 | +0.31% | 0.10x | MODERATE 58/100 | VERY_HIGH 75/100 | Watch |
| 8 | HYPE/USD | 67.11 | 52.04 | +0.27% | 0.48x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 9 | AKT/USD | 0.5392 | 51.64 | +0.28% | 0.48x | MODERATE 51/100 | VERY_HIGH 81/100 | Watch |
| 10 | INJ/USD | 7.086 | 51.32 | +0.20% | 0.64x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 11 | PYTH/USD | 0.05307 | 29.06 | -0.15% | 0.53x | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CT/USD ⭐ | 0.1291 | 69.34 | +0.39% | 1.11x | 2241 | STRONG 70/100 | VERY_HIGH 79/100 | Watch |
| 2 | VVV/USD ⭐ | 21.982 | 67.73 | +0.17% | 2.55x | 13384 | STRONG 89/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, CT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
