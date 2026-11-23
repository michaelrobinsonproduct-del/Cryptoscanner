# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T03:11:13.902339+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45104292338
**Source SHA:** 193371a597e6dbc5a6a884defbe9e1519a6a183a
**Previous ledger commit:** 11adeb15700f5eed79e35730d497f6c71069f08d (atomic ledger/results publication)
**Ledger generation:** 1373 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 14.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PAXG/USD | 3588.31 | 60.849 | 47.201 | +0.45% | +0.33% | 2.20x | 1.0 | 2026-11-23T03:11:09.201131+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 2 | AUD/USD | 0.66348 | 55.400 | 40.581 | +0.29% | -0.04% | 2.85x | 3.6 | 2026-11-23T03:11:09.201131+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 3 | BLESS/USD | 0.016831 | 47.460 | 54.572 | +4.59% | -0.10% | 0.34x | 32.1 | 2026-11-23T03:11:09.201131+00:00 | Not calibrated | WEAK 19/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | PEARL/USD | 2.0656 | 37.400 | 35.212 | +0.55% | +1.30% | 0.57x | 18.9 | 2026-11-23T03:11:09.201131+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 5 | DRV/USD | 0.37032 | 34.217 | 38.519 | +0.40% | -0.62% | 0.88x | 17.9 | 2026-11-23T03:11:09.201131+00:00 | Not calibrated | WEAK 17/100 | VERY_HIGH 74/100 | Do nothing | WATCH |
| 6 | CAP/USD | 0.094108 | 30.572 | 33.015 | +0.57% | +0.19% | 0.66x | 6.1 | 2026-11-23T03:11:09.201131+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | XAUT/USD | 3588.3 | 29.715 | 35.855 | +0.45% | +0.22% | 0.28x | 0.6 | 2026-11-23T03:11:09.201131+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | ICNT/USD | 0.3589 | 29.531 | 36.724 | +1.90% | -1.51% | 1.04x | 19.5 | 2026-11-23T03:11:09.201131+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 83/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | BLESS/USD | 54.572 | 0.016831 | -0.10% | 0.34x |
| 2 | PAXG/USD | 47.201 | 3588.31 | +0.33% | 2.20x |
| 3 | AUD/USD | 40.581 | 0.66348 | -0.04% | 2.85x |
| 4 | DRV/USD | 38.519 | 0.37032 | -0.62% | 0.88x |
| 5 | ICNT/USD | 36.724 | 0.3589 | -1.51% | 1.04x |
| 6 | XAUT/USD | 35.855 | 3588.3 | +0.22% | 0.28x |
| 7 | PEARL/USD | 35.212 | 2.0656 | +1.30% | 0.57x |
| 8 | CAP/USD | 33.015 | 0.094108 | +0.19% | 0.66x |

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

- Persisted scans: 1373; predictions: 11243; observations: 831262.
- Matured sampled outcomes across 1/6/24/48h: 18101; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 88 (sampled only; not a success-rate estimate).
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

**Writer:** 45104292338 · **Generation:** 1373 · **Legacy run:** 45104292338
**Main quote time:** 2026-11-23T03:11:13.902339+00:00 · **Legacy report time:** 2026-11-23T03:12:00.760814+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PAXG/USD ⭐ | 3588.31 | 60.85 | +0.33% | 2.20x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 2 | AUD/USD | 0.66348 | 55.40 | -0.04% | 2.85x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 3 | BLESS/USD | 0.016831 | 47.46 | -0.10% | 0.34x | WEAK 19/100 | EXTREME 88/100 | Do nothing |
| 4 | PEARL/USD | 2.0656 | 37.40 | +1.30% | 0.57x | WEAK 44/100 | VERY_HIGH 76/100 | Watch |
| 5 | DRV/USD | 0.37032 | 34.22 | -0.62% | 0.88x | WEAK 17/100 | VERY_HIGH 74/100 | Do nothing |
| 6 | CAP/USD | 0.094108 | 30.57 | +0.19% | 0.66x | WEAK 35/100 | VERY_HIGH 75/100 | Watch |
| 7 | XAUT/USD | 3588.3 | 29.71 | +0.22% | 0.28x | MODERATE 45/100 | VERY_HIGH 75/100 | Watch |
| 8 | ICNT/USD | 0.3589 | 29.53 | -1.51% | 1.04x | WEAK 20/100 | VERY_HIGH 83/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PAXG/USD ⭐ | 3591.97 | 56.09 | +0.33% | 2.20x | 7063 | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD | 4.7154 | 44.17 | +0.91% | 1.92x | 4603 | MODERATE 67/100 | HIGH 55/100 | Watch |

**Same-run overlap:** PAXG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
