# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T16:37:30.976292+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45655359246
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b886531c8a8a7e7f15cb65ff7b592bf761602131 (atomic ledger/results publication)
**Ledger generation:** 1739 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 608; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01059 | 98.491 | 78.698 | +11.83% | +3.34% | 1.31x | 19.0 | 2026-11-25T16:37:27.457573+00:00 | Not calibrated | STRONG 89/100 | VERY_HIGH 71/100 | Watch | WATCH |
| 2 | XPL/USD | 0.0455 | 55.617 | 48.478 | +3.41% | +0.66% | 1.38x | 21.9 | 2026-11-25T16:37:27.457573+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | PIEVERSE/USD | 3.3284 | 55.604 | 57.679 | +8.05% | -1.20% | 1.39x | 38.3 | 2026-11-25T16:37:27.457573+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 4 | VVV/USD | 24.982 | 55.053 | 64.255 | +1.81% | -0.07% | 0.12x | 6.8 | 2026-11-25T16:37:27.457573+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | DRV/USD | 0.32554 | 46.777 | 55.277 | +3.58% | -0.19% | 0.25x | 15.4 | 2026-11-25T16:37:27.457573+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 6 | ASTER/USD | 0.48245 | 36.700 | 32.025 | +0.34% | +0.97% | 0.98x | 5.4 | 2026-11-25T16:37:27.457573+00:00 | Not calibrated | MODERATE 48/100 | HIGH 67/100 | Watch | WATCH |
| 7 | CAP/USD | 0.092721 | 34.300 | 30.686 | +0.33% | +0.60% | 1.06x | 6.1 | 2026-11-25T16:37:27.457573+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 74/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 78.698 | 0.01059 | +3.34% | 1.31x |
| 2 | VVV/USD | 64.255 | 24.982 | -0.07% | 0.12x |
| 3 | PIEVERSE/USD | 57.679 | 3.3284 | -1.20% | 1.39x |
| 4 | DRV/USD | 55.277 | 0.32554 | -0.19% | 0.25x |
| 5 | XPL/USD | 48.478 | 0.0455 | +0.66% | 1.38x |
| 6 | ASTER/USD | 32.025 | 0.48245 | +0.97% | 0.98x |
| 7 | CAP/USD | 30.686 | 0.092721 | +0.60% | 1.06x |

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

- Persisted scans: 1739; predictions: 14631; observations: 1054097.
- Matured sampled outcomes across 1/6/24/48h: 32504; gap abstentions: 22396. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45655359246 · **Generation:** 1739 · **Legacy run:** 45655359246
**Main quote time:** 2026-11-25T16:37:30.976292+00:00 · **Legacy report time:** 2026-11-25T16:38:32.941805+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01059 | 98.49 | +3.34% | 1.31x | STRONG 99/100 | VERY_HIGH 71/100 | Watch |
| 2 | XPL/USD ⭐ | 0.0455 | 55.62 | +0.66% | 1.38x | STRONG 73/100 | VERY_HIGH 72/100 | Watch |
| 3 | PIEVERSE/USD | 3.3284 | 55.60 | -1.20% | 1.39x | WEAK 33/100 | VERY_HIGH 82/100 | Do nothing |
| 4 | VVV/USD | 24.982 | 55.05 | -0.07% | 0.12x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | DRV/USD | 0.32554 | 46.78 | -0.19% | 0.25x | WEAK 23/100 | VERY_HIGH 82/100 | Do nothing |
| 6 | ASTER/USD | 0.48245 | 36.70 | +0.97% | 0.98x | MODERATE 48/100 | HIGH 67/100 | Watch |
| 7 | CAP/USD ⭐ | 0.092721 | 34.30 | +0.60% | 1.06x | MODERATE 62/100 | VERY_HIGH 74/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01056 | 87.11 | +3.34% | 1.31x | 13942 | STRONG 94/100 | VERY_HIGH 71/100 | Watch |
| 2 | XPL/USD ⭐ | 0.0456 | 65.31 | +0.66% | 1.38x | 1776 | STRONG 78/100 | VERY_HIGH 72/100 | Watch |
| 3 | CAP/USD ⭐ | 0.092631 | 30.38 | +0.60% | 1.06x | 3345 | MODERATE 60/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** MON/USD, XPL/USD, CAP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
