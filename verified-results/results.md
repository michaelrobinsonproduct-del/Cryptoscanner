# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-20T08:10:41.299171+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44700323339
**Source SHA:** bdc7e68f7fa75fae6636b7738d52f10a65d92038
**Previous ledger commit:** cce67101c286a89b7c6e78c4177a8a52e88af0f1 (atomic ledger/results publication)
**Ledger generation:** 952 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 605; OHLC screened: 20.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XLM/USD | 0.13406 | 72.790 | 60.198 | +1.02% | -0.13% | 2.32x | 4.0 | 2026-11-20T08:10:35.639291+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ICNT/USD | 0.4559 | 68.736 | 66.430 | +6.99% | +1.83% | 0.32x | 35.2 | 2026-11-20T08:10:35.639291+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 3 | PROS/USD | 0.5903 | 57.735 | 62.257 | +9.58% | -1.24% | 1.17x | 27.2 | 2026-11-20T08:10:35.639291+00:00 | Not calibrated | WEAK 29/100 | EXTREME 96/100 | Do nothing | WATCH |
| 4 | SKR/USD | 0.010484 | 56.302 | 49.387 | +4.36% | +1.35% | 1.01x | 24.8 | 2026-11-20T08:10:35.639291+00:00 | Not calibrated | MODERATE 53/100 | EXTREME 86/100 | Do nothing | WATCH |
| 5 | SYRUP/USD | 0.09961 | 53.514 | 48.696 | +3.51% | -0.29% | 1.63x | 16.0 | 2026-11-20T08:10:35.639291+00:00 | Not calibrated | WEAK 42/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 6 | XRP/USD | 0.96544 | 52.590 | 59.000 | +0.65% | +0.17% | 0.27x | 1.0 | 2026-11-20T08:10:35.639291+00:00 | Not calibrated | MODERATE 46/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | STRK/USD | 0.03188 | 46.233 | 32.170 | +0.60% | -0.19% | 8.86x | 12.6 | 2026-11-20T08:10:35.639291+00:00 | Not calibrated | MODERATE 48/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 8 | ENA/USD | 0.1057 | 43.873 | 43.483 | +0.86% | +0.28% | 0.90x | 18.9 | 2026-11-20T08:10:35.639291+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 9 | CC/USD | 0.08078 | 33.607 | 34.674 | +0.47% | +1.04% | 0.37x | 6.2 | 2026-11-20T08:10:35.639291+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 10 | ATOM/USD | 1.2693 | 30.648 | 34.143 | +0.62% | +0.15% | 0.58x | 5.5 | 2026-11-20T08:10:35.639291+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 66.430 | 0.4559 | +1.83% | 0.32x |
| 2 | PROS/USD | 62.257 | 0.5903 | -1.24% | 1.17x |
| 3 | XLM/USD | 60.198 | 0.13406 | -0.13% | 2.32x |
| 4 | XRP/USD | 59.000 | 0.96544 | +0.17% | 0.27x |
| 5 | SKR/USD | 49.387 | 0.010484 | +1.35% | 1.01x |
| 6 | SYRUP/USD | 48.696 | 0.09961 | -0.29% | 1.63x |
| 7 | ENA/USD | 43.483 | 0.1057 | +0.28% | 0.90x |
| 8 | CC/USD | 34.674 | 0.08078 | +1.04% | 0.37x |
| 9 | ATOM/USD | 34.143 | 1.2693 | +0.15% | 0.58x |
| 10 | STRK/USD | 32.170 | 0.03188 | -0.19% | 8.86x |

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

- Persisted scans: 952; predictions: 8085; observations: 575231.
- Matured sampled outcomes across 1/6/24/48h: 9573; gap abstentions: 17471. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44700323339 · **Generation:** 952 · **Legacy run:** 44700323339
**Main quote time:** 2026-11-20T08:10:41.299171+00:00 · **Legacy report time:** 2026-11-20T08:11:38.169457+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XLM/USD | 0.13406 | 72.79 | -0.13% | 2.32x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 2 | ICNT/USD | 0.4559 | 68.74 | +1.83% | 0.32x | MODERATE 49/100 | VERY_HIGH 82/100 | Watch |
| 3 | PROS/USD | 0.5903 | 57.73 | -1.24% | 1.17x | WEAK 29/100 | EXTREME 96/100 | Do nothing |
| 4 | SKR/USD ⭐ | 0.010484 | 56.30 | +1.35% | 1.01x | MODERATE 63/100 | EXTREME 86/100 | Do nothing |
| 5 | SYRUP/USD | 0.09961 | 53.51 | -0.29% | 1.63x | WEAK 42/100 | VERY_HIGH 72/100 | Watch |
| 6 | XRP/USD | 0.96544 | 52.59 | +0.17% | 0.27x | MODERATE 46/100 | VERY_HIGH 70/100 | Watch |
| 7 | STRK/USD | 0.03188 | 46.23 | -0.19% | 8.86x | MODERATE 48/100 | VERY_HIGH 72/100 | Watch |
| 8 | ENA/USD | 0.1057 | 43.87 | +0.28% | 0.90x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 9 | CC/USD | 0.08078 | 33.61 | +1.04% | 0.37x | MODERATE 47/100 | VERY_HIGH 75/100 | Watch |
| 10 | ATOM/USD | 1.2693 | 30.65 | +0.15% | 0.58x | WEAK 35/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKR/USD ⭐ | 0.010477 | 66.90 | +1.35% | 1.01x | 1681 | MODERATE 68/100 | EXTREME 86/100 | Do nothing |
| 2 | ETH/USD | 1757.23 | 58.20 | +0.32% | 2.02x | 67548 | STRONG 84/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SKR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
