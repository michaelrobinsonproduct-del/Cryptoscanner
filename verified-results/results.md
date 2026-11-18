# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T18:52:54.371408+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44374366262
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** d43849a5dbd2fa1d34ef00bdcb26dc2031f49cbf (atomic ledger/results publication)
**Ledger generation:** 641 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 17.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INFI/USD | 0.1342 | 107.103 | 67.103 | +5.67% | +7.58% | 3.69x | 7.5 | 2026-11-18T18:52:48.223230+00:00 | Not calibrated | STRONG 100/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019883 | 85.111 | 73.369 | +6.50% | -0.65% | 2.82x | 5.5 | 2026-11-18T18:52:48.223230+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | STABLE/USD | 0.02341 | 57.986 | 63.152 | +11.21% | +0.60% | 0.18x | 25.7 | 2026-11-18T18:52:48.223230+00:00 | Not calibrated | MODERATE 49/100 | EXTREME 94/100 | Do nothing | WATCH |
| 4 | AKT/USD | 0.5108 | 46.141 | 27.202 | +0.29% | +0.79% | 4.31x | 13.7 | 2026-11-18T18:52:48.223230+00:00 | Not calibrated | STRONG 73/100 | HIGH 66/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04508 | 44.881 | 47.505 | +0.42% | -0.13% | 0.80x | 6.7 | 2026-11-18T18:52:48.223230+00:00 | Not calibrated | WEAK 27/100 | HIGH 68/100 | Do nothing | WATCH |
| 6 | MNT/USD | 0.3851 | 41.884 | 50.106 | +3.16% | -0.05% | 0.20x | 7.8 | 2026-11-18T18:52:48.223230+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 7 | W/USD | 0.00899 | 37.588 | 30.435 | +0.67% | +0.90% | 1.27x | 11.1 | 2026-11-18T18:52:48.223230+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | UAI/USD | 0.03357 | 30.979 | 30.391 | +0.57% | +0.48% | 0.82x | 8.9 | 2026-11-18T18:52:48.223230+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 74/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 73.369 | 0.019883 | -0.65% | 2.82x |
| 2 | INFI/USD | 67.103 | 0.1342 | +7.58% | 3.69x |
| 3 | STABLE/USD | 63.152 | 0.02341 | +0.60% | 0.18x |
| 4 | MNT/USD | 50.106 | 0.3851 | -0.05% | 0.20x |
| 5 | NIGHT/USD | 47.505 | 0.04508 | -0.13% | 0.80x |
| 6 | W/USD | 30.435 | 0.00899 | +0.90% | 1.27x |
| 7 | UAI/USD | 30.391 | 0.03357 | +0.48% | 0.82x |
| 8 | AKT/USD | 27.202 | 0.5108 | +0.79% | 4.31x |

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

- Persisted scans: 641; predictions: 5442; observations: 387376.
- Matured sampled outcomes across 1/6/24/48h: 4730; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44374366262 · **Generation:** 641 · **Legacy run:** 44374366262
**Main quote time:** 2026-11-18T18:52:54.371408+00:00 · **Legacy report time:** 2026-11-18T18:53:21.384270+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INFI/USD ⭐ | 0.1342 | 107.10 | +7.58% | 3.69x | STRONG 100/100 | VERY_HIGH 77/100 | Watch |
| 2 | SENT/USD | 0.019883 | 85.11 | -0.65% | 2.82x | STRONG 73/100 | VERY_HIGH 73/100 | Watch |
| 3 | STABLE/USD | 0.02341 | 57.99 | +0.60% | 0.18x | MODERATE 49/100 | EXTREME 94/100 | Do nothing |
| 4 | AKT/USD ⭐ | 0.5108 | 46.14 | +0.79% | 4.31x | STRONG 83/100 | HIGH 66/100 | Consider small entry |
| 5 | NIGHT/USD | 0.04508 | 44.88 | -0.13% | 0.80x | WEAK 27/100 | HIGH 68/100 | Do nothing |
| 6 | MNT/USD | 0.3851 | 41.88 | -0.05% | 0.20x | WEAK 26/100 | VERY_HIGH 81/100 | Do nothing |
| 7 | W/USD ⭐ | 0.00899 | 37.59 | +0.90% | 1.27x | MODERATE 59/100 | VERY_HIGH 73/100 | Watch |
| 8 | UAI/USD | 0.03357 | 30.98 | +0.48% | 0.82x | MODERATE 45/100 | VERY_HIGH 74/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INFI/USD ⭐ | 0.1342 | 86.69 | +7.58% | 3.69x | 3680 | STRONG 98/100 | EXTREME 89/100 | Do nothing |
| 2 | TRX/USD | 0.30846 | 44.63 | +0.07% | 1.05x | 4158 | MODERATE 47/100 | HIGH 62/100 | Watch |
| 3 | AKT/USD ⭐ | 0.5108 | 37.10 | +0.79% | 4.31x | 4476 | STRONG 79/100 | HIGH 66/100 | Consider small entry |
| 4 | W/USD ⭐ | 0.00899 | 20.94 | +0.90% | 1.27x | 1000 | MODERATE 45/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** INFI/USD, AKT/USD, W/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
