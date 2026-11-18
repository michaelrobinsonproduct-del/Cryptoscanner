# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T15:35:18.999113+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44337225765
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** dcd1a2f5f10d389df5c56d9f278cb203c14eb619 (atomic ledger/results publication)
**Ledger generation:** 602 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 23.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019816 | 80.755 | 70.029 | +6.14% | +0.99% | 1.58x | 8.1 | 2026-11-18T15:35:13.112539+00:00 | Not calibrated | STRONG 85/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | CT/USD | 0.1215 | 72.639 | 63.736 | +7.52% | -1.22% | 2.70x | 24.8 | 2026-11-18T15:35:13.112539+00:00 | Not calibrated | MODERATE 56/100 | EXTREME 89/100 | Do nothing | WATCH |
| 3 | STABLE/USD | 0.02306 | 72.317 | 65.180 | +9.55% | +0.00% | 1.71x | 21.7 | 2026-11-18T15:35:13.112539+00:00 | Not calibrated | MODERATE 61/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 4 | MNT/USD | 0.3859 | 53.754 | 52.751 | +3.38% | -0.03% | 1.11x | 7.8 | 2026-11-18T15:35:13.112539+00:00 | Not calibrated | WEAK 37/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | TRX/USD | 0.309927 | 48.606 | 45.459 | +0.66% | -0.05% | 1.34x | 0.3 | 2026-11-18T15:35:13.112539+00:00 | Not calibrated | WEAK 44/100 | HIGH 61/100 | Watch | WATCH |
| 6 | AKE/USD | 0.0104074 | 47.137 | 48.579 | +4.24% | -0.37% | 1.04x | 29.2 | 2026-11-18T15:35:13.112539+00:00 | Not calibrated | WEAK 24/100 | EXTREME 85/100 | Do nothing | WATCH |
| 7 | NIGHT/USD | 0.04548 | 46.615 | 49.555 | +1.31% | +0.53% | 0.44x | 15.4 | 2026-11-18T15:35:13.112539+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 8 | INFI/USD | 0.1385 | 40.782 | 58.469 | +9.06% | -1.84% | 0.15x | 36.2 | 2026-11-18T15:35:13.112539+00:00 | Not calibrated | WEAK 10/100 | EXTREME 100/100 | Do nothing | WATCH |
| 9 | AKT/USD | 0.5141 | 38.615 | 33.029 | +0.94% | +0.04% | 1.54x | 11.7 | 2026-11-18T15:35:13.112539+00:00 | Not calibrated | MODERATE 49/100 | HIGH 66/100 | Watch | WATCH |
| 10 | RE/USD | 0.23921 | 33.338 | 41.794 | +2.96% | -0.36% | 0.33x | 19.2 | 2026-11-18T15:35:13.112539+00:00 | Not calibrated | WEAK 17/100 | EXTREME 94/100 | Do nothing | WATCH |
| 11 | CAP/USD | 0.101431 | 31.312 | 29.188 | +0.45% | -1.10% | 1.76x | 10.7 | 2026-11-18T15:35:13.112539+00:00 | Not calibrated | WEAK 31/100 | VERY_HIGH 83/100 | Do nothing | WATCH |
| 12 | CC/USD | 0.08262 | 30.064 | 38.028 | +0.60% | -0.23% | 0.32x | 3.6 | 2026-11-18T15:35:13.112539+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 70.029 | 0.019816 | +0.99% | 1.58x |
| 2 | STABLE/USD | 65.180 | 0.02306 | +0.00% | 1.71x |
| 3 | CT/USD | 63.736 | 0.1215 | -1.22% | 2.70x |
| 4 | INFI/USD | 58.469 | 0.1385 | -1.84% | 0.15x |
| 5 | MNT/USD | 52.751 | 0.3859 | -0.03% | 1.11x |
| 6 | NIGHT/USD | 49.555 | 0.04548 | +0.53% | 0.44x |
| 7 | AKE/USD | 48.579 | 0.0104074 | -0.37% | 1.04x |
| 8 | TRX/USD | 45.459 | 0.309927 | -0.05% | 1.34x |
| 9 | RE/USD | 41.794 | 0.23921 | -0.36% | 0.33x |
| 10 | CC/USD | 38.028 | 0.08262 | -0.23% | 0.32x |
| 11 | AKT/USD | 33.029 | 0.5141 | +0.04% | 1.54x |
| 12 | CAP/USD | 29.188 | 0.101431 | -1.10% | 1.76x |

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

- Persisted scans: 602; predictions: 5160; observations: 363625.
- Matured sampled outcomes across 1/6/24/48h: 4371; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44337225765 · **Generation:** 602 · **Legacy run:** 44337225765
**Main quote time:** 2026-11-18T15:35:18.999113+00:00 · **Legacy report time:** 2026-11-18T15:35:39.480727+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019816 | 80.76 | +0.99% | 1.58x | STRONG 95/100 | HIGH 67/100 | Consider small entry |
| 2 | CT/USD | 0.1215 | 72.64 | -1.22% | 2.70x | MODERATE 56/100 | EXTREME 89/100 | Do nothing |
| 3 | STABLE/USD | 0.02306 | 72.32 | +0.00% | 1.71x | MODERATE 61/100 | VERY_HIGH 79/100 | Watch |
| 4 | MNT/USD | 0.3859 | 53.75 | -0.03% | 1.11x | WEAK 37/100 | VERY_HIGH 73/100 | Watch |
| 5 | TRX/USD | 0.309927 | 48.61 | -0.05% | 1.34x | WEAK 44/100 | HIGH 61/100 | Watch |
| 6 | AKE/USD | 0.0104074 | 47.14 | -0.37% | 1.04x | WEAK 24/100 | EXTREME 85/100 | Do nothing |
| 7 | NIGHT/USD | 0.04548 | 46.62 | +0.53% | 0.44x | MODERATE 48/100 | VERY_HIGH 76/100 | Watch |
| 8 | INFI/USD | 0.1385 | 40.78 | -1.84% | 0.15x | WEAK 10/100 | EXTREME 100/100 | Do nothing |
| 9 | AKT/USD | 0.5141 | 38.62 | +0.04% | 1.54x | MODERATE 49/100 | HIGH 66/100 | Watch |
| 10 | RE/USD | 0.23921 | 33.34 | -0.36% | 0.33x | WEAK 17/100 | EXTREME 94/100 | Do nothing |
| 11 | CAP/USD | 0.101431 | 31.31 | -1.10% | 1.76x | WEAK 31/100 | VERY_HIGH 83/100 | Do nothing |
| 12 | CC/USD | 0.08262 | 30.06 | -0.23% | 0.32x | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD ⭐ | 0.019816 | 75.92 | +0.99% | 1.58x | 5863 | STRONG 93/100 | HIGH 67/100 | Consider small entry |

**Same-run overlap:** SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
