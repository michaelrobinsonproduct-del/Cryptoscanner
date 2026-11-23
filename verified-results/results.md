# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T02:11:34.684230+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45098574326
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 2a3f7ce12407b0582e855c4434efc2c5e64b3e38 (atomic ledger/results publication)
**Ledger generation:** 1366 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CC/USD | 0.07402 | 54.122 | 38.039 | +1.02% | +0.22% | 5.00x | 9.5 | 2026-11-23T02:11:30.284797+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Watch | WATCH |
| 2 | AUD/USD | 0.66373 | 53.841 | 39.037 | +0.33% | -0.04% | 7.41x | 5.6 | 2026-11-23T02:11:30.284797+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 3 | BLESS/USD | 0.016609 | 44.947 | 41.270 | +3.21% | -1.02% | 1.88x | 39.2 | 2026-11-23T02:11:30.284797+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 4 | DRV/USD | 0.37749 | 39.486 | 52.996 | +2.34% | -1.82% | 0.56x | 16.7 | 2026-11-23T02:11:30.284797+00:00 | Not calibrated | WEAK 20/100 | EXTREME 86/100 | Do nothing | WATCH |
| 5 | PEARL/USD | 2.0904 | 34.531 | 38.620 | +1.75% | -0.45% | 0.81x | 29.7 | 2026-11-23T02:11:30.284797+00:00 | Not calibrated | WEAK 12/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 6 | ICNT/USD | 0.3595 | 29.868 | 30.825 | +2.07% | +1.21% | 0.30x | 33.5 | 2026-11-23T02:11:30.284797+00:00 | Not calibrated | WEAK 35/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 52.996 | 0.37749 | -1.82% | 0.56x |
| 2 | BLESS/USD | 41.270 | 0.016609 | -1.02% | 1.88x |
| 3 | AUD/USD | 39.037 | 0.66373 | -0.04% | 7.41x |
| 4 | PEARL/USD | 38.620 | 2.0904 | -0.45% | 0.81x |
| 5 | CC/USD | 38.039 | 0.07402 | +0.22% | 5.00x |
| 6 | ICNT/USD | 30.825 | 0.3595 | +1.21% | 0.30x |

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

- Persisted scans: 1366; predictions: 11208; observations: 827000.
- Matured sampled outcomes across 1/6/24/48h: 17860; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 80 (sampled only; not a success-rate estimate).
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

**Writer:** 45098574326 · **Generation:** 1366 · **Legacy run:** 45098574326
**Main quote time:** 2026-11-23T02:11:34.684230+00:00 · **Legacy report time:** 2026-11-23T02:12:43.610088+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.07402 | 54.12 | +0.22% | 5.00x | STRONG 92/100 | HIGH 60/100 | Consider small entry |
| 2 | AUD/USD | 0.66373 | 53.84 | -0.04% | 7.41x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 3 | BLESS/USD | 0.016609 | 44.95 | -1.02% | 1.88x | WEAK 27/100 | VERY_HIGH 77/100 | Do nothing |
| 4 | DRV/USD | 0.37749 | 39.49 | -1.82% | 0.56x | WEAK 20/100 | EXTREME 86/100 | Do nothing |
| 5 | PEARL/USD | 2.0904 | 34.53 | -0.45% | 0.81x | WEAK 12/100 | VERY_HIGH 80/100 | Do nothing |
| 6 | ICNT/USD | 0.3595 | 29.87 | +1.21% | 0.30x | WEAK 35/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.07402 | 50.50 | +0.22% | 5.00x | 3726 | STRONG 90/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
