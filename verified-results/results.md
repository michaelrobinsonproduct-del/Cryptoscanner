# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T06:01:27.409805+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45337139123
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 32f92e7ce3ce811ec1ea5e3e66e7d6fbb1deb968 (atomic ledger/results publication)
**Ledger generation:** 1534 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEPE/USD | 3.573e-06 | 94.644 | 78.527 | +4.41% | +0.22% | 2.66x | 5.6 | 2026-11-24T06:01:21.233547+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | NEAR/USD | 3.0438 | 84.123 | 67.397 | +2.10% | +0.35% | 3.40x | 4.6 | 2026-11-24T06:01:21.233547+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | VVV/USD | 25.269 | 74.229 | 76.727 | +3.36% | +0.68% | 0.41x | 3.6 | 2026-11-24T06:01:21.233547+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.3278 | 70.204 | 64.005 | +6.05% | +1.45% | 0.90x | 21.4 | 2026-11-24T06:01:21.233547+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | XRP/USD | 0.95374 | 66.091 | 65.326 | +1.53% | -0.28% | 1.22x | 0.7 | 2026-11-24T06:01:21.233547+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XMR/USD | 494.89 | 65.926 | 63.424 | +1.82% | +0.25% | 1.12x | 8.7 | 2026-11-24T06:01:21.233547+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6765 | 55.796 | 57.056 | +0.51% | -0.13% | 0.94x | 3.0 | 2026-11-24T06:01:21.233547+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | LTC/USD | 41.94 | 55.383 | 61.397 | +1.26% | -0.05% | 0.42x | 4.8 | 2026-11-24T06:01:21.233547+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | LINK/USD | 9.10439 | 54.538 | 59.710 | +1.10% | -0.05% | 0.51x | 6.0 | 2026-11-24T06:01:21.233547+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | HYPE/USD | 64.26 | 51.971 | 60.263 | +0.97% | +0.00% | 0.17x | 3.1 | 2026-11-24T06:01:21.233547+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0566364 | 49.312 | 57.123 | +0.59% | -0.14% | 0.29x | 4.0 | 2026-11-24T06:01:21.233547+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | AVAX/USD | 6.811 | 47.679 | 47.237 | +0.50% | -0.16% | 1.12x | 4.4 | 2026-11-24T06:01:21.233547+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEPE/USD | 78.527 | 3.573e-06 | +0.22% | 2.66x |
| 2 | VVV/USD | 76.727 | 25.269 | +0.68% | 0.41x |
| 3 | NEAR/USD | 67.397 | 3.0438 | +0.35% | 3.40x |
| 4 | XRP/USD | 65.326 | 0.95374 | -0.28% | 1.22x |
| 5 | ICNT/USD | 64.005 | 0.3278 | +1.45% | 0.90x |
| 6 | XMR/USD | 63.424 | 494.89 | +0.25% | 1.12x |
| 7 | LTC/USD | 61.397 | 41.94 | -0.05% | 0.42x |
| 8 | HYPE/USD | 60.263 | 64.26 | +0.00% | 0.17x |
| 9 | LINK/USD | 59.710 | 9.10439 | -0.05% | 0.51x |
| 10 | XDG/USD | 57.123 | 0.0566364 | -0.14% | 0.29x |
| 11 | SUI/USD | 57.056 | 0.6765 | -0.13% | 0.94x |
| 12 | AVAX/USD | 47.237 | 6.811 | -0.16% | 1.12x |

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

- Persisted scans: 1534; predictions: 13141; observations: 929304.
- Matured sampled outcomes across 1/6/24/48h: 24641; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 136 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45337139123 · **Generation:** 1534 · **Legacy run:** 45337139123
**Main quote time:** 2026-11-24T06:01:27.409805+00:00 · **Legacy report time:** 2026-11-24T06:02:24.813964+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.573e-06 | 94.64 | +0.22% | 2.66x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.0438 | 84.12 | +0.35% | 3.40x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD | 25.269 | 74.23 | +0.68% | 0.41x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 4 | ICNT/USD | 0.3278 | 70.20 | +1.45% | 0.90x | MODERATE 55/100 | VERY_HIGH 79/100 | Watch |
| 5 | XRP/USD | 0.95374 | 66.09 | -0.28% | 1.22x | WEAK 43/100 | HIGH 68/100 | Watch |
| 6 | XMR/USD ⭐ | 494.89 | 65.93 | +0.25% | 1.12x | STRONG 78/100 | HIGH 62/100 | Watch |
| 7 | SUI/USD | 0.6765 | 55.80 | -0.13% | 0.94x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 8 | LTC/USD | 41.94 | 55.38 | -0.05% | 0.42x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | LINK/USD | 9.10439 | 54.54 | -0.05% | 0.51x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | HYPE/USD | 64.26 | 51.97 | +0.00% | 0.17x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 11 | XDG/USD | 0.0566364 | 49.31 | -0.14% | 0.29x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | AVAX/USD | 6.811 | 47.68 | -0.16% | 1.12x | WEAK 34/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD ⭐ | 3.558e-06 | 89.27 | +0.22% | 2.66x | 9196 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | BAT/USD | 0.08013 | 77.62 | +0.10% | 3.64x | 3223 | STRONG 74/100 | VERY_HIGH 72/100 | Watch |
| 3 | NEAR/USD ⭐ | 3.0344 | 72.56 | +0.35% | 3.40x | 23202 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XMR/USD ⭐ | 494.06 | 59.73 | +0.25% | 1.12x | 11738 | STRONG 75/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PEPE/USD, NEAR/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
