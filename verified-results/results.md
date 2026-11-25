# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T13:12:36.775662+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45620734347
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 97be04484831d536243390c13cb5e1a5a833d4ff (atomic ledger/results publication)
**Ledger generation:** 1722 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.00982 | 82.809 | 68.826 | +3.70% | -0.20% | 10.57x | 10.2 | 2026-11-25T13:12:32.891494+00:00 | Not calibrated | MODERATE 66/100 | HIGH 67/100 | Watch | WATCH |
| 2 | VVV/USD | 25.358 | 72.155 | 73.855 | +3.34% | +0.24% | 0.71x | 9.1 | 2026-11-25T13:12:32.891494+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | DRV/USD | 0.33341 | 66.504 | 69.351 | +6.09% | +0.18% | 0.63x | 22.5 | 2026-11-25T13:12:32.891494+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 4 | MOODENG/USD | 0.02675 | 56.335 | 58.589 | +9.95% | +0.45% | 0.55x | 37.6 | 2026-11-25T13:12:32.891494+00:00 | Not calibrated | WEAK 43/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | INX/USD | 0.003994 | 31.528 | 39.178 | +4.25% | +0.10% | 0.18x | 42.6 | 2026-11-25T13:12:32.891494+00:00 | Not calibrated | WEAK 21/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 73.855 | 25.358 | +0.24% | 0.71x |
| 2 | DRV/USD | 69.351 | 0.33341 | +0.18% | 0.63x |
| 3 | MON/USD | 68.826 | 0.00982 | -0.20% | 10.57x |
| 4 | MOODENG/USD | 58.589 | 0.02675 | +0.45% | 0.55x |
| 5 | INX/USD | 39.178 | 0.003994 | +0.10% | 0.18x |

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

- Persisted scans: 1722; predictions: 14533; observations: 1043761.
- Matured sampled outcomes across 1/6/24/48h: 31861; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45620734347 · **Generation:** 1722 · **Legacy run:** 45620734347
**Main quote time:** 2026-11-25T13:12:36.775662+00:00 · **Legacy report time:** 2026-11-25T13:13:52.457831+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.00982 | 82.81 | -0.20% | 10.57x | MODERATE 66/100 | HIGH 67/100 | Watch |
| 2 | VVV/USD | 25.358 | 72.15 | +0.24% | 0.71x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 3 | DRV/USD | 0.33341 | 66.50 | +0.18% | 0.63x | WEAK 43/100 | VERY_HIGH 82/100 | Watch |
| 4 | MOODENG/USD | 0.02675 | 56.33 | +0.45% | 0.55x | WEAK 43/100 | EXTREME 87/100 | Do nothing |
| 5 | INX/USD | 0.003994 | 31.53 | +0.10% | 0.18x | WEAK 21/100 | EXTREME 100/100 | Do nothing |

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
