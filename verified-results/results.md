# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T15:12:37.177294+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45641983682
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 92ce73d1e9b8fbbf72ae83abc1451ee6079b109f (atomic ledger/results publication)
**Ledger generation:** 1734 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.00988 | 72.736 | 63.994 | +4.33% | +0.20% | 1.77x | 20.2 | 2026-11-25T15:12:32.624561+00:00 | Not calibrated | STRONG 71/100 | HIGH 67/100 | Watch | WATCH |
| 2 | PIEVERSE/USD | 3.3035 | 68.597 | 61.662 | +7.24% | -1.61% | 10.87x | 29.8 | 2026-11-25T15:12:32.624561+00:00 | Not calibrated | MODERATE 54/100 | EXTREME 89/100 | Do nothing | WATCH |
| 3 | DRV/USD | 0.32223 | 62.919 | 45.455 | +2.53% | +0.86% | 2.32x | 20.2 | 2026-11-25T15:12:32.624561+00:00 | Not calibrated | STRONG 76/100 | HIGH 67/100 | Watch | WATCH |
| 4 | MOODENG/USD | 0.0266 | 61.972 | 58.999 | +9.33% | +0.95% | 0.82x | 37.8 | 2026-11-25T15:12:32.624561+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | CT/USD | 0.1302 | 60.051 | 45.051 | +3.09% | +0.00% | 3.02x | 15.4 | 2026-11-25T15:12:32.624561+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | VVV/USD | 24.708 | 58.501 | 55.598 | +0.69% | -1.78% | 2.18x | 8.5 | 2026-11-25T15:12:32.624561+00:00 | Not calibrated | MODERATE 59/100 | HIGH 65/100 | Do nothing | WATCH |
| 7 | XPL/USD | 0.045 | 51.260 | 40.223 | +2.27% | +0.00% | 2.10x | 22.2 | 2026-11-25T15:12:32.624561+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 72/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 63.994 | 0.00988 | +0.20% | 1.77x |
| 2 | PIEVERSE/USD | 61.662 | 3.3035 | -1.61% | 10.87x |
| 3 | MOODENG/USD | 58.999 | 0.0266 | +0.95% | 0.82x |
| 4 | VVV/USD | 55.598 | 24.708 | -1.78% | 2.18x |
| 5 | DRV/USD | 45.455 | 0.32223 | +0.86% | 2.32x |
| 6 | CT/USD | 45.051 | 0.1302 | +0.00% | 3.02x |
| 7 | XPL/USD | 40.223 | 0.045 | +0.00% | 2.10x |

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

- Persisted scans: 1734; predictions: 14601; observations: 1051057.
- Matured sampled outcomes across 1/6/24/48h: 32260; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45641983682 · **Generation:** 1734 · **Legacy run:** 45641983682
**Main quote time:** 2026-11-25T15:12:37.177294+00:00 · **Legacy report time:** 2026-11-25T15:13:36.193682+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.00988 | 72.74 | +0.20% | 1.77x | STRONG 81/100 | HIGH 67/100 | Consider small entry |
| 2 | PIEVERSE/USD | 3.3035 | 68.60 | -1.61% | 10.87x | MODERATE 54/100 | EXTREME 89/100 | Do nothing |
| 3 | DRV/USD ⭐ | 0.32223 | 62.92 | +0.86% | 2.32x | STRONG 86/100 | HIGH 67/100 | Consider small entry |
| 4 | MOODENG/USD | 0.0266 | 61.97 | +0.95% | 0.82x | MODERATE 46/100 | VERY_HIGH 79/100 | Watch |
| 5 | CT/USD | 0.1302 | 60.05 | +0.00% | 3.02x | STRONG 70/100 | VERY_HIGH 73/100 | Watch |
| 6 | VVV/USD | 24.708 | 58.50 | -1.78% | 2.18x | MODERATE 59/100 | HIGH 65/100 | Do nothing |
| 7 | XPL/USD | 0.045 | 51.26 | +0.00% | 2.10x | MODERATE 61/100 | VERY_HIGH 72/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.00988 | 81.97 | +0.20% | 1.77x | 14940 | STRONG 86/100 | HIGH 67/100 | Consider small entry |
| 2 | DRV/USD ⭐ | 0.32278 | 67.01 | +0.86% | 2.32x | 10653 | STRONG 94/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** MON/USD, DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
