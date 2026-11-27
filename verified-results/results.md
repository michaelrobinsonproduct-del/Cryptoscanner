# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T06:51:34.188503+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45954347184
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** dbea66e4ef47fdce6f58b5e5231de274f15a49d2 (atomic ledger/results publication)
**Ledger generation:** 1973 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 747.65 | 106.022 | 98.193 | +9.68% | -1.43% | 9.07x | 3.6 | 2026-11-27T06:51:25.439613+00:00 | Not calibrated | STRONG 80/100 | HIGH 65/100 | Do nothing | WATCH |
| 2 | HYPE/USD | 66.01 | 102.787 | 96.882 | +6.09% | -0.27% | 1.73x | 1.5 | 2026-11-27T06:51:25.439613+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | ADA/USD | 0.152808 | 78.653 | 70.964 | +2.93% | -0.22% | 1.88x | 3.1 | 2026-11-27T06:51:25.439613+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LINK/USD | 9.59435 | 76.120 | 78.302 | +3.52% | -0.42% | 0.99x | 2.6 | 2026-11-27T06:51:25.439613+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 5 | ETH/USD | 1731.15 | 73.378 | 73.001 | +2.58% | -0.19% | 1.14x | 0.1 | 2026-11-27T06:51:25.439613+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 6 | W/USD | 0.00976 | 72.032 | 68.182 | +10.78% | +1.35% | 0.71x | 20.5 | 2026-11-27T06:51:25.439613+00:00 | Not calibrated | MODERATE 56/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | SOL/USD | 72.92 | 69.229 | 73.852 | +2.79% | -0.07% | 0.57x | 1.4 | 2026-11-27T06:51:25.439613+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XRP/USD | 0.97058 | 68.956 | 75.612 | +2.95% | -0.01% | 0.34x | 0.1 | 2026-11-27T06:51:25.439613+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | XBT/USD | 61605 | 67.745 | 67.801 | +1.83% | -0.18% | 1.08x | 0.0 | 2026-11-27T06:51:25.439613+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0580463 | 66.728 | 66.476 | +2.97% | -0.15% | 1.10x | 0.3 | 2026-11-27T06:51:25.439613+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XAUT/USD | 3642.7 | 63.779 | 49.218 | +2.33% | -0.09% | 4.02x | 0.3 | 2026-11-27T06:51:25.439613+00:00 | Not calibrated | MODERATE 62/100 | HIGH 66/100 | Watch | WATCH |
| 12 | DOT/USD | 0.6898 | 57.485 | 50.236 | +2.57% | -0.17% | 1.81x | 1.5 | 2026-11-27T06:51:25.439613+00:00 | Not calibrated | MODERATE 49/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.193 | 747.65 | -1.43% | 9.07x |
| 2 | HYPE/USD | 96.882 | 66.01 | -0.27% | 1.73x |
| 3 | LINK/USD | 78.302 | 9.59435 | -0.42% | 0.99x |
| 4 | XRP/USD | 75.612 | 0.97058 | -0.01% | 0.34x |
| 5 | SOL/USD | 73.852 | 72.92 | -0.07% | 0.57x |
| 6 | ETH/USD | 73.001 | 1731.15 | -0.19% | 1.14x |
| 7 | ADA/USD | 70.964 | 0.152808 | -0.22% | 1.88x |
| 8 | W/USD | 68.182 | 0.00976 | +1.35% | 0.71x |
| 9 | XBT/USD | 67.801 | 61605 | -0.18% | 1.08x |
| 10 | XDG/USD | 66.476 | 0.0580463 | -0.15% | 1.10x |
| 11 | DOT/USD | 50.236 | 0.6898 | -0.17% | 1.81x |
| 12 | XAUT/USD | 49.218 | 3642.7 | -0.09% | 4.02x |

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

- Persisted scans: 1973; predictions: 17378; observations: 1194872.
- Matured sampled outcomes across 1/6/24/48h: 38385; gap abstentions: 25592. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45954347184 · **Generation:** 1973 · **Legacy run:** 45954347184
**Main quote time:** 2026-11-27T06:51:34.188503+00:00 · **Legacy report time:** 2026-11-27T06:52:16.705851+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 747.65 | 106.02 | -1.43% | 9.07x | STRONG 80/100 | HIGH 65/100 | Do nothing |
| 2 | HYPE/USD | 66.01 | 102.79 | -0.27% | 1.73x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | ADA/USD | 0.152808 | 78.65 | -0.22% | 1.88x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 4 | LINK/USD | 9.59435 | 76.12 | -0.42% | 0.99x | WEAK 43/100 | HIGH 68/100 | Watch |
| 5 | ETH/USD | 1731.15 | 73.38 | -0.19% | 1.14x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 6 | W/USD | 0.00976 | 72.03 | +1.35% | 0.71x | MODERATE 56/100 | EXTREME 87/100 | Do nothing |
| 7 | SOL/USD | 72.92 | 69.23 | -0.07% | 0.57x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 8 | XRP/USD | 0.97058 | 68.96 | -0.01% | 0.34x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 9 | XBT/USD | 61605 | 67.75 | -0.18% | 1.08x | WEAK 44/100 | HIGH 68/100 | Watch |
| 10 | XDG/USD | 0.0580463 | 66.73 | -0.15% | 1.10x | WEAK 43/100 | HIGH 68/100 | Watch |
| 11 | XAUT/USD | 3642.7 | 63.78 | -0.09% | 4.02x | MODERATE 62/100 | HIGH 66/100 | Watch |
| 12 | DOT/USD | 0.6898 | 57.49 | -0.17% | 1.81x | MODERATE 49/100 | HIGH 66/100 | Watch |

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
