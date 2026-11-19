# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T04:15:22.217638+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44456950787
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** cdfb67889e4633527da5c8fe10b2188d7e6164f4 (atomic ledger/results publication)
**Ledger generation:** 752 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.411 | 96.746 | 77.355 | +3.45% | +0.88% | 4.05x | 3.5 | 2026-11-19T04:15:16.738992+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | VVV/USD | 22.396 | 89.243 | 70.966 | +3.35% | +0.66% | 6.09x | 7.6 | 2026-11-19T04:15:16.738992+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | PYTH/USD | 0.05567 | 81.734 | 62.350 | +5.52% | +1.36% | 2.26x | 16.2 | 2026-11-19T04:15:16.738992+00:00 | Not calibrated | STRONG 91/100 | HIGH 66/100 | Consider small entry | WATCH |
| 4 | ETH/USD | 1795.41 | 79.300 | 63.117 | +1.16% | +0.24% | 4.37x | 0.1 | 2026-11-19T04:15:16.738992+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | HYPE/USD | 67.43 | 76.204 | 60.015 | +0.82% | +0.24% | 3.19x | 1.5 | 2026-11-19T04:15:16.738992+00:00 | Not calibrated | STRONG 93/100 | HIGH 55/100 | Consider small entry | WATCH |
| 6 | XRP/USD | 0.97092 | 74.866 | 58.244 | +0.47% | +0.32% | 15.50x | 0.1 | 2026-11-19T04:15:16.738992+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | SOL/USD | 74.21 | 70.635 | 60.704 | +0.91% | +0.12% | 1.93x | 1.3 | 2026-11-19T04:15:16.738992+00:00 | Not calibrated | STRONG 70/100 | HIGH 55/100 | Watch | WATCH |
| 8 | LINK/USD | 9.1092 | 68.274 | 55.530 | +0.40% | +0.11% | 2.22x | 4.6 | 2026-11-19T04:15:16.738992+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 9 | ZEC/USD | 924 | 67.095 | 63.221 | +1.32% | +0.72% | 1.03x | 2.1 | 2026-11-19T04:15:16.738992+00:00 | Not calibrated | MODERATE 69/100 | HIGH 62/100 | Watch | WATCH |
| 10 | ADA/USD | 0.152331 | 66.636 | 58.539 | +0.71% | +0.12% | 1.75x | 2.9 | 2026-11-19T04:15:16.738992+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 11 | LTC/USD | 44.41 | 63.815 | 51.551 | +0.91% | +0.07% | 2.19x | 2.3 | 2026-11-19T04:15:16.738992+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 12 | TAO/USD | 194.3393 | 61.824 | 60.698 | +1.24% | +0.12% | 1.05x | 6.0 | 2026-11-19T04:15:16.738992+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 77.355 | 3.411 | +0.88% | 4.05x |
| 2 | VVV/USD | 70.966 | 22.396 | +0.66% | 6.09x |
| 3 | ZEC/USD | 63.221 | 924 | +0.72% | 1.03x |
| 4 | ETH/USD | 63.117 | 1795.41 | +0.24% | 4.37x |
| 5 | PYTH/USD | 62.350 | 0.05567 | +1.36% | 2.26x |
| 6 | SOL/USD | 60.704 | 74.21 | +0.12% | 1.93x |
| 7 | TAO/USD | 60.698 | 194.3393 | +0.12% | 1.05x |
| 8 | HYPE/USD | 60.015 | 67.43 | +0.24% | 3.19x |
| 9 | ADA/USD | 58.539 | 0.152331 | +0.12% | 1.75x |
| 10 | XRP/USD | 58.244 | 0.97092 | +0.32% | 15.50x |
| 11 | LINK/USD | 55.530 | 9.1092 | +0.11% | 2.22x |
| 12 | LTC/USD | 51.551 | 44.41 | +0.07% | 2.19x |

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

- Persisted scans: 752; predictions: 6168; observations: 454974.
- Matured sampled outcomes across 1/6/24/48h: 6146; gap abstentions: 13631. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44456950787 · **Generation:** 752 · **Legacy run:** 44456950787
**Main quote time:** 2026-11-19T04:15:22.217638+00:00 · **Legacy report time:** 2026-11-19T04:16:02.412089+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.411 | 96.75 | +0.88% | 4.05x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 22.396 | 89.24 | +0.66% | 6.09x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | PYTH/USD ⭐ | 0.05567 | 81.73 | +1.36% | 2.26x | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 4 | ETH/USD ⭐ | 1795.41 | 79.30 | +0.24% | 4.37x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | HYPE/USD ⭐ | 67.43 | 76.20 | +0.24% | 3.19x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | XRP/USD ⭐ | 0.97092 | 74.87 | +0.32% | 15.50x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | SOL/USD ⭐ | 74.21 | 70.64 | +0.12% | 1.93x | STRONG 80/100 | HIGH 55/100 | Watch |
| 8 | LINK/USD | 9.1092 | 68.27 | +0.11% | 2.22x | STRONG 79/100 | HIGH 55/100 | Watch |
| 9 | ZEC/USD ⭐ | 924 | 67.09 | +0.72% | 1.03x | STRONG 79/100 | HIGH 62/100 | Watch |
| 10 | ADA/USD | 0.152331 | 66.64 | +0.12% | 1.75x | MODERATE 68/100 | HIGH 55/100 | Watch |
| 11 | LTC/USD | 44.41 | 63.81 | +0.07% | 2.19x | STRONG 77/100 | HIGH 55/100 | Watch |
| 12 | TAO/USD | 194.3393 | 61.82 | +0.12% | 1.05x | MODERATE 56/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.4051 | 100.00 | +0.88% | 4.05x | 14207 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | VVV/USD ⭐ | 22.367 | 87.57 | +0.66% | 6.09x | 8861 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | PYTH/USD ⭐ | 0.05552 | 75.11 | +1.36% | 2.26x | 2027 | STRONG 93/100 | VERY_HIGH 72/100 | Watch |
| 4 | ETH/USD ⭐ | 1794.26 | 73.78 | +0.24% | 4.37x | 58417 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | ZEC/USD ⭐ | 924.35 | 70.37 | +0.72% | 1.03x | 21992 | STRONG 80/100 | HIGH 62/100 | Watch |
| 6 | HYPE/USD ⭐ | 67.43 | 67.62 | +0.24% | 3.19x | 14508 | STRONG 99/100 | HIGH 55/100 | Consider small entry |
| 7 | XRP/USD ⭐ | 0.97003 | 65.31 | +0.32% | 15.50x | 36121 | STRONG 98/100 | HIGH 55/100 | Consider small entry |
| 8 | SOL/USD ⭐ | 74.18 | 63.84 | +0.12% | 1.93x | 35065 | STRONG 77/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NEAR/USD, VVV/USD, PYTH/USD, ETH/USD, HYPE/USD, XRP/USD, SOL/USD, ZEC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
