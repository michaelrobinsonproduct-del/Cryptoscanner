# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T16:43:06.410197+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46166324077
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** fd05aeda62c5844f662b386335a2b0c12322c3f4 (atomic ledger/results publication)
**Ledger generation:** 2179 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05189 | 73.477 | 73.117 | +3.28% | +0.85% | 0.61x | 7.7 | 2026-11-28T16:43:02.420104+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | XMR/USD | 417.89 | 67.909 | 60.297 | +2.61% | -1.15% | 2.34x | 25.9 | 2026-11-28T16:43:02.420104+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 3 | VVV/USD | 26.574 | 51.109 | 60.234 | +3.20% | -0.12% | 0.15x | 8.3 | 2026-11-28T16:43:02.420104+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | SENT/USD | 0.023876 | 33.124 | 34.203 | +0.68% | -0.03% | 0.90x | 3.8 | 2026-11-28T16:43:02.420104+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 5 | LUNA/USD | 4.756e-05 | 32.078 | 40.191 | +4.32% | +0.08% | 0.15x | 42.2 | 2026-11-28T16:43:02.420104+00:00 | Not calibrated | WEAK 21/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 73.117 | 0.05189 | +0.85% | 0.61x |
| 2 | XMR/USD | 60.297 | 417.89 | -1.15% | 2.34x |
| 3 | VVV/USD | 60.234 | 26.574 | -0.12% | 0.15x |
| 4 | LUNA/USD | 40.191 | 4.756e-05 | +0.08% | 0.15x |
| 5 | SENT/USD | 34.203 | 0.023876 | -0.03% | 0.90x |

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

- Persisted scans: 2179; predictions: 19321; observations: 1319520.
- Matured sampled outcomes across 1/6/24/48h: 46747; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 156 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46166324077 · **Generation:** 2179 · **Legacy run:** 46166324077
**Main quote time:** 2026-11-28T16:43:06.410197+00:00 · **Legacy report time:** 2026-11-28T16:43:59.157694+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.05189 | 73.48 | +0.85% | 0.61x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 2 | XMR/USD | 417.89 | 67.91 | -1.15% | 2.34x | MODERATE 54/100 | VERY_HIGH 77/100 | Watch |
| 3 | VVV/USD | 26.574 | 51.11 | -0.12% | 0.15x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | SENT/USD | 0.023876 | 33.12 | -0.03% | 0.90x | WEAK 22/100 | VERY_HIGH 80/100 | Do nothing |
| 5 | LUNA/USD | 4.756e-05 | 32.08 | +0.08% | 0.15x | WEAK 21/100 | EXTREME 100/100 | Do nothing |

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
