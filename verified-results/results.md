# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T11:10:42.721155+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44725267851
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** ecee4612191fb28cdfeb6bac5a1e73c2596144bb (atomic ledger/results publication)
**Ledger generation:** 970 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 607; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.022139 | 66.942 | 57.868 | +3.99% | +1.25% | 1.28x | 6.3 | 2026-11-20T11:10:39.144194+00:00 | Not calibrated | MODERATE 68/100 | HIGH 60/100 | Watch | WATCH |
| 2 | HBAR/USD | 0.05401 | 55.577 | 42.605 | +0.47% | -0.41% | 4.81x | 1.9 | 2026-11-20T11:10:39.144194+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SYRUP/USD | 0.098 | 32.370 | 38.865 | +1.84% | +0.13% | 0.28x | 12.3 | 2026-11-20T11:10:39.144194+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 4 | MNT/USD | 0.3943 | 26.144 | 31.760 | +0.69% | +0.05% | 0.41x | 7.6 | 2026-11-20T11:10:39.144194+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 57.868 | 0.022139 | +1.25% | 1.28x |
| 2 | HBAR/USD | 42.605 | 0.05401 | -0.41% | 4.81x |
| 3 | SYRUP/USD | 38.865 | 0.098 | +0.13% | 0.28x |
| 4 | MNT/USD | 31.760 | 0.3943 | +0.05% | 0.41x |

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

- Persisted scans: 970; predictions: 8184; observations: 586144.
- Matured sampled outcomes across 1/6/24/48h: 9828; gap abstentions: 17479. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44725267851 · **Generation:** 970 · **Legacy run:** 44725267851
**Main quote time:** 2026-11-20T11:10:42.721155+00:00 · **Legacy report time:** 2026-11-20T11:11:47.511811+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022139 | 66.94 | +1.25% | 1.28x | STRONG 78/100 | HIGH 60/100 | Watch |
| 2 | HBAR/USD | 0.05401 | 55.58 | -0.41% | 4.81x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 3 | SYRUP/USD | 0.098 | 32.37 | +0.13% | 0.28x | WEAK 31/100 | VERY_HIGH 81/100 | Do nothing |
| 4 | MNT/USD | 0.3943 | 26.14 | +0.05% | 0.41x | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022139 | 76.64 | +1.25% | 1.28x | 8623 | STRONG 83/100 | HIGH 60/100 | Watch |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
