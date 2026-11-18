# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T18:20:07.751539+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44368458697
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 399ddbc51c6e8080ed70a45586a90c9ae65e1ac2 (atomic ledger/results publication)
**Ledger generation:** 634 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.020009 | 68.836 | 73.102 | +7.18% | +0.43% | 0.36x | 6.0 | 2026-11-18T18:20:04.239113+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | MNT/USD | 0.384 | 50.119 | 48.027 | +2.87% | +0.58% | 0.92x | 7.8 | 2026-11-18T18:20:04.239113+00:00 | Not calibrated | MODERATE 55/100 | HIGH 67/100 | Watch | WATCH |
| 3 | MEGA/USD | 0.05324 | 42.019 | 47.176 | +3.10% | +0.53% | 0.22x | 11.3 | 2026-11-18T18:20:04.239113+00:00 | Not calibrated | MODERATE 46/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | NIGHT/USD | 0.04519 | 39.490 | 52.104 | +0.67% | -0.86% | 0.17x | 2.2 | 2026-11-18T18:20:04.239113+00:00 | Not calibrated | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 73.102 | 0.020009 | +0.43% | 0.36x |
| 2 | NIGHT/USD | 52.104 | 0.04519 | -0.86% | 0.17x |
| 3 | MNT/USD | 48.027 | 0.384 | +0.58% | 0.92x |
| 4 | MEGA/USD | 47.176 | 0.05324 | +0.53% | 0.22x |

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

- Persisted scans: 634; predictions: 5395; observations: 383113.
- Matured sampled outcomes across 1/6/24/48h: 4705; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44368458697 · **Generation:** 634 · **Legacy run:** 44368458697
**Main quote time:** 2026-11-18T18:20:07.751539+00:00 · **Legacy report time:** 2026-11-18T18:20:31.784066+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.020009 | 68.84 | +0.43% | 0.36x | MODERATE 64/100 | VERY_HIGH 82/100 | Watch |
| 2 | MNT/USD | 0.384 | 50.12 | +0.58% | 0.92x | MODERATE 55/100 | HIGH 67/100 | Watch |
| 3 | MEGA/USD | 0.05324 | 42.02 | +0.53% | 0.22x | MODERATE 46/100 | EXTREME 88/100 | Do nothing |
| 4 | NIGHT/USD | 0.04519 | 39.49 | -0.86% | 0.17x | WEAK 25/100 | VERY_HIGH 76/100 | Do nothing |

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
