# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T02:35:55.952225+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45743330577
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** dc86f8e0bd2ca480fc1bb75d220b209df2a550b7 (atomic ledger/results publication)
**Ledger generation:** 1800 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | TIA/USD | 0.3545 | 83.718 | 64.742 | +5.35% | +0.80% | 9.96x | 8.5 | 2026-11-26T02:35:47.061529+00:00 | Not calibrated | STRONG 97/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | ADA/USD | 0.148228 | 78.198 | 64.983 | +1.69% | -0.36% | 3.57x | 3.6 | 2026-11-26T02:35:47.061529+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 3 | TAO/USD | 184.917 | 77.260 | 64.394 | +1.83% | -0.26% | 2.42x | 6.8 | 2026-11-26T02:35:47.061529+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SOL/USD | 71.25 | 77.220 | 62.851 | +1.22% | -0.13% | 2.61x | 1.4 | 2026-11-26T02:35:47.061529+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 5 | LINK/USD | 9.1754 | 72.850 | 60.146 | +1.45% | -0.46% | 27.64x | 1.9 | 2026-11-26T02:35:47.061529+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XDG/USD | 0.0566421 | 71.788 | 58.563 | +1.22% | -0.35% | 5.71x | 0.0 | 2026-11-26T02:35:47.061529+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SYRUP/USD | 0.07069 | 69.069 | 65.692 | +6.67% | +1.60% | 0.54x | 22.7 | 2026-11-26T02:35:47.061529+00:00 | Not calibrated | MODERATE 55/100 | EXTREME 87/100 | Do nothing | WATCH |
| 8 | XRP/USD | 0.95499 | 64.944 | 68.723 | +1.97% | -0.08% | 0.66x | 0.1 | 2026-11-26T02:35:47.061529+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | ETH/USD | 1701.2 | 64.837 | 59.439 | +0.64% | -0.01% | 1.54x | 0.1 | 2026-11-26T02:35:47.061529+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 10 | LTC/USD | 43.67 | 62.805 | 69.589 | +2.25% | -0.23% | 0.44x | 2.3 | 2026-11-26T02:35:47.061529+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | NEAR/USD | 3.0884 | 62.334 | 60.759 | +1.26% | -0.45% | 1.38x | 6.2 | 2026-11-26T02:35:47.061529+00:00 | Not calibrated | MODERATE 51/100 | HIGH 61/100 | Watch | WATCH |
| 12 | XAUT/USD | 3591.9 | 60.503 | 43.897 | +0.64% | +0.32% | 17.44x | 1.1 | 2026-11-26T02:35:47.061529+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 69.589 | 43.67 | -0.23% | 0.44x |
| 2 | XRP/USD | 68.723 | 0.95499 | -0.08% | 0.66x |
| 3 | SYRUP/USD | 65.692 | 0.07069 | +1.60% | 0.54x |
| 4 | ADA/USD | 64.983 | 0.148228 | -0.36% | 3.57x |
| 5 | TIA/USD | 64.742 | 0.3545 | +0.80% | 9.96x |
| 6 | TAO/USD | 64.394 | 184.917 | -0.26% | 2.42x |
| 7 | SOL/USD | 62.851 | 71.25 | -0.13% | 2.61x |
| 8 | NEAR/USD | 60.759 | 3.0884 | -0.45% | 1.38x |
| 9 | LINK/USD | 60.146 | 9.1754 | -0.46% | 27.64x |
| 10 | ETH/USD | 59.439 | 1701.2 | -0.01% | 1.54x |
| 11 | XDG/USD | 58.563 | 0.0566421 | -0.35% | 5.71x |
| 12 | XAUT/USD | 43.897 | 3591.9 | +0.32% | 17.44x |

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

- Persisted scans: 1800; predictions: 15335; observations: 1091244.
- Matured sampled outcomes across 1/6/24/48h: 33311; gap abstentions: 23698. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45743330577 · **Generation:** 1800 · **Legacy run:** 45743330577
**Main quote time:** 2026-11-26T02:35:55.952225+00:00 · **Legacy report time:** 2026-11-26T02:36:59.491373+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | TIA/USD ⭐ | 0.3545 | 83.72 | +0.80% | 9.96x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 2 | ADA/USD | 0.148228 | 78.20 | -0.36% | 3.57x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 3 | TAO/USD | 184.917 | 77.26 | -0.26% | 2.42x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 4 | SOL/USD | 71.25 | 77.22 | -0.13% | 2.61x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 5 | LINK/USD | 9.1754 | 72.85 | -0.46% | 27.64x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 6 | XDG/USD | 0.0566421 | 71.79 | -0.35% | 5.71x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 7 | SYRUP/USD | 0.07069 | 69.07 | +1.60% | 0.54x | MODERATE 55/100 | EXTREME 87/100 | Do nothing |
| 8 | XRP/USD | 0.95499 | 64.94 | -0.08% | 0.66x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 9 | ETH/USD | 1701.2 | 64.84 | -0.01% | 1.54x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 10 | LTC/USD | 43.67 | 62.80 | -0.23% | 0.44x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 11 | NEAR/USD | 3.0884 | 62.33 | -0.45% | 1.38x | MODERATE 51/100 | HIGH 61/100 | Watch |
| 12 | XAUT/USD | 3591.9 | 60.50 | +0.32% | 17.44x | STRONG 85/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TIA/USD ⭐ | 0.3571 | 81.32 | +0.80% | 9.96x | 3743 | STRONG 100/100 | VERY_HIGH 73/100 | Watch |
| 2 | INJ/USD | 6.167 | 73.41 | +0.34% | 1.13x | 6787 | MODERATE 67/100 | HIGH 68/100 | Watch |

**Same-run overlap:** TIA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
