# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T10:21:33.948010+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45155054294
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 66798bdc4a03f2df41f92307da2ee13ce5d22990 (atomic ledger/results publication)
**Ledger generation:** 1416 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ALGO/USD | 0.08038 | 91.627 | 76.378 | +6.56% | +0.05% | 3.69x | 5.0 | 2026-11-23T10:21:26.210404+00:00 | Not calibrated | STRONG 91/100 | HIGH 60/100 | Watch | WATCH |
| 2 | KAS/USD | 0.02722 | 79.609 | 70.691 | +5.46% | +0.15% | 1.82x | 3.7 | 2026-11-23T10:21:26.210404+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |
| 3 | SUI/USD | 0.6685 | 79.413 | 67.169 | +1.95% | -0.19% | 2.32x | 3.0 | 2026-11-23T10:21:26.210404+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 4 | QNT/USD | 150.56 | 77.353 | 78.230 | +4.96% | -1.12% | 1.47x | 6.0 | 2026-11-23T10:21:26.210404+00:00 | Not calibrated | MODERATE 59/100 | HIGH 65/100 | Watch | WATCH |
| 5 | JUP/USD | 0.24292 | 69.210 | 74.678 | +8.17% | -0.79% | 0.85x | 11.2 | 2026-11-23T10:21:26.210404+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 6 | PAXG/USD | 3608.15 | 66.556 | 51.481 | +1.01% | +0.01% | 16.11x | 0.1 | 2026-11-23T10:21:26.210404+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SOL/USD | 72.18 | 65.207 | 69.669 | +2.19% | -0.25% | 0.68x | 1.4 | 2026-11-23T10:21:26.210404+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XRP/USD | 0.93764 | 59.753 | 62.035 | +1.09% | -0.07% | 0.81x | 1.2 | 2026-11-23T10:21:26.210404+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XMR/USD | 502.65 | 58.081 | 65.885 | +1.81% | -0.20% | 0.32x | 3.6 | 2026-11-23T10:21:26.210404+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | XAUT/USD | 3608.1 | 55.787 | 40.482 | +1.01% | +0.06% | 3.73x | 0.3 | 2026-11-23T10:21:26.210404+00:00 | Not calibrated | STRONG 73/100 | HIGH 60/100 | Watch | WATCH |
| 11 | HYPE/USD | 63.58 | 55.745 | 59.986 | +0.82% | -0.27% | 0.71x | 1.6 | 2026-11-23T10:21:26.210404+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | XLM/USD | 0.128307 | 55.440 | 57.827 | +0.61% | -0.04% | 0.78x | 2.0 | 2026-11-23T10:21:26.210404+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 78.230 | 150.56 | -1.12% | 1.47x |
| 2 | ALGO/USD | 76.378 | 0.08038 | +0.05% | 3.69x |
| 3 | JUP/USD | 74.678 | 0.24292 | -0.79% | 0.85x |
| 4 | KAS/USD | 70.691 | 0.02722 | +0.15% | 1.82x |
| 5 | SOL/USD | 69.669 | 72.18 | -0.25% | 0.68x |
| 6 | SUI/USD | 67.169 | 0.6685 | -0.19% | 2.32x |
| 7 | XMR/USD | 65.885 | 502.65 | -0.20% | 0.32x |
| 8 | XRP/USD | 62.035 | 0.93764 | -0.07% | 0.81x |
| 9 | HYPE/USD | 59.986 | 63.58 | -0.27% | 0.71x |
| 10 | XLM/USD | 57.827 | 0.128307 | -0.04% | 0.78x |
| 11 | PAXG/USD | 51.481 | 3608.15 | +0.01% | 16.11x |
| 12 | XAUT/USD | 40.482 | 3608.1 | +0.06% | 3.73x |

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

- Persisted scans: 1416; predictions: 11759; observations: 857447.
- Matured sampled outcomes across 1/6/24/48h: 19366; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 130 (sampled only; not a success-rate estimate).
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

**Writer:** 45155054294 · **Generation:** 1416 · **Legacy run:** 45155054294
**Main quote time:** 2026-11-23T10:21:33.948010+00:00 · **Legacy report time:** 2026-11-23T10:22:19.128942+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD | 0.08038 | 91.63 | +0.05% | 3.69x | STRONG 91/100 | HIGH 60/100 | Watch |
| 2 | KAS/USD ⭐ | 0.02722 | 79.61 | +0.15% | 1.82x | STRONG 85/100 | HIGH 60/100 | Watch |
| 3 | SUI/USD | 0.6685 | 79.41 | -0.19% | 2.32x | STRONG 70/100 | HIGH 61/100 | Watch |
| 4 | QNT/USD | 150.56 | 77.35 | -1.12% | 1.47x | MODERATE 59/100 | HIGH 65/100 | Watch |
| 5 | JUP/USD | 0.24292 | 69.21 | -0.79% | 0.85x | WEAK 35/100 | VERY_HIGH 79/100 | Watch |
| 6 | PAXG/USD | 3608.15 | 66.56 | +0.01% | 16.11x | STRONG 78/100 | HIGH 55/100 | Watch |
| 7 | SOL/USD | 72.18 | 65.21 | -0.25% | 0.68x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 8 | XRP/USD | 0.93764 | 59.75 | -0.07% | 0.81x | WEAK 35/100 | HIGH 68/100 | Watch |
| 9 | XMR/USD | 502.65 | 58.08 | -0.20% | 0.32x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | XAUT/USD | 3608.1 | 55.79 | +0.06% | 3.73x | STRONG 73/100 | HIGH 60/100 | Watch |
| 11 | HYPE/USD | 63.58 | 55.74 | -0.27% | 0.71x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | XLM/USD | 0.128307 | 55.44 | -0.04% | 0.78x | WEAK 33/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | KAS/USD ⭐ | 0.02719 | 76.28 | +0.15% | 1.82x | 3167 | STRONG 78/100 | HIGH 66/100 | Watch |

**Same-run overlap:** KAS/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
