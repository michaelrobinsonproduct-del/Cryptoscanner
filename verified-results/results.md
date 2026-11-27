# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T03:01:14.130301+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45931519256
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 6ec9e0b9a82ec5ad0575fca5c862b11dfb0ee538 (atomic ledger/results publication)
**Ledger generation:** 1949 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 472.84 | 91.391 | 76.380 | +3.48% | +0.00% | 2.67x | 5.9 | 2026-11-27T03:01:07.670429+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ZEC/USD | 741.8 | 85.324 | 97.642 | +8.82% | -0.74% | 0.14x | 4.7 | 2026-11-27T03:01:07.670429+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 3 | HYPE/USD | 64.88 | 80.564 | 83.386 | +4.28% | +0.05% | 0.69x | 3.1 | 2026-11-27T03:01:07.670429+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | SOL/USD | 72.35 | 68.725 | 68.222 | +1.99% | -0.26% | 1.18x | 1.4 | 2026-11-27T03:01:07.670429+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 5 | LINK/USD | 9.46022 | 65.213 | 66.615 | +2.07% | -0.52% | 1.12x | 5.7 | 2026-11-27T03:01:07.670429+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XRP/USD | 0.95874 | 63.563 | 66.351 | +1.70% | -0.27% | 0.86x | 1.0 | 2026-11-27T03:01:07.670429+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 7 | VVV/USD | 26.782 | 63.306 | 66.908 | +2.29% | +0.19% | 0.55x | 8.2 | 2026-11-27T03:01:07.670429+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | XBT/USD | 61263.4 | 60.497 | 63.848 | +1.27% | -0.31% | 0.82x | 0.0 | 2026-11-27T03:01:07.670429+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 9 | ETH/USD | 1720.61 | 59.508 | 68.629 | +1.95% | -0.31% | 0.24x | 0.1 | 2026-11-27T03:01:07.670429+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 10 | NEAR/USD | 3.1081 | 57.701 | 66.898 | +1.98% | -0.52% | 0.34x | 3.9 | 2026-11-27T03:01:07.670429+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 11 | LTC/USD | 44.34 | 54.137 | 62.729 | +1.37% | -0.69% | 0.49x | 2.3 | 2026-11-27T03:01:07.670429+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | TRX/USD | 0.304528 | 52.419 | 37.675 | +0.26% | -0.05% | 4.41x | 0.0 | 2026-11-27T03:01:07.670429+00:00 | Not calibrated | MODERATE 56/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 97.642 | 741.8 | -0.74% | 0.14x |
| 2 | HYPE/USD | 83.386 | 64.88 | +0.05% | 0.69x |
| 3 | XMR/USD | 76.380 | 472.84 | +0.00% | 2.67x |
| 4 | ETH/USD | 68.629 | 1720.61 | -0.31% | 0.24x |
| 5 | SOL/USD | 68.222 | 72.35 | -0.26% | 1.18x |
| 6 | VVV/USD | 66.908 | 26.782 | +0.19% | 0.55x |
| 7 | NEAR/USD | 66.898 | 3.1081 | -0.52% | 0.34x |
| 8 | LINK/USD | 66.615 | 9.46022 | -0.52% | 1.12x |
| 9 | XRP/USD | 66.351 | 0.95874 | -0.27% | 0.86x |
| 10 | XBT/USD | 63.848 | 61263.4 | -0.31% | 0.82x |
| 11 | LTC/USD | 62.729 | 44.34 | -0.69% | 0.49x |
| 12 | TRX/USD | 37.675 | 0.304528 | -0.05% | 4.41x |

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

- Persisted scans: 1949; predictions: 17090; observations: 1180433.
- Matured sampled outcomes across 1/6/24/48h: 37526; gap abstentions: 25470. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45931519256 · **Generation:** 1949 · **Legacy run:** 45931519256
**Main quote time:** 2026-11-27T03:01:14.130301+00:00 · **Legacy report time:** 2026-11-27T03:01:54.695621+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 472.84 | 91.39 | +0.00% | 2.67x | STRONG 91/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD | 741.8 | 85.32 | -0.74% | 0.14x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 3 | HYPE/USD | 64.88 | 80.56 | +0.05% | 0.69x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 4 | SOL/USD | 72.35 | 68.72 | -0.26% | 1.18x | WEAK 44/100 | HIGH 68/100 | Watch |
| 5 | LINK/USD | 9.46022 | 65.21 | -0.52% | 1.12x | WEAK 43/100 | HIGH 68/100 | Watch |
| 6 | XRP/USD | 0.95874 | 63.56 | -0.27% | 0.86x | WEAK 37/100 | HIGH 68/100 | Watch |
| 7 | VVV/USD | 26.782 | 63.31 | +0.19% | 0.55x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 8 | XBT/USD | 61263.4 | 60.50 | -0.31% | 0.82x | WEAK 35/100 | HIGH 68/100 | Watch |
| 9 | ETH/USD | 1720.61 | 59.51 | -0.31% | 0.24x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 10 | NEAR/USD | 3.1081 | 57.70 | -0.52% | 0.34x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |
| 11 | LTC/USD | 44.34 | 54.14 | -0.69% | 0.49x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | TRX/USD | 0.304528 | 52.42 | -0.05% | 4.41x | MODERATE 56/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD | 0.04897 | 81.11 | +1.02% | 2.32x | 6843 | STRONG 91/100 | HIGH 66/100 | Consider small entry |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
