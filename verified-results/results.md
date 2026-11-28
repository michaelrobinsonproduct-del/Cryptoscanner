# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T19:02:58.822301+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46178781549
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** c8f455b3c287b6d840405c658f515a76765ffea7 (atomic ledger/results publication)
**Ledger generation:** 2194 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 13.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05219 | 94.433 | 78.954 | +3.88% | +0.10% | 2.99x | 3.8 | 2026-11-28T19:02:54.022217+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XMR/USD | 429.47 | 70.542 | 71.847 | +5.45% | +0.49% | 0.63x | 42.6 | 2026-11-28T19:02:54.022217+00:00 | Not calibrated | MODERATE 50/100 | EXTREME 92/100 | Do nothing | WATCH |
| 3 | VVV/USD | 26.479 | 64.400 | 57.316 | +2.84% | +0.56% | 1.43x | 8.7 | 2026-11-28T19:02:54.022217+00:00 | Not calibrated | STRONG 77/100 | HIGH 55/100 | Watch | WATCH |
| 4 | BCH/USD | 208.67 | 48.328 | 36.763 | +0.81% | -0.69% | 69.90x | 3.8 | 2026-11-28T19:02:54.022217+00:00 | Not calibrated | MODERATE 54/100 | HIGH 66/100 | Watch | WATCH |
| 5 | SENT/USD | 0.024147 | 37.632 | 40.179 | +1.83% | +0.40% | 0.54x | 7.9 | 2026-11-28T19:02:54.022217+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | CC/USD | 0.07457 | 33.929 | 36.364 | +0.57% | +0.30% | 0.61x | 4.0 | 2026-11-28T19:02:54.022217+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 78.954 | 0.05219 | +0.10% | 2.99x |
| 2 | XMR/USD | 71.847 | 429.47 | +0.49% | 0.63x |
| 3 | VVV/USD | 57.316 | 26.479 | +0.56% | 1.43x |
| 4 | SENT/USD | 40.179 | 0.024147 | +0.40% | 0.54x |
| 5 | BCH/USD | 36.763 | 208.67 | -0.69% | 69.90x |
| 6 | CC/USD | 36.364 | 0.07457 | +0.30% | 0.61x |

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

- Persisted scans: 2194; predictions: 19377; observations: 1328620.
- Matured sampled outcomes across 1/6/24/48h: 47233; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 158 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 7; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46178781549 · **Generation:** 2194 · **Legacy run:** 46178781549
**Main quote time:** 2026-11-28T19:02:58.822301+00:00 · **Legacy report time:** 2026-11-28T19:03:58.423356+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05219 | 94.43 | +0.10% | 2.99x | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD | 429.47 | 70.54 | +0.49% | 0.63x | MODERATE 50/100 | EXTREME 92/100 | Do nothing |
| 3 | VVV/USD ⭐ | 26.479 | 64.40 | +0.56% | 1.43x | STRONG 87/100 | HIGH 55/100 | Watch |
| 4 | BCH/USD | 208.67 | 48.33 | -0.69% | 69.90x | MODERATE 54/100 | HIGH 66/100 | Watch |
| 5 | SENT/USD | 0.024147 | 37.63 | +0.40% | 0.54x | MODERATE 49/100 | VERY_HIGH 82/100 | Watch |
| 6 | CC/USD | 0.07457 | 33.93 | +0.30% | 0.61x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05217 | 97.89 | +0.10% | 2.99x | 18194 | STRONG 100/100 | HIGH 55/100 | Watch |
| 2 | VVV/USD ⭐ | 26.497 | 67.35 | +0.56% | 1.43x | 6620 | STRONG 89/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NIGHT/USD, VVV/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
