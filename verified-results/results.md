# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T21:21:57.404580+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45268496615
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** a4ec820109a6e7f7397b3231fd1bcd5dfe9f9b9a (atomic ledger/results publication)
**Ledger generation:** 1483 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ALGO/USD | 0.08139 | 103.234 | 91.288 | +7.90% | -0.61% | 7.11x | 7.4 | 2026-11-23T21:21:48.393222+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | QNT/USD | 157.28 | 96.184 | 97.139 | +9.65% | -0.52% | 1.16x | 5.7 | 2026-11-23T21:21:48.393222+00:00 | Not calibrated | MODERATE 58/100 | HIGH 68/100 | Watch | WATCH |
| 3 | CC/USD | 0.07719 | 83.146 | 70.658 | +5.35% | -0.50% | 3.70x | 6.5 | 2026-11-23T21:21:48.393222+00:00 | Not calibrated | STRONG 72/100 | HIGH 66/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0564863 | 82.177 | 69.659 | +2.18% | -0.34% | 2.42x | 1.1 | 2026-11-23T21:21:48.393222+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 5 | UNI/USD | 4.8219 | 79.265 | 70.705 | +3.01% | -0.73% | 2.22x | 5.6 | 2026-11-23T21:21:48.393222+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 6 | WINGS/USD | 0.002055 | 78.292 | 74.805 | +7.65% | +0.15% | 1.28x | 4.8 | 2026-11-23T21:21:48.393222+00:00 | Not calibrated | MODERATE 64/100 | HIGH 60/100 | Watch | WATCH |
| 7 | LTC/USD | 41.15 | 78.030 | 69.825 | +2.47% | -0.36% | 2.00x | 4.9 | 2026-11-23T21:21:48.393222+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6714 | 72.733 | 70.273 | +2.39% | -0.31% | 1.40x | 3.0 | 2026-11-23T21:21:48.393222+00:00 | Not calibrated | MODERATE 56/100 | HIGH 61/100 | Watch | WATCH |
| 9 | SOL/USD | 72.43 | 68.489 | 71.459 | +2.55% | -0.17% | 0.79x | 2.8 | 2026-11-23T21:21:48.393222+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 10 | CAP/USD | 0.103939 | 68.283 | 76.095 | +11.08% | -1.52% | 0.98x | 6.1 | 2026-11-23T21:21:48.393222+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 11 | INJ/USD | 6.421 | 65.953 | 72.957 | +3.10% | -0.51% | 0.56x | 3.1 | 2026-11-23T21:21:48.393222+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | ATOM/USD | 1.2695 | 63.285 | 71.757 | +8.32% | -0.17% | 0.24x | 12.6 | 2026-11-23T21:21:48.393222+00:00 | Not calibrated | WEAK 32/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 97.139 | 157.28 | -0.52% | 1.16x |
| 2 | ALGO/USD | 91.288 | 0.08139 | -0.61% | 7.11x |
| 3 | CAP/USD | 76.095 | 0.103939 | -1.52% | 0.98x |
| 4 | WINGS/USD | 74.805 | 0.002055 | +0.15% | 1.28x |
| 5 | INJ/USD | 72.957 | 6.421 | -0.51% | 0.56x |
| 6 | ATOM/USD | 71.757 | 1.2695 | -0.17% | 0.24x |
| 7 | SOL/USD | 71.459 | 72.43 | -0.17% | 0.79x |
| 8 | UNI/USD | 70.705 | 4.8219 | -0.73% | 2.22x |
| 9 | CC/USD | 70.658 | 0.07719 | -0.50% | 3.70x |
| 10 | SUI/USD | 70.273 | 0.6714 | -0.31% | 1.40x |
| 11 | LTC/USD | 69.825 | 41.15 | -0.36% | 2.00x |
| 12 | XDG/USD | 69.659 | 0.0564863 | -0.34% | 2.42x |

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

- Persisted scans: 1483; predictions: 12563; observations: 898249.
- Matured sampled outcomes across 1/6/24/48h: 22528; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45268496615 · **Generation:** 1483 · **Legacy run:** 45268496615
**Main quote time:** 2026-11-23T21:21:57.404580+00:00 · **Legacy report time:** 2026-11-23T21:23:01.097061+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD | 0.08139 | 103.23 | -0.61% | 7.11x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | QNT/USD | 157.28 | 96.18 | -0.52% | 1.16x | MODERATE 58/100 | HIGH 68/100 | Watch |
| 3 | CC/USD | 0.07719 | 83.15 | -0.50% | 3.70x | STRONG 72/100 | HIGH 66/100 | Watch |
| 4 | XDG/USD | 0.0564863 | 82.18 | -0.34% | 2.42x | STRONG 71/100 | HIGH 61/100 | Watch |
| 5 | UNI/USD | 4.8219 | 79.26 | -0.73% | 2.22x | STRONG 70/100 | HIGH 61/100 | Watch |
| 6 | WINGS/USD ⭐ | 0.002055 | 78.29 | +0.15% | 1.28x | STRONG 74/100 | HIGH 60/100 | Watch |
| 7 | LTC/USD | 41.15 | 78.03 | -0.36% | 2.00x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 8 | SUI/USD | 0.6714 | 72.73 | -0.31% | 1.40x | MODERATE 56/100 | HIGH 61/100 | Watch |
| 9 | SOL/USD | 72.43 | 68.49 | -0.17% | 0.79x | WEAK 39/100 | HIGH 68/100 | Watch |
| 10 | CAP/USD | 0.103939 | 68.28 | -1.52% | 0.98x | WEAK 39/100 | VERY_HIGH 77/100 | Do nothing |
| 11 | INJ/USD | 6.421 | 65.95 | -0.51% | 0.56x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 12 | ATOM/USD | 1.2695 | 63.29 | -0.17% | 0.24x | WEAK 32/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | KAS/USD | 0.02718 | 81.67 | +0.07% | 2.82x | 4214 | STRONG 81/100 | HIGH 61/100 | Watch |
| 2 | WINGS/USD ⭐ | 0.002055 | 78.20 | +0.15% | 1.28x | 6024 | STRONG 74/100 | HIGH 60/100 | Watch |

**Same-run overlap:** WINGS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
