# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T11:42:36.689871+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46140912573
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 47a31558cd11063995e9aff3574ada6bfbdd0f43 (atomic ledger/results publication)
**Ledger generation:** 2149 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 4s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 11.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05455 | 125.255 | 99.084 | +8.58% | +2.23% | 7.40x | 1.8 | 2026-11-28T11:42:33.095780+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SENT/USD | 0.024954 | 89.366 | 66.403 | +5.23% | +1.71% | 2.44x | 3.2 | 2026-11-28T11:42:33.095780+00:00 | Not calibrated | STRONG 100/100 | HIGH 67/100 | Consider small entry | WATCH |
| 3 | AKE/USD | 0.00116234 | 80.724 | 60.954 | +6.98% | +2.74% | 1.61x | 42.0 | 2026-11-28T11:42:33.095780+00:00 | Not calibrated | STRONG 70/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 4 | XMR/USD | 426.99 | 70.537 | 76.952 | +4.84% | -0.63% | 0.67x | 23.9 | 2026-11-28T11:42:33.095780+00:00 | Not calibrated | WEAK 30/100 | EXTREME 88/100 | Do nothing | WATCH |
| 5 | SPACE/USD | 0.004511 | 69.729 | 71.026 | +7.97% | +0.63% | 0.56x | 11.1 | 2026-11-28T11:42:33.095780+00:00 | Not calibrated | MODERATE 60/100 | EXTREME 88/100 | Do nothing | WATCH |
| 6 | VVV/USD | 26.907 | 68.113 | 66.960 | +4.50% | +0.58% | 0.83x | 16.3 | 2026-11-28T11:42:33.095780+00:00 | Not calibrated | MODERATE 59/100 | HIGH 68/100 | Watch | WATCH |
| 7 | CC/USD | 0.07437 | 38.017 | 32.651 | +0.30% | -0.08% | 1.58x | 6.7 | 2026-11-28T11:42:33.095780+00:00 | Not calibrated | WEAK 39/100 | HIGH 66/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 99.084 | 0.05455 | +2.23% | 7.40x |
| 2 | XMR/USD | 76.952 | 426.99 | -0.63% | 0.67x |
| 3 | SPACE/USD | 71.026 | 0.004511 | +0.63% | 0.56x |
| 4 | VVV/USD | 66.960 | 26.907 | +0.58% | 0.83x |
| 5 | SENT/USD | 66.403 | 0.024954 | +1.71% | 2.44x |
| 6 | AKE/USD | 60.954 | 0.00116234 | +2.74% | 1.61x |
| 7 | CC/USD | 32.651 | 0.07437 | -0.08% | 1.58x |

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

- Persisted scans: 2149; predictions: 19168; observations: 1301340.
- Matured sampled outcomes across 1/6/24/48h: 45661; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 4; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46140912573 · **Generation:** 2149 · **Legacy run:** 46140912573
**Main quote time:** 2026-11-28T11:42:36.689871+00:00 · **Legacy report time:** 2026-11-28T11:43:23.109236+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05455 | 125.26 | +2.23% | 7.40x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.024954 | 89.37 | +1.71% | 2.44x | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | AKE/USD ⭐ | 0.00116234 | 80.72 | +2.74% | 1.61x | STRONG 80/100 | VERY_HIGH 77/100 | Watch |
| 4 | XMR/USD | 426.99 | 70.54 | -0.63% | 0.67x | WEAK 30/100 | EXTREME 88/100 | Do nothing |
| 5 | SPACE/USD | 0.004511 | 69.73 | +0.63% | 0.56x | MODERATE 60/100 | EXTREME 88/100 | Do nothing |
| 6 | VVV/USD | 26.907 | 68.11 | +0.58% | 0.83x | MODERATE 59/100 | HIGH 68/100 | Watch |
| 7 | CC/USD | 0.07437 | 38.02 | -0.08% | 1.58x | WEAK 39/100 | HIGH 66/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05464 | 100.00 | +2.23% | 7.40x | 19246 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | SENT/USD ⭐ | 0.025008 | 87.94 | +1.71% | 2.44x | 5723 | STRONG 100/100 | HIGH 67/100 | Consider small entry |
| 3 | AKE/USD ⭐ | 0.00116234 | 84.61 | +2.74% | 1.61x | 8994 | STRONG 82/100 | VERY_HIGH 77/100 | Watch |
| 4 | XTZ/USD | 0.22755 | 30.92 | +0.50% | 3.92x | 2299 | MODERATE 65/100 | VERY_HIGH 73/100 | Watch |

**Same-run overlap:** NIGHT/USD, SENT/USD, AKE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
