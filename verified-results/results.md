# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T18:11:41.270735+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45235366294
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9d6ec44427fc6f46fce7ad0ce13e427992364fcb (atomic ledger/results publication)
**Ledger generation:** 1464 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 6.647 | 98.704 | 95.789 | +6.73% | +0.32% | 1.13x | 4.5 | 2026-11-23T18:11:34.997805+00:00 | Not calibrated | STRONG 84/100 | HIGH 62/100 | Watch | WATCH |
| 2 | UNI/USD | 4.9255 | 97.213 | 84.764 | +5.22% | -0.51% | 4.39x | 5.3 | 2026-11-23T18:11:34.997805+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Watch | WATCH |
| 3 | JUP/USD | 0.24787 | 96.707 | 77.150 | +10.38% | +1.10% | 2.41x | 8.5 | 2026-11-23T18:11:34.997805+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 4 | LTC/USD | 41.99 | 94.202 | 84.514 | +4.56% | -0.33% | 2.13x | 4.8 | 2026-11-23T18:11:34.997805+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ICP/USD | 2.091 | 93.439 | 80.582 | +6.36% | -0.43% | 3.00x | 4.8 | 2026-11-23T18:11:34.997805+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 6 | CC/USD | 0.07815 | 92.012 | 77.012 | +6.66% | +0.00% | 3.19x | 9.0 | 2026-11-23T18:11:34.997805+00:00 | Not calibrated | STRONG 91/100 | HIGH 60/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6872 | 91.907 | 87.900 | +4.80% | -0.45% | 1.63x | 1.5 | 2026-11-23T18:11:34.997805+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ADA/USD | 0.150957 | 86.602 | 84.235 | +4.39% | +0.15% | 1.16x | 3.0 | 2026-11-23T18:11:34.997805+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 9 | HYPE/USD | 65.25 | 82.384 | 78.544 | +3.47% | -0.70% | 1.73x | 1.5 | 2026-11-23T18:11:34.997805+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XRP/USD | 0.95339 | 78.759 | 74.456 | +2.79% | -0.60% | 1.73x | 0.1 | 2026-11-23T18:11:34.997805+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0573753 | 78.164 | 80.087 | +3.78% | -0.21% | 0.91x | 2.8 | 2026-11-23T18:11:34.997805+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 12 | SOL/USD | 73.49 | 76.725 | 82.665 | +4.05% | -0.37% | 0.59x | 1.4 | 2026-11-23T18:11:34.997805+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 95.789 | 6.647 | +0.32% | 1.13x |
| 2 | SUI/USD | 87.900 | 0.6872 | -0.45% | 1.63x |
| 3 | UNI/USD | 84.764 | 4.9255 | -0.51% | 4.39x |
| 4 | LTC/USD | 84.514 | 41.99 | -0.33% | 2.13x |
| 5 | ADA/USD | 84.235 | 0.150957 | +0.15% | 1.16x |
| 6 | SOL/USD | 82.665 | 73.49 | -0.37% | 0.59x |
| 7 | ICP/USD | 80.582 | 2.091 | -0.43% | 3.00x |
| 8 | XDG/USD | 80.087 | 0.0573753 | -0.21% | 0.91x |
| 9 | HYPE/USD | 78.544 | 65.25 | -0.70% | 1.73x |
| 10 | JUP/USD | 77.150 | 0.24787 | +1.10% | 2.41x |
| 11 | CC/USD | 77.012 | 0.07815 | +0.00% | 3.19x |
| 12 | XRP/USD | 74.456 | 0.95339 | -0.60% | 1.73x |

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

- Persisted scans: 1464; predictions: 12335; observations: 886678.
- Matured sampled outcomes across 1/6/24/48h: 21616; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 0; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45235366294 · **Generation:** 1464 · **Legacy run:** 45235366294
**Main quote time:** 2026-11-23T18:11:41.270735+00:00 · **Legacy report time:** 2026-11-23T18:12:49.218340+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 6.647 | 98.70 | +0.32% | 1.13x | STRONG 94/100 | HIGH 62/100 | Watch |
| 2 | UNI/USD | 4.9255 | 97.21 | -0.51% | 4.39x | STRONG 79/100 | HIGH 61/100 | Watch |
| 3 | JUP/USD | 0.24787 | 96.71 | +1.10% | 2.41x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 4 | LTC/USD | 41.99 | 94.20 | -0.33% | 2.13x | STRONG 77/100 | HIGH 61/100 | Watch |
| 5 | ICP/USD | 2.091 | 93.44 | -0.43% | 3.00x | STRONG 77/100 | HIGH 61/100 | Watch |
| 6 | CC/USD | 0.07815 | 92.01 | +0.00% | 3.19x | STRONG 91/100 | HIGH 60/100 | Watch |
| 7 | SUI/USD | 0.6872 | 91.91 | -0.45% | 1.63x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 8 | ADA/USD ⭐ | 0.150957 | 86.60 | +0.15% | 1.16x | STRONG 78/100 | HIGH 62/100 | Watch |
| 9 | HYPE/USD | 65.25 | 82.38 | -0.70% | 1.73x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 10 | XRP/USD | 0.95339 | 78.76 | -0.60% | 1.73x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 11 | XDG/USD | 0.0573753 | 78.16 | -0.21% | 0.91x | WEAK 44/100 | HIGH 68/100 | Watch |
| 12 | SOL/USD | 73.49 | 76.73 | -0.37% | 0.59x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.150943 | 92.08 | +0.15% | 1.16x | 12991 | STRONG 81/100 | HIGH 62/100 | Watch |
| 2 | INJ/USD ⭐ | 6.62 | 91.21 | +0.32% | 1.13x | 8593 | STRONG 91/100 | HIGH 62/100 | Watch |
| 3 | ALGO/USD | 0.08522 | 86.72 | +0.09% | 1.95x | 8766 | STRONG 78/100 | HIGH 55/100 | Watch |
| 4 | DOT/USD | 0.6926 | 86.07 | +0.49% | 1.48x | 8980 | STRONG 88/100 | HIGH 60/100 | Watch |

**Same-run overlap:** INJ/USD, ADA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
