# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-24T02:31:44.841193+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45312762764
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9a4300807301d1954663f555716a9d5e9006b6a7 (atomic ledger/results publication)
**Ledger generation:** 1513 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | MON/USD | 0.01206 | 87.688 | 62.553 | +4.69% | +2.03% | 3.51x | 16.6 | 2026-11-24T02:31:36.481576+00:00 | Not calibrated | STRONG 94/100 | HIGH 61/100 | Consider small entry | WATCH |
| 2 | LINK/USD | 9.03847 | 68.345 | 54.690 | +0.37% | -0.27% | 3.76x | 5.8 | 2026-11-24T02:31:36.481576+00:00 | Not calibrated | MODERATE 64/100 | HIGH 61/100 | Watch | WATCH |
| 3 | AI/USD | 0.01617 | 63.667 | 68.173 | +6.17% | +0.00% | 0.55x | 12.4 | 2026-11-24T02:31:36.481576+00:00 | Not calibrated | MODERATE 47/100 | EXTREME 88/100 | Do nothing | WATCH |
| 4 | ADA/USD | 0.148899 | 63.521 | 54.176 | +0.30% | -0.06% | 1.96x | 5.9 | 2026-11-24T02:31:36.481576+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 5 | NIGHT/USD | 0.04858 | 62.723 | 50.997 | +0.89% | -0.65% | 7.02x | 10.3 | 2026-11-24T02:31:36.481576+00:00 | Not calibrated | MODERATE 56/100 | HIGH 67/100 | Watch | WATCH |
| 6 | XRP/USD | 0.9434 | 58.233 | 57.829 | +0.43% | -0.23% | 1.15x | 0.3 | 2026-11-24T02:31:36.481576+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 7 | PEPE/USD | 3.454e-06 | 54.186 | 52.264 | +0.94% | -0.06% | 1.22x | 5.8 | 2026-11-24T02:31:36.481576+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 8 | XLM/USD | 0.13059 | 54.028 | 54.301 | +0.46% | -0.62% | 1.28x | 7.8 | 2026-11-24T02:31:36.481576+00:00 | Not calibrated | WEAK 37/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XDG/USD | 0.0565333 | 52.804 | 55.076 | +0.41% | -0.36% | 0.95x | 5.5 | 2026-11-24T02:31:36.481576+00:00 | Not calibrated | WEAK 31/100 | HIGH 68/100 | Do nothing | WATCH |
| 10 | XDC/USD | 0.02611 | 50.712 | 34.944 | +0.50% | +0.15% | 3.70x | 7.7 | 2026-11-24T02:31:36.481576+00:00 | Not calibrated | STRONG 70/100 | HIGH 60/100 | Watch | WATCH |
| 11 | PENGU/USD | 0.00444 | 49.970 | 35.982 | +0.38% | -0.20% | 3.66x | 4.5 | 2026-11-24T02:31:36.481576+00:00 | Not calibrated | MODERATE 55/100 | HIGH 66/100 | Watch | WATCH |
| 12 | AAVE/USD | 97.97 | 46.192 | 50.146 | +0.95% | +0.11% | 0.55x | 7.2 | 2026-11-24T02:31:36.481576+00:00 | Not calibrated | WEAK 43/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | AI/USD | 68.173 | 0.01617 | +0.00% | 0.55x |
| 2 | MON/USD | 62.553 | 0.01206 | +2.03% | 3.51x |
| 3 | XRP/USD | 57.829 | 0.9434 | -0.23% | 1.15x |
| 4 | XDG/USD | 55.076 | 0.0565333 | -0.36% | 0.95x |
| 5 | LINK/USD | 54.690 | 9.03847 | -0.27% | 3.76x |
| 6 | XLM/USD | 54.301 | 0.13059 | -0.62% | 1.28x |
| 7 | ADA/USD | 54.176 | 0.148899 | -0.06% | 1.96x |
| 8 | PEPE/USD | 52.264 | 3.454e-06 | -0.06% | 1.22x |
| 9 | NIGHT/USD | 50.997 | 0.04858 | -0.65% | 7.02x |
| 10 | AAVE/USD | 50.146 | 97.97 | +0.11% | 0.55x |
| 11 | PENGU/USD | 35.982 | 0.00444 | -0.20% | 3.66x |
| 12 | XDC/USD | 34.944 | 0.02611 | +0.15% | 3.70x |

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

- Persisted scans: 1513; predictions: 12913; observations: 916518.
- Matured sampled outcomes across 1/6/24/48h: 23874; gap abstentions: 22370. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 135 (sampled only; not a success-rate estimate).
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

**Writer:** 45312762764 · **Generation:** 1513 · **Legacy run:** 45312762764
**Main quote time:** 2026-11-24T02:31:44.841193+00:00 · **Legacy report time:** 2026-11-24T02:32:55.913274+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01206 | 87.69 | +2.03% | 3.51x | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 2 | LINK/USD | 9.03847 | 68.35 | -0.27% | 3.76x | MODERATE 64/100 | HIGH 61/100 | Watch |
| 3 | AI/USD | 0.01617 | 63.67 | +0.00% | 0.55x | MODERATE 47/100 | EXTREME 88/100 | Do nothing |
| 4 | ADA/USD | 0.148899 | 63.52 | -0.06% | 1.96x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 5 | NIGHT/USD | 0.04858 | 62.72 | -0.65% | 7.02x | MODERATE 56/100 | HIGH 67/100 | Watch |
| 6 | XRP/USD | 0.9434 | 58.23 | -0.23% | 1.15x | WEAK 39/100 | HIGH 68/100 | Watch |
| 7 | PEPE/USD | 3.454e-06 | 54.19 | -0.06% | 1.22x | WEAK 37/100 | HIGH 68/100 | Watch |
| 8 | XLM/USD | 0.13059 | 54.03 | -0.62% | 1.28x | WEAK 37/100 | HIGH 61/100 | Watch |
| 9 | XDG/USD | 0.0565333 | 52.80 | -0.36% | 0.95x | WEAK 31/100 | HIGH 68/100 | Do nothing |
| 10 | XDC/USD | 0.02611 | 50.71 | +0.15% | 3.70x | STRONG 70/100 | HIGH 60/100 | Watch |
| 11 | PENGU/USD | 0.00444 | 49.97 | -0.20% | 3.66x | MODERATE 55/100 | HIGH 66/100 | Watch |
| 12 | AAVE/USD | 97.97 | 46.19 | +0.11% | 0.55x | WEAK 43/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | MON/USD ⭐ | 0.01207 | 88.92 | +2.03% | 3.51x | 7045 | STRONG 100/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** MON/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
