# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-21T17:20:53.008516+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44929411698
**Source SHA:** 7ac7b40f8385b7b363a3015feba153e001ac4fc4
**Previous ledger commit:** 02cff75ff0179b04750ca38bafe77688bf2a66d4 (atomic ledger/results publication)
**Ledger generation:** 1163 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 608; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NIGHT/USD | 0.0452 | 106.588 | 87.527 | +7.06% | +2.61% | 1.60x | 8.8 | 2026-11-21T17:20:44.934453+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | UNI/USD | 4.7295 | 100.377 | 93.564 | +5.87% | -0.20% | 1.78x | 5.1 | 2026-11-21T17:20:44.934453+00:00 | Not calibrated | STRONG 70/100 | HIGH 61/100 | Watch | WATCH |
| 3 | XMR/USD | 484.3 | 96.730 | 94.353 | +6.14% | +0.79% | 0.84x | 7.2 | 2026-11-21T17:20:44.934453+00:00 | Not calibrated | STRONG 78/100 | HIGH 62/100 | Watch | WATCH |
| 4 | CT/USD | 0.1322 | 81.739 | 68.998 | +9.17% | -0.45% | 4.38x | 15.2 | 2026-11-21T17:20:44.934453+00:00 | Not calibrated | MODERATE 66/100 | VERY_HIGH 79/100 | Watch | WATCH |
| 5 | ETH/USD | 1682.24 | 79.852 | 82.169 | +3.89% | -0.01% | 0.77x | 0.1 | 2026-11-21T17:20:44.934453+00:00 | Not calibrated | MODERATE 45/100 | HIGH 68/100 | Watch | WATCH |
| 6 | XBT/USD | 60105.7 | 79.740 | 70.458 | +2.21% | +0.07% | 1.90x | 0.0 | 2026-11-21T17:20:44.934453+00:00 | Not calibrated | STRONG 75/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ZEC/USD | 788.37 | 78.980 | 83.069 | +4.02% | +0.12% | 0.53x | 0.1 | 2026-11-21T17:20:44.934453+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | SOL/USD | 70.71 | 78.931 | 74.668 | +2.91% | +0.01% | 1.42x | 1.4 | 2026-11-21T17:20:44.934453+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 9 | TAO/USD | 185.8412 | 73.151 | 72.140 | +2.95% | -0.00% | 1.10x | 7.1 | 2026-11-21T17:20:44.934453+00:00 | Not calibrated | MODERATE 47/100 | HIGH 68/100 | Watch | WATCH |
| 10 | PAXG/USD | 3549.14 | 72.790 | 57.654 | +0.50% | +0.03% | 2.84x | 1.0 | 2026-11-21T17:20:44.934453+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 11 | XRP/USD | 0.93075 | 66.953 | 71.333 | +2.43% | +0.13% | 0.50x | 1.3 | 2026-11-21T17:20:44.934453+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0551567 | 64.962 | 66.145 | +1.62% | +0.20% | 0.78x | 0.5 | 2026-11-21T17:20:44.934453+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | XMR/USD | 94.353 | 484.3 | +0.79% | 0.84x |
| 2 | UNI/USD | 93.564 | 4.7295 | -0.20% | 1.78x |
| 3 | NIGHT/USD | 87.527 | 0.0452 | +2.61% | 1.60x |
| 4 | ZEC/USD | 83.069 | 788.37 | +0.12% | 0.53x |
| 5 | ETH/USD | 82.169 | 1682.24 | -0.01% | 0.77x |
| 6 | SOL/USD | 74.668 | 70.71 | +0.01% | 1.42x |
| 7 | TAO/USD | 72.140 | 185.8412 | -0.00% | 1.10x |
| 8 | XRP/USD | 71.333 | 0.93075 | +0.13% | 0.50x |
| 9 | XBT/USD | 70.458 | 60105.7 | +0.07% | 1.90x |
| 10 | CT/USD | 68.998 | 0.1322 | -0.45% | 4.38x |
| 11 | XDG/USD | 66.145 | 0.0551567 | +0.20% | 0.78x |
| 12 | PAXG/USD | 57.654 | 3549.14 | +0.03% | 2.84x |

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

- Persisted scans: 1163; predictions: 9265; observations: 703463.
- Matured sampled outcomes across 1/6/24/48h: 12195; gap abstentions: 20915. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 16 (sampled only; not a success-rate estimate).
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

**Writer:** 44929411698 · **Generation:** 1163 · **Legacy run:** 44929411698
**Main quote time:** 2026-11-21T17:20:53.008516+00:00 · **Legacy report time:** 2026-11-21T17:21:37.807745+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.0452 | 106.59 | +2.61% | 1.60x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | UNI/USD | 4.7295 | 100.38 | -0.20% | 1.78x | STRONG 70/100 | HIGH 61/100 | Watch |
| 3 | XMR/USD | 484.3 | 96.73 | +0.79% | 0.84x | STRONG 78/100 | HIGH 62/100 | Watch |
| 4 | CT/USD | 0.1322 | 81.74 | -0.45% | 4.38x | MODERATE 66/100 | VERY_HIGH 79/100 | Watch |
| 5 | ETH/USD | 1682.24 | 79.85 | -0.01% | 0.77x | MODERATE 45/100 | HIGH 68/100 | Watch |
| 6 | XBT/USD ⭐ | 60105.7 | 79.74 | +0.07% | 1.90x | STRONG 85/100 | HIGH 55/100 | Watch |
| 7 | ZEC/USD | 788.37 | 78.98 | +0.12% | 0.53x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 8 | SOL/USD | 70.71 | 78.93 | +0.01% | 1.42x | STRONG 74/100 | HIGH 55/100 | Watch |
| 9 | TAO/USD | 185.8412 | 73.15 | -0.00% | 1.10x | MODERATE 47/100 | HIGH 68/100 | Watch |
| 10 | PAXG/USD | 3549.14 | 72.79 | +0.03% | 2.84x | STRONG 81/100 | HIGH 55/100 | Watch |
| 11 | XRP/USD | 0.93075 | 66.95 | +0.13% | 0.50x | MODERATE 53/100 | VERY_HIGH 70/100 | Watch |
| 12 | XDG/USD | 0.0551567 | 64.96 | +0.20% | 0.78x | MODERATE 52/100 | HIGH 62/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NIGHT/USD ⭐ | 0.04521 | 92.16 | +2.61% | 1.60x | 11110 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XBT/USD ⭐ | 60087.8 | 81.79 | +0.07% | 1.90x | 247014 | STRONG 86/100 | HIGH 55/100 | Watch |
| 3 | SHX/USD | 0.003515 | 74.02 | +0.14% | 1.63x | 2744 | MODERATE 67/100 | HIGH 66/100 | Watch |

**Same-run overlap:** NIGHT/USD, XBT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
