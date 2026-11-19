# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T01:50:32.548850+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44439794214
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 02a1444c609c8fc846eb95b1774ab6aeafc4f0c2 (atomic ledger/results publication)
**Ledger generation:** 723 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021619 | 64.772 | 62.453 | +4.92% | +1.79% | 0.34x | 6.9 | 2026-11-19T01:50:24.223418+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | TRX/USD | 0.310471 | 57.823 | 41.941 | +0.38% | +0.18% | 6.29x | 0.0 | 2026-11-19T01:50:24.223418+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 3 | PROS/USD | 0.6892 | 49.874 | 34.618 | +2.90% | +3.25% | 0.90x | 34.7 | 2026-11-19T01:50:24.223418+00:00 | Not calibrated | MODERATE 45/100 | EXTREME 89/100 | Do nothing | WATCH |
| 4 | DRV/USD | 0.26626 | 46.389 | 31.614 | +0.59% | -0.04% | 4.39x | 11.7 | 2026-11-19T01:50:24.223418+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | PYTH/USD | 0.05362 | 39.640 | 34.738 | +1.63% | +0.90% | 1.04x | 16.8 | 2026-11-19T01:50:24.223418+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | BAT/USD | 0.09342 | 39.038 | 31.384 | +0.43% | +0.60% | 1.46x | 5.4 | 2026-11-19T01:50:24.223418+00:00 | Not calibrated | MODERATE 65/100 | HIGH 67/100 | Watch | WATCH |
| 7 | MEGA/USD | 0.05707 | 37.690 | 36.704 | +1.91% | -0.44% | 1.32x | 15.8 | 2026-11-19T01:50:24.223418+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 8 | PAXG/USD | 3743.04 | 36.741 | 43.665 | +0.32% | +0.30% | 0.16x | 1.8 | 2026-11-19T01:50:24.223418+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 62.453 | 0.021619 | +1.79% | 0.34x |
| 2 | PAXG/USD | 43.665 | 3743.04 | +0.30% | 0.16x |
| 3 | TRX/USD | 41.941 | 0.310471 | +0.18% | 6.29x |
| 4 | MEGA/USD | 36.704 | 0.05707 | -0.44% | 1.32x |
| 5 | PYTH/USD | 34.738 | 0.05362 | +0.90% | 1.04x |
| 6 | PROS/USD | 34.618 | 0.6892 | +3.25% | 0.90x |
| 7 | DRV/USD | 31.614 | 0.26626 | -0.04% | 4.39x |
| 8 | BAT/USD | 31.384 | 0.09342 | +0.60% | 1.46x |

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

- Persisted scans: 723; predictions: 5864; observations: 437314.
- Matured sampled outcomes across 1/6/24/48h: 5784; gap abstentions: 13463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44439794214 · **Generation:** 723 · **Legacy run:** 44439794214
**Main quote time:** 2026-11-19T01:50:32.548850+00:00 · **Legacy report time:** 2026-11-19T01:51:18.735808+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.021619 | 64.77 | +1.79% | 0.34x | MODERATE 62/100 | VERY_HIGH 82/100 | Watch |
| 2 | TRX/USD ⭐ | 0.310471 | 57.82 | +0.18% | 6.29x | STRONG 84/100 | HIGH 55/100 | Watch |
| 3 | PROS/USD | 0.6892 | 49.87 | +3.25% | 0.90x | MODERATE 45/100 | EXTREME 89/100 | Do nothing |
| 4 | DRV/USD | 0.26626 | 46.39 | -0.04% | 4.39x | MODERATE 48/100 | VERY_HIGH 72/100 | Watch |
| 5 | PYTH/USD ⭐ | 0.05362 | 39.64 | +0.90% | 1.04x | MODERATE 60/100 | VERY_HIGH 73/100 | Watch |
| 6 | BAT/USD | 0.09342 | 39.04 | +0.60% | 1.46x | MODERATE 65/100 | HIGH 67/100 | Watch |
| 7 | MEGA/USD | 0.05707 | 37.69 | -0.44% | 1.32x | WEAK 34/100 | VERY_HIGH 79/100 | Do nothing |
| 8 | PAXG/USD | 3743.04 | 36.74 | +0.30% | 0.16x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRX/USD ⭐ | 0.310471 | 54.48 | +0.18% | 6.29x | 4101 | STRONG 82/100 | HIGH 55/100 | Watch |
| 2 | LTC/USD | 44.08 | 46.08 | +0.57% | 2.19x | 11742 | STRONG 78/100 | HIGH 55/100 | Watch |
| 3 | PYTH/USD ⭐ | 0.05362 | 39.77 | +0.90% | 1.04x | 1956 | MODERATE 60/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** TRX/USD, PYTH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
