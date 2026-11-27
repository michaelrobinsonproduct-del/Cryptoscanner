# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T14:42:17.666247+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46017898104
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** cfb9df0b3b66dcdc6221000f2d7d0cc2b1511e87 (atomic ledger/results publication)
**Ledger generation:** 2021 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 604; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 728.23 | 87.693 | 89.967 | +6.83% | -3.06% | 2.31x | 20.1 | 2026-11-27T14:42:09.631961+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 2 | HYPE/USD | 63.75 | 68.893 | 70.647 | +2.46% | -3.06% | 2.35x | 3.1 | 2026-11-27T14:42:09.631961+00:00 | Not calibrated | MODERATE 64/100 | HIGH 65/100 | Do nothing | WATCH |
| 3 | PAXG/USD | 3617.6 | 65.683 | 52.622 | +1.71% | -0.39% | 7.96x | 1.4 | 2026-11-27T14:42:09.631961+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 4 | UNI/USD | 4.7824 | 65.145 | 60.346 | +2.85% | -2.04% | 20.87x | 25.2 | 2026-11-27T14:42:09.631961+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 5 | SOL/USD | 71.39 | 64.158 | 58.740 | +0.63% | -1.92% | 6.48x | 1.4 | 2026-11-27T14:42:09.631961+00:00 | Not calibrated | MODERATE 62/100 | HIGH 65/100 | Do nothing | WATCH |
| 6 | XRP/USD | 0.94646 | 63.273 | 55.852 | +0.39% | -1.52% | 6.37x | 3.8 | 2026-11-27T14:42:09.631961+00:00 | Not calibrated | MODERATE 62/100 | HIGH 65/100 | Do nothing | WATCH |
| 7 | XDG/USD | 0.0572416 | 62.305 | 57.611 | +1.54% | -2.06% | 6.85x | 2.8 | 2026-11-27T14:42:09.631961+00:00 | Not calibrated | MODERATE 61/100 | HIGH 65/100 | Do nothing | WATCH |
| 8 | XAUT/USD | 3618.4 | 61.561 | 47.939 | +1.65% | -0.28% | 377.78x | 0.3 | 2026-11-27T14:42:09.631961+00:00 | Not calibrated | MODERATE 61/100 | HIGH 66/100 | Watch | WATCH |
| 9 | FET/USD | 0.1259 | 59.886 | 55.011 | +4.57% | -2.02% | 3.92x | 23.9 | 2026-11-27T14:42:09.631961+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 10 | VIRTUAL/USD | 0.3752 | 57.529 | 51.703 | +2.96% | -1.48% | 2.32x | 2.7 | 2026-11-27T14:42:09.631961+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 11 | VVV/USD | 26.645 | 52.922 | 62.932 | +1.76% | -2.00% | 1.00x | 1.5 | 2026-11-27T14:42:09.631961+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 72/100 | Do nothing | WATCH |
| 12 | NIGHT/USD | 0.0487 | 51.361 | 52.294 | +0.47% | -1.15% | 1.48x | 6.2 | 2026-11-27T14:42:09.631961+00:00 | Not calibrated | MODERATE 46/100 | HIGH 65/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 89.967 | 728.23 | -3.06% | 2.31x |
| 2 | HYPE/USD | 70.647 | 63.75 | -3.06% | 2.35x |
| 3 | VVV/USD | 62.932 | 26.645 | -2.00% | 1.00x |
| 4 | UNI/USD | 60.346 | 4.7824 | -2.04% | 20.87x |
| 5 | SOL/USD | 58.740 | 71.39 | -1.92% | 6.48x |
| 6 | XDG/USD | 57.611 | 0.0572416 | -2.06% | 6.85x |
| 7 | XRP/USD | 55.852 | 0.94646 | -1.52% | 6.37x |
| 8 | FET/USD | 55.011 | 0.1259 | -2.02% | 3.92x |
| 9 | PAXG/USD | 52.622 | 3617.6 | -0.39% | 7.96x |
| 10 | NIGHT/USD | 52.294 | 0.0487 | -1.15% | 1.48x |
| 11 | VIRTUAL/USD | 51.703 | 0.3752 | -1.48% | 2.32x |
| 12 | XAUT/USD | 47.939 | 3618.4 | -0.28% | 377.78x |

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

- Persisted scans: 2021; predictions: 17954; observations: 1223816.
- Matured sampled outcomes across 1/6/24/48h: 40085; gap abstentions: 25904. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 46017898104 · **Generation:** 2021 · **Legacy run:** 46017898104
**Main quote time:** 2026-11-27T14:42:17.666247+00:00 · **Legacy report time:** 2026-11-27T14:43:11.757136+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 728.23 | 87.69 | -3.06% | 2.31x | MODERATE 64/100 | VERY_HIGH 77/100 | Do nothing |
| 2 | HYPE/USD | 63.75 | 68.89 | -3.06% | 2.35x | MODERATE 64/100 | HIGH 65/100 | Do nothing |
| 3 | PAXG/USD | 3617.6 | 65.68 | -0.39% | 7.96x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 4 | UNI/USD | 4.7824 | 65.14 | -2.04% | 20.87x | MODERATE 53/100 | VERY_HIGH 77/100 | Do nothing |
| 5 | SOL/USD | 71.39 | 64.16 | -1.92% | 6.48x | MODERATE 62/100 | HIGH 65/100 | Do nothing |
| 6 | XRP/USD | 0.94646 | 63.27 | -1.52% | 6.37x | MODERATE 62/100 | HIGH 65/100 | Do nothing |
| 7 | XDG/USD | 0.0572416 | 62.30 | -2.06% | 6.85x | MODERATE 61/100 | HIGH 65/100 | Do nothing |
| 8 | XAUT/USD | 3618.4 | 61.56 | -0.28% | 377.78x | MODERATE 61/100 | HIGH 66/100 | Watch |
| 9 | FET/USD | 0.1259 | 59.89 | -2.02% | 3.92x | MODERATE 50/100 | VERY_HIGH 82/100 | Do nothing |
| 10 | VIRTUAL/USD | 0.3752 | 57.53 | -1.48% | 2.32x | MODERATE 59/100 | VERY_HIGH 70/100 | Do nothing |
| 11 | VVV/USD | 26.645 | 52.92 | -2.00% | 1.00x | WEAK 31/100 | VERY_HIGH 72/100 | Do nothing |
| 12 | NIGHT/USD | 0.0487 | 51.36 | -1.15% | 1.48x | MODERATE 46/100 | HIGH 65/100 | Watch |

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
