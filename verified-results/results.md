# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T03:10:23.570605+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44449446330
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 9a2ab0d17686f728e7c841520836e967b54fec0d (atomic ledger/results publication)
**Ledger generation:** 739 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 10s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.022423 | 82.841 | 73.732 | +8.82% | +1.39% | 1.22x | 5.8 | 2026-11-19T03:10:13.973930+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 2 | BMT/USD | 0.01955 | 67.834 | 47.927 | +3.55% | +0.98% | 9.02x | 15.4 | 2026-11-19T03:10:13.973930+00:00 | Not calibrated | STRONG 84/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | NEAR/USD | 3.321 | 50.150 | 58.350 | +0.72% | -0.32% | 0.34x | 3.3 | 2026-11-19T03:10:13.973930+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | VVV/USD | 21.942 | 44.778 | 56.756 | +1.25% | -0.78% | 0.19x | 2.3 | 2026-11-19T03:10:13.973930+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 5 | ICP/USD | 2.239 | 44.396 | 53.169 | +2.80% | -0.13% | 0.19x | 8.9 | 2026-11-19T03:10:13.973930+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 6 | AKE/USD | 0.01051697 | 35.892 | 40.878 | +1.21% | +0.36% | 0.32x | 4.4 | 2026-11-19T03:10:13.973930+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | TON/USD | 1.024 | 33.181 | 31.324 | +0.29% | -0.19% | 1.28x | 9.8 | 2026-11-19T03:10:13.973930+00:00 | Not calibrated | WEAK 27/100 | HIGH 66/100 | Do nothing | WATCH |
| 8 | TRUMP/USD | 0.948 | 30.996 | 31.888 | +0.32% | -0.42% | 1.12x | 10.6 | 2026-11-19T03:10:13.973930+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 9 | DRV/USD | 0.26573 | 28.295 | 29.666 | +0.39% | -0.12% | 0.92x | 12.8 | 2026-11-19T03:10:13.973930+00:00 | Not calibrated | WEAK 14/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 10 | MEGA/USD | 0.05667 | 18.878 | 32.611 | +1.20% | -1.10% | 0.18x | 14.1 | 2026-11-19T03:10:13.973930+00:00 | Not calibrated | WEAK 9/100 | EXTREME 98/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 73.732 | 0.022423 | +1.39% | 1.22x |
| 2 | NEAR/USD | 58.350 | 3.321 | -0.32% | 0.34x |
| 3 | VVV/USD | 56.756 | 21.942 | -0.78% | 0.19x |
| 4 | ICP/USD | 53.169 | 2.239 | -0.13% | 0.19x |
| 5 | BMT/USD | 47.927 | 0.01955 | +0.98% | 9.02x |
| 6 | AKE/USD | 40.878 | 0.01051697 | +0.36% | 0.32x |
| 7 | MEGA/USD | 32.611 | 0.05667 | -1.10% | 0.18x |
| 8 | TRUMP/USD | 31.888 | 0.948 | -0.42% | 1.12x |
| 9 | TON/USD | 31.324 | 1.024 | -0.19% | 1.28x |
| 10 | DRV/USD | 29.666 | 0.26573 | -0.12% | 0.92x |

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

- Persisted scans: 739; predictions: 6029; observations: 447058.
- Matured sampled outcomes across 1/6/24/48h: 5987; gap abstentions: 13529. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 12; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44449446330 · **Generation:** 739 · **Legacy run:** 44449446330
**Main quote time:** 2026-11-19T03:10:23.570605+00:00 · **Legacy report time:** 2026-11-19T03:11:07.275228+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022423 | 82.84 | +1.39% | 1.22x | STRONG 86/100 | VERY_HIGH 74/100 | Watch |
| 2 | BMT/USD ⭐ | 0.01955 | 67.83 | +0.98% | 9.02x | STRONG 94/100 | VERY_HIGH 73/100 | Watch |
| 3 | NEAR/USD | 3.321 | 50.15 | -0.32% | 0.34x | WEAK 30/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | VVV/USD | 21.942 | 44.78 | -0.78% | 0.19x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 5 | ICP/USD | 2.239 | 44.40 | -0.13% | 0.19x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |
| 6 | AKE/USD | 0.01051697 | 35.89 | +0.36% | 0.32x | MODERATE 48/100 | VERY_HIGH 75/100 | Watch |
| 7 | TON/USD | 1.024 | 33.18 | -0.19% | 1.28x | WEAK 27/100 | HIGH 66/100 | Do nothing |
| 8 | TRUMP/USD | 0.948 | 31.00 | -0.42% | 1.12x | WEAK 20/100 | VERY_HIGH 79/100 | Do nothing |
| 9 | DRV/USD | 0.26573 | 28.29 | -0.12% | 0.92x | WEAK 14/100 | VERY_HIGH 79/100 | Do nothing |
| 10 | MEGA/USD | 0.05667 | 18.88 | -1.10% | 0.18x | WEAK 9/100 | EXTREME 98/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.022398 | 78.50 | +1.39% | 1.22x | 8045 | STRONG 84/100 | VERY_HIGH 74/100 | Watch |
| 2 | BMT/USD ⭐ | 0.01952 | 65.42 | +0.98% | 9.02x | 1600 | STRONG 93/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** SENT/USD, BMT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
