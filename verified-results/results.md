# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T14:23:42.817306+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45632810934
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 609343976341c1d3dcbd06519a9c57068af49130 (atomic ledger/results publication)
**Ledger generation:** 1729 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.00983 | 66.140 | 67.235 | +3.80% | +0.31% | 0.74x | 10.2 | 2026-11-25T14:23:38.016320+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | VVV/USD | 24.807 | 59.371 | 58.240 | +1.10% | +0.61% | 0.81x | 8.9 | 2026-11-25T14:23:38.016320+00:00 | Not calibrated | MODERATE 60/100 | HIGH 62/100 | Watch | WATCH |
| 3 | DRV/USD | 0.32382 | 52.855 | 55.191 | +3.04% | -0.38% | 0.96x | 7.7 | 2026-11-25T14:23:38.016320+00:00 | Not calibrated | WEAK 31/100 | HIGH 68/100 | Do nothing | WATCH |
| 4 | MOODENG/USD | 0.02715 | 52.546 | 64.852 | +11.59% | -1.78% | 0.66x | 25.8 | 2026-11-25T14:23:38.016320+00:00 | Not calibrated | WEAK 21/100 | EXTREME 97/100 | Do nothing | WATCH |
| 5 | ZEUS/USD | 0.00479 | 47.513 | 35.921 | +3.46% | +2.72% | 0.80x | 41.8 | 2026-11-25T14:23:38.016320+00:00 | Not calibrated | WEAK 39/100 | EXTREME 89/100 | Do nothing | WATCH |
| 6 | CT/USD | 0.1296 | 28.578 | 33.981 | +2.61% | +0.15% | 0.38x | 30.8 | 2026-11-25T14:23:38.016320+00:00 | Not calibrated | WEAK 24/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 67.235 | 0.00983 | +0.31% | 0.74x |
| 2 | MOODENG/USD | 64.852 | 0.02715 | -1.78% | 0.66x |
| 3 | VVV/USD | 58.240 | 24.807 | +0.61% | 0.81x |
| 4 | DRV/USD | 55.191 | 0.32382 | -0.38% | 0.96x |
| 5 | ZEUS/USD | 35.921 | 0.00479 | +2.72% | 0.80x |
| 6 | CT/USD | 33.981 | 0.1296 | +0.15% | 0.38x |

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

- Persisted scans: 1729; predictions: 14569; observations: 1048017.
- Matured sampled outcomes across 1/6/24/48h: 32093; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45632810934 · **Generation:** 1729 · **Legacy run:** 45632810934
**Main quote time:** 2026-11-25T14:23:42.817306+00:00 · **Legacy report time:** 2026-11-25T14:24:46.283036+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD | 0.00983 | 66.14 | +0.31% | 0.74x | MODERATE 58/100 | VERY_HIGH 76/100 | Watch |
| 2 | VVV/USD | 24.807 | 59.37 | +0.61% | 0.81x | MODERATE 60/100 | HIGH 62/100 | Watch |
| 3 | DRV/USD | 0.32382 | 52.85 | -0.38% | 0.96x | WEAK 31/100 | HIGH 68/100 | Do nothing |
| 4 | MOODENG/USD | 0.02715 | 52.55 | -1.78% | 0.66x | WEAK 21/100 | EXTREME 97/100 | Do nothing |
| 5 | ZEUS/USD | 0.00479 | 47.51 | +2.72% | 0.80x | WEAK 39/100 | EXTREME 89/100 | Do nothing |
| 6 | CT/USD | 0.1296 | 28.58 | +0.15% | 0.38x | WEAK 24/100 | EXTREME 94/100 | Do nothing |

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
