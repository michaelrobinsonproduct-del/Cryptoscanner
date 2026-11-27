# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T20:27:52.683305+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46063028860
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7a7e7ee0fa27f846710203f5fb64cf9f10d793ff (atomic ledger/results publication)
**Ledger generation:** 2056 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 739.37 | 109.435 | 98.716 | +8.47% | -0.45% | 2.29x | 2.6 | 2026-11-27T20:27:44.431511+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | HYPE/USD | 63.95 | 83.099 | 72.900 | +2.78% | +0.19% | 1.93x | 3.1 | 2026-11-27T20:27:44.431511+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.05032 | 82.770 | 80.724 | +3.82% | -0.40% | 1.40x | 2.0 | 2026-11-27T20:27:44.431511+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SKY/USD | 0.05009 | 76.632 | 73.511 | +7.93% | +0.49% | 1.07x | 14.0 | 2026-11-27T20:27:44.431511+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6716 | 72.676 | 58.344 | +0.58% | -0.13% | 4.05x | 1.5 | 2026-11-27T20:27:44.431511+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 6 | UNI/USD | 4.8349 | 69.680 | 78.222 | +3.97% | -0.06% | 0.17x | 4.6 | 2026-11-27T20:27:44.431511+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0575501 | 67.330 | 69.484 | +2.09% | -0.18% | 0.88x | 0.2 | 2026-11-27T20:27:44.431511+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 8 | SOL/USD | 71.98 | 64.449 | 64.567 | +1.47% | -0.03% | 1.00x | 1.4 | 2026-11-27T20:27:44.431511+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 9 | RENDER/USD | 1.402 | 60.955 | 62.040 | +5.18% | +0.50% | 0.64x | 14.3 | 2026-11-27T20:27:44.431511+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 10 | JUP/USD | 0.24806 | 60.846 | 62.407 | +4.86% | -0.03% | 0.86x | 9.3 | 2026-11-27T20:27:44.431511+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 11 | PAXG/USD | 3642.07 | 57.056 | 59.060 | +2.40% | -0.05% | 0.82x | 1.6 | 2026-11-27T20:27:44.431511+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | FET/USD | 0.1262 | 55.149 | 62.622 | +4.82% | -0.16% | 0.33x | 15.9 | 2026-11-27T20:27:44.431511+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.716 | 739.37 | -0.45% | 2.29x |
| 2 | NIGHT/USD | 80.724 | 0.05032 | -0.40% | 1.40x |
| 3 | UNI/USD | 78.222 | 4.8349 | -0.06% | 0.17x |
| 4 | SKY/USD | 73.511 | 0.05009 | +0.49% | 1.07x |
| 5 | HYPE/USD | 72.900 | 63.95 | +0.19% | 1.93x |
| 6 | XDG/USD | 69.484 | 0.0575501 | -0.18% | 0.88x |
| 7 | SOL/USD | 64.567 | 71.98 | -0.03% | 1.00x |
| 8 | FET/USD | 62.622 | 0.1262 | -0.16% | 0.33x |
| 9 | JUP/USD | 62.407 | 0.24806 | -0.03% | 0.86x |
| 10 | RENDER/USD | 62.040 | 1.402 | +0.50% | 0.64x |
| 11 | PAXG/USD | 59.060 | 3642.07 | -0.05% | 0.82x |
| 12 | SUI/USD | 58.344 | 0.6716 | -0.13% | 4.05x |

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

- Persisted scans: 2056; predictions: 18374; observations: 1244989.
- Matured sampled outcomes across 1/6/24/48h: 41567; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
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

**Writer:** 46063028860 · **Generation:** 2056 · **Legacy run:** 46063028860
**Main quote time:** 2026-11-27T20:27:52.683305+00:00 · **Legacy report time:** 2026-11-27T20:28:49.547677+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 739.37 | 109.44 | -0.45% | 2.29x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | HYPE/USD ⭐ | 63.95 | 83.10 | +0.19% | 1.93x | STRONG 87/100 | HIGH 55/100 | Watch |
| 3 | NIGHT/USD | 0.05032 | 82.77 | -0.40% | 1.40x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 4 | SKY/USD ⭐ | 0.05009 | 76.63 | +0.49% | 1.07x | STRONG 78/100 | VERY_HIGH 73/100 | Watch |
| 5 | SUI/USD | 0.6716 | 72.68 | -0.13% | 4.05x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 6 | UNI/USD | 4.8349 | 69.68 | -0.06% | 0.17x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 7 | XDG/USD | 0.0575501 | 67.33 | -0.18% | 0.88x | WEAK 39/100 | HIGH 68/100 | Watch |
| 8 | SOL/USD | 71.98 | 64.45 | -0.03% | 1.00x | WEAK 42/100 | HIGH 68/100 | Watch |
| 9 | RENDER/USD | 1.402 | 60.95 | +0.50% | 0.64x | MODERATE 55/100 | VERY_HIGH 81/100 | Watch |
| 10 | JUP/USD | 0.24806 | 60.85 | -0.03% | 0.86x | WEAK 35/100 | VERY_HIGH 73/100 | Watch |
| 11 | PAXG/USD | 3642.07 | 57.06 | -0.05% | 0.82x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 12 | FET/USD | 0.1262 | 55.15 | -0.16% | 0.33x | WEAK 28/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 63.95 | 86.51 | +0.19% | 1.93x | 20084 | STRONG 88/100 | HIGH 55/100 | Watch |
| 2 | SKY/USD ⭐ | 0.05011 | 78.07 | +0.49% | 1.07x | 6587 | STRONG 84/100 | HIGH 67/100 | Watch |

**Same-run overlap:** HYPE/USD, SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
