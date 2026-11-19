# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T02:40:32.226856+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44445920791
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 70b8a1a50b3ab30100050866b2acd378aa2fa295 (atomic ledger/results publication)
**Ledger generation:** 733 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LUNA/USD | 4.645e-05 | 79.453 | 69.778 | +6.68% | -1.06% | 4.52x | 15.1 | 2026-11-19T02:40:23.392885+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | SENT/USD | 0.022087 | 73.922 | 69.769 | +7.19% | +0.29% | 1.27x | 13.6 | 2026-11-19T02:40:23.392885+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | VVV/USD | 21.983 | 69.925 | 56.105 | +1.44% | -0.24% | 7.90x | 5.9 | 2026-11-19T02:40:23.392885+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 4 | NEAR/USD | 3.3103 | 68.520 | 55.625 | +0.39% | -0.42% | 6.73x | 4.2 | 2026-11-19T02:40:23.392885+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ICP/USD | 2.246 | 59.780 | 55.394 | +3.12% | -0.04% | 1.46x | 8.9 | 2026-11-19T02:40:23.392885+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 6 | UAI/USD | 0.03377 | 52.460 | 40.404 | +1.99% | -0.59% | 3.01x | 8.9 | 2026-11-19T02:40:23.392885+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | TON/USD | 1.027 | 39.905 | 33.383 | +0.59% | +0.10% | 1.60x | 9.8 | 2026-11-19T02:40:23.392885+00:00 | Not calibrated | MODERATE 55/100 | HIGH 60/100 | Watch | WATCH |
| 8 | BMT/USD | 0.01958 | 37.995 | 51.582 | +3.71% | -0.96% | 0.12x | 10.2 | 2026-11-19T02:40:23.392885+00:00 | Not calibrated | WEAK 19/100 | EXTREME 94/100 | Do nothing | WATCH |
| 9 | DRV/USD | 0.26618 | 33.937 | 33.101 | +0.56% | -0.08% | 1.12x | 8.3 | 2026-11-19T02:40:23.392885+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 10 | TRUMP/USD | 0.953 | 33.658 | 35.583 | +0.85% | +0.11% | 0.75x | 10.5 | 2026-11-19T02:40:23.392885+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 73/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LUNA/USD | 69.778 | 4.645e-05 | -1.06% | 4.52x |
| 2 | SENT/USD | 69.769 | 0.022087 | +0.29% | 1.27x |
| 3 | VVV/USD | 56.105 | 21.983 | -0.24% | 7.90x |
| 4 | NEAR/USD | 55.625 | 3.3103 | -0.42% | 6.73x |
| 5 | ICP/USD | 55.394 | 2.246 | -0.04% | 1.46x |
| 6 | BMT/USD | 51.582 | 0.01958 | -0.96% | 0.12x |
| 7 | UAI/USD | 40.404 | 0.03377 | -0.59% | 3.01x |
| 8 | TRUMP/USD | 35.583 | 0.953 | +0.11% | 0.75x |
| 9 | TON/USD | 33.383 | 1.027 | +0.10% | 1.60x |
| 10 | DRV/USD | 33.101 | 0.26618 | -0.08% | 1.12x |

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

- Persisted scans: 733; predictions: 5967; observations: 443404.
- Matured sampled outcomes across 1/6/24/48h: 5917; gap abstentions: 13497. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44445920791 · **Generation:** 733 · **Legacy run:** 44445920791
**Main quote time:** 2026-11-19T02:40:32.226856+00:00 · **Legacy report time:** 2026-11-19T02:41:16.027085+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LUNA/USD | 4.645e-05 | 79.45 | -1.06% | 4.52x | MODERATE 65/100 | VERY_HIGH 76/100 | Watch |
| 2 | SENT/USD ⭐ | 0.022087 | 73.92 | +0.29% | 1.27x | STRONG 77/100 | VERY_HIGH 73/100 | Watch |
| 3 | VVV/USD | 21.983 | 69.92 | -0.24% | 7.90x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 4 | NEAR/USD | 3.3103 | 68.52 | -0.42% | 6.73x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 5 | ICP/USD | 2.246 | 59.78 | -0.04% | 1.46x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 6 | UAI/USD | 0.03377 | 52.46 | -0.59% | 3.01x | MODERATE 56/100 | VERY_HIGH 73/100 | Watch |
| 7 | TON/USD | 1.027 | 39.91 | +0.10% | 1.60x | MODERATE 55/100 | HIGH 60/100 | Watch |
| 8 | BMT/USD | 0.01958 | 37.99 | -0.96% | 0.12x | WEAK 19/100 | EXTREME 94/100 | Do nothing |
| 9 | DRV/USD | 0.26618 | 33.94 | -0.08% | 1.12x | WEAK 27/100 | VERY_HIGH 73/100 | Do nothing |
| 10 | TRUMP/USD | 0.953 | 33.66 | +0.11% | 0.75x | WEAK 32/100 | VERY_HIGH 73/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022105 | 72.89 | +0.29% | 1.27x | 7844 | STRONG 81/100 | HIGH 67/100 | Watch |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
