# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-28T11:32:40.157586+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/46140121949
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 2fe768f155e4afddf1a438ca2f3e5f671206f778 (atomic ledger/results publication)
**Ledger generation:** 2148 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 2s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 606; OHLC screened: 8.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.05386 | 106.965 | 93.493 | +7.21% | +1.06% | 1.82x | 13.0 | 2026-11-28T11:32:38.160061+00:00 | Not calibrated | STRONG 90/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | SPACE/USD | 0.004499 | 79.109 | 72.099 | +7.68% | +3.19% | 0.11x | 8.9 | 2026-11-28T11:32:38.160061+00:00 | Not calibrated | STRONG 70/100 | EXTREME 92/100 | Do nothing | WATCH |
| 3 | AKE/USD | 0.0011375 | 70.655 | 47.543 | +4.69% | +1.62% | 5.13x | 44.3 | 2026-11-28T11:32:38.160061+00:00 | Not calibrated | STRONG 75/100 | VERY_HIGH 77/100 | Watch | WATCH |
| 4 | XMR/USD | 424.11 | 64.620 | 73.694 | +4.13% | -0.88% | 0.53x | 20.5 | 2026-11-28T11:32:38.160061+00:00 | Not calibrated | WEAK 27/100 | EXTREME 88/100 | Do nothing | WATCH |
| 5 | SENT/USD | 0.024484 | 60.079 | 52.870 | +3.25% | -0.22% | 1.83x | 2.5 | 2026-11-28T11:32:38.160061+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | VVV/USD | 26.723 | 54.870 | 60.971 | +3.78% | -0.78% | 0.78x | 18.3 | 2026-11-28T11:32:38.160061+00:00 | Not calibrated | WEAK 27/100 | VERY_HIGH 74/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NIGHT/USD | 93.493 | 0.05386 | +1.06% | 1.82x |
| 2 | XMR/USD | 73.694 | 424.11 | -0.88% | 0.53x |
| 3 | SPACE/USD | 72.099 | 0.004499 | +3.19% | 0.11x |
| 4 | VVV/USD | 60.971 | 26.723 | -0.78% | 0.78x |
| 5 | SENT/USD | 52.870 | 0.024484 | -0.22% | 1.83x |
| 6 | AKE/USD | 47.543 | 0.0011375 | +1.62% | 5.13x |

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

- Persisted scans: 2148; predictions: 19161; observations: 1300734.
- Matured sampled outcomes across 1/6/24/48h: 45637; gap abstentions: 25968. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 155 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 2; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 46140121949 · **Generation:** 2148 · **Legacy run:** 46140121949
**Main quote time:** 2026-11-28T11:32:40.157586+00:00 · **Legacy report time:** 2026-11-28T11:33:25.681829+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.05386 | 106.97 | +1.06% | 1.82x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | SPACE/USD | 0.004499 | 79.11 | +3.19% | 0.11x | STRONG 70/100 | EXTREME 92/100 | Do nothing |
| 3 | AKE/USD ⭐ | 0.0011375 | 70.66 | +1.62% | 5.13x | STRONG 85/100 | VERY_HIGH 77/100 | Watch |
| 4 | XMR/USD | 424.11 | 64.62 | -0.88% | 0.53x | WEAK 27/100 | EXTREME 88/100 | Do nothing |
| 5 | SENT/USD | 0.024484 | 60.08 | -0.22% | 1.83x | MODERATE 50/100 | VERY_HIGH 73/100 | Watch |
| 6 | VVV/USD | 26.723 | 54.87 | -0.78% | 0.78x | WEAK 27/100 | VERY_HIGH 74/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.0538 | 100.00 | +1.06% | 1.82x | 19810 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | AKE/USD ⭐ | 0.0011375 | 86.95 | +1.62% | 5.13x | 8996 | STRONG 93/100 | VERY_HIGH 77/100 | Watch |

**Same-run overlap:** NIGHT/USD, AKE/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
