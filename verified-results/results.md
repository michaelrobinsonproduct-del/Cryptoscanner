# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T09:22:14.895608+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45364112631
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f05e4767458631aab632c5853bb70d738a2ca355 (atomic ledger/results publication)
**Ledger generation:** 1555 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01287 | 76.146 | 79.017 | +11.72% | +0.08% | 0.67x | 15.6 | 2026-11-24T09:22:06.842728+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | VVV/USD | 24.949 | 74.693 | 65.332 | +2.05% | -0.04% | 1.95x | 8.0 | 2026-11-24T09:22:06.842728+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LCX/USD | 0.03456 | 74.676 | 63.668 | +8.88% | +1.26% | 1.47x | 26.0 | 2026-11-24T09:22:06.842728+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.49e-06 | 65.669 | 60.146 | +1.99% | -0.23% | 1.67x | 8.6 | 2026-11-24T09:22:06.842728+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 5 | LINK/USD | 9.0348 | 64.370 | 55.335 | +0.33% | -0.06% | 1.93x | 4.0 | 2026-11-24T09:22:06.842728+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XMR/USD | 498.18 | 58.254 | 66.481 | +2.50% | +0.14% | 0.11x | 12.1 | 2026-11-24T09:22:06.842728+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | MANA/USD | 0.05727 | 46.279 | 29.266 | +0.39% | +0.40% | 2.54x | 8.7 | 2026-11-24T09:22:06.842728+00:00 | Not calibrated | STRONG 78/100 | HIGH 67/100 | Watch | WATCH |
| 8 | BAT/USD | 0.07954 | 44.275 | 51.368 | +3.07% | -0.10% | 0.34x | 5.0 | 2026-11-24T09:22:06.842728+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | BABY/USD | 0.00881 | 43.281 | 52.507 | +3.65% | -0.22% | 0.19x | 11.3 | 2026-11-24T09:22:06.842728+00:00 | Not calibrated | WEAK 22/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | FET/USD | 0.109 | 29.373 | 31.244 | +0.37% | +0.37% | 0.63x | 18.4 | 2026-11-24T09:22:06.842728+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | ATOM/USD | 1.2964 | 27.524 | 35.207 | +1.11% | -0.42% | 0.44x | 11.6 | 2026-11-24T09:22:06.842728+00:00 | Not calibrated | WEAK 14/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 79.017 | 0.01287 | +0.08% | 0.67x |
| 2 | XMR/USD | 66.481 | 498.18 | +0.14% | 0.11x |
| 3 | VVV/USD | 65.332 | 24.949 | -0.04% | 1.95x |
| 4 | LCX/USD | 63.668 | 0.03456 | +1.26% | 1.47x |
| 5 | PEPE/USD | 60.146 | 3.49e-06 | -0.23% | 1.67x |
| 6 | LINK/USD | 55.335 | 9.0348 | -0.06% | 1.93x |
| 7 | BABY/USD | 52.507 | 0.00881 | -0.22% | 0.19x |
| 8 | BAT/USD | 51.368 | 0.07954 | -0.10% | 0.34x |
| 9 | ATOM/USD | 35.207 | 1.2964 | -0.42% | 0.44x |
| 10 | FET/USD | 31.244 | 0.109 | +0.37% | 0.63x |
| 11 | MANA/USD | 29.266 | 0.05727 | +0.40% | 2.54x |

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

- Persisted scans: 1555; predictions: 13386; observations: 942093.
- Matured sampled outcomes across 1/6/24/48h: 25443; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 142 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45364112631 · **Generation:** 1555 · **Legacy run:** 45364112631
**Main quote time:** 2026-11-24T09:22:14.895608+00:00 · **Legacy report time:** 2026-11-24T09:23:26.557404+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.01287 | 76.15 | +0.08% | 0.67x | MODERATE 53/100 | VERY_HIGH 76/100 | Watch |
| 2 | VVV/USD | 24.949 | 74.69 | -0.04% | 1.95x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 3 | LCX/USD ⭐ | 0.03456 | 74.68 | +1.26% | 1.47x | STRONG 82/100 | VERY_HIGH 72/100 | Watch |
| 4 | PEPE/USD | 3.49e-06 | 65.67 | -0.23% | 1.67x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 5 | LINK/USD | 9.0348 | 64.37 | -0.06% | 1.93x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 6 | XMR/USD | 498.18 | 58.25 | +0.14% | 0.11x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 7 | MANA/USD | 0.05727 | 46.28 | +0.40% | 2.54x | STRONG 78/100 | HIGH 67/100 | Watch |
| 8 | BAT/USD | 0.07954 | 44.28 | -0.10% | 0.34x | WEAK 27/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | BABY/USD | 0.00881 | 43.28 | -0.22% | 0.19x | WEAK 22/100 | EXTREME 87/100 | Do nothing |
| 10 | FET/USD | 0.109 | 29.37 | +0.37% | 0.63x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 11 | ATOM/USD | 1.2964 | 27.52 | -0.42% | 0.44x | WEAK 14/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LCX/USD ⭐ | 0.03387 | 79.84 | +1.26% | 1.47x | 2805 | STRONG 95/100 | HIGH 67/100 | Watch |

**Same-run overlap:** LCX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
