# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T20:50:16.169241+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44395058221
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 77cd43ec8859417e0ee1f92289c3a9602bff666b (atomic ledger/results publication)
**Ledger generation:** 664 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | WINGS/USD | 0.00193 | 74.214 | 61.125 | +5.29% | +2.93% | 0.84x | 15.3 | 2026-11-18T20:50:12.646304+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | SENT/USD | 0.019993 | 73.300 | 74.416 | +7.09% | +0.49% | 0.64x | 3.5 | 2026-11-18T20:50:12.646304+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | UAI/USD | 0.03397 | 42.449 | 32.980 | +1.77% | -1.11% | 7.29x | 20.6 | 2026-11-18T20:50:12.646304+00:00 | Not calibrated | WEAK 41/100 | EXTREME 89/100 | Do nothing | WATCH |
| 4 | AKE/USD | 0.01021157 | 33.018 | 39.536 | +2.28% | -0.25% | 0.47x | 21.9 | 2026-11-18T20:50:12.646304+00:00 | Not calibrated | WEAK 12/100 | EXTREME 93/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 74.416 | 0.019993 | +0.49% | 0.64x |
| 2 | WINGS/USD | 61.125 | 0.00193 | +2.93% | 0.84x |
| 3 | AKE/USD | 39.536 | 0.01021157 | -0.25% | 0.47x |
| 4 | UAI/USD | 32.980 | 0.03397 | -1.11% | 7.29x |

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

- Persisted scans: 664; predictions: 5516; observations: 401383.
- Matured sampled outcomes across 1/6/24/48h: 5079; gap abstentions: 13137. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 6 (sampled only; not a success-rate estimate).
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

**Writer:** 44395058221 · **Generation:** 664 · **Legacy run:** 44395058221
**Main quote time:** 2026-11-18T20:50:16.169241+00:00 · **Legacy report time:** 2026-11-18T20:50:52.921023+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | WINGS/USD | 0.00193 | 74.21 | +2.93% | 0.84x | MODERATE 62/100 | VERY_HIGH 73/100 | Watch |
| 2 | SENT/USD | 0.019993 | 73.30 | +0.49% | 0.64x | MODERATE 67/100 | VERY_HIGH 82/100 | Watch |
| 3 | UAI/USD | 0.03397 | 42.45 | -1.11% | 7.29x | WEAK 41/100 | EXTREME 89/100 | Do nothing |
| 4 | AKE/USD | 0.01021157 | 33.02 | -0.25% | 0.47x | WEAK 12/100 | EXTREME 93/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRX/USD | 0.308449 | 45.55 | +0.07% | 1.54x | 4004 | MODERATE 58/100 | HIGH 55/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
