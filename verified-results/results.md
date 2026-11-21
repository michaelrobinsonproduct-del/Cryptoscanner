# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T02:55:41.325845+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44858382828
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 91fbc29d5f37d59714b595f7aa3f02abc0a6ddf8 (atomic ledger/results publication)
**Ledger generation:** 1067 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.26975 | 90.591 | 76.924 | +9.86% | -0.27% | 3.40x | 10.0 | 2026-11-21T02:55:35.040784+00:00 | Not calibrated | STRONG 70/100 | HIGH 67/100 | Watch | WATCH |
| 2 | VVV/USD | 20.898 | 53.166 | 55.582 | +0.77% | +0.19% | 0.67x | 9.6 | 2026-11-21T02:55:35.040784+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | CAP/USD | 0.094466 | 50.363 | 53.525 | +3.19% | +0.35% | 0.51x | 4.4 | 2026-11-21T02:55:35.040784+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 4 | STBL/USD | 0.01608 | 28.858 | 31.589 | +1.28% | -0.39% | 0.92x | 16.8 | 2026-11-21T02:55:35.040784+00:00 | Not calibrated | WEAK 14/100 | EXTREME 86/100 | Do nothing | WATCH |
| 5 | DCR/USD | 10.189 | 21.230 | 31.155 | +0.83% | -0.17% | 0.09x | 10.8 | 2026-11-21T02:55:35.040784+00:00 | Not calibrated | WEAK 11/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 76.924 | 0.26975 | -0.27% | 3.40x |
| 2 | VVV/USD | 55.582 | 20.898 | +0.19% | 0.67x |
| 3 | CAP/USD | 53.525 | 0.094466 | +0.35% | 0.51x |
| 4 | STBL/USD | 31.589 | 0.01608 | -0.39% | 0.92x |
| 5 | DCR/USD | 31.155 | 10.189 | -0.17% | 0.09x |

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

- Persisted scans: 1067; predictions: 8559; observations: 645096.
- Matured sampled outcomes across 1/6/24/48h: 11030; gap abstentions: 19479. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44858382828 · **Generation:** 1067 · **Legacy run:** 44858382828
**Main quote time:** 2026-11-21T02:55:41.325845+00:00 · **Legacy report time:** 2026-11-21T02:56:27.478934+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD | 0.26975 | 90.59 | -0.27% | 3.40x | STRONG 70/100 | HIGH 67/100 | Watch |
| 2 | VVV/USD | 20.898 | 53.17 | +0.19% | 0.67x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |
| 3 | CAP/USD | 0.094466 | 50.36 | +0.35% | 0.51x | MODERATE 55/100 | VERY_HIGH 75/100 | Watch |
| 4 | STBL/USD | 0.01608 | 28.86 | -0.39% | 0.92x | WEAK 14/100 | EXTREME 86/100 | Do nothing |
| 5 | DCR/USD | 10.189 | 21.23 | -0.17% | 0.09x | WEAK 11/100 | EXTREME 94/100 | Do nothing |

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
