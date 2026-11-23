# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T02:21:22.337015+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45099549292
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 160ecd44246a5a7563b2d4f06e4cb3f1026c8e22 (atomic ledger/results publication)
**Ledger generation:** 1367 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CAP/USD | 0.094018 | 50.365 | 32.614 | +0.48% | +0.55% | 3.59x | 6.2 | 2026-11-23T02:21:18.151768+00:00 | Not calibrated | STRONG 80/100 | HIGH 60/100 | Watch | WATCH |
| 2 | AUD/USD | 0.66389 | 41.452 | 40.509 | +0.35% | -0.01% | 1.10x | 3.3 | 2026-11-23T02:21:18.151768+00:00 | Not calibrated | WEAK 31/100 | HIGH 68/100 | Do nothing | WATCH |
| 3 | ICNT/USD | 0.3613 | 39.970 | 40.072 | +2.58% | +0.11% | 0.93x | 22.1 | 2026-11-23T02:21:18.151768+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 4 | PEARL/USD | 2.0601 | 32.952 | 37.943 | +0.28% | -0.62% | 0.81x | 10.2 | 2026-11-23T02:21:18.151768+00:00 | Not calibrated | WEAK 16/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 5 | BLESS/USD | 0.016401 | 32.505 | 32.128 | +1.91% | -1.87% | 1.97x | 39.2 | 2026-11-23T02:21:18.151768+00:00 | Not calibrated | WEAK 21/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 6 | DRV/USD | 0.37458 | 28.107 | 39.789 | +1.55% | -1.62% | 0.64x | 31.9 | 2026-11-23T02:21:18.151768+00:00 | Not calibrated | WEAK 9/100 | EXTREME 92/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AUD/USD | 40.509 | 0.66389 | -0.01% | 1.10x |
| 2 | ICNT/USD | 40.072 | 0.3613 | +0.11% | 0.93x |
| 3 | DRV/USD | 39.789 | 0.37458 | -1.62% | 0.64x |
| 4 | PEARL/USD | 37.943 | 2.0601 | -0.62% | 0.81x |
| 5 | CAP/USD | 32.614 | 0.094018 | +0.55% | 3.59x |
| 6 | BLESS/USD | 32.128 | 0.016401 | -1.87% | 1.97x |

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

- Persisted scans: 1367; predictions: 11214; observations: 827608.
- Matured sampled outcomes across 1/6/24/48h: 17894; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 84 (sampled only; not a success-rate estimate).
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

**Writer:** 45099549292 · **Generation:** 1367 · **Legacy run:** 45099549292
**Main quote time:** 2026-11-23T02:21:22.337015+00:00 · **Legacy report time:** 2026-11-23T02:22:18.051341+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD ⭐ | 0.094018 | 50.37 | +0.55% | 3.59x | STRONG 90/100 | HIGH 60/100 | Consider small entry |
| 2 | AUD/USD | 0.66389 | 41.45 | -0.01% | 1.10x | WEAK 31/100 | HIGH 68/100 | Do nothing |
| 3 | ICNT/USD | 0.3613 | 39.97 | +0.11% | 0.93x | WEAK 30/100 | VERY_HIGH 79/100 | Do nothing |
| 4 | PEARL/USD | 2.0601 | 32.95 | -0.62% | 0.81x | WEAK 16/100 | VERY_HIGH 74/100 | Do nothing |
| 5 | BLESS/USD | 0.016401 | 32.51 | -1.87% | 1.97x | WEAK 21/100 | VERY_HIGH 77/100 | Do nothing |
| 6 | DRV/USD | 0.37458 | 28.11 | -1.62% | 0.64x | WEAK 9/100 | EXTREME 92/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 494.21 | 50.53 | +0.35% | 4.75x | 8182 | STRONG 80/100 | HIGH 55/100 | Watch |
| 2 | CAP/USD ⭐ | 0.09452 | 45.24 | +0.55% | 3.59x | 4546 | STRONG 83/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
