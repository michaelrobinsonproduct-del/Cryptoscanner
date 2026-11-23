# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T02:28:44.758472+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45100260957
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** c01996d0722d2419918016e706697962d7f18576 (atomic ledger/results publication)
**Ledger generation:** 1368 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.3624 | 62.504 | 39.596 | +2.90% | +1.58% | 5.93x | 27.6 | 2026-11-23T02:28:40.840223+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 2 | AUD/USD | 0.66437 | 40.021 | 40.602 | +0.42% | +0.03% | 0.93x | 4.2 | 2026-11-23T02:28:40.840223+00:00 | Not calibrated | WEAK 40/100 | HIGH 62/100 | Watch | WATCH |
| 3 | DRV/USD | 0.37146 | 35.991 | 43.133 | +0.71% | -1.32% | 0.95x | 13.2 | 2026-11-23T02:28:40.840223+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 4 | CAP/USD | 0.093988 | 24.953 | 26.925 | +0.44% | +0.96% | 0.32x | 17.1 | 2026-11-23T02:28:40.840223+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 43.133 | 0.37146 | -1.32% | 0.95x |
| 2 | AUD/USD | 40.602 | 0.66437 | +0.03% | 0.93x |
| 3 | ICNT/USD | 39.596 | 0.3624 | +1.58% | 5.93x |
| 4 | CAP/USD | 26.925 | 0.093988 | +0.96% | 0.32x |

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

- Persisted scans: 1368; predictions: 11218; observations: 828217.
- Matured sampled outcomes across 1/6/24/48h: 17923; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 84 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45100260957 · **Generation:** 1368 · **Legacy run:** 45100260957
**Main quote time:** 2026-11-23T02:28:44.758472+00:00 · **Legacy report time:** 2026-11-23T02:29:54.517809+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.3624 | 62.50 | +1.58% | 5.93x | STRONG 86/100 | VERY_HIGH 72/100 | Watch |
| 2 | AUD/USD | 0.66437 | 40.02 | +0.03% | 0.93x | WEAK 40/100 | HIGH 62/100 | Watch |
| 3 | DRV/USD | 0.37146 | 35.99 | -1.32% | 0.95x | WEAK 18/100 | VERY_HIGH 78/100 | Do nothing |
| 4 | CAP/USD | 0.093988 | 24.95 | +0.96% | 0.32x | WEAK 37/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.3612 | 67.16 | +1.58% | 5.93x | 2626 | STRONG 89/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** ICNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
