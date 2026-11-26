# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T07:06:50.694690+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45772633644
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 9d8f763e9540aac6ed7f0a4305428ffbf14b14ca (atomic ledger/results publication)
**Ledger generation:** 1828 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XRP/USD | 0.94936 | 75.937 | 63.461 | +1.37% | -0.03% | 2.26x | 2.2 | 2026-11-26T07:06:42.680679+00:00 | Not calibrated | MODERATE 68/100 | HIGH 61/100 | Watch | WATCH |
| 2 | NEAR/USD | 3.0582 | 72.381 | 56.578 | +0.27% | +0.16% | 3.73x | 0.7 | 2026-11-26T07:06:42.680679+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XDG/USD | 0.0563204 | 68.795 | 53.768 | +0.65% | +0.01% | 2.79x | 2.8 | 2026-11-26T07:06:42.680679+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 4 | LINK/USD | 9.1515 | 67.860 | 60.927 | +1.18% | +0.12% | 1.63x | 3.6 | 2026-11-26T07:06:42.680679+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SYRUP/USD | 0.07096 | 67.236 | 67.940 | +7.08% | +0.77% | 0.55x | 18.4 | 2026-11-26T07:06:42.680679+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | XMR/USD | 526.92 | 64.871 | 58.720 | +1.93% | +0.66% | 1.29x | 19.6 | 2026-11-26T07:06:42.680679+00:00 | Not calibrated | MODERATE 62/100 | HIGH 61/100 | Watch | WATCH |
| 7 | ADA/USD | 0.147921 | 63.627 | 62.997 | +1.48% | +0.19% | 0.97x | 4.7 | 2026-11-26T07:06:42.680679+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 8 | LTC/USD | 43.3 | 60.693 | 63.515 | +1.38% | -0.05% | 0.74x | 2.3 | 2026-11-26T07:06:42.680679+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 9 | HBAR/USD | 0.053 | 58.955 | 48.195 | +1.73% | +0.36% | 1.90x | 1.9 | 2026-11-26T07:06:42.680679+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 10 | INJ/USD | 6.092 | 58.126 | 56.812 | +2.32% | -0.13% | 1.20x | 3.3 | 2026-11-26T07:06:42.680679+00:00 | Not calibrated | WEAK 39/100 | HIGH 68/100 | Watch | WATCH |
| 11 | QNT/USD | 147.92 | 57.051 | 62.554 | +2.15% | +0.59% | 0.15x | 4.7 | 2026-11-26T07:06:42.680679+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | SOL/USD | 70.68 | 54.981 | 57.176 | +0.41% | +0.09% | 0.74x | 1.4 | 2026-11-26T07:06:42.680679+00:00 | Not calibrated | MODERATE 47/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SYRUP/USD | 67.940 | 0.07096 | +0.77% | 0.55x |
| 2 | LTC/USD | 63.515 | 43.3 | -0.05% | 0.74x |
| 3 | XRP/USD | 63.461 | 0.94936 | -0.03% | 2.26x |
| 4 | ADA/USD | 62.997 | 0.147921 | +0.19% | 0.97x |
| 5 | QNT/USD | 62.554 | 147.92 | +0.59% | 0.15x |
| 6 | LINK/USD | 60.927 | 9.1515 | +0.12% | 1.63x |
| 7 | XMR/USD | 58.720 | 526.92 | +0.66% | 1.29x |
| 8 | SOL/USD | 57.176 | 70.68 | +0.09% | 0.74x |
| 9 | INJ/USD | 56.812 | 6.092 | -0.13% | 1.20x |
| 10 | NEAR/USD | 56.578 | 3.0582 | +0.16% | 3.73x |
| 11 | XDG/USD | 53.768 | 0.0563204 | +0.01% | 2.79x |
| 12 | HBAR/USD | 48.195 | 0.053 | +0.36% | 1.90x |

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

- Persisted scans: 1828; predictions: 15671; observations: 1108296.
- Matured sampled outcomes across 1/6/24/48h: 33974; gap abstentions: 24171. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45772633644 · **Generation:** 1828 · **Legacy run:** 45772633644
**Main quote time:** 2026-11-26T07:06:50.694690+00:00 · **Legacy report time:** 2026-11-26T07:08:08.499155+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD | 0.94936 | 75.94 | -0.03% | 2.26x | MODERATE 68/100 | HIGH 61/100 | Watch |
| 2 | NEAR/USD | 3.0582 | 72.38 | +0.16% | 3.73x | STRONG 81/100 | HIGH 55/100 | Watch |
| 3 | XDG/USD | 0.0563204 | 68.80 | +0.01% | 2.79x | STRONG 79/100 | HIGH 55/100 | Watch |
| 4 | LINK/USD ⭐ | 9.1515 | 67.86 | +0.12% | 1.63x | STRONG 79/100 | HIGH 55/100 | Watch |
| 5 | SYRUP/USD | 0.07096 | 67.24 | +0.77% | 0.55x | MODERATE 59/100 | VERY_HIGH 81/100 | Watch |
| 6 | XMR/USD ⭐ | 526.92 | 64.87 | +0.66% | 1.29x | STRONG 72/100 | HIGH 61/100 | Watch |
| 7 | ADA/USD | 0.147921 | 63.63 | +0.19% | 0.97x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 8 | LTC/USD | 43.3 | 60.69 | -0.05% | 0.74x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 9 | HBAR/USD | 0.053 | 58.95 | +0.36% | 1.90x | STRONG 74/100 | HIGH 55/100 | Watch |
| 10 | INJ/USD | 6.092 | 58.13 | -0.13% | 1.20x | WEAK 39/100 | HIGH 68/100 | Watch |
| 11 | QNT/USD | 147.92 | 57.05 | +0.59% | 0.15x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 12 | SOL/USD | 70.68 | 54.98 | +0.09% | 0.74x | MODERATE 47/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | LINK/USD ⭐ | 9.15939 | 66.30 | +0.12% | 1.63x | 9305 | STRONG 78/100 | HIGH 55/100 | Watch |
| 2 | XMR/USD ⭐ | 525.51 | 59.99 | +0.66% | 1.29x | 8252 | STRONG 75/100 | HIGH 55/100 | Watch |

**Same-run overlap:** LINK/USD, XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
