# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T03:05:28.122909+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44448841349
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 8844dc0a3eb259d17fc43a7ba1bbe80bf3eee519 (atomic ledger/results publication)
**Ledger generation:** 738 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | BMT/USD | 0.01969 | 72.480 | 53.126 | +4.29% | +0.87% | 4.28x | 15.4 | 2026-11-19T03:05:19.189871+00:00 | Not calibrated | STRONG 86/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | SENT/USD | 0.022202 | 72.109 | 72.538 | +7.75% | +0.57% | 0.67x | 8.1 | 2026-11-19T03:05:19.189871+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | NEAR/USD | 3.3212 | 63.258 | 57.943 | +0.72% | +0.19% | 1.44x | 4.2 | 2026-11-19T03:05:19.189871+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 4 | VVV/USD | 21.972 | 49.694 | 56.424 | +1.39% | +0.26% | 0.20x | 5.0 | 2026-11-19T03:05:19.189871+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | ICP/USD | 2.242 | 44.987 | 51.898 | +2.94% | -0.09% | 0.35x | 13.4 | 2026-11-19T03:05:19.189871+00:00 | Not calibrated | WEAK 22/100 | VERY_HIGH 82/100 | Do nothing | WATCH |
| 6 | TRUMP/USD | 0.951 | 36.603 | 34.135 | +0.63% | +0.11% | 1.19x | 10.5 | 2026-11-19T03:05:19.189871+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | FARTCOIN/USD | 0.0861 | 34.838 | 23.241 | +0.35% | -0.12% | 2.22x | 23.3 | 2026-11-19T03:05:19.189871+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 78/100 | Watch | WATCH |
| 8 | DRV/USD | 0.26597 | 31.870 | 32.182 | +0.48% | -0.11% | 1.02x | 9.0 | 2026-11-19T03:05:19.189871+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 9 | TON/USD | 1.025 | 31.776 | 32.020 | +0.39% | -0.29% | 1.12x | 9.8 | 2026-11-19T03:05:19.189871+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 10 | AKE/USD | 0.0104263 | 18.782 | 26.657 | +0.34% | -0.11% | 0.27x | 20.5 | 2026-11-19T03:05:19.189871+00:00 | Not calibrated | WEAK 4/100 | EXTREME 93/100 | Do nothing | WATCH |
| 11 | MEGA/USD | 0.05648 | 16.115 | 25.812 | +0.86% | -0.63% | 0.35x | 23.0 | 2026-11-19T03:05:19.189871+00:00 | Not calibrated | WEAK 3/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 72.538 | 0.022202 | +0.57% | 0.67x |
| 2 | NEAR/USD | 57.943 | 3.3212 | +0.19% | 1.44x |
| 3 | VVV/USD | 56.424 | 21.972 | +0.26% | 0.20x |
| 4 | BMT/USD | 53.126 | 0.01969 | +0.87% | 4.28x |
| 5 | ICP/USD | 51.898 | 2.242 | -0.09% | 0.35x |
| 6 | TRUMP/USD | 34.135 | 0.951 | +0.11% | 1.19x |
| 7 | DRV/USD | 32.182 | 0.26597 | -0.11% | 1.02x |
| 8 | TON/USD | 32.020 | 1.025 | -0.29% | 1.12x |
| 9 | AKE/USD | 26.657 | 0.0104263 | -0.11% | 0.27x |
| 10 | MEGA/USD | 25.812 | 0.05648 | -0.63% | 0.35x |
| 11 | FARTCOIN/USD | 23.241 | 0.0861 | -0.12% | 2.22x |

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

- Persisted scans: 738; predictions: 6019; observations: 446449.
- Matured sampled outcomes across 1/6/24/48h: 5985; gap abstentions: 13523. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44448841349 · **Generation:** 738 · **Legacy run:** 44448841349
**Main quote time:** 2026-11-19T03:05:28.122909+00:00 · **Legacy report time:** 2026-11-19T03:06:07.290934+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | BMT/USD ⭐ | 0.01969 | 72.48 | +0.87% | 4.28x | STRONG 96/100 | VERY_HIGH 73/100 | Watch |
| 2 | SENT/USD | 0.022202 | 72.11 | +0.57% | 0.67x | MODERATE 66/100 | VERY_HIGH 82/100 | Watch |
| 3 | NEAR/USD ⭐ | 3.3212 | 63.26 | +0.19% | 1.44x | STRONG 77/100 | HIGH 55/100 | Watch |
| 4 | VVV/USD | 21.972 | 49.69 | +0.26% | 0.20x | MODERATE 55/100 | VERY_HIGH 70/100 | Watch |
| 5 | ICP/USD | 2.242 | 44.99 | -0.09% | 0.35x | WEAK 22/100 | VERY_HIGH 82/100 | Do nothing |
| 6 | TRUMP/USD ⭐ | 0.951 | 36.60 | +0.11% | 1.19x | MODERATE 48/100 | VERY_HIGH 73/100 | Watch |
| 7 | FARTCOIN/USD | 0.0861 | 34.84 | -0.12% | 2.22x | WEAK 37/100 | VERY_HIGH 78/100 | Watch |
| 8 | DRV/USD | 0.26597 | 31.87 | -0.11% | 1.02x | WEAK 26/100 | VERY_HIGH 73/100 | Do nothing |
| 9 | TON/USD | 1.025 | 31.78 | -0.29% | 1.12x | WEAK 26/100 | VERY_HIGH 73/100 | Do nothing |
| 10 | AKE/USD | 0.0104263 | 18.78 | -0.11% | 0.27x | WEAK 4/100 | EXTREME 93/100 | Do nothing |
| 11 | MEGA/USD | 0.05648 | 16.11 | -0.63% | 0.35x | WEAK 3/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | BMT/USD ⭐ | 0.01969 | 72.38 | +0.87% | 4.28x | 1596 | STRONG 96/100 | VERY_HIGH 73/100 | Watch |
| 2 | NEAR/USD ⭐ | 3.3195 | 53.93 | +0.19% | 1.44x | 13315 | STRONG 72/100 | HIGH 55/100 | Watch |
| 3 | TRUMP/USD ⭐ | 0.951 | 33.69 | +0.11% | 1.19x | 2743 | MODERATE 47/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** BMT/USD, NEAR/USD, TRUMP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
