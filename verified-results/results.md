# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T12:31:18.119273+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45820131148
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** f28f0a48b4efd230fda4ecc1828a8936cc38a893 (atomic ledger/results publication)
**Ledger generation:** 1861 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 588; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SKY/USD | 0.04645 | 93.738 | 76.152 | +10.91% | +0.52% | 3.50x | 6.5 | 2026-11-26T12:31:11.382699+00:00 | Not calibrated | STRONG 100/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | INJ/USD | 6.189 | 82.541 | 68.591 | +3.95% | -0.21% | 2.53x | 4.8 | 2026-11-26T12:31:11.382699+00:00 | Not calibrated | STRONG 71/100 | HIGH 61/100 | Watch | WATCH |
| 3 | LINK/USD | 9.20758 | 79.026 | 65.871 | +1.80% | -0.37% | 7.93x | 3.5 | 2026-11-26T12:31:11.382699+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 4 | ADA/USD | 0.148555 | 77.357 | 66.590 | +1.91% | -0.25% | 2.20x | 3.6 | 2026-11-26T12:31:11.382699+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 5 | XRP/USD | 0.94802 | 76.607 | 62.880 | +1.22% | -0.25% | 5.04x | 1.4 | 2026-11-26T12:31:11.382699+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 6 | ETH/USD | 1698.99 | 73.565 | 58.523 | +0.51% | +0.01% | 6.27x | 0.1 | 2026-11-26T12:31:11.382699+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 7 | SOL/USD | 70.64 | 71.142 | 56.778 | +0.36% | -0.13% | 10.63x | 1.4 | 2026-11-26T12:31:11.382699+00:00 | Not calibrated | MODERATE 66/100 | HIGH 61/100 | Watch | WATCH |
| 8 | SYRUP/USD | 0.0726 | 70.694 | 69.701 | +9.55% | +0.82% | 0.69x | 15.1 | 2026-11-26T12:31:11.382699+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 9 | NEAR/USD | 3.074 | 69.921 | 59.067 | +0.79% | +0.11% | 2.03x | 2.9 | 2026-11-26T12:31:11.382699+00:00 | Not calibrated | STRONG 80/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XBT/USD | 60527.7 | 69.757 | 56.837 | +0.26% | -0.06% | 2.32x | 0.0 | 2026-11-26T12:31:11.382699+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 11 | LTC/USD | 43.38 | 68.177 | 63.675 | +1.57% | -0.18% | 1.54x | 4.6 | 2026-11-26T12:31:11.382699+00:00 | Not calibrated | MODERATE 54/100 | HIGH 61/100 | Watch | WATCH |
| 12 | QNT/USD | 149.12 | 63.449 | 66.355 | +2.98% | +0.45% | 0.48x | 6.0 | 2026-11-26T12:31:11.382699+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 76.152 | 0.04645 | +0.52% | 3.50x |
| 2 | SYRUP/USD | 69.701 | 0.0726 | +0.82% | 0.69x |
| 3 | INJ/USD | 68.591 | 6.189 | -0.21% | 2.53x |
| 4 | ADA/USD | 66.590 | 0.148555 | -0.25% | 2.20x |
| 5 | QNT/USD | 66.355 | 149.12 | +0.45% | 0.48x |
| 6 | LINK/USD | 65.871 | 9.20758 | -0.37% | 7.93x |
| 7 | LTC/USD | 63.675 | 43.38 | -0.18% | 1.54x |
| 8 | XRP/USD | 62.880 | 0.94802 | -0.25% | 5.04x |
| 9 | NEAR/USD | 59.067 | 3.074 | +0.11% | 2.03x |
| 10 | ETH/USD | 58.523 | 1698.99 | +0.01% | 6.27x |
| 11 | XBT/USD | 56.837 | 60527.7 | -0.06% | 2.32x |
| 12 | SOL/USD | 56.778 | 70.64 | -0.13% | 10.63x |

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

- Persisted scans: 1861; predictions: 16067; observations: 1127949.
- Matured sampled outcomes across 1/6/24/48h: 34766; gap abstentions: 24745. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45820131148 · **Generation:** 1861 · **Legacy run:** 45820131148
**Main quote time:** 2026-11-26T12:31:18.119273+00:00 · **Legacy report time:** 2026-11-26T12:32:37.078811+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04645 | 93.74 | +0.52% | 3.50x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | INJ/USD | 6.189 | 82.54 | -0.21% | 2.53x | STRONG 71/100 | HIGH 61/100 | Watch |
| 3 | LINK/USD | 9.20758 | 79.03 | -0.37% | 7.93x | STRONG 70/100 | HIGH 61/100 | Watch |
| 4 | ADA/USD | 0.148555 | 77.36 | -0.25% | 2.20x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 5 | XRP/USD | 0.94802 | 76.61 | -0.25% | 5.04x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 6 | ETH/USD | 1698.99 | 73.56 | +0.01% | 6.27x | STRONG 82/100 | HIGH 55/100 | Watch |
| 7 | SOL/USD | 70.64 | 71.14 | -0.13% | 10.63x | MODERATE 66/100 | HIGH 61/100 | Watch |
| 8 | SYRUP/USD | 0.0726 | 70.69 | +0.82% | 0.69x | MODERATE 60/100 | VERY_HIGH 81/100 | Watch |
| 9 | NEAR/USD | 3.074 | 69.92 | +0.11% | 2.03x | STRONG 80/100 | HIGH 55/100 | Watch |
| 10 | XBT/USD | 60527.7 | 69.76 | -0.06% | 2.32x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 11 | LTC/USD | 43.38 | 68.18 | -0.18% | 1.54x | MODERATE 54/100 | HIGH 61/100 | Watch |
| 12 | QNT/USD | 149.12 | 63.45 | +0.45% | 0.48x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SKY/USD ⭐ | 0.04653 | 84.28 | +0.52% | 3.50x | 4847 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | SEI/USD | 0.03731 | 82.36 | +1.13% | 2.81x | 3132 | STRONG 96/100 | HIGH 60/100 | Consider small entry |

**Same-run overlap:** SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
