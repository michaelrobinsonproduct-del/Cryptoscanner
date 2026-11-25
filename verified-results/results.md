# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T20:02:41.559749+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45690887040
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 875d9b267f3b568e74dafc3ac6823895b1b6ba79 (atomic ledger/results publication)
**Ledger generation:** 1760 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PUMP/USD | 0.002523 | 75.526 | 63.588 | +3.44% | +0.16% | 2.11x | 4.0 | 2026-11-25T20:02:32.633404+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 2 | LTC/USD | 42.38 | 70.436 | 77.678 | +3.75% | +0.07% | 0.24x | 7.1 | 2026-11-25T20:02:32.633404+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | HYPE/USD | 61.23 | 70.107 | 69.269 | +2.27% | -0.16% | 1.17x | 3.3 | 2026-11-25T20:02:32.633404+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 4 | ZEC/USD | 752.21 | 69.499 | 64.893 | +1.80% | -0.15% | 1.53x | 5.5 | 2026-11-25T20:02:32.633404+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XRP/USD | 0.9392 | 65.549 | 66.336 | +1.69% | -0.15% | 0.99x | 1.0 | 2026-11-25T20:02:32.633404+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 6 | SUI/USD | 0.6612 | 62.045 | 68.298 | +2.12% | +0.05% | 0.35x | 3.0 | 2026-11-25T20:02:32.633404+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | HBAR/USD | 0.05158 | 61.788 | 53.617 | +2.63% | -0.06% | 1.85x | 1.9 | 2026-11-25T20:02:32.633404+00:00 | Not calibrated | MODERATE 51/100 | HIGH 66/100 | Watch | WATCH |
| 8 | SOL/USD | 70.41 | 61.348 | 62.436 | +1.16% | -0.17% | 0.98x | 1.4 | 2026-11-25T20:02:32.633404+00:00 | Not calibrated | WEAK 36/100 | HIGH 68/100 | Watch | WATCH |
| 9 | XMR/USD | 517.4 | 59.637 | 64.361 | +1.53% | +0.20% | 0.43x | 2.7 | 2026-11-25T20:02:32.633404+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | LINK/USD | 9.07122 | 58.565 | 63.935 | +2.60% | +0.11% | 0.41x | 4.3 | 2026-11-25T20:02:32.633404+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ETH/USD | 1684 | 56.387 | 56.823 | +0.37% | -0.08% | 0.99x | 1.6 | 2026-11-25T20:02:32.633404+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 12 | ADA/USD | 0.1462 | 52.630 | 62.344 | +1.28% | -0.35% | 0.20x | 3.2 | 2026-11-25T20:02:32.633404+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | LTC/USD | 77.678 | 42.38 | +0.07% | 0.24x |
| 2 | HYPE/USD | 69.269 | 61.23 | -0.16% | 1.17x |
| 3 | SUI/USD | 68.298 | 0.6612 | +0.05% | 0.35x |
| 4 | XRP/USD | 66.336 | 0.9392 | -0.15% | 0.99x |
| 5 | ZEC/USD | 64.893 | 752.21 | -0.15% | 1.53x |
| 6 | XMR/USD | 64.361 | 517.4 | +0.20% | 0.43x |
| 7 | LINK/USD | 63.935 | 9.07122 | +0.11% | 0.41x |
| 8 | PUMP/USD | 63.588 | 0.002523 | +0.16% | 2.11x |
| 9 | SOL/USD | 62.436 | 70.41 | -0.17% | 0.98x |
| 10 | ADA/USD | 62.344 | 0.1462 | -0.35% | 0.20x |
| 11 | ETH/USD | 56.823 | 1684 | -0.08% | 0.99x |
| 12 | HBAR/USD | 53.617 | 0.05158 | -0.06% | 1.85x |

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

- Persisted scans: 1760; predictions: 14864; observations: 1066884.
- Matured sampled outcomes across 1/6/24/48h: 32618; gap abstentions: 22920. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45690887040 · **Generation:** 1760 · **Legacy run:** 45690887040
**Main quote time:** 2026-11-25T20:02:41.559749+00:00 · **Legacy report time:** 2026-11-25T20:03:45.919740+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002523 | 75.53 | +0.16% | 2.11x | STRONG 93/100 | HIGH 55/100 | Watch |
| 2 | LTC/USD | 42.38 | 70.44 | +0.07% | 0.24x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 3 | HYPE/USD | 61.23 | 70.11 | -0.16% | 1.17x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 4 | ZEC/USD | 752.21 | 69.50 | -0.15% | 1.53x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 5 | XRP/USD | 0.9392 | 65.55 | -0.15% | 0.99x | WEAK 38/100 | HIGH 68/100 | Watch |
| 6 | SUI/USD | 0.6612 | 62.05 | +0.05% | 0.35x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 7 | HBAR/USD | 0.05158 | 61.79 | -0.06% | 1.85x | MODERATE 51/100 | HIGH 66/100 | Watch |
| 8 | SOL/USD | 70.41 | 61.35 | -0.17% | 0.98x | WEAK 36/100 | HIGH 68/100 | Watch |
| 9 | XMR/USD | 517.4 | 59.64 | +0.20% | 0.43x | MODERATE 50/100 | VERY_HIGH 70/100 | Watch |
| 10 | LINK/USD | 9.07122 | 58.56 | +0.11% | 0.41x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 11 | ETH/USD | 1684 | 56.39 | -0.08% | 0.99x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 12 | ADA/USD | 0.1462 | 52.63 | -0.35% | 0.20x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PUMP/USD ⭐ | 0.002527 | 84.22 | +0.16% | 2.11x | 5170 | STRONG 97/100 | HIGH 55/100 | Watch |
| 2 | DRV/USD | 0.35628 | 77.24 | +0.46% | 1.04x | 12027 | MODERATE 69/100 | HIGH 68/100 | Watch |
| 3 | SHX/USD | 0.003551 | 67.96 | +0.20% | 1.43x | 2047 | MODERATE 64/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** PUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
