# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T09:07:52.040961+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46128743036
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 96e7f416becc4dd27999d7eb396b0c5722733f66 (atomic ledger/results publication)
**Ledger generation:** 2133 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 9.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SPACE/USD | 0.004625 | 115.367 | 75.557 | +10.70% | +4.96% | 203.32x | 2.2 | 2026-11-28T09:07:48.828730+00:00 | Not calibrated | STRONG 100/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.05163 | 87.250 | 69.516 | +2.77% | +0.55% | 10.31x | 9.7 | 2026-11-28T09:07:48.828730+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | VVV/USD | 26.405 | 52.837 | 58.142 | +2.55% | +0.20% | 0.37x | 8.3 | 2026-11-28T09:07:48.828730+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | CC/USD | 0.07468 | 31.124 | 35.751 | +0.71% | -0.20% | 0.64x | 6.7 | 2026-11-28T09:07:48.828730+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SPACE/USD | 75.557 | 0.004625 | +4.96% | 203.32x |
| 2 | NIGHT/USD | 69.516 | 0.05163 | +0.55% | 10.31x |
| 3 | VVV/USD | 58.142 | 26.405 | +0.20% | 0.37x |
| 4 | CC/USD | 35.751 | 0.07468 | -0.20% | 0.64x |

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

- Persisted scans: 2133; predictions: 19077; observations: 1291644.
- Matured sampled outcomes across 1/6/24/48h: 45042; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46128743036 · **Generation:** 2133 · **Legacy run:** 46128743036
**Main quote time:** 2026-11-28T09:07:52.040961+00:00 · **Legacy report time:** 2026-11-28T09:08:39.592676+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SPACE/USD ⭐ | 0.004625 | 115.37 | +4.96% | 203.32x | STRONG 100/100 | VERY_HIGH 77/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.05163 | 87.25 | +0.55% | 10.31x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD | 26.405 | 52.84 | +0.20% | 0.37x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 4 | CC/USD | 0.07468 | 31.12 | -0.20% | 0.64x | WEAK 21/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SPACE/USD ⭐ | 0.00462 | 86.98 | +4.96% | 203.32x | 3216 | STRONG 100/100 | VERY_HIGH 83/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.05154 | 77.69 | +0.55% | 10.31x | 19273 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | W/USD | 0.00922 | 16.34 | +0.76% | 1.25x | 1271 | WEAK 38/100 | HIGH 66/100 | Watch |

**Same-run overlap:** SPACE/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
