# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T12:03:22.534905+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46142440922
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 7787d851aba8fff48b06244053153b4f600ee7fe (atomic ledger/results publication)
**Ledger generation:** 2151 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 12.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05498 | 100.920 | 93.304 | +9.43% | +0.18% | 1.67x | 10.9 | 2026-11-28T12:03:18.122225+00:00 | Not calibrated | STRONG 80/100 | HIGH 61/100 | Watch | WATCH |
| 2 | XMR/USD | 438.96 | 87.836 | 82.394 | +7.78% | +0.81% | 1.14x | 35.2 | 2026-11-28T12:03:18.122225+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | VVV/USD | 27.179 | 80.209 | 79.147 | +5.55% | +0.66% | 0.78x | 7.0 | 2026-11-28T12:03:18.122225+00:00 | Not calibrated | STRONG 70/100 | HIGH 62/100 | Watch | WATCH |
| 4 | SENT/USD | 0.024565 | 66.887 | 54.109 | +3.59% | -0.44% | 2.68x | 4.9 | 2026-11-28T12:03:18.122225+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | AKE/USD | 0.00113619 | 37.239 | 46.211 | +4.57% | -0.52% | 0.36x | 44.8 | 2026-11-28T12:03:18.122225+00:00 | Not calibrated | WEAK 9/100 | EXTREME 100/100 | Do nothing | WATCH |
| 6 | CC/USD | 0.07453 | 30.876 | 34.106 | +0.51% | -0.03% | 0.69x | 6.7 | 2026-11-28T12:03:18.122225+00:00 | Not calibrated | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 93.304 | 0.05498 | +0.18% | 1.67x |
| 2 | XMR/USD | 82.394 | 438.96 | +0.81% | 1.14x |
| 3 | VVV/USD | 79.147 | 27.179 | +0.66% | 0.78x |
| 4 | SENT/USD | 54.109 | 0.024565 | -0.44% | 2.68x |
| 5 | AKE/USD | 46.211 | 0.00113619 | -0.52% | 0.36x |
| 6 | CC/USD | 34.106 | 0.07453 | -0.03% | 0.69x |

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

- Persisted scans: 2151; predictions: 19180; observations: 1302552.
- Matured sampled outcomes across 1/6/24/48h: 45745; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
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

**Writer:** 46142440922 · **Generation:** 2151 · **Legacy run:** 46142440922
**Main quote time:** 2026-11-28T12:03:22.534905+00:00 · **Legacy report time:** 2026-11-28T12:04:21.612293+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05498 | 100.92 | +0.18% | 1.67x | STRONG 90/100 | HIGH 61/100 | Watch |
| 2 | XMR/USD ⭐ | 438.96 | 87.84 | +0.81% | 1.14x | STRONG 74/100 | VERY_HIGH 74/100 | Watch |
| 3 | VVV/USD | 27.179 | 80.21 | +0.66% | 0.78x | STRONG 70/100 | HIGH 62/100 | Watch |
| 4 | SENT/USD | 0.024565 | 66.89 | -0.44% | 2.68x | MODERATE 63/100 | VERY_HIGH 73/100 | Watch |
| 5 | AKE/USD | 0.00113619 | 37.24 | -0.52% | 0.36x | WEAK 9/100 | EXTREME 100/100 | Do nothing |
| 6 | CC/USD | 0.07453 | 30.88 | -0.03% | 0.69x | WEAK 20/100 | VERY_HIGH 81/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 436.41 | 87.99 | +0.81% | 1.14x | 17101 | STRONG 74/100 | VERY_HIGH 74/100 | Watch |
| 2 | NIGHT/USD ⭐ | 0.05377 | 87.13 | +0.18% | 1.67x | 19007 | STRONG 84/100 | HIGH 61/100 | Watch |

**Same-run overlap:** NIGHT/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
