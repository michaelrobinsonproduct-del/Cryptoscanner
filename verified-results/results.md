# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T05:11:19.887337+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45331303991
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 100a42f42f5984ce472efdb8969b56192dfef461 (atomic ledger/results publication)
**Ledger generation:** 1529 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEPE/USD | 3.56e-06 | 75.308 | 72.852 | +4.03% | +1.31% | 0.59x | 11.2 | 2026-11-24T05:11:12.168737+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | LINK/USD | 9.08065 | 75.264 | 60.881 | +0.84% | -0.12% | 7.52x | 0.0 | 2026-11-24T05:11:12.168737+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LTC/USD | 41.73 | 74.165 | 57.842 | +0.75% | +0.26% | 4.52x | 4.8 | 2026-11-24T05:11:12.168737+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | AI/USD | 0.01638 | 71.792 | 73.133 | +7.55% | +0.80% | 0.47x | 6.1 | 2026-11-24T05:11:12.168737+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | VVV/USD | 25.09 | 62.085 | 65.611 | +2.63% | +0.30% | 0.50x | 15.5 | 2026-11-24T05:11:12.168737+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | ADA/USD | 0.148931 | 62.055 | 56.175 | +0.33% | +0.27% | 1.46x | 2.2 | 2026-11-24T05:11:12.168737+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 7 | XRP/USD | 0.95342 | 60.675 | 64.825 | +1.49% | -0.02% | 0.59x | 1.3 | 2026-11-24T05:11:12.168737+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XMR/USD | 492.2 | 59.301 | 58.310 | +1.27% | +0.50% | 0.85x | 11.2 | 2026-11-24T05:11:12.168737+00:00 | Not calibrated | MODERATE 55/100 | HIGH 68/100 | Watch | WATCH |
| 9 | HYPE/USD | 63.81 | 57.129 | 56.087 | +0.27% | +0.05% | 1.08x | 1.6 | 2026-11-24T05:11:12.168737+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 10 | XDG/USD | 0.056581 | 56.925 | 56.972 | +0.49% | +0.13% | 0.93x | 2.9 | 2026-11-24T05:11:12.168737+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |
| 11 | DOT/USD | 0.6839 | 56.658 | 40.852 | +1.24% | +0.16% | 3.48x | 5.9 | 2026-11-24T05:11:12.168737+00:00 | Not calibrated | STRONG 73/100 | HIGH 60/100 | Watch | WATCH |
| 12 | UNI/USD | 4.9126 | 55.713 | 59.554 | +1.54% | +0.58% | 0.33x | 3.3 | 2026-11-24T05:11:12.168737+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AI/USD | 73.133 | 0.01638 | +0.80% | 0.47x |
| 2 | PEPE/USD | 72.852 | 3.56e-06 | +1.31% | 0.59x |
| 3 | VVV/USD | 65.611 | 25.09 | +0.30% | 0.50x |
| 4 | XRP/USD | 64.825 | 0.95342 | -0.02% | 0.59x |
| 5 | LINK/USD | 60.881 | 9.08065 | -0.12% | 7.52x |
| 6 | UNI/USD | 59.554 | 4.9126 | +0.58% | 0.33x |
| 7 | XMR/USD | 58.310 | 492.2 | +0.50% | 0.85x |
| 8 | LTC/USD | 57.842 | 41.73 | +0.26% | 4.52x |
| 9 | XDG/USD | 56.972 | 0.056581 | +0.13% | 0.93x |
| 10 | ADA/USD | 56.175 | 0.148931 | +0.27% | 1.46x |
| 11 | HYPE/USD | 56.087 | 63.81 | +0.05% | 1.08x |
| 12 | DOT/USD | 40.852 | 0.6839 | +0.16% | 3.48x |

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

- Persisted scans: 1529; predictions: 13081; observations: 926259.
- Matured sampled outcomes across 1/6/24/48h: 24437; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 136 (sampled only; not a success-rate estimate).
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

**Writer:** 45331303991 · **Generation:** 1529 · **Legacy run:** 45331303991
**Main quote time:** 2026-11-24T05:11:19.887337+00:00 · **Legacy report time:** 2026-11-24T05:12:11.186403+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEPE/USD | 3.56e-06 | 75.31 | +1.31% | 0.59x | MODERATE 63/100 | VERY_HIGH 76/100 | Watch |
| 2 | LINK/USD | 9.08065 | 75.26 | -0.12% | 7.52x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 3 | LTC/USD | 41.73 | 74.17 | +0.26% | 4.52x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 4 | AI/USD | 0.01638 | 71.79 | +0.80% | 0.47x | MODERATE 66/100 | VERY_HIGH 82/100 | Watch |
| 5 | VVV/USD | 25.09 | 62.09 | +0.30% | 0.50x | MODERATE 56/100 | VERY_HIGH 76/100 | Watch |
| 6 | ADA/USD | 0.148931 | 62.05 | +0.27% | 1.46x | STRONG 76/100 | HIGH 55/100 | Watch |
| 7 | XRP/USD | 0.95342 | 60.67 | -0.02% | 0.59x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 8 | XMR/USD | 492.2 | 59.30 | +0.50% | 0.85x | MODERATE 55/100 | HIGH 68/100 | Watch |
| 9 | HYPE/USD | 63.81 | 57.13 | +0.05% | 1.08x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 10 | XDG/USD | 0.056581 | 56.93 | +0.13% | 0.93x | MODERATE 48/100 | HIGH 62/100 | Watch |
| 11 | DOT/USD ⭐ | 0.6839 | 56.66 | +0.16% | 3.48x | STRONG 83/100 | HIGH 60/100 | Watch |
| 12 | UNI/USD | 4.9126 | 55.71 | +0.58% | 0.33x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DOT/USD ⭐ | 0.6839 | 60.52 | +0.16% | 3.48x | 9543 | STRONG 85/100 | HIGH 60/100 | Watch |

**Same-run overlap:** DOT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
