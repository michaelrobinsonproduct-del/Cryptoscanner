# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T15:32:51.397198+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46160131412
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 62e15aa4ab4c85e4cf8f6250b3658a44b6c22d6d (atomic ledger/results publication)
**Ledger generation:** 2172 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 429.41 | 84.303 | 82.669 | +5.44% | -0.06% | 1.19x | 20.8 | 2026-11-28T15:32:46.983094+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 2 | LUNA/USD | 4.819e-05 | 67.392 | 53.327 | +5.70% | -0.19% | 3.17x | 35.4 | 2026-11-28T15:32:46.983094+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 85/100 | Do nothing | WATCH |
| 3 | NIGHT/USD | 0.05224 | 62.672 | 76.480 | +3.98% | -2.11% | 0.67x | 11.5 | 2026-11-28T15:32:46.983094+00:00 | Not calibrated | WEAK 31/100 | EXTREME 86/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.024094 | 35.765 | 40.007 | +1.60% | +0.19% | 0.48x | 5.4 | 2026-11-28T15:32:46.983094+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 82/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 82.669 | 429.41 | -0.06% | 1.19x |
| 2 | NIGHT/USD | 76.480 | 0.05224 | -2.11% | 0.67x |
| 3 | LUNA/USD | 53.327 | 4.819e-05 | -0.19% | 3.17x |
| 4 | SENT/USD | 40.007 | 0.024094 | +0.19% | 0.48x |

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

- Persisted scans: 2172; predictions: 19291; observations: 1315278.
- Matured sampled outcomes across 1/6/24/48h: 46512; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46160131412 · **Generation:** 2172 · **Legacy run:** 46160131412
**Main quote time:** 2026-11-28T15:32:51.397198+00:00 · **Legacy report time:** 2026-11-28T15:33:39.144194+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 429.41 | 84.30 | -0.06% | 1.19x | WEAK 42/100 | VERY_HIGH 80/100 | Watch |
| 2 | LUNA/USD | 4.819e-05 | 67.39 | -0.19% | 3.17x | MODERATE 49/100 | EXTREME 85/100 | Do nothing |
| 3 | NIGHT/USD | 0.05224 | 62.67 | -2.11% | 0.67x | WEAK 31/100 | EXTREME 86/100 | Do nothing |
| 4 | SENT/USD | 0.024094 | 35.77 | +0.19% | 0.48x | WEAK 38/100 | VERY_HIGH 82/100 | Watch |

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
