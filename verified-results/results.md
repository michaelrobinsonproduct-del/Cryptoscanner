# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T12:01:42.112419+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45389240247
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e8ecd9ed453eb4da6d02904106d0e15c6ec1b4bb (atomic ledger/results publication)
**Ledger generation:** 1571 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 25.955 | 90.508 | 91.976 | +6.16% | +1.13% | 0.29x | 12.3 | 2026-11-24T12:01:34.206485+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | MON/USD | 0.01264 | 72.478 | 78.898 | +9.72% | -0.39% | 0.55x | 15.9 | 2026-11-24T12:01:34.206485+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | XMR/USD | 499.78 | 66.635 | 70.305 | +2.83% | +0.33% | 0.47x | 9.0 | 2026-11-24T12:01:34.206485+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.3297 | 64.900 | 59.450 | +6.66% | +0.00% | 1.54x | 36.6 | 2026-11-24T12:01:34.206485+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | PEPE/USD | 3.48e-06 | 61.921 | 61.842 | +1.69% | +0.61% | 0.70x | 2.9 | 2026-11-24T12:01:34.206485+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | GBP/USD | 1.30845 | 56.365 | 57.640 | +0.40% | +0.05% | 0.85x | 0.3 | 2026-11-24T12:01:34.206485+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.0486 | 44.109 | 50.064 | +0.93% | +0.41% | 0.20x | 10.3 | 2026-11-24T12:01:34.206485+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | BAT/USD | 0.0779 | 33.943 | 35.834 | +0.95% | +0.37% | 0.62x | 6.4 | 2026-11-24T12:01:34.206485+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | BABY/USD | 0.00855 | 26.180 | 25.083 | +0.59% | -0.58% | 1.40x | 23.4 | 2026-11-24T12:01:34.206485+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 10 | KAVA/USD | 0.0243 | 24.753 | 13.123 | +0.41% | +0.83% | 1.75x | 41.3 | 2026-11-24T12:01:34.206485+00:00 | Not calibrated | WEAK 42/100 | EXTREME 89/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 91.976 | 25.955 | +1.13% | 0.29x |
| 2 | MON/USD | 78.898 | 0.01264 | -0.39% | 0.55x |
| 3 | XMR/USD | 70.305 | 499.78 | +0.33% | 0.47x |
| 4 | PEPE/USD | 61.842 | 3.48e-06 | +0.61% | 0.70x |
| 5 | ICNT/USD | 59.450 | 0.3297 | +0.00% | 1.54x |
| 6 | GBP/USD | 57.640 | 1.30845 | +0.05% | 0.85x |
| 7 | NIGHT/USD | 50.064 | 0.0486 | +0.41% | 0.20x |
| 8 | BAT/USD | 35.834 | 0.0779 | +0.37% | 0.62x |
| 9 | BABY/USD | 25.083 | 0.00855 | -0.58% | 1.40x |
| 10 | KAVA/USD | 13.123 | 0.0243 | +0.83% | 1.75x |

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

- Persisted scans: 1571; predictions: 13549; observations: 951837.
- Matured sampled outcomes across 1/6/24/48h: 26187; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45389240247 · **Generation:** 1571 · **Legacy run:** 45389240247
**Main quote time:** 2026-11-24T12:01:42.112419+00:00 · **Legacy report time:** 2026-11-24T12:02:28.699717+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 25.955 | 90.51 | +1.13% | 0.29x | STRONG 70/100 | VERY_HIGH 76/100 | Watch |
| 2 | MON/USD | 0.01264 | 72.48 | -0.39% | 0.55x | WEAK 36/100 | VERY_HIGH 82/100 | Watch |
| 3 | XMR/USD | 499.78 | 66.63 | +0.33% | 0.47x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 4 | ICNT/USD | 0.3297 | 64.90 | +0.00% | 1.54x | MODERATE 52/100 | VERY_HIGH 72/100 | Watch |
| 5 | PEPE/USD | 3.48e-06 | 61.92 | +0.61% | 0.70x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 6 | GBP/USD | 1.30845 | 56.36 | +0.05% | 0.85x | MODERATE 48/100 | HIGH 62/100 | Watch |
| 7 | NIGHT/USD | 0.0486 | 44.11 | +0.41% | 0.20x | MODERATE 47/100 | VERY_HIGH 76/100 | Watch |
| 8 | BAT/USD | 0.0779 | 33.94 | +0.37% | 0.62x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |
| 9 | BABY/USD | 0.00855 | 26.18 | -0.58% | 1.40x | WEAK 23/100 | VERY_HIGH 78/100 | Do nothing |
| 10 | KAVA/USD | 0.0243 | 24.75 | +0.83% | 1.75x | WEAK 42/100 | EXTREME 89/100 | Do nothing |

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
