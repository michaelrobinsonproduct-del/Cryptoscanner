# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T05:05:04.379749+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44241667956
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 50adfece2c2f68d8c5389795b8d0e63727e56992 (atomic ledger/results publication)
**Ledger generation:** 538 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XDC/USD | 0.03091 | 53.961 | 48.163 | +1.95% | +0.10% | 1.53x | 6.5 | 2026-11-18T05:05:00.234060+00:00 | Not calibrated | MODERATE 62/100 | HIGH 55/100 | Watch | WATCH |
| 2 | PEARL/USD | 1.8427 | 49.509 | 35.962 | +1.78% | -0.03% | 2.37x | 23.0 | 2026-11-18T05:05:00.234060+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 3 | SENT/USD | 0.019225 | 41.711 | 47.369 | +2.98% | -0.43% | 0.65x | 8.8 | 2026-11-18T05:05:00.234060+00:00 | Not calibrated | WEAK 26/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | UP/USD | 0.05501 | 40.259 | 41.512 | +3.81% | -0.83% | 1.29x | 34.6 | 2026-11-18T05:05:00.234060+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 5 | CC/USD | 0.08302 | 34.218 | 40.149 | +1.08% | -0.25% | 0.53x | 6.0 | 2026-11-18T05:05:00.234060+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 6 | MEGA/USD | 0.05214 | 27.656 | 27.512 | +0.97% | +0.12% | 0.96x | 21.1 | 2026-11-18T05:05:00.234060+00:00 | Not calibrated | WEAK 24/100 | EXTREME 86/100 | Do nothing | WATCH |
| 7 | MELANIA/USD | 0.0496 | 23.831 | 23.511 | +1.85% | -1.39% | 1.73x | 40.4 | 2026-11-18T05:05:00.234060+00:00 | Not calibrated | WEAK 17/100 | EXTREME 99/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XDC/USD | 48.163 | 0.03091 | +0.10% | 1.53x |
| 2 | SENT/USD | 47.369 | 0.019225 | -0.43% | 0.65x |
| 3 | UP/USD | 41.512 | 0.05501 | -0.83% | 1.29x |
| 4 | CC/USD | 40.149 | 0.08302 | -0.25% | 0.53x |
| 5 | PEARL/USD | 35.962 | 1.8427 | -0.03% | 2.37x |
| 6 | MEGA/USD | 27.512 | 0.05214 | +0.12% | 0.96x |
| 7 | MELANIA/USD | 23.511 | 0.0496 | -1.39% | 1.73x |

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

- Persisted scans: 538; predictions: 4546; observations: 324649.
- Matured sampled outcomes across 1/6/24/48h: 3614; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44241667956 · **Generation:** 538 · **Legacy run:** 44241667956
**Main quote time:** 2026-11-18T05:05:04.379749+00:00 · **Legacy report time:** 2026-11-18T05:05:25.042412+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XDC/USD ⭐ | 0.03091 | 53.96 | +0.10% | 1.53x | STRONG 72/100 | HIGH 55/100 | Watch |
| 2 | PEARL/USD | 1.8427 | 49.51 | -0.03% | 2.37x | MODERATE 45/100 | VERY_HIGH 78/100 | Watch |
| 3 | SENT/USD | 0.019225 | 41.71 | -0.43% | 0.65x | WEAK 26/100 | EXTREME 88/100 | Do nothing |
| 4 | UP/USD | 0.05501 | 40.26 | -0.83% | 1.29x | WEAK 20/100 | VERY_HIGH 78/100 | Do nothing |
| 5 | CC/USD | 0.08302 | 34.22 | -0.25% | 0.53x | WEAK 22/100 | VERY_HIGH 81/100 | Do nothing |
| 6 | MEGA/USD | 0.05214 | 27.66 | +0.12% | 0.96x | WEAK 24/100 | EXTREME 86/100 | Do nothing |
| 7 | MELANIA/USD | 0.0496 | 23.83 | -1.39% | 1.73x | WEAK 17/100 | EXTREME 99/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDC/USD ⭐ | 0.03091 | 54.48 | +0.10% | 1.53x | 5978 | STRONG 72/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XDC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
