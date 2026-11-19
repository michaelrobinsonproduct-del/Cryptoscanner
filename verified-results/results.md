# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T16:40:25.309035+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44568578186
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** b84eab0a60ccebb39f87e49583513da8e5800335 (atomic ledger/results publication)
**Ledger generation:** 815 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 598; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 22.649 | 78.237 | 83.504 | +4.51% | +0.22% | 0.36x | 6.2 | 2026-11-19T16:40:19.329443+00:00 | Not calibrated | MODERATE 69/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | TRUST/USD | 0.05443 | 72.711 | 75.285 | +10.63% | -0.22% | 0.85x | 1.8 | 2026-11-19T16:40:19.329443+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 3 | AKT/USD | 0.5466 | 66.618 | 64.638 | +5.52% | +0.79% | 0.80x | 11.0 | 2026-11-19T16:40:19.329443+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 4 | USELESS/USD | 0.10089 | 64.168 | 70.827 | +5.58% | -0.04% | 0.35x | 10.9 | 2026-11-19T16:40:19.329443+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 5 | HYPE/USD | 68.01 | 64.004 | 66.092 | +1.69% | +0.44% | 0.57x | 1.5 | 2026-11-19T16:40:19.329443+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | SKR/USD | 0.010366 | 63.867 | 70.748 | +7.61% | -0.30% | 0.46x | 10.6 | 2026-11-19T16:40:19.329443+00:00 | Not calibrated | WEAK 32/100 | EXTREME 94/100 | Do nothing | WATCH |
| 7 | BMT/USD | 0.02028 | 62.976 | 71.248 | +7.42% | +0.20% | 0.07x | 9.9 | 2026-11-19T16:40:19.329443+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 8 | PYTH/USD | 0.05634 | 62.916 | 68.311 | +6.79% | +0.28% | 0.32x | 17.8 | 2026-11-19T16:40:19.329443+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | XRP/USD | 0.97554 | 62.733 | 61.079 | +0.95% | +0.30% | 1.02x | 1.1 | 2026-11-19T16:40:19.329443+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 10 | ZEC/USD | 922.85 | 60.980 | 62.284 | +1.20% | +0.15% | 0.80x | 2.2 | 2026-11-19T16:40:19.329443+00:00 | Not calibrated | MODERATE 50/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0588524 | 60.654 | 51.522 | +0.25% | +0.16% | 1.83x | 0.0 | 2026-11-19T16:40:19.329443+00:00 | Not calibrated | MODERATE 65/100 | HIGH 55/100 | Watch | WATCH |
| 12 | ADA/USD | 0.153107 | 58.455 | 61.684 | +1.23% | +0.34% | 0.51x | 3.8 | 2026-11-19T16:40:19.329443+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 83.504 | 22.649 | +0.22% | 0.36x |
| 2 | TRUST/USD | 75.285 | 0.05443 | -0.22% | 0.85x |
| 3 | BMT/USD | 71.248 | 0.02028 | +0.20% | 0.07x |
| 4 | USELESS/USD | 70.827 | 0.10089 | -0.04% | 0.35x |
| 5 | SKR/USD | 70.748 | 0.010366 | -0.30% | 0.46x |
| 6 | PYTH/USD | 68.311 | 0.05634 | +0.28% | 0.32x |
| 7 | HYPE/USD | 66.092 | 68.01 | +0.44% | 0.57x |
| 8 | AKT/USD | 64.638 | 0.5466 | +0.79% | 0.80x |
| 9 | ZEC/USD | 62.284 | 922.85 | +0.15% | 0.80x |
| 10 | ADA/USD | 61.684 | 0.153107 | +0.34% | 0.51x |
| 11 | XRP/USD | 61.079 | 0.97554 | +0.30% | 1.02x |
| 12 | XDG/USD | 51.522 | 0.0588524 | +0.16% | 1.83x |

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

- Persisted scans: 815; predictions: 6924; observations: 492781.
- Matured sampled outcomes across 1/6/24/48h: 6899; gap abstentions: 15370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44568578186 · **Generation:** 815 · **Legacy run:** 44568578186
**Main quote time:** 2026-11-19T16:40:25.309035+00:00 · **Legacy report time:** 2026-11-19T16:41:21.500555+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD | 22.649 | 78.24 | +0.22% | 0.36x | MODERATE 69/100 | VERY_HIGH 70/100 | Watch |
| 2 | TRUST/USD | 0.05443 | 72.71 | -0.22% | 0.85x | WEAK 41/100 | VERY_HIGH 80/100 | Watch |
| 3 | AKT/USD | 0.5466 | 66.62 | +0.79% | 0.80x | MODERATE 58/100 | VERY_HIGH 80/100 | Watch |
| 4 | USELESS/USD | 0.10089 | 64.17 | -0.04% | 0.35x | WEAK 32/100 | VERY_HIGH 82/100 | Do nothing |
| 5 | HYPE/USD | 68.01 | 64.00 | +0.44% | 0.57x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 6 | SKR/USD | 0.010366 | 63.87 | -0.30% | 0.46x | WEAK 32/100 | EXTREME 94/100 | Do nothing |
| 7 | BMT/USD | 0.02028 | 62.98 | +0.20% | 0.07x | MODERATE 51/100 | VERY_HIGH 82/100 | Watch |
| 8 | PYTH/USD | 0.05634 | 62.92 | +0.28% | 0.32x | MODERATE 56/100 | VERY_HIGH 81/100 | Watch |
| 9 | XRP/USD | 0.97554 | 62.73 | +0.30% | 1.02x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 10 | ZEC/USD | 922.85 | 60.98 | +0.15% | 0.80x | MODERATE 50/100 | HIGH 62/100 | Watch |
| 11 | XDG/USD | 0.0588524 | 60.65 | +0.16% | 1.83x | MODERATE 65/100 | HIGH 55/100 | Watch |
| 12 | ADA/USD | 0.153107 | 58.46 | +0.34% | 0.51x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CAP/USD | 0.099516 | 81.99 | +3.13% | 2.40x | 7914 | STRONG 91/100 | VERY_HIGH 76/100 | Watch |
| 2 | INJ/USD | 7.16 | 66.95 | +0.62% | 1.13x | 6810 | MODERATE 68/100 | HIGH 62/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
