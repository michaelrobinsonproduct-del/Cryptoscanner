# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T06:50:12.778436+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44254206855
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 1937e2550bd871a202115e83c96fc3b9182e9abf (atomic ledger/results publication)
**Ledger generation:** 559 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 1.9147 | 108.446 | 75.679 | +5.76% | +3.55% | 41.45x | 0.5 | 2026-11-18T06:50:05.597562+00:00 | Not calibrated | STRONG 100/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 2 | ICNT/USD | 0.3038 | 68.391 | 68.700 | +10.03% | +0.66% | 0.64x | 19.8 | 2026-11-18T06:50:05.597562+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 3 | SENT/USD | 0.01959 | 59.492 | 63.432 | +4.93% | -0.32% | 0.76x | 4.1 | 2026-11-18T06:50:05.597562+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 80/100 | Watch | WATCH |
| 4 | TRX/USD | 0.308845 | 55.178 | 42.635 | +0.31% | +0.15% | 2.18x | 0.0 | 2026-11-18T06:50:05.597562+00:00 | Not calibrated | STRONG 73/100 | HIGH 55/100 | Watch | WATCH |
| 5 | MNT/USD | 0.378 | 50.398 | 37.706 | +1.26% | +0.13% | 2.20x | 7.9 | 2026-11-18T06:50:05.597562+00:00 | Not calibrated | STRONG 70/100 | HIGH 60/100 | Watch | WATCH |
| 6 | CC/USD | 0.0844 | 46.157 | 51.516 | +2.76% | +0.27% | 0.33x | 7.1 | 2026-11-18T06:50:05.597562+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 7 | AKE/USD | 0.0101219 | 36.126 | 31.415 | +1.38% | +0.36% | 1.29x | 25.4 | 2026-11-18T06:50:05.597562+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | AKT/USD | 0.5155 | 33.100 | 39.969 | +1.22% | +0.21% | 0.21x | 1.9 | 2026-11-18T06:50:05.597562+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | PEARL/USD | 75.679 | 1.9147 | +3.55% | 41.45x |
| 2 | ICNT/USD | 68.700 | 0.3038 | +0.66% | 0.64x |
| 3 | SENT/USD | 63.432 | 0.01959 | -0.32% | 0.76x |
| 4 | CC/USD | 51.516 | 0.0844 | +0.27% | 0.33x |
| 5 | TRX/USD | 42.635 | 0.308845 | +0.15% | 2.18x |
| 6 | AKT/USD | 39.969 | 0.5155 | +0.21% | 0.21x |
| 7 | MNT/USD | 37.706 | 0.378 | +0.13% | 2.20x |
| 8 | AKE/USD | 31.415 | 0.0101219 | +0.36% | 1.29x |

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

- Persisted scans: 559; predictions: 4715; observations: 337438.
- Matured sampled outcomes across 1/6/24/48h: 4041; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44254206855 · **Generation:** 559 · **Legacy run:** 44254206855
**Main quote time:** 2026-11-18T06:50:12.778436+00:00 · **Legacy report time:** 2026-11-18T06:50:38.286097+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD | 1.9147 | 108.45 | +3.55% | 41.45x | STRONG 100/100 | VERY_HIGH 70/100 | Watch |
| 2 | ICNT/USD | 0.3038 | 68.39 | +0.66% | 0.64x | MODERATE 59/100 | VERY_HIGH 81/100 | Watch |
| 3 | SENT/USD | 0.01959 | 59.49 | -0.32% | 0.76x | WEAK 35/100 | VERY_HIGH 80/100 | Watch |
| 4 | TRX/USD ⭐ | 0.308845 | 55.18 | +0.15% | 2.18x | STRONG 83/100 | HIGH 55/100 | Watch |
| 5 | MNT/USD ⭐ | 0.378 | 50.40 | +0.13% | 2.20x | STRONG 80/100 | HIGH 60/100 | Watch |
| 6 | CC/USD | 0.0844 | 46.16 | +0.27% | 0.33x | MODERATE 53/100 | VERY_HIGH 75/100 | Watch |
| 7 | AKE/USD ⭐ | 0.0101219 | 36.13 | +0.36% | 1.29x | MODERATE 53/100 | VERY_HIGH 72/100 | Watch |
| 8 | AKT/USD | 0.5155 | 33.10 | +0.21% | 0.21x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | TRX/USD ⭐ | 0.308845 | 52.08 | +0.15% | 2.18x | 4108 | STRONG 81/100 | HIGH 55/100 | Watch |
| 2 | AKE/USD ⭐ | 0.0101219 | 43.45 | +0.36% | 1.29x | 4714 | MODERATE 57/100 | VERY_HIGH 72/100 | Watch |
| 3 | MNT/USD ⭐ | 0.3783 | 39.70 | +0.13% | 2.20x | 2004 | STRONG 70/100 | HIGH 66/100 | Watch |

**Same-run overlap:** TRX/USD, MNT/USD, AKE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
