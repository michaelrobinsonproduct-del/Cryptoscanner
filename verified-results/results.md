# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T16:50:12.828996+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44351687667
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** ad1ca435ba9d2cd93387b4184844aac7300865fa (atomic ledger/results publication)
**Ledger generation:** 616 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019577 | 57.833 | 58.707 | +4.86% | +0.10% | 0.86x | 12.8 | 2026-11-18T16:50:10.223836+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 2 | TRUST/USD | 0.04921 | 47.409 | 51.697 | +4.37% | -0.77% | 0.95x | 22.3 | 2026-11-18T16:50:10.223836+00:00 | Not calibrated | WEAK 19/100 | EXTREME 85/100 | Do nothing | WATCH |
| 3 | MEGA/USD | 0.05297 | 38.129 | 36.886 | +2.58% | +0.27% | 0.99x | 24.5 | 2026-11-18T16:50:10.223836+00:00 | Not calibrated | WEAK 39/100 | EXTREME 86/100 | Do nothing | WATCH |
| 4 | CT/USD | 0.1153 | 34.502 | 36.628 | +2.04% | -0.69% | 1.13x | 17.4 | 2026-11-18T16:50:10.223836+00:00 | Not calibrated | WEAK 22/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 58.707 | 0.019577 | +0.10% | 0.86x |
| 2 | TRUST/USD | 51.697 | 0.04921 | -0.77% | 0.95x |
| 3 | MEGA/USD | 36.886 | 0.05297 | +0.27% | 0.99x |
| 4 | CT/USD | 36.628 | 0.1153 | -0.69% | 1.13x |

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

- Persisted scans: 616; predictions: 5274; observations: 372151.
- Matured sampled outcomes across 1/6/24/48h: 4532; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44351687667 · **Generation:** 616 · **Legacy run:** 44351687667
**Main quote time:** 2026-11-18T16:50:12.828996+00:00 · **Legacy report time:** 2026-11-18T16:50:39.353040+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019577 | 57.83 | +0.10% | 0.86x | WEAK 44/100 | VERY_HIGH 80/100 | Watch |
| 2 | TRUST/USD | 0.04921 | 47.41 | -0.77% | 0.95x | WEAK 19/100 | EXTREME 85/100 | Do nothing |
| 3 | MEGA/USD | 0.05297 | 38.13 | +0.27% | 0.99x | WEAK 39/100 | EXTREME 86/100 | Do nothing |
| 4 | CT/USD | 0.1153 | 34.50 | -0.69% | 1.13x | WEAK 22/100 | EXTREME 86/100 | Do nothing |

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
