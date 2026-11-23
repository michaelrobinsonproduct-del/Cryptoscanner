# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-23T23:41:48.916138+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45290715854
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0205f427c22b9c7ee1419f51d0280735b6e6a40e (atomic ledger/results publication)
**Ledger generation:** 1497 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ALGO/USD | 0.08117 | 92.934 | 92.570 | +7.61% | +0.17% | 0.95x | 4.9 | 2026-11-23T23:41:39.757938+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 2 | QNT/USD | 153.89 | 92.326 | 97.727 | +7.29% | -0.69% | 0.80x | 4.5 | 2026-11-23T23:41:39.757938+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 3 | CAP/USD | 0.10064 | 76.718 | 72.254 | +7.55% | -0.20% | 1.55x | 13.7 | 2026-11-23T23:41:39.757938+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 4 | SOL/USD | 71.75 | 76.546 | 65.403 | +1.59% | +0.07% | 2.08x | 1.4 | 2026-11-23T23:41:39.757938+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 5 | LTC/USD | 41.28 | 74.137 | 72.098 | +2.79% | +0.15% | 1.13x | 4.8 | 2026-11-23T23:41:39.757938+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 6 | ATOM/USD | 1.272 | 70.959 | 73.479 | +8.53% | +0.39% | 0.55x | 9.4 | 2026-11-23T23:41:39.757938+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | SHX/USD | 0.003606 | 70.238 | 70.806 | +6.84% | +0.08% | 0.90x | 11.1 | 2026-11-23T23:41:39.757938+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 8 | SUI/USD | 0.6699 | 69.243 | 69.413 | +2.17% | +0.12% | 0.92x | 1.5 | 2026-11-23T23:41:39.757938+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 9 | XRP/USD | 0.93691 | 60.499 | 62.018 | +1.01% | -0.07% | 0.88x | 0.1 | 2026-11-23T23:41:39.757938+00:00 | Not calibrated | WEAK 35/100 | HIGH 68/100 | Watch | WATCH |
| 10 | HYPE/USD | 63.49 | 49.954 | 58.986 | +0.68% | +0.05% | 0.07x | 1.6 | 2026-11-23T23:41:39.757938+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | DOT/USD | 0.6736 | 46.676 | 47.839 | +1.94% | +0.16% | 0.80x | 1.5 | 2026-11-23T23:41:39.757938+00:00 | Not calibrated | WEAK 43/100 | HIGH 67/100 | Watch | WATCH |
| 12 | TRX/USD | 0.309333 | 44.734 | 50.686 | +1.36% | -0.03% | 0.42x | 0.8 | 2026-11-23T23:41:39.757938+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 97.727 | 153.89 | -0.69% | 0.80x |
| 2 | ALGO/USD | 92.570 | 0.08117 | +0.17% | 0.95x |
| 3 | ATOM/USD | 73.479 | 1.272 | +0.39% | 0.55x |
| 4 | CAP/USD | 72.254 | 0.10064 | -0.20% | 1.55x |
| 5 | LTC/USD | 72.098 | 41.28 | +0.15% | 1.13x |
| 6 | SHX/USD | 70.806 | 0.003606 | +0.08% | 0.90x |
| 7 | SUI/USD | 69.413 | 0.6699 | +0.12% | 0.92x |
| 8 | SOL/USD | 65.403 | 71.75 | +0.07% | 2.08x |
| 9 | XRP/USD | 62.018 | 0.93691 | -0.07% | 0.88x |
| 10 | HYPE/USD | 58.986 | 63.49 | +0.05% | 0.07x |
| 11 | TRX/USD | 50.686 | 0.309333 | -0.03% | 0.42x |
| 12 | DOT/USD | 47.839 | 0.6736 | +0.16% | 0.80x |

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

- Persisted scans: 1497; predictions: 12731; observations: 906775.
- Matured sampled outcomes across 1/6/24/48h: 23212; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45290715854 · **Generation:** 1497 · **Legacy run:** 45290715854
**Main quote time:** 2026-11-23T23:41:48.916138+00:00 · **Legacy report time:** 2026-11-23T23:42:48.293838+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ALGO/USD | 0.08117 | 92.93 | +0.17% | 0.95x | MODERATE 66/100 | HIGH 62/100 | Watch |
| 2 | QNT/USD | 153.89 | 92.33 | -0.69% | 0.80x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 3 | CAP/USD | 0.10064 | 76.72 | -0.20% | 1.55x | MODERATE 53/100 | VERY_HIGH 72/100 | Watch |
| 4 | SOL/USD | 71.75 | 76.55 | +0.07% | 2.08x | STRONG 83/100 | HIGH 55/100 | Watch |
| 5 | LTC/USD ⭐ | 41.28 | 74.14 | +0.15% | 1.13x | STRONG 72/100 | HIGH 62/100 | Watch |
| 6 | ATOM/USD | 1.272 | 70.96 | +0.39% | 0.55x | MODERATE 65/100 | VERY_HIGH 75/100 | Watch |
| 7 | SHX/USD | 0.003606 | 70.24 | +0.08% | 0.90x | MODERATE 50/100 | VERY_HIGH 80/100 | Watch |
| 8 | SUI/USD | 0.6699 | 69.24 | +0.12% | 0.92x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 9 | XRP/USD | 0.93691 | 60.50 | -0.07% | 0.88x | WEAK 35/100 | HIGH 68/100 | Watch |
| 10 | HYPE/USD | 63.49 | 49.95 | +0.05% | 0.07x | MODERATE 45/100 | VERY_HIGH 70/100 | Watch |
| 11 | DOT/USD | 0.6736 | 46.68 | +0.16% | 0.80x | WEAK 43/100 | HIGH 67/100 | Watch |
| 12 | TRX/USD | 0.309333 | 44.73 | -0.03% | 0.42x | WEAK 27/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 2.3113 | 96.08 | +1.03% | 3.21x | 16233 | STRONG 98/100 | HIGH 61/100 | Consider small entry |
| 2 | LTC/USD ⭐ | 41.24 | 80.38 | +0.15% | 1.13x | 12794 | STRONG 75/100 | HIGH 62/100 | Watch |

**Same-run overlap:** LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
