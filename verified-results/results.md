# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T04:21:02.652455+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44984545344
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** af38096ee2b02a16c6214b93180fd575a9715716 (atomic ledger/results publication)
**Ledger generation:** 1232 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TRUMP/USD | 0.893 | 51.708 | 34.458 | +0.79% | +0.45% | 5.09x | 11.2 | 2026-11-22T04:20:59.265080+00:00 | Not calibrated | STRONG 76/100 | HIGH 66/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.0444 | 33.188 | 44.577 | +0.27% | -0.60% | 0.16x | 11.3 | 2026-11-22T04:20:59.265080+00:00 | Not calibrated | WEAK 17/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 3 | SPX/USD | 0.2811 | 28.919 | 28.121 | +0.61% | -0.18% | 1.17x | 17.8 | 2026-11-22T04:20:59.265080+00:00 | Not calibrated | WEAK 19/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 44.577 | 0.0444 | -0.60% | 0.16x |
| 2 | TRUMP/USD | 34.458 | 0.893 | +0.45% | 5.09x |
| 3 | SPX/USD | 28.121 | 0.2811 | -0.18% | 1.17x |

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

- Persisted scans: 1232; predictions: 9902; observations: 745414.
- Matured sampled outcomes across 1/6/24/48h: 13961; gap abstentions: 21953. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 32 (sampled only; not a success-rate estimate).
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

**Writer:** 44984545344 · **Generation:** 1232 · **Legacy run:** 44984545344
**Main quote time:** 2026-11-22T04:21:02.652455+00:00 · **Legacy report time:** 2026-11-22T04:22:07.182032+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TRUMP/USD ⭐ | 0.893 | 51.71 | +0.45% | 5.09x | STRONG 86/100 | HIGH 66/100 | Consider small entry |
| 2 | NIGHT/USD | 0.0444 | 33.19 | -0.60% | 0.16x | WEAK 17/100 | VERY_HIGH 82/100 | Do nothing |
| 3 | SPX/USD | 0.2811 | 28.92 | -0.18% | 1.17x | WEAK 19/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 1.9941 | 59.62 | +0.42% | 1.10x | 9241 | MODERATE 55/100 | VERY_HIGH 74/100 | Watch |
| 2 | TRUMP/USD ⭐ | 0.888 | 36.77 | +0.45% | 5.09x | 2933 | STRONG 73/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** TRUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
