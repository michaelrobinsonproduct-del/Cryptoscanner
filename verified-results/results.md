# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T10:16:37.927779+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45799476658
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 42bcbcc3bc88a4bfe3dc4bac352a9e3754fb3c7e (atomic ledger/results publication)
**Ledger generation:** 1847 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 584; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SEI/USD | 0.03607 | 80.241 | 73.115 | +8.29% | +1.69% | 0.87x | 8.3 | 2026-11-26T10:16:31.104408+00:00 | Not calibrated | STRONG 70/100 | HIGH 67/100 | Watch | WATCH |
| 2 | SYRUP/USD | 0.07097 | 76.577 | 68.225 | +7.09% | +0.70% | 1.49x | 18.3 | 2026-11-26T10:16:31.104408+00:00 | Not calibrated | STRONG 78/100 | HIGH 66/100 | Watch | WATCH |
| 3 | LINK/USD | 9.23393 | 70.596 | 69.654 | +2.09% | -0.04% | 1.11x | 0.0 | 2026-11-26T10:16:31.104408+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 4 | LTC/USD | 43.59 | 69.782 | 68.275 | +2.06% | -0.25% | 1.28x | 2.3 | 2026-11-26T10:16:31.104408+00:00 | Not calibrated | MODERATE 45/100 | HIGH 61/100 | Watch | WATCH |
| 5 | INJ/USD | 6.202 | 68.419 | 71.174 | +4.17% | -0.97% | 1.21x | 3.2 | 2026-11-26T10:16:31.104408+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 6 | ADA/USD | 0.148633 | 67.600 | 66.998 | +1.96% | -0.13% | 1.13x | 3.5 | 2026-11-26T10:16:31.104408+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 7 | SOL/USD | 70.94 | 65.491 | 59.765 | +0.78% | +0.00% | 1.57x | 1.4 | 2026-11-26T10:16:31.104408+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 8 | XRP/USD | 0.95223 | 63.242 | 66.450 | +1.67% | +0.04% | 0.66x | 0.5 | 2026-11-26T10:16:31.104408+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | ETH/USD | 1700.42 | 59.851 | 59.116 | +0.59% | +0.05% | 1.05x | 0.1 | 2026-11-26T10:16:31.104408+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 10 | XBT/USD | 60805.8 | 58.271 | 60.061 | +0.72% | +0.03% | 0.81x | 0.0 | 2026-11-26T10:16:31.104408+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 11 | XDG/USD | 0.0566207 | 57.356 | 58.606 | +1.18% | -0.00% | 0.88x | 0.0 | 2026-11-26T10:16:31.104408+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | NEAR/USD | 3.0611 | 46.921 | 55.609 | +0.37% | +0.03% | 0.12x | 3.9 | 2026-11-26T10:16:31.104408+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SEI/USD | 73.115 | 0.03607 | +1.69% | 0.87x |
| 2 | INJ/USD | 71.174 | 6.202 | -0.97% | 1.21x |
| 3 | LINK/USD | 69.654 | 9.23393 | -0.04% | 1.11x |
| 4 | LTC/USD | 68.275 | 43.59 | -0.25% | 1.28x |
| 5 | SYRUP/USD | 68.225 | 0.07097 | +0.70% | 1.49x |
| 6 | ADA/USD | 66.998 | 0.148633 | -0.13% | 1.13x |
| 7 | XRP/USD | 66.450 | 0.95223 | +0.04% | 0.66x |
| 8 | XBT/USD | 60.061 | 60805.8 | +0.03% | 0.81x |
| 9 | SOL/USD | 59.765 | 70.94 | +0.00% | 1.57x |
| 10 | ETH/USD | 59.116 | 1700.42 | +0.05% | 1.05x |
| 11 | XDG/USD | 58.606 | 0.0566207 | -0.00% | 0.88x |
| 12 | NEAR/USD | 55.609 | 3.0611 | +0.03% | 0.12x |

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

- Persisted scans: 1847; predictions: 15899; observations: 1119740.
- Matured sampled outcomes across 1/6/24/48h: 34442; gap abstentions: 24537. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45799476658 · **Generation:** 1847 · **Legacy run:** 45799476658
**Main quote time:** 2026-11-26T10:16:37.927779+00:00 · **Legacy report time:** 2026-11-26T10:17:49.519596+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SEI/USD | 0.03607 | 80.24 | +1.69% | 0.87x | STRONG 70/100 | HIGH 67/100 | Watch |
| 2 | SYRUP/USD ⭐ | 0.07097 | 76.58 | +0.70% | 1.49x | STRONG 88/100 | HIGH 66/100 | Watch |
| 3 | LINK/USD | 9.23393 | 70.60 | -0.04% | 1.11x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 4 | LTC/USD | 43.59 | 69.78 | -0.25% | 1.28x | MODERATE 45/100 | HIGH 61/100 | Watch |
| 5 | INJ/USD | 6.202 | 68.42 | -0.97% | 1.21x | WEAK 44/100 | HIGH 68/100 | Watch |
| 6 | ADA/USD | 0.148633 | 67.60 | -0.13% | 1.13x | WEAK 44/100 | HIGH 68/100 | Watch |
| 7 | SOL/USD | 70.94 | 65.49 | +0.00% | 1.57x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 8 | XRP/USD | 0.95223 | 63.24 | +0.04% | 0.66x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 9 | ETH/USD | 1700.42 | 59.85 | +0.05% | 1.05x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 10 | XBT/USD | 60805.8 | 58.27 | +0.03% | 0.81x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 11 | XDG/USD | 0.0566207 | 57.36 | -0.00% | 0.88x | WEAK 34/100 | HIGH 68/100 | Do nothing |
| 12 | NEAR/USD | 3.0611 | 46.92 | +0.03% | 0.12x | WEAK 43/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.07101 | 75.48 | +0.70% | 1.49x | 4078 | STRONG 88/100 | HIGH 66/100 | Watch |

**Same-run overlap:** SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
