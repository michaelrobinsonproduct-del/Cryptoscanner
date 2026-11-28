# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T11:12:51.861992+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46138540081
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 761fa69a422232f27ec0b79818ea036c70711d74 (atomic ledger/results publication)
**Ledger generation:** 2146 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 3s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 10.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | VVV/USD | 26.972 | 87.096 | 72.792 | +4.75% | +0.52% | 2.17x | 9.3 | 2026-11-28T11:12:48.364356+00:00 | Not calibrated | STRONG 99/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 429.07 | 79.651 | 80.122 | +5.35% | -1.33% | 1.62x | 24.7 | 2026-11-28T11:12:48.364356+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 77/100 | Do nothing | WATCH |
| 3 | NIGHT/USD | 0.05261 | 75.049 | 83.269 | +4.72% | -0.23% | 0.29x | 9.5 | 2026-11-28T11:12:48.364356+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 4 | SPACE/USD | 0.004391 | 61.061 | 66.097 | +5.10% | +0.44% | 0.28x | 2.3 | 2026-11-28T11:12:48.364356+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | SENT/USD | 0.024443 | 46.468 | 50.830 | +3.07% | -0.02% | 0.57x | 4.1 | 2026-11-28T11:12:48.364356+00:00 | Not calibrated | WEAK 28/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | KAVA/USD | 0.0279 | 45.120 | 29.190 | +2.20% | +0.72% | 2.23x | 36.0 | 2026-11-28T11:12:48.364356+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | CC/USD | 0.0746 | 31.287 | 33.551 | +0.61% | +0.15% | 0.70x | 9.4 | 2026-11-28T11:12:48.364356+00:00 | Not calibrated | WEAK 36/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 83.269 | 0.05261 | -0.23% | 0.29x |
| 2 | XMR/USD | 80.122 | 429.07 | -1.33% | 1.62x |
| 3 | VVV/USD | 72.792 | 26.972 | +0.52% | 2.17x |
| 4 | SPACE/USD | 66.097 | 0.004391 | +0.44% | 0.28x |
| 5 | SENT/USD | 50.830 | 0.024443 | -0.02% | 0.57x |
| 6 | CC/USD | 33.551 | 0.0746 | +0.15% | 0.70x |
| 7 | KAVA/USD | 29.190 | 0.0279 | +0.72% | 2.23x |

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

- Persisted scans: 2146; predictions: 19147; observations: 1299522.
- Matured sampled outcomes across 1/6/24/48h: 45558; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46138540081 · **Generation:** 2146 · **Legacy run:** 46138540081
**Main quote time:** 2026-11-28T11:12:51.861992+00:00 · **Legacy report time:** 2026-11-28T11:13:33.324500+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.972 | 87.10 | +0.52% | 2.17x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD | 429.07 | 79.65 | -1.33% | 1.62x | MODERATE 50/100 | VERY_HIGH 77/100 | Do nothing |
| 3 | NIGHT/USD | 0.05261 | 75.05 | -0.23% | 0.29x | WEAK 43/100 | VERY_HIGH 76/100 | Watch |
| 4 | SPACE/USD | 0.004391 | 61.06 | +0.44% | 0.28x | MODERATE 61/100 | VERY_HIGH 82/100 | Watch |
| 5 | SENT/USD | 0.024443 | 46.47 | -0.02% | 0.57x | WEAK 28/100 | EXTREME 88/100 | Do nothing |
| 6 | KAVA/USD ⭐ | 0.0279 | 45.12 | +0.72% | 2.23x | STRONG 73/100 | VERY_HIGH 72/100 | Watch |
| 7 | CC/USD | 0.0746 | 31.29 | +0.15% | 0.70x | WEAK 36/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 26.982 | 85.67 | +0.52% | 2.17x | 7726 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | KAVA/USD ⭐ | 0.0279 | 52.64 | +0.72% | 2.23x | 2172 | STRONG 76/100 | VERY_HIGH 72/100 | Watch |

**Same-run overlap:** VVV/USD, KAVA/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
