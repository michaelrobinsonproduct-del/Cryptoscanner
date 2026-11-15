# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-15T19:16:48.374276+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43751470378
**Source SHA:** 885b4a0465f5c74a8a87db5ca921c3c0a00021af
**Previous ledger commit:** 897eb66eca51d7c6dbae5c6d9fdf4c3bee1f30ef (atomic ledger/results publication)
**Ledger generation:** 433 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ADA/USD | 0.154284 | 102.934 | 84.476 | +4.49% | +0.69% | 4.12x | 3.9 | 2026-11-15T19:16:40.178268+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | XMR/USD | 499.4 | 102.293 | 93.811 | +6.22% | +0.69% | 1.50x | 9.4 | 2026-11-15T19:16:40.178268+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | ZEC/USD | 901.58 | 101.431 | 82.173 | +4.37% | +0.85% | 4.45x | 6.8 | 2026-11-15T19:16:40.178268+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | QNT/USD | 155.03 | 100.532 | 96.124 | +8.18% | +1.41% | 0.73x | 7.8 | 2026-11-15T19:16:40.178268+00:00 | Not calibrated | STRONG 80/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 5 | UNI/USD | 5.1708 | 98.451 | 93.686 | +5.91% | +0.57% | 1.19x | 5.4 | 2026-11-15T19:16:40.178268+00:00 | Not calibrated | STRONG 84/100 | HIGH 62/100 | Watch | WATCH |
| 6 | CC/USD | 0.08305 | 98.327 | 85.661 | +7.01% | -0.47% | 3.99x | 8.4 | 2026-11-15T19:16:40.178268+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Watch | WATCH |
| 7 | AAVE/USD | 108.18 | 97.924 | 86.369 | +7.59% | +1.04% | 1.64x | 7.4 | 2026-11-15T19:16:40.178268+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 8 | XRP/USD | 0.95608 | 94.373 | 86.881 | +4.63% | +0.46% | 1.52x | 1.0 | 2026-11-15T19:16:40.178268+00:00 | Not calibrated | STRONG 92/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | ETH/USD | 1821.52 | 93.590 | 76.093 | +3.02% | +0.50% | 2.57x | 0.1 | 2026-11-15T19:16:40.178268+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 10 | NEAR/USD | 3.1592 | 91.382 | 82.579 | +4.30% | +0.64% | 1.56x | 5.1 | 2026-11-15T19:16:40.178268+00:00 | Not calibrated | STRONG 91/100 | HIGH 55/100 | Consider small entry | WATCH |
| 11 | HYPE/USD | 66.99 | 83.468 | 83.425 | +4.17% | +0.89% | 0.56x | 1.5 | 2026-11-15T19:16:40.178268+00:00 | Not calibrated | STRONG 72/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | NIGHT/USD | 0.04992 | 83.380 | 85.413 | +5.21% | +0.00% | 0.80x | 12.1 | 2026-11-15T19:16:40.178268+00:00 | Not calibrated | MODERATE 57/100 | HIGH 68/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 96.124 | 155.03 | +1.41% | 0.73x |
| 2 | XMR/USD | 93.811 | 499.4 | +0.69% | 1.50x |
| 3 | UNI/USD | 93.686 | 5.1708 | +0.57% | 1.19x |
| 4 | XRP/USD | 86.881 | 0.95608 | +0.46% | 1.52x |
| 5 | AAVE/USD | 86.369 | 108.18 | +1.04% | 1.64x |
| 6 | CC/USD | 85.661 | 0.08305 | -0.47% | 3.99x |
| 7 | NIGHT/USD | 85.413 | 0.04992 | +0.00% | 0.80x |
| 8 | ADA/USD | 84.476 | 0.154284 | +0.69% | 4.12x |
| 9 | HYPE/USD | 83.425 | 66.99 | +0.89% | 0.56x |
| 10 | NEAR/USD | 82.579 | 3.1592 | +0.64% | 1.56x |
| 11 | ZEC/USD | 82.173 | 901.58 | +0.85% | 4.45x |
| 12 | ETH/USD | 76.093 | 1821.52 | +0.50% | 2.57x |

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

- Persisted scans: 433; predictions: 3712; observations: 260746.
- Matured sampled outcomes across 1/6/24/48h: 3195; gap abstentions: 11129. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 43751470378 · **Generation:** 433 · **Legacy run:** 43751470378
**Main quote time:** 2026-11-15T19:16:48.374276+00:00 · **Legacy report time:** 2026-11-15T19:17:05.473602+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD ⭐ | 0.154284 | 102.93 | +0.69% | 4.12x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XMR/USD ⭐ | 499.4 | 102.29 | +0.69% | 1.50x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ZEC/USD ⭐ | 901.58 | 101.43 | +0.85% | 4.45x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | QNT/USD | 155.03 | 100.53 | +1.41% | 0.73x | STRONG 80/100 | VERY_HIGH 70/100 | Watch |
| 5 | UNI/USD ⭐ | 5.1708 | 98.45 | +0.57% | 1.19x | STRONG 94/100 | HIGH 62/100 | Watch |
| 6 | CC/USD | 0.08305 | 98.33 | -0.47% | 3.99x | STRONG 79/100 | HIGH 61/100 | Watch |
| 7 | AAVE/USD | 108.18 | 97.92 | +1.04% | 1.64x | STRONG 94/100 | HIGH 55/100 | Consider small entry |
| 8 | XRP/USD ⭐ | 0.95608 | 94.37 | +0.46% | 1.52x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | ETH/USD ⭐ | 1821.52 | 93.59 | +0.50% | 2.57x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 10 | NEAR/USD ⭐ | 3.1592 | 91.38 | +0.64% | 1.56x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 11 | HYPE/USD | 66.99 | 83.47 | +0.89% | 0.56x | STRONG 72/100 | VERY_HIGH 70/100 | Watch |
| 12 | NIGHT/USD | 0.04992 | 83.38 | +0.00% | 0.80x | MODERATE 57/100 | HIGH 68/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | XRP/USD ⭐ | 0.95591 | 100.00 | +0.46% | 1.52x | 56450 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 901.68 | 100.00 | +0.85% | 4.45x | 33298 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | ADA/USD ⭐ | 0.15419 | 98.91 | +0.69% | 4.12x | 24698 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ETH/USD ⭐ | 1821.44 | 95.81 | +0.50% | 2.57x | 85077 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | NEAR/USD ⭐ | 3.1585 | 94.65 | +0.64% | 1.56x | 16369 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 6 | UNI/USD ⭐ | 5.1708 | 93.20 | +0.57% | 1.19x | 13011 | STRONG 92/100 | HIGH 62/100 | Watch |
| 7 | SUI/USD | 0.7238 | 91.96 | +0.61% | 1.29x | 21805 | STRONG 81/100 | HIGH 55/100 | Watch |
| 8 | TAO/USD | 191.9855 | 91.51 | +0.72% | 2.09x | 14825 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | HBAR/USD | 0.05876 | 89.97 | +0.65% | 1.78x | 10737 | STRONG 90/100 | HIGH 55/100 | Consider small entry |
| 10 | XMR/USD ⭐ | 499 | 89.08 | +0.69% | 1.50x | 12239 | STRONG 95/100 | HIGH 61/100 | Consider small entry |
| 11 | XDG/USD | 0.0589063 | 88.97 | +0.54% | 1.52x | 21685 | STRONG 89/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** ADA/USD, XMR/USD, ZEC/USD, UNI/USD, XRP/USD, ETH/USD, NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
