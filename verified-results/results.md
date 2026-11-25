# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T17:17:34.607030+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45662649989
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** daa63daa3afeb5ef48a2b4b87429c8a442003776 (atomic ledger/results publication)
**Ledger generation:** 1743 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.096 | 127.817 | 92.350 | +6.35% | +4.09% | 7.74x | 14.2 | 2026-11-25T17:17:25.484503+00:00 | Not calibrated | STRONG 100/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 2 | DRV/USD | 0.33642 | 94.139 | 71.001 | +7.04% | +1.64% | 2.49x | 24.7 | 2026-11-25T17:17:25.484503+00:00 | Not calibrated | STRONG 92/100 | HIGH 67/100 | Consider small entry | WATCH |
| 3 | XPL/USD | 0.0471 | 90.534 | 70.555 | +7.05% | +1.73% | 2.13x | 21.2 | 2026-11-25T17:17:25.484503+00:00 | Not calibrated | STRONG 90/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | LTC/USD | 41.46 | 69.446 | 64.247 | +1.49% | +1.22% | 0.91x | 2.4 | 2026-11-25T17:17:25.484503+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 5 | INJ/USD | 5.872 | 63.068 | 38.302 | +0.41% | +1.95% | 2.58x | 5.1 | 2026-11-25T17:17:25.484503+00:00 | Not calibrated | STRONG 87/100 | HIGH 55/100 | Watch | WATCH |
| 6 | STRK/USD | 0.03031 | 61.618 | 36.321 | +1.61% | +2.06% | 3.33x | 13.2 | 2026-11-25T17:17:25.484503+00:00 | Not calibrated | STRONG 81/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | HBAR/USD | 0.05057 | 60.313 | 38.076 | +0.62% | +1.45% | 3.06x | 4.0 | 2026-11-25T17:17:25.484503+00:00 | Not calibrated | STRONG 85/100 | HIGH 60/100 | Watch | WATCH |
| 8 | ASTER/USD | 0.48799 | 59.783 | 40.902 | +1.49% | +1.05% | 2.37x | 4.3 | 2026-11-25T17:17:25.484503+00:00 | Not calibrated | STRONG 85/100 | HIGH 60/100 | Watch | WATCH |
| 9 | APT/USD | 0.3656 | 51.745 | 28.519 | +0.44% | +1.65% | 18.49x | 10.9 | 2026-11-25T17:17:25.484503+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 10 | KAS/USD | 0.02653 | 40.861 | 33.147 | +1.57% | +1.18% | 1.18x | 22.6 | 2026-11-25T17:17:25.484503+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 11 | ICP/USD | 2.005 | 40.000 | 30.062 | +0.60% | +0.81% | 1.59x | 15.0 | 2026-11-25T17:17:25.484503+00:00 | Not calibrated | MODERATE 60/100 | HIGH 66/100 | Watch | WATCH |
| 12 | XTZ/USD | 0.21279 | 35.708 | 29.527 | +0.69% | +1.96% | 0.64x | 12.2 | 2026-11-25T17:17:25.484503+00:00 | Not calibrated | WEAK 43/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 92.350 | 26.096 | +4.09% | 7.74x |
| 2 | DRV/USD | 71.001 | 0.33642 | +1.64% | 2.49x |
| 3 | XPL/USD | 70.555 | 0.0471 | +1.73% | 2.13x |
| 4 | LTC/USD | 64.247 | 41.46 | +1.22% | 0.91x |
| 5 | ASTER/USD | 40.902 | 0.48799 | +1.05% | 2.37x |
| 6 | INJ/USD | 38.302 | 5.872 | +1.95% | 2.58x |
| 7 | HBAR/USD | 38.076 | 0.05057 | +1.45% | 3.06x |
| 8 | STRK/USD | 36.321 | 0.03031 | +2.06% | 3.33x |
| 9 | KAS/USD | 33.147 | 0.02653 | +1.18% | 1.18x |
| 10 | ICP/USD | 30.062 | 2.005 | +0.81% | 1.59x |
| 11 | XTZ/USD | 29.527 | 0.21279 | +1.96% | 0.64x |
| 12 | APT/USD | 28.519 | 0.3656 | +1.65% | 18.49x |

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

