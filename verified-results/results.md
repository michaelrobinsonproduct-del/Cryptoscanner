# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T04:10:02.390886+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44235367412
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** 697469aae30b203b4ab949fec1ed35a990f7de23 (atomic ledger/results publication)
**Ledger generation:** 527 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CC/USD | 0.08428 | 70.096 | 51.398 | +2.62% | +0.74% | 4.38x | 4.7 | 2026-11-18T04:09:58.221853+00:00 | Not calibrated | STRONG 90/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | XDC/USD | 0.03078 | 61.540 | 43.263 | +1.52% | +0.66% | 18.69x | 9.8 | 2026-11-18T04:09:58.221853+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 3 | NIGHT/USD | 0.04509 | 55.708 | 44.204 | +0.45% | +1.39% | 1.46x | 11.1 | 2026-11-18T04:09:58.221853+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ZAMA/USD | 0.06109 | 54.254 | 40.477 | +1.94% | -0.13% | 2.44x | 13.1 | 2026-11-18T04:09:58.221853+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 5 | SENT/USD | 0.019012 | 51.612 | 39.824 | +1.84% | -0.30% | 2.33x | 7.9 | 2026-11-18T04:09:58.221853+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | ICNT/USD | 0.2843 | 44.307 | 44.312 | +2.97% | +1.22% | 0.39x | 17.6 | 2026-11-18T04:09:58.221853+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | PEARL/USD | 1.8429 | 43.726 | 44.740 | +1.79% | +0.40% | 0.70x | 6.0 | 2026-11-18T04:09:58.221853+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 8 | AKT/USD | 0.5174 | 27.602 | 33.814 | +1.59% | +0.10% | 0.33x | 19.4 | 2026-11-18T04:09:58.221853+00:00 | Not calibrated | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | MELANIA/USD | 0.0503 | 17.151 | 33.812 | +3.29% | -1.95% | 0.31x | 39.8 | 2026-11-18T04:09:58.221853+00:00 | Not calibrated | WEAK 0/100 | EXTREME 100/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | CC/USD | 51.398 | 0.08428 | +0.74% | 4.38x |
| 2 | PEARL/USD | 44.740 | 1.8429 | +0.40% | 0.70x |
| 3 | ICNT/USD | 44.312 | 0.2843 | +1.22% | 0.39x |
| 4 | NIGHT/USD | 44.204 | 0.04509 | +1.39% | 1.46x |
| 5 | XDC/USD | 43.263 | 0.03078 | +0.66% | 18.69x |
| 6 | ZAMA/USD | 40.477 | 0.06109 | -0.13% | 2.44x |
| 7 | SENT/USD | 39.824 | 0.019012 | -0.30% | 2.33x |
| 8 | AKT/USD | 33.814 | 0.5174 | +0.10% | 0.33x |
| 9 | MELANIA/USD | 33.812 | 0.0503 | -1.95% | 0.31x |

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

- Persisted scans: 527; predictions: 4455; observations: 317950.
- Matured sampled outcomes across 1/6/24/48h: 3552; gap abstentions: 12451. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 6; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44235367412 · **Generation:** 527 · **Legacy run:** 44235367412
**Main quote time:** 2026-11-18T04:10:02.390886+00:00 · **Legacy report time:** 2026-11-18T04:10:15.613798+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.08428 | 70.10 | +0.74% | 4.38x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | XDC/USD ⭐ | 0.03078 | 61.54 | +0.66% | 18.69x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 3 | NIGHT/USD ⭐ | 0.04509 | 55.71 | +1.39% | 1.46x | STRONG 78/100 | HIGH 61/100 | Watch |
| 4 | ZAMA/USD | 0.06109 | 54.25 | -0.13% | 2.44x | MODERATE 52/100 | VERY_HIGH 72/100 | Watch |
| 5 | SENT/USD | 0.019012 | 51.61 | -0.30% | 2.33x | MODERATE 56/100 | VERY_HIGH 73/100 | Watch |
| 6 | ICNT/USD | 0.2843 | 44.31 | +1.22% | 0.39x | MODERATE 47/100 | VERY_HIGH 81/100 | Watch |
| 7 | PEARL/USD ⭐ | 1.8429 | 43.73 | +0.40% | 0.70x | MODERATE 62/100 | VERY_HIGH 75/100 | Watch |
| 8 | AKT/USD | 0.5174 | 27.60 | +0.10% | 0.33x | WEAK 29/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | MELANIA/USD | 0.0503 | 17.15 | -1.95% | 0.31x | WEAK 0/100 | EXTREME 100/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CC/USD ⭐ | 0.08428 | 72.05 | +0.62% | 5.09x | 4126 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | NIGHT/USD ⭐ | 0.04507 | 50.29 | +0.60% | 1.28x | 13871 | STRONG 70/100 | HIGH 55/100 | Watch |
| 3 | PEARL/USD ⭐ | 1.8429 | 49.96 | +0.66% | 1.35x | 4168 | STRONG 75/100 | HIGH 66/100 | Watch |
| 4 | XDC/USD ⭐ | 0.03078 | 47.51 | +0.72% | 1.16x | 5859 | MODERATE 69/100 | HIGH 62/100 | Watch |

**Same-run overlap:** CC/USD, XDC/USD, NIGHT/USD, PEARL/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
