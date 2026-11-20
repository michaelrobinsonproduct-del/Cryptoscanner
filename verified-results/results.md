# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T11:30:46.424853+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44728034453
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 2ebd587483b042235d3ac1cfed8072e8729007ec (atomic ledger/results publication)
**Ledger generation:** 972 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 607; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TREAD/USD | 1.0402 | 64.934 | 58.042 | +4.19% | +0.43% | 1.47x | 3.9 | 2026-11-20T11:30:42.326667+00:00 | Not calibrated | STRONG 77/100 | HIGH 67/100 | Watch | WATCH |
| 2 | ICNT/USD | 0.4341 | 55.333 | 37.642 | +1.88% | +3.88% | 0.83x | 27.7 | 2026-11-20T11:30:42.326667+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 84/100 | Watch | WATCH |
| 3 | SENT/USD | 0.022015 | 47.657 | 53.044 | +3.41% | -0.94% | 0.93x | 7.7 | 2026-11-20T11:30:42.326667+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 4 | MON/USD | 0.01393 | 39.831 | 38.578 | +1.24% | +1.38% | 0.43x | 7.2 | 2026-11-20T11:30:42.326667+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | WINGS/USD | 0.001932 | 37.205 | 44.092 | +4.77% | +0.00% | 0.31x | 41.4 | 2026-11-20T11:30:42.326667+00:00 | Not calibrated | WEAK 24/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | TREAD/USD | 58.042 | 1.0402 | +0.43% | 1.47x |
| 2 | SENT/USD | 53.044 | 0.022015 | -0.94% | 0.93x |
| 3 | WINGS/USD | 44.092 | 0.001932 | +0.00% | 0.31x |
| 4 | MON/USD | 38.578 | 0.01393 | +1.38% | 0.43x |
| 5 | ICNT/USD | 37.642 | 0.4341 | +3.88% | 0.83x |

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

- Persisted scans: 972; predictions: 8192; observations: 587358.
- Matured sampled outcomes across 1/6/24/48h: 9838; gap abstentions: 17479. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44728034453 · **Generation:** 972 · **Legacy run:** 44728034453
**Main quote time:** 2026-11-20T11:30:46.424853+00:00 · **Legacy report time:** 2026-11-20T11:31:44.637342+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TREAD/USD ⭐ | 1.0402 | 64.93 | +0.43% | 1.47x | STRONG 87/100 | HIGH 67/100 | Watch |
| 2 | ICNT/USD | 0.4341 | 55.33 | +3.88% | 0.83x | MODERATE 48/100 | VERY_HIGH 84/100 | Watch |
| 3 | SENT/USD | 0.022015 | 47.66 | -0.94% | 0.93x | WEAK 29/100 | VERY_HIGH 73/100 | Do nothing |
| 4 | MON/USD | 0.01393 | 39.83 | +1.38% | 0.43x | MODERATE 50/100 | VERY_HIGH 75/100 | Watch |
| 5 | WINGS/USD | 0.001932 | 37.20 | +0.00% | 0.31x | WEAK 24/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TREAD/USD ⭐ | 1.0402 | 80.85 | +0.43% | 1.47x | 3534 | STRONG 95/100 | HIGH 67/100 | Watch |
| 2 | HBAR/USD | 0.05386 | 38.49 | +0.15% | 1.02x | 8416 | WEAK 44/100 | HIGH 62/100 | Watch |

**Same-run overlap:** TREAD/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
