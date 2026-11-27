# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T05:01:53.968128+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45943097918
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ebf0f23242281461a6afd70bff2ab40f2db0561a (atomic ledger/results publication)
**Ledger generation:** 1962 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ETH/USD | 1733.33 | 87.507 | 73.905 | +2.70% | -0.28% | 3.44x | 0.1 | 2026-11-27T05:01:45.844680+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 2 | HYPE/USD | 66 | 86.374 | 96.011 | +6.08% | -0.11% | 0.09x | 3.0 | 2026-11-27T05:01:45.844680+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | ZEC/USD | 758.03 | 85.934 | 95.910 | +11.20% | -0.35% | 0.18x | 8.2 | 2026-11-27T05:01:45.844680+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | LINK/USD | 9.60401 | 80.997 | 77.512 | +3.62% | -0.15% | 1.42x | 5.7 | 2026-11-27T05:01:45.844680+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XRP/USD | 0.95988 | 73.973 | 67.667 | +1.82% | -0.22% | 1.74x | 0.1 | 2026-11-27T05:01:45.844680+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.1066 | 73.231 | 66.549 | +1.93% | -0.03% | 1.68x | 3.9 | 2026-11-27T05:01:45.844680+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0576572 | 72.511 | 58.641 | +2.28% | -0.23% | 4.66x | 0.2 | 2026-11-27T05:01:45.844680+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6833 | 67.996 | 70.623 | +2.34% | -0.12% | 0.80x | 1.5 | 2026-11-27T05:01:45.844680+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 9 | VVV/USD | 26.977 | 67.125 | 71.964 | +3.03% | +0.20% | 0.42x | 8.5 | 2026-11-27T05:01:45.844680+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SOL/USD | 72.77 | 64.114 | 72.370 | +2.58% | -0.27% | 0.31x | 1.4 | 2026-11-27T05:01:45.844680+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | LTC/USD | 44.65 | 62.112 | 67.324 | +2.08% | +0.11% | 0.42x | 4.5 | 2026-11-27T05:01:45.844680+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | ADA/USD | 0.15159 | 61.768 | 66.666 | +2.11% | -0.23% | 0.63x | 2.8 | 2026-11-27T05:01:45.844680+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | HYPE/USD | 96.011 | 66 | -0.11% | 0.09x |
| 2 | ZEC/USD | 95.910 | 758.03 | -0.35% | 0.18x |
| 3 | LINK/USD | 77.512 | 9.60401 | -0.15% | 1.42x |
| 4 | ETH/USD | 73.905 | 1733.33 | -0.28% | 3.44x |
| 5 | SOL/USD | 72.370 | 72.77 | -0.27% | 0.31x |
| 6 | VVV/USD | 71.964 | 26.977 | +0.20% | 0.42x |
| 7 | SUI/USD | 70.623 | 0.6833 | -0.12% | 0.80x |
| 8 | XRP/USD | 67.667 | 0.95988 | -0.22% | 1.74x |
| 9 | LTC/USD | 67.324 | 44.65 | +0.11% | 0.42x |
| 10 | ADA/USD | 66.666 | 0.15159 | -0.23% | 0.63x |
| 11 | NEAR/USD | 66.549 | 3.1066 | -0.03% | 1.68x |
| 12 | XDG/USD | 58.641 | 0.0576572 | -0.23% | 4.66x |

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

- Persisted scans: 1962; predictions: 17246; observations: 1188246.
- Matured sampled outcomes across 1/6/24/48h: 38006; gap abstentions: 25525. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 45943097918 · **Generation:** 1962 · **Legacy run:** 45943097918
**Main quote time:** 2026-11-27T05:01:53.968128+00:00 · **Legacy report time:** 2026-11-27T05:02:36.758910+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ETH/USD | 1733.33 | 87.51 | -0.28% | 3.44x | STRONG 74/100 | HIGH 61/100 | Watch |
| 2 | HYPE/USD | 66 | 86.37 | -0.11% | 0.09x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 3 | ZEC/USD | 758.03 | 85.93 | -0.35% | 0.18x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 4 | LINK/USD | 9.60401 | 81.00 | -0.15% | 1.42x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 5 | XRP/USD | 0.95988 | 73.97 | -0.22% | 1.74x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 6 | NEAR/USD | 3.1066 | 73.23 | -0.03% | 1.68x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 7 | XDG/USD | 0.0576572 | 72.51 | -0.23% | 4.66x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 8 | SUI/USD | 0.6833 | 68.00 | -0.12% | 0.80x | WEAK 39/100 | HIGH 68/100 | Watch |
| 9 | VVV/USD | 26.977 | 67.13 | +0.20% | 0.42x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 10 | SOL/USD | 72.77 | 64.11 | -0.27% | 0.31x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 11 | LTC/USD | 44.65 | 62.11 | +0.11% | 0.42x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 12 | ADA/USD | 0.15159 | 61.77 | -0.23% | 0.63x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
