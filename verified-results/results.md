# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T10:42:37.270882+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45376868978
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 57b8b6237ac0dbfc78af32b4198c815c04f2f52f (atomic ledger/results publication)
**Ledger generation:** 1563 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01263 | 98.732 | 82.493 | +9.64% | +0.64% | 2.31x | 7.9 | 2026-11-24T10:42:31.022334+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 496.13 | 79.597 | 63.208 | +2.08% | +0.28% | 3.83x | 12.7 | 2026-11-24T10:42:31.022334+00:00 | Not calibrated | STRONG 90/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | PEPE/USD | 3.446e-06 | 64.860 | 54.183 | +0.70% | -0.86% | 5.61x | 2.9 | 2026-11-24T10:42:31.022334+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 4 | VVV/USD | 25.147 | 59.715 | 68.846 | +2.86% | -0.36% | 0.27x | 12.3 | 2026-11-24T10:42:31.022334+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 5 | DBR/USD | 0.01447 | 50.636 | 65.784 | +7.82% | -2.16% | 0.57x | 20.7 | 2026-11-24T10:42:31.022334+00:00 | Not calibrated | WEAK 20/100 | EXTREME 100/100 | Do nothing | WATCH |
| 6 | 2Z/USD | 0.0161 | 38.898 | 44.605 | +2.88% | -0.06% | 0.46x | 12.4 | 2026-11-24T10:42:31.022334+00:00 | Not calibrated | WEAK 19/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | BAT/USD | 0.0778 | 30.291 | 35.529 | +0.82% | -0.27% | 0.61x | 5.1 | 2026-11-24T10:42:31.022334+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 8 | ATOM/USD | 1.2883 | 28.392 | 31.948 | +0.48% | -0.10% | 0.69x | 9.3 | 2026-11-24T10:42:31.022334+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | INX/USD | 0.003919 | 26.781 | 22.724 | +0.54% | -2.19% | 3.00x | 25.5 | 2026-11-24T10:42:31.022334+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 82.493 | 0.01263 | +0.64% | 2.31x |
| 2 | VVV/USD | 68.846 | 25.147 | -0.36% | 0.27x |
| 3 | DBR/USD | 65.784 | 0.01447 | -2.16% | 0.57x |
| 4 | XMR/USD | 63.208 | 496.13 | +0.28% | 3.83x |
| 5 | PEPE/USD | 54.183 | 3.446e-06 | -0.86% | 5.61x |
| 6 | 2Z/USD | 44.605 | 0.0161 | -0.06% | 0.46x |
| 7 | BAT/USD | 35.529 | 0.0778 | -0.27% | 0.61x |
| 8 | ATOM/USD | 31.948 | 1.2883 | -0.10% | 0.69x |
| 9 | INX/USD | 22.724 | 0.003919 | -2.19% | 3.00x |

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

- Persisted scans: 1563; predictions: 13465; observations: 946965.
- Matured sampled outcomes across 1/6/24/48h: 25806; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45376868978 · **Generation:** 1563 · **Legacy run:** 45376868978
**Main quote time:** 2026-11-24T10:42:37.270882+00:00 · **Legacy report time:** 2026-11-24T10:43:40.430947+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01263 | 98.73 | +0.64% | 2.31x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 496.13 | 79.60 | +0.28% | 3.83x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 3 | PEPE/USD | 3.446e-06 | 64.86 | -0.86% | 5.61x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 4 | VVV/USD | 25.147 | 59.72 | -0.36% | 0.27x | WEAK 30/100 | VERY_HIGH 82/100 | Do nothing |
| 5 | DBR/USD | 0.01447 | 50.64 | -2.16% | 0.57x | WEAK 20/100 | EXTREME 100/100 | Do nothing |
| 6 | 2Z/USD | 0.0161 | 38.90 | -0.06% | 0.46x | WEAK 19/100 | EXTREME 94/100 | Do nothing |
| 7 | BAT/USD | 0.0778 | 30.29 | -0.27% | 0.61x | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing |
| 8 | ATOM/USD | 1.2883 | 28.39 | -0.10% | 0.69x | WEAK 19/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | INX/USD | 0.003919 | 26.78 | -2.19% | 3.00x | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01264 | 84.00 | +0.64% | 2.31x | 10311 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 496.39 | 71.44 | +0.28% | 3.83x | 10980 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** MON/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
