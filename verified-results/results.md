# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-15T19:24:35.771810+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/43752217568
**Source SHA:** 885b4a0465f5c74a8a87db5ca921c3c0a00021af
**Previous ledger commit:** 919e12ff58d06275d427c66a54498b6214c03520 (atomic ledger/results publication)
**Ledger generation:** 434 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 7s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 625; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 607; valid market observations: 607; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | XMR/USD | 498.99 | 103.866 | 93.394 | +6.13% | +0.40% | 1.85x | 9.0 | 2026-11-15T19:24:28.973991+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | ZEC/USD | 900.73 | 100.790 | 82.869 | +4.27% | +0.58% | 5.87x | 4.0 | 2026-11-15T19:24:28.973991+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 3 | UNI/USD | 5.1743 | 100.700 | 94.290 | +5.99% | +0.48% | 1.40x | 5.2 | 2026-11-15T19:24:28.973991+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Watch | WATCH |
| 4 | AAVE/USD | 107.9 | 99.175 | 87.803 | +7.31% | +0.63% | 1.82x | 4.6 | 2026-11-15T19:24:28.973991+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 5 | CC/USD | 0.08304 | 97.673 | 86.200 | +7.00% | -0.71% | 4.03x | 7.2 | 2026-11-15T19:24:28.973991+00:00 | Not calibrated | STRONG 79/100 | HIGH 61/100 | Watch | WATCH |
| 6 | NEAR/USD | 3.1503 | 95.537 | 81.151 | +4.01% | +0.32% | 2.28x | 3.8 | 2026-11-15T19:24:28.973991+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 7 | QNT/USD | 155.05 | 94.956 | 97.098 | +8.19% | +0.64% | 0.47x | 5.8 | 2026-11-15T19:24:28.973991+00:00 | Not calibrated | STRONG 77/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | ETH/USD | 1822.54 | 93.053 | 76.497 | +3.07% | +0.31% | 2.74x | 0.1 | 2026-11-15T19:24:28.973991+00:00 | Not calibrated | STRONG 100/100 | HIGH 55/100 | Consider small entry | WATCH |
| 9 | XRP/USD | 0.95563 | 91.690 | 86.745 | +4.58% | +0.20% | 1.40x | 0.6 | 2026-11-15T19:24:28.973991+00:00 | Not calibrated | STRONG 81/100 | HIGH 55/100 | Watch | WATCH |
| 10 | ADA/USD | 0.154166 | 89.595 | 84.240 | +4.41% | +0.42% | 1.33x | 3.2 | 2026-11-15T19:24:28.973991+00:00 | Not calibrated | STRONG 90/100 | HIGH 55/100 | Watch | WATCH |
| 11 | ASTER/USD | 0.54559 | 89.361 | 83.310 | +8.99% | -0.10% | 1.66x | 6.4 | 2026-11-15T19:24:28.973991+00:00 | Not calibrated | MODERATE 65/100 | HIGH 61/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0588877 | 81.443 | 73.874 | +2.74% | +0.17% | 1.67x | 0.7 | 2026-11-15T19:24:28.973991+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | QNT/USD | 97.098 | 155.05 | +0.64% | 0.47x |
| 2 | UNI/USD | 94.290 | 5.1743 | +0.48% | 1.40x |
| 3 | XMR/USD | 93.394 | 498.99 | +0.40% | 1.85x |
| 4 | AAVE/USD | 87.803 | 107.9 | +0.63% | 1.82x |
| 5 | XRP/USD | 86.745 | 0.95563 | +0.20% | 1.40x |
| 6 | CC/USD | 86.200 | 0.08304 | -0.71% | 4.03x |
| 7 | ADA/USD | 84.240 | 0.154166 | +0.42% | 1.33x |
| 8 | ASTER/USD | 83.310 | 0.54559 | -0.10% | 1.66x |
| 9 | ZEC/USD | 82.869 | 900.73 | +0.58% | 5.87x |
| 10 | NEAR/USD | 81.151 | 3.1503 | +0.32% | 2.28x |
| 11 | ETH/USD | 76.497 | 1822.54 | +0.31% | 2.74x |
| 12 | XDG/USD | 73.874 | 0.0588877 | +0.17% | 1.67x |

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

