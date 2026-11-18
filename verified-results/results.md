# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T00:20:18.509073+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44206889436
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 9fb36e7b4faa82d1b5a59048bfef3a3475aca204 (atomic ledger/results publication)
**Ledger generation:** 481 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 7.455 | 54.554 | 56.656 | +0.62% | +0.66% | 0.46x | 5.4 | 2026-11-18T00:20:10.781354+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | SENT/USD | 0.018757 | 46.833 | 30.711 | +0.47% | +0.22% | 4.53x | 6.9 | 2026-11-18T00:20:10.781354+00:00 | Not calibrated | STRONG 78/100 | HIGH 67/100 | Watch | WATCH |
| 3 | KAS/USD | 0.02761 | 28.731 | 32.382 | +0.44% | +0.36% | 0.45x | 7.3 | 2026-11-18T00:20:10.781354+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 56.656 | 7.455 | +0.66% | 0.46x |
| 2 | KAS/USD | 32.382 | 0.02761 | +0.36% | 0.45x |
| 3 | SENT/USD | 30.711 | 0.018757 | +0.22% | 4.53x |

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

- Persisted scans: 481; predictions: 4211; observations: 289936.
- Matured sampled outcomes across 1/6/24/48h: 3243; gap abstentions: 12410. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 18; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44206889436 · **Generation:** 481 · **Legacy run:** 44206889436
**Main quote time:** 2026-11-18T00:20:18.509073+00:00 · **Legacy report time:** 2026-11-18T00:20:30.749026+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 7.455 | 54.55 | +0.66% | 0.46x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 2 | SENT/USD ⭐ | 0.018757 | 46.83 | +0.22% | 4.53x | STRONG 88/100 | HIGH 67/100 | Consider small entry |
| 3 | KAS/USD | 0.02761 | 28.73 | +0.36% | 0.45x | WEAK 44/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.018757 | 36.86 | +0.22% | 4.53x | 3805 | STRONG 83/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
