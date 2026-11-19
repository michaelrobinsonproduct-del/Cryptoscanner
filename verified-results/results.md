# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T04:30:22.807420+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44458685709
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 5c8e9b28d819d2c0c2b80bc0880cd7eae53b215a (atomic ledger/results publication)
**Ledger generation:** 755 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.4026 | 89.368 | 75.863 | +3.19% | -0.30% | 4.01x | 2.9 | 2026-11-19T04:30:16.706260+00:00 | Not calibrated | STRONG 75/100 | HIGH 61/100 | Watch | WATCH |
| 2 | LUNA/USD | 4.87e-05 | 79.552 | 65.899 | +11.85% | +0.60% | 2.07x | 24.8 | 2026-11-19T04:30:16.706260+00:00 | Not calibrated | STRONG 85/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | TAO/USD | 194.8394 | 75.918 | 61.858 | +1.50% | +0.14% | 2.34x | 7.3 | 2026-11-19T04:30:16.706260+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ETH/USD | 1794.53 | 72.927 | 62.770 | +1.11% | -0.10% | 2.07x | 0.1 | 2026-11-19T04:30:16.706260+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 5 | HYPE/USD | 67.52 | 71.918 | 60.219 | +0.96% | +0.12% | 2.11x | 3.0 | 2026-11-19T04:30:16.706260+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 6 | VVV/USD | 22.512 | 71.539 | 75.254 | +3.88% | +0.35% | 0.45x | 7.6 | 2026-11-19T04:30:16.706260+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | PYTH/USD | 0.05566 | 68.669 | 64.015 | +5.50% | +0.04% | 1.45x | 12.6 | 2026-11-19T04:30:16.706260+00:00 | Not calibrated | MODERATE 64/100 | HIGH 66/100 | Watch | WATCH |
| 8 | XDG/USD | 0.0590405 | 65.701 | 53.438 | +0.57% | +0.15% | 2.15x | 0.0 | 2026-11-19T04:30:16.706260+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 9 | XBT/USD | 63314.1 | 65.392 | 58.655 | +0.52% | -0.01% | 1.68x | 0.0 | 2026-11-19T04:30:16.706260+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 10 | ZEC/USD | 928.34 | 62.192 | 66.181 | +1.80% | +0.15% | 0.53x | 2.8 | 2026-11-19T04:30:16.706260+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | LINK/USD | 9.12331 | 61.328 | 58.898 | +0.56% | +0.03% | 1.23x | 0.0 | 2026-11-19T04:30:16.706260+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 12 | SOL/USD | 74.41 | 61.316 | 62.609 | +1.18% | +0.19% | 0.78x | 1.3 | 2026-11-19T04:30:16.706260+00:00 | Not calibrated | MODERATE 51/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 75.863 | 3.4026 | -0.30% | 4.01x |
| 2 | VVV/USD | 75.254 | 22.512 | +0.35% | 0.45x |
| 3 | ZEC/USD | 66.181 | 928.34 | +0.15% | 0.53x |
| 4 | LUNA/USD | 65.899 | 4.87e-05 | +0.60% | 2.07x |
| 5 | PYTH/USD | 64.015 | 0.05566 | +0.04% | 1.45x |
| 6 | ETH/USD | 62.770 | 1794.53 | -0.10% | 2.07x |
| 7 | SOL/USD | 62.609 | 74.41 | +0.19% | 0.78x |
| 8 | TAO/USD | 61.858 | 194.8394 | +0.14% | 2.34x |
| 9 | HYPE/USD | 60.219 | 67.52 | +0.12% | 2.11x |
| 10 | LINK/USD | 58.898 | 9.12331 | +0.03% | 1.23x |
| 11 | XBT/USD | 58.655 | 63314.1 | -0.01% | 1.68x |
| 12 | XDG/USD | 53.438 | 0.0590405 | +0.15% | 2.15x |

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

- Persisted scans: 755; predictions: 6204; observations: 456801.
- Matured sampled outcomes across 1/6/24/48h: 6176; gap abstentions: 13657. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44458685709 · **Generation:** 755 · **Legacy run:** 44458685709
**Main quote time:** 2026-11-19T04:30:22.807420+00:00 · **Legacy report time:** 2026-11-19T04:31:11.928361+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.4026 | 89.37 | -0.30% | 4.01x | STRONG 75/100 | HIGH 61/100 | Watch |
| 2 | LUNA/USD | 4.87e-05 | 79.55 | +0.60% | 2.07x | STRONG 85/100 | VERY_HIGH 72/100 | Watch |
| 3 | TAO/USD ⭐ | 194.8394 | 75.92 | +0.14% | 2.34x | STRONG 93/100 | HIGH 55/100 | Watch |
| 4 | ETH/USD | 1794.53 | 72.93 | -0.10% | 2.07x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 5 | HYPE/USD ⭐ | 67.52 | 71.92 | +0.12% | 2.11x | STRONG 91/100 | HIGH 55/100 | Watch |
| 6 | VVV/USD | 22.512 | 71.54 | +0.35% | 0.45x | MODERATE 66/100 | VERY_HIGH 70/100 | Watch |
| 7 | PYTH/USD | 0.05566 | 68.67 | +0.04% | 1.45x | MODERATE 64/100 | HIGH 66/100 | Watch |
| 8 | XDG/USD | 0.0590405 | 65.70 | +0.15% | 2.15x | STRONG 78/100 | HIGH 55/100 | Watch |
| 9 | XBT/USD | 63314.1 | 65.39 | -0.01% | 1.68x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 10 | ZEC/USD | 928.34 | 62.19 | +0.15% | 0.53x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |
| 11 | LINK/USD | 9.12331 | 61.33 | +0.03% | 1.23x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 12 | SOL/USD | 74.41 | 61.32 | +0.19% | 0.78x | MODERATE 51/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TAO/USD ⭐ | 195.022 | 65.86 | +0.14% | 2.34x | 4941 | STRONG 88/100 | HIGH 55/100 | Watch |
| 2 | HYPE/USD ⭐ | 67.64 | 64.52 | +0.12% | 2.11x | 14529 | STRONG 87/100 | HIGH 55/100 | Watch |
| 3 | AKT/USD | 0.5319 | 61.10 | +0.45% | 1.22x | 3448 | MODERATE 66/100 | VERY_HIGH 74/100 | Watch |

**Same-run overlap:** TAO/USD, HYPE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
