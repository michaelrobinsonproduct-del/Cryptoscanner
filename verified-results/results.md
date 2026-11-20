# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T07:30:51.880578+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44695345934
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 66e3fa87454db4e45170cdf787b13ee21b22a4a0 (atomic ledger/results publication)
**Ledger generation:** 948 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 15.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.4516 | 89.800 | 71.906 | +5.98% | +0.58% | 2.87x | 17.7 | 2026-11-20T07:30:46.471488+00:00 | Not calibrated | STRONG 95/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | BMT/USD | 0.02236 | 72.561 | 56.512 | +11.35% | +0.86% | 2.17x | 40.3 | 2026-11-20T07:30:46.471488+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | XLM/USD | 0.13411 | 66.531 | 60.683 | +1.06% | +0.09% | 1.54x | 3.5 | 2026-11-20T07:30:46.471488+00:00 | Not calibrated | MODERATE 68/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SYRUP/USD | 0.09982 | 54.925 | 52.204 | +3.73% | +0.36% | 1.09x | 12.0 | 2026-11-20T07:30:46.471488+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 5 | SKR/USD | 0.010321 | 53.413 | 46.014 | +2.74% | +0.72% | 1.38x | 8.7 | 2026-11-20T07:30:46.471488+00:00 | Not calibrated | STRONG 72/100 | HIGH 67/100 | Watch | WATCH |
| 6 | ATOM/USD | 1.2651 | 44.776 | 29.381 | +0.29% | +0.08% | 3.17x | 10.3 | 2026-11-20T07:30:46.471488+00:00 | Not calibrated | MODERATE 62/100 | HIGH 66/100 | Watch | WATCH |
| 7 | AUD/USD | 0.66737 | 36.131 | 40.903 | +0.28% | -0.06% | 0.55x | 0.1 | 2026-11-20T07:30:46.471488+00:00 | Not calibrated | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 8 | BLUR/USD | 0.0068 | 23.351 | 28.198 | +1.64% | +0.00% | 0.52x | 29.4 | 2026-11-20T07:30:46.471488+00:00 | Not calibrated | WEAK 22/100 | EXTREME 94/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 71.906 | 0.4516 | +0.58% | 2.87x |
| 2 | XLM/USD | 60.683 | 0.13411 | +0.09% | 1.54x |
| 3 | BMT/USD | 56.512 | 0.02236 | +0.86% | 2.17x |
| 4 | SYRUP/USD | 52.204 | 0.09982 | +0.36% | 1.09x |
| 5 | SKR/USD | 46.014 | 0.010321 | +0.72% | 1.38x |
| 6 | AUD/USD | 40.903 | 0.66737 | -0.06% | 0.55x |
| 7 | ATOM/USD | 29.381 | 1.2651 | +0.08% | 3.17x |
| 8 | BLUR/USD | 28.198 | 0.0068 | +0.00% | 0.52x |

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

- Persisted scans: 948; predictions: 8048; observations: 572811.
- Matured sampled outcomes across 1/6/24/48h: 9470; gap abstentions: 17404. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
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

**Writer:** 44695345934 · **Generation:** 948 · **Legacy run:** 44695345934
**Main quote time:** 2026-11-20T07:30:51.880578+00:00 · **Legacy report time:** 2026-11-20T07:31:40.736408+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.4516 | 89.80 | +0.58% | 2.87x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | BMT/USD | 0.02236 | 72.56 | +0.86% | 2.17x | STRONG 76/100 | VERY_HIGH 82/100 | Watch |
| 3 | XLM/USD ⭐ | 0.13411 | 66.53 | +0.09% | 1.54x | STRONG 78/100 | HIGH 55/100 | Watch |
| 4 | SYRUP/USD ⭐ | 0.09982 | 54.93 | +0.36% | 1.09x | MODERATE 67/100 | VERY_HIGH 73/100 | Watch |
| 5 | SKR/USD ⭐ | 0.010321 | 53.41 | +0.72% | 1.38x | STRONG 82/100 | HIGH 67/100 | Watch |
| 6 | ATOM/USD ⭐ | 1.2651 | 44.78 | +0.08% | 3.17x | STRONG 72/100 | HIGH 66/100 | Watch |
| 7 | AUD/USD | 0.66737 | 36.13 | -0.06% | 0.55x | WEAK 23/100 | VERY_HIGH 76/100 | Do nothing |
| 8 | BLUR/USD | 0.0068 | 23.35 | +0.00% | 0.52x | WEAK 22/100 | EXTREME 94/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD ⭐ | 0.4516 | 84.56 | +0.58% | 2.87x | 7857 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | SYRUP/USD ⭐ | 0.09982 | 69.49 | +0.36% | 1.09x | 2726 | STRONG 75/100 | VERY_HIGH 73/100 | Watch |
| 3 | XLM/USD ⭐ | 0.133861 | 63.74 | +0.09% | 1.54x | 9671 | STRONG 77/100 | HIGH 55/100 | Watch |
| 4 | SKR/USD ⭐ | 0.010337 | 52.65 | +0.72% | 1.38x | 1618 | STRONG 71/100 | VERY_HIGH 79/100 | Watch |
| 5 | ATOM/USD ⭐ | 1.2651 | 35.18 | +0.08% | 3.17x | 3279 | STRONG 73/100 | HIGH 60/100 | Watch |

**Same-run overlap:** ICNT/USD, XLM/USD, SYRUP/USD, SKR/USD, ATOM/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
