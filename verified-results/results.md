# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T02:32:56.724236+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46098326183
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ae7edfc641618c358b505def0f25d3b3e7153416 (atomic ledger/results publication)
**Ledger generation:** 2093 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 755.9 | 88.968 | 73.275 | +2.90% | +0.14% | 3.03x | 4.1 | 2026-11-28T02:32:48.567807+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XRP/USD | 0.95062 | 70.010 | 56.477 | +0.27% | -0.29% | 3.19x | 0.8 | 2026-11-28T02:32:48.567807+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 3 | HYPE/USD | 64.32 | 65.958 | 63.373 | +1.31% | -0.23% | 1.37x | 1.6 | 2026-11-28T02:32:48.567807+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 4 | VVV/USD | 26.049 | 60.984 | 51.149 | +1.17% | +0.32% | 1.82x | 8.1 | 2026-11-28T02:32:48.567807+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 5 | BCH/USD | 209.25 | 59.858 | 44.021 | +1.09% | +0.17% | 4.17x | 2.4 | 2026-11-28T02:32:48.567807+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 6 | XMR/USD | 409.37 | 55.024 | 39.768 | +0.52% | +0.05% | 3.69x | 37.7 | 2026-11-28T02:32:48.567807+00:00 | Not calibrated | MODERATE 58/100 | HIGH 67/100 | Watch | WATCH |
| 7 | ETH/USD | 1666.15 | 53.779 | 57.178 | +0.32% | -0.15% | 0.74x | 0.1 | 2026-11-28T02:32:48.567807+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | TAO/USD | 188.0577 | 52.377 | 56.007 | +0.59% | -0.15% | 0.71x | 6.3 | 2026-11-28T02:32:48.567807+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | NEAR/USD | 3.0481 | 51.212 | 60.130 | +0.99% | -0.15% | 0.18x | 3.6 | 2026-11-28T02:32:48.567807+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | XBT/USD | 60032.2 | 49.994 | 56.961 | +0.28% | -0.15% | 0.38x | 0.0 | 2026-11-28T02:32:48.567807+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | CC/USD | 0.0749 | 36.666 | 38.900 | +1.01% | -0.28% | 0.92x | 5.3 | 2026-11-28T02:32:48.567807+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 12 | SENT/USD | 0.02414 | 34.952 | 42.178 | +1.80% | -0.49% | 0.52x | 2.5 | 2026-11-28T02:32:48.567807+00:00 | Not calibrated | WEAK 22/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 73.275 | 755.9 | +0.14% | 3.03x |
| 2 | HYPE/USD | 63.373 | 64.32 | -0.23% | 1.37x |
| 3 | NEAR/USD | 60.130 | 3.0481 | -0.15% | 0.18x |
| 4 | ETH/USD | 57.178 | 1666.15 | -0.15% | 0.74x |
| 5 | XBT/USD | 56.961 | 60032.2 | -0.15% | 0.38x |
| 6 | XRP/USD | 56.477 | 0.95062 | -0.29% | 3.19x |
| 7 | TAO/USD | 56.007 | 188.0577 | -0.15% | 0.71x |
| 8 | VVV/USD | 51.149 | 26.049 | +0.32% | 1.82x |
| 9 | BCH/USD | 44.021 | 209.25 | +0.17% | 4.17x |
| 10 | SENT/USD | 42.178 | 0.02414 | -0.49% | 0.52x |
| 11 | XMR/USD | 39.768 | 409.37 | +0.05% | 3.69x |
| 12 | CC/USD | 38.900 | 0.0749 | -0.28% | 0.92x |

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

- Persisted scans: 2093; predictions: 18779; observations: 1267404.
- Matured sampled outcomes across 1/6/24/48h: 43268; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46098326183 · **Generation:** 2093 · **Legacy run:** 46098326183
**Main quote time:** 2026-11-28T02:32:56.724236+00:00 · **Legacy report time:** 2026-11-28T02:33:53.778230+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 755.9 | 88.97 | +0.14% | 3.03x | STRONG 99/100 | HIGH 55/100 | Watch |
| 2 | XRP/USD | 0.95062 | 70.01 | -0.29% | 3.19x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 3 | HYPE/USD | 64.32 | 65.96 | -0.23% | 1.37x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 4 | VVV/USD ⭐ | 26.049 | 60.98 | +0.32% | 1.82x | STRONG 85/100 | HIGH 55/100 | Consider small entry |
| 5 | BCH/USD ⭐ | 209.25 | 59.86 | +0.17% | 4.17x | STRONG 85/100 | HIGH 55/100 | Watch |
| 6 | XMR/USD | 409.37 | 55.02 | +0.05% | 3.69x | MODERATE 58/100 | HIGH 67/100 | Watch |
| 7 | ETH/USD | 1666.15 | 53.78 | -0.15% | 0.74x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | TAO/USD | 188.0577 | 52.38 | -0.15% | 0.71x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | NEAR/USD | 3.0481 | 51.21 | -0.15% | 0.18x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | XBT/USD | 60032.2 | 49.99 | -0.15% | 0.38x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | CC/USD | 0.0749 | 36.67 | -0.28% | 0.92x | WEAK 23/100 | VERY_HIGH 73/100 | Do nothing |
| 12 | SENT/USD | 0.02414 | 34.95 | -0.49% | 0.52x | WEAK 22/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD ⭐ | 755.37 | 86.72 | +0.14% | 3.03x | 30928 | STRONG 98/100 | HIGH 55/100 | Watch |
| 2 | BIGTIME/USD | 0.005825 | 65.01 | +2.33% | 1.90x | 5088 | MODERATE 68/100 | VERY_HIGH 79/100 | Watch |
| 3 | BCH/USD ⭐ | 209.26 | 56.47 | +0.17% | 4.17x | 3087 | STRONG 83/100 | HIGH 55/100 | Watch |
| 4 | VVV/USD ⭐ | 26.055 | 50.72 | +0.32% | 1.82x | 8634 | STRONG 80/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ZEC/USD, VVV/USD, BCH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
