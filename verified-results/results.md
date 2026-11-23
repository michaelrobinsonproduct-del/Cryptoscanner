# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T13:21:51.839725+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45182798870
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** e62a475e4c8e824aa52fcce57e59fd00bd2aa608 (atomic ledger/results publication)
**Ledger generation:** 1435 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 2.255 | 101.255 | 83.948 | +9.76% | +0.46% | 16.95x | 12.8 | 2026-11-23T13:21:43.445771+00:00 | Not calibrated | STRONG 100/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | SUI/USD | 0.6693 | 85.421 | 68.772 | +2.07% | +0.33% | 2.53x | 1.5 | 2026-11-23T13:21:43.445771+00:00 | Not calibrated | STRONG 98/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ALGO/USD | 0.08363 | 84.004 | 78.013 | +10.87% | -0.11% | 1.65x | 6.0 | 2026-11-23T13:21:43.445771+00:00 | Not calibrated | MODERATE 62/100 | HIGH 66/100 | Watch | WATCH |
| 4 | QNT/USD | 157.25 | 82.536 | 86.963 | +9.63% | +0.47% | 0.32x | 12.1 | 2026-11-23T13:21:43.445771+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | GRT/USD | 0.01697 | 81.287 | 67.758 | +6.13% | +1.06% | 1.82x | 11.8 | 2026-11-23T13:21:43.445771+00:00 | Not calibrated | STRONG 81/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | XMR/USD | 503.29 | 76.343 | 65.497 | +1.94% | +0.11% | 2.03x | 6.2 | 2026-11-23T13:21:43.445771+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 7 | HYPE/USD | 64.03 | 70.995 | 64.987 | +1.54% | +0.31% | 1.44x | 1.6 | 2026-11-23T13:21:43.445771+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 8 | SOL/USD | 72.48 | 70.630 | 72.645 | +2.62% | +0.33% | 0.63x | 1.4 | 2026-11-23T13:21:43.445771+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | CC/USD | 0.07682 | 66.931 | 67.503 | +4.85% | +0.07% | 0.91x | 2.6 | 2026-11-23T13:21:43.445771+00:00 | Not calibrated | MODERATE 53/100 | HIGH 67/100 | Watch | WATCH |
| 10 | XLM/USD | 0.128762 | 64.665 | 58.356 | +0.97% | +0.23% | 1.51x | 0.1 | 2026-11-23T13:21:43.445771+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XRP/USD | 0.94477 | 64.531 | 67.633 | +1.86% | +0.35% | 0.52x | 0.7 | 2026-11-23T13:21:43.445771+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | UAI/USD | 0.03181 | 59.781 | 67.931 | +7.58% | +0.16% | 0.11x | 15.8 | 2026-11-23T13:21:43.445771+00:00 | Not calibrated | MODERATE 45/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 86.963 | 157.25 | +0.47% | 0.32x |
| 2 | PEARL/USD | 83.948 | 2.255 | +0.46% | 16.95x |
| 3 | ALGO/USD | 78.013 | 0.08363 | -0.11% | 1.65x |
| 4 | SOL/USD | 72.645 | 72.48 | +0.33% | 0.63x |
| 5 | SUI/USD | 68.772 | 0.6693 | +0.33% | 2.53x |
| 6 | UAI/USD | 67.931 | 0.03181 | +0.16% | 0.11x |
| 7 | GRT/USD | 67.758 | 0.01697 | +1.06% | 1.82x |
| 8 | XRP/USD | 67.633 | 0.94477 | +0.35% | 0.52x |
| 9 | CC/USD | 67.503 | 0.07682 | +0.07% | 0.91x |
| 10 | XMR/USD | 65.497 | 503.29 | +0.11% | 2.03x |
| 11 | HYPE/USD | 64.987 | 64.03 | +0.31% | 1.44x |
| 12 | XLM/USD | 58.356 | 0.128762 | +0.23% | 1.51x |

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

- Persisted scans: 1435; predictions: 11987; observations: 869017.
- Matured sampled outcomes across 1/6/24/48h: 20191; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45182798870 · **Generation:** 1435 · **Legacy run:** 45182798870
**Main quote time:** 2026-11-23T13:21:51.839725+00:00 · **Legacy report time:** 2026-11-23T13:22:56.411122+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 2.255 | 101.26 | +0.46% | 16.95x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | SUI/USD ⭐ | 0.6693 | 85.42 | +0.33% | 2.53x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ALGO/USD | 0.08363 | 84.00 | -0.11% | 1.65x | MODERATE 62/100 | HIGH 66/100 | Watch |
| 4 | QNT/USD | 157.25 | 82.54 | +0.47% | 0.32x | MODERATE 66/100 | VERY_HIGH 76/100 | Watch |
| 5 | GRT/USD | 0.01697 | 81.29 | +1.06% | 1.82x | STRONG 81/100 | VERY_HIGH 73/100 | Watch |
| 6 | XMR/USD | 503.29 | 76.34 | +0.11% | 2.03x | STRONG 83/100 | HIGH 55/100 | Watch |
| 7 | HYPE/USD | 64.03 | 70.99 | +0.31% | 1.44x | STRONG 80/100 | HIGH 55/100 | Watch |
| 8 | SOL/USD | 72.48 | 70.63 | +0.33% | 0.63x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 9 | CC/USD | 0.07682 | 66.93 | +0.07% | 0.91x | MODERATE 53/100 | HIGH 67/100 | Watch |
| 10 | XLM/USD | 0.128762 | 64.66 | +0.23% | 1.51x | STRONG 77/100 | HIGH 55/100 | Watch |
| 11 | XRP/USD | 0.94477 | 64.53 | +0.35% | 0.52x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 12 | UAI/USD | 0.03181 | 59.78 | +0.16% | 0.11x | MODERATE 45/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 2.2619 | 88.64 | +0.46% | 16.95x | 8883 | STRONG 99/100 | HIGH 67/100 | Consider small entry |
| 2 | CCD/USD | 0.002904 | 81.16 | +0.87% | 4.70x | 3027 | STRONG 91/100 | VERY_HIGH 73/100 | Watch |
| 3 | SUI/USD ⭐ | 0.6693 | 81.02 | +0.33% | 2.53x | 5802 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | INJ/USD | 6.437 | 76.44 | +0.52% | 1.22x | 4196 | STRONG 73/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PEARL/USD, SUI/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
