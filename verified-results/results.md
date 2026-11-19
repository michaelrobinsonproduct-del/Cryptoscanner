# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T03:25:17.889724+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44451218854
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 570169f371d2d4f6b01aa6cf43c29a7ccd7d9ab6 (atomic ledger/results publication)
**Ledger generation:** 742 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.3491 | 73.217 | 63.885 | +1.57% | +0.85% | 1.51x | 4.2 | 2026-11-19T03:25:11.042723+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | INFI/USD | 0.1194 | 72.936 | 57.097 | +4.92% | +0.17% | 2.51x | 16.8 | 2026-11-19T03:25:11.042723+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | VVV/USD | 22.007 | 51.882 | 57.383 | +1.55% | +0.30% | 0.30x | 5.5 | 2026-11-19T03:25:11.042723+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | AKE/USD | 0.01050425 | 47.145 | 38.083 | +1.09% | +0.17% | 1.82x | 8.2 | 2026-11-19T03:25:11.042723+00:00 | Not calibrated | MODERATE 59/100 | HIGH 60/100 | Watch | WATCH |
| 5 | ICP/USD | 2.238 | 43.723 | 50.632 | +2.75% | -0.22% | 0.42x | 13.4 | 2026-11-19T03:25:11.042723+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 6 | TRUMP/USD | 0.954 | 32.889 | 36.358 | +0.95% | +0.42% | 0.44x | 10.5 | 2026-11-19T03:25:11.042723+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | WIF/USD | 0.1329 | 32.308 | 30.219 | +0.45% | +0.38% | 1.02x | 7.5 | 2026-11-19T03:25:11.042723+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 8 | FIL/USD | 0.569 | 29.221 | 25.681 | +0.35% | +0.89% | 0.91x | 17.6 | 2026-11-19T03:25:11.042723+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | MEGA/USD | 0.05623 | 25.806 | 27.972 | +0.41% | -0.78% | 1.17x | 12.5 | 2026-11-19T03:25:11.042723+00:00 | Not calibrated | WEAK 18/100 | EXTREME 86/100 | Do nothing | WATCH |
| 10 | TON/USD | 1.024 | 24.453 | 31.281 | +0.29% | +0.00% | 0.32x | 9.8 | 2026-11-19T03:25:11.042723+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 75/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 63.885 | 3.3491 | +0.85% | 1.51x |
| 2 | VVV/USD | 57.383 | 22.007 | +0.30% | 0.30x |
| 3 | INFI/USD | 57.097 | 0.1194 | +0.17% | 2.51x |
| 4 | ICP/USD | 50.632 | 2.238 | -0.22% | 0.42x |
| 5 | AKE/USD | 38.083 | 0.01050425 | +0.17% | 1.82x |
| 6 | TRUMP/USD | 36.358 | 0.954 | +0.42% | 0.44x |
| 7 | TON/USD | 31.281 | 1.024 | +0.00% | 0.32x |
| 8 | WIF/USD | 30.219 | 0.1329 | +0.38% | 1.02x |
| 9 | MEGA/USD | 27.972 | 0.05623 | -0.78% | 1.17x |
| 10 | FIL/USD | 25.681 | 0.569 | +0.89% | 0.91x |

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

- Persisted scans: 742; predictions: 6055; observations: 448885.
- Matured sampled outcomes across 1/6/24/48h: 6011; gap abstentions: 13544. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 14; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44451218854 · **Generation:** 742 · **Legacy run:** 44451218854
**Main quote time:** 2026-11-19T03:25:17.889724+00:00 · **Legacy report time:** 2026-11-19T03:25:56.628451+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.3491 | 73.22 | +0.85% | 1.51x | STRONG 92/100 | HIGH 55/100 | Consider small entry |
| 2 | INFI/USD ⭐ | 0.1194 | 72.94 | +0.17% | 2.51x | STRONG 86/100 | VERY_HIGH 73/100 | Watch |
| 3 | VVV/USD | 22.007 | 51.88 | +0.30% | 0.30x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 4 | AKE/USD ⭐ | 0.01050425 | 47.14 | +0.17% | 1.82x | MODERATE 69/100 | HIGH 60/100 | Watch |
| 5 | ICP/USD | 2.238 | 43.72 | -0.22% | 0.42x | WEAK 22/100 | VERY_HIGH 82/100 | Do nothing |
| 6 | TRUMP/USD | 0.954 | 32.89 | +0.42% | 0.44x | WEAK 41/100 | VERY_HIGH 81/100 | Watch |
| 7 | WIF/USD | 0.1329 | 32.31 | +0.38% | 1.02x | MODERATE 51/100 | VERY_HIGH 74/100 | Watch |
| 8 | FIL/USD | 0.569 | 29.22 | +0.89% | 0.91x | WEAK 40/100 | VERY_HIGH 73/100 | Watch |
| 9 | MEGA/USD | 0.05623 | 25.81 | -0.78% | 1.17x | WEAK 18/100 | EXTREME 86/100 | Do nothing |
| 10 | TON/USD | 1.024 | 24.45 | +0.00% | 0.32x | WEAK 32/100 | VERY_HIGH 75/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INFI/USD ⭐ | 0.1194 | 77.17 | +0.17% | 2.51x | 3588 | STRONG 94/100 | HIGH 67/100 | Watch |
| 2 | NEAR/USD ⭐ | 3.3491 | 66.44 | +0.85% | 1.51x | 13552 | STRONG 88/100 | HIGH 55/100 | Consider small entry |
| 3 | TRX/USD | 0.309848 | 53.61 | +0.11% | 3.52x | 4227 | STRONG 72/100 | HIGH 55/100 | Watch |
| 4 | LTC/USD | 44.08 | 46.43 | +0.64% | 1.10x | 11688 | MODERATE 58/100 | HIGH 62/100 | Watch |
| 5 | AKE/USD ⭐ | 0.01050004 | 41.14 | +0.17% | 1.82x | 3481 | MODERATE 61/100 | HIGH 66/100 | Watch |

**Same-run overlap:** NEAR/USD, INFI/USD, AKE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
