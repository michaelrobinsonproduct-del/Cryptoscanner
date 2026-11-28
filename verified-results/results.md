# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T06:27:40.771690+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46116461392
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** efb473e16418238aa8e575855790ccd875bfc41a (atomic ledger/results publication)
**Ledger generation:** 2117 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 429.22 | 87.559 | 81.514 | +5.39% | +1.50% | 0.85x | 22.4 | 2026-11-28T06:27:37.524584+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0269 | 73.626 | 55.531 | +0.29% | +0.62% | 6.61x | 3.0 | 2026-11-28T06:27:37.524584+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ZEC/USD | 740.43 | 63.194 | 59.572 | +0.80% | +0.74% | 0.99x | 2.0 | 2026-11-28T06:27:37.524584+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 4 | SPACE/USD | 0.004298 | 62.304 | 45.033 | +2.87% | +0.58% | 2.43x | 11.7 | 2026-11-28T06:27:37.524584+00:00 | Not calibrated | STRONG 81/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | VVV/USD | 26.21 | 62.096 | 53.917 | +1.79% | +0.27% | 1.68x | 8.0 | 2026-11-28T06:27:37.524584+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 6 | CFG/USD | 0.0631 | 52.785 | 62.105 | +11.88% | -0.32% | 0.23x | 31.7 | 2026-11-28T06:27:37.524584+00:00 | Not calibrated | WEAK 21/100 | EXTREME 93/100 | Do nothing | WATCH |
| 7 | SENT/USD | 0.024294 | 50.149 | 45.513 | +2.45% | +1.20% | 0.86x | 5.4 | 2026-11-28T06:27:37.524584+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 8 | KAVA/USD | 0.0274 | 24.460 | 15.739 | +0.37% | +1.10% | 1.32x | 36.5 | 2026-11-28T06:27:37.524584+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 79/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 81.514 | 429.22 | +1.50% | 0.85x |
| 2 | CFG/USD | 62.105 | 0.0631 | -0.32% | 0.23x |
| 3 | ZEC/USD | 59.572 | 740.43 | +0.74% | 0.99x |
| 4 | NEAR/USD | 55.531 | 3.0269 | +0.62% | 6.61x |
| 5 | VVV/USD | 53.917 | 26.21 | +0.27% | 1.68x |
| 6 | SENT/USD | 45.513 | 0.024294 | +1.20% | 0.86x |
| 7 | SPACE/USD | 45.033 | 0.004298 | +0.58% | 2.43x |
| 8 | KAVA/USD | 15.739 | 0.0274 | +1.10% | 1.32x |

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

- Persisted scans: 2117; predictions: 18981; observations: 1281948.
- Matured sampled outcomes across 1/6/24/48h: 44416; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46116461392 · **Generation:** 2117 · **Legacy run:** 46116461392
**Main quote time:** 2026-11-28T06:27:40.771690+00:00 · **Legacy report time:** 2026-11-28T06:28:37.751707+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 429.22 | 87.56 | +1.50% | 0.85x | MODERATE 64/100 | VERY_HIGH 74/100 | Watch |
| 2 | NEAR/USD ⭐ | 3.0269 | 73.63 | +0.62% | 6.61x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ZEC/USD | 740.43 | 63.19 | +0.74% | 0.99x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 4 | SPACE/USD ⭐ | 0.004298 | 62.30 | +0.58% | 2.43x | STRONG 91/100 | VERY_HIGH 73/100 | Watch |
| 5 | VVV/USD ⭐ | 26.21 | 62.10 | +0.27% | 1.68x | STRONG 86/100 | HIGH 55/100 | Consider small entry |
| 6 | CFG/USD | 0.0631 | 52.78 | -0.32% | 0.23x | WEAK 21/100 | EXTREME 93/100 | Do nothing |
| 7 | SENT/USD | 0.024294 | 50.15 | +1.20% | 0.86x | MODERATE 55/100 | VERY_HIGH 74/100 | Watch |
| 8 | KAVA/USD ⭐ | 0.0274 | 24.46 | +1.10% | 1.32x | MODERATE 52/100 | VERY_HIGH 79/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SPACE/USD ⭐ | 0.004298 | 58.79 | +0.58% | 2.43x | 1965 | STRONG 94/100 | HIGH 67/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.0265 | 57.23 | +0.62% | 6.61x | 13641 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD ⭐ | 26.164 | 54.12 | +0.27% | 1.68x | 7933 | STRONG 82/100 | HIGH 55/100 | Consider small entry |
| 4 | KAVA/USD ⭐ | 0.0275 | 26.76 | +1.10% | 1.32x | 1502 | MODERATE 53/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** NEAR/USD, SPACE/USD, VVV/USD, KAVA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
