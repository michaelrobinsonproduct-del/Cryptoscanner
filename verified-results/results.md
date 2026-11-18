# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T05:00:03.036373+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44241079774
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** f2031122624f3b4a510e7104cd31e2fbb1976b17 (atomic ledger/results publication)
**Ledger generation:** 537 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XDC/USD | 0.03092 | 56.641 | 50.006 | +1.98% | -0.87% | 2.10x | 3.2 | 2026-11-18T04:59:57.384707+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 2 | UP/USD | 0.05549 | 55.813 | 64.145 | +4.72% | -0.38% | 0.36x | 1.8 | 2026-11-18T04:59:57.384707+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 3 | SENT/USD | 0.019314 | 53.275 | 50.989 | +3.45% | +1.32% | 0.57x | 8.3 | 2026-11-18T04:59:57.384707+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | PEARL/USD | 1.8489 | 46.443 | 49.588 | +2.12% | +0.17% | 0.60x | 0.5 | 2026-11-18T04:59:57.384707+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | UAI/USD | 0.0336 | 46.307 | 31.158 | +0.66% | +0.03% | 5.02x | 8.9 | 2026-11-18T04:59:57.384707+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 6 | MELANIA/USD | 0.0498 | 38.182 | 36.525 | +2.26% | +0.20% | 1.07x | 20.1 | 2026-11-18T04:59:57.384707+00:00 | Not calibrated | WEAK 44/100 | EXTREME 86/100 | Do nothing | WATCH |
| 7 | CC/USD | 0.08337 | 35.343 | 42.557 | +1.51% | -0.26% | 0.41x | 7.2 | 2026-11-18T04:59:57.384707+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 8 | MEGA/USD | 0.05209 | 21.770 | 24.897 | +0.87% | +0.08% | 0.65x | 25.0 | 2026-11-18T04:59:57.384707+00:00 | Not calibrated | WEAK 21/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | ICNT/USD | 0.2784 | 10.541 | 30.934 | +0.83% | -3.73% | 0.83x | 14.4 | 2026-11-18T04:59:57.384707+00:00 | Not calibrated | WEAK 5/100 | VERY_HIGH 83/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | UP/USD | 64.145 | 0.05549 | -0.38% | 0.36x |
| 2 | SENT/USD | 50.989 | 0.019314 | +1.32% | 0.57x |
| 3 | XDC/USD | 50.006 | 0.03092 | -0.87% | 2.10x |
| 4 | PEARL/USD | 49.588 | 1.8489 | +0.17% | 0.60x |
| 5 | CC/USD | 42.557 | 0.08337 | -0.26% | 0.41x |
| 6 | MELANIA/USD | 36.525 | 0.0498 | +0.20% | 1.07x |
| 7 | UAI/USD | 31.158 | 0.0336 | +0.03% | 5.02x |
| 8 | ICNT/USD | 30.934 | 0.2784 | -3.73% | 0.83x |
| 9 | MEGA/USD | 24.897 | 0.05209 | +0.08% | 0.65x |

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

- Persisted scans: 537; predictions: 4539; observations: 324040.
- Matured sampled outcomes across 1/6/24/48h: 3600; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44241079774 · **Generation:** 537 · **Legacy run:** 44241079774
**Main quote time:** 2026-11-18T05:00:03.036373+00:00 · **Legacy report time:** 2026-11-18T05:00:20.399901+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XDC/USD ⭐ | 0.03092 | 56.64 | -0.87% | 2.10x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 2 | UP/USD | 0.05549 | 55.81 | -0.38% | 0.36x | WEAK 33/100 | VERY_HIGH 81/100 | Do nothing |
| 3 | SENT/USD | 0.019314 | 53.28 | +1.32% | 0.57x | MODERATE 57/100 | VERY_HIGH 82/100 | Watch |
| 4 | PEARL/USD ⭐ | 1.8489 | 46.44 | +0.17% | 0.60x | MODERATE 53/100 | VERY_HIGH 75/100 | Watch |
| 5 | UAI/USD | 0.0336 | 46.31 | +0.03% | 5.02x | MODERATE 68/100 | HIGH 67/100 | Watch |
| 6 | MELANIA/USD | 0.0498 | 38.18 | +0.20% | 1.07x | WEAK 44/100 | EXTREME 86/100 | Do nothing |
| 7 | CC/USD | 0.08337 | 35.34 | -0.26% | 0.41x | WEAK 23/100 | VERY_HIGH 81/100 | Do nothing |
| 8 | MEGA/USD | 0.05209 | 21.77 | +0.08% | 0.65x | WEAK 21/100 | EXTREME 94/100 | Do nothing |
| 9 | ICNT/USD | 0.2784 | 10.54 | -3.73% | 0.83x | WEAK 5/100 | VERY_HIGH 83/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 1.849 | 70.34 | +0.61% | 2.02x | 4018 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | XDC/USD ⭐ | 0.03092 | 62.40 | +0.06% | 1.82x | 5978 | STRONG 76/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XDC/USD, PEARL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
