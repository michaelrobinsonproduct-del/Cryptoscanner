# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T05:56:01.975640+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45764623687
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 92420a88dd405e882214dc0610747ad306b3c309 (atomic ledger/results publication)
**Ledger generation:** 1821 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ADA/USD | 0.149018 | 83.186 | 68.819 | +2.23% | -0.13% | 7.45x | 3.6 | 2026-11-26T05:55:56.039707+00:00 | Not calibrated | STRONG 72/100 | HIGH 61/100 | Watch | WATCH |
| 2 | SYRUP/USD | 0.07065 | 81.081 | 65.797 | +6.61% | +0.06% | 2.99x | 22.7 | 2026-11-26T05:55:56.039707+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 3 | LTC/USD | 43.47 | 80.732 | 66.306 | +1.78% | -0.11% | 3.41x | 2.3 | 2026-11-26T05:55:56.039707+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 4 | QNT/USD | 147.21 | 78.765 | 60.858 | +1.66% | +0.82% | 2.38x | 0.7 | 2026-11-26T05:55:56.039707+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | PIEVERSE/USD | 3.8981 | 70.843 | 66.838 | +10.09% | +2.10% | 0.35x | 30.8 | 2026-11-26T05:55:56.039707+00:00 | Not calibrated | MODERATE 55/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 6 | LINK/USD | 9.21 | 70.604 | 64.781 | +1.83% | -0.27% | 1.72x | 1.5 | 2026-11-26T05:55:56.039707+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 7 | XRP/USD | 0.9584 | 69.758 | 71.271 | +2.33% | -0.21% | 0.95x | 0.1 | 2026-11-26T05:55:56.039707+00:00 | Not calibrated | WEAK 40/100 | HIGH 68/100 | Watch | WATCH |
| 8 | HBAR/USD | 0.05356 | 69.115 | 55.790 | +2.80% | -0.33% | 5.55x | 1.9 | 2026-11-26T05:55:56.039707+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 9 | XDG/USD | 0.0566653 | 63.170 | 58.960 | +1.26% | -0.13% | 1.48x | 0.4 | 2026-11-26T05:55:56.039707+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 10 | TAO/USD | 184.0012 | 62.373 | 60.661 | +1.33% | +0.02% | 1.16x | 7.2 | 2026-11-26T05:55:56.039707+00:00 | Not calibrated | MODERATE 56/100 | HIGH 62/100 | Watch | WATCH |
| 11 | AVAX/USD | 6.691 | 62.123 | 50.666 | +1.06% | -0.13% | 2.21x | 1.5 | 2026-11-26T05:55:56.039707+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 12 | SOL/USD | 70.93 | 58.157 | 59.665 | +0.77% | -0.21% | 0.95x | 1.4 | 2026-11-26T05:55:56.039707+00:00 | Not calibrated | WEAK 34/100 | HIGH 68/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XRP/USD | 71.271 | 0.9584 | -0.21% | 0.95x |
| 2 | ADA/USD | 68.819 | 0.149018 | -0.13% | 7.45x |
| 3 | PIEVERSE/USD | 66.838 | 3.8981 | +2.10% | 0.35x |
| 4 | LTC/USD | 66.306 | 43.47 | -0.11% | 3.41x |
| 5 | SYRUP/USD | 65.797 | 0.07065 | +0.06% | 2.99x |
| 6 | LINK/USD | 64.781 | 9.21 | -0.27% | 1.72x |
| 7 | QNT/USD | 60.858 | 147.21 | +0.82% | 2.38x |
| 8 | TAO/USD | 60.661 | 184.0012 | +0.02% | 1.16x |
| 9 | SOL/USD | 59.665 | 70.93 | -0.21% | 0.95x |
| 10 | XDG/USD | 58.960 | 0.0566653 | -0.13% | 1.48x |
| 11 | HBAR/USD | 55.790 | 0.05356 | -0.33% | 5.55x |
| 12 | AVAX/USD | 50.666 | 6.691 | -0.13% | 2.21x |

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

- Persisted scans: 1821; predictions: 15587; observations: 1104033.
- Matured sampled outcomes across 1/6/24/48h: 33815; gap abstentions: 24011. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 8; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45764623687 · **Generation:** 1821 · **Legacy run:** 45764623687
**Main quote time:** 2026-11-26T05:56:01.975640+00:00 · **Legacy report time:** 2026-11-26T05:57:05.899562+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD | 0.149018 | 83.19 | -0.13% | 7.45x | STRONG 72/100 | HIGH 61/100 | Watch |
| 2 | SYRUP/USD ⭐ | 0.07065 | 81.08 | +0.06% | 2.99x | STRONG 86/100 | VERY_HIGH 72/100 | Watch |
| 3 | LTC/USD | 43.47 | 80.73 | -0.11% | 3.41x | STRONG 70/100 | HIGH 61/100 | Watch |
| 4 | QNT/USD | 147.21 | 78.77 | +0.82% | 2.38x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 5 | PIEVERSE/USD | 3.8981 | 70.84 | +2.10% | 0.35x | MODERATE 55/100 | VERY_HIGH 82/100 | Watch |
| 6 | LINK/USD | 9.21 | 70.60 | -0.27% | 1.72x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 7 | XRP/USD | 0.9584 | 69.76 | -0.21% | 0.95x | WEAK 40/100 | HIGH 68/100 | Watch |
| 8 | HBAR/USD | 0.05356 | 69.12 | -0.33% | 5.55x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 9 | XDG/USD | 0.0566653 | 63.17 | -0.13% | 1.48x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 10 | TAO/USD | 184.0012 | 62.37 | +0.02% | 1.16x | MODERATE 56/100 | HIGH 62/100 | Watch |
| 11 | AVAX/USD | 6.691 | 62.12 | -0.13% | 2.21x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 12 | SOL/USD | 70.93 | 58.16 | -0.21% | 0.95x | WEAK 34/100 | HIGH 68/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SYRUP/USD ⭐ | 0.07065 | 79.42 | +0.06% | 2.99x | 3661 | STRONG 90/100 | HIGH 66/100 | Watch |

**Same-run overlap:** SYRUP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
