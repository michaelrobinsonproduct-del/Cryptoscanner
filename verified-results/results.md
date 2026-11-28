# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T09:57:59.160487+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46132652011
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 1f2c036a2b14f5931fcdbbbd3ac89f6b7d20ca1a (atomic ledger/results publication)
**Ledger generation:** 2138 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05291 | 104.005 | 87.477 | +5.31% | +0.31% | 4.21x | 9.4 | 2026-11-28T09:57:53.976643+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 26.685 | 69.935 | 65.524 | +3.64% | +0.80% | 1.04x | 8.6 | 2026-11-28T09:57:53.976643+00:00 | Not calibrated | STRONG 70/100 | HIGH 62/100 | Watch | WATCH |
| 3 | SPACE/USD | 0.004527 | 63.860 | 75.539 | +8.35% | -0.46% | 0.06x | 2.2 | 2026-11-28T09:57:53.976643+00:00 | Not calibrated | WEAK 37/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.024032 | 59.668 | 40.492 | +1.34% | +0.84% | 4.29x | 0.4 | 2026-11-28T09:57:53.976643+00:00 | Not calibrated | STRONG 85/100 | HIGH 67/100 | Watch | WATCH |
| 5 | TON/USD | 0.982 | 47.923 | 29.852 | +0.31% | +0.61% | 12.43x | 10.2 | 2026-11-28T09:57:53.976643+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 6 | PONS/USD | 0.1027 | 26.912 | 24.445 | +0.39% | +0.00% | 1.25x | 19.5 | 2026-11-28T09:57:53.976643+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 80/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 87.477 | 0.05291 | +0.31% | 4.21x |
| 2 | SPACE/USD | 75.539 | 0.004527 | -0.46% | 0.06x |
| 3 | VVV/USD | 65.524 | 26.685 | +0.80% | 1.04x |
| 4 | SENT/USD | 40.492 | 0.024032 | +0.84% | 4.29x |
| 5 | TON/USD | 29.852 | 0.982 | +0.61% | 12.43x |
| 6 | PONS/USD | 24.445 | 0.1027 | +0.00% | 1.25x |

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

- Persisted scans: 2138; predictions: 19100; observations: 1294674.
- Matured sampled outcomes across 1/6/24/48h: 45265; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46132652011 · **Generation:** 2138 · **Legacy run:** 46132652011
**Main quote time:** 2026-11-28T09:57:59.160487+00:00 · **Legacy report time:** 2026-11-28T09:58:57.383407+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05291 | 104.00 | +0.31% | 4.21x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 26.685 | 69.93 | +0.80% | 1.04x | STRONG 80/100 | HIGH 62/100 | Watch |
| 3 | SPACE/USD | 0.004527 | 63.86 | -0.46% | 0.06x | WEAK 37/100 | EXTREME 88/100 | Do nothing |
| 4 | SENT/USD ⭐ | 0.024032 | 59.67 | +0.84% | 4.29x | STRONG 95/100 | HIGH 67/100 | Consider small entry |
| 5 | TON/USD ⭐ | 0.982 | 47.92 | +0.61% | 12.43x | STRONG 84/100 | HIGH 66/100 | Consider small entry |
| 6 | PONS/USD | 0.1027 | 26.91 | +0.00% | 1.25x | WEAK 33/100 | VERY_HIGH 80/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05303 | 100.00 | +0.31% | 4.21x | 20349 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 26.736 | 79.21 | +0.80% | 1.04x | 7563 | STRONG 85/100 | HIGH 62/100 | Watch |
| 3 | SENT/USD ⭐ | 0.024014 | 60.97 | +0.84% | 4.29x | 5564 | STRONG 95/100 | HIGH 67/100 | Consider small entry |
| 4 | TON/USD ⭐ | 0.981 | 33.29 | +0.61% | 12.43x | 2318 | STRONG 77/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** NIGHT/USD, VVV/USD, SENT/USD, TON/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
