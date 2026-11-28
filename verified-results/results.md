# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T08:57:52.764747+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46127979646
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** b8076443c2b3e219a993a21818fa35f09b680753 (atomic ledger/results publication)
**Ledger generation:** 2132 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SPACE/USD | 0.004633 | 115.389 | 75.389 | +10.89% | +6.22% | 169.14x | 2.2 | 2026-11-28T08:57:49.612354+00:00 | Not calibrated | STRONG 100/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 2 | XMR/USD | 430.89 | 93.375 | 89.563 | +5.80% | +0.13% | 1.32x | 12.1 | 2026-11-28T08:57:49.612354+00:00 | Not calibrated | STRONG 77/100 | HIGH 61/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.05116 | 84.452 | 62.928 | +1.83% | +1.30% | 2.54x | 9.8 | 2026-11-28T08:57:49.612354+00:00 | Not calibrated | STRONG 97/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | VVV/USD | 26.339 | 48.367 | 56.664 | +2.29% | -1.05% | 0.70x | 7.6 | 2026-11-28T08:57:49.612354+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 5 | AKE/USD | 0.00113507 | 44.100 | 45.470 | +4.47% | +0.83% | 0.45x | 44.2 | 2026-11-28T08:57:49.612354+00:00 | Not calibrated | WEAK 37/100 | EXTREME 97/100 | Do nothing | WATCH |
| 6 | CC/USD | 0.07493 | 34.494 | 37.441 | +1.05% | +0.09% | 0.66x | 8.0 | 2026-11-28T08:57:49.612354+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 89.563 | 430.89 | +0.13% | 1.32x |
| 2 | SPACE/USD | 75.389 | 0.004633 | +6.22% | 169.14x |
| 3 | NIGHT/USD | 62.928 | 0.05116 | +1.30% | 2.54x |
| 4 | VVV/USD | 56.664 | 26.339 | -1.05% | 0.70x |
| 5 | AKE/USD | 45.470 | 0.00113507 | +0.83% | 0.45x |
| 6 | CC/USD | 37.441 | 0.07493 | +0.09% | 0.66x |

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

- Persisted scans: 2132; predictions: 19073; observations: 1291038.
- Matured sampled outcomes across 1/6/24/48h: 45011; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46127979646 · **Generation:** 2132 · **Legacy run:** 46127979646
**Main quote time:** 2026-11-28T08:57:52.764747+00:00 · **Legacy report time:** 2026-11-28T08:58:43.236873+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SPACE/USD ⭐ | 0.004633 | 115.39 | +6.22% | 169.14x | STRONG 100/100 | VERY_HIGH 77/100 | Watch |
| 2 | XMR/USD ⭐ | 430.89 | 93.37 | +0.13% | 1.32x | STRONG 87/100 | HIGH 61/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.05116 | 84.45 | +1.30% | 2.54x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | VVV/USD | 26.339 | 48.37 | -1.05% | 0.70x | WEAK 29/100 | VERY_HIGH 80/100 | Do nothing |
| 5 | AKE/USD | 0.00113507 | 44.10 | +0.83% | 0.45x | WEAK 37/100 | EXTREME 97/100 | Do nothing |
| 6 | CC/USD | 0.07493 | 34.49 | +0.09% | 0.66x | WEAK 37/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SPACE/USD ⭐ | 0.004692 | 97.63 | +6.22% | 169.14x | 2990 | STRONG 100/100 | VERY_HIGH 77/100 | Watch |
| 2 | XMR/USD ⭐ | 432.27 | 86.66 | +0.13% | 1.32x | 15201 | STRONG 73/100 | HIGH 67/100 | Watch |
| 3 | NIGHT/USD ⭐ | 0.05116 | 69.06 | +1.30% | 2.54x | 19214 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** SPACE/USD, XMR/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
