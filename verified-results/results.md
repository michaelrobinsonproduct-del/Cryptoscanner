# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-15T19:59:45.520650+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43755438923
**Source SHA:** 885b4a0465f5c74a8a87db5ca921c3c0a00021af
**Previous ledger commit:** 37ba413977fe4859a2a60e7bad763ca1c4186763 (atomic ledger/results publication)
**Ledger generation:** 441 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | QNT/USD | 156.03 | 112.946 | 96.475 | +8.88% | +0.29% | 6.64x | 7.1 | 2026-11-15T19:59:37.424319+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | UNI/USD | 5.1883 | 104.469 | 97.264 | +6.27% | +0.34% | 1.55x | 3.3 | 2026-11-15T19:59:37.424319+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | XMR/USD | 501.41 | 91.968 | 98.302 | +6.64% | +0.26% | 0.24x | 3.4 | 2026-11-15T19:59:37.424319+00:00 | Not calibrated | STRONG 76/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | XDG/USD | 0.0590176 | 91.561 | 75.783 | +2.97% | +0.16% | 3.58x | 0.0 | 2026-11-15T19:59:37.424319+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Watch | WATCH |
| 5 | NEAR/USD | 3.1724 | 91.294 | 86.587 | +4.74% | +0.61% | 1.16x | 3.2 | 2026-11-15T19:59:37.424319+00:00 | Not calibrated | STRONG 81/100 | HIGH 62/100 | Watch | WATCH |
| 6 | XRP/USD | 0.96083 | 88.902 | 90.991 | +5.15% | +0.28% | 0.65x | 0.1 | 2026-11-15T19:59:37.424319+00:00 | Not calibrated | STRONG 74/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | ADA/USD | 0.154798 | 86.822 | 87.824 | +4.84% | +0.34% | 0.73x | 2.1 | 2026-11-15T19:59:37.424319+00:00 | Not calibrated | STRONG 73/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | NIGHT/USD | 0.04954 | 86.124 | 82.807 | +4.40% | +0.28% | 1.19x | 6.1 | 2026-11-15T19:59:37.424319+00:00 | Not calibrated | STRONG 78/100 | HIGH 62/100 | Watch | WATCH |
| 9 | ASTER/USD | 0.54736 | 83.767 | 82.134 | +9.35% | -0.27% | 1.30x | 6.0 | 2026-11-15T19:59:37.424319+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 10 | CC/USD | 0.08329 | 83.374 | 88.058 | +7.32% | +0.26% | 0.40x | 3.6 | 2026-11-15T19:59:37.424319+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | HYPE/USD | 67.19 | 79.355 | 85.604 | +4.48% | +0.16% | 0.29x | 1.5 | 2026-11-15T19:59:37.424319+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | AAVE/USD | 108.09 | 78.594 | 87.334 | +7.50% | +0.13% | 0.06x | 5.5 | 2026-11-15T19:59:37.424319+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 98.302 | 501.41 | +0.26% | 0.24x |
| 2 | UNI/USD | 97.264 | 5.1883 | +0.34% | 1.55x |
| 3 | QNT/USD | 96.475 | 156.03 | +0.29% | 6.64x |
| 4 | XRP/USD | 90.991 | 0.96083 | +0.28% | 0.65x |
| 5 | CC/USD | 88.058 | 0.08329 | +0.26% | 0.40x |
| 6 | ADA/USD | 87.824 | 0.154798 | +0.34% | 0.73x |
| 7 | AAVE/USD | 87.334 | 108.09 | +0.13% | 0.06x |
| 8 | NEAR/USD | 86.587 | 3.1724 | +0.61% | 1.16x |
| 9 | HYPE/USD | 85.604 | 67.19 | +0.16% | 0.29x |
| 10 | NIGHT/USD | 82.807 | 0.04954 | +0.28% | 1.19x |
| 11 | ASTER/USD | 82.134 | 0.54736 | -0.27% | 1.30x |
| 12 | XDG/USD | 75.783 | 0.0590176 | +0.16% | 3.58x |

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

- Persisted scans: 441; predictions: 3808; observations: 265602.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 11135. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 43755438923 · **Generation:** 441 · **Legacy run:** 43755438923
**Main quote time:** 2026-11-15T19:59:45.520650+00:00 · **Legacy report time:** 2026-11-15T19:59:57.753192+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 156.03 | 112.95 | +0.29% | 6.64x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD ⭐ | 5.1883 | 104.47 | +0.34% | 1.55x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | XMR/USD | 501.41 | 91.97 | +0.26% | 0.24x | STRONG 76/100 | VERY_HIGH 70/100 | Watch |
| 4 | XDG/USD ⭐ | 0.0590176 | 91.56 | +0.16% | 3.58x | STRONG 100/100 | HIGH 55/100 | Watch |
| 5 | NEAR/USD ⭐ | 3.1724 | 91.29 | +0.61% | 1.16x | STRONG 91/100 | HIGH 62/100 | Watch |
| 6 | XRP/USD | 0.96083 | 88.90 | +0.28% | 0.65x | STRONG 74/100 | VERY_HIGH 70/100 | Watch |
| 7 | ADA/USD | 0.154798 | 86.82 | +0.34% | 0.73x | STRONG 73/100 | VERY_HIGH 70/100 | Watch |
| 8 | NIGHT/USD ⭐ | 0.04954 | 86.12 | +0.28% | 1.19x | STRONG 88/100 | HIGH 62/100 | Watch |
| 9 | ASTER/USD | 0.54736 | 83.77 | -0.27% | 1.30x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 10 | CC/USD | 0.08329 | 83.37 | +0.26% | 0.40x | STRONG 72/100 | VERY_HIGH 70/100 | Watch |
| 11 | HYPE/USD | 67.19 | 79.36 | +0.16% | 0.29x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 12 | AAVE/USD | 108.09 | 78.59 | +0.13% | 0.06x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | UNI/USD ⭐ | 5.1883 | 98.59 | +0.34% | 1.55x | 12677 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XDG/USD ⭐ | 0.0590176 | 96.08 | +0.16% | 3.58x | 21615 | STRONG 100/100 | HIGH 55/100 | Watch |
| 3 | QNT/USD ⭐ | 155.95 | 93.88 | +0.29% | 6.64x | 9583 | STRONG 100/100 | HIGH 61/100 | Consider small entry |
| 4 | NEAR/USD ⭐ | 3.1706 | 93.66 | +0.61% | 1.16x | 16005 | STRONG 92/100 | HIGH 62/100 | Watch |
| 5 | NIGHT/USD ⭐ | 0.04961 | 93.55 | +0.28% | 1.19x | 18811 | STRONG 92/100 | HIGH 62/100 | Watch |
| 6 | LINK/USD | 9.23865 | 92.54 | +0.09% | 1.11x | 12006 | STRONG 71/100 | HIGH 62/100 | Watch |

**Same-run overlap:** QNT/USD, UNI/USD, XDG/USD, NEAR/USD, NIGHT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
