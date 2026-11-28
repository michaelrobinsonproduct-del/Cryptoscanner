# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T14:42:40.689135+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46155788846
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6b66fa5f1a61865dfdc6722ed640b142eaad14c2 (atomic ledger/results publication)
**Ledger generation:** 2167 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05383 | 92.528 | 96.282 | +7.15% | +0.04% | 0.61x | 7.4 | 2026-11-28T14:42:37.022570+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | XMR/USD | 429.02 | 85.378 | 84.797 | +5.34% | +0.26% | 0.93x | 15.2 | 2026-11-28T14:42:37.022570+00:00 | Not calibrated | MODERATE 68/100 | HIGH 68/100 | Watch | WATCH |
| 3 | MNT/USD | 0.3911 | 68.272 | 60.312 | +6.22% | -0.81% | 2.20x | 28.2 | 2026-11-28T14:42:37.022570+00:00 | Not calibrated | MODERATE 54/100 | EXTREME 85/100 | Do nothing | WATCH |
| 4 | VVV/USD | 26.85 | 64.456 | 68.873 | +4.28% | -0.15% | 0.63x | 8.2 | 2026-11-28T14:42:37.022570+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | SENT/USD | 0.024472 | 49.161 | 51.854 | +3.20% | -1.32% | 1.39x | 4.1 | 2026-11-28T14:42:37.022570+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 6 | LUNA/USD | 4.774e-05 | 48.811 | 44.302 | +4.72% | +0.93% | 0.99x | 39.9 | 2026-11-28T14:42:37.022570+00:00 | Not calibrated | WEAK 39/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 96.282 | 0.05383 | +0.04% | 0.61x |
| 2 | XMR/USD | 84.797 | 429.02 | +0.26% | 0.93x |
| 3 | VVV/USD | 68.873 | 26.85 | -0.15% | 0.63x |
| 4 | MNT/USD | 60.312 | 0.3911 | -0.81% | 2.20x |
| 5 | SENT/USD | 51.854 | 0.024472 | -1.32% | 1.39x |
| 6 | LUNA/USD | 44.302 | 4.774e-05 | +0.93% | 0.99x |

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

- Persisted scans: 2167; predictions: 19264; observations: 1312248.
- Matured sampled outcomes across 1/6/24/48h: 46337; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46155788846 · **Generation:** 2167 · **Legacy run:** 46155788846
**Main quote time:** 2026-11-28T14:42:40.689135+00:00 · **Legacy report time:** 2026-11-28T14:43:18.023059+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.05383 | 92.53 | +0.04% | 0.61x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 2 | XMR/USD | 429.02 | 85.38 | +0.26% | 0.93x | MODERATE 68/100 | HIGH 68/100 | Watch |
| 3 | MNT/USD | 0.3911 | 68.27 | -0.81% | 2.20x | MODERATE 54/100 | EXTREME 85/100 | Do nothing |
| 4 | VVV/USD | 26.85 | 64.46 | -0.15% | 0.63x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 5 | SENT/USD | 0.024472 | 49.16 | -1.32% | 1.39x | MODERATE 45/100 | VERY_HIGH 77/100 | Do nothing |
| 6 | LUNA/USD | 4.774e-05 | 48.81 | +0.93% | 0.99x | WEAK 39/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
