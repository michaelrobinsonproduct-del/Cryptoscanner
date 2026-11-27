# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T13:32:04.390751+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46007549844
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4bd61ee7f61402e9093473afc7e7b2d0d790d47a (atomic ledger/results publication)
**Ledger generation:** 2014 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 66.08 | 114.263 | 97.670 | +6.20% | +0.32% | 4.09x | 1.5 | 2026-11-27T13:31:58.126989+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 755.44 | 104.838 | 97.947 | +10.82% | +0.08% | 1.65x | 4.1 | 2026-11-27T13:31:58.126989+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 3 | SUI/USD | 0.6859 | 77.992 | 72.622 | +2.73% | -0.03% | 1.55x | 2.9 | 2026-11-27T13:31:58.126989+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 4 | VVV/USD | 27.253 | 77.225 | 76.417 | +4.09% | +0.04% | 1.06x | 8.5 | 2026-11-27T13:31:58.126989+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 5 | XRP/USD | 0.96989 | 76.617 | 74.842 | +2.88% | -0.07% | 1.21x | 0.6 | 2026-11-27T13:31:58.126989+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.62e-06 | 76.443 | 71.055 | +4.08% | -0.06% | 1.57x | 2.8 | 2026-11-27T13:31:58.126989+00:00 | Not calibrated | MODERATE 58/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XDG/USD | 0.058612 | 72.156 | 74.236 | +3.97% | +0.04% | 0.77x | 0.4 | 2026-11-27T13:31:58.126989+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XBT/USD | 61380.7 | 70.470 | 65.205 | +1.46% | -0.09% | 1.57x | 0.0 | 2026-11-27T13:31:58.126989+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 9 | SOL/USD | 73.17 | 70.004 | 76.321 | +3.14% | +0.10% | 0.32x | 1.4 | 2026-11-27T13:31:58.126989+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ETH/USD | 1717.13 | 67.828 | 66.603 | +1.75% | -0.11% | 1.18x | 1.2 | 2026-11-27T13:31:58.126989+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 11 | VIRTUAL/USD | 0.3861 | 66.919 | 71.160 | +5.96% | -0.16% | 0.65x | 5.2 | 2026-11-27T13:31:58.126989+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 12 | XLM/USD | 0.129217 | 56.695 | 56.588 | +2.06% | -0.09% | 1.06x | 0.2 | 2026-11-27T13:31:58.126989+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.947 | 755.44 | +0.08% | 1.65x |
| 2 | HYPE/USD | 97.670 | 66.08 | +0.32% | 4.09x |
| 3 | VVV/USD | 76.417 | 27.253 | +0.04% | 1.06x |
| 4 | SOL/USD | 76.321 | 73.17 | +0.10% | 0.32x |
| 5 | XRP/USD | 74.842 | 0.96989 | -0.07% | 1.21x |
| 6 | XDG/USD | 74.236 | 0.058612 | +0.04% | 0.77x |
| 7 | SUI/USD | 72.622 | 0.6859 | -0.03% | 1.55x |
| 8 | VIRTUAL/USD | 71.160 | 0.3861 | -0.16% | 0.65x |
| 9 | PEPE/USD | 71.055 | 3.62e-06 | -0.06% | 1.57x |
| 10 | ETH/USD | 66.603 | 1717.13 | -0.11% | 1.18x |
| 11 | XBT/USD | 65.205 | 61380.7 | -0.09% | 1.57x |
| 12 | XLM/USD | 56.588 | 0.129217 | -0.09% | 1.06x |

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

- Persisted scans: 2014; predictions: 17870; observations: 1219591.
- Matured sampled outcomes across 1/6/24/48h: 39821; gap abstentions: 25865. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 46007549844 · **Generation:** 2014 · **Legacy run:** 46007549844
**Main quote time:** 2026-11-27T13:32:04.390751+00:00 · **Legacy report time:** 2026-11-27T13:32:43.064146+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 66.08 | 114.26 | +0.32% | 4.09x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 755.44 | 104.84 | +0.08% | 1.65x | STRONG 95/100 | HIGH 55/100 | Watch |
| 3 | SUI/USD | 0.6859 | 77.99 | -0.03% | 1.55x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 4 | VVV/USD | 27.253 | 77.23 | +0.04% | 1.06x | MODERATE 64/100 | HIGH 62/100 | Watch |
| 5 | XRP/USD | 0.96989 | 76.62 | -0.07% | 1.21x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 6 | PEPE/USD | 3.62e-06 | 76.44 | -0.06% | 1.57x | MODERATE 58/100 | HIGH 61/100 | Watch |
| 7 | XDG/USD | 0.058612 | 72.16 | +0.04% | 0.77x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 8 | XBT/USD | 61380.7 | 70.47 | -0.09% | 1.57x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 9 | SOL/USD | 73.17 | 70.00 | +0.10% | 0.32x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 10 | ETH/USD | 1717.13 | 67.83 | -0.11% | 1.18x | WEAK 44/100 | HIGH 68/100 | Watch |
| 11 | VIRTUAL/USD | 0.3861 | 66.92 | -0.16% | 0.65x | WEAK 38/100 | VERY_HIGH 81/100 | Watch |
| 12 | XLM/USD | 0.129217 | 56.69 | -0.09% | 1.06x | WEAK 38/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD ⭐ | 66.03 | 100.00 | +0.32% | 4.09x | 15855 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 755.44 | 95.67 | +0.08% | 1.65x | 39457 | STRONG 93/100 | HIGH 55/100 | Watch |
| 3 | ADA/USD | 0.152278 | 83.68 | +0.17% | 3.38x | 9521 | STRONG 87/100 | HIGH 55/100 | Watch |
| 4 | TAO/USD | 189.5159 | 82.79 | +0.12% | 4.47x | 5703 | STRONG 86/100 | HIGH 55/100 | Watch |

**Same-run overlap:** HYPE/USD, ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
