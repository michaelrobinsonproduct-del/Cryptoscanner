# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T20:08:27.150670+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45476922967
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9d6a37cfe2c21e81597ee2b7f815203047881573 (atomic ledger/results publication)
**Ledger generation:** 1620 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 498.97 | 84.837 | 71.245 | +2.66% | -0.28% | 3.63x | 4.8 | 2026-11-24T20:08:23.273314+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 2 | GBP/USD | 1.31113 | 59.915 | 59.004 | +0.60% | +0.00% | 1.09x | 0.5 | 2026-11-24T20:08:23.273314+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 3 | AUD/USD | 0.66449 | 57.327 | 42.282 | +0.29% | +0.01% | 31.41x | 6.3 | 2026-11-24T20:08:23.273314+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.45e-06 | 43.275 | 46.274 | +0.82% | +0.20% | 0.60x | 5.8 | 2026-11-24T20:08:23.273314+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04854 | 40.512 | 42.152 | +0.81% | -0.37% | 1.02x | 8.2 | 2026-11-24T20:08:23.273314+00:00 | Not calibrated | WEAK 30/100 | HIGH 68/100 | Do nothing | WATCH |
| 6 | 2Z/USD | 0.01621 | 40.420 | 46.618 | +3.58% | -1.33% | 1.05x | 18.5 | 2026-11-24T20:08:23.273314+00:00 | Not calibrated | WEAK 25/100 | EXTREME 90/100 | Do nothing | WATCH |
| 7 | ZEUS/USD | 0.00466 | 37.934 | 54.770 | +6.39% | -2.16% | 0.40x | 43.2 | 2026-11-24T20:08:23.273314+00:00 | Not calibrated | WEAK 9/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 71.245 | 498.97 | -0.28% | 3.63x |
| 2 | GBP/USD | 59.004 | 1.31113 | +0.00% | 1.09x |
| 3 | ZEUS/USD | 54.770 | 0.00466 | -2.16% | 0.40x |
| 4 | 2Z/USD | 46.618 | 0.01621 | -1.33% | 1.05x |
| 5 | PEPE/USD | 46.274 | 3.45e-06 | +0.20% | 0.60x |
| 6 | AUD/USD | 42.282 | 0.66449 | +0.01% | 31.41x |
| 7 | NIGHT/USD | 42.152 | 0.04854 | -0.37% | 1.02x |

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

- Persisted scans: 1620; predictions: 13903; observations: 981672.
- Matured sampled outcomes across 1/6/24/48h: 28308; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45476922967 · **Generation:** 1620 · **Legacy run:** 45476922967
**Main quote time:** 2026-11-24T20:08:27.150670+00:00 · **Legacy report time:** 2026-11-24T20:09:27.061087+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 498.97 | 84.84 | -0.28% | 3.63x | STRONG 72/100 | HIGH 61/100 | Watch |
| 2 | GBP/USD | 1.31113 | 59.91 | +0.00% | 1.09x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 3 | AUD/USD | 0.66449 | 57.33 | +0.01% | 31.41x | STRONG 74/100 | HIGH 55/100 | Watch |
| 4 | PEPE/USD | 3.45e-06 | 43.27 | +0.20% | 0.60x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 5 | NIGHT/USD | 0.04854 | 40.51 | -0.37% | 1.02x | WEAK 30/100 | HIGH 68/100 | Do nothing |
| 6 | 2Z/USD | 0.01621 | 40.42 | -1.33% | 1.05x | WEAK 25/100 | EXTREME 90/100 | Do nothing |
| 7 | ZEUS/USD | 0.00466 | 37.93 | -2.16% | 0.40x | WEAK 9/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
