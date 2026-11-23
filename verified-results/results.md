# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T10:31:37.462855+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45156577487
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** dee4bc100c652bfdac2b02f908815da07492575f (atomic ledger/results publication)
**Ledger generation:** 1417 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 503.42 | 79.306 | 65.091 | +1.97% | -0.16% | 3.04x | 7.4 | 2026-11-23T10:31:30.676090+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SOL/USD | 72.27 | 77.312 | 70.562 | +2.32% | +0.01% | 1.67x | 1.4 | 2026-11-23T10:31:30.676090+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 3 | ALGO/USD | 0.08085 | 69.974 | 75.820 | +7.19% | -0.15% | 0.49x | 6.2 | 2026-11-23T10:31:30.676090+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | JUP/USD | 0.24204 | 68.917 | 75.874 | +7.78% | -0.09% | 0.35x | 8.7 | 2026-11-23T10:31:30.676090+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 5 | SUI/USD | 0.6679 | 67.933 | 67.276 | +1.86% | -0.12% | 1.13x | 1.5 | 2026-11-23T10:31:30.676090+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 6 | QNT/USD | 150.68 | 67.650 | 78.274 | +5.05% | -0.34% | 0.11x | 7.3 | 2026-11-23T10:31:30.676090+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 7 | PAXG/USD | 3607.05 | 64.950 | 50.570 | +0.98% | -0.12% | 18.22x | 1.0 | 2026-11-23T10:31:30.676090+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 8 | HYPE/USD | 63.9 | 61.823 | 63.542 | +1.33% | +0.20% | 0.73x | 1.6 | 2026-11-23T10:31:30.676090+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | DOT/USD | 0.6713 | 57.691 | 44.029 | +1.59% | -0.27% | 5.13x | 1.5 | 2026-11-23T10:31:30.676090+00:00 | Not calibrated | MODERATE 59/100 | HIGH 66/100 | Watch | WATCH |
| 10 | XRP/USD | 0.93946 | 56.939 | 63.943 | +1.29% | -0.17% | 0.39x | 0.1 | 2026-11-23T10:31:30.676090+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | XBT/USD | 61393.7 | 56.559 | 57.551 | +0.37% | +0.01% | 0.89x | 0.0 | 2026-11-23T10:31:30.676090+00:00 | Not calibrated | MODERATE 48/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XAUT/USD | 3604.9 | 54.233 | 39.760 | +0.92% | -0.11% | 7.96x | 0.6 | 2026-11-23T10:31:30.676090+00:00 | Not calibrated | MODERATE 57/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 78.274 | 150.68 | -0.34% | 0.11x |
| 2 | JUP/USD | 75.874 | 0.24204 | -0.09% | 0.35x |
| 3 | ALGO/USD | 75.820 | 0.08085 | -0.15% | 0.49x |
| 4 | SOL/USD | 70.562 | 72.27 | +0.01% | 1.67x |
| 5 | SUI/USD | 67.276 | 0.6679 | -0.12% | 1.13x |
| 6 | XMR/USD | 65.091 | 503.42 | -0.16% | 3.04x |
| 7 | XRP/USD | 63.943 | 0.93946 | -0.17% | 0.39x |
| 8 | HYPE/USD | 63.542 | 63.9 | +0.20% | 0.73x |
| 9 | XBT/USD | 57.551 | 61393.7 | +0.01% | 0.89x |
| 10 | PAXG/USD | 50.570 | 3607.05 | -0.12% | 18.22x |
| 11 | DOT/USD | 44.029 | 0.6713 | -0.27% | 5.13x |
| 12 | XAUT/USD | 39.760 | 3604.9 | -0.11% | 7.96x |

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

- Persisted scans: 1417; predictions: 11771; observations: 858056.
- Matured sampled outcomes across 1/6/24/48h: 19408; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
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

**Writer:** 45156577487 · **Generation:** 1417 · **Legacy run:** 45156577487
**Main quote time:** 2026-11-23T10:31:37.462855+00:00 · **Legacy report time:** 2026-11-23T10:32:44.252568+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 503.42 | 79.31 | -0.16% | 3.04x | STRONG 70/100 | HIGH 61/100 | Watch |
| 2 | SOL/USD | 72.27 | 77.31 | +0.01% | 1.67x | STRONG 74/100 | HIGH 55/100 | Watch |
| 3 | ALGO/USD | 0.08085 | 69.97 | -0.15% | 0.49x | WEAK 40/100 | VERY_HIGH 81/100 | Watch |
| 4 | JUP/USD | 0.24204 | 68.92 | -0.09% | 0.35x | WEAK 39/100 | VERY_HIGH 81/100 | Watch |
| 5 | SUI/USD | 0.6679 | 67.93 | -0.12% | 1.13x | WEAK 44/100 | HIGH 68/100 | Watch |
| 6 | QNT/USD | 150.68 | 67.65 | -0.34% | 0.11x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 7 | PAXG/USD | 3607.05 | 64.95 | -0.12% | 18.22x | MODERATE 62/100 | HIGH 61/100 | Watch |
| 8 | HYPE/USD | 63.9 | 61.82 | +0.20% | 0.73x | MODERATE 61/100 | VERY_HIGH 70/100 | Watch |
| 9 | DOT/USD | 0.6713 | 57.69 | -0.27% | 5.13x | MODERATE 59/100 | HIGH 66/100 | Watch |
| 10 | XRP/USD | 0.93946 | 56.94 | -0.17% | 0.39x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | XBT/USD | 61393.7 | 56.56 | +0.01% | 0.89x | MODERATE 48/100 | HIGH 62/100 | Watch |
| 12 | XAUT/USD | 3604.9 | 54.23 | -0.11% | 7.96x | MODERATE 57/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD | 0.07603 | 80.58 | +0.20% | 3.15x | 4046 | STRONG 85/100 | HIGH 60/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
