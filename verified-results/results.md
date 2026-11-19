# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T03:20:22.100425+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44450636489
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 6f871fe6ea6b6fcd6d305a88dcb6751408787de3 (atomic ledger/results publication)
**Ledger generation:** 741 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.022272 | 75.956 | 72.816 | +8.09% | -0.01% | 1.32x | 7.6 | 2026-11-19T03:20:13.680356+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.3357 | 61.670 | 61.184 | +1.16% | +0.40% | 0.85x | 3.9 | 2026-11-19T03:20:13.680356+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 3 | ICP/USD | 2.236 | 44.202 | 52.194 | +2.66% | -0.27% | 0.33x | 8.9 | 2026-11-19T03:20:13.680356+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | VVV/USD | 21.89 | 43.782 | 52.794 | +1.01% | -0.74% | 0.47x | 6.9 | 2026-11-19T03:20:13.680356+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | DRV/USD | 0.26636 | 33.043 | 33.624 | +0.63% | +0.15% | 0.87x | 8.3 | 2026-11-19T03:20:13.680356+00:00 | Not calibrated | WEAK 37/100 | HIGH 67/100 | Watch | WATCH |
| 6 | TRUMP/USD | 0.949 | 27.105 | 32.613 | +0.42% | -0.21% | 0.55x | 10.5 | 2026-11-19T03:20:13.680356+00:00 | Not calibrated | WEAK 14/100 | EXTREME 87/100 | Do nothing | WATCH |
| 7 | MEGA/USD | 0.05625 | 26.017 | 27.351 | +0.45% | -0.76% | 1.25x | 14.2 | 2026-11-19T03:20:13.680356+00:00 | Not calibrated | WEAK 18/100 | EXTREME 86/100 | Do nothing | WATCH |
| 8 | TON/USD | 1.024 | 24.214 | 31.290 | +0.29% | -0.10% | 0.34x | 9.8 | 2026-11-19T03:20:13.680356+00:00 | Not calibrated | WEAK 17/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | AKE/USD | 0.01043783 | 22.355 | 25.895 | +0.45% | +0.11% | 0.59x | 23.7 | 2026-11-19T03:20:13.680356+00:00 | Not calibrated | WEAK 21/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 72.816 | 0.022272 | -0.01% | 1.32x |
| 2 | NEAR/USD | 61.184 | 3.3357 | +0.40% | 0.85x |
| 3 | VVV/USD | 52.794 | 21.89 | -0.74% | 0.47x |
| 4 | ICP/USD | 52.194 | 2.236 | -0.27% | 0.33x |
| 5 | DRV/USD | 33.624 | 0.26636 | +0.15% | 0.87x |
| 6 | TRUMP/USD | 32.613 | 0.949 | -0.21% | 0.55x |
| 7 | TON/USD | 31.290 | 1.024 | -0.10% | 0.34x |
| 8 | MEGA/USD | 27.351 | 0.05625 | -0.76% | 1.25x |
| 9 | AKE/USD | 25.895 | 0.01043783 | +0.11% | 0.59x |

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

- Persisted scans: 741; predictions: 6045; observations: 448276.
- Matured sampled outcomes across 1/6/24/48h: 6008; gap abstentions: 13540. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44450636489 · **Generation:** 741 · **Legacy run:** 44450636489
**Main quote time:** 2026-11-19T03:20:22.100425+00:00 · **Legacy report time:** 2026-11-19T03:21:08.828659+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.022272 | 75.96 | -0.01% | 1.32x | MODERATE 58/100 | VERY_HIGH 73/100 | Watch |
| 2 | NEAR/USD | 3.3357 | 61.67 | +0.40% | 0.85x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 3 | ICP/USD | 2.236 | 44.20 | -0.27% | 0.33x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | VVV/USD | 21.89 | 43.78 | -0.74% | 0.47x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | DRV/USD | 0.26636 | 33.04 | +0.15% | 0.87x | WEAK 37/100 | HIGH 67/100 | Watch |
| 6 | TRUMP/USD | 0.949 | 27.11 | -0.21% | 0.55x | WEAK 14/100 | EXTREME 87/100 | Do nothing |
| 7 | MEGA/USD | 0.05625 | 26.02 | -0.76% | 1.25x | WEAK 18/100 | EXTREME 86/100 | Do nothing |
| 8 | TON/USD | 1.024 | 24.21 | -0.10% | 0.34x | WEAK 17/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | AKE/USD | 0.01043783 | 22.35 | +0.11% | 0.59x | WEAK 21/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRX/USD | 0.309811 | 53.29 | +0.07% | 3.69x | 4223 | STRONG 72/100 | HIGH 55/100 | Watch |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
