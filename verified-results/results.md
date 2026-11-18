# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T20:55:15.752277+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44395933150
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** aad6aeec62d1ec15dc6cec7b8f3c467b5a31b748 (atomic ledger/results publication)
**Ledger generation:** 665 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | WINGS/USD | 0.001949 | 88.668 | 65.766 | +6.33% | +4.90% | 0.84x | 20.5 | 2026-11-18T20:55:12.328893+00:00 | Not calibrated | MODERATE 64/100 | EXTREME 89/100 | Do nothing | WATCH |
| 2 | SENT/USD | 0.020104 | 72.939 | 74.432 | +7.69% | +0.46% | 0.62x | 3.5 | 2026-11-18T20:55:12.328893+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | TRX/USD | 0.308689 | 57.230 | 41.944 | +0.26% | +0.06% | 2.61x | 0.0 | 2026-11-18T20:55:12.328893+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 4 | UAI/USD | 0.03377 | 41.983 | 31.676 | +1.17% | -0.94% | 5.97x | 14.8 | 2026-11-18T20:55:12.328893+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 79/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 74.432 | 0.020104 | +0.46% | 0.62x |
| 2 | WINGS/USD | 65.766 | 0.001949 | +4.90% | 0.84x |
| 3 | TRX/USD | 41.944 | 0.308689 | +0.06% | 2.61x |
| 4 | UAI/USD | 31.676 | 0.03377 | -0.94% | 5.97x |

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

- Persisted scans: 665; predictions: 5520; observations: 401992.
- Matured sampled outcomes across 1/6/24/48h: 5094; gap abstentions: 13137. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 7 (sampled only; not a success-rate estimate).
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

**Writer:** 44395933150 · **Generation:** 665 · **Legacy run:** 44395933150
**Main quote time:** 2026-11-18T20:55:15.752277+00:00 · **Legacy report time:** 2026-11-18T20:55:52.474881+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | WINGS/USD | 0.001949 | 88.67 | +4.90% | 0.84x | MODERATE 64/100 | EXTREME 89/100 | Do nothing |
| 2 | SENT/USD | 0.020104 | 72.94 | +0.46% | 0.62x | MODERATE 66/100 | VERY_HIGH 82/100 | Watch |
| 3 | TRX/USD ⭐ | 0.308689 | 57.23 | +0.06% | 2.61x | STRONG 84/100 | HIGH 55/100 | Watch |
| 4 | UAI/USD | 0.03377 | 41.98 | -0.94% | 5.97x | MODERATE 46/100 | VERY_HIGH 79/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRX/USD ⭐ | 0.308689 | 52.70 | +0.06% | 2.61x | 4010 | STRONG 81/100 | HIGH 55/100 | Watch |

**Same-run overlap:** TRX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
