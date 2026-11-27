# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T20:52:31.396425+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46066237250
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 66f626877b89b86cf72837b8ac2c10550ea2100a (atomic ledger/results publication)
**Ledger generation:** 2059 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 605; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 737.62 | 91.189 | 99.051 | +8.21% | -0.58% | 0.50x | 1.9 | 2026-11-27T20:52:24.993243+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 2 | SKY/USD | 0.05037 | 89.181 | 76.143 | +8.53% | -0.39% | 4.27x | 9.9 | 2026-11-27T20:52:24.993243+00:00 | Not calibrated | STRONG 75/100 | HIGH 66/100 | Watch | WATCH |
| 3 | UNI/USD | 4.8299 | 78.025 | 78.501 | +3.87% | -0.36% | 1.13x | 1.9 | 2026-11-27T20:52:24.993243+00:00 | Not calibrated | MODERATE 49/100 | HIGH 68/100 | Watch | WATCH |
| 4 | HYPE/USD | 63.99 | 72.090 | 74.132 | +2.84% | -0.11% | 0.85x | 1.6 | 2026-11-27T20:52:24.993243+00:00 | Not calibrated | WEAK 41/100 | HIGH 68/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.05009 | 69.017 | 77.398 | +3.34% | -0.30% | 0.31x | 2.0 | 2026-11-27T20:52:24.993243+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | RENDER/USD | 1.404 | 68.454 | 66.817 | +5.33% | +0.21% | 1.06x | 7.1 | 2026-11-27T20:52:24.993243+00:00 | Not calibrated | MODERATE 69/100 | HIGH 67/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0576302 | 61.212 | 69.820 | +2.23% | -0.11% | 0.20x | 1.5 | 2026-11-27T20:52:24.993243+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | LTC/USD | 44.11 | 60.968 | 59.788 | +0.85% | +0.02% | 1.11x | 2.3 | 2026-11-27T20:52:24.993243+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 9 | PEPE/USD | 3.531e-06 | 60.470 | 54.984 | +1.52% | -0.11% | 1.61x | 2.8 | 2026-11-27T20:52:24.993243+00:00 | Not calibrated | MODERATE 50/100 | HIGH 61/100 | Watch | WATCH |
| 10 | LINK/USD | 9.38353 | 59.683 | 62.941 | +1.24% | -0.10% | 0.72x | 1.5 | 2026-11-27T20:52:24.993243+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | SOL/USD | 71.94 | 59.334 | 64.172 | +1.41% | -0.19% | 0.61x | 1.4 | 2026-11-27T20:52:24.993243+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | SUI/USD | 0.6723 | 54.668 | 59.079 | +0.69% | -0.15% | 0.63x | 1.5 | 2026-11-27T20:52:24.993243+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 99.051 | 737.62 | -0.58% | 0.50x |
| 2 | UNI/USD | 78.501 | 4.8299 | -0.36% | 1.13x |
| 3 | NIGHT/USD | 77.398 | 0.05009 | -0.30% | 0.31x |
| 4 | SKY/USD | 76.143 | 0.05037 | -0.39% | 4.27x |
| 5 | HYPE/USD | 74.132 | 63.99 | -0.11% | 0.85x |
| 6 | XDG/USD | 69.820 | 0.0576302 | -0.11% | 0.20x |
| 7 | RENDER/USD | 66.817 | 1.404 | +0.21% | 1.06x |
| 8 | SOL/USD | 64.172 | 71.94 | -0.19% | 0.61x |
| 9 | LINK/USD | 62.941 | 9.38353 | -0.10% | 0.72x |
| 10 | LTC/USD | 59.788 | 44.11 | +0.02% | 1.11x |
| 11 | SUI/USD | 59.079 | 0.6723 | -0.15% | 0.63x |
| 12 | PEPE/USD | 54.984 | 3.531e-06 | -0.11% | 1.61x |

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

- Persisted scans: 2059; predictions: 18410; observations: 1246804.
- Matured sampled outcomes across 1/6/24/48h: 41687; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 46066237250 · **Generation:** 2059 · **Legacy run:** 46066237250
**Main quote time:** 2026-11-27T20:52:31.396425+00:00 · **Legacy report time:** 2026-11-27T20:53:27.314590+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 737.62 | 91.19 | -0.58% | 0.50x | MODERATE 51/100 | VERY_HIGH 76/100 | Watch |
| 2 | SKY/USD | 0.05037 | 89.18 | -0.39% | 4.27x | STRONG 75/100 | HIGH 66/100 | Watch |
| 3 | UNI/USD | 4.8299 | 78.03 | -0.36% | 1.13x | MODERATE 49/100 | HIGH 68/100 | Watch |
| 4 | HYPE/USD | 63.99 | 72.09 | -0.11% | 0.85x | WEAK 41/100 | HIGH 68/100 | Watch |
| 5 | NIGHT/USD | 0.05009 | 69.02 | -0.30% | 0.31x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 6 | RENDER/USD ⭐ | 1.404 | 68.45 | +0.21% | 1.06x | STRONG 79/100 | HIGH 67/100 | Watch |
| 7 | XDG/USD | 0.0576302 | 61.21 | -0.11% | 0.20x | WEAK 36/100 | VERY_HIGH 76/100 | Watch |
| 8 | LTC/USD | 44.11 | 60.97 | +0.02% | 1.11x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 9 | PEPE/USD | 3.531e-06 | 60.47 | -0.11% | 1.61x | MODERATE 50/100 | HIGH 61/100 | Watch |
| 10 | LINK/USD | 9.38353 | 59.68 | -0.10% | 0.72x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 11 | SOL/USD | 71.94 | 59.33 | -0.19% | 0.61x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | SUI/USD | 0.6723 | 54.67 | -0.15% | 0.63x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | RENDER/USD ⭐ | 1.404 | 66.64 | +0.21% | 1.06x | 1910 | STRONG 73/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** RENDER/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
