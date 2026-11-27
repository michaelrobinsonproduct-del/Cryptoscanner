# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T18:32:31.867557+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46049861957
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f12e2aeba2071b1d6d82a3fa8b68f19311e50687 (atomic ledger/results publication)
**Ledger generation:** 2044 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 743.54 | 96.390 | 98.656 | +9.08% | -0.72% | 1.13x | 2.7 | 2026-11-27T18:32:23.328488+00:00 | Not calibrated | MODERATE 58/100 | HIGH 68/100 | Watch | WATCH |
| 2 | SPACE/USD | 0.004267 | 88.010 | 71.126 | +10.20% | +0.38% | 3.84x | 9.4 | 2026-11-27T18:32:23.328488+00:00 | Not calibrated | STRONG 99/100 | HIGH 67/100 | Consider small entry | WATCH |
| 3 | NIGHT/USD | 0.05001 | 86.254 | 76.241 | +3.18% | +0.04% | 1.98x | 2.0 | 2026-11-27T18:32:23.328488+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 4 | UNI/USD | 4.7849 | 74.020 | 70.854 | +2.90% | -0.01% | 1.32x | 3.5 | 2026-11-27T18:32:23.328488+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 5 | PAXG/USD | 3628.12 | 70.168 | 55.971 | +2.01% | -0.16% | 6.25x | 1.6 | 2026-11-27T18:32:23.328488+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XAUT/USD | 3633.3 | 58.988 | 51.988 | +2.07% | -0.15% | 1.77x | 0.3 | 2026-11-27T18:32:23.328488+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0574637 | 58.808 | 68.490 | +1.93% | -0.30% | 0.18x | 0.1 | 2026-11-27T18:32:23.328488+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | HYPE/USD | 63.45 | 57.882 | 68.050 | +1.98% | -0.50% | 0.23x | 1.6 | 2026-11-27T18:32:23.328488+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 9 | FET/USD | 0.126 | 56.864 | 65.870 | +4.65% | +0.08% | 0.06x | 7.9 | 2026-11-27T18:32:23.328488+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SOL/USD | 71.79 | 56.474 | 62.691 | +1.20% | -0.31% | 0.53x | 1.4 | 2026-11-27T18:32:23.328488+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | LINK/USD | 9.34681 | 52.428 | 60.069 | +0.85% | -0.10% | 0.28x | 1.7 | 2026-11-27T18:32:23.328488+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | SUI/USD | 0.67 | 48.660 | 55.919 | +0.34% | -0.18% | 0.36x | 3.0 | 2026-11-27T18:32:23.328488+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.656 | 743.54 | -0.72% | 1.13x |
| 2 | NIGHT/USD | 76.241 | 0.05001 | +0.04% | 1.98x |
| 3 | SPACE/USD | 71.126 | 0.004267 | +0.38% | 3.84x |
| 4 | UNI/USD | 70.854 | 4.7849 | -0.01% | 1.32x |
| 5 | XDG/USD | 68.490 | 0.0574637 | -0.30% | 0.18x |
| 6 | HYPE/USD | 68.050 | 63.45 | -0.50% | 0.23x |
| 7 | FET/USD | 65.870 | 0.126 | +0.08% | 0.06x |
| 8 | SOL/USD | 62.691 | 71.79 | -0.31% | 0.53x |
| 9 | LINK/USD | 60.069 | 9.34681 | -0.10% | 0.28x |
| 10 | PAXG/USD | 55.971 | 3628.12 | -0.16% | 6.25x |
| 11 | SUI/USD | 55.919 | 0.67 | -0.18% | 0.36x |
| 12 | XAUT/USD | 51.988 | 3633.3 | -0.15% | 1.77x |

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

- Persisted scans: 2044; predictions: 18230; observations: 1237729.
- Matured sampled outcomes across 1/6/24/48h: 40979; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46049861957 · **Generation:** 2044 · **Legacy run:** 46049861957
**Main quote time:** 2026-11-27T18:32:31.867557+00:00 · **Legacy report time:** 2026-11-27T18:33:28.197187+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 743.54 | 96.39 | -0.72% | 1.13x | MODERATE 58/100 | HIGH 68/100 | Watch |
| 2 | SPACE/USD ⭐ | 0.004267 | 88.01 | +0.38% | 3.84x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | NIGHT/USD | 0.05001 | 86.25 | +0.04% | 1.98x | STRONG 78/100 | HIGH 55/100 | Watch |
| 4 | UNI/USD | 4.7849 | 74.02 | -0.01% | 1.32x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 5 | PAXG/USD | 3628.12 | 70.17 | -0.16% | 6.25x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 6 | XAUT/USD | 3633.3 | 58.99 | -0.15% | 1.77x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 7 | XDG/USD | 0.0574637 | 58.81 | -0.30% | 0.18x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | HYPE/USD | 63.45 | 57.88 | -0.50% | 0.23x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 9 | FET/USD | 0.126 | 56.86 | +0.08% | 0.06x | MODERATE 48/100 | VERY_HIGH 70/100 | Watch |
| 10 | SOL/USD | 71.79 | 56.47 | -0.31% | 0.53x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | LINK/USD | 9.34681 | 52.43 | -0.10% | 0.28x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | SUI/USD | 0.67 | 48.66 | -0.18% | 0.36x | WEAK 29/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SPACE/USD ⭐ | 0.004275 | 78.79 | +0.38% | 3.84x | 2540 | STRONG 100/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** SPACE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
