# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T12:01:41.479091+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45170100386
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 94ba067e8346ecd26f3731a191e06cb43f9f81d3 (atomic ledger/results publication)
**Ledger generation:** 1427 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 154.55 | 81.072 | 89.399 | +7.75% | -0.97% | 0.65x | 6.5 | 2026-11-23T12:01:34.865822+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | ALGO/USD | 0.08331 | 80.266 | 76.502 | +10.45% | +0.97% | 0.89x | 7.2 | 2026-11-23T12:01:34.865822+00:00 | Not calibrated | STRONG 70/100 | HIGH 67/100 | Watch | WATCH |
| 3 | XMR/USD | 502.96 | 79.456 | 64.635 | +1.87% | -0.04% | 4.22x | 7.0 | 2026-11-23T12:01:34.865822+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6715 | 76.406 | 71.123 | +2.41% | -0.28% | 1.67x | 1.5 | 2026-11-23T12:01:34.865822+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SOL/USD | 72.42 | 69.705 | 72.050 | +2.53% | -0.32% | 0.92x | 1.4 | 2026-11-23T12:01:34.865822+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XRP/USD | 0.94029 | 61.180 | 64.303 | +1.37% | -0.04% | 0.71x | 0.6 | 2026-11-23T12:01:34.865822+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | HYPE/USD | 64 | 60.599 | 63.872 | +1.49% | +0.00% | 0.67x | 3.1 | 2026-11-23T12:01:34.865822+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | PENGU/USD | 0.00436 | 60.204 | 47.032 | +2.25% | -0.37% | 2.57x | 2.3 | 2026-11-23T12:01:34.865822+00:00 | Not calibrated | MODERATE 60/100 | HIGH 66/100 | Watch | WATCH |
| 9 | PAXG/USD | 3607.69 | 59.579 | 51.526 | +0.99% | -0.09% | 1.85x | 0.8 | 2026-11-23T12:01:34.865822+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 10 | CC/USD | 0.07628 | 56.563 | 61.666 | +4.11% | -0.18% | 0.58x | 3.9 | 2026-11-23T12:01:34.865822+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 11 | UAI/USD | 0.03111 | 56.404 | 60.787 | +5.21% | +0.32% | 0.40x | 12.9 | 2026-11-23T12:01:34.865822+00:00 | Not calibrated | MODERATE 53/100 | EXTREME 88/100 | Do nothing | WATCH |
| 12 | XLM/USD | 0.128856 | 55.910 | 60.008 | +1.04% | -0.17% | 0.67x | 1.7 | 2026-11-23T12:01:34.865822+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 89.399 | 154.55 | -0.97% | 0.65x |
| 2 | ALGO/USD | 76.502 | 0.08331 | +0.97% | 0.89x |
| 3 | SOL/USD | 72.050 | 72.42 | -0.32% | 0.92x |
| 4 | SUI/USD | 71.123 | 0.6715 | -0.28% | 1.67x |
| 5 | XMR/USD | 64.635 | 502.96 | -0.04% | 4.22x |
| 6 | XRP/USD | 64.303 | 0.94029 | -0.04% | 0.71x |
| 7 | HYPE/USD | 63.872 | 64 | +0.00% | 0.67x |
| 8 | CC/USD | 61.666 | 0.07628 | -0.18% | 0.58x |
| 9 | UAI/USD | 60.787 | 0.03111 | +0.32% | 0.40x |
| 10 | XLM/USD | 60.008 | 0.128856 | -0.17% | 0.67x |
| 11 | PAXG/USD | 51.526 | 3607.69 | -0.09% | 1.85x |
| 12 | PENGU/USD | 47.032 | 0.00436 | -0.37% | 2.57x |

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

- Persisted scans: 1427; predictions: 11891; observations: 864146.
- Matured sampled outcomes across 1/6/24/48h: 19798; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45170100386 · **Generation:** 1427 · **Legacy run:** 45170100386
**Main quote time:** 2026-11-23T12:01:41.479091+00:00 · **Legacy report time:** 2026-11-23T12:02:48.099951+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 154.55 | 81.07 | -0.97% | 0.65x | MODERATE 46/100 | VERY_HIGH 76/100 | Watch |
| 2 | ALGO/USD | 0.08331 | 80.27 | +0.97% | 0.89x | STRONG 70/100 | HIGH 67/100 | Watch |
| 3 | XMR/USD | 502.96 | 79.46 | -0.04% | 4.22x | STRONG 70/100 | HIGH 61/100 | Watch |
| 4 | SUI/USD | 0.6715 | 76.41 | -0.28% | 1.67x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 5 | SOL/USD | 72.42 | 69.70 | -0.32% | 0.92x | WEAK 40/100 | HIGH 68/100 | Watch |
| 6 | XRP/USD | 0.94029 | 61.18 | -0.04% | 0.71x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 7 | HYPE/USD | 64 | 60.60 | +0.00% | 0.67x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 8 | PENGU/USD | 0.00436 | 60.20 | -0.37% | 2.57x | MODERATE 60/100 | HIGH 66/100 | Watch |
| 9 | PAXG/USD | 3607.69 | 59.58 | -0.09% | 1.85x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 10 | CC/USD | 0.07628 | 56.56 | -0.18% | 0.58x | WEAK 33/100 | VERY_HIGH 81/100 | Do nothing |
| 11 | UAI/USD | 0.03111 | 56.40 | +0.32% | 0.40x | MODERATE 53/100 | EXTREME 88/100 | Do nothing |
| 12 | XLM/USD | 0.128856 | 55.91 | -0.17% | 0.67x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 6.423 | 70.91 | +1.00% | 1.51x | 4417 | STRONG 75/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
