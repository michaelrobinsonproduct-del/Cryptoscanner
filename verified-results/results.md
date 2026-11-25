# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T22:16:10.002433+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45711519026
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** afc0148292e01026d05a645ef1077ca0536d94ac (atomic ledger/results publication)
**Ledger generation:** 1774 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | LTC/USD | 42.36 | 92.696 | 79.695 | +3.70% | -0.40% | 2.84x | 2.4 | 2026-11-25T22:16:02.460681+00:00 | Not calibrated | STRONG 76/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0438 | 92.398 | 92.180 | +5.52% | +0.90% | 0.57x | 3.0 | 2026-11-25T22:16:02.460681+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | PAXG/USD | 3579.85 | 76.406 | 61.762 | +1.07% | -0.07% | 4.71x | 1.5 | 2026-11-25T22:16:02.460681+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XMR/USD | 520.41 | 75.929 | 63.789 | +2.12% | -0.57% | 4.82x | 12.1 | 2026-11-25T22:16:02.460681+00:00 | Not calibrated | MODERATE 63/100 | HIGH 67/100 | Watch | WATCH |
| 5 | LINK/USD | 9.04423 | 73.475 | 62.993 | +2.30% | -0.13% | 2.12x | 2.9 | 2026-11-25T22:16:02.460681+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 6 | ADA/USD | 0.145518 | 72.162 | 60.610 | +0.81% | -0.53% | 2.42x | 0.1 | 2026-11-25T22:16:02.460681+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XBT/USD | 60049.8 | 70.784 | 58.606 | +0.52% | -0.21% | 2.32x | 0.0 | 2026-11-25T22:16:02.460681+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6613 | 67.921 | 68.409 | +2.13% | -0.26% | 1.08x | 3.0 | 2026-11-25T22:16:02.460681+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 9 | HYPE/USD | 61.44 | 67.057 | 72.543 | +2.62% | -0.41% | 0.65x | 1.6 | 2026-11-25T22:16:02.460681+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | ZEC/USD | 756.02 | 61.578 | 66.994 | +2.32% | -1.04% | 0.98x | 8.5 | 2026-11-25T22:16:02.460681+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0558351 | 58.519 | 55.040 | +1.08% | -0.21% | 1.45x | 0.3 | 2026-11-25T22:16:02.460681+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 12 | SOL/USD | 70.44 | 57.819 | 62.738 | +1.21% | -0.26% | 0.64x | 1.4 | 2026-11-25T22:16:02.460681+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 92.180 | 3.0438 | +0.90% | 0.57x |
| 2 | LTC/USD | 79.695 | 42.36 | -0.40% | 2.84x |
| 3 | HYPE/USD | 72.543 | 61.44 | -0.41% | 0.65x |
| 4 | SUI/USD | 68.409 | 0.6613 | -0.26% | 1.08x |
| 5 | ZEC/USD | 66.994 | 756.02 | -1.04% | 0.98x |
| 6 | XMR/USD | 63.789 | 520.41 | -0.57% | 4.82x |
| 7 | LINK/USD | 62.993 | 9.04423 | -0.13% | 2.12x |
| 8 | SOL/USD | 62.738 | 70.44 | -0.26% | 0.64x |
| 9 | PAXG/USD | 61.762 | 3579.85 | -0.07% | 4.71x |
| 10 | ADA/USD | 60.610 | 0.145518 | -0.53% | 2.42x |
| 11 | XBT/USD | 58.606 | 60049.8 | -0.21% | 2.32x |
| 12 | XDG/USD | 55.040 | 0.0558351 | -0.21% | 1.45x |

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

- Persisted scans: 1774; predictions: 15032; observations: 1075410.
- Matured sampled outcomes across 1/6/24/48h: 32786; gap abstentions: 23233. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45711519026 · **Generation:** 1774 · **Legacy run:** 45711519026
**Main quote time:** 2026-11-25T22:16:10.002433+00:00 · **Legacy report time:** 2026-11-25T22:17:25.871129+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | LTC/USD | 42.36 | 92.70 | -0.40% | 2.84x | STRONG 76/100 | HIGH 61/100 | Watch |
| 2 | NEAR/USD | 3.0438 | 92.40 | +0.90% | 0.57x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 3 | PAXG/USD | 3579.85 | 76.41 | -0.07% | 4.71x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 4 | XMR/USD | 520.41 | 75.93 | -0.57% | 4.82x | MODERATE 63/100 | HIGH 67/100 | Watch |
| 5 | LINK/USD | 9.04423 | 73.48 | -0.13% | 2.12x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 6 | ADA/USD | 0.145518 | 72.16 | -0.53% | 2.42x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 7 | XBT/USD | 60049.8 | 70.78 | -0.21% | 2.32x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 8 | SUI/USD | 0.6613 | 67.92 | -0.26% | 1.08x | WEAK 44/100 | HIGH 68/100 | Watch |
| 9 | HYPE/USD | 61.44 | 67.06 | -0.41% | 0.65x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 10 | ZEC/USD | 756.02 | 61.58 | -1.04% | 0.98x | WEAK 36/100 | VERY_HIGH 72/100 | Watch |
| 11 | XDG/USD | 0.0558351 | 58.52 | -0.21% | 1.45x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 12 | SOL/USD | 70.44 | 57.82 | -0.26% | 0.64x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HBAR/USD | 0.05208 | 87.75 | +0.10% | 2.75x | 5977 | STRONG 89/100 | HIGH 60/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
