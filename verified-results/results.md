# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T20:31:51.892150+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45259910040
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2d4b7730e3618a7067c541554377718ec8d6db85 (atomic ledger/results publication)
**Ledger generation:** 1478 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ALGO/USD | 0.08308 | 105.543 | 91.024 | +10.14% | -0.10% | 2.57x | 7.2 | 2026-11-23T20:31:43.921949+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | QNT/USD | 158.62 | 86.739 | 94.326 | +10.58% | -0.16% | 0.32x | 11.3 | 2026-11-23T20:31:43.921949+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | UNI/USD | 4.8644 | 80.641 | 75.672 | +3.91% | -0.51% | 1.75x | 7.6 | 2026-11-23T20:31:43.921949+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 4 | INJ/USD | 6.514 | 77.427 | 82.395 | +4.59% | -0.14% | 0.57x | 6.2 | 2026-11-23T20:31:43.921949+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | ATOM/USD | 1.2732 | 76.482 | 72.124 | +8.63% | +0.83% | 1.02x | 11.8 | 2026-11-23T20:31:43.921949+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0567652 | 72.834 | 73.564 | +2.68% | -0.03% | 0.94x | 0.4 | 2026-11-23T20:31:43.921949+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 7 | SOL/USD | 72.99 | 72.091 | 77.704 | +3.34% | -0.14% | 0.51x | 1.4 | 2026-11-23T20:31:43.921949+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | LTC/USD | 41.44 | 68.864 | 74.897 | +3.19% | -0.29% | 0.54x | 4.8 | 2026-11-23T20:31:43.921949+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6769 | 68.206 | 76.154 | +3.23% | -0.31% | 0.36x | 3.0 | 2026-11-23T20:31:43.921949+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | CC/USD | 0.07778 | 67.942 | 77.057 | +6.16% | -0.13% | 0.15x | 5.1 | 2026-11-23T20:31:43.921949+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 11 | HYPE/USD | 64.39 | 61.121 | 68.987 | +2.11% | -0.59% | 0.51x | 1.6 | 2026-11-23T20:31:43.921949+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | HBAR/USD | 0.05291 | 61.073 | 54.638 | +2.54% | -0.28% | 1.78x | 1.9 | 2026-11-23T20:31:43.921949+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 94.326 | 158.62 | -0.16% | 0.32x |
| 2 | ALGO/USD | 91.024 | 0.08308 | -0.10% | 2.57x |
| 3 | INJ/USD | 82.395 | 6.514 | -0.14% | 0.57x |
| 4 | SOL/USD | 77.704 | 72.99 | -0.14% | 0.51x |
| 5 | CC/USD | 77.057 | 0.07778 | -0.13% | 0.15x |
| 6 | SUI/USD | 76.154 | 0.6769 | -0.31% | 0.36x |
| 7 | UNI/USD | 75.672 | 4.8644 | -0.51% | 1.75x |
| 8 | LTC/USD | 74.897 | 41.44 | -0.29% | 0.54x |
| 9 | XDG/USD | 73.564 | 0.0567652 | -0.03% | 0.94x |
| 10 | ATOM/USD | 72.124 | 1.2732 | +0.83% | 1.02x |
| 11 | HYPE/USD | 68.987 | 64.39 | -0.59% | 0.51x |
| 12 | HBAR/USD | 54.638 | 0.05291 | -0.28% | 1.78x |

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

- Persisted scans: 1478; predictions: 12503; observations: 895204.
- Matured sampled outcomes across 1/6/24/48h: 22288; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45259910040 · **Generation:** 1478 · **Legacy run:** 45259910040
**Main quote time:** 2026-11-23T20:31:51.892150+00:00 · **Legacy report time:** 2026-11-23T20:33:00.555001+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD | 0.08308 | 105.54 | -0.10% | 2.57x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | QNT/USD | 158.62 | 86.74 | -0.16% | 0.32x | WEAK 43/100 | VERY_HIGH 82/100 | Watch |
| 3 | UNI/USD | 4.8644 | 80.64 | -0.51% | 1.75x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 4 | INJ/USD | 6.514 | 77.43 | -0.14% | 0.57x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 5 | ATOM/USD ⭐ | 1.2732 | 76.48 | +0.83% | 1.02x | STRONG 78/100 | VERY_HIGH 73/100 | Watch |
| 6 | XDG/USD | 0.0567652 | 72.83 | -0.03% | 0.94x | WEAK 41/100 | HIGH 68/100 | Watch |
| 7 | SOL/USD | 72.99 | 72.09 | -0.14% | 0.51x | WEAK 41/100 | VERY_HIGH 76/100 | Watch |
| 8 | LTC/USD | 41.44 | 68.86 | -0.29% | 0.54x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 9 | SUI/USD | 0.6769 | 68.21 | -0.31% | 0.36x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 10 | CC/USD | 0.07778 | 67.94 | -0.13% | 0.15x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |
| 11 | HYPE/USD | 64.39 | 61.12 | -0.59% | 0.51x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 12 | HBAR/USD | 0.05291 | 61.07 | -0.28% | 1.78x | MODERATE 51/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ATOM/USD ⭐ | 1.2719 | 74.40 | +0.83% | 1.02x | 3496 | STRONG 77/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** ATOM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
