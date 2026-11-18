# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T15:10:15.371434+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44332351144
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 0b6f08a9aa6629620953f31f3b0dcd6e2b0936e5 (atomic ledger/results publication)
**Ledger generation:** 597 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 19.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | STABLE/USD | 0.0232 | 77.602 | 69.542 | +10.21% | +0.26% | 1.68x | 12.9 | 2026-11-18T15:10:08.511660+00:00 | Not calibrated | STRONG 79/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | CT/USD | 0.1222 | 71.379 | 67.803 | +8.14% | +0.74% | 0.99x | 16.3 | 2026-11-18T15:10:08.511660+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 3 | AKE/USD | 0.01066952 | 68.608 | 66.890 | +6.86% | +1.35% | 0.50x | 23.5 | 2026-11-18T15:10:08.511660+00:00 | Not calibrated | MODERATE 54/100 | EXTREME 87/100 | Do nothing | WATCH |
| 4 | TRX/USD | 0.309981 | 61.181 | 45.708 | +0.67% | +0.09% | 2.60x | 0.0 | 2026-11-18T15:10:08.511660+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04518 | 60.896 | 51.477 | +0.65% | -1.12% | 4.20x | 2.2 | 2026-11-18T15:10:08.511660+00:00 | Not calibrated | MODERATE 60/100 | HIGH 65/100 | Watch | WATCH |
| 6 | SENT/USD | 0.019511 | 56.558 | 58.777 | +4.51% | -0.97% | 1.26x | 7.7 | 2026-11-18T15:10:08.511660+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 7 | MNT/USD | 0.3852 | 55.292 | 51.418 | +3.19% | -0.36% | 1.57x | 7.8 | 2026-11-18T15:10:08.511660+00:00 | Not calibrated | MODERATE 48/100 | HIGH 66/100 | Watch | WATCH |
| 8 | ZAMA/USD | 0.06063 | 48.511 | 34.827 | +1.17% | -0.26% | 5.32x | 9.9 | 2026-11-18T15:10:08.511660+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | AKT/USD | 0.5165 | 45.210 | 35.481 | +1.41% | -0.69% | 2.32x | 13.6 | 2026-11-18T15:10:08.511660+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 10 | CC/USD | 0.083 | 41.242 | 40.087 | +1.06% | +0.07% | 1.08x | 6.0 | 2026-11-18T15:10:08.511660+00:00 | Not calibrated | MODERATE 46/100 | HIGH 67/100 | Watch | WATCH |
| 11 | ME/USD | 0.0392 | 29.838 | 29.547 | +1.55% | -0.25% | 1.16x | 25.6 | 2026-11-18T15:10:08.511660+00:00 | Not calibrated | WEAK 15/100 | EXTREME 92/100 | Do nothing | WATCH |
| 12 | XPL/USD | 0.0467 | 25.884 | 26.747 | +0.65% | +0.00% | 0.91x | 21.4 | 2026-11-18T15:10:08.511660+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | STABLE/USD | 69.542 | 0.0232 | +0.26% | 1.68x |
| 2 | CT/USD | 67.803 | 0.1222 | +0.74% | 0.99x |
| 3 | AKE/USD | 66.890 | 0.01066952 | +1.35% | 0.50x |
| 4 | SENT/USD | 58.777 | 0.019511 | -0.97% | 1.26x |
| 5 | NIGHT/USD | 51.477 | 0.04518 | -1.12% | 4.20x |
| 6 | MNT/USD | 51.418 | 0.3852 | -0.36% | 1.57x |
| 7 | TRX/USD | 45.708 | 0.309981 | +0.09% | 2.60x |
| 8 | CC/USD | 40.087 | 0.083 | +0.07% | 1.08x |
| 9 | AKT/USD | 35.481 | 0.5165 | -0.69% | 2.32x |
| 10 | ZAMA/USD | 34.827 | 0.06063 | -0.26% | 5.32x |
| 11 | ME/USD | 29.547 | 0.0392 | -0.25% | 1.16x |
| 12 | XPL/USD | 26.747 | 0.0467 | +0.00% | 0.91x |

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

- Persisted scans: 597; predictions: 5100; observations: 360580.
- Matured sampled outcomes across 1/6/24/48h: 4315; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44332351144 · **Generation:** 597 · **Legacy run:** 44332351144
**Main quote time:** 2026-11-18T15:10:15.371434+00:00 · **Legacy report time:** 2026-11-18T15:10:44.616589+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | STABLE/USD ⭐ | 0.0232 | 77.60 | +0.26% | 1.68x | STRONG 89/100 | VERY_HIGH 73/100 | Watch |
| 2 | CT/USD | 0.1222 | 71.38 | +0.74% | 0.99x | MODERATE 61/100 | VERY_HIGH 80/100 | Watch |
| 3 | AKE/USD | 0.01066952 | 68.61 | +1.35% | 0.50x | MODERATE 54/100 | EXTREME 87/100 | Do nothing |
| 4 | TRX/USD ⭐ | 0.309981 | 61.18 | +0.09% | 2.60x | STRONG 86/100 | HIGH 55/100 | Watch |
| 5 | NIGHT/USD | 0.04518 | 60.90 | -1.12% | 4.20x | MODERATE 60/100 | HIGH 65/100 | Watch |
| 6 | SENT/USD | 0.019511 | 56.56 | -0.97% | 1.26x | WEAK 38/100 | VERY_HIGH 73/100 | Watch |
| 7 | MNT/USD | 0.3852 | 55.29 | -0.36% | 1.57x | MODERATE 48/100 | HIGH 66/100 | Watch |
| 8 | ZAMA/USD | 0.06063 | 48.51 | -0.26% | 5.32x | MODERATE 54/100 | VERY_HIGH 73/100 | Watch |
| 9 | AKT/USD | 0.5165 | 45.21 | -0.69% | 2.32x | MODERATE 48/100 | VERY_HIGH 72/100 | Watch |
| 10 | CC/USD ⭐ | 0.083 | 41.24 | +0.07% | 1.08x | MODERATE 56/100 | HIGH 67/100 | Watch |
| 11 | ME/USD | 0.0392 | 29.84 | -0.25% | 1.16x | WEAK 15/100 | EXTREME 92/100 | Do nothing |
| 12 | XPL/USD | 0.0467 | 25.88 | +0.00% | 0.91x | WEAK 23/100 | VERY_HIGH 79/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | STABLE/USD ⭐ | 0.02313 | 74.09 | +0.26% | 1.68x | 2890 | STRONG 87/100 | VERY_HIGH 73/100 | Watch |
| 2 | TRX/USD ⭐ | 0.309981 | 56.31 | +0.09% | 2.60x | 4246 | STRONG 83/100 | HIGH 55/100 | Watch |
| 3 | CC/USD ⭐ | 0.083 | 39.19 | +0.07% | 1.08x | 4845 | MODERATE 55/100 | HIGH 67/100 | Watch |
| 4 | XCN/USD | 0.00312 | 37.52 | +0.65% | 2.52x | 2393 | MODERATE 64/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** STABLE/USD, TRX/USD, CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
