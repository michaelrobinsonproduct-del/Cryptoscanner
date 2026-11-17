# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T23:45:06.541968+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44202002509
**Source SHA:** 113db7a045b71125e52affc5c74a39ca3094a032
**Previous ledger commit:** 9500f95608a11bae428daf6f3f5b2e78e313c642 (atomic ledger/results publication)
**Ledger generation:** 474 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 963 | 118.243 | 99.948 | +6.55% | +0.66% | 3.46x | 0.1 | 2026-11-17T23:44:58.349464+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | INJ/USD | 7.382 | 110.076 | 97.294 | +7.00% | +1.13% | 1.71x | 5.4 | 2026-11-17T23:44:58.349464+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.3813 | 103.445 | 97.486 | +7.08% | +0.50% | 1.34x | 5.0 | 2026-11-17T23:44:58.349464+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 4 | XRP/USD | 0.98383 | 91.471 | 76.262 | +3.04% | +0.04% | 2.78x | 0.1 | 2026-11-17T23:44:58.349464+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 5 | VVV/USD | 21.125 | 86.479 | 77.232 | +4.85% | +0.29% | 1.78x | 9.0 | 2026-11-17T23:44:58.349464+00:00 | Not calibrated | STRONG 88/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | SOL/USD | 74.94 | 86.235 | 87.806 | +4.78% | +0.01% | 0.84x | 1.3 | 2026-11-17T23:44:58.349464+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XMR/USD | 509.47 | 75.263 | 74.001 | +3.22% | -0.16% | 1.21x | 7.1 | 2026-11-17T23:44:58.349464+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 8 | RENDER/USD | 1.474 | 74.224 | 75.757 | +7.04% | -1.28% | 1.49x | 6.8 | 2026-11-17T23:44:58.349464+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 9 | TAO/USD | 197.1979 | 66.738 | 72.742 | +3.14% | -0.10% | 0.45x | 8.4 | 2026-11-17T23:44:58.349464+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | SUI/USD | 0.7379 | 65.560 | 71.645 | +2.57% | +0.15% | 0.32x | 2.7 | 2026-11-17T23:44:58.349464+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0599805 | 59.303 | 67.499 | +1.86% | +0.01% | 0.18x | 0.1 | 2026-11-17T23:44:58.349464+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XLM/USD | 0.14102 | 56.488 | 60.235 | +2.34% | -0.09% | 0.67x | 0.1 | 2026-11-17T23:44:58.349464+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.948 | 963 | +0.66% | 3.46x |
| 2 | NEAR/USD | 97.486 | 3.3813 | +0.50% | 1.34x |
| 3 | INJ/USD | 97.294 | 7.382 | +1.13% | 1.71x |
| 4 | SOL/USD | 87.806 | 74.94 | +0.01% | 0.84x |
| 5 | VVV/USD | 77.232 | 21.125 | +0.29% | 1.78x |
| 6 | XRP/USD | 76.262 | 0.98383 | +0.04% | 2.78x |
| 7 | RENDER/USD | 75.757 | 1.474 | -1.28% | 1.49x |
| 8 | XMR/USD | 74.001 | 509.47 | -0.16% | 1.21x |
| 9 | TAO/USD | 72.742 | 197.1979 | -0.10% | 0.45x |
| 10 | SUI/USD | 71.645 | 0.7379 | +0.15% | 0.32x |
| 11 | XDG/USD | 67.499 | 0.0599805 | +0.01% | 0.18x |
| 12 | XLM/USD | 60.235 | 0.14102 | -0.09% | 0.67x |

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

- Persisted scans: 474; predictions: 4169; observations: 285673.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12398. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44202002509 · **Generation:** 474 · **Legacy run:** 44202002509
**Main quote time:** 2026-11-17T23:45:06.541968+00:00 · **Legacy report time:** 2026-11-17T23:45:17.619176+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 963 | 118.24 | +0.66% | 3.46x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 7.382 | 110.08 | +1.13% | 1.71x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD | 3.3813 | 103.45 | +0.50% | 1.34x | STRONG 95/100 | HIGH 55/100 | Watch |
| 4 | XRP/USD | 0.98383 | 91.47 | +0.04% | 2.78x | STRONG 91/100 | HIGH 55/100 | Watch |
| 5 | VVV/USD | 21.125 | 86.48 | +0.29% | 1.78x | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 6 | SOL/USD | 74.94 | 86.24 | +0.01% | 0.84x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 7 | XMR/USD | 509.47 | 75.26 | -0.16% | 1.21x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 8 | RENDER/USD | 1.474 | 74.22 | -1.28% | 1.49x | MODERATE 57/100 | VERY_HIGH 70/100 | Do nothing |
| 9 | TAO/USD | 197.1979 | 66.74 | -0.10% | 0.45x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 10 | SUI/USD | 0.7379 | 65.56 | +0.15% | 0.32x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 11 | XDG/USD | 0.0599805 | 59.30 | +0.01% | 0.18x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 12 | XLM/USD | 0.14102 | 56.49 | -0.09% | 0.67x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 7.382 | 87.80 | +0.54% | 1.29x | 9932 | STRONG 89/100 | HIGH 55/100 | Watch |

**Same-run overlap:** INJ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
