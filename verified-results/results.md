# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T14:31:56.388863+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45414678776
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e137b356b364c6069ea27b2207533a0f8240738c (atomic ledger/results publication)
**Ledger generation:** 1586 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 498.22 | 83.092 | 66.935 | +2.51% | +0.23% | 7.14x | 11.3 | 2026-11-24T14:31:51.369540+00:00 | Not calibrated | STRONG 92/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 25.517 | 80.941 | 79.521 | +4.37% | +0.24% | 1.02x | 12.2 | 2026-11-24T14:31:51.369540+00:00 | Not calibrated | STRONG 70/100 | HIGH 68/100 | Watch | WATCH |
| 3 | 2Z/USD | 0.01627 | 71.329 | 55.407 | +3.96% | +0.18% | 4.10x | 6.2 | 2026-11-24T14:31:51.369540+00:00 | Not calibrated | STRONG 81/100 | HIGH 67/100 | Watch | WATCH |
| 4 | GBP/USD | 1.30998 | 65.080 | 58.462 | +0.52% | +0.04% | 1.64x | 0.3 | 2026-11-24T14:31:51.369540+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 5 | AUD/USD | 0.66432 | 48.283 | 43.518 | +0.26% | +0.03% | 1.46x | 0.9 | 2026-11-24T14:31:51.369540+00:00 | Not calibrated | MODERATE 59/100 | HIGH 55/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.04832 | 41.732 | 45.447 | +0.35% | -0.08% | 0.67x | 2.1 | 2026-11-24T14:31:51.369540+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | Q/USD | 0.026766 | 41.376 | 39.427 | +3.47% | -0.60% | 1.49x | 31.1 | 2026-11-24T14:31:51.369540+00:00 | Not calibrated | WEAK 31/100 | EXTREME 85/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 79.521 | 25.517 | +0.24% | 1.02x |
| 2 | XMR/USD | 66.935 | 498.22 | +0.23% | 7.14x |
| 3 | GBP/USD | 58.462 | 1.30998 | +0.04% | 1.64x |
| 4 | 2Z/USD | 55.407 | 0.01627 | +0.18% | 4.10x |
| 5 | NIGHT/USD | 45.447 | 0.04832 | -0.08% | 0.67x |
| 6 | AUD/USD | 43.518 | 0.66432 | +0.03% | 1.46x |
| 7 | Q/USD | 39.427 | 0.026766 | -0.60% | 1.49x |

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

- Persisted scans: 1586; predictions: 13675; observations: 960969.
- Matured sampled outcomes across 1/6/24/48h: 26901; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 143 (sampled only; not a success-rate estimate).
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

**Writer:** 45414678776 · **Generation:** 1586 · **Legacy run:** 45414678776
**Main quote time:** 2026-11-24T14:31:56.388863+00:00 · **Legacy report time:** 2026-11-24T14:32:58.024141+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 498.22 | 83.09 | +0.23% | 7.14x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 25.517 | 80.94 | +0.24% | 1.02x | STRONG 80/100 | HIGH 68/100 | Watch |
| 3 | 2Z/USD ⭐ | 0.01627 | 71.33 | +0.18% | 4.10x | STRONG 91/100 | HIGH 67/100 | Watch |
| 4 | GBP/USD | 1.30998 | 65.08 | +0.04% | 1.64x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 5 | AUD/USD | 0.66432 | 48.28 | +0.03% | 1.46x | MODERATE 59/100 | HIGH 55/100 | Watch |
| 6 | NIGHT/USD | 0.04832 | 41.73 | -0.08% | 0.67x | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | Q/USD | 0.026766 | 41.38 | -0.60% | 1.49x | WEAK 31/100 | EXTREME 85/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 25.474 | 85.81 | +0.24% | 1.02x | 13202 | STRONG 88/100 | HIGH 62/100 | Watch |
| 2 | XMR/USD ⭐ | 495.79 | 69.82 | +0.23% | 7.14x | 9988 | STRONG 95/100 | HIGH 61/100 | Consider small entry |
| 3 | 2Z/USD ⭐ | 0.0162 | 62.25 | +0.18% | 4.10x | 1329 | STRONG 71/100 | EXTREME 89/100 | Do nothing |

**Same-run overlap:** XMR/USD, VVV/USD, 2Z/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
