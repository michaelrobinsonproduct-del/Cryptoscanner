# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T03:30:22.737603+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44451798610
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 4f9877a068dcbbb90b946e194fe0f7a1fc9f2dc9 (atomic ledger/results publication)
**Ledger generation:** 743 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.36 | 76.794 | 66.206 | +1.90% | +0.81% | 1.65x | 4.2 | 2026-11-19T03:30:14.492169+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SENT/USD | 0.022578 | 66.480 | 55.163 | +9.58% | +1.16% | 1.55x | 43.0 | 2026-11-19T03:30:14.492169+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | VVV/USD | 22.104 | 58.257 | 61.548 | +2.00% | +0.59% | 0.38x | 3.6 | 2026-11-19T03:30:14.492169+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ICP/USD | 2.248 | 55.762 | 56.145 | +3.21% | +0.63% | 0.65x | 8.9 | 2026-11-19T03:30:14.492169+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | LTC/USD | 44.14 | 50.885 | 47.193 | +0.30% | +0.85% | 0.95x | 2.3 | 2026-11-19T03:30:14.492169+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 6 | AKT/USD | 0.5199 | 46.258 | 26.402 | +0.37% | +0.97% | 2.93x | 15.4 | 2026-11-19T03:30:14.492169+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | WIF/USD | 0.1331 | 39.436 | 31.294 | +0.60% | +0.99% | 1.32x | 7.5 | 2026-11-19T03:30:14.492169+00:00 | Not calibrated | MODERATE 65/100 | HIGH 67/100 | Watch | WATCH |
| 8 | DRV/USD | 0.26725 | 37.238 | 35.262 | +0.97% | +0.45% | 0.97x | 9.7 | 2026-11-19T03:30:14.492169+00:00 | Not calibrated | MODERATE 49/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 66.206 | 3.36 | +0.81% | 1.65x |
| 2 | VVV/USD | 61.548 | 22.104 | +0.59% | 0.38x |
| 3 | ICP/USD | 56.145 | 2.248 | +0.63% | 0.65x |
| 4 | SENT/USD | 55.163 | 0.022578 | +1.16% | 1.55x |
| 5 | LTC/USD | 47.193 | 44.14 | +0.85% | 0.95x |
| 6 | DRV/USD | 35.262 | 0.26725 | +0.45% | 0.97x |
| 7 | WIF/USD | 31.294 | 0.1331 | +0.99% | 1.32x |
| 8 | AKT/USD | 26.402 | 0.5199 | +0.97% | 2.93x |

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

- Persisted scans: 743; predictions: 6063; observations: 449494.
- Matured sampled outcomes across 1/6/24/48h: 6020; gap abstentions: 13549. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 16; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44451798610 · **Generation:** 743 · **Legacy run:** 44451798610
**Main quote time:** 2026-11-19T03:30:22.737603+00:00 · **Legacy report time:** 2026-11-19T03:31:12.086951+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.36 | 76.79 | +0.81% | 1.65x | STRONG 93/100 | HIGH 55/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.022578 | 66.48 | +1.16% | 1.55x | STRONG 73/100 | VERY_HIGH 82/100 | Watch |
| 3 | VVV/USD | 22.104 | 58.26 | +0.59% | 0.38x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 4 | ICP/USD | 2.248 | 55.76 | +0.63% | 0.65x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 5 | LTC/USD | 44.14 | 50.88 | +0.85% | 0.95x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 6 | AKT/USD | 0.5199 | 46.26 | +0.97% | 2.93x | STRONG 73/100 | VERY_HIGH 73/100 | Watch |
| 7 | WIF/USD | 0.1331 | 39.44 | +0.99% | 1.32x | MODERATE 65/100 | HIGH 67/100 | Watch |
| 8 | DRV/USD | 0.26725 | 37.24 | +0.45% | 0.97x | MODERATE 49/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022588 | 83.71 | +1.16% | 1.55x | 8252 | STRONG 97/100 | HIGH 60/100 | Consider small entry |
| 2 | NEAR/USD ⭐ | 3.3646 | 77.93 | +0.81% | 1.65x | 13579 | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 3 | TRX/USD | 0.309917 | 53.05 | +0.07% | 4.26x | 4236 | STRONG 72/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NEAR/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
