# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T04:31:18.478279+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45940244310
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 33f7a190c2089187fbeda9f29d4686c28749c759 (atomic ledger/results publication)
**Ledger generation:** 1959 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 601; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | HYPE/USD | 66.06 | 110.633 | 97.445 | +6.17% | -0.36% | 2.54x | 1.5 | 2026-11-27T04:31:11.751813+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ZEC/USD | 756.11 | 110.118 | 98.148 | +10.92% | -0.61% | 3.12x | 3.7 | 2026-11-27T04:31:11.751813+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LINK/USD | 9.54973 | 90.668 | 73.825 | +3.04% | +0.37% | 7.55x | 4.8 | 2026-11-27T04:31:11.751813+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | VVV/USD | 27.077 | 79.214 | 75.583 | +3.41% | -0.74% | 1.73x | 6.6 | 2026-11-27T04:31:11.751813+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 5 | ETH/USD | 1729.19 | 77.398 | 72.188 | +2.46% | -0.06% | 1.55x | 0.1 | 2026-11-27T04:31:11.751813+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 6 | W/USD | 0.00963 | 76.816 | 67.204 | +9.31% | +0.62% | 1.65x | 20.8 | 2026-11-27T04:31:11.751813+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | XMR/USD | 469.29 | 73.808 | 70.598 | +2.70% | +0.85% | 0.90x | 6.6 | 2026-11-27T04:31:11.751813+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XRP/USD | 0.9587 | 66.108 | 66.791 | +1.69% | -0.08% | 0.97x | 0.1 | 2026-11-27T04:31:11.751813+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 9 | SUI/USD | 0.6814 | 66.098 | 68.352 | +2.05% | -0.04% | 0.80x | 1.5 | 2026-11-27T04:31:11.751813+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 10 | SOL/USD | 72.76 | 64.818 | 72.272 | +2.57% | +0.10% | 0.21x | 1.4 | 2026-11-27T04:31:11.751813+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | JUP/USD | 0.24914 | 62.106 | 65.416 | +5.31% | -0.02% | 0.68x | 9.7 | 2026-11-27T04:31:11.751813+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 12 | XBT/USD | 61391.2 | 60.874 | 65.327 | +1.48% | -0.04% | 0.57x | 0.0 | 2026-11-27T04:31:11.751813+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.148 | 756.11 | -0.61% | 3.12x |
| 2 | HYPE/USD | 97.445 | 66.06 | -0.36% | 2.54x |
| 3 | VVV/USD | 75.583 | 27.077 | -0.74% | 1.73x |
| 4 | LINK/USD | 73.825 | 9.54973 | +0.37% | 7.55x |
| 5 | SOL/USD | 72.272 | 72.76 | +0.10% | 0.21x |
| 6 | ETH/USD | 72.188 | 1729.19 | -0.06% | 1.55x |
| 7 | XMR/USD | 70.598 | 469.29 | +0.85% | 0.90x |
| 8 | SUI/USD | 68.352 | 0.6814 | -0.04% | 0.80x |
| 9 | W/USD | 67.204 | 0.00963 | +0.62% | 1.65x |
| 10 | XRP/USD | 66.791 | 0.9587 | -0.08% | 0.97x |
| 11 | JUP/USD | 65.416 | 0.24914 | -0.02% | 0.68x |
| 12 | XBT/USD | 65.327 | 61391.2 | -0.04% | 0.57x |

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

- Persisted scans: 1959; predictions: 17210; observations: 1186443.
- Matured sampled outcomes across 1/6/24/48h: 37886; gap abstentions: 25507. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45940244310 · **Generation:** 1959 · **Legacy run:** 45940244310
**Main quote time:** 2026-11-27T04:31:18.478279+00:00 · **Legacy report time:** 2026-11-27T04:31:58.799139+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | HYPE/USD | 66.06 | 110.63 | -0.36% | 2.54x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | ZEC/USD | 756.11 | 110.12 | -0.61% | 3.12x | STRONG 80/100 | HIGH 61/100 | Watch |
| 3 | LINK/USD ⭐ | 9.54973 | 90.67 | +0.37% | 7.55x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | VVV/USD | 27.077 | 79.21 | -0.74% | 1.73x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 5 | ETH/USD | 1729.19 | 77.40 | -0.06% | 1.55x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 6 | W/USD | 0.00963 | 76.82 | +0.62% | 1.65x | STRONG 73/100 | VERY_HIGH 72/100 | Watch |
| 7 | XMR/USD | 469.29 | 73.81 | +0.85% | 0.90x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 8 | XRP/USD | 0.9587 | 66.11 | -0.08% | 0.97x | WEAK 38/100 | HIGH 68/100 | Watch |
| 9 | SUI/USD | 0.6814 | 66.10 | -0.04% | 0.80x | WEAK 38/100 | HIGH 68/100 | Watch |
| 10 | SOL/USD | 72.76 | 64.82 | +0.10% | 0.21x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 11 | JUP/USD | 0.24914 | 62.11 | -0.02% | 0.68x | WEAK 36/100 | VERY_HIGH 81/100 | Watch |
| 12 | XBT/USD | 61391.2 | 60.87 | -0.04% | 0.57x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.56097 | 84.70 | +0.37% | 7.55x | 7134 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** LINK/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