- Persisted scans: 434; predictions: 3724; observations: 261353.
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

**Writer:** 43752217568 · **Generation:** 434 · **Legacy run:** 43752217568
**Main quote time:** 2026-11-15T19:24:35.771810+00:00 · **Legacy report time:** 2026-11-15T19:24:51.572797+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | XMR/USD ⭐ | 498.99 | 103.87 | +0.40% | 1.85x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | ZEC/USD ⭐ | 900.73 | 100.79 | +0.58% | 5.87x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 3 | UNI/USD ⭐ | 5.1743 | 100.70 | +0.48% | 1.40x | STRONG 100/100 | HIGH 55/100 | Watch |
| 4 | AAVE/USD ⭐ | 107.9 | 99.17 | +0.63% | 1.82x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | CC/USD | 0.08304 | 97.67 | -0.71% | 4.03x | STRONG 79/100 | HIGH 61/100 | Watch |
| 6 | NEAR/USD ⭐ | 3.1503 | 95.54 | +0.32% | 2.28x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 7 | QNT/USD | 155.05 | 94.96 | +0.64% | 0.47x | STRONG 77/100 | VERY_HIGH 70/100 | Watch |
| 8 | ETH/USD ⭐ | 1822.54 | 93.05 | +0.31% | 2.74x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | XRP/USD ⭐ | 0.95563 | 91.69 | +0.20% | 1.40x | STRONG 91/100 | HIGH 55/100 | Watch |
| 10 | ADA/USD ⭐ | 0.154166 | 89.59 | +0.42% | 1.33x | STRONG 100/100 | HIGH 55/100 | Watch |
| 11 | ASTER/USD | 0.54559 | 89.36 | -0.10% | 1.66x | MODERATE 65/100 | HIGH 61/100 | Watch |
| 12 | XDG/USD ⭐ | 0.0588877 | 81.44 | +0.17% | 1.67x | STRONG 86/100 | HIGH 55/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.1503 | 100.00 | +0.32% | 2.28x | 16197 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | XRP/USD ⭐ | 0.95558 | 100.00 | +0.20% | 1.40x | 56194 | STRONG 95/100 | HIGH 55/100 | Watch |
| 3 | ZEC/USD ⭐ | 899.76 | 97.53 | +0.58% | 5.87x | 33258 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | ETH/USD ⭐ | 1822.84 | 96.88 | +0.31% | 2.74x | 84856 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 5 | ADA/USD ⭐ | 0.154166 | 93.34 | +0.42% | 1.33x | 24605 | STRONG 100/100 | HIGH 55/100 | Watch |
| 6 | TAO/USD | 191.7634 | 91.29 | +0.58% | 2.13x | 14719 | STRONG 96/100 | HIGH 61/100 | Consider small entry |
| 7 | XMR/USD ⭐ | 498.99 | 90.95 | +0.40% | 1.85x | 12143 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 8 | AAVE/USD ⭐ | 107.9 | 89.98 | +0.63% | 1.82x | 6403 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 9 | UNI/USD ⭐ | 5.1743 | 88.05 | +0.48% | 1.40x | 12827 | STRONG 99/100 | HIGH 55/100 | Watch |
| 10 | SUI/USD | 0.7227 | 87.82 | +0.49% | 1.51x | 21768 | STRONG 89/100 | HIGH 55/100 | Consider small entry |
| 11 | XDG/USD ⭐ | 0.0589014 | 86.68 | +0.17% | 1.67x | 21626 | STRONG 88/100 | HIGH 55/100 | Watch |
| 12 | HBAR/USD | 0.05888 | 85.84 | +0.70% | 1.58x | 10633 | STRONG 88/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** XMR/USD, ZEC/USD, UNI/USD, AAVE/USD, NEAR/USD, ETH/USD, XRP/USD, ADA/USD, XDG/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
