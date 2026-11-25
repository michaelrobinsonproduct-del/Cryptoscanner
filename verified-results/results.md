# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T15:33:04.086226+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45645751426
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1ff74dc58cb0200e3349245c4f2cfff65d094813 (atomic ledger/results publication)
**Ledger generation:** 1736 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.00999 | 68.173 | 71.378 | +5.49% | +0.40% | 0.48x | 20.0 | 2026-11-25T15:33:00.486222+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | BLUR/USD | 0.00964 | 50.415 | 55.281 | +11.96% | -0.21% | 0.62x | 41.6 | 2026-11-25T15:33:00.486222+00:00 | Not calibrated | WEAK 15/100 | EXTREME 100/100 | Do nothing | WATCH |
| 3 | DRV/USD | 0.3223 | 43.645 | 46.415 | +2.55% | -0.19% | 0.82x | 18.3 | 2026-11-25T15:33:00.486222+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 4 | XPL/USD | 0.0448 | 24.682 | 25.764 | +1.82% | -0.22% | 1.00x | 44.7 | 2026-11-25T15:33:00.486222+00:00 | Not calibrated | WEAK 7/100 | EXTREME 95/100 | Do nothing | WATCH |
| 5 | CT/USD | 0.1291 | 20.961 | 34.994 | +2.22% | -1.45% | 0.32x | 23.3 | 2026-11-25T15:33:00.486222+00:00 | Not calibrated | WEAK 5/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 71.378 | 0.00999 | +0.40% | 0.48x |
| 2 | BLUR/USD | 55.281 | 0.00964 | -0.21% | 0.62x |
| 3 | DRV/USD | 46.415 | 0.3223 | -0.19% | 0.82x |
| 4 | CT/USD | 34.994 | 0.1291 | -1.45% | 0.32x |
| 5 | XPL/USD | 25.764 | 0.0448 | -0.22% | 1.00x |

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

- Persisted scans: 1736; predictions: 14612; observations: 1052273.
- Matured sampled outcomes across 1/6/24/48h: 32337; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45645751426 · **Generation:** 1736 · **Legacy run:** 45645751426
**Main quote time:** 2026-11-25T15:33:04.086226+00:00 · **Legacy report time:** 2026-11-25T15:33:58.094594+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.00999 | 68.17 | +0.40% | 0.48x | MODERATE 54/100 | VERY_HIGH 82/100 | Watch |
| 2 | BLUR/USD | 0.00964 | 50.41 | -0.21% | 0.62x | WEAK 15/100 | EXTREME 100/100 | Do nothing |
| 3 | DRV/USD | 0.3223 | 43.65 | -0.19% | 0.82x | WEAK 22/100 | VERY_HIGH 74/100 | Do nothing |
| 4 | XPL/USD | 0.0448 | 24.68 | -0.22% | 1.00x | WEAK 7/100 | EXTREME 95/100 | Do nothing |
| 5 | CT/USD | 0.1291 | 20.96 | -1.45% | 0.32x | WEAK 5/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 24.752 | 48.68 | +0.16% | 1.24x | 12305 | WEAK 44/100 | HIGH 68/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
