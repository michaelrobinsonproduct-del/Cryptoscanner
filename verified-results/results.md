# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T00:35:36.511768+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44844733571
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** b41a43777c3e85608ff7ed37dd64a565e2c00edc (atomic ledger/results publication)
**Ledger generation:** 1047 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 1.8656 | 64.409 | 50.148 | +2.04% | +2.93% | 0.96x | 25.8 | 2026-11-21T00:35:29.297224+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | SOL/USD | 68.95 | 59.419 | 56.720 | +0.35% | +0.23% | 1.15x | 1.5 | 2026-11-21T00:35:29.297224+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 3 | AKE/USD | 0.00616878 | 58.101 | 48.673 | +0.94% | +2.98% | 0.45x | 25.9 | 2026-11-21T00:35:29.297224+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | AKT/USD | 0.508 | 47.865 | 27.682 | +0.81% | +1.04% | 5.03x | 21.7 | 2026-11-21T00:35:29.297224+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | CAP/USD | 0.091955 | 46.414 | 34.560 | +0.45% | -0.04% | 2.20x | 2.6 | 2026-11-21T00:35:29.297224+00:00 | Not calibrated | MODERATE 53/100 | HIGH 66/100 | Watch | WATCH |
| 6 | DRV/USD | 0.24746 | 44.054 | 36.988 | +0.78% | +0.58% | 1.42x | 7.7 | 2026-11-21T00:35:29.297224+00:00 | Not calibrated | MODERATE 67/100 | HIGH 60/100 | Watch | WATCH |
| 7 | CT/USD | 0.1218 | 39.918 | 27.714 | +0.58% | +1.16% | 1.64x | 16.4 | 2026-11-21T00:35:29.297224+00:00 | Not calibrated | MODERATE 60/100 | HIGH 66/100 | Watch | WATCH |
| 8 | USELESS/USD | 0.0749 | 37.977 | 33.392 | +0.54% | +1.24% | 0.84x | 22.7 | 2026-11-21T00:35:29.297224+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 9 | PIEVERSE/USD | 3.0193 | 27.646 | 29.034 | +0.69% | +0.67% | 0.53x | 21.2 | 2026-11-21T00:35:29.297224+00:00 | Not calibrated | WEAK 34/100 | EXTREME 87/100 | Do nothing | WATCH |
| 10 | ZBCN/USD | 0.001599 | 27.053 | 29.337 | +0.50% | -0.25% | 0.90x | 12.5 | 2026-11-21T00:35:29.297224+00:00 | Not calibrated | WEAK 14/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SOL/USD | 56.720 | 68.95 | +0.23% | 1.15x |
| 2 | PEARL/USD | 50.148 | 1.8656 | +2.93% | 0.96x |
| 3 | AKE/USD | 48.673 | 0.00616878 | +2.98% | 0.45x |
| 4 | DRV/USD | 36.988 | 0.24746 | +0.58% | 1.42x |
| 5 | CAP/USD | 34.560 | 0.091955 | -0.04% | 2.20x |
| 6 | USELESS/USD | 33.392 | 0.0749 | +1.24% | 0.84x |
| 7 | ZBCN/USD | 29.337 | 0.001599 | -0.25% | 0.90x |
| 8 | PIEVERSE/USD | 29.034 | 3.0193 | +0.67% | 0.53x |
| 9 | CT/USD | 27.714 | 0.1218 | +1.16% | 1.64x |
| 10 | AKT/USD | 27.682 | 0.508 | +1.04% | 5.03x |

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

- Persisted scans: 1047; predictions: 8373; observations: 632936.
- Matured sampled outcomes across 1/6/24/48h: 10928; gap abstentions: 19022. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44844733571 · **Generation:** 1047 · **Legacy run:** 44844733571
**Main quote time:** 2026-11-21T00:35:36.511768+00:00 · **Legacy report time:** 2026-11-21T00:36:32.839405+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 1.8656 | 64.41 | +2.93% | 0.96x | MODERATE 52/100 | VERY_HIGH 74/100 | Watch |
| 2 | SOL/USD ⭐ | 68.95 | 59.42 | +0.23% | 1.15x | STRONG 75/100 | HIGH 62/100 | Watch |
| 3 | AKE/USD | 0.00616878 | 58.10 | +2.98% | 0.45x | MODERATE 49/100 | VERY_HIGH 82/100 | Watch |
| 4 | AKT/USD | 0.508 | 47.86 | +1.04% | 5.03x | MODERATE 69/100 | VERY_HIGH 72/100 | Watch |
| 5 | CAP/USD | 0.091955 | 46.41 | -0.04% | 2.20x | MODERATE 53/100 | HIGH 66/100 | Watch |
| 6 | DRV/USD ⭐ | 0.24746 | 44.05 | +0.58% | 1.42x | STRONG 77/100 | HIGH 60/100 | Watch |
| 7 | CT/USD | 0.1218 | 39.92 | +1.16% | 1.64x | MODERATE 60/100 | HIGH 66/100 | Watch |
| 8 | USELESS/USD | 0.0749 | 37.98 | +1.24% | 0.84x | WEAK 39/100 | VERY_HIGH 74/100 | Watch |
| 9 | PIEVERSE/USD | 3.0193 | 27.65 | +0.67% | 0.53x | WEAK 34/100 | EXTREME 87/100 | Do nothing |
| 10 | ZBCN/USD | 0.001599 | 27.05 | -0.25% | 0.90x | WEAK 14/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 68.97 | 54.95 | +0.23% | 1.15x | 43600 | STRONG 72/100 | HIGH 62/100 | Watch |
| 2 | DRV/USD ⭐ | 0.2477 | 39.18 | +0.58% | 1.42x | 5963 | STRONG 70/100 | HIGH 66/100 | Watch |

**Same-run overlap:** SOL/USD, DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
