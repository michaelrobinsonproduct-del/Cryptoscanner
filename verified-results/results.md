# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T08:57:22.874510+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45580433846
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** ec0cd95929679c5ed39c391a41a017533d2664b2 (atomic ledger/results publication)
**Ledger generation:** 1696 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | DRV/USD | 0.33823 | 96.972 | 73.126 | +7.62% | +1.77% | 3.80x | 18.9 | 2026-11-25T08:57:15.680354+00:00 | Not calibrated | STRONG 98/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | MON/USD | 0.0106 | 79.814 | 85.706 | +11.93% | -0.09% | 0.46x | 18.9 | 2026-11-25T08:57:15.680354+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | BABY/USD | 0.00888 | 77.144 | 71.033 | +7.51% | +2.90% | 0.16x | 11.3 | 2026-11-25T08:57:15.680354+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | PROS/USD | 0.7148 | 61.808 | 65.142 | +6.58% | +0.13% | 0.60x | 23.8 | 2026-11-25T08:57:15.680354+00:00 | Not calibrated | WEAK 41/100 | EXTREME 87/100 | Do nothing | WATCH |
| 5 | VVV/USD | 24.681 | 52.925 | 57.060 | +0.58% | -0.27% | 0.72x | 4.0 | 2026-11-25T08:57:15.680354+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | PEPE/USD | 3.48e-06 | 46.878 | 47.545 | +0.78% | -0.23% | 1.05x | 5.7 | 2026-11-25T08:57:15.680354+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 7 | ATOM/USD | 1.2607 | 27.661 | 34.465 | +1.23% | +0.10% | 0.27x | 12.7 | 2026-11-25T08:57:15.680354+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | MON/USD | 85.706 | 0.0106 | -0.09% | 0.46x |
| 2 | DRV/USD | 73.126 | 0.33823 | +1.77% | 3.80x |
| 3 | BABY/USD | 71.033 | 0.00888 | +2.90% | 0.16x |
| 4 | PROS/USD | 65.142 | 0.7148 | +0.13% | 0.60x |
| 5 | VVV/USD | 57.060 | 24.681 | -0.27% | 0.72x |
| 6 | PEPE/USD | 47.545 | 3.48e-06 | -0.23% | 1.05x |
| 7 | ATOM/USD | 34.465 | 1.2607 | +0.10% | 0.27x |

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

- Persisted scans: 1696; predictions: 14401; observations: 1027951.
- Matured sampled outcomes across 1/6/24/48h: 30971; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 17; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45580433846 · **Generation:** 1696 · **Legacy run:** 45580433846
**Main quote time:** 2026-11-25T08:57:22.874510+00:00 · **Legacy report time:** 2026-11-25T08:58:10.838624+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.33823 | 96.97 | +1.77% | 3.80x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | MON/USD | 0.0106 | 79.81 | -0.09% | 0.46x | WEAK 40/100 | VERY_HIGH 82/100 | Watch |
| 3 | BABY/USD | 0.00888 | 77.14 | +2.90% | 0.16x | MODERATE 64/100 | VERY_HIGH 81/100 | Watch |
| 4 | PROS/USD | 0.7148 | 61.81 | +0.13% | 0.60x | WEAK 41/100 | EXTREME 87/100 | Do nothing |
| 5 | VVV/USD | 24.681 | 52.93 | -0.27% | 0.72x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | PEPE/USD | 3.48e-06 | 46.88 | -0.23% | 1.05x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 7 | ATOM/USD | 1.2607 | 27.66 | +0.10% | 0.27x | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | DRV/USD ⭐ | 0.33823 | 91.04 | +1.77% | 3.80x | 9293 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** DRV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
