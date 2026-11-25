# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T02:37:24.778811+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45533937879
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 61388b511d8ff6a4ae01e96ddb8f557922b01d64 (atomic ledger/results publication)
**Ledger generation:** 1658 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.32957 | 87.623 | 68.366 | +4.87% | +2.14% | 1.86x | 0.6 | 2026-11-25T02:37:21.491994+00:00 | Not calibrated | STRONG 89/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | XAUT/USD | 3554.4 | 51.912 | 35.419 | +0.48% | +0.30% | 4.79x | 0.6 | 2026-11-25T02:37:21.491994+00:00 | Not calibrated | STRONG 81/100 | HIGH 60/100 | Watch | WATCH |
| 3 | BABY/USD | 0.00835 | 48.083 | 34.278 | +1.09% | -0.24% | 6.39x | 12.0 | 2026-11-25T02:37:21.491994+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | PAXG/USD | 3555.19 | 40.523 | 41.379 | +0.38% | +0.26% | 0.79x | 0.7 | 2026-11-25T02:37:21.491994+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | DRV/USD | 68.366 | 0.32957 | +2.14% | 1.86x |
| 2 | PAXG/USD | 41.379 | 3555.19 | +0.26% | 0.79x |
| 3 | XAUT/USD | 35.419 | 3554.4 | +0.30% | 4.79x |
| 4 | BABY/USD | 34.278 | 0.00835 | -0.24% | 6.39x |

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

- Persisted scans: 1658; predictions: 14130; observations: 1004813.
- Matured sampled outcomes across 1/6/24/48h: 29662; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 144 (sampled only; not a success-rate estimate).
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

**Writer:** 45533937879 · **Generation:** 1658 · **Legacy run:** 45533937879
**Main quote time:** 2026-11-25T02:37:24.778811+00:00 · **Legacy report time:** 2026-11-25T02:38:37.996258+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.32957 | 87.62 | +2.14% | 1.86x | STRONG 99/100 | HIGH 60/100 | Consider small entry |
| 2 | XAUT/USD ⭐ | 3554.4 | 51.91 | +0.30% | 4.79x | STRONG 91/100 | HIGH 60/100 | Consider small entry |
| 3 | BABY/USD | 0.00835 | 48.08 | -0.24% | 6.39x | MODERATE 49/100 | VERY_HIGH 72/100 | Watch |
| 4 | PAXG/USD | 3555.19 | 40.52 | +0.26% | 0.79x | MODERATE 50/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.32858 | 82.60 | +2.14% | 1.86x | 6549 | STRONG 91/100 | HIGH 66/100 | Consider small entry |
| 2 | XAUT/USD ⭐ | 3554.4 | 43.58 | +0.30% | 4.79x | 1708 | STRONG 87/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** DRV/USD, XAUT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
