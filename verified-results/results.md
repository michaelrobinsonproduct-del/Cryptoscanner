# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T17:22:31.297351+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46040924430
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 84d2a52923096de3ae4c71a7bb88bf905386c1ce (atomic ledger/results publication)
**Ledger generation:** 2037 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 742.42 | 85.258 | 95.352 | +8.91% | -0.62% | 0.30x | 9.3 | 2026-11-27T17:22:24.239154+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | HYPE/USD | 64.12 | 79.142 | 75.596 | +3.05% | -0.43% | 1.57x | 1.6 | 2026-11-27T17:22:24.239154+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SPACE/USD | 0.004172 | 71.337 | 70.967 | +7.75% | -0.05% | 1.06x | 9.6 | 2026-11-27T17:22:24.239154+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 4 | NIGHT/USD | 0.04981 | 69.955 | 66.915 | +2.76% | +0.36% | 1.12x | 14.1 | 2026-11-27T17:22:24.239154+00:00 | Not calibrated | MODERATE 65/100 | HIGH 68/100 | Watch | WATCH |
| 5 | UNI/USD | 4.7896 | 67.680 | 69.896 | +3.00% | +0.47% | 0.54x | 7.3 | 2026-11-27T17:22:24.239154+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XDG/USD | 0.057794 | 65.349 | 72.401 | +2.52% | +0.09% | 0.25x | 0.5 | 2026-11-27T17:22:24.239154+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | SUI/USD | 0.6723 | 62.484 | 58.335 | +0.69% | +0.40% | 1.21x | 3.0 | 2026-11-27T17:22:24.239154+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 8 | SOL/USD | 71.97 | 61.716 | 64.469 | +1.45% | -0.21% | 0.83x | 1.4 | 2026-11-27T17:22:24.239154+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XRP/USD | 0.9503 | 61.709 | 60.185 | +0.80% | +0.09% | 1.11x | 0.8 | 2026-11-27T17:22:24.239154+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 10 | MELANIA/USD | 0.05 | 59.820 | 65.853 | +6.84% | -0.20% | 0.50x | 20.0 | 2026-11-27T17:22:24.239154+00:00 | Not calibrated | WEAK 30/100 | EXTREME 94/100 | Do nothing | WATCH |
| 11 | PEPE/USD | 3.503e-06 | 59.479 | 49.049 | +0.72% | +0.23% | 1.93x | 2.9 | 2026-11-27T17:22:24.239154+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 12 | ADA/USD | 0.149011 | 58.337 | 55.181 | +0.37% | +0.34% | 1.15x | 4.8 | 2026-11-27T17:22:24.239154+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 95.352 | 742.42 | -0.62% | 0.30x |
| 2 | HYPE/USD | 75.596 | 64.12 | -0.43% | 1.57x |
| 3 | XDG/USD | 72.401 | 0.057794 | +0.09% | 0.25x |
| 4 | SPACE/USD | 70.967 | 0.004172 | -0.05% | 1.06x |
| 5 | UNI/USD | 69.896 | 4.7896 | +0.47% | 0.54x |
| 6 | NIGHT/USD | 66.915 | 0.04981 | +0.36% | 1.12x |
| 7 | MELANIA/USD | 65.853 | 0.05 | -0.20% | 0.50x |
| 8 | SOL/USD | 64.469 | 71.97 | -0.21% | 0.83x |
| 9 | XRP/USD | 60.185 | 0.9503 | +0.09% | 1.11x |
| 10 | SUI/USD | 58.335 | 0.6723 | +0.40% | 1.21x |
| 11 | ADA/USD | 55.181 | 0.149011 | +0.34% | 1.15x |
| 12 | PEPE/USD | 49.049 | 3.503e-06 | +0.23% | 1.93x |

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

- Persisted scans: 2037; predictions: 18146; observations: 1233494.
- Matured sampled outcomes across 1/6/24/48h: 40674; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 153 (sampled only; not a success-rate estimate).
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

**Writer:** 46040924430 · **Generation:** 2037 · **Legacy run:** 46040924430
**Main quote time:** 2026-11-27T17:22:31.297351+00:00 · **Legacy report time:** 2026-11-27T17:23:08.938095+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 742.42 | 85.26 | -0.62% | 0.30x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 2 | HYPE/USD | 64.12 | 79.14 | -0.43% | 1.57x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 3 | SPACE/USD | 0.004172 | 71.34 | -0.05% | 1.06x | MODERATE 46/100 | VERY_HIGH 80/100 | Watch |
| 4 | NIGHT/USD ⭐ | 0.04981 | 69.95 | +0.36% | 1.12x | STRONG 75/100 | HIGH 68/100 | Watch |
| 5 | UNI/USD | 4.7896 | 67.68 | +0.47% | 0.54x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 6 | XDG/USD | 0.057794 | 65.35 | +0.09% | 0.25x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 7 | SUI/USD | 0.6723 | 62.48 | +0.40% | 1.21x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 8 | SOL/USD | 71.97 | 61.72 | -0.21% | 0.83x | WEAK 36/100 | HIGH 68/100 | Watch |
| 9 | XRP/USD | 0.9503 | 61.71 | +0.09% | 1.11x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 10 | MELANIA/USD | 0.05 | 59.82 | -0.20% | 0.50x | WEAK 30/100 | EXTREME 94/100 | Do nothing |
| 11 | PEPE/USD | 3.503e-06 | 59.48 | +0.23% | 1.93x | STRONG 75/100 | HIGH 55/100 | Watch |
| 12 | ADA/USD | 0.149011 | 58.34 | +0.34% | 1.15x | MODERATE 64/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04972 | 69.26 | +0.36% | 1.12x | 16226 | STRONG 75/100 | HIGH 68/100 | Watch |

**Same-run overlap:** NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
