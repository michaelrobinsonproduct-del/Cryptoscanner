# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T00:32:20.717055+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45297579184
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 4141b528a8b3a535242e36eb2346717587326438 (atomic ledger/results publication)
**Ledger generation:** 1501 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.94205 | 74.096 | 56.823 | +0.28% | +0.45% | 2.83x | 0.3 | 2026-11-24T00:32:12.355549+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ADA/USD | 0.148928 | 73.553 | 56.529 | +0.32% | +0.40% | 3.07x | 1.5 | 2026-11-24T00:32:12.355549+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XLM/USD | 0.13074 | 62.005 | 57.372 | +0.57% | +0.53% | 1.20x | 3.3 | 2026-11-24T00:32:12.355549+00:00 | Not calibrated | MODERATE 66/100 | HIGH 62/100 | Watch | WATCH |
| 4 | UNI/USD | 4.868 | 60.719 | 53.754 | +0.62% | +0.53% | 1.43x | 4.1 | 2026-11-24T00:32:12.355549+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 5 | CC/USD | 0.07911 | 59.767 | 40.915 | +0.70% | +0.85% | 2.46x | 1.3 | 2026-11-24T00:32:12.355549+00:00 | Not calibrated | STRONG 85/100 | HIGH 60/100 | Watch | WATCH |
| 6 | LTC/USD | 41.59 | 58.856 | 56.670 | +0.41% | +0.41% | 1.01x | 2.4 | 2026-11-24T00:32:12.355549+00:00 | Not calibrated | MODERATE 64/100 | HIGH 62/100 | Watch | WATCH |
| 7 | NEAR/USD | 2.9912 | 58.472 | 55.509 | +0.34% | +0.75% | 0.92x | 3.7 | 2026-11-24T00:32:12.355549+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 8 | QNT/USD | 154.52 | 54.827 | 54.493 | +0.30% | +0.96% | 0.55x | 5.2 | 2026-11-24T00:32:12.355549+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | LINK/USD | 9.04571 | 53.289 | 56.089 | +0.45% | +0.34% | 0.55x | 4.2 | 2026-11-24T00:32:12.355549+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | VVV/USD | 24.531 | 51.090 | 53.705 | +0.34% | +0.51% | 0.48x | 7.3 | 2026-11-24T00:32:12.355549+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ENA/USD | 0.1015 | 48.635 | 53.287 | +0.49% | +0.89% | 0.09x | 9.9 | 2026-11-24T00:32:12.355549+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | PAXG/USD | 3640.88 | 44.429 | 52.113 | +0.55% | +0.30% | 0.08x | 1.1 | 2026-11-24T00:32:12.355549+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XLM/USD | 57.372 | 0.13074 | +0.53% | 1.20x |
| 2 | XRP/USD | 56.823 | 0.94205 | +0.45% | 2.83x |
| 3 | LTC/USD | 56.670 | 41.59 | +0.41% | 1.01x |
| 4 | ADA/USD | 56.529 | 0.148928 | +0.40% | 3.07x |
| 5 | LINK/USD | 56.089 | 9.04571 | +0.34% | 0.55x |
| 6 | NEAR/USD | 55.509 | 2.9912 | +0.75% | 0.92x |
| 7 | QNT/USD | 54.493 | 154.52 | +0.96% | 0.55x |
| 8 | UNI/USD | 53.754 | 4.868 | +0.53% | 1.43x |
| 9 | VVV/USD | 53.705 | 24.531 | +0.51% | 0.48x |
| 10 | ENA/USD | 53.287 | 0.1015 | +0.89% | 0.09x |
| 11 | PAXG/USD | 52.113 | 3640.88 | +0.30% | 0.08x |
| 12 | CC/USD | 40.915 | 0.07911 | +0.85% | 2.46x |

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

- Persisted scans: 1501; predictions: 12769; observations: 909211.
- Matured sampled outcomes across 1/6/24/48h: 23464; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 131 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 9; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45297579184 · **Generation:** 1501 · **Legacy run:** 45297579184
**Main quote time:** 2026-11-24T00:32:20.717055+00:00 · **Legacy report time:** 2026-11-24T00:33:32.068395+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.94205 | 74.10 | +0.45% | 2.83x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ADA/USD ⭐ | 0.148928 | 73.55 | +0.40% | 3.07x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XLM/USD ⭐ | 0.13074 | 62.00 | +0.53% | 1.20x | STRONG 76/100 | HIGH 62/100 | Watch |
| 4 | UNI/USD | 4.868 | 60.72 | +0.53% | 1.43x | STRONG 75/100 | HIGH 55/100 | Watch |
| 5 | CC/USD | 0.07911 | 59.77 | +0.85% | 2.46x | STRONG 85/100 | HIGH 60/100 | Watch |
| 6 | LTC/USD ⭐ | 41.59 | 58.86 | +0.41% | 1.01x | STRONG 74/100 | HIGH 62/100 | Watch |
| 7 | NEAR/USD | 2.9912 | 58.47 | +0.75% | 0.92x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 8 | QNT/USD | 154.52 | 54.83 | +0.96% | 0.55x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 9 | LINK/USD | 9.04571 | 53.29 | +0.34% | 0.55x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 10 | VVV/USD | 24.531 | 51.09 | +0.51% | 0.48x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 11 | ENA/USD | 0.1015 | 48.63 | +0.89% | 0.09x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 12 | PAXG/USD | 3640.88 | 44.43 | +0.30% | 0.08x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.94212 | 62.48 | +0.45% | 2.83x | 44133 | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 2 | XLM/USD ⭐ | 0.130812 | 61.78 | +0.53% | 1.20x | 17889 | STRONG 76/100 | HIGH 62/100 | Watch |
| 3 | ADA/USD ⭐ | 0.148924 | 60.24 | +0.40% | 3.07x | 14217 | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 4 | USELESS/USD | 0.07775 | 50.53 | +1.70% | 1.20x | 4558 | MODERATE 50/100 | VERY_HIGH 74/100 | Watch |
| 5 | LTC/USD ⭐ | 41.61 | 49.18 | +0.41% | 1.01x | 12848 | STRONG 70/100 | HIGH 62/100 | Watch |
| 6 | ALGO/USD | 0.08197 | 47.11 | +0.29% | 1.23x | 10518 | MODERATE 59/100 | HIGH 62/100 | Watch |
| 7 | TRX/USD | 0.310275 | 44.78 | +0.25% | 1.16x | 3990 | MODERATE 57/100 | HIGH 62/100 | Watch |

**Same-run overlap:** XRP/USD, ADA/USD, XLM/USD, LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
