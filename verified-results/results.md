# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T00:42:19.307150+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46089057558
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0b7fa8a8bf5f305db0044128674e75767f8ca2eb (atomic ledger/results publication)
**Ledger generation:** 2082 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 45.37 | 54.154 | 55.105 | +0.49% | -0.37% | 1.09x | 6.6 | 2026-11-28T00:42:13.163459+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 2 | ONDO/USD | 0.28811 | 53.318 | 37.448 | +0.35% | +0.17% | 4.57x | 0.3 | 2026-11-28T00:42:13.163459+00:00 | Not calibrated | STRONG 72/100 | HIGH 60/100 | Watch | WATCH |
| 3 | DRV/USD | 0.36505 | 51.234 | 33.953 | +0.61% | +0.46% | 12.25x | 10.4 | 2026-11-28T00:42:13.163459+00:00 | Not calibrated | STRONG 76/100 | HIGH 66/100 | Watch | WATCH |
| 4 | HYPE/USD | 63.84 | 50.144 | 58.075 | +0.55% | +0.20% | 0.10x | 1.6 | 2026-11-28T00:42:13.163459+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | SKR/USD | 0.00931 | 42.293 | 26.647 | +0.34% | +0.13% | 2.91x | 12.9 | 2026-11-28T00:42:13.163459+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | AVAX/USD | 6.623 | 40.228 | 41.572 | +0.27% | +0.03% | 0.85x | 1.5 | 2026-11-28T00:42:13.163459+00:00 | Not calibrated | WEAK 40/100 | HIGH 62/100 | Watch | WATCH |
| 7 | SENT/USD | 0.023906 | 36.739 | 32.838 | +0.81% | +0.65% | 1.06x | 7.1 | 2026-11-28T00:42:13.163459+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 8 | SKY/USD | 0.05237 | 25.695 | 36.432 | +0.91% | -1.23% | 0.54x | 19.1 | 2026-11-28T00:42:13.163459+00:00 | Not calibrated | WEAK 13/100 | EXTREME 86/100 | Do nothing | WATCH |
| 9 | SPX/USD | 0.2733 | 12.053 | 21.575 | +0.33% | +0.07% | 0.01x | 25.6 | 2026-11-28T00:42:13.163459+00:00 | Not calibrated | WEAK 16/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 58.075 | 63.84 | +0.20% | 0.10x |
| 2 | LTC/USD | 55.105 | 45.37 | -0.37% | 1.09x |
| 3 | AVAX/USD | 41.572 | 6.623 | +0.03% | 0.85x |
| 4 | ONDO/USD | 37.448 | 0.28811 | +0.17% | 4.57x |
| 5 | SKY/USD | 36.432 | 0.05237 | -1.23% | 0.54x |
| 6 | DRV/USD | 33.953 | 0.36505 | +0.46% | 12.25x |
| 7 | SENT/USD | 32.838 | 0.023906 | +0.65% | 1.06x |
| 8 | SKR/USD | 26.647 | 0.00931 | +0.13% | 2.91x |
| 9 | SPX/USD | 21.575 | 0.2733 | +0.07% | 0.01x |

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

- Persisted scans: 2082; predictions: 18653; observations: 1260739.
- Matured sampled outcomes across 1/6/24/48h: 42807; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 154 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46089057558 · **Generation:** 2082 · **Legacy run:** 46089057558
**Main quote time:** 2026-11-28T00:42:19.307150+00:00 · **Legacy report time:** 2026-11-28T00:42:54.417491+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD | 45.37 | 54.15 | -0.37% | 1.09x | WEAK 37/100 | HIGH 68/100 | Watch |
| 2 | ONDO/USD ⭐ | 0.28811 | 53.32 | +0.17% | 4.57x | STRONG 82/100 | HIGH 60/100 | Watch |
| 3 | DRV/USD | 0.36505 | 51.23 | +0.46% | 12.25x | STRONG 76/100 | HIGH 66/100 | Watch |
| 4 | HYPE/USD | 63.84 | 50.14 | +0.20% | 0.10x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 5 | SKR/USD | 0.00931 | 42.29 | +0.13% | 2.91x | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 6 | AVAX/USD | 6.623 | 40.23 | +0.03% | 0.85x | WEAK 40/100 | HIGH 62/100 | Watch |
| 7 | SENT/USD ⭐ | 0.023906 | 36.74 | +0.65% | 1.06x | MODERATE 63/100 | VERY_HIGH 74/100 | Watch |
| 8 | SKY/USD | 0.05237 | 25.70 | -1.23% | 0.54x | WEAK 13/100 | EXTREME 86/100 | Do nothing |
| 9 | SPX/USD | 0.2733 | 12.05 | +0.07% | 0.01x | WEAK 16/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ONDO/USD ⭐ | 0.2879 | 51.24 | +0.17% | 4.57x | 3194 | STRONG 81/100 | HIGH 60/100 | Watch |
| 2 | ZEC/USD | 736.19 | 50.04 | +0.55% | 1.13x | 34032 | MODERATE 60/100 | HIGH 62/100 | Watch |
| 3 | SENT/USD ⭐ | 0.023939 | 43.51 | +0.65% | 1.06x | 3517 | MODERATE 67/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** ONDO/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
