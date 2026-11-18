# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T05:55:04.733229+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44247489961
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 973dd40d9a689a359e683c9698b5f4e93c3bde9d (atomic ledger/results publication)
**Ledger generation:** 548 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 18.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.2856 | 69.091 | 51.761 | +3.44% | +3.77% | 0.85x | 10.5 | 2026-11-18T05:54:58.653191+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 83/100 | Watch | WATCH |
| 2 | VVV/USD | 21.224 | 66.146 | 50.650 | +0.94% | +0.10% | 16.27x | 8.5 | 2026-11-18T05:54:58.653191+00:00 | Not calibrated | STRONG 78/100 | HIGH 55/100 | Watch | WATCH |
| 3 | SENT/USD | 0.019503 | 54.297 | 58.663 | +4.47% | -0.56% | 0.84x | 7.2 | 2026-11-18T05:54:58.653191+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 80/100 | Do nothing | WATCH |
| 4 | CT/USD | 0.1154 | 52.190 | 37.190 | +2.12% | +0.00% | 3.78x | 17.3 | 2026-11-18T05:54:58.653191+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | CC/USD | 0.08459 | 46.322 | 53.014 | +3.00% | +0.15% | 0.25x | 7.1 | 2026-11-18T05:54:58.653191+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 6 | MNT/USD | 0.3775 | 37.013 | 38.089 | +1.13% | -0.11% | 0.95x | 5.3 | 2026-11-18T05:54:58.653191+00:00 | Not calibrated | WEAK 24/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 7 | PEARL/USD | 1.8489 | 35.642 | 43.100 | +2.12% | +0.22% | 0.15x | 13.0 | 2026-11-18T05:54:58.653191+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 58.663 | 0.019503 | -0.56% | 0.84x |
| 2 | CC/USD | 53.014 | 0.08459 | +0.15% | 0.25x |
| 3 | ICNT/USD | 51.761 | 0.2856 | +3.77% | 0.85x |
| 4 | VVV/USD | 50.650 | 21.224 | +0.10% | 16.27x |
| 5 | PEARL/USD | 43.100 | 1.8489 | +0.22% | 0.15x |
| 6 | MNT/USD | 38.089 | 0.3775 | -0.11% | 0.95x |
| 7 | CT/USD | 37.190 | 0.1154 | +0.00% | 3.78x |

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

- Persisted scans: 548; predictions: 4627; observations: 330739.
- Matured sampled outcomes across 1/6/24/48h: 3829; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44247489961 · **Generation:** 548 · **Legacy run:** 44247489961
**Main quote time:** 2026-11-18T05:55:04.733229+00:00 · **Legacy report time:** 2026-11-18T05:55:19.810808+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD | 0.2856 | 69.09 | +3.77% | 0.85x | MODERATE 60/100 | VERY_HIGH 83/100 | Watch |
| 2 | VVV/USD | 21.224 | 66.15 | +0.10% | 16.27x | STRONG 78/100 | HIGH 55/100 | Watch |
| 3 | SENT/USD | 0.019503 | 54.30 | -0.56% | 0.84x | WEAK 32/100 | VERY_HIGH 80/100 | Do nothing |
| 4 | CT/USD | 0.1154 | 52.19 | +0.00% | 3.78x | MODERATE 66/100 | VERY_HIGH 73/100 | Watch |
| 5 | CC/USD | 0.08459 | 46.32 | +0.15% | 0.25x | WEAK 43/100 | VERY_HIGH 75/100 | Watch |
| 6 | MNT/USD | 0.3775 | 37.01 | -0.11% | 0.95x | WEAK 24/100 | VERY_HIGH 73/100 | Do nothing |
| 7 | PEARL/USD | 1.8489 | 35.64 | +0.22% | 0.15x | WEAK 43/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
