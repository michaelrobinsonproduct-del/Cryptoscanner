# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T22:42:14.227594+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45281772306
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** dc4b9ae3a0b5622215057bf4792c492115af737d (atomic ledger/results publication)
**Ledger generation:** 1491 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 156.13 | 89.495 | 97.116 | +8.85% | -0.20% | 0.34x | 5.8 | 2026-11-23T22:42:07.449434+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | ALGO/USD | 0.08101 | 86.062 | 91.147 | +7.40% | -0.47% | 0.73x | 7.4 | 2026-11-23T22:42:07.449434+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | SHX/USD | 0.003607 | 82.787 | 73.569 | +6.87% | -0.08% | 1.96x | 5.6 | 2026-11-23T22:42:07.449434+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | CAP/USD | 0.101428 | 77.097 | 76.128 | +8.40% | +0.46% | 0.87x | 6.1 | 2026-11-23T22:42:07.449434+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0561188 | 76.449 | 65.296 | +1.51% | -0.77% | 4.84x | 0.6 | 2026-11-23T22:42:07.449434+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 6 | ATOM/USD | 1.2501 | 72.870 | 74.463 | +6.66% | +0.01% | 0.84x | 7.2 | 2026-11-23T22:42:07.449434+00:00 | Not calibrated | MODERATE 56/100 | HIGH 67/100 | Watch | WATCH |
| 7 | LTC/USD | 41.13 | 71.981 | 70.691 | +2.42% | -0.41% | 1.33x | 2.4 | 2026-11-23T22:42:07.449434+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 8 | INJ/USD | 6.251 | 65.692 | 52.762 | +0.37% | -0.41% | 10.29x | 6.4 | 2026-11-23T22:42:07.449434+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 9 | PAXG/USD | 3624.7 | 61.765 | 60.700 | +1.47% | -0.03% | 1.12x | 1.5 | 2026-11-23T22:42:07.449434+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 10 | XRP/USD | 0.93582 | 61.388 | 61.195 | +0.89% | -0.60% | 1.32x | 0.1 | 2026-11-23T22:42:07.449434+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 11 | SOL/USD | 72.07 | 60.208 | 68.577 | +2.04% | -0.50% | 0.41x | 1.4 | 2026-11-23T22:42:07.449434+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | CC/USD | 0.07687 | 57.864 | 67.454 | +4.91% | -0.56% | 0.32x | 6.5 | 2026-11-23T22:42:07.449434+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 97.116 | 156.13 | -0.20% | 0.34x |
| 2 | ALGO/USD | 91.147 | 0.08101 | -0.47% | 0.73x |
| 3 | CAP/USD | 76.128 | 0.101428 | +0.46% | 0.87x |
| 4 | ATOM/USD | 74.463 | 1.2501 | +0.01% | 0.84x |
| 5 | SHX/USD | 73.569 | 0.003607 | -0.08% | 1.96x |
| 6 | LTC/USD | 70.691 | 41.13 | -0.41% | 1.33x |
| 7 | SOL/USD | 68.577 | 72.07 | -0.50% | 0.41x |
| 8 | CC/USD | 67.454 | 0.07687 | -0.56% | 0.32x |
| 9 | XDG/USD | 65.296 | 0.0561188 | -0.77% | 4.84x |
| 10 | XRP/USD | 61.195 | 0.93582 | -0.60% | 1.32x |
| 11 | PAXG/USD | 60.700 | 3624.7 | -0.03% | 1.12x |
| 12 | INJ/USD | 52.762 | 6.251 | -0.41% | 10.29x |

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

- Persisted scans: 1491; predictions: 12659; observations: 903121.
- Matured sampled outcomes across 1/6/24/48h: 22924; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45281772306 · **Generation:** 1491 · **Legacy run:** 45281772306
**Main quote time:** 2026-11-23T22:42:14.227594+00:00 · **Legacy report time:** 2026-11-23T22:43:24.596392+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD | 156.13 | 89.49 | -0.20% | 0.34x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |
| 2 | ALGO/USD | 0.08101 | 86.06 | -0.47% | 0.73x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 3 | SHX/USD | 0.003607 | 82.79 | -0.08% | 1.96x | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 4 | CAP/USD | 0.101428 | 77.10 | +0.46% | 0.87x | MODERATE 69/100 | HIGH 67/100 | Watch |
| 5 | XDG/USD | 0.0561188 | 76.45 | -0.77% | 4.84x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 6 | ATOM/USD | 1.2501 | 72.87 | +0.01% | 0.84x | MODERATE 56/100 | HIGH 67/100 | Watch |
| 7 | LTC/USD | 41.13 | 71.98 | -0.41% | 1.33x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 8 | INJ/USD | 6.251 | 65.69 | -0.41% | 10.29x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 9 | PAXG/USD | 3624.7 | 61.77 | -0.03% | 1.12x | WEAK 41/100 | HIGH 68/100 | Watch |
| 10 | XRP/USD | 0.93582 | 61.39 | -0.60% | 1.32x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 11 | SOL/USD | 72.07 | 60.21 | -0.50% | 0.41x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | CC/USD | 0.07687 | 57.86 | -0.56% | 0.32x | WEAK 34/100 | VERY_HIGH 81/100 | Do nothing |

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
