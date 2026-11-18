# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T06:20:07.555869+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44250497316
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 358d5e0d3d230e0dda921eedc936807350c76b17 (atomic ledger/results publication)
**Ledger generation:** 553 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 21.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019784 | 82.197 | 70.535 | +5.97% | -0.67% | 3.73x | 4.5 | 2026-11-18T06:20:00.234043+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | CC/USD | 0.08453 | 65.902 | 52.024 | +2.92% | -0.22% | 8.12x | 8.3 | 2026-11-18T06:20:00.234043+00:00 | Not calibrated | MODERATE 63/100 | HIGH 66/100 | Watch | WATCH |
| 3 | VVV/USD | 21.261 | 62.188 | 48.103 | +1.12% | -0.18% | 2.50x | 16.4 | 2026-11-18T06:20:00.234043+00:00 | Not calibrated | MODERATE 56/100 | HIGH 67/100 | Watch | WATCH |
| 4 | ICNT/USD | 0.2888 | 58.144 | 49.807 | +4.60% | +1.58% | 1.04x | 31.2 | 2026-11-18T06:20:00.234043+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.4225 | 54.636 | 59.688 | +0.88% | +0.49% | 0.25x | 2.9 | 2026-11-18T06:20:00.234043+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | PEARL/USD | 1.8442 | 47.181 | 38.802 | +1.86% | +0.02% | 1.83x | 17.9 | 2026-11-18T06:20:00.234043+00:00 | Not calibrated | MODERATE 54/100 | HIGH 66/100 | Watch | WATCH |
| 7 | MNT/USD | 0.3786 | 38.466 | 38.849 | +1.42% | +0.11% | 0.91x | 7.9 | 2026-11-18T06:20:00.234043+00:00 | Not calibrated | WEAK 39/100 | HIGH 67/100 | Watch | WATCH |
| 8 | AKT/USD | 0.5138 | 37.406 | 34.708 | +0.88% | -0.23% | 1.39x | 7.8 | 2026-11-18T06:20:00.234043+00:00 | Not calibrated | WEAK 39/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 70.535 | 0.019784 | -0.67% | 3.73x |
| 2 | NEAR/USD | 59.688 | 3.4225 | +0.49% | 0.25x |
| 3 | CC/USD | 52.024 | 0.08453 | -0.22% | 8.12x |
| 4 | ICNT/USD | 49.807 | 0.2888 | +1.58% | 1.04x |
| 5 | VVV/USD | 48.103 | 21.261 | -0.18% | 2.50x |
| 6 | MNT/USD | 38.849 | 0.3786 | +0.11% | 0.91x |
| 7 | PEARL/USD | 38.802 | 1.8442 | +0.02% | 1.83x |
| 8 | AKT/USD | 34.708 | 0.5138 | -0.23% | 1.39x |

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

- Persisted scans: 553; predictions: 4668; observations: 333784.
- Matured sampled outcomes across 1/6/24/48h: 3930; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44250497316 · **Generation:** 553 · **Legacy run:** 44250497316
**Main quote time:** 2026-11-18T06:20:07.555869+00:00 · **Legacy report time:** 2026-11-18T06:20:23.785762+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019784 | 82.20 | -0.67% | 3.73x | STRONG 71/100 | VERY_HIGH 73/100 | Watch |
| 2 | CC/USD | 0.08453 | 65.90 | -0.22% | 8.12x | MODERATE 63/100 | HIGH 66/100 | Watch |
| 3 | VVV/USD | 21.261 | 62.19 | -0.18% | 2.50x | MODERATE 56/100 | HIGH 67/100 | Watch |
| 4 | ICNT/USD ⭐ | 0.2888 | 58.14 | +1.58% | 1.04x | MODERATE 64/100 | VERY_HIGH 79/100 | Watch |
| 5 | NEAR/USD | 3.4225 | 54.64 | +0.49% | 0.25x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 6 | PEARL/USD | 1.8442 | 47.18 | +0.02% | 1.83x | MODERATE 54/100 | HIGH 66/100 | Watch |
| 7 | MNT/USD | 0.3786 | 38.47 | +0.11% | 0.91x | WEAK 39/100 | HIGH 67/100 | Watch |
| 8 | AKT/USD | 0.5138 | 37.41 | -0.23% | 1.39x | WEAK 39/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.2892 | 76.85 | +1.58% | 1.04x | 4719 | STRONG 73/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** ICNT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
