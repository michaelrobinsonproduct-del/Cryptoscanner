# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T11:41:43.372681+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45167166015
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** fc9463801e1ef82e6903cd6efc1440119aa5ee25 (atomic ledger/results publication)
**Ledger generation:** 1425 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ALGO/USD | 0.08269 | 94.106 | 75.021 | +9.62% | +0.82% | 2.91x | 9.7 | 2026-11-23T11:41:35.779840+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | QNT/USD | 155.14 | 92.596 | 88.501 | +8.16% | -1.51% | 2.17x | 8.4 | 2026-11-23T11:41:35.779840+00:00 | Not calibrated | STRONG 76/100 | HIGH 65/100 | Do nothing | WATCH |
| 3 | JUP/USD | 0.24197 | 90.664 | 74.567 | +7.75% | +0.22% | 4.99x | 11.6 | 2026-11-23T11:41:35.779840+00:00 | Not calibrated | STRONG 95/100 | HIGH 66/100 | Consider small entry | WATCH |
| 4 | XMR/USD | 502.88 | 81.642 | 65.118 | +1.86% | +0.30% | 4.55x | 5.8 | 2026-11-23T11:41:35.779840+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | SOL/USD | 72.64 | 76.490 | 74.232 | +2.85% | +0.48% | 0.98x | 1.4 | 2026-11-23T11:41:35.779840+00:00 | Not calibrated | MODERATE 68/100 | HIGH 62/100 | Watch | WATCH |
| 6 | ICP/USD | 2.064 | 74.352 | 63.971 | +4.98% | +0.49% | 1.79x | 9.7 | 2026-11-23T11:41:35.779840+00:00 | Not calibrated | STRONG 82/100 | HIGH 60/100 | Consider small entry | WATCH |
| 7 | SUI/USD | 0.6729 | 70.876 | 72.619 | +2.62% | +0.67% | 0.49x | 1.5 | 2026-11-23T11:41:35.779840+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | CC/USD | 0.07639 | 66.447 | 64.043 | +4.26% | +0.08% | 1.20x | 1.3 | 2026-11-23T11:41:35.779840+00:00 | Not calibrated | MODERATE 58/100 | HIGH 67/100 | Watch | WATCH |
| 9 | HYPE/USD | 64.13 | 63.518 | 66.097 | +1.70% | +0.58% | 0.45x | 1.6 | 2026-11-23T11:41:35.779840+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XRP/USD | 0.94031 | 62.156 | 64.584 | +1.38% | +0.16% | 0.68x | 0.1 | 2026-11-23T11:41:35.779840+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | AI/USD | 0.01543 | 61.221 | 66.455 | +5.54% | -1.15% | 1.05x | 6.5 | 2026-11-23T11:41:35.779840+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 84/100 | Watch | WATCH |
| 12 | LTC/USD | 40.87 | 59.582 | 53.499 | +1.77% | +0.42% | 1.40x | 2.4 | 2026-11-23T11:41:35.779840+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 88.501 | 155.14 | -1.51% | 2.17x |
| 2 | ALGO/USD | 75.021 | 0.08269 | +0.82% | 2.91x |
| 3 | JUP/USD | 74.567 | 0.24197 | +0.22% | 4.99x |
| 4 | SOL/USD | 74.232 | 72.64 | +0.48% | 0.98x |
| 5 | SUI/USD | 72.619 | 0.6729 | +0.67% | 0.49x |
| 6 | AI/USD | 66.455 | 0.01543 | -1.15% | 1.05x |
| 7 | HYPE/USD | 66.097 | 64.13 | +0.58% | 0.45x |
| 8 | XMR/USD | 65.118 | 502.88 | +0.30% | 4.55x |
| 9 | XRP/USD | 64.584 | 0.94031 | +0.16% | 0.68x |
| 10 | CC/USD | 64.043 | 0.07639 | +0.08% | 1.20x |
| 11 | ICP/USD | 63.971 | 2.064 | +0.49% | 1.79x |
| 12 | LTC/USD | 53.499 | 40.87 | +0.42% | 1.40x |

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

- Persisted scans: 1425; predictions: 11867; observations: 862928.
- Matured sampled outcomes across 1/6/24/48h: 19711; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45167166015 · **Generation:** 1425 · **Legacy run:** 45167166015
**Main quote time:** 2026-11-23T11:41:43.372681+00:00 · **Legacy report time:** 2026-11-23T11:42:51.109082+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD ⭐ | 0.08269 | 94.11 | +0.82% | 2.91x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | QNT/USD | 155.14 | 92.60 | -1.51% | 2.17x | STRONG 76/100 | HIGH 65/100 | Do nothing |
| 3 | JUP/USD ⭐ | 0.24197 | 90.66 | +0.22% | 4.99x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 4 | XMR/USD | 502.88 | 81.64 | +0.30% | 4.55x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 5 | SOL/USD | 72.64 | 76.49 | +0.48% | 0.98x | MODERATE 68/100 | HIGH 62/100 | Watch |
| 6 | ICP/USD ⭐ | 2.064 | 74.35 | +0.49% | 1.79x | STRONG 92/100 | HIGH 60/100 | Consider small entry |
| 7 | SUI/USD | 0.6729 | 70.88 | +0.67% | 0.49x | MODERATE 65/100 | VERY_HIGH 70/100 | Watch |
| 8 | CC/USD ⭐ | 0.07639 | 66.45 | +0.08% | 1.20x | MODERATE 68/100 | HIGH 67/100 | Watch |
| 9 | HYPE/USD | 64.13 | 63.52 | +0.58% | 0.45x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 10 | XRP/USD | 0.94031 | 62.16 | +0.16% | 0.68x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 11 | AI/USD | 0.01543 | 61.22 | -1.15% | 1.05x | WEAK 41/100 | VERY_HIGH 84/100 | Watch |
| 12 | LTC/USD | 40.87 | 59.58 | +0.42% | 1.40x | STRONG 75/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD ⭐ | 0.08272 | 83.52 | +0.82% | 2.91x | 3617 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | JUP/USD ⭐ | 0.24197 | 81.88 | +0.22% | 4.99x | 3535 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 3 | CC/USD ⭐ | 0.07636 | 75.87 | +0.08% | 1.20x | 3990 | STRONG 73/100 | HIGH 67/100 | Watch |
| 4 | DOT/USD | 0.6758 | 72.32 | +0.24% | 11.63x | 7644 | STRONG 91/100 | HIGH 60/100 | Consider small entry |
| 5 | ICP/USD ⭐ | 2.063 | 67.41 | +0.49% | 1.79x | 1490 | STRONG 89/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** ALGO/USD, JUP/USD, ICP/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
