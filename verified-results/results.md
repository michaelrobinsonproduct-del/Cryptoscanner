# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-22T06:30:52.094530+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44993953128
**Source SHA:** 4066e028afbd46ef7ad268722dcaaaa2ca6a4e7e
**Previous ledger commit:** 276198f9e7fce3b6d33f083dd5f7d4572fb3486e (atomic ledger/results publication)
**Ledger generation:** 1245 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 785.13 | 57.597 | 59.285 | +0.89% | +0.47% | 0.59x | 4.0 | 2026-11-22T06:30:48.078618+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | TRUMP/USD | 0.895 | 49.961 | 30.456 | +1.02% | +0.90% | 2.94x | 22.4 | 2026-11-22T06:30:48.078618+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | PEARL/USD | 1.9695 | 39.798 | 36.216 | +1.09% | +0.51% | 1.11x | 27.5 | 2026-11-22T06:30:48.078618+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 74/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 59.285 | 785.13 | +0.47% | 0.59x |
| 2 | PEARL/USD | 36.216 | 1.9695 | +0.51% | 1.11x |
| 3 | TRUMP/USD | 30.456 | 0.895 | +0.90% | 2.94x |

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

- Persisted scans: 1245; predictions: 9939; observations: 753318.
- Matured sampled outcomes across 1/6/24/48h: 14231; gap abstentions: 21999. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 55 (sampled only; not a success-rate estimate).
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

**Writer:** 44993953128 · **Generation:** 1245 · **Legacy run:** 44993953128
**Main quote time:** 2026-11-22T06:30:52.094530+00:00 · **Legacy report time:** 2026-11-22T06:31:32.509322+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 785.13 | 57.60 | +0.47% | 0.59x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 2 | TRUMP/USD ⭐ | 0.895 | 49.96 | +0.90% | 2.94x | STRONG 80/100 | VERY_HIGH 72/100 | Watch |
| 3 | PEARL/USD ⭐ | 1.9695 | 39.80 | +0.51% | 1.11x | MODERATE 55/100 | VERY_HIGH 74/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRUMP/USD ⭐ | 0.895 | 47.38 | +0.90% | 2.94x | 2944 | STRONG 84/100 | HIGH 66/100 | Consider small entry |
| 2 | PEARL/USD ⭐ | 1.9699 | 44.57 | +0.51% | 1.11x | 8695 | MODERATE 57/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** TRUMP/USD, PEARL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
