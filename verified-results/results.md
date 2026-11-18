# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T06:00:09.427040+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44248052166
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** b822034f488abfd8552de602161fbd278510fa83 (atomic ledger/results publication)
**Ledger generation:** 549 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SENT/USD | 0.019711 | 67.743 | 66.777 | +5.58% | -0.91% | 1.55x | 6.6 | 2026-11-18T06:00:01.761718+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 2 | VVV/USD | 21.254 | 59.544 | 55.727 | +1.08% | +0.41% | 1.18x | 0.5 | 2026-11-18T06:00:01.761718+00:00 | Not calibrated | MODERATE 65/100 | HIGH 62/100 | Watch | WATCH |
| 3 | CT/USD | 0.1157 | 54.905 | 39.039 | +2.39% | +0.17% | 4.34x | 17.3 | 2026-11-18T06:00:01.761718+00:00 | Not calibrated | MODERATE 67/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 4 | CC/USD | 0.08472 | 54.846 | 57.100 | +3.15% | +0.26% | 0.64x | 1.2 | 2026-11-18T06:00:01.761718+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | BLESS/USD | 0.010273 | 44.825 | 36.741 | +3.00% | +3.06% | 0.28x | 32.2 | 2026-11-18T06:00:01.761718+00:00 | Not calibrated | WEAK 42/100 | EXTREME 97/100 | Do nothing | WATCH |
| 6 | PEARL/USD | 1.8461 | 31.817 | 38.480 | +1.97% | -0.09% | 0.38x | 20.1 | 2026-11-18T06:00:01.761718+00:00 | Not calibrated | WEAK 11/100 | EXTREME 93/100 | Do nothing | WATCH |
| 7 | MNT/USD | 0.3772 | 30.897 | 36.196 | +1.04% | -0.24% | 0.59x | 8.0 | 2026-11-18T06:00:01.761718+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SENT/USD | 66.777 | 0.019711 | -0.91% | 1.55x |
| 2 | CC/USD | 57.100 | 0.08472 | +0.26% | 0.64x |
| 3 | VVV/USD | 55.727 | 21.254 | +0.41% | 1.18x |
| 4 | CT/USD | 39.039 | 0.1157 | +0.17% | 4.34x |
| 5 | PEARL/USD | 38.480 | 1.8461 | -0.09% | 0.38x |
| 6 | BLESS/USD | 36.741 | 0.010273 | +3.06% | 0.28x |
| 7 | MNT/USD | 36.196 | 0.3772 | -0.24% | 0.59x |

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

- Persisted scans: 549; predictions: 4634; observations: 331348.
- Matured sampled outcomes across 1/6/24/48h: 3841; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44248052166 · **Generation:** 549 · **Legacy run:** 44248052166
**Main quote time:** 2026-11-18T06:00:09.427040+00:00 · **Legacy report time:** 2026-11-18T06:00:31.616363+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.019711 | 67.74 | -0.91% | 1.55x | MODERATE 54/100 | VERY_HIGH 73/100 | Watch |
| 2 | VVV/USD ⭐ | 21.254 | 59.54 | +0.41% | 1.18x | STRONG 75/100 | HIGH 62/100 | Watch |
| 3 | CT/USD ⭐ | 0.1157 | 54.90 | +0.17% | 4.34x | STRONG 77/100 | VERY_HIGH 73/100 | Watch |
| 4 | CC/USD | 0.08472 | 54.85 | +0.26% | 0.64x | MODERATE 57/100 | VERY_HIGH 75/100 | Watch |
| 5 | BLESS/USD | 0.010273 | 44.82 | +3.06% | 0.28x | WEAK 42/100 | EXTREME 97/100 | Do nothing |
| 6 | PEARL/USD | 1.8461 | 31.82 | -0.09% | 0.38x | WEAK 11/100 | EXTREME 93/100 | Do nothing |
| 7 | MNT/USD | 0.3772 | 30.90 | -0.24% | 0.59x | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | VVV/USD ⭐ | 21.307 | 51.04 | +0.41% | 1.18x | 7310 | STRONG 71/100 | HIGH 62/100 | Watch |
| 2 | CT/USD ⭐ | 0.1157 | 47.90 | +0.17% | 4.34x | 1214 | STRONG 74/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** VVV/USD, CT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
