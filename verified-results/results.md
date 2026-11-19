# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T23:50:53.090353+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44640846761
**Source SHA:** f854bf15990e1aa3564d35bbec4100f929bd3d42
**Previous ledger commit:** b7dcfbfcddb1aab273f4a4103c115c6ce92f8ccd (atomic ledger/results publication)
**Ledger generation:** 882 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 603; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | CSPR/USD | 0.0016911 | 75.960 | 56.197 | +3.55% | +1.20% | 2.37x | 1.2 | 2026-11-19T23:50:44.520012+00:00 | Not calibrated | STRONG 93/100 | HIGH 60/100 | Consider small entry | WATCH |
| 2 | INJ/USD | 7.075 | 61.504 | 52.286 | +1.35% | +0.21% | 1.82x | 5.7 | 2026-11-19T23:50:44.520012+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 3 | VVV/USD | 21.841 | 61.130 | 57.286 | +0.78% | +0.06% | 1.35x | 6.4 | 2026-11-19T23:50:44.520012+00:00 | Not calibrated | MODERATE 66/100 | HIGH 55/100 | Watch | WATCH |
| 4 | USELESS/USD | 0.09909 | 59.962 | 56.930 | +3.69% | +0.49% | 1.06x | 19.2 | 2026-11-19T23:50:44.520012+00:00 | Not calibrated | MODERATE 60/100 | HIGH 68/100 | Watch | WATCH |
| 5 | SENT/USD | 0.02125 | 59.937 | 52.926 | +3.13% | +0.36% | 1.52x | 6.6 | 2026-11-19T23:50:44.520012+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |
| 6 | AKT/USD | 0.5351 | 48.532 | 50.005 | +3.30% | +1.02% | 0.34x | 11.2 | 2026-11-19T23:50:44.520012+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 7 | TRX/USD | 0.310111 | 47.541 | 44.142 | +0.27% | +0.02% | 1.33x | 0.0 | 2026-11-19T23:50:44.520012+00:00 | Not calibrated | MODERATE 59/100 | HIGH 55/100 | Watch | WATCH |
| 8 | BABY/USD | 0.00843 | 47.433 | 32.433 | +1.08% | +0.00% | 8.53x | 11.9 | 2026-11-19T23:50:44.520012+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 9 | LIGHTER/USD | 2.76 | 47.195 | 43.109 | +1.69% | +0.47% | 1.17x | 7.3 | 2026-11-19T23:50:44.520012+00:00 | Not calibrated | MODERATE 59/100 | HIGH 67/100 | Watch | WATCH |
| 10 | CAP/USD | 0.096533 | 30.472 | 35.323 | +0.54% | +0.32% | 0.35x | 6.1 | 2026-11-19T23:50:44.520012+00:00 | Not calibrated | MODERATE 45/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 11 | AKE/USD | 0.01049944 | 28.511 | 33.347 | +1.05% | -0.58% | 0.81x | 17.0 | 2026-11-19T23:50:44.520012+00:00 | Not calibrated | WEAK 14/100 | VERY_HIGH 79/100 | Do nothing | WATCH |
| 12 | ZEREBRO/USD | 0.02198 | 26.227 | 22.266 | +0.73% | +0.18% | 1.30x | 27.3 | 2026-11-19T23:50:44.520012+00:00 | Not calibrated | WEAK 38/100 | VERY_HIGH 79/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | VVV/USD | 57.286 | 21.841 | +0.06% | 1.35x |
| 2 | USELESS/USD | 56.930 | 0.09909 | +0.49% | 1.06x |
| 3 | CSPR/USD | 56.197 | 0.0016911 | +1.20% | 2.37x |
| 4 | SENT/USD | 52.926 | 0.02125 | +0.36% | 1.52x |
| 5 | INJ/USD | 52.286 | 7.075 | +0.21% | 1.82x |
| 6 | AKT/USD | 50.005 | 0.5351 | +1.02% | 0.34x |
| 7 | TRX/USD | 44.142 | 0.310111 | +0.02% | 1.33x |
| 8 | LIGHTER/USD | 43.109 | 2.76 | +0.47% | 1.17x |
| 9 | CAP/USD | 35.323 | 0.096533 | +0.32% | 0.35x |
| 10 | AKE/USD | 33.347 | 0.01049944 | -0.58% | 0.81x |
| 11 | BABY/USD | 32.433 | 0.00843 | +0.00% | 8.53x |
| 12 | ZEREBRO/USD | 22.266 | 0.02198 | +0.18% | 1.30x |

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

