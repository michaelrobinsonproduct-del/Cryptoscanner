# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-17T03:09:24.227200+00:00
**GitHub trigger:** scheduled (verified event=schedule; originating cron=2,7,12,17,22,27,32,37,42,47,52,57 * * * *, intended UTC minute=2,7,12,17,22,27,32,37,42,47,52,57; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44008107241
**Source SHA:** d368ec72564813f9b0a53eca24a9b768cfd51747
**Previous ledger commit:** 1f17e85f4d0f5b95a127d7cfa8a6297d952537e3 (atomic ledger/results publication)
**Ledger generation:** 451 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.049 | 85.008 | 70.112 | +3.18% | -0.02% | 21.30x | 14.3 | 2026-11-17T03:09:17.608408+00:00 | Not calibrated | MODERATE 68/100 | HIGH 67/100 | Watch | WATCH |
| 2 | INJ/USD | 7.194 | 79.595 | 70.497 | +4.28% | +0.25% | 1.78x | 8.3 | 2026-11-17T03:09:17.608408+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | NEAR/USD | 3.2024 | 79.024 | 64.731 | +1.41% | -0.14% | 2.73x | 0.3 | 2026-11-17T03:09:17.608408+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SOL/USD | 72.2 | 74.988 | 60.963 | +0.95% | -0.20% | 3.26x | 1.4 | 2026-11-17T03:09:17.608408+00:00 | Not calibrated | MODERATE 67/100 | HIGH 61/100 | Watch | WATCH |
| 5 | VVV/USD | 20.708 | 71.617 | 56.471 | +2.78% | +0.03% | 2.60x | 7.7 | 2026-11-17T03:09:17.608408+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 6 | ADA/USD | 0.153512 | 69.570 | 55.351 | +0.33% | -0.16% | 2.90x | 4.0 | 2026-11-17T03:09:17.608408+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 7 | SUI/USD | 0.7212 | 66.751 | 51.890 | +0.25% | -0.03% | 3.03x | 1.4 | 2026-11-17T03:09:17.608408+00:00 | Not calibrated | MODERATE 63/100 | HIGH 61/100 | Watch | WATCH |
| 8 | ASTER/USD | 0.57896 | 62.948 | 50.248 | +1.69% | +0.05% | 2.24x | 4.1 | 2026-11-17T03:09:17.608408+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 9 | XLM/USD | 0.138509 | 59.164 | 46.944 | +0.52% | +0.06% | 2.19x | 3.2 | 2026-11-17T03:09:17.608408+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0590411 | 55.762 | 55.358 | +0.27% | -0.11% | 1.10x | 3.0 | 2026-11-17T03:09:17.608408+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 11 | XRP/USD | 0.959 | 53.637 | 57.639 | +0.44% | -0.17% | 0.69x | 0.9 | 2026-11-17T03:09:17.608408+00:00 | Not calibrated | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 12 | AAVE/USD | 111.07 | 53.130 | 54.054 | +2.39% | +0.11% | 0.85x | 9.9 | 2026-11-17T03:09:17.608408+00:00 | Not calibrated | MODERATE 47/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INJ/USD | 70.497 | 7.194 | +0.25% | 1.78x |
| 2 | NIGHT/USD | 70.112 | 0.049 | -0.02% | 21.30x |
| 3 | NEAR/USD | 64.731 | 3.2024 | -0.14% | 2.73x |
| 4 | SOL/USD | 60.963 | 72.2 | -0.20% | 3.26x |
| 5 | XRP/USD | 57.639 | 0.959 | -0.17% | 0.69x |
| 6 | VVV/USD | 56.471 | 20.708 | +0.03% | 2.60x |
| 7 | XDG/USD | 55.358 | 0.0590411 | -0.11% | 1.10x |
| 8 | ADA/USD | 55.351 | 0.153512 | -0.16% | 2.90x |
| 9 | AAVE/USD | 54.054 | 111.07 | +0.11% | 0.85x |
| 10 | SUI/USD | 51.890 | 0.7212 | -0.03% | 3.03x |
| 11 | ASTER/USD | 50.248 | 0.57896 | +0.05% | 2.24x |
| 12 | XLM/USD | 46.944 | 0.138509 | +0.06% | 2.19x |

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

- Persisted scans: 451; predictions: 3893; observations: 271672.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 12014. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44008107241 · **Generation:** 451 · **Legacy run:** 44008107241
**Main quote time:** 2026-11-17T03:09:24.227200+00:00 · **Legacy report time:** 2026-11-17T03:09:33.980660+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD | 0.049 | 85.01 | -0.02% | 21.30x | MODERATE 68/100 | HIGH 67/100 | Watch |
| 2 | INJ/USD ⭐ | 7.194 | 79.59 | +0.25% | 1.78x | STRONG 95/100 | HIGH 55/100 | Consider small entry |
| 3 | NEAR/USD | 3.2024 | 79.02 | -0.14% | 2.73x | STRONG 70/100 | HIGH 61/100 | Watch |
| 4 | SOL/USD | 72.2 | 74.99 | -0.20% | 3.26x | MODERATE 67/100 | HIGH 61/100 | Watch |
| 5 | VVV/USD | 20.708 | 71.62 | +0.03% | 2.60x | STRONG 81/100 | HIGH 55/100 | Watch |
| 6 | ADA/USD | 0.153512 | 69.57 | -0.16% | 2.90x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 7 | SUI/USD | 0.7212 | 66.75 | -0.03% | 3.03x | MODERATE 63/100 | HIGH 61/100 | Watch |
| 8 | ASTER/USD ⭐ | 0.57896 | 62.95 | +0.05% | 2.24x | STRONG 86/100 | HIGH 55/100 | Watch |
| 9 | XLM/USD | 0.138509 | 59.16 | +0.06% | 2.19x | STRONG 75/100 | HIGH 55/100 | Watch |
| 10 | XDG/USD | 0.0590411 | 55.76 | -0.11% | 1.10x | WEAK 38/100 | HIGH 68/100 | Watch |
| 11 | XRP/USD | 0.959 | 53.64 | -0.17% | 0.69x | WEAK 32/100 | VERY_HIGH 76/100 | Do nothing |
| 12 | AAVE/USD | 111.07 | 53.13 | +0.11% | 0.85x | MODERATE 47/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | INJ/USD ⭐ | 7.199 | 89.41 | +0.25% | 1.78x | 7595 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ASTER/USD ⭐ | 0.57896 | 58.69 | +0.05% | 2.24x | 4411 | STRONG 84/100 | HIGH 55/100 | Watch |

**Same-run overlap:** INJ/USD, ASTER/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