- Persisted scans: 1743; predictions: 14661; observations: 1056531.
- Matured sampled outcomes across 1/6/24/48h: 32504; gap abstentions: 22505. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45662649989 · **Generation:** 1743 · **Legacy run:** 45662649989
**Main quote time:** 2026-11-25T17:17:34.607030+00:00 · **Legacy report time:** 2026-11-25T17:18:30.705306+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.096 | 127.82 | +4.09% | 7.74x | STRONG 100/100 | VERY_HIGH 71/100 | Watch |
| 2 | DRV/USD ⭐ | 0.33642 | 94.14 | +1.64% | 2.49x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | XPL/USD ⭐ | 0.0471 | 90.53 | +1.73% | 2.13x | STRONG 100/100 | VERY_HIGH 72/100 | Watch |
| 4 | LTC/USD | 41.46 | 69.45 | +1.22% | 0.91x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 5 | INJ/USD ⭐ | 5.872 | 63.07 | +1.95% | 2.58x | STRONG 97/100 | HIGH 55/100 | Consider small entry |
| 6 | STRK/USD | 0.03031 | 61.62 | +2.06% | 3.33x | STRONG 81/100 | VERY_HIGH 73/100 | Watch |
| 7 | HBAR/USD ⭐ | 0.05057 | 60.31 | +1.45% | 3.06x | STRONG 95/100 | HIGH 60/100 | Consider small entry |
| 8 | ASTER/USD ⭐ | 0.48799 | 59.78 | +1.05% | 2.37x | STRONG 95/100 | HIGH 60/100 | Consider small entry |
| 9 | APT/USD | 0.3656 | 51.75 | +1.65% | 18.49x | STRONG 76/100 | VERY_HIGH 73/100 | Watch |
| 10 | KAS/USD ⭐ | 0.02653 | 40.86 | +1.18% | 1.18x | MODERATE 55/100 | VERY_HIGH 79/100 | Watch |
| 11 | ICP/USD | 2.005 | 40.00 | +0.81% | 1.59x | MODERATE 60/100 | HIGH 66/100 | Watch |
| 12 | XTZ/USD | 0.21279 | 35.71 | +1.96% | 0.64x | WEAK 43/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.172 | 100.00 | +4.09% | 7.74x | 10574 | STRONG 100/100 | VERY_HIGH 77/100 | Watch |
| 2 | DRV/USD ⭐ | 0.33815 | 85.93 | +1.64% | 2.49x | 10782 | STRONG 98/100 | HIGH 67/100 | Consider small entry |
| 3 | XPL/USD ⭐ | 0.0474 | 77.23 | +1.73% | 2.13x | 1893 | STRONG 94/100 | VERY_HIGH 72/100 | Watch |
| 4 | HBAR/USD ⭐ | 0.05068 | 58.93 | +1.45% | 3.06x | 5358 | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 5 | ASTER/USD ⭐ | 0.48873 | 55.46 | +1.05% | 2.37x | 2958 | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 6 | INJ/USD ⭐ | 5.914 | 52.56 | +1.95% | 2.58x | 6573 | STRONG 86/100 | HIGH 61/100 | Consider small entry |
| 7 | XMR/USD | 510.96 | 50.39 | +0.73% | 4.36x | 7671 | STRONG 80/100 | HIGH 55/100 | Watch |
| 8 | XLM/USD | 0.124992 | 50.22 | +0.96% | 2.12x | 7840 | STRONG 80/100 | HIGH 55/100 | Watch |
| 9 | KAS/USD ⭐ | 0.02661 | 49.47 | +1.18% | 1.18x | 2471 | MODERATE 65/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** VVV/USD, DRV/USD, XPL/USD, INJ/USD, HBAR/USD, ASTER/USD, KAS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
