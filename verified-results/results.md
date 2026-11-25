# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T20:06:19.605040+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45691407728
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 3961fe29bd53c1ea748fb1a0f9105ea06d1afbb6 (atomic ledger/results publication)
**Ledger generation:** 1761 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 2.9415 | 78.337 | 65.431 | +1.98% | +1.01% | 1.79x | 6.8 | 2026-11-25T20:06:10.372525+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 752.69 | 70.983 | 65.812 | +1.87% | +0.62% | 1.21x | 4.5 | 2026-11-25T20:06:10.372525+00:00 | Not calibrated | STRONG 70/100 | HIGH 62/100 | Watch | WATCH |
| 3 | LTC/USD | 42.3 | 68.547 | 77.481 | +3.55% | -0.12% | 0.17x | 4.7 | 2026-11-25T20:06:10.372525+00:00 | Not calibrated | WEAK 39/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | CT/USD | 0.1345 | 66.340 | 64.831 | +6.49% | +0.68% | 0.81x | 22.4 | 2026-11-25T20:06:10.372525+00:00 | Not calibrated | MODERATE 53/100 | EXTREME 86/100 | Do nothing | WATCH |
| 5 | HYPE/USD | 61.2 | 66.004 | 68.914 | +2.22% | +0.26% | 0.58x | 3.3 | 2026-11-25T20:06:10.372525+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XPL/USD | 0.0479 | 63.814 | 71.912 | +8.86% | -0.21% | 0.29x | 20.9 | 2026-11-25T20:06:10.372525+00:00 | Not calibrated | WEAK 27/100 | EXTREME 88/100 | Do nothing | WATCH |
| 7 | SUI/USD | 0.6608 | 62.844 | 67.862 | +2.05% | -0.14% | 0.57x | 3.0 | 2026-11-25T20:06:10.372525+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | XRP/USD | 0.936 | 61.231 | 63.696 | +1.34% | -0.20% | 0.85x | 1.4 | 2026-11-25T20:06:10.372525+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 9 | PUMP/USD | 0.002525 | 59.361 | 60.208 | +3.53% | +0.88% | 0.48x | 11.9 | 2026-11-25T20:06:10.372525+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | XMR/USD | 517.26 | 57.863 | 62.521 | +1.50% | +0.20% | 0.43x | 6.0 | 2026-11-25T20:06:10.372525+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | LINK/USD | 9.06205 | 56.430 | 63.378 | +2.50% | +0.02% | 0.30x | 4.1 | 2026-11-25T20:06:10.372525+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SOL/USD | 70.24 | 55.621 | 60.013 | +0.92% | +0.06% | 0.53x | 2.8 | 2026-11-25T20:06:10.372525+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 77.481 | 42.3 | -0.12% | 0.17x |
| 2 | XPL/USD | 71.912 | 0.0479 | -0.21% | 0.29x |
| 3 | HYPE/USD | 68.914 | 61.2 | +0.26% | 0.58x |
| 4 | SUI/USD | 67.862 | 0.6608 | -0.14% | 0.57x |
| 5 | ZEC/USD | 65.812 | 752.69 | +0.62% | 1.21x |
| 6 | NEAR/USD | 65.431 | 2.9415 | +1.01% | 1.79x |
| 7 | CT/USD | 64.831 | 0.1345 | +0.68% | 0.81x |
| 8 | XRP/USD | 63.696 | 0.936 | -0.20% | 0.85x |
| 9 | LINK/USD | 63.378 | 9.06205 | +0.02% | 0.30x |
| 10 | XMR/USD | 62.521 | 517.26 | +0.20% | 0.43x |
| 11 | PUMP/USD | 60.208 | 0.002525 | +0.88% | 0.48x |
| 12 | SOL/USD | 60.013 | 70.24 | +0.06% | 0.53x |

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

- Persisted scans: 1761; predictions: 14876; observations: 1067493.
- Matured sampled outcomes across 1/6/24/48h: 32618; gap abstentions: 22920. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45691407728 · **Generation:** 1761 · **Legacy run:** 45691407728
**Main quote time:** 2026-11-25T20:06:19.605040+00:00 · **Legacy report time:** 2026-11-25T20:07:21.897319+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 2.9415 | 78.34 | +1.01% | 1.79x | STRONG 84/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD | 752.69 | 70.98 | +0.62% | 1.21x | STRONG 70/100 | HIGH 62/100 | Watch |
| 3 | LTC/USD | 42.3 | 68.55 | -0.12% | 0.17x | WEAK 39/100 | VERY_HIGH 76/100 | Watch |
| 4 | CT/USD | 0.1345 | 66.34 | +0.68% | 0.81x | MODERATE 53/100 | EXTREME 86/100 | Do nothing |
| 5 | HYPE/USD | 61.2 | 66.00 | +0.26% | 0.58x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 6 | XPL/USD | 0.0479 | 63.81 | -0.21% | 0.29x | WEAK 27/100 | EXTREME 88/100 | Do nothing |
| 7 | SUI/USD | 0.6608 | 62.84 | -0.14% | 0.57x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 8 | XRP/USD | 0.936 | 61.23 | -0.20% | 0.85x | WEAK 36/100 | HIGH 68/100 | Watch |
| 9 | PUMP/USD | 0.002525 | 59.36 | +0.88% | 0.48x | MODERATE 55/100 | VERY_HIGH 76/100 | Watch |
| 10 | XMR/USD | 517.26 | 57.86 | +0.20% | 0.43x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 11 | LINK/USD | 9.06205 | 56.43 | +0.02% | 0.30x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 12 | SOL/USD | 70.24 | 55.62 | +0.06% | 0.53x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BCH/USD | 203.38 | 67.19 | +0.10% | 1.06x | 2158 | MODERATE 59/100 | HIGH 67/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
