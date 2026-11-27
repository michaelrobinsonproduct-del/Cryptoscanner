# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T13:12:30.900602+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46004686118
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6bc20fb0b32fbbe66d2ceee40728d7b03c2619ec (atomic ledger/results publication)
**Ledger generation:** 2012 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 65.94 | 93.199 | 96.093 | +5.98% | +0.34% | 0.54x | 1.5 | 2026-11-27T13:12:23.555179+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | ZEC/USD | 757.69 | 91.299 | 98.018 | +11.15% | +0.07% | 0.29x | 4.0 | 2026-11-27T13:12:23.555179+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | VVV/USD | 27.306 | 89.025 | 78.999 | +4.29% | +0.17% | 1.92x | 6.6 | 2026-11-27T13:12:23.555179+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 4 | PEPE/USD | 3.645e-06 | 88.051 | 74.794 | +4.80% | +0.47% | 2.09x | 5.5 | 2026-11-27T13:12:23.555179+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | SOL/USD | 73.04 | 87.057 | 75.037 | +2.96% | +0.14% | 2.13x | 1.4 | 2026-11-27T13:12:23.555179+00:00 | Not calibrated | STRONG 89/100 | HIGH 55/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6862 | 82.795 | 72.937 | +2.77% | -0.03% | 2.00x | 2.9 | 2026-11-27T13:12:23.555179+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ETH/USD | 1720.14 | 78.241 | 68.260 | +1.92% | +0.18% | 1.91x | 0.4 | 2026-11-27T13:12:23.555179+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0585888 | 77.780 | 73.880 | +3.93% | +0.24% | 1.27x | 0.6 | 2026-11-27T13:12:23.555179+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 9 | XRP/USD | 0.97 | 69.665 | 74.975 | +2.89% | +0.00% | 0.47x | 0.5 | 2026-11-27T13:12:23.555179+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | XBT/USD | 61438.5 | 65.704 | 65.874 | +1.55% | +0.12% | 0.92x | 0.0 | 2026-11-27T13:12:23.555179+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 11 | BNB/USD | 563.19 | 63.414 | 47.578 | +1.77% | +0.17% | 2.86x | 0.2 | 2026-11-27T13:12:23.555179+00:00 | Not calibrated | STRONG 77/100 | HIGH 60/100 | Watch | WATCH |
| 12 | XAUT/USD | 3654.9 | 62.877 | 50.263 | +2.67% | +0.08% | 2.22x | 0.3 | 2026-11-27T13:12:23.555179+00:00 | Not calibrated | STRONG 76/100 | HIGH 60/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.018 | 757.69 | +0.07% | 0.29x |
| 2 | HYPE/USD | 96.093 | 65.94 | +0.34% | 0.54x |
| 3 | VVV/USD | 78.999 | 27.306 | +0.17% | 1.92x |
| 4 | SOL/USD | 75.037 | 73.04 | +0.14% | 2.13x |
| 5 | XRP/USD | 74.975 | 0.97 | +0.00% | 0.47x |
| 6 | PEPE/USD | 74.794 | 3.645e-06 | +0.47% | 2.09x |
| 7 | XDG/USD | 73.880 | 0.0585888 | +0.24% | 1.27x |
| 8 | SUI/USD | 72.937 | 0.6862 | -0.03% | 2.00x |
| 9 | ETH/USD | 68.260 | 1720.14 | +0.18% | 1.91x |
| 10 | XBT/USD | 65.874 | 61438.5 | +0.12% | 0.92x |
| 11 | XAUT/USD | 50.263 | 3654.9 | +0.08% | 2.22x |
| 12 | BNB/USD | 47.578 | 563.19 | +0.17% | 2.86x |

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

- Persisted scans: 2012; predictions: 17846; observations: 1218385.
- Matured sampled outcomes across 1/6/24/48h: 39749; gap abstentions: 25853. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 46004686118 · **Generation:** 2012 · **Legacy run:** 46004686118
**Main quote time:** 2026-11-27T13:12:30.900602+00:00 · **Legacy report time:** 2026-11-27T13:13:24.960215+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 65.94 | 93.20 | +0.34% | 0.54x | STRONG 77/100 | VERY_HIGH 70/100 | Watch |
| 2 | ZEC/USD | 757.69 | 91.30 | +0.07% | 0.29x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 3 | VVV/USD ⭐ | 27.306 | 89.02 | +0.17% | 1.92x | STRONG 90/100 | HIGH 55/100 | Watch |
| 4 | PEPE/USD ⭐ | 3.645e-06 | 88.05 | +0.47% | 2.09x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | SOL/USD ⭐ | 73.04 | 87.06 | +0.14% | 2.13x | STRONG 99/100 | HIGH 55/100 | Watch |
| 6 | SUI/USD | 0.6862 | 82.79 | -0.03% | 2.00x | STRONG 71/100 | HIGH 61/100 | Watch |
| 7 | ETH/USD ⭐ | 1720.14 | 78.24 | +0.18% | 1.91x | STRONG 84/100 | HIGH 55/100 | Watch |
| 8 | XDG/USD ⭐ | 0.0585888 | 77.78 | +0.24% | 1.27x | STRONG 84/100 | HIGH 55/100 | Watch |
| 9 | XRP/USD | 0.97 | 69.66 | +0.00% | 0.47x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 10 | XBT/USD | 61438.5 | 65.70 | +0.12% | 0.92x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 11 | BNB/USD | 563.19 | 63.41 | +0.17% | 2.86x | STRONG 77/100 | HIGH 60/100 | Watch |
| 12 | XAUT/USD | 3654.9 | 62.88 | +0.08% | 2.22x | STRONG 76/100 | HIGH 60/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XDG/USD ⭐ | 0.0585565 | 95.13 | +0.24% | 1.27x | 6043 | STRONG 93/100 | HIGH 55/100 | Watch |
| 2 | PEPE/USD ⭐ | 3.633e-06 | 93.59 | +0.47% | 2.09x | 5666 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | SOL/USD ⭐ | 73.04 | 89.73 | +0.14% | 2.13x | 34050 | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | VVV/USD ⭐ | 27.26 | 87.52 | +0.17% | 1.92x | 9373 | STRONG 89/100 | HIGH 55/100 | Watch |
| 5 | ETH/USD ⭐ | 1719.78 | 78.88 | +0.18% | 1.91x | 36036 | STRONG 84/100 | HIGH 55/100 | Watch |
| 6 | ADA/USD | 0.152038 | 75.05 | +0.11% | 1.52x | 9460 | STRONG 73/100 | HIGH 55/100 | Watch |

**Same-run overlap:** VVV/USD, PEPE/USD, SOL/USD, ETH/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
