# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T15:43:15.626160+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46161018157
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9e75de031814b317575242af1c6f4a4225bc7aef (atomic ledger/results publication)
**Ledger generation:** 2173 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 425.38 | 69.484 | 81.186 | +4.45% | -1.43% | 0.54x | 9.9 | 2026-11-28T15:43:11.986580+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 2 | LUNA/USD | 4.819e-05 | 67.967 | 52.242 | +5.70% | +0.14% | 3.06x | 37.5 | 2026-11-28T15:43:11.986580+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.05235 | 66.163 | 76.603 | +4.20% | -1.44% | 0.67x | 13.4 | 2026-11-28T15:43:11.986580+00:00 | Not calibrated | WEAK 33/100 | EXTREME 86/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.024185 | 36.745 | 41.464 | +1.99% | -0.26% | 0.66x | 7.9 | 2026-11-28T15:43:11.986580+00:00 | Not calibrated | WEAK 23/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 81.186 | 425.38 | -1.43% | 0.54x |
| 2 | NIGHT/USD | 76.603 | 0.05235 | -1.44% | 0.67x |
| 3 | LUNA/USD | 52.242 | 4.819e-05 | +0.14% | 3.06x |
| 4 | SENT/USD | 41.464 | 0.024185 | -0.26% | 0.66x |

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

- Persisted scans: 2173; predictions: 19295; observations: 1315884.
- Matured sampled outcomes across 1/6/24/48h: 46547; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46161018157 · **Generation:** 2173 · **Legacy run:** 46161018157
**Main quote time:** 2026-11-28T15:43:15.626160+00:00 · **Legacy report time:** 2026-11-28T15:44:02.494263+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 425.38 | 69.48 | -1.43% | 0.54x | WEAK 40/100 | VERY_HIGH 80/100 | Do nothing |
| 2 | LUNA/USD ⭐ | 4.819e-05 | 67.97 | +0.14% | 3.06x | STRONG 74/100 | VERY_HIGH 79/100 | Watch |
| 3 | NIGHT/USD | 0.05235 | 66.16 | -1.44% | 0.67x | WEAK 33/100 | EXTREME 86/100 | Do nothing |
| 4 | SENT/USD | 0.024185 | 36.75 | -0.26% | 0.66x | WEAK 23/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD ⭐ | 4.845e-05 | 67.25 | +0.14% | 3.06x | 1221 | STRONG 74/100 | EXTREME 89/100 | Do nothing |

**Same-run overlap:** LUNA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
