# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T09:26:26.498516+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45791687015
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** cc8ea12e58cc764ef3798df3ef3a30eab5969b7b (atomic ledger/results publication)
**Ledger generation:** 1842 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INJ/USD | 6.224 | 78.538 | 71.828 | +4.53% | -0.05% | 1.70x | 6.4 | 2026-11-26T09:26:18.393052+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 2 | QNT/USD | 147.73 | 73.049 | 60.234 | +2.02% | +0.17% | 2.20x | 6.1 | 2026-11-26T09:26:18.393052+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ETH/USD | 1697.4 | 72.953 | 57.865 | +0.41% | +0.02% | 3.00x | 0.1 | 2026-11-26T09:26:18.393052+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 4 | LTC/USD | 43.67 | 67.082 | 68.442 | +2.25% | -0.02% | 0.88x | 4.6 | 2026-11-26T09:26:18.393052+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 5 | XDG/USD | 0.0565689 | 66.623 | 57.984 | +1.09% | +0.00% | 1.86x | 0.0 | 2026-11-26T09:26:18.393052+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 6 | SEI/USD | 0.03535 | 64.538 | 69.355 | +6.12% | -0.20% | 0.62x | 11.3 | 2026-11-26T09:26:18.393052+00:00 | Not calibrated | WEAK 32/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | W/USD | 0.00871 | 64.398 | 60.720 | +4.94% | +0.69% | 1.02x | 11.5 | 2026-11-26T09:26:18.393052+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 8 | ADA/USD | 0.148637 | 64.109 | 67.590 | +1.97% | +0.20% | 0.55x | 2.4 | 2026-11-26T09:26:18.393052+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | AVAX/USD | 6.651 | 61.546 | 46.396 | +0.45% | +0.03% | 2.82x | 1.5 | 2026-11-26T09:26:18.393052+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XRP/USD | 0.95157 | 61.396 | 66.166 | +1.60% | -0.19% | 0.62x | 0.1 | 2026-11-26T09:26:18.393052+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | SYRUP/USD | 0.07079 | 57.885 | 63.925 | +6.82% | -0.96% | 0.88x | 26.8 | 2026-11-26T09:26:18.393052+00:00 | Not calibrated | WEAK 24/100 | EXTREME 85/100 | Do nothing | WATCH |
| 12 | LINK/USD | 9.21722 | 57.628 | 66.652 | +1.91% | -0.15% | 0.17x | 3.4 | 2026-11-26T09:26:18.393052+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 71.828 | 6.224 | -0.05% | 1.70x |
| 2 | SEI/USD | 69.355 | 0.03535 | -0.20% | 0.62x |
| 3 | LTC/USD | 68.442 | 43.67 | -0.02% | 0.88x |
| 4 | ADA/USD | 67.590 | 0.148637 | +0.20% | 0.55x |
| 5 | LINK/USD | 66.652 | 9.21722 | -0.15% | 0.17x |
| 6 | XRP/USD | 66.166 | 0.95157 | -0.19% | 0.62x |
| 7 | SYRUP/USD | 63.925 | 0.07079 | -0.96% | 0.88x |
| 8 | W/USD | 60.720 | 0.00871 | +0.69% | 1.02x |
| 9 | QNT/USD | 60.234 | 147.73 | +0.17% | 2.20x |
| 10 | XDG/USD | 57.984 | 0.0565689 | +0.00% | 1.86x |
| 11 | ETH/USD | 57.865 | 1697.4 | +0.02% | 3.00x |
| 12 | AVAX/USD | 46.396 | 6.651 | +0.03% | 2.82x |

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

- Persisted scans: 1842; predictions: 15839; observations: 1116820.
- Matured sampled outcomes across 1/6/24/48h: 34310; gap abstentions: 24448. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45791687015 · **Generation:** 1842 · **Legacy run:** 45791687015
**Main quote time:** 2026-11-26T09:26:26.498516+00:00 · **Legacy report time:** 2026-11-26T09:27:24.079481+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD | 6.224 | 78.54 | -0.05% | 1.70x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 2 | QNT/USD | 147.73 | 73.05 | +0.17% | 2.20x | STRONG 82/100 | HIGH 55/100 | Watch |
| 3 | ETH/USD | 1697.4 | 72.95 | +0.02% | 3.00x | STRONG 81/100 | HIGH 55/100 | Watch |
| 4 | LTC/USD | 43.67 | 67.08 | -0.02% | 0.88x | WEAK 39/100 | HIGH 68/100 | Watch |
| 5 | XDG/USD | 0.0565689 | 66.62 | +0.00% | 1.86x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 6 | SEI/USD | 0.03535 | 64.54 | -0.20% | 0.62x | WEAK 32/100 | EXTREME 87/100 | Do nothing |
| 7 | W/USD | 0.00871 | 64.40 | +0.69% | 1.02x | MODERATE 62/100 | VERY_HIGH 73/100 | Watch |
| 8 | ADA/USD | 0.148637 | 64.11 | +0.20% | 0.55x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 9 | AVAX/USD | 6.651 | 61.55 | +0.03% | 2.82x | STRONG 76/100 | HIGH 55/100 | Watch |
| 10 | XRP/USD | 0.95157 | 61.40 | -0.19% | 0.62x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 11 | SYRUP/USD | 0.07079 | 57.88 | -0.96% | 0.88x | WEAK 24/100 | EXTREME 85/100 | Do nothing |
| 12 | LINK/USD | 9.21722 | 57.63 | -0.15% | 0.17x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD | 3.9574 | 83.15 | +1.70% | 1.50x | 3233 | STRONG 72/100 | HIGH 67/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
