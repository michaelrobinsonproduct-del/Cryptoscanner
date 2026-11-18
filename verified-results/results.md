# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T13:50:09.581619+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44317667858
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 1db961a5a81d59c6849044982be8eaecef5cb059 (atomic ledger/results publication)
**Ledger generation:** 581 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04673 | 69.704 | 73.979 | +4.10% | +0.75% | 0.20x | 6.4 | 2026-11-18T13:50:03.189036+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | VVV/USD | 21.251 | 65.577 | 55.101 | +1.07% | -0.90% | 3.77x | 1.4 | 2026-11-18T13:50:03.189036+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 3 | TRX/USD | 0.309609 | 53.858 | 45.224 | +0.55% | -0.01% | 1.87x | 0.9 | 2026-11-18T13:50:03.189036+00:00 | Not calibrated | MODERATE 47/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XRP/USD | 0.98743 | 51.253 | 58.440 | +0.50% | +0.04% | 0.26x | 0.1 | 2026-11-18T13:50:03.189036+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | CAP/USD | 0.101921 | 50.715 | 34.811 | +0.94% | +0.18% | 4.60x | 6.1 | 2026-11-18T13:50:03.189036+00:00 | Not calibrated | STRONG 70/100 | HIGH 67/100 | Watch | WATCH |
| 6 | SENT/USD | 0.019238 | 47.167 | 45.607 | +3.05% | -0.24% | 1.28x | 13.5 | 2026-11-18T13:50:03.189036+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.5222 | 44.467 | 49.283 | +2.53% | -0.29% | 0.66x | 1.9 | 2026-11-18T13:50:03.189036+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 8 | ME/USD | 0.04 | 42.936 | 44.359 | +3.63% | +0.25% | 0.73x | 25.0 | 2026-11-18T13:50:03.189036+00:00 | Not calibrated | WEAK 41/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | USELESS/USD | 0.0997 | 35.952 | 48.973 | +2.17% | -1.15% | 0.27x | 16.1 | 2026-11-18T13:50:03.189036+00:00 | Not calibrated | WEAK 18/100 | EXTREME 86/100 | Do nothing | WATCH |
| 10 | W/USD | 0.00906 | 35.573 | 36.385 | +1.46% | -0.33% | 1.08x | 11.1 | 2026-11-18T13:50:03.189036+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 11 | CC/USD | 0.08313 | 31.896 | 40.955 | +1.22% | -0.42% | 0.30x | 6.0 | 2026-11-18T13:50:03.189036+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 12 | PEARL/USD | 1.8216 | 28.465 | 35.097 | +0.61% | -0.82% | 0.75x | 14.8 | 2026-11-18T13:50:03.189036+00:00 | Not calibrated | WEAK 14/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 73.979 | 0.04673 | +0.75% | 0.20x |
| 2 | XRP/USD | 58.440 | 0.98743 | +0.04% | 0.26x |
| 3 | VVV/USD | 55.101 | 21.251 | -0.90% | 3.77x |
| 4 | AKT/USD | 49.283 | 0.5222 | -0.29% | 0.66x |
| 5 | USELESS/USD | 48.973 | 0.0997 | -1.15% | 0.27x |
| 6 | SENT/USD | 45.607 | 0.019238 | -0.24% | 1.28x |
| 7 | TRX/USD | 45.224 | 0.309609 | -0.01% | 1.87x |
| 8 | ME/USD | 44.359 | 0.04 | +0.25% | 0.73x |
| 9 | CC/USD | 40.955 | 0.08313 | -0.42% | 0.30x |
| 10 | W/USD | 36.385 | 0.00906 | -0.33% | 1.08x |
| 11 | PEARL/USD | 35.097 | 1.8216 | -0.82% | 0.75x |
| 12 | CAP/USD | 34.811 | 0.101921 | +0.18% | 4.60x |

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

- Persisted scans: 581; predictions: 4927; observations: 350836.
- Matured sampled outcomes across 1/6/24/48h: 4226; gap abstentions: 13081. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44317667858 · **Generation:** 581 · **Legacy run:** 44317667858
**Main quote time:** 2026-11-18T13:50:09.581619+00:00 · **Legacy report time:** 2026-11-18T13:50:35.326525+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04673 | 69.70 | +0.75% | 0.20x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 2 | VVV/USD | 21.251 | 65.58 | -0.90% | 3.77x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 3 | TRX/USD | 0.309609 | 53.86 | -0.01% | 1.87x | MODERATE 47/100 | HIGH 61/100 | Watch |
| 4 | XRP/USD | 0.98743 | 51.25 | +0.04% | 0.26x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 5 | CAP/USD | 0.101921 | 50.72 | +0.18% | 4.60x | STRONG 70/100 | HIGH 67/100 | Watch |
| 6 | SENT/USD | 0.019238 | 47.17 | -0.24% | 1.28x | WEAK 29/100 | VERY_HIGH 79/100 | Do nothing |
| 7 | AKT/USD | 0.5222 | 44.47 | -0.29% | 0.66x | WEAK 27/100 | VERY_HIGH 81/100 | Do nothing |
| 8 | ME/USD | 0.04 | 42.94 | +0.25% | 0.73x | WEAK 41/100 | EXTREME 94/100 | Do nothing |
| 9 | USELESS/USD | 0.0997 | 35.95 | -1.15% | 0.27x | WEAK 18/100 | EXTREME 86/100 | Do nothing |
| 10 | W/USD | 0.00906 | 35.57 | -0.33% | 1.08x | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing |
| 11 | CC/USD | 0.08313 | 31.90 | -0.42% | 0.30x | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing |
| 12 | PEARL/USD | 1.8216 | 28.46 | -0.82% | 0.75x | WEAK 14/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
