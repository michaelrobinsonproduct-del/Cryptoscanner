# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T01:00:26.181971+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44650196453
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** 07832db155b0e054c1fc19a4d8ce6c4b332110f1 (atomic ledger/results publication)
**Ledger generation:** 892 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 5s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 16.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XLM/USD | 0.133621 | 64.116 | 57.574 | +0.69% | +0.11% | 1.60x | 4.6 | 2026-11-20T01:00:21.528448+00:00 | Not calibrated | MODERATE 67/100 | HIGH 55/100 | Watch | WATCH |
| 2 | XRP/USD | 0.96174 | 57.965 | 56.089 | +0.26% | -0.02% | 1.20x | 1.5 | 2026-11-20T01:00:21.528448+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 3 | XMR/USD | 500.67 | 55.173 | 58.390 | +0.64% | -0.08% | 0.72x | 2.2 | 2026-11-20T01:00:21.528448+00:00 | Not calibrated | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 4 | HBAR/USD | 0.05393 | 53.005 | 38.283 | +0.32% | -0.06% | 4.07x | 1.9 | 2026-11-20T01:00:21.528448+00:00 | Not calibrated | MODERATE 57/100 | HIGH 61/100 | Watch | WATCH |
| 5 | SYRUP/USD | 0.09876 | 41.745 | 40.469 | +2.63% | +1.20% | 0.53x | 19.3 | 2026-11-20T01:00:21.528448+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | RARE/USD | 0.01376 | 37.377 | 43.095 | +3.77% | -1.00% | 0.93x | 29.1 | 2026-11-20T01:00:21.528448+00:00 | Not calibrated | WEAK 14/100 | EXTREME 96/100 | Do nothing | WATCH |
| 7 | BAT/USD | 0.08886 | 31.814 | 31.250 | +0.49% | +0.11% | 1.00x | 6.8 | 2026-11-20T01:00:21.528448+00:00 | Not calibrated | WEAK 41/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 8 | AKT/USD | 0.5349 | 25.065 | 31.904 | +0.26% | +0.22% | 0.20x | 5.6 | 2026-11-20T01:00:21.528448+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 9 | MEGA/USD | 0.05888 | 24.126 | 27.817 | +1.06% | -1.27% | 1.27x | 23.8 | 2026-11-20T01:00:21.528448+00:00 | Not calibrated | WEAK 12/100 | VERY_HIGH 82/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 58.390 | 500.67 | -0.08% | 0.72x |
| 2 | XLM/USD | 57.574 | 0.133621 | +0.11% | 1.60x |
| 3 | XRP/USD | 56.089 | 0.96174 | -0.02% | 1.20x |
| 4 | RARE/USD | 43.095 | 0.01376 | -1.00% | 0.93x |
| 5 | SYRUP/USD | 40.469 | 0.09876 | +1.20% | 0.53x |
| 6 | HBAR/USD | 38.283 | 0.05393 | -0.06% | 4.07x |
| 7 | AKT/USD | 31.904 | 0.5349 | +0.22% | 0.20x |
| 8 | BAT/USD | 31.250 | 0.08886 | +0.11% | 1.00x |
| 9 | MEGA/USD | 27.817 | 0.05888 | -1.27% | 1.27x |

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

- Persisted scans: 892; predictions: 7778; observations: 539001.
- Matured sampled outcomes across 1/6/24/48h: 8512; gap abstentions: 16134. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 44650196453 · **Generation:** 892 · **Legacy run:** 44650196453
**Main quote time:** 2026-11-20T01:00:26.181971+00:00 · **Legacy report time:** 2026-11-20T01:01:30.047799+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD ⭐ | 0.133621 | 64.12 | +0.11% | 1.60x | STRONG 77/100 | HIGH 55/100 | Watch |
| 2 | XRP/USD | 0.96174 | 57.96 | -0.02% | 1.20x | WEAK 39/100 | HIGH 68/100 | Watch |
| 3 | XMR/USD | 500.67 | 55.17 | -0.08% | 0.72x | WEAK 33/100 | VERY_HIGH 76/100 | Do nothing |
| 4 | HBAR/USD | 0.05393 | 53.00 | -0.06% | 4.07x | MODERATE 57/100 | HIGH 61/100 | Watch |
| 5 | SYRUP/USD | 0.09876 | 41.74 | +1.20% | 0.53x | MODERATE 46/100 | VERY_HIGH 81/100 | Watch |
| 6 | RARE/USD | 0.01376 | 37.38 | -1.00% | 0.93x | WEAK 14/100 | EXTREME 96/100 | Do nothing |
| 7 | BAT/USD ⭐ | 0.08886 | 31.81 | +0.11% | 1.00x | MODERATE 51/100 | VERY_HIGH 74/100 | Watch |
| 8 | AKT/USD | 0.5349 | 25.06 | +0.22% | 0.20x | WEAK 43/100 | VERY_HIGH 75/100 | Watch |
| 9 | MEGA/USD | 0.05888 | 24.13 | -1.27% | 1.27x | WEAK 12/100 | VERY_HIGH 82/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD ⭐ | 0.133621 | 56.01 | +0.11% | 1.60x | 10448 | STRONG 73/100 | HIGH 55/100 | Watch |
| 2 | BAT/USD ⭐ | 0.08866 | 22.66 | +0.11% | 1.00x | 2216 | WEAK 41/100 | VERY_HIGH 80/100 | Watch |

**Same-run overlap:** XLM/USD, BAT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
