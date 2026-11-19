# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T01:25:27.391424+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44436680579
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 463aceb1de16800049bcfe8277125e9ce10a3c4b (atomic ledger/results publication)
**Ledger generation:** 718 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.021259 | 59.596 | 49.644 | +3.17% | +0.05% | 1.97x | 8.0 | 2026-11-19T01:25:20.739638+00:00 | Not calibrated | MODERATE 65/100 | HIGH 67/100 | Watch | WATCH |
| 2 | MEGA/USD | 0.05748 | 58.919 | 44.539 | +2.64% | +0.61% | 2.13x | 10.5 | 2026-11-19T01:25:20.739638+00:00 | Not calibrated | STRONG 79/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | DRV/USD | 0.26711 | 31.585 | 34.116 | +0.91% | -0.10% | 0.80x | 10.9 | 2026-11-19T01:25:20.739638+00:00 | Not calibrated | WEAK 16/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 4 | STABLE/USD | 0.02285 | 18.384 | 21.051 | +0.48% | +0.18% | 0.65x | 26.3 | 2026-11-19T01:25:20.739638+00:00 | Not calibrated | WEAK 19/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 49.644 | 0.021259 | +0.05% | 1.97x |
| 2 | MEGA/USD | 44.539 | 0.05748 | +0.61% | 2.13x |
| 3 | DRV/USD | 34.116 | 0.26711 | -0.10% | 0.80x |
| 4 | STABLE/USD | 21.051 | 0.02285 | +0.18% | 0.65x |

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

- Persisted scans: 718; predictions: 5829; observations: 434269.
- Matured sampled outcomes across 1/6/24/48h: 5717; gap abstentions: 13449. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44436680579 · **Generation:** 718 · **Legacy run:** 44436680579
**Main quote time:** 2026-11-19T01:25:27.391424+00:00 · **Legacy report time:** 2026-11-19T01:26:00.602515+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.021259 | 59.60 | +0.05% | 1.97x | MODERATE 65/100 | HIGH 67/100 | Watch |
| 2 | MEGA/USD ⭐ | 0.05748 | 58.92 | +0.61% | 2.13x | STRONG 89/100 | VERY_HIGH 73/100 | Watch |
| 3 | DRV/USD | 0.26711 | 31.58 | -0.10% | 0.80x | WEAK 16/100 | VERY_HIGH 79/100 | Do nothing |
| 4 | STABLE/USD | 0.02285 | 18.38 | +0.18% | 0.65x | WEAK 19/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MEGA/USD ⭐ | 0.05754 | 51.57 | +0.61% | 2.13x | 1373 | STRONG 86/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** MEGA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
