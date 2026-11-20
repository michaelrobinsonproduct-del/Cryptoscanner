# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T08:20:44.602772+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44701626799
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** 1df5376ebb8048cec4679228cbb5c5f7f292b40e (atomic ledger/results publication)
**Ledger generation:** 953 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 606; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.4556 | 68.033 | 72.978 | +6.92% | +0.07% | 0.47x | 22.0 | 2026-11-20T08:20:38.659566+00:00 | Not calibrated | WEAK 44/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 2 | SKR/USD | 0.010563 | 67.346 | 59.252 | +5.15% | +0.74% | 1.44x | 16.2 | 2026-11-20T08:20:38.659566+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 3 | SYRUP/USD | 0.09963 | 62.115 | 49.285 | +3.53% | +0.84% | 1.86x | 15.1 | 2026-11-20T08:20:38.659566+00:00 | Not calibrated | STRONG 71/100 | HIGH 66/100 | Watch | WATCH |
| 4 | ENA/USD | 0.1053 | 60.955 | 45.955 | +0.48% | +0.00% | 16.05x | 9.5 | 2026-11-20T08:20:38.659566+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 5 | XRP/USD | 0.96414 | 58.953 | 58.154 | +0.51% | +0.02% | 1.07x | 0.8 | 2026-11-20T08:20:38.659566+00:00 | Not calibrated | MODERATE 54/100 | HIGH 62/100 | Watch | WATCH |
| 6 | PROS/USD | 0.5755 | 58.090 | 60.257 | +6.83% | -1.57% | 1.57x | 31.2 | 2026-11-20T08:20:38.659566+00:00 | Not calibrated | WEAK 39/100 | EXTREME 89/100 | Do nothing | WATCH |
| 7 | XLM/USD | 0.13378 | 56.886 | 58.678 | +0.81% | -0.08% | 0.86x | 4.0 | 2026-11-20T08:20:38.659566+00:00 | Not calibrated | WEAK 33/100 | HIGH 68/100 | Do nothing | WATCH |
| 8 | CC/USD | 0.08065 | 30.071 | 33.533 | +0.31% | +0.54% | 0.39x | 6.2 | 2026-11-20T08:20:38.659566+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | STRK/USD | 0.03188 | 26.884 | 33.703 | +0.60% | -0.93% | 0.79x | 9.4 | 2026-11-20T08:20:38.659566+00:00 | Not calibrated | WEAK 18/100 | VERY_HIGH 73/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 72.978 | 0.4556 | +0.07% | 0.47x |
| 2 | PROS/USD | 60.257 | 0.5755 | -1.57% | 1.57x |
| 3 | SKR/USD | 59.252 | 0.010563 | +0.74% | 1.44x |
| 4 | XLM/USD | 58.678 | 0.13378 | -0.08% | 0.86x |
| 5 | XRP/USD | 58.154 | 0.96414 | +0.02% | 1.07x |
| 6 | SYRUP/USD | 49.285 | 0.09963 | +0.84% | 1.86x |
| 7 | ENA/USD | 45.955 | 0.1053 | +0.00% | 16.05x |
| 8 | STRK/USD | 33.703 | 0.03188 | -0.93% | 0.79x |
| 9 | CC/USD | 33.533 | 0.08065 | +0.54% | 0.39x |

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

- Persisted scans: 953; predictions: 8094; observations: 575837.
- Matured sampled outcomes across 1/6/24/48h: 9592; gap abstentions: 17479. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44701626799 · **Generation:** 953 · **Legacy run:** 44701626799
**Main quote time:** 2026-11-20T08:20:44.602772+00:00 · **Legacy report time:** 2026-11-20T08:21:42.488719+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD | 0.4556 | 68.03 | +0.07% | 0.47x | WEAK 44/100 | VERY_HIGH 82/100 | Watch |
| 2 | SKR/USD ⭐ | 0.010563 | 67.35 | +0.74% | 1.44x | STRONG 84/100 | VERY_HIGH 73/100 | Watch |
| 3 | SYRUP/USD ⭐ | 0.09963 | 62.11 | +0.84% | 1.86x | STRONG 81/100 | HIGH 66/100 | Consider small entry |
| 4 | ENA/USD | 0.1053 | 60.95 | +0.00% | 16.05x | STRONG 75/100 | HIGH 55/100 | Watch |
| 5 | XRP/USD | 0.96414 | 58.95 | +0.02% | 1.07x | MODERATE 54/100 | HIGH 62/100 | Watch |
| 6 | PROS/USD | 0.5755 | 58.09 | -1.57% | 1.57x | WEAK 39/100 | EXTREME 89/100 | Do nothing |
| 7 | XLM/USD | 0.13378 | 56.89 | -0.08% | 0.86x | WEAK 33/100 | HIGH 68/100 | Do nothing |
| 8 | CC/USD | 0.08065 | 30.07 | +0.54% | 0.39x | MODERATE 45/100 | VERY_HIGH 75/100 | Watch |
| 9 | STRK/USD | 0.03188 | 26.88 | -0.93% | 0.79x | WEAK 18/100 | VERY_HIGH 73/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.09945 | 69.39 | +0.84% | 1.86x | 2768 | STRONG 85/100 | HIGH 66/100 | Consider small entry |
| 2 | SKR/USD ⭐ | 0.010498 | 67.00 | +0.74% | 1.44x | 1709 | STRONG 78/100 | VERY_HIGH 79/100 | Watch |

**Same-run overlap:** SKR/USD, SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
