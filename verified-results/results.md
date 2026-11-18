# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-18T07:05:08.794310+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44256053365
**Source SHA:** 394c17eeb7071fba40e02dbbb1ea97cedb3a0a8a
**Previous ledger commit:** e92b3b2cd80a8216b03fec1b6fe5a1e098de77ac (atomic ledger/results publication)
**Ledger generation:** 562 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 22.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ICNT/USD | 0.2977 | 82.235 | 77.275 | +7.82% | -2.01% | 3.85x | 3.4 | 2026-11-18T07:05:03.061171+00:00 | Not calibrated | STRONG 71/100 | VERY_HIGH 70/100 | Do nothing | WATCH |
| 2 | XRP/USD | 0.98696 | 69.048 | 57.498 | +0.45% | +0.33% | 1.99x | 1.3 | 2026-11-18T07:05:03.061171+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 3 | TRX/USD | 0.309156 | 53.513 | 43.358 | +0.41% | +0.10% | 1.97x | 0.0 | 2026-11-18T07:05:03.061171+00:00 | Not calibrated | MODERATE 62/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SENT/USD | 0.019515 | 52.188 | 56.251 | +4.53% | -0.08% | 0.63x | 12.8 | 2026-11-18T07:05:03.061171+00:00 | Not calibrated | WEAK 26/100 | EXTREME 94/100 | Do nothing | WATCH |
| 5 | AKE/USD | 0.0103764 | 51.359 | 46.424 | +3.93% | +2.51% | 0.24x | 31.3 | 2026-11-18T07:05:03.061171+00:00 | Not calibrated | MODERATE 46/100 | EXTREME 87/100 | Do nothing | WATCH |
| 6 | XDC/USD | 0.03093 | 41.057 | 47.752 | +2.01% | -0.06% | 0.36x | 9.7 | 2026-11-18T07:05:03.061171+00:00 | Not calibrated | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing | WATCH |
| 7 | AKT/USD | 0.5149 | 40.567 | 39.125 | +1.10% | -0.12% | 1.20x | 1.9 | 2026-11-18T07:05:03.061171+00:00 | Not calibrated | WEAK 30/100 | VERY_HIGH 73/100 | Do nothing | WATCH |
| 8 | MNT/USD | 0.3776 | 36.590 | 29.005 | +1.15% | -0.11% | 1.81x | 23.8 | 2026-11-18T07:05:03.061171+00:00 | Not calibrated | WEAK 28/100 | VERY_HIGH 78/100 | Do nothing | WATCH |
| 9 | TRUST/USD | 0.04775 | 30.881 | 33.796 | +1.27% | +0.36% | 0.53x | 16.8 | 2026-11-18T07:05:03.061171+00:00 | Not calibrated | WEAK 40/100 | VERY_HIGH 81/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | ICNT/USD | 77.275 | 0.2977 | -2.01% | 3.85x |
| 2 | XRP/USD | 57.498 | 0.98696 | +0.33% | 1.99x |
| 3 | SENT/USD | 56.251 | 0.019515 | -0.08% | 0.63x |
| 4 | XDC/USD | 47.752 | 0.03093 | -0.06% | 0.36x |
| 5 | AKE/USD | 46.424 | 0.0103764 | +2.51% | 0.24x |
| 6 | TRX/USD | 43.358 | 0.309156 | +0.10% | 1.97x |
| 7 | AKT/USD | 39.125 | 0.5149 | -0.12% | 1.20x |
| 8 | TRUST/USD | 33.796 | 0.04775 | +0.36% | 0.53x |
| 9 | MNT/USD | 29.005 | 0.3776 | -0.11% | 1.81x |

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

- Persisted scans: 562; predictions: 4738; observations: 339265.
- Matured sampled outcomes across 1/6/24/48h: 4064; gap abstentions: 12463. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 0 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 13; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44256053365 · **Generation:** 562 · **Legacy run:** 44256053365
**Main quote time:** 2026-11-18T07:05:08.794310+00:00 · **Legacy report time:** 2026-11-18T07:05:31.890862+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ICNT/USD | 0.2977 | 82.24 | -2.01% | 3.85x | STRONG 71/100 | VERY_HIGH 70/100 | Do nothing |
| 2 | XRP/USD ⭐ | 0.98696 | 69.05 | +0.33% | 1.99x | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 3 | TRX/USD ⭐ | 0.309156 | 53.51 | +0.10% | 1.97x | STRONG 72/100 | HIGH 55/100 | Watch |
| 4 | SENT/USD | 0.019515 | 52.19 | -0.08% | 0.63x | WEAK 26/100 | EXTREME 94/100 | Do nothing |
| 5 | AKE/USD | 0.0103764 | 51.36 | +2.51% | 0.24x | MODERATE 46/100 | EXTREME 87/100 | Do nothing |
| 6 | XDC/USD | 0.03093 | 41.06 | -0.06% | 0.36x | WEAK 26/100 | VERY_HIGH 76/100 | Do nothing |
| 7 | AKT/USD | 0.5149 | 40.57 | -0.12% | 1.20x | WEAK 30/100 | VERY_HIGH 73/100 | Do nothing |
| 8 | MNT/USD | 0.3776 | 36.59 | -0.11% | 1.81x | WEAK 28/100 | VERY_HIGH 78/100 | Do nothing |
| 9 | TRUST/USD | 0.04775 | 30.88 | +0.36% | 0.53x | WEAK 40/100 | VERY_HIGH 81/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.98689 | 62.07 | +0.33% | 1.99x | 32037 | STRONG 86/100 | HIGH 55/100 | Consider small entry |
| 2 | TRX/USD ⭐ | 0.309156 | 52.30 | +0.10% | 1.97x | 4110 | STRONG 71/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XRP/USD, TRX/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
