# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T03:00:57.372133+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44978550233
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 95606869a41839ad442ed1498ab2454822cc36bd (atomic ledger/results publication)
**Ledger generation:** 1224 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZBCN/USD | 0.001813 | 71.334 | 45.975 | +4.98% | +2.07% | 5.42x | 44.1 | 2026-11-22T03:00:54.221414+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | ENSO/USD | 0.505 | 57.748 | 54.131 | +4.77% | +1.81% | 0.45x | 20.0 | 2026-11-22T03:00:54.221414+00:00 | Not calibrated | MODERATE 54/100 | EXTREME 88/100 | Do nothing | WATCH |
| 3 | SPX/USD | 0.2809 | 41.423 | 24.631 | +0.54% | +0.36% | 7.21x | 25.0 | 2026-11-22T03:00:54.221414+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | PEARL/USD | 1.9807 | 35.213 | 32.462 | +1.66% | +1.38% | 0.58x | 44.8 | 2026-11-22T03:00:54.221414+00:00 | Not calibrated | WEAK 33/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ENSO/USD | 54.131 | 0.505 | +1.81% | 0.45x |
| 2 | ZBCN/USD | 45.975 | 0.001813 | +2.07% | 5.42x |
| 3 | PEARL/USD | 32.462 | 1.9807 | +1.38% | 0.58x |
| 4 | SPX/USD | 24.631 | 0.2809 | +0.36% | 7.21x |

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

- Persisted scans: 1224; predictions: 9879; observations: 740550.
- Matured sampled outcomes across 1/6/24/48h: 13753; gap abstentions: 21916. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 25 (sampled only; not a success-rate estimate).
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

**Writer:** 44978550233 · **Generation:** 1224 · **Legacy run:** 44978550233
**Main quote time:** 2026-11-22T03:00:57.372133+00:00 · **Legacy report time:** 2026-11-22T03:01:48.626046+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZBCN/USD ⭐ | 0.001813 | 71.33 | +2.07% | 5.42x | STRONG 86/100 | VERY_HIGH 82/100 | Watch |
| 2 | ENSO/USD | 0.505 | 57.75 | +1.81% | 0.45x | MODERATE 54/100 | EXTREME 88/100 | Do nothing |
| 3 | SPX/USD ⭐ | 0.2809 | 41.42 | +0.36% | 7.21x | STRONG 76/100 | VERY_HIGH 72/100 | Watch |
| 4 | PEARL/USD | 1.9807 | 35.21 | +1.38% | 0.58x | WEAK 33/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ZBCN/USD ⭐ | 0.001814 | 86.12 | +2.07% | 5.42x | 3753 | STRONG 98/100 | VERY_HIGH 72/100 | Watch |
| 2 | VVV/USD | 25.067 | 48.56 | +0.17% | 1.40x | 15970 | MODERATE 59/100 | HIGH 55/100 | Watch |
| 3 | SPX/USD ⭐ | 0.2809 | 34.14 | +0.36% | 7.21x | 1993 | STRONG 77/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** ZBCN/USD, SPX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
