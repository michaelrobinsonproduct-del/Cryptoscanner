# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T21:04:00.418250+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46067300751
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 5707b7bd6c3e11712d23ed9e45add57da745089c (atomic ledger/results publication)
**Ledger generation:** 2060 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 737.34 | 88.753 | 97.896 | +8.17% | -0.46% | 0.32x | 4.2 | 2026-11-27T21:03:53.756287+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | SKY/USD | 0.05145 | 87.008 | 78.544 | +10.86% | -0.51% | 2.10x | 5.8 | 2026-11-27T21:03:53.756287+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 3 | TAO/USD | 188.566 | 84.477 | 64.613 | +2.60% | +0.97% | 84.34x | 17.2 | 2026-11-27T21:03:53.756287+00:00 | Not calibrated | STRONG 92/100 | HIGH 61/100 | Consider small entry | WATCH |
| 4 | RENDER/USD | 1.405 | 80.590 | 67.366 | +5.40% | -0.36% | 3.12x | 7.1 | 2026-11-27T21:03:53.756287+00:00 | Not calibrated | STRONG 70/100 | HIGH 66/100 | Watch | WATCH |
| 5 | HYPE/USD | 64.15 | 74.691 | 75.933 | +3.10% | -0.02% | 0.88x | 1.6 | 2026-11-27T21:03:53.756287+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 6 | NIGHT/USD | 0.05024 | 71.380 | 77.576 | +3.65% | +0.08% | 0.34x | 6.0 | 2026-11-27T21:03:53.756287+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SPACE/USD | 0.004168 | 71.194 | 69.852 | +7.64% | +0.27% | 1.00x | 12.0 | 2026-11-27T21:03:53.756287+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 8 | LTC/USD | 44.35 | 68.894 | 63.634 | +1.39% | -0.23% | 1.64x | 2.3 | 2026-11-27T21:03:53.756287+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XDG/USD | 0.057713 | 67.565 | 71.447 | +2.37% | -0.02% | 0.62x | 0.3 | 2026-11-27T21:03:53.756287+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | PEPE/USD | 3.53e-06 | 64.385 | 54.972 | +1.50% | -0.42% | 2.15x | 2.8 | 2026-11-27T21:03:53.756287+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 11 | SOL/USD | 71.95 | 61.186 | 64.271 | +1.42% | -0.10% | 0.74x | 1.4 | 2026-11-27T21:03:53.756287+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | XRP/USD | 0.94889 | 57.290 | 59.506 | +0.65% | -0.10% | 0.83x | 0.1 | 2026-11-27T21:03:53.756287+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.896 | 737.34 | -0.46% | 0.32x |
| 2 | SKY/USD | 78.544 | 0.05145 | -0.51% | 2.10x |
| 3 | NIGHT/USD | 77.576 | 0.05024 | +0.08% | 0.34x |
| 4 | HYPE/USD | 75.933 | 64.15 | -0.02% | 0.88x |
| 5 | XDG/USD | 71.447 | 0.057713 | -0.02% | 0.62x |
| 6 | SPACE/USD | 69.852 | 0.004168 | +0.27% | 1.00x |
| 7 | RENDER/USD | 67.366 | 1.405 | -0.36% | 3.12x |
| 8 | TAO/USD | 64.613 | 188.566 | +0.97% | 84.34x |
| 9 | SOL/USD | 64.271 | 71.95 | -0.10% | 0.74x |
| 10 | LTC/USD | 63.634 | 44.35 | -0.23% | 1.64x |
| 11 | XRP/USD | 59.506 | 0.94889 | -0.10% | 0.83x |
| 12 | PEPE/USD | 54.972 | 3.53e-06 | -0.42% | 2.15x |

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

- Persisted scans: 2060; predictions: 18422; observations: 1247409.
- Matured sampled outcomes across 1/6/24/48h: 41735; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46067300751 · **Generation:** 2060 · **Legacy run:** 46067300751
**Main quote time:** 2026-11-27T21:04:00.418250+00:00 · **Legacy report time:** 2026-11-27T21:05:02.627075+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 737.34 | 88.75 | -0.46% | 0.32x | MODERATE 49/100 | VERY_HIGH 76/100 | Watch |
| 2 | SKY/USD | 0.05145 | 87.01 | -0.51% | 2.10x | STRONG 74/100 | HIGH 66/100 | Watch |
| 3 | TAO/USD ⭐ | 188.566 | 84.48 | +0.97% | 84.34x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 4 | RENDER/USD | 1.405 | 80.59 | -0.36% | 3.12x | STRONG 70/100 | HIGH 66/100 | Watch |
| 5 | HYPE/USD | 64.15 | 74.69 | -0.02% | 0.88x | WEAK 42/100 | HIGH 68/100 | Watch |
| 6 | NIGHT/USD | 0.05024 | 71.38 | +0.08% | 0.34x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 7 | SPACE/USD | 0.004168 | 71.19 | +0.27% | 1.00x | MODERATE 66/100 | VERY_HIGH 80/100 | Watch |
| 8 | LTC/USD | 44.35 | 68.89 | -0.23% | 1.64x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 9 | XDG/USD | 0.057713 | 67.57 | -0.02% | 0.62x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 10 | PEPE/USD | 3.53e-06 | 64.39 | -0.42% | 2.15x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 11 | SOL/USD | 71.95 | 61.19 | -0.10% | 0.74x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 12 | XRP/USD | 0.94889 | 57.29 | -0.10% | 0.83x | WEAK 34/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 188.2883 | 79.91 | +1.83% | 22.55x | 8383 | STRONG 100/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** TAO/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
