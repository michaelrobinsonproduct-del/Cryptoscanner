# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T15:20:18.739909+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44334320306
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 1988e4229a8ddb16952e86ba419764b99bc6dbab (atomic ledger/results publication)
**Ledger generation:** 599 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | INFI/USD | 0.141 | 91.410 | 69.525 | +11.02% | +7.22% | 0.69x | 14.2 | 2026-11-18T15:20:11.471584+00:00 | Not calibrated | STRONG 71/100 | EXTREME 98/100 | Do nothing | WATCH |
| 2 | SENT/USD | 0.019703 | 67.889 | 65.775 | +5.54% | +0.70% | 0.86x | 8.1 | 2026-11-18T15:20:11.471584+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 74/100 | Watch | WATCH |
| 3 | STABLE/USD | 0.02303 | 67.787 | 62.958 | +9.41% | -0.65% | 1.81x | 26.1 | 2026-11-18T15:20:11.471584+00:00 | Not calibrated | WEAK 44/100 | EXTREME 85/100 | Do nothing | WATCH |
| 4 | CT/USD | 0.123 | 60.295 | 63.786 | +8.85% | +0.16% | 0.57x | 24.4 | 2026-11-18T15:20:11.471584+00:00 | Not calibrated | WEAK 40/100 | EXTREME 94/100 | Do nothing | WATCH |
| 5 | TRX/USD | 0.310085 | 55.931 | 45.941 | +0.71% | +0.04% | 1.98x | 0.0 | 2026-11-18T15:20:11.471584+00:00 | Not calibrated | MODERATE 63/100 | HIGH 55/100 | Watch | WATCH |
| 6 | RE/USD | 0.24007 | 52.552 | 44.997 | +3.33% | -0.58% | 2.05x | 17.9 | 2026-11-18T15:20:11.471584+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 7 | NIGHT/USD | 0.04534 | 50.728 | 50.669 | +1.00% | +0.44% | 0.78x | 8.8 | 2026-11-18T15:20:11.471584+00:00 | Not calibrated | MODERATE 55/100 | HIGH 62/100 | Watch | WATCH |
| 8 | MNT/USD | 0.386 | 46.513 | 52.912 | +3.40% | -0.08% | 0.40x | 7.8 | 2026-11-18T15:20:11.471584+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing | WATCH |
| 9 | AKT/USD | 0.5139 | 44.670 | 35.764 | +0.90% | -0.54% | 2.16x | 5.8 | 2026-11-18T15:20:11.471584+00:00 | Not calibrated | MODERATE 52/100 | HIGH 66/100 | Watch | WATCH |
| 10 | CC/USD | 0.08289 | 38.541 | 40.346 | +0.93% | +0.00% | 0.82x | 3.6 | 2026-11-18T15:20:11.471584+00:00 | Not calibrated | WEAK 39/100 | HIGH 67/100 | Watch | WATCH |
| 11 | AKE/USD | 0.01043682 | 36.546 | 45.926 | +4.53% | -1.21% | 0.67x | 38.7 | 2026-11-18T15:20:11.471584+00:00 | Not calibrated | WEAK 8/100 | EXTREME 97/100 | Do nothing | WATCH |
| 12 | ME/USD | 0.0392 | 31.924 | 29.584 | +1.55% | +0.26% | 1.11x | 25.5 | 2026-11-18T15:20:11.471584+00:00 | Not calibrated | WEAK 41/100 | EXTREME 86/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | INFI/USD | 69.525 | 0.141 | +7.22% | 0.69x |
| 2 | SENT/USD | 65.775 | 0.019703 | +0.70% | 0.86x |
| 3 | CT/USD | 63.786 | 0.123 | +0.16% | 0.57x |
| 4 | STABLE/USD | 62.958 | 0.02303 | -0.65% | 1.81x |
| 5 | MNT/USD | 52.912 | 0.386 | -0.08% | 0.40x |
| 6 | NIGHT/USD | 50.669 | 0.04534 | +0.44% | 0.78x |
| 7 | TRX/USD | 45.941 | 0.310085 | +0.04% | 1.98x |
| 8 | AKE/USD | 45.926 | 0.01043682 | -1.21% | 0.67x |
| 9 | RE/USD | 44.997 | 0.24007 | -0.58% | 2.05x |
| 10 | CC/USD | 40.346 | 0.08289 | +0.00% | 0.82x |
| 11 | AKT/USD | 35.764 | 0.5139 | -0.54% | 2.16x |
| 12 | ME/USD | 29.584 | 0.0392 | +0.26% | 1.11x |

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

- Persisted scans: 599; predictions: 5124; observations: 361798.
- Matured sampled outcomes across 1/6/24/48h: 4336; gap abstentions: 13125. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
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

**Writer:** 44334320306 · **Generation:** 599 · **Legacy run:** 44334320306
**Main quote time:** 2026-11-18T15:20:18.739909+00:00 · **Legacy report time:** 2026-11-18T15:20:41.467419+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | INFI/USD | 0.141 | 91.41 | +7.22% | 0.69x | STRONG 71/100 | EXTREME 98/100 | Do nothing |
| 2 | SENT/USD | 0.019703 | 67.89 | +0.70% | 0.86x | MODERATE 64/100 | VERY_HIGH 74/100 | Watch |
| 3 | STABLE/USD | 0.02303 | 67.79 | -0.65% | 1.81x | WEAK 44/100 | EXTREME 85/100 | Do nothing |
| 4 | CT/USD | 0.123 | 60.30 | +0.16% | 0.57x | WEAK 40/100 | EXTREME 94/100 | Do nothing |
| 5 | TRX/USD | 0.310085 | 55.93 | +0.04% | 1.98x | MODERATE 63/100 | HIGH 55/100 | Watch |
| 6 | RE/USD | 0.24007 | 52.55 | -0.58% | 2.05x | MODERATE 51/100 | VERY_HIGH 79/100 | Watch |
| 7 | NIGHT/USD | 0.04534 | 50.73 | +0.44% | 0.78x | MODERATE 55/100 | HIGH 62/100 | Watch |
| 8 | MNT/USD | 0.386 | 46.51 | -0.08% | 0.40x | WEAK 28/100 | VERY_HIGH 81/100 | Do nothing |
| 9 | AKT/USD | 0.5139 | 44.67 | -0.54% | 2.16x | MODERATE 52/100 | HIGH 66/100 | Watch |
| 10 | CC/USD | 0.08289 | 38.54 | +0.00% | 0.82x | WEAK 39/100 | HIGH 67/100 | Watch |
| 11 | AKE/USD | 0.01043682 | 36.55 | -1.21% | 0.67x | WEAK 8/100 | EXTREME 97/100 | Do nothing |
| 12 | ME/USD | 0.0392 | 31.92 | +0.26% | 1.11x | WEAK 41/100 | EXTREME 86/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| — | No confirmed WATCH signals | — | — | — | — | — | — | — | — |

**Same-run overlap:** None
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
