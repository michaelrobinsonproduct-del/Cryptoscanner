# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T06:45:08.534828+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44253581127
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** c5db0dbbb335a0e038c05bf919ca03420c6725fb (atomic ledger/results publication)
**Ledger generation:** 558 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | PEARL/USD | 1.8899 | 91.828 | 65.767 | +4.39% | +2.21% | 38.71x | 0.5 | 2026-11-18T06:45:02.355289+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | SENT/USD | 0.01975 | 72.686 | 67.431 | +5.79% | +1.58% | 0.73x | 8.1 | 2026-11-18T06:45:02.355289+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | ICNT/USD | 0.3016 | 65.704 | 70.196 | +9.24% | +0.33% | 0.38x | 16.6 | 2026-11-18T06:45:02.355289+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 4 | MNT/USD | 0.3778 | 52.190 | 37.322 | +1.21% | -0.03% | 2.62x | 7.9 | 2026-11-18T06:45:02.355289+00:00 | Not calibrated | MODERATE 56/100 | HIGH 66/100 | Watch | WATCH |
| 5 | CC/USD | 0.08433 | 45.818 | 50.314 | +2.68% | +0.15% | 0.47x | 8.3 | 2026-11-18T06:45:02.355289+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | TRX/USD | 0.308854 | 44.145 | 42.565 | +0.31% | +0.20% | 1.06x | 0.0 | 2026-11-18T06:45:02.355289+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |
| 7 | FLR/USD | 0.00517 | 32.287 | 19.801 | +1.17% | +0.00% | 2.25x | 38.8 | 2026-11-18T06:45:02.355289+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 8 | AKT/USD | 0.5155 | 30.749 | 38.030 | +1.22% | +0.02% | 0.26x | 5.8 | 2026-11-18T06:45:02.355289+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | AKE/USD | 0.01001589 | 30.228 | 19.771 | +0.32% | -0.91% | 4.12x | 33.7 | 2026-11-18T06:45:02.355289+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 78/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 70.196 | 0.3016 | +0.33% | 0.38x |
| 2 | SENT/USD | 67.431 | 0.01975 | +1.58% | 0.73x |
| 3 | PEARL/USD | 65.767 | 1.8899 | +2.21% | 38.71x |
| 4 | CC/USD | 50.314 | 0.08433 | +0.15% | 0.47x |
| 5 | TRX/USD | 42.565 | 0.308854 | +0.20% | 1.06x |
| 6 | AKT/USD | 38.030 | 0.5155 | +0.02% | 0.26x |
| 7 | MNT/USD | 37.322 | 0.3778 | -0.03% | 2.62x |
| 8 | FLR/USD | 19.801 | 0.00517 | +0.00% | 2.25x |
| 9 | AKE/USD | 19.771 | 0.01001589 | -0.91% | 4.12x |

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

- Persisted scans: 558; predictions: 4707; observations: 336829.
- Matured sampled outcomes across 1/6/24/48h: 4021; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 15; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44253581127 · **Generation:** 558 · **Legacy run:** 44253581127
**Main quote time:** 2026-11-18T06:45:08.534828+00:00 · **Legacy report time:** 2026-11-18T06:45:31.614088+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 1.8899 | 91.83 | +2.21% | 38.71x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | SENT/USD | 0.01975 | 72.69 | +1.58% | 0.73x | MODERATE 66/100 | VERY_HIGH 82/100 | Watch |
| 3 | ICNT/USD | 0.3016 | 65.70 | +0.33% | 0.38x | MODERATE 58/100 | VERY_HIGH 81/100 | Watch |
| 4 | MNT/USD | 0.3778 | 52.19 | -0.03% | 2.62x | MODERATE 56/100 | HIGH 66/100 | Watch |
| 5 | CC/USD | 0.08433 | 45.82 | +0.15% | 0.47x | WEAK 43/100 | VERY_HIGH 75/100 | Watch |
| 6 | TRX/USD ⭐ | 0.308854 | 44.14 | +0.20% | 1.06x | MODERATE 57/100 | HIGH 62/100 | Watch |
| 7 | FLR/USD | 0.00517 | 32.29 | +0.00% | 2.25x | MODERATE 46/100 | VERY_HIGH 79/100 | Watch |
| 8 | AKT/USD | 0.5155 | 30.75 | +0.02% | 0.26x | WEAK 35/100 | VERY_HIGH 75/100 | Watch |
| 9 | AKE/USD | 0.01001589 | 30.23 | -0.91% | 4.12x | WEAK 35/100 | VERY_HIGH 78/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | PEARL/USD ⭐ | 1.8899 | 87.85 | +2.21% | 38.71x | 3931 | STRONG 100/100 | HIGH 66/100 | Consider small entry |
| 2 | TRX/USD ⭐ | 0.308854 | 47.72 | +0.20% | 1.06x | 4093 | MODERATE 59/100 | HIGH 62/100 | Watch |

**Same-run overlap:** PEARL/USD, TRX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
