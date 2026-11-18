# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T04:05:13.991010+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44234780748
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** d6fa7f0d099d02647c9e0476ba7805ce03251423 (atomic ledger/results publication)
**Ledger generation:** 526 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CC/USD | 0.08446 | 69.850 | 51.152 | +2.84% | +0.74% | 4.38x | 8.3 | 2026-11-18T04:05:08.691313+00:00 | Not calibrated | STRONG 90/100 | HIGH 60/100 | Watch | WATCH |
| 2 | XDC/USD | 0.03071 | 58.365 | 40.087 | +1.29% | +0.66% | 18.69x | 13.0 | 2026-11-18T04:05:08.691313+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04533 | 56.236 | 44.732 | +0.98% | +1.39% | 1.46x | 17.7 | 2026-11-18T04:05:08.691313+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ZAMA/USD | 0.06116 | 55.887 | 42.111 | +2.05% | -0.13% | 2.44x | 11.5 | 2026-11-18T04:05:08.691313+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | AKT/USD | 0.5173 | 42.649 | 41.426 | +1.57% | -0.04% | 1.14x | 3.9 | 2026-11-18T04:05:08.691313+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 6 | MELANIA/USD | 0.0509 | 36.470 | 42.596 | +4.52% | -0.39% | 0.58x | 39.4 | 2026-11-18T04:05:08.691313+00:00 | Not calibrated | WEAK 8/100 | EXTREME 100/100 | Do nothing | WATCH |
| 7 | PEARL/USD | 1.8373 | 36.358 | 37.372 | +1.48% | +0.40% | 0.70x | 16.3 | 2026-11-18T04:05:08.691313+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 8 | SENT/USD | 0.019039 | 35.071 | 37.952 | +1.98% | +0.34% | 0.54x | 13.7 | 2026-11-18T04:05:08.691313+00:00 | Not calibrated | WEAK 43/100 | EXTREME 88/100 | Do nothing | WATCH |
| 9 | ICNT/USD | 0.2821 | 29.793 | 29.798 | +2.17% | +1.22% | 0.39x | 35.4 | 2026-11-18T04:05:08.691313+00:00 | Not calibrated | WEAK 30/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | CC/USD | 51.152 | 0.08446 | +0.74% | 4.38x |
| 2 | NIGHT/USD | 44.732 | 0.04533 | +1.39% | 1.46x |
| 3 | MELANIA/USD | 42.596 | 0.0509 | -0.39% | 0.58x |
| 4 | ZAMA/USD | 42.111 | 0.06116 | -0.13% | 2.44x |
| 5 | AKT/USD | 41.426 | 0.5173 | -0.04% | 1.14x |
| 6 | XDC/USD | 40.087 | 0.03071 | +0.66% | 18.69x |
| 7 | SENT/USD | 37.952 | 0.019039 | +0.34% | 0.54x |
| 8 | PEARL/USD | 37.372 | 1.8373 | +0.40% | 0.70x |
| 9 | ICNT/USD | 29.798 | 0.2821 | +1.22% | 0.39x |

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

- Persisted scans: 526; predictions: 4446; observations: 317341.
- Matured sampled outcomes across 1/6/24/48h: 3546; gap abstentions: 12451. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44234780748 · **Generation:** 526 · **Legacy run:** 44234780748
**Main quote time:** 2026-11-18T04:05:13.991010+00:00 · **Legacy report time:** 2026-11-18T04:05:29.493364+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.08446 | 69.85 | +0.74% | 4.38x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | XDC/USD ⭐ | 0.03071 | 58.36 | +0.66% | 18.69x | STRONG 89/100 | HIGH 61/100 | Consider small entry |
| 3 | NIGHT/USD ⭐ | 0.04533 | 56.24 | +1.39% | 1.46x | STRONG 78/100 | HIGH 61/100 | Watch |
| 4 | ZAMA/USD | 0.06116 | 55.89 | -0.13% | 2.44x | MODERATE 53/100 | VERY_HIGH 72/100 | Watch |
| 5 | AKT/USD | 0.5173 | 42.65 | -0.04% | 1.14x | WEAK 31/100 | VERY_HIGH 73/100 | Do nothing |
| 6 | MELANIA/USD | 0.0509 | 36.47 | -0.39% | 0.58x | WEAK 8/100 | EXTREME 100/100 | Do nothing |
| 7 | PEARL/USD | 1.8373 | 36.36 | +0.40% | 0.70x | WEAK 43/100 | VERY_HIGH 81/100 | Watch |
| 8 | SENT/USD | 0.019039 | 35.07 | +0.34% | 0.54x | WEAK 43/100 | EXTREME 88/100 | Do nothing |
| 9 | ICNT/USD | 0.2821 | 29.79 | +1.22% | 0.39x | WEAK 30/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.08446 | 72.68 | +0.74% | 4.38x | 4113 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | XDC/USD ⭐ | 0.03071 | 51.96 | +0.66% | 18.69x | 5941 | STRONG 86/100 | HIGH 61/100 | Consider small entry |
| 3 | NIGHT/USD ⭐ | 0.04533 | 49.77 | +1.39% | 1.46x | 13827 | STRONG 75/100 | HIGH 61/100 | Watch |

**Same-run overlap:** CC/USD, XDC/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
