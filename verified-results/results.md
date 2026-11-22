# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T20:51:23.883575+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45068610849
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 98d4d799acafc0f3efc9a0fb5b00589f1e491c3a (atomic ledger/results publication)
**Ledger generation:** 1334 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.036 | 100.458 | 86.167 | +4.56% | -0.14% | 2.62x | 1.5 | 2026-11-22T20:51:15.371730+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.04833 | 85.036 | 90.721 | +9.15% | -0.51% | 0.69x | 4.1 | 2026-11-22T20:51:15.371730+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | DRV/USD | 0.37387 | 84.633 | 82.194 | +11.54% | -0.03% | 1.26x | 14.2 | 2026-11-22T20:51:15.371730+00:00 | Not calibrated | MODERATE 47/100 | HIGH 67/100 | Watch | WATCH |
| 4 | PUMP/USD | 0.00257 | 78.556 | 80.680 | +9.64% | +0.82% | 0.38x | 11.7 | 2026-11-22T20:51:15.371730+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6546 | 77.887 | 61.816 | +1.13% | +0.21% | 4.06x | 1.5 | 2026-11-22T20:51:15.371730+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | XBT/USD | 60776.3 | 76.669 | 62.988 | +1.14% | +0.31% | 2.21x | 0.0 | 2026-11-22T20:51:15.371730+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | HYPE/USD | 62.67 | 76.406 | 70.547 | +2.34% | +0.34% | 1.42x | 1.6 | 2026-11-22T20:51:15.371730+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 8 | ETH/USD | 1716.62 | 69.393 | 69.260 | +2.04% | +0.31% | 0.86x | 0.1 | 2026-11-22T20:51:15.371730+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 9 | NEAR/USD | 2.9639 | 67.382 | 72.976 | +2.69% | +0.17% | 0.35x | 1.7 | 2026-11-22T20:51:15.371730+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | BNB/USD | 556.62 | 45.484 | 47.465 | +1.68% | +0.27% | 0.67x | 2.0 | 2026-11-22T20:51:15.371730+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | LTC/USD | 39.94 | 42.630 | 45.777 | +0.53% | +0.28% | 0.55x | 2.5 | 2026-11-22T20:51:15.371730+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ALGO/USD | 0.07512 | 35.120 | 35.323 | +0.64% | +0.41% | 0.77x | 4.0 | 2026-11-22T20:51:15.371730+00:00 | Not calibrated | MODERATE 48/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 90.721 | 0.04833 | -0.51% | 0.69x |
| 2 | VVV/USD | 86.167 | 26.036 | -0.14% | 2.62x |
| 3 | DRV/USD | 82.194 | 0.37387 | -0.03% | 1.26x |
| 4 | PUMP/USD | 80.680 | 0.00257 | +0.82% | 0.38x |
| 5 | NEAR/USD | 72.976 | 2.9639 | +0.17% | 0.35x |
| 6 | HYPE/USD | 70.547 | 62.67 | +0.34% | 1.42x |
| 7 | ETH/USD | 69.260 | 1716.62 | +0.31% | 0.86x |
| 8 | XBT/USD | 62.988 | 60776.3 | +0.31% | 2.21x |
| 9 | SUI/USD | 61.816 | 0.6546 | +0.21% | 4.06x |
| 10 | BNB/USD | 47.465 | 556.62 | +0.27% | 0.67x |
| 11 | LTC/USD | 45.777 | 39.94 | +0.28% | 0.55x |
| 12 | ALGO/USD | 35.323 | 0.07512 | +0.41% | 0.77x |

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

- Persisted scans: 1334; predictions: 10927; observations: 807514.
- Matured sampled outcomes across 1/6/24/48h: 16629; gap abstentions: 22356. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 61 (sampled only; not a success-rate estimate).
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

**Writer:** 45068610849 · **Generation:** 1334 · **Legacy run:** 45068610849
**Main quote time:** 2026-11-22T20:51:23.883575+00:00 · **Legacy report time:** 2026-11-22T20:52:20.090410+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 26.036 | 100.46 | -0.14% | 2.62x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | NIGHT/USD | 0.04833 | 85.04 | -0.51% | 0.69x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 3 | DRV/USD | 0.37387 | 84.63 | -0.03% | 1.26x | MODERATE 47/100 | HIGH 67/100 | Watch |
| 4 | PUMP/USD | 0.00257 | 78.56 | +0.82% | 0.38x | MODERATE 64/100 | VERY_HIGH 76/100 | Watch |
| 5 | SUI/USD | 0.6546 | 77.89 | +0.21% | 4.06x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 6 | XBT/USD ⭐ | 60776.3 | 76.67 | +0.31% | 2.21x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | HYPE/USD ⭐ | 62.67 | 76.41 | +0.34% | 1.42x | STRONG 93/100 | HIGH 55/100 | Watch |
| 8 | ETH/USD | 1716.62 | 69.39 | +0.31% | 0.86x | MODERATE 65/100 | HIGH 62/100 | Watch |
| 9 | NEAR/USD | 2.9639 | 67.38 | +0.17% | 0.35x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 10 | BNB/USD | 556.62 | 45.48 | +0.27% | 0.67x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 11 | LTC/USD | 39.94 | 42.63 | +0.28% | 0.55x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 12 | ALGO/USD | 0.07512 | 35.12 | +0.41% | 0.77x | MODERATE 48/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 62.58 | 77.74 | +0.34% | 1.42x | 9959 | STRONG 94/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD | 788.84 | 73.69 | +0.57% | 2.90x | 19482 | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 3 | XBT/USD ⭐ | 60791.1 | 71.75 | +0.31% | 2.21x | 128280 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XBT/USD, HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
