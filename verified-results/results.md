# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T14:02:37.497278+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45629216497
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 347c65cb3ea35f025b7219a20151e0e61a3d9d77 (atomic ledger/results publication)
**Ledger generation:** 1727 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.00981 | 67.759 | 63.228 | +3.59% | -2.09% | 3.75x | 20.4 | 2026-11-25T14:02:34.461854+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 2 | VVV/USD | 24.696 | 51.798 | 54.636 | +0.64% | -0.81% | 1.12x | 9.7 | 2026-11-25T14:02:34.461854+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 3 | DRV/USD | 0.32436 | 45.031 | 58.268 | +3.21% | -1.63% | 0.49x | 4.0 | 2026-11-25T14:02:34.461854+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 4 | CT/USD | 0.1304 | 31.326 | 38.436 | +3.25% | -0.15% | 0.37x | 30.8 | 2026-11-25T14:02:34.461854+00:00 | Not calibrated | WEAK 11/100 | EXTREME 100/100 | Do nothing | WATCH |
| 5 | ZEUS/USD | 0.00483 | 12.664 | 42.020 | +4.32% | -4.16% | 0.14x | 41.7 | 2026-11-25T14:02:34.461854+00:00 | Not calibrated | WEAK 0/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 63.228 | 0.00981 | -2.09% | 3.75x |
| 2 | DRV/USD | 58.268 | 0.32436 | -1.63% | 0.49x |
| 3 | VVV/USD | 54.636 | 24.696 | -0.81% | 1.12x |
| 4 | ZEUS/USD | 42.020 | 0.00483 | -4.16% | 0.14x |
| 5 | CT/USD | 38.436 | 0.1304 | -0.15% | 0.37x |

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

- Persisted scans: 1727; predictions: 14559; observations: 1046801.
- Matured sampled outcomes across 1/6/24/48h: 32031; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45629216497 · **Generation:** 1727 · **Legacy run:** 45629216497
**Main quote time:** 2026-11-25T14:02:37.497278+00:00 · **Legacy report time:** 2026-11-25T14:03:51.747255+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.00981 | 67.76 | -2.09% | 3.75x | MODERATE 54/100 | VERY_HIGH 77/100 | Do nothing |
| 2 | VVV/USD | 24.696 | 51.80 | -0.81% | 1.12x | WEAK 36/100 | HIGH 68/100 | Watch |
| 3 | DRV/USD | 0.32436 | 45.03 | -1.63% | 0.49x | WEAK 28/100 | VERY_HIGH 80/100 | Do nothing |
| 4 | CT/USD | 0.1304 | 31.33 | -0.15% | 0.37x | WEAK 11/100 | EXTREME 100/100 | Do nothing |
| 5 | ZEUS/USD | 0.00483 | 12.66 | -4.16% | 0.14x | WEAK 0/100 | EXTREME 100/100 | Do nothing |

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
