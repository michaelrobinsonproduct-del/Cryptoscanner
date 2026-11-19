# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T02:55:21.404284+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44447678142
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** f5f0e5a5fe59c542cedb26ca0feb16904d71425e (atomic ledger/results publication)
**Ledger generation:** 736 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.3387 | 79.469 | 61.221 | +1.25% | +0.65% | 3.33x | 5.1 | 2026-11-19T02:55:15.029176+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SENT/USD | 0.022116 | 73.607 | 73.419 | +7.33% | +0.19% | 0.92x | 6.3 | 2026-11-19T02:55:15.029176+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | VVV/USD | 22.112 | 61.709 | 60.299 | +2.04% | +0.61% | 0.84x | 6.3 | 2026-11-19T02:55:15.029176+00:00 | Not calibrated | MODERATE 61/100 | HIGH 62/100 | Watch | WATCH |
| 4 | INFI/USD | 0.1214 | 53.847 | 67.787 | +6.68% | -3.57% | 1.39x | 16.5 | 2026-11-19T02:55:15.029176+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 5 | ICP/USD | 2.254 | 49.578 | 53.606 | +3.49% | +0.00% | 0.60x | 17.8 | 2026-11-19T02:55:15.029176+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 6 | TRUMP/USD | 0.953 | 46.888 | 35.612 | +0.85% | +0.00% | 2.13x | 10.5 | 2026-11-19T02:55:15.029176+00:00 | Not calibrated | MODERATE 63/100 | HIGH 66/100 | Watch | WATCH |
| 7 | MEGA/USD | 0.0573 | 39.897 | 38.830 | +2.32% | +0.77% | 0.72x | 17.5 | 2026-11-19T02:55:15.029176+00:00 | Not calibrated | MODERATE 45/100 | EXTREME 88/100 | Do nothing | WATCH |
| 8 | TON/USD | 1.026 | 39.246 | 32.726 | +0.49% | +0.00% | 1.65x | 9.7 | 2026-11-19T02:55:15.029176+00:00 | Not calibrated | MODERATE 55/100 | HIGH 60/100 | Watch | WATCH |
| 9 | DRV/USD | 0.26627 | 32.691 | 30.714 | +0.60% | +0.15% | 1.12x | 13.5 | 2026-11-19T02:55:15.029176+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 10 | AKE/USD | 0.01044898 | 24.923 | 32.729 | +0.56% | -0.20% | 0.32x | 11.4 | 2026-11-19T02:55:15.029176+00:00 | Not calibrated | WEAK 12/100 | EXTREME 87/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 73.419 | 0.022116 | +0.19% | 0.92x |
| 2 | INFI/USD | 67.787 | 0.1214 | -3.57% | 1.39x |
| 3 | NEAR/USD | 61.221 | 3.3387 | +0.65% | 3.33x |
| 4 | VVV/USD | 60.299 | 22.112 | +0.61% | 0.84x |
| 5 | ICP/USD | 53.606 | 2.254 | +0.00% | 0.60x |
| 6 | MEGA/USD | 38.830 | 0.0573 | +0.77% | 0.72x |
| 7 | TRUMP/USD | 35.612 | 0.953 | +0.00% | 2.13x |
| 8 | AKE/USD | 32.729 | 0.01044898 | -0.20% | 0.32x |
| 9 | TON/USD | 32.726 | 1.026 | +0.00% | 1.65x |
| 10 | DRV/USD | 30.714 | 0.26627 | +0.15% | 1.12x |

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

- Persisted scans: 736; predictions: 5997; observations: 445231.
- Matured sampled outcomes across 1/6/24/48h: 5961; gap abstentions: 13511. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44447678142 · **Generation:** 736 · **Legacy run:** 44447678142
**Main quote time:** 2026-11-19T02:55:21.404284+00:00 · **Legacy report time:** 2026-11-19T02:55:58.632097+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.3387 | 79.47 | +0.65% | 3.33x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SENT/USD | 0.022116 | 73.61 | +0.19% | 0.92x | MODERATE 57/100 | VERY_HIGH 74/100 | Watch |
| 3 | VVV/USD | 22.112 | 61.71 | +0.61% | 0.84x | MODERATE 61/100 | HIGH 62/100 | Watch |
| 4 | INFI/USD | 0.1214 | 53.85 | -3.57% | 1.39x | WEAK 42/100 | VERY_HIGH 83/100 | Do nothing |
| 5 | ICP/USD | 2.254 | 49.58 | +0.00% | 0.60x | WEAK 40/100 | VERY_HIGH 76/100 | Watch |
| 6 | TRUMP/USD | 0.953 | 46.89 | +0.00% | 2.13x | MODERATE 63/100 | HIGH 66/100 | Watch |
| 7 | MEGA/USD | 0.0573 | 39.90 | +0.77% | 0.72x | MODERATE 45/100 | EXTREME 88/100 | Do nothing |
| 8 | TON/USD | 1.026 | 39.25 | +0.00% | 1.65x | MODERATE 55/100 | HIGH 60/100 | Watch |
| 9 | DRV/USD | 0.26627 | 32.69 | +0.15% | 1.12x | WEAK 36/100 | VERY_HIGH 73/100 | Watch |
| 10 | AKE/USD | 0.01044898 | 24.92 | -0.20% | 0.32x | WEAK 12/100 | EXTREME 87/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.3429 | 63.51 | +0.65% | 3.33x | 13327 | STRONG 97/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
