# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T21:42:01.657174+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45493312642
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 56211f7274685d482d851b407b6adc67cad09220 (atomic ledger/results publication)
**Ledger generation:** 1629 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 501.59 | 78.983 | 75.331 | +3.20% | +0.28% | 1.22x | 4.2 | 2026-11-24T21:41:57.450932+00:00 | Not calibrated | STRONG 74/100 | HIGH 62/100 | Watch | WATCH |
| 2 | LUNA/USD | 4.593e-05 | 65.160 | 70.371 | +5.66% | -0.28% | 0.62x | 2.2 | 2026-11-24T21:41:57.450932+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 3 | GBP/USD | 1.31088 | 58.468 | 59.060 | +0.59% | -0.00% | 0.94x | 0.1 | 2026-11-24T21:41:57.450932+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 4 | PEPE/USD | 3.477e-06 | 51.663 | 52.795 | +1.61% | -0.26% | 1.02x | 5.8 | 2026-11-24T21:41:57.450932+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 5 | SKY/USD | 0.04064 | 48.412 | 34.319 | +0.62% | +0.32% | 2.25x | 7.4 | 2026-11-24T21:41:57.450932+00:00 | Not calibrated | STRONG 79/100 | HIGH 60/100 | Watch | WATCH |
| 6 | REKT/USD | 7.85e-08 | 46.141 | 30.495 | +0.26% | +0.13% | 3.11x | 12.7 | 2026-11-24T21:41:57.450932+00:00 | Not calibrated | MODERATE 63/100 | HIGH 66/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.04841 | 38.067 | 43.051 | +0.54% | +0.23% | 0.39x | 2.1 | 2026-11-24T21:41:57.450932+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 75.331 | 501.59 | +0.28% | 1.22x |
| 2 | LUNA/USD | 70.371 | 4.593e-05 | -0.28% | 0.62x |
| 3 | GBP/USD | 59.060 | 1.31088 | -0.00% | 0.94x |
| 4 | PEPE/USD | 52.795 | 3.477e-06 | -0.26% | 1.02x |
| 5 | NIGHT/USD | 43.051 | 0.04841 | +0.23% | 0.39x |
| 6 | SKY/USD | 34.319 | 0.04064 | +0.32% | 2.25x |
| 7 | REKT/USD | 30.495 | 7.85e-08 | +0.13% | 3.11x |

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

- Persisted scans: 1629; predictions: 13962; observations: 987152.
- Matured sampled outcomes across 1/6/24/48h: 28670; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45493312642 · **Generation:** 1629 · **Legacy run:** 45493312642
**Main quote time:** 2026-11-24T21:42:01.657174+00:00 · **Legacy report time:** 2026-11-24T21:43:01.849793+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 501.59 | 78.98 | +0.28% | 1.22x | STRONG 84/100 | HIGH 62/100 | Watch |
| 2 | LUNA/USD | 4.593e-05 | 65.16 | -0.28% | 0.62x | WEAK 38/100 | VERY_HIGH 81/100 | Watch |
| 3 | GBP/USD | 1.31088 | 58.47 | -0.00% | 0.94x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 4 | PEPE/USD | 3.477e-06 | 51.66 | -0.26% | 1.02x | WEAK 36/100 | HIGH 68/100 | Watch |
| 5 | SKY/USD ⭐ | 0.04064 | 48.41 | +0.32% | 2.25x | STRONG 89/100 | HIGH 60/100 | Consider small entry |
| 6 | REKT/USD ⭐ | 7.85e-08 | 46.14 | +0.13% | 3.11x | STRONG 73/100 | HIGH 66/100 | Watch |
| 7 | NIGHT/USD | 0.04841 | 38.07 | +0.23% | 0.39x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 501.63 | 82.31 | +0.28% | 1.22x | 7766 | STRONG 86/100 | HIGH 62/100 | Watch |
| 2 | REKT/USD ⭐ | 7.91e-08 | 45.73 | +0.13% | 3.11x | 11740 | MODERATE 63/100 | VERY_HIGH 72/100 | Watch |
| 3 | SKY/USD ⭐ | 0.04058 | 36.02 | +0.32% | 2.25x | 4345 | STRONG 83/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** XMR/USD, SKY/USD, REKT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
