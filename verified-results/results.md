# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T03:27:19.667578+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45539770665
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0d39c6f19788c55f3972e460cd8ab5c98926ac0c (atomic ledger/results publication)
**Ledger generation:** 1663 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 24.868 | 61.233 | 60.389 | +1.34% | +1.12% | 0.52x | 8.0 | 2026-11-25T03:27:15.329276+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | SYRUP/USD | 0.07169 | 60.632 | 41.562 | +2.90% | +0.81% | 5.73x | 20.9 | 2026-11-25T03:27:15.329276+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | DRV/USD | 0.32757 | 53.163 | 56.477 | +4.23% | +0.71% | 0.31x | 15.3 | 2026-11-25T03:27:15.329276+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | MON/USD | 0.00968 | 44.306 | 53.228 | +2.22% | -0.10% | 0.16x | 20.7 | 2026-11-25T03:27:15.329276+00:00 | Not calibrated | WEAK 17/100 | EXTREME 88/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 60.389 | 24.868 | +1.12% | 0.52x |
| 2 | DRV/USD | 56.477 | 0.32757 | +0.71% | 0.31x |
| 3 | MON/USD | 53.228 | 0.00968 | -0.10% | 0.16x |
| 4 | SYRUP/USD | 41.562 | 0.07169 | +0.81% | 5.73x |

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

- Persisted scans: 1663; predictions: 14150; observations: 1007858.
- Matured sampled outcomes across 1/6/24/48h: 29816; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45539770665 · **Generation:** 1663 · **Legacy run:** 45539770665
**Main quote time:** 2026-11-25T03:27:19.667578+00:00 · **Legacy report time:** 2026-11-25T03:28:33.732071+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 24.868 | 61.23 | +1.12% | 0.52x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 2 | SYRUP/USD ⭐ | 0.07169 | 60.63 | +0.81% | 5.73x | STRONG 85/100 | VERY_HIGH 72/100 | Watch |
| 3 | DRV/USD | 0.32757 | 53.16 | +0.71% | 0.31x | MODERATE 52/100 | VERY_HIGH 81/100 | Watch |
| 4 | MON/USD | 0.00968 | 44.31 | -0.10% | 0.16x | WEAK 17/100 | EXTREME 88/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.07169 | 68.27 | +0.81% | 5.73x | 3430 | STRONG 89/100 | VERY_HIGH 72/100 | Watch |
| 2 | TRX/USD | 0.308283 | 50.64 | +0.35% | 2.58x | 3597 | STRONG 80/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
