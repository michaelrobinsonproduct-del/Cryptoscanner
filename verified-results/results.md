# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T21:31:23.464940+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45898492432
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** dea9abe9fbda048d87fd81c7baa1bd1afe8e894c (atomic ledger/results publication)
**Ledger generation:** 1916 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.38963 | 92.437 | 76.678 | +8.90% | +0.15% | 2.55x | 11.6 | 2026-11-26T21:31:14.839172+00:00 | Not calibrated | STRONG 86/100 | HIGH 61/100 | Watch | WATCH |
| 2 | LINK/USD | 9.35404 | 90.420 | 74.990 | +3.42% | +0.09% | 14.39x | 1.8 | 2026-11-26T21:31:14.839172+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 3 | LTC/USD | 44.02 | 89.426 | 75.334 | +3.07% | -0.18% | 5.19x | 2.3 | 2026-11-26T21:31:14.839172+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ADA/USD | 0.150615 | 86.863 | 76.673 | +3.32% | -0.18% | 2.11x | 3.2 | 2026-11-26T21:31:14.839172+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ETH/USD | 1704.42 | 75.898 | 60.772 | +0.83% | +0.03% | 2.51x | 0.1 | 2026-11-26T21:31:14.839172+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XRP/USD | 0.95256 | 69.143 | 66.906 | +1.71% | +0.08% | 1.18x | 0.1 | 2026-11-26T21:31:14.839172+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 7 | HBAR/USD | 0.05497 | 67.275 | 71.738 | +5.51% | -0.22% | 0.66x | 3.6 | 2026-11-26T21:31:14.839172+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | XBT/USD | 60857.3 | 67.254 | 60.658 | +0.81% | +0.16% | 1.58x | 0.0 | 2026-11-26T21:31:14.839172+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 9 | HYPE/USD | 63.32 | 64.527 | 72.733 | +2.76% | -0.11% | 0.23x | 3.2 | 2026-11-26T21:31:14.839172+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | SOL/USD | 71.5 | 64.515 | 65.339 | +1.58% | +0.04% | 0.90x | 1.4 | 2026-11-26T21:31:14.839172+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 11 | INJ/USD | 6.264 | 64.491 | 72.114 | +5.21% | -0.46% | 0.47x | 8.0 | 2026-11-26T21:31:14.839172+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0569156 | 60.046 | 54.781 | +1.71% | -0.04% | 1.55x | 0.1 | 2026-11-26T21:31:14.839172+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 76.678 | 0.38963 | +0.15% | 2.55x |
| 2 | ADA/USD | 76.673 | 0.150615 | -0.18% | 2.11x |
| 3 | LTC/USD | 75.334 | 44.02 | -0.18% | 5.19x |
| 4 | LINK/USD | 74.990 | 9.35404 | +0.09% | 14.39x |
| 5 | HYPE/USD | 72.733 | 63.32 | -0.11% | 0.23x |
| 6 | INJ/USD | 72.114 | 6.264 | -0.46% | 0.47x |
| 7 | HBAR/USD | 71.738 | 0.05497 | -0.22% | 0.66x |
| 8 | XRP/USD | 66.906 | 0.95256 | +0.08% | 1.18x |
| 9 | SOL/USD | 65.339 | 71.5 | +0.04% | 0.90x |
| 10 | ETH/USD | 60.772 | 1704.42 | +0.03% | 2.51x |
| 11 | XBT/USD | 60.658 | 60857.3 | +0.16% | 1.58x |
| 12 | XDG/USD | 54.781 | 0.0569156 | -0.04% | 1.55x |

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

- Persisted scans: 1916; predictions: 16727; observations: 1160618.
- Matured sampled outcomes across 1/6/24/48h: 36368; gap abstentions: 25274. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45898492432 · **Generation:** 1916 · **Legacy run:** 45898492432
**Main quote time:** 2026-11-26T21:31:23.464940+00:00 · **Legacy report time:** 2026-11-26T21:32:09.643270+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.38963 | 92.44 | +0.15% | 2.55x | STRONG 96/100 | HIGH 61/100 | Watch |
| 2 | LINK/USD ⭐ | 9.35404 | 90.42 | +0.09% | 14.39x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | LTC/USD | 44.02 | 89.43 | -0.18% | 5.19x | STRONG 75/100 | HIGH 61/100 | Watch |
| 4 | ADA/USD | 0.150615 | 86.86 | -0.18% | 2.11x | STRONG 73/100 | HIGH 61/100 | Watch |
| 5 | ETH/USD | 1704.42 | 75.90 | +0.03% | 2.51x | STRONG 83/100 | HIGH 55/100 | Watch |
| 6 | XRP/USD | 0.95256 | 69.14 | +0.08% | 1.18x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 7 | HBAR/USD | 0.05497 | 67.28 | -0.22% | 0.66x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |
| 8 | XBT/USD | 60857.3 | 67.25 | +0.16% | 1.58x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 9 | HYPE/USD | 63.32 | 64.53 | -0.11% | 0.23x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 10 | SOL/USD | 71.5 | 64.51 | +0.04% | 0.90x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 11 | INJ/USD | 6.264 | 64.49 | -0.46% | 0.47x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 12 | XDG/USD | 0.0569156 | 60.05 | -0.04% | 1.55x | MODERATE 50/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.35854 | 95.07 | +0.09% | 14.39x | 6603 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | DRV/USD ⭐ | 0.38963 | 81.13 | +0.15% | 2.55x | 8054 | STRONG 91/100 | HIGH 61/100 | Watch |

**Same-run overlap:** DRV/USD, LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
