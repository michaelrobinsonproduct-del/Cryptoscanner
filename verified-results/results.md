# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T12:32:31.214368+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46144917808
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 24078f942220f420e737af80178afdabd1346a36 (atomic ledger/results publication)
**Ledger generation:** 2154 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 443.11 | 92.799 | 92.439 | +8.80% | -0.64% | 1.36x | 15.1 | 2026-11-28T12:32:27.450475+00:00 | Not calibrated | MODERATE 61/100 | HIGH 67/100 | Watch | WATCH |
| 2 | NIGHT/USD | 0.05459 | 92.758 | 94.863 | +8.66% | -0.29% | 0.94x | 7.3 | 2026-11-28T12:32:27.450475+00:00 | Not calibrated | MODERATE 51/100 | HIGH 68/100 | Watch | WATCH |
| 3 | VVV/USD | 27.041 | 83.427 | 74.309 | +5.02% | -0.69% | 2.26x | 8.9 | 2026-11-28T12:32:27.450475+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SPACE/USD | 0.004461 | 68.419 | 72.053 | +6.77% | +0.70% | 0.29x | 9.0 | 2026-11-28T12:32:27.450475+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 5 | SENT/USD | 0.024441 | 49.725 | 50.050 | +3.07% | +0.35% | 0.79x | 5.7 | 2026-11-28T12:32:27.450475+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 6 | CC/USD | 0.07446 | 39.923 | 35.448 | +0.42% | +0.07% | 1.41x | 2.7 | 2026-11-28T12:32:27.450475+00:00 | Not calibrated | MODERATE 55/100 | HIGH 60/100 | Watch | WATCH |
| 7 | AKE/USD | 0.00112707 | 32.542 | 40.392 | +3.73% | -0.58% | 0.51x | 43.7 | 2026-11-28T12:32:27.450475+00:00 | Not calibrated | WEAK 6/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 94.863 | 0.05459 | -0.29% | 0.94x |
| 2 | XMR/USD | 92.439 | 443.11 | -0.64% | 1.36x |
| 3 | VVV/USD | 74.309 | 27.041 | -0.69% | 2.26x |
| 4 | SPACE/USD | 72.053 | 0.004461 | +0.70% | 0.29x |
| 5 | SENT/USD | 50.050 | 0.024441 | +0.35% | 0.79x |
| 6 | AKE/USD | 40.392 | 0.00112707 | -0.58% | 0.51x |
| 7 | CC/USD | 35.448 | 0.07446 | +0.07% | 1.41x |

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

- Persisted scans: 2154; predictions: 19201; observations: 1304370.
- Matured sampled outcomes across 1/6/24/48h: 45841; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46144917808 · **Generation:** 2154 · **Legacy run:** 46144917808
**Main quote time:** 2026-11-28T12:32:31.214368+00:00 · **Legacy report time:** 2026-11-28T12:33:11.871346+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD | 443.11 | 92.80 | -0.64% | 1.36x | MODERATE 61/100 | HIGH 67/100 | Watch |
| 2 | NIGHT/USD | 0.05459 | 92.76 | -0.29% | 0.94x | MODERATE 51/100 | HIGH 68/100 | Watch |
| 3 | VVV/USD | 27.041 | 83.43 | -0.69% | 2.26x | STRONG 72/100 | HIGH 61/100 | Watch |
| 4 | SPACE/USD | 0.004461 | 68.42 | +0.70% | 0.29x | MODERATE 64/100 | VERY_HIGH 82/100 | Watch |
| 5 | SENT/USD | 0.024441 | 49.72 | +0.35% | 0.79x | MODERATE 55/100 | VERY_HIGH 74/100 | Watch |
| 6 | CC/USD ⭐ | 0.07446 | 39.92 | +0.07% | 1.41x | MODERATE 65/100 | HIGH 60/100 | Watch |
| 7 | AKE/USD | 0.00112707 | 32.54 | -0.58% | 0.51x | WEAK 6/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.07442 | 42.86 | +0.07% | 1.41x | 4671 | MODERATE 66/100 | HIGH 60/100 | Watch |

**Same-run overlap:** CC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
