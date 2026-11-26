# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T05:06:11.798063+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45759193410
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** dd55333c8c82470bd9de92b094f6b362c62abfd8 (atomic ledger/results publication)
**Ledger generation:** 1816 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SYRUP/USD | 0.0716 | 72.425 | 68.013 | +8.04% | +0.94% | 0.97x | 18.2 | 2026-11-26T05:06:05.705846+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | PAXG/USD | 3587.81 | 72.264 | 57.634 | +0.51% | -0.07% | 8.95x | 1.8 | 2026-11-26T05:06:05.705846+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 3 | PEPE/USD | 3.563e-06 | 71.745 | 58.704 | +2.27% | -0.39% | 3.19x | 5.6 | 2026-11-26T05:06:05.705846+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 4 | LTC/USD | 43.83 | 70.185 | 72.217 | +2.62% | -0.32% | 0.96x | 2.3 | 2026-11-26T05:06:05.705846+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 5 | XRP/USD | 0.95868 | 63.264 | 71.481 | +2.36% | +0.06% | 0.15x | 0.1 | 2026-11-26T05:06:05.705846+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | QNT/USD | 145.46 | 61.657 | 48.822 | +0.46% | -0.43% | 8.28x | 4.8 | 2026-11-26T05:06:05.705846+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ADA/USD | 0.148651 | 61.286 | 67.221 | +1.98% | -0.28% | 0.55x | 3.2 | 2026-11-26T05:06:05.705846+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XAUT/USD | 3589.4 | 59.752 | 45.003 | +0.57% | -0.05% | 5.28x | 0.3 | 2026-11-26T05:06:05.705846+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 9 | LINK/USD | 9.2174 | 58.490 | 64.414 | +1.91% | -0.30% | 0.56x | 3.4 | 2026-11-26T05:06:05.705846+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 10 | HYPE/USD | 61.86 | 58.451 | 56.110 | +0.39% | -0.15% | 1.31x | 3.2 | 2026-11-26T05:06:05.705846+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 11 | SOL/USD | 71.1 | 57.793 | 61.357 | +1.01% | -0.01% | 0.65x | 1.4 | 2026-11-26T05:06:05.705846+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | SEI/USD | 0.03495 | 56.325 | 60.612 | +4.92% | -0.45% | 0.80x | 11.5 | 2026-11-26T05:06:05.705846+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 72.217 | 43.83 | -0.32% | 0.96x |
| 2 | XRP/USD | 71.481 | 0.95868 | +0.06% | 0.15x |
| 3 | SYRUP/USD | 68.013 | 0.0716 | +0.94% | 0.97x |
| 4 | ADA/USD | 67.221 | 0.148651 | -0.28% | 0.55x |
| 5 | LINK/USD | 64.414 | 9.2174 | -0.30% | 0.56x |
| 6 | SOL/USD | 61.357 | 71.1 | -0.01% | 0.65x |
| 7 | SEI/USD | 60.612 | 0.03495 | -0.45% | 0.80x |
| 8 | PEPE/USD | 58.704 | 3.563e-06 | -0.39% | 3.19x |
| 9 | PAXG/USD | 57.634 | 3587.81 | -0.07% | 8.95x |
| 10 | HYPE/USD | 56.110 | 61.86 | -0.15% | 1.31x |
| 11 | QNT/USD | 48.822 | 145.46 | -0.43% | 8.28x |
| 12 | XAUT/USD | 45.003 | 3589.4 | -0.05% | 5.28x |

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

- Persisted scans: 1816; predictions: 15527; observations: 1100988.
- Matured sampled outcomes across 1/6/24/48h: 33695; gap abstentions: 23924. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45759193410 · **Generation:** 1816 · **Legacy run:** 45759193410
**Main quote time:** 2026-11-26T05:06:11.798063+00:00 · **Legacy report time:** 2026-11-26T05:07:30.340488+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD | 0.0716 | 72.43 | +0.94% | 0.97x | MODERATE 61/100 | VERY_HIGH 73/100 | Watch |
| 2 | PAXG/USD | 3587.81 | 72.26 | -0.07% | 8.95x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 3 | PEPE/USD | 3.563e-06 | 71.75 | -0.39% | 3.19x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 4 | LTC/USD | 43.83 | 70.19 | -0.32% | 0.96x | WEAK 40/100 | HIGH 68/100 | Watch |
| 5 | XRP/USD | 0.95868 | 63.26 | +0.06% | 0.15x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 6 | QNT/USD | 145.46 | 61.66 | -0.43% | 8.28x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 7 | ADA/USD | 0.148651 | 61.29 | -0.28% | 0.55x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 8 | XAUT/USD | 3589.4 | 59.75 | -0.05% | 5.28x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 9 | LINK/USD | 9.2174 | 58.49 | -0.30% | 0.56x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 10 | HYPE/USD | 61.86 | 58.45 | -0.15% | 1.31x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 11 | SOL/USD | 71.1 | 57.79 | -0.01% | 0.65x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | SEI/USD | 0.03495 | 56.33 | -0.45% | 0.80x | WEAK 28/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PIEVERSE/USD | 3.829 | 74.40 | +0.92% | 1.30x | 2285 | MODERATE 67/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
