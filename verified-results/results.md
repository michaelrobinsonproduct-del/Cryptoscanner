# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-27T12:32:16.328967+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45999073628
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f6f7d25afabf96607c2ac3edef0e14f7c5838c82 (atomic ledger/results publication)
**Ledger generation:** 2008 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ZEC/USD | 755.88 | 110.360 | 96.165 | +10.89% | -0.16% | 8.04x | 7.7 | 2026-11-27T12:32:07.613494+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | KNTQ/USD | 0.2203 | 97.731 | 67.392 | +5.01% | +3.07% | 4.65x | 0.5 | 2026-11-27T12:32:07.613494+00:00 | Not calibrated | STRONG 100/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 3 | HYPE/USD | 65.55 | 93.438 | 90.938 | +5.35% | -0.21% | 1.36x | 3.1 | 2026-11-27T12:32:07.613494+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SOL/USD | 72.99 | 86.722 | 74.543 | +2.89% | -0.23% | 2.33x | 1.4 | 2026-11-27T12:32:07.613494+00:00 | Not calibrated | STRONG 73/100 | HIGH 61/100 | Watch | WATCH |
| 5 | UNI/USD | 4.8822 | 80.922 | 78.191 | +4.99% | -0.25% | 1.40x | 3.3 | 2026-11-27T12:32:07.613494+00:00 | Not calibrated | MODERATE 60/100 | HIGH 61/100 | Watch | WATCH |
| 6 | XRP/USD | 0.97213 | 75.067 | 76.403 | +3.12% | -0.31% | 1.02x | 0.8 | 2026-11-27T12:32:07.613494+00:00 | Not calibrated | MODERATE 48/100 | HIGH 68/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0586923 | 74.269 | 75.745 | +4.11% | -0.05% | 0.88x | 0.0 | 2026-11-27T12:32:07.613494+00:00 | Not calibrated | WEAK 42/100 | HIGH 68/100 | Watch | WATCH |
| 8 | VVV/USD | 27.172 | 74.235 | 76.260 | +3.78% | +0.47% | 0.56x | 4.4 | 2026-11-27T12:32:07.613494+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | PEPE/USD | 3.635e-06 | 67.690 | 74.254 | +4.51% | +0.11% | 0.29x | 2.8 | 2026-11-27T12:32:07.613494+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | SUI/USD | 0.6863 | 65.616 | 73.042 | +2.79% | -0.30% | 0.41x | 2.9 | 2026-11-27T12:32:07.613494+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 11 | LINK/USD | 9.516 | 64.510 | 71.275 | +2.67% | -0.11% | 0.38x | 4.8 | 2026-11-27T12:32:07.613494+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | ETH/USD | 1718.91 | 64.204 | 67.924 | +1.85% | -0.03% | 0.65x | 0.1 | 2026-11-27T12:32:07.613494+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ZEC/USD | 96.165 | 755.88 | -0.16% | 8.04x |
| 2 | HYPE/USD | 90.938 | 65.55 | -0.21% | 1.36x |
| 3 | UNI/USD | 78.191 | 4.8822 | -0.25% | 1.40x |
| 4 | XRP/USD | 76.403 | 0.97213 | -0.31% | 1.02x |
| 5 | VVV/USD | 76.260 | 27.172 | +0.47% | 0.56x |
| 6 | XDG/USD | 75.745 | 0.0586923 | -0.05% | 0.88x |
| 7 | SOL/USD | 74.543 | 72.99 | -0.23% | 2.33x |
| 8 | PEPE/USD | 74.254 | 3.635e-06 | +0.11% | 0.29x |
| 9 | SUI/USD | 73.042 | 0.6863 | -0.30% | 0.41x |
| 10 | LINK/USD | 71.275 | 9.516 | -0.11% | 0.38x |
| 11 | ETH/USD | 67.924 | 1718.91 | -0.03% | 0.65x |
| 12 | KNTQ/USD | 67.392 | 0.2203 | +3.07% | 4.65x |

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

- Persisted scans: 2008; predictions: 17798; observations: 1215973.
- Matured sampled outcomes across 1/6/24/48h: 39605; gap abstentions: 25833. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 150 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45999073628 · **Generation:** 2008 · **Legacy run:** 45999073628
**Main quote time:** 2026-11-27T12:32:16.328967+00:00 · **Legacy report time:** 2026-11-27T12:33:04.634966+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ZEC/USD | 755.88 | 110.36 | -0.16% | 8.04x | STRONG 80/100 | HIGH 61/100 | Watch |
| 2 | KNTQ/USD ⭐ | 0.2203 | 97.73 | +3.07% | 4.65x | STRONG 100/100 | VERY_HIGH 70/100 | Watch |
| 3 | HYPE/USD | 65.55 | 93.44 | -0.21% | 1.36x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 4 | SOL/USD | 72.99 | 86.72 | -0.23% | 2.33x | STRONG 73/100 | HIGH 61/100 | Watch |
| 5 | UNI/USD | 4.8822 | 80.92 | -0.25% | 1.40x | MODERATE 60/100 | HIGH 61/100 | Watch |
| 6 | XRP/USD | 0.97213 | 75.07 | -0.31% | 1.02x | MODERATE 48/100 | HIGH 68/100 | Watch |
| 7 | XDG/USD | 0.0586923 | 74.27 | -0.05% | 0.88x | WEAK 42/100 | HIGH 68/100 | Watch |
| 8 | VVV/USD | 27.172 | 74.24 | +0.47% | 0.56x | MODERATE 67/100 | VERY_HIGH 70/100 | Watch |
| 9 | PEPE/USD | 3.635e-06 | 67.69 | +0.11% | 0.29x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 10 | SUI/USD | 0.6863 | 65.62 | -0.30% | 0.41x | WEAK 38/100 | VERY_HIGH 76/100 | Watch |
| 11 | LINK/USD | 9.516 | 64.51 | -0.11% | 0.38x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |
| 12 | ETH/USD | 1718.91 | 64.20 | -0.03% | 0.65x | WEAK 37/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | KNTQ/USD ⭐ | 0.2203 | 96.42 | +3.07% | 4.65x | 2016 | STRONG 100/100 | VERY_HIGH 70/100 | Watch |

**Same-run overlap:** KNTQ/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
