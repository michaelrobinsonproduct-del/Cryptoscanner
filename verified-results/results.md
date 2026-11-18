# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T04:25:06.718071+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44237112645
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** be82b047fc387e8b9948c3e7b95ab0a5197f8f3c (atomic ledger/results publication)
**Ledger generation:** 530 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.2867 | 72.125 | 52.194 | +3.84% | +0.99% | 3.75x | 14.0 | 2026-11-18T04:25:02.247923+00:00 | Not calibrated | STRONG 86/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | SENT/USD | 0.019107 | 55.328 | 43.942 | +2.35% | +0.50% | 1.89x | 6.8 | 2026-11-18T04:25:02.247923+00:00 | Not calibrated | STRONG 73/100 | HIGH 67/100 | Watch | WATCH |
| 3 | MELANIA/USD | 0.051 | 45.058 | 44.100 | +4.72% | +1.39% | 0.40x | 39.4 | 2026-11-18T04:25:02.247923+00:00 | Not calibrated | WEAK 38/100 | EXTREME 94/100 | Do nothing | WATCH |
| 4 | CC/USD | 0.08338 | 40.418 | 43.173 | +1.52% | -1.07% | 1.26x | 6.0 | 2026-11-18T04:25:02.247923+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 5 | XDC/USD | 0.03084 | 39.119 | 44.616 | +1.72% | +0.19% | 0.35x | 9.7 | 2026-11-18T04:25:02.247923+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | AKT/USD | 0.5175 | 30.277 | 38.796 | +1.61% | +0.02% | 0.14x | 9.7 | 2026-11-18T04:25:02.247923+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | ZAMA/USD | 0.06081 | 28.331 | 35.334 | +1.47% | -0.46% | 0.53x | 16.5 | 2026-11-18T04:25:02.247923+00:00 | Not calibrated | WEAK 14/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 52.194 | 0.2867 | +0.99% | 3.75x |
| 2 | XDC/USD | 44.616 | 0.03084 | +0.19% | 0.35x |
| 3 | MELANIA/USD | 44.100 | 0.051 | +1.39% | 0.40x |
| 4 | SENT/USD | 43.942 | 0.019107 | +0.50% | 1.89x |
| 5 | CC/USD | 43.173 | 0.08338 | -1.07% | 1.26x |
| 6 | AKT/USD | 38.796 | 0.5175 | +0.02% | 0.14x |
| 7 | ZAMA/USD | 35.334 | 0.06081 | -0.46% | 0.53x |

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

- Persisted scans: 530; predictions: 4480; observations: 319777.
- Matured sampled outcomes across 1/6/24/48h: 3567; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44237112645 · **Generation:** 530 · **Legacy run:** 44237112645
**Main quote time:** 2026-11-18T04:25:06.718071+00:00 · **Legacy report time:** 2026-11-18T04:25:27.479392+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.2867 | 72.12 | +0.99% | 3.75x | STRONG 96/100 | HIGH 66/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.019107 | 55.33 | +0.50% | 1.89x | STRONG 83/100 | HIGH 67/100 | Consider small entry |
| 3 | MELANIA/USD | 0.051 | 45.06 | +1.39% | 0.40x | WEAK 38/100 | EXTREME 94/100 | Do nothing |
| 4 | CC/USD | 0.08338 | 40.42 | -1.07% | 1.26x | WEAK 30/100 | VERY_HIGH 70/100 | Do nothing |
| 5 | XDC/USD | 0.03084 | 39.12 | +0.19% | 0.35x | WEAK 40/100 | VERY_HIGH 70/100 | Watch |
| 6 | AKT/USD | 0.5175 | 30.28 | +0.02% | 0.14x | WEAK 35/100 | VERY_HIGH 75/100 | Watch |
| 7 | ZAMA/USD | 0.06081 | 28.33 | -0.46% | 0.53x | WEAK 14/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.2864 | 79.11 | +0.99% | 3.75x | 3768 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.019124 | 57.22 | +0.50% | 1.89x | 4001 | STRONG 84/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** ICNT/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
