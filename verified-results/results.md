# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T22:31:16.574160+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45078007203
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 8e60dfe47ba16f8955d81ad17cd304f0b0f8a3aa (atomic ledger/results publication)
**Ledger generation:** 1345 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.04915 | 101.247 | 90.024 | +11.00% | -0.04% | 2.14x | 8.1 | 2026-11-22T22:31:08.970176+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | DRV/USD | 0.37052 | 95.899 | 82.884 | +10.54% | -0.40% | 3.11x | 12.2 | 2026-11-22T22:31:08.970176+00:00 | Not calibrated | STRONG 73/100 | HIGH 67/100 | Watch | WATCH |
| 3 | PUMP/USD | 0.002547 | 88.912 | 82.748 | +8.66% | -1.20% | 2.22x | 7.9 | 2026-11-22T22:31:08.970176+00:00 | Not calibrated | STRONG 74/100 | HIGH 65/100 | Do nothing | WATCH |
| 4 | PIEVERSE/USD | 3.6976 | 86.087 | 67.525 | +8.65% | +0.71% | 12.93x | 36.3 | 2026-11-22T22:31:08.970176+00:00 | Not calibrated | STRONG 83/100 | HIGH 67/100 | Consider small entry | WATCH |
| 5 | VVV/USD | 25.877 | 82.006 | 78.795 | +3.92% | -0.35% | 1.49x | 7.3 | 2026-11-22T22:31:08.970176+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 6 | STBL/USD | 0.017113 | 79.639 | 73.128 | +6.93% | -0.42% | 1.86x | 5.8 | 2026-11-22T22:31:08.970176+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | NEAR/USD | 2.9469 | 75.719 | 68.001 | +2.10% | -1.46% | 4.88x | 3.4 | 2026-11-22T22:31:08.970176+00:00 | Not calibrated | MODERATE 68/100 | HIGH 65/100 | Do nothing | WATCH |
| 8 | HYPE/USD | 62.01 | 73.115 | 62.188 | +1.26% | -0.81% | 3.80x | 3.2 | 2026-11-22T22:31:08.970176+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6502 | 68.748 | 56.500 | +0.45% | -0.55% | 3.16x | 3.1 | 2026-11-22T22:31:08.970176+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 10 | LINK/USD | 8.74083 | 68.111 | 54.644 | +1.70% | -0.31% | 3.52x | 0.6 | 2026-11-22T22:31:08.970176+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 11 | XBT/USD | 60705 | 66.209 | 62.157 | +1.02% | -0.20% | 1.51x | 0.0 | 2026-11-22T22:31:08.970176+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 12 | ETH/USD | 1710.09 | 64.303 | 66.543 | +1.65% | -0.24% | 0.90x | 0.1 | 2026-11-22T22:31:08.970176+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 90.024 | 0.04915 | -0.04% | 2.14x |
| 2 | DRV/USD | 82.884 | 0.37052 | -0.40% | 3.11x |
| 3 | PUMP/USD | 82.748 | 0.002547 | -1.20% | 2.22x |
| 4 | VVV/USD | 78.795 | 25.877 | -0.35% | 1.49x |
| 5 | STBL/USD | 73.128 | 0.017113 | -0.42% | 1.86x |
| 6 | NEAR/USD | 68.001 | 2.9469 | -1.46% | 4.88x |
| 7 | PIEVERSE/USD | 67.525 | 3.6976 | +0.71% | 12.93x |
| 8 | ETH/USD | 66.543 | 1710.09 | -0.24% | 0.90x |
| 9 | HYPE/USD | 62.188 | 62.01 | -0.81% | 3.80x |
| 10 | XBT/USD | 62.157 | 60705 | -0.20% | 1.51x |
| 11 | SUI/USD | 56.500 | 0.6502 | -0.55% | 3.16x |
| 12 | LINK/USD | 54.644 | 8.74083 | -0.31% | 3.52x |

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

- Persisted scans: 1345; predictions: 11059; observations: 814212.
- Matured sampled outcomes across 1/6/24/48h: 16989; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45078007203 · **Generation:** 1345 · **Legacy run:** 45078007203
**Main quote time:** 2026-11-22T22:31:16.574160+00:00 · **Legacy report time:** 2026-11-22T22:32:12.051912+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.04915 | 101.25 | -0.04% | 2.14x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | DRV/USD | 0.37052 | 95.90 | -0.40% | 3.11x | STRONG 73/100 | HIGH 67/100 | Watch |
| 3 | PUMP/USD | 0.002547 | 88.91 | -1.20% | 2.22x | STRONG 74/100 | HIGH 65/100 | Do nothing |
| 4 | PIEVERSE/USD ⭐ | 3.6976 | 86.09 | +0.71% | 12.93x | STRONG 93/100 | HIGH 67/100 | Consider small entry |
| 5 | VVV/USD | 25.877 | 82.01 | -0.35% | 1.49x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 6 | STBL/USD | 0.017113 | 79.64 | -0.42% | 1.86x | MODERATE 60/100 | VERY_HIGH 73/100 | Watch |
| 7 | NEAR/USD | 2.9469 | 75.72 | -1.46% | 4.88x | MODERATE 68/100 | HIGH 65/100 | Do nothing |
| 8 | HYPE/USD | 62.01 | 73.11 | -0.81% | 3.80x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 9 | SUI/USD | 0.6502 | 68.75 | -0.55% | 3.16x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 10 | LINK/USD | 8.74083 | 68.11 | -0.31% | 3.52x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 11 | XBT/USD | 60705 | 66.21 | -0.20% | 1.51x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 12 | ETH/USD | 1710.09 | 64.30 | -0.24% | 0.90x | WEAK 37/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD ⭐ | 3.6912 | 86.53 | +0.71% | 12.93x | 5881 | STRONG 93/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** PIEVERSE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
