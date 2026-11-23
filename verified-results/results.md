# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T09:31:43.051162+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45147498337
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ef9b985a372b322cbdb26fad3ecdcf0375292fa1 (atomic ledger/results publication)
**Ledger generation:** 1411 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | JUP/USD | 0.24539 | 92.327 | 71.389 | +9.27% | +1.19% | 5.39x | 17.6 | 2026-11-23T09:31:34.549471+00:00 | Not calibrated | STRONG 96/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | SOL/USD | 72.61 | 89.693 | 73.935 | +2.80% | +0.15% | 2.93x | 1.4 | 2026-11-23T09:31:34.549471+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 3 | HYPE/USD | 64.12 | 82.483 | 65.205 | +1.68% | +0.46% | 3.55x | 3.1 | 2026-11-23T09:31:34.549471+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | QNT/USD | 151.19 | 75.744 | 79.614 | +5.40% | +0.51% | 0.36x | 6.0 | 2026-11-23T09:31:34.549471+00:00 | Not calibrated | MODERATE 68/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6698 | 70.964 | 69.306 | +2.15% | -0.07% | 1.20x | 1.5 | 2026-11-23T09:31:34.549471+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XBT/USD | 61590.2 | 69.546 | 59.799 | +0.69% | -0.06% | 2.01x | 0.0 | 2026-11-23T09:31:34.549471+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ALGO/USD | 0.08012 | 69.219 | 73.951 | +6.22% | +0.46% | 0.29x | 7.5 | 2026-11-23T09:31:34.549471+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | XDG/USD | 0.055608 | 67.846 | 52.814 | +0.59% | +0.01% | 14.75x | 0.4 | 2026-11-23T09:31:34.549471+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 9 | XMR/USD | 505.5 | 65.707 | 68.650 | +2.39% | +0.41% | 0.50x | 6.1 | 2026-11-23T09:31:34.549471+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | UAI/USD | 0.03127 | 62.818 | 62.917 | +5.75% | +0.06% | 0.96x | 16.0 | 2026-11-23T09:31:34.549471+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 11 | XRP/USD | 0.93813 | 57.688 | 62.939 | +1.14% | -0.18% | 0.56x | 0.1 | 2026-11-23T09:31:34.549471+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | NEAR/USD | 2.9927 | 56.477 | 56.747 | +0.37% | -0.40% | 1.17x | 1.7 | 2026-11-23T09:31:34.549471+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 79.614 | 151.19 | +0.51% | 0.36x |
| 2 | ALGO/USD | 73.951 | 0.08012 | +0.46% | 0.29x |
| 3 | SOL/USD | 73.935 | 72.61 | +0.15% | 2.93x |
| 4 | JUP/USD | 71.389 | 0.24539 | +1.19% | 5.39x |
| 5 | SUI/USD | 69.306 | 0.6698 | -0.07% | 1.20x |
| 6 | XMR/USD | 68.650 | 505.5 | +0.41% | 0.50x |
| 7 | HYPE/USD | 65.205 | 64.12 | +0.46% | 3.55x |
| 8 | XRP/USD | 62.939 | 0.93813 | -0.18% | 0.56x |
| 9 | UAI/USD | 62.917 | 0.03127 | +0.06% | 0.96x |
| 10 | XBT/USD | 59.799 | 61590.2 | -0.06% | 2.01x |
| 11 | NEAR/USD | 56.747 | 2.9927 | -0.40% | 1.17x |
| 12 | XDG/USD | 52.814 | 0.055608 | +0.01% | 14.75x |

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

- Persisted scans: 1411; predictions: 11699; observations: 854402.
- Matured sampled outcomes across 1/6/24/48h: 19166; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 130 (sampled only; not a success-rate estimate).
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

**Writer:** 45147498337 · **Generation:** 1411 · **Legacy run:** 45147498337
**Main quote time:** 2026-11-23T09:31:43.051162+00:00 · **Legacy report time:** 2026-11-23T09:32:51.715015+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | JUP/USD ⭐ | 0.24539 | 92.33 | +1.19% | 5.39x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | SOL/USD ⭐ | 72.61 | 89.69 | +0.15% | 2.93x | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | HYPE/USD | 64.12 | 82.48 | +0.46% | 3.55x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 4 | QNT/USD | 151.19 | 75.74 | +0.51% | 0.36x | MODERATE 68/100 | VERY_HIGH 70/100 | Watch |
| 5 | SUI/USD | 0.6698 | 70.96 | -0.07% | 1.20x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 6 | XBT/USD | 61590.2 | 69.55 | -0.06% | 2.01x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 7 | ALGO/USD | 0.08012 | 69.22 | +0.46% | 0.29x | MODERATE 65/100 | VERY_HIGH 75/100 | Watch |
| 8 | XDG/USD | 0.055608 | 67.85 | +0.01% | 14.75x | STRONG 79/100 | HIGH 55/100 | Watch |
| 9 | XMR/USD | 505.5 | 65.71 | +0.41% | 0.50x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 10 | UAI/USD | 0.03127 | 62.82 | +0.06% | 0.96x | MODERATE 46/100 | VERY_HIGH 80/100 | Watch |
| 11 | XRP/USD | 0.93813 | 57.69 | -0.18% | 0.56x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | NEAR/USD | 2.9927 | 56.48 | -0.40% | 1.17x | WEAK 38/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 72.55 | 90.05 | +0.15% | 2.93x | 29995 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | JUP/USD ⭐ | 0.24539 | 84.66 | +1.19% | 5.39x | 3584 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | PEARL/USD | 2.3196 | 84.56 | +1.91% | 1.24x | 7508 | STRONG 72/100 | HIGH 68/100 | Watch |
| 4 | INJ/USD | 6.34 | 67.02 | +1.05% | 1.54x | 4721 | STRONG 79/100 | HIGH 55/100 | Watch |

**Same-run overlap:** JUP/USD, SOL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
