# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T12:52:15.073061+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46001882923
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 03898d510cd44057f4a296be872990e7ee57f5f1 (atomic ledger/results publication)
**Ledger generation:** 2010 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 758.09 | 112.495 | 98.088 | +11.21% | -0.12% | 13.66x | 3.8 | 2026-11-27T12:52:06.474701+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | HYPE/USD | 65.61 | 107.225 | 92.377 | +5.45% | -0.03% | 4.13x | 1.5 | 2026-11-27T12:52:06.474701+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 3 | SOL/USD | 72.98 | 88.897 | 74.445 | +2.88% | -0.11% | 2.99x | 1.4 | 2026-11-27T12:52:06.474701+00:00 | Not calibrated | STRONG 74/100 | HIGH 61/100 | Watch | WATCH |
| 4 | XRP/USD | 0.96983 | 82.647 | 75.056 | +2.87% | -0.25% | 1.89x | 0.1 | 2026-11-27T12:52:06.474701+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 5 | VVV/USD | 27.276 | 79.889 | 77.094 | +4.17% | +0.20% | 1.18x | 8.4 | 2026-11-27T12:52:06.474701+00:00 | Not calibrated | STRONG 75/100 | HIGH 62/100 | Watch | WATCH |
| 6 | PEPE/USD | 3.625e-06 | 74.377 | 72.027 | +4.23% | -0.33% | 1.40x | 2.8 | 2026-11-27T12:52:06.474701+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0584704 | 72.209 | 72.390 | +3.72% | -0.14% | 1.05x | 0.6 | 2026-11-27T12:52:06.474701+00:00 | Not calibrated | MODERATE 46/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XBT/USD | 61410.7 | 70.980 | 65.552 | +1.51% | -0.14% | 1.61x | 0.0 | 2026-11-27T12:52:06.474701+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 9 | KNTQ/USD | 0.22191 | 68.916 | 72.691 | +5.78% | +0.83% | 0.21x | 0.5 | 2026-11-27T12:52:06.474701+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6856 | 68.860 | 72.308 | +2.68% | +0.01% | 0.65x | 2.9 | 2026-11-27T12:52:06.474701+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ETH/USD | 1717.99 | 68.022 | 66.669 | +1.80% | -0.13% | 1.20x | 1.8 | 2026-11-27T12:52:06.474701+00:00 | Not calibrated | WEAK 44/100 | HIGH 68/100 | Watch | WATCH |
| 12 | QNT/USD | 150.66 | 67.590 | 52.922 | +2.00% | -0.07% | 4.29x | 0.7 | 2026-11-27T12:52:06.474701+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 98.088 | 758.09 | -0.12% | 13.66x |
| 2 | HYPE/USD | 92.377 | 65.61 | -0.03% | 4.13x |
| 3 | VVV/USD | 77.094 | 27.276 | +0.20% | 1.18x |
| 4 | XRP/USD | 75.056 | 0.96983 | -0.25% | 1.89x |
| 5 | SOL/USD | 74.445 | 72.98 | -0.11% | 2.99x |
| 6 | KNTQ/USD | 72.691 | 0.22191 | +0.83% | 0.21x |
| 7 | XDG/USD | 72.390 | 0.0584704 | -0.14% | 1.05x |
| 8 | SUI/USD | 72.308 | 0.6856 | +0.01% | 0.65x |
| 9 | PEPE/USD | 72.027 | 3.625e-06 | -0.33% | 1.40x |
| 10 | ETH/USD | 66.669 | 1717.99 | -0.13% | 1.20x |
| 11 | XBT/USD | 65.552 | 61410.7 | -0.14% | 1.61x |
| 12 | QNT/USD | 52.922 | 150.66 | -0.07% | 4.29x |

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

- Persisted scans: 2010; predictions: 17822; observations: 1217179.
- Matured sampled outcomes across 1/6/24/48h: 39677; gap abstentions: 25843. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
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

**Writer:** 46001882923 · **Generation:** 2010 · **Legacy run:** 46001882923
**Main quote time:** 2026-11-27T12:52:15.073061+00:00 · **Legacy report time:** 2026-11-27T12:53:09.503340+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 758.09 | 112.50 | -0.12% | 13.66x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | HYPE/USD | 65.61 | 107.22 | -0.03% | 4.13x | STRONG 80/100 | HIGH 61/100 | Watch |
| 3 | SOL/USD | 72.98 | 88.90 | -0.11% | 2.99x | STRONG 74/100 | HIGH 61/100 | Watch |
| 4 | XRP/USD | 0.96983 | 82.65 | -0.25% | 1.89x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 5 | VVV/USD ⭐ | 27.276 | 79.89 | +0.20% | 1.18x | STRONG 85/100 | HIGH 62/100 | Watch |
| 6 | PEPE/USD | 3.625e-06 | 74.38 | -0.33% | 1.40x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 7 | XDG/USD | 0.0584704 | 72.21 | -0.14% | 1.05x | MODERATE 46/100 | HIGH 68/100 | Watch |
| 8 | XBT/USD | 61410.7 | 70.98 | -0.14% | 1.61x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 9 | KNTQ/USD | 0.22191 | 68.92 | +0.83% | 0.21x | MODERATE 64/100 | VERY_HIGH 75/100 | Watch |
| 10 | SUI/USD | 0.6856 | 68.86 | +0.01% | 0.65x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 11 | ETH/USD | 1717.99 | 68.02 | -0.13% | 1.20x | WEAK 44/100 | HIGH 68/100 | Watch |
| 12 | QNT/USD | 150.66 | 67.59 | -0.07% | 4.29x | MODERATE 64/100 | HIGH 61/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 27.243 | 84.56 | +0.20% | 1.18x | 9364 | STRONG 87/100 | HIGH 62/100 | Watch |
| 2 | NEAR/USD | 3.1205 | 81.38 | +0.35% | 1.90x | 12959 | STRONG 86/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
