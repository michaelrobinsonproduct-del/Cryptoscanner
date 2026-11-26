# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T20:51:22.340875+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45893818547
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c530e973d7a7f01d7f3202fd7e72c1e1b40eb39f (atomic ledger/results publication)
**Ledger generation:** 1912 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 599; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | AKT/USD | 0.5054 | 87.946 | 76.874 | +6.83% | -0.24% | 2.23x | 2.0 | 2026-11-26T20:51:13.645369+00:00 | Not calibrated | STRONG 74/100 | HIGH 66/100 | Watch | WATCH |
| 2 | DRV/USD | 0.38971 | 85.450 | 75.031 | +8.92% | +0.89% | 1.60x | 14.9 | 2026-11-26T20:51:13.645369+00:00 | Not calibrated | STRONG 83/100 | HIGH 61/100 | Consider small entry | WATCH |
| 3 | LTC/USD | 43.84 | 76.269 | 72.379 | +2.65% | +0.09% | 1.34x | 2.3 | 2026-11-26T20:51:13.645369+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 4 | ADA/USD | 0.15059 | 74.013 | 75.688 | +3.31% | -0.14% | 0.90x | 4.9 | 2026-11-26T20:51:13.645369+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 5 | HBAR/USD | 0.05511 | 73.966 | 73.568 | +5.78% | -0.18% | 1.13x | 3.6 | 2026-11-26T20:51:13.645369+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | WIF/USD | 0.1378 | 72.719 | 73.217 | +8.25% | +0.15% | 0.88x | 7.3 | 2026-11-26T20:51:13.645369+00:00 | Not calibrated | MODERATE 56/100 | HIGH 67/100 | Watch | WATCH |
| 7 | XBT/USD | 60697.8 | 70.696 | 58.809 | +0.55% | +0.03% | 2.17x | 0.0 | 2026-11-26T20:51:13.645369+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6743 | 67.216 | 59.825 | +1.20% | -0.01% | 1.75x | 1.5 | 2026-11-26T20:51:13.645369+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XRP/USD | 0.95166 | 65.176 | 66.023 | +1.61% | -0.17% | 1.00x | 0.5 | 2026-11-26T20:51:13.645369+00:00 | Not calibrated | WEAK 43/100 | HIGH 68/100 | Watch | WATCH |
| 10 | SOL/USD | 71.27 | 63.163 | 63.050 | +1.25% | -0.07% | 1.05x | 1.4 | 2026-11-26T20:51:13.645369+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 11 | ETH/USD | 1703.06 | 58.031 | 60.209 | +0.75% | +0.04% | 0.76x | 0.1 | 2026-11-26T20:51:13.645369+00:00 | Not calibrated | MODERATE 49/100 | HIGH 62/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0569208 | 52.196 | 56.405 | +1.72% | -0.12% | 0.64x | 0.5 | 2026-11-26T20:51:13.645369+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AKT/USD | 76.874 | 0.5054 | -0.24% | 2.23x |
| 2 | ADA/USD | 75.688 | 0.15059 | -0.14% | 0.90x |
| 3 | DRV/USD | 75.031 | 0.38971 | +0.89% | 1.60x |
| 4 | HBAR/USD | 73.568 | 0.05511 | -0.18% | 1.13x |
| 5 | WIF/USD | 73.217 | 0.1378 | +0.15% | 0.88x |
| 6 | LTC/USD | 72.379 | 43.84 | +0.09% | 1.34x |
| 7 | XRP/USD | 66.023 | 0.95166 | -0.17% | 1.00x |
| 8 | SOL/USD | 63.050 | 71.27 | -0.07% | 1.05x |
| 9 | ETH/USD | 60.209 | 1703.06 | +0.04% | 0.76x |
| 10 | SUI/USD | 59.825 | 0.6743 | -0.01% | 1.75x |
| 11 | XBT/USD | 58.809 | 60697.8 | +0.03% | 2.17x |
| 12 | XDG/USD | 56.405 | 0.0569208 | -0.12% | 0.64x |

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

- Persisted scans: 1912; predictions: 16679; observations: 1158222.
- Matured sampled outcomes across 1/6/24/48h: 36236; gap abstentions: 25246. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45893818547 · **Generation:** 1912 · **Legacy run:** 45893818547
**Main quote time:** 2026-11-26T20:51:22.340875+00:00 · **Legacy report time:** 2026-11-26T20:52:00.726384+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | AKT/USD | 0.5054 | 87.95 | -0.24% | 2.23x | STRONG 74/100 | HIGH 66/100 | Watch |
| 2 | DRV/USD ⭐ | 0.38971 | 85.45 | +0.89% | 1.60x | STRONG 93/100 | HIGH 61/100 | Consider small entry |
| 3 | LTC/USD ⭐ | 43.84 | 76.27 | +0.09% | 1.34x | STRONG 83/100 | HIGH 55/100 | Watch |
| 4 | ADA/USD | 0.15059 | 74.01 | -0.14% | 0.90x | WEAK 42/100 | HIGH 68/100 | Watch |
| 5 | HBAR/USD | 0.05511 | 73.97 | -0.18% | 1.13x | MODERATE 47/100 | VERY_HIGH 73/100 | Watch |
| 6 | WIF/USD | 0.1378 | 72.72 | +0.15% | 0.88x | MODERATE 56/100 | HIGH 67/100 | Watch |
| 7 | XBT/USD | 60697.8 | 70.70 | +0.03% | 2.17x | STRONG 80/100 | HIGH 55/100 | Watch |
| 8 | SUI/USD | 0.6743 | 67.22 | -0.01% | 1.75x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 9 | XRP/USD | 0.95166 | 65.18 | -0.17% | 1.00x | WEAK 43/100 | HIGH 68/100 | Watch |
| 10 | SOL/USD | 71.27 | 63.16 | -0.07% | 1.05x | WEAK 42/100 | HIGH 68/100 | Watch |
| 11 | ETH/USD | 1703.06 | 58.03 | +0.04% | 0.76x | MODERATE 49/100 | HIGH 62/100 | Watch |
| 12 | XDG/USD | 0.0569208 | 52.20 | -0.12% | 0.64x | WEAK 31/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CRV/USD | 0.17857 | 82.31 | +0.31% | 4.28x | 3901 | STRONG 91/100 | HIGH 66/100 | Consider small entry |
| 2 | LTC/USD ⭐ | 43.86 | 81.40 | +0.09% | 1.34x | 14339 | STRONG 86/100 | HIGH 55/100 | Watch |
| 3 | DRV/USD ⭐ | 0.38971 | 79.54 | +0.89% | 1.60x | 7756 | STRONG 90/100 | HIGH 61/100 | Consider small entry |

**Same-run overlap:** DRV/USD, LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