- Persisted scans: 882; predictions: 7691; observations: 532971.
- Matured sampled outcomes across 1/6/24/48h: 8266; gap abstentions: 15919. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 11; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44640846761 · **Generation:** 882 · **Legacy run:** 44640846761
**Main quote time:** 2026-11-19T23:50:53.090353+00:00 · **Legacy report time:** 2026-11-19T23:51:42.579983+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | CSPR/USD ⭐ | 0.0016911 | 75.96 | +1.20% | 2.37x | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | INJ/USD ⭐ | 7.075 | 61.50 | +0.21% | 1.82x | STRONG 86/100 | HIGH 55/100 | Consider small entry |
| 3 | VVV/USD ⭐ | 21.841 | 61.13 | +0.06% | 1.35x | STRONG 76/100 | HIGH 55/100 | Watch |
| 4 | USELESS/USD ⭐ | 0.09909 | 59.96 | +0.49% | 1.06x | STRONG 70/100 | HIGH 68/100 | Watch |
| 5 | SENT/USD ⭐ | 0.02125 | 59.94 | +0.36% | 1.52x | STRONG 85/100 | HIGH 60/100 | Consider small entry |
| 6 | AKT/USD | 0.5351 | 48.53 | +1.02% | 0.34x | MODERATE 49/100 | VERY_HIGH 81/100 | Watch |
| 7 | TRX/USD | 0.310111 | 47.54 | +0.02% | 1.33x | MODERATE 59/100 | HIGH 55/100 | Watch |
| 8 | BABY/USD | 0.00843 | 47.43 | +0.00% | 8.53x | MODERATE 64/100 | VERY_HIGH 73/100 | Watch |
| 9 | LIGHTER/USD | 2.76 | 47.19 | +0.47% | 1.17x | MODERATE 59/100 | HIGH 67/100 | Watch |
| 10 | CAP/USD | 0.096533 | 30.47 | +0.32% | 0.35x | MODERATE 45/100 | VERY_HIGH 75/100 | Watch |
| 11 | AKE/USD | 0.01049944 | 28.51 | -0.58% | 0.81x | WEAK 14/100 | VERY_HIGH 79/100 | Do nothing |
| 12 | ZEREBRO/USD | 0.02198 | 26.23 | +0.18% | 1.30x | WEAK 38/100 | VERY_HIGH 79/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | CSPR/USD ⭐ | 0.0016911 | 87.52 | +1.20% | 2.37x | 6244 | STRONG 100/100 | HIGH 60/100 | Consider small entry |
| 2 | USELESS/USD ⭐ | 0.09868 | 69.27 | +0.49% | 1.06x | 6381 | STRONG 70/100 | VERY_HIGH 74/100 | Watch |
| 3 | SENT/USD ⭐ | 0.021237 | 64.55 | +0.36% | 1.52x | 14679 | STRONG 87/100 | HIGH 60/100 | Consider small entry |
| 4 | INJ/USD ⭐ | 7.075 | 57.97 | +0.21% | 1.82x | 7542 | STRONG 84/100 | HIGH 55/100 | Consider small entry |
| 5 | VVV/USD ⭐ | 21.83 | 49.56 | +0.06% | 1.35x | 13228 | STRONG 70/100 | HIGH 55/100 | Watch |

**Same-run overlap:** CSPR/USD, INJ/USD, VVV/USD, USELESS/USD, SENT/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
