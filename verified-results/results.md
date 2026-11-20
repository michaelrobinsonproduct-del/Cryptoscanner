# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T10:50:54.069536+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44722470529
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 4c5bdc104008ecf7ee02bb3bf6443f425cfca0e1 (atomic ledger/results publication)
**Ledger generation:** 968 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 607; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HBAR/USD | 0.05428 | 62.648 | 44.307 | +0.97% | +0.67% | 2.64x | 5.5 | 2026-11-20T10:50:46.806780+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 2 | SENT/USD | 0.021911 | 62.199 | 49.250 | +2.92% | -0.41% | 3.18x | 8.7 | 2026-11-20T10:50:46.806780+00:00 | Not calibrated | MODERATE 61/100 | HIGH 66/100 | Watch | WATCH |
| 3 | XRP/USD | 0.96338 | 53.847 | 57.494 | +0.43% | -0.05% | 0.66x | 1.0 | 2026-11-20T10:50:46.806780+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | XLM/USD | 0.13325 | 53.677 | 56.550 | +0.41% | -0.03% | 0.73x | 2.7 | 2026-11-20T10:50:46.806780+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | ATOM/USD | 1.2705 | 46.059 | 33.066 | +0.71% | +0.47% | 2.06x | 9.5 | 2026-11-20T10:50:46.806780+00:00 | Not calibrated | STRONG 78/100 | HIGH 60/100 | Watch | WATCH |
| 6 | BLESS/USD | 0.012439 | 44.600 | 34.370 | +2.04% | +2.30% | 0.87x | 25.8 | 2026-11-20T10:50:46.806780+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 7 | PROS/USD | 0.5915 | 41.855 | 62.498 | +9.80% | -2.36% | 0.12x | 27.0 | 2026-11-20T10:50:46.806780+00:00 | Not calibrated | WEAK 16/100 | EXTREME 100/100 | Do nothing | WATCH |
| 8 | ICNT/USD | 0.43 | 28.854 | 31.811 | +0.92% | +0.05% | 0.68x | 25.6 | 2026-11-20T10:50:46.806780+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PROS/USD | 62.498 | 0.5915 | -2.36% | 0.12x |
| 2 | XRP/USD | 57.494 | 0.96338 | -0.05% | 0.66x |
| 3 | XLM/USD | 56.550 | 0.13325 | -0.03% | 0.73x |
| 4 | SENT/USD | 49.250 | 0.021911 | -0.41% | 3.18x |
| 5 | HBAR/USD | 44.307 | 0.05428 | +0.67% | 2.64x |
| 6 | BLESS/USD | 34.370 | 0.012439 | +2.30% | 0.87x |
| 7 | ATOM/USD | 33.066 | 1.2705 | +0.47% | 2.06x |
| 8 | ICNT/USD | 31.811 | 0.43 | +0.05% | 0.68x |

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

- Persisted scans: 968; predictions: 8173; observations: 584930.
- Matured sampled outcomes across 1/6/24/48h: 9812; gap abstentions: 17479. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44722470529 · **Generation:** 968 · **Legacy run:** 44722470529
**Main quote time:** 2026-11-20T10:50:54.069536+00:00 · **Legacy report time:** 2026-11-20T10:51:52.758262+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HBAR/USD ⭐ | 0.05428 | 62.65 | +0.67% | 2.64x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 2 | SENT/USD | 0.021911 | 62.20 | -0.41% | 3.18x | MODERATE 61/100 | HIGH 66/100 | Watch |
| 3 | XRP/USD | 0.96338 | 53.85 | -0.05% | 0.66x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | XLM/USD | 0.13325 | 53.68 | -0.03% | 0.73x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | ATOM/USD ⭐ | 1.2705 | 46.06 | +0.47% | 2.06x | STRONG 88/100 | HIGH 60/100 | Consider small entry |
| 6 | BLESS/USD | 0.012439 | 44.60 | +2.30% | 0.87x | WEAK 42/100 | VERY_HIGH 79/100 | Watch |
| 7 | PROS/USD | 0.5915 | 41.85 | -2.36% | 0.12x | WEAK 16/100 | EXTREME 100/100 | Do nothing |
| 8 | ICNT/USD | 0.43 | 28.85 | +0.05% | 0.68x | WEAK 24/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HBAR/USD ⭐ | 0.0542 | 54.16 | +0.67% | 2.64x | 8476 | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 2 | ATOM/USD ⭐ | 1.2705 | 37.91 | +0.47% | 2.06x | 3345 | STRONG 79/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** HBAR/USD, ATOM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
