# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T11:05:59.754118+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45807207737
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** d7577dd18333fe9d52b5da663073578e0d099e3a (atomic ledger/results publication)
**Ledger generation:** 1852 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 585; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SEI/USD | 0.03617 | 83.441 | 71.906 | +8.59% | +1.04% | 1.63x | 11.1 | 2026-11-26T11:05:51.594549+00:00 | Not calibrated | STRONG 82/100 | HIGH 66/100 | Consider small entry | WATCH |
| 2 | ADA/USD | 0.148034 | 77.975 | 63.778 | +1.55% | +0.14% | 2.35x | 4.2 | 2026-11-26T11:05:51.594549+00:00 | Not calibrated | STRONG 84/100 | HIGH 55/100 | Watch | WATCH |
| 3 | XRP/USD | 0.94918 | 71.630 | 64.222 | +1.35% | +0.11% | 1.69x | 0.4 | 2026-11-26T11:05:51.594549+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 4 | SKY/USD | 0.04439 | 69.981 | 72.435 | +5.99% | +0.32% | 0.60x | 6.8 | 2026-11-26T11:05:51.594549+00:00 | Not calibrated | MODERATE 65/100 | VERY_HIGH 75/100 | Watch | WATCH |
| 5 | SYRUP/USD | 0.07162 | 69.212 | 70.378 | +8.07% | +1.37% | 0.20x | 14.0 | 2026-11-26T11:05:51.594549+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 81/100 | Watch | WATCH |
| 6 | CC/USD | 0.07955 | 66.970 | 52.535 | +2.71% | -0.11% | 5.05x | 3.8 | 2026-11-26T11:05:51.594549+00:00 | Not calibrated | MODERATE 63/100 | HIGH 66/100 | Watch | WATCH |
| 7 | XDG/USD | 0.0565276 | 66.949 | 57.565 | +1.02% | -0.03% | 1.95x | 0.0 | 2026-11-26T11:05:51.594549+00:00 | Not calibrated | MODERATE 53/100 | HIGH 61/100 | Watch | WATCH |
| 8 | LTC/USD | 43.41 | 65.045 | 65.320 | +1.64% | +0.14% | 0.90x | 2.3 | 2026-11-26T11:05:51.594549+00:00 | Not calibrated | MODERATE 53/100 | HIGH 62/100 | Watch | WATCH |
| 9 | BAT/USD | 0.08072 | 64.763 | 47.085 | +2.41% | +0.54% | 3.48x | 3.7 | 2026-11-26T11:05:51.594549+00:00 | Not calibrated | STRONG 87/100 | HIGH 60/100 | Watch | WATCH |
| 10 | LINK/USD | 9.19805 | 63.367 | 64.761 | +1.70% | +0.08% | 0.82x | 4.2 | 2026-11-26T11:05:51.594549+00:00 | Not calibrated | MODERATE 52/100 | HIGH 62/100 | Watch | WATCH |
| 11 | INJ/USD | 6.167 | 58.865 | 65.395 | +3.58% | +0.08% | 0.31x | 6.5 | 2026-11-26T11:05:51.594549+00:00 | Not calibrated | MODERATE 49/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | DOT/USD | 0.67 | 44.427 | 44.070 | +1.78% | +0.22% | 0.92x | 3.0 | 2026-11-26T11:05:51.594549+00:00 | Not calibrated | MODERATE 52/100 | HIGH 67/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 72.435 | 0.04439 | +0.32% | 0.60x |
| 2 | SEI/USD | 71.906 | 0.03617 | +1.04% | 1.63x |
| 3 | SYRUP/USD | 70.378 | 0.07162 | +1.37% | 0.20x |
| 4 | INJ/USD | 65.395 | 6.167 | +0.08% | 0.31x |
| 5 | LTC/USD | 65.320 | 43.41 | +0.14% | 0.90x |
| 6 | LINK/USD | 64.761 | 9.19805 | +0.08% | 0.82x |
| 7 | XRP/USD | 64.222 | 0.94918 | +0.11% | 1.69x |
| 8 | ADA/USD | 63.778 | 0.148034 | +0.14% | 2.35x |
| 9 | XDG/USD | 57.565 | 0.0565276 | -0.03% | 1.95x |
| 10 | CC/USD | 52.535 | 0.07955 | -0.11% | 5.05x |
| 11 | BAT/USD | 47.085 | 0.08072 | +0.54% | 3.48x |
| 12 | DOT/USD | 44.070 | 0.67 | +0.22% | 0.92x |

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

- Persisted scans: 1852; predictions: 15959; observations: 1122665.
- Matured sampled outcomes across 1/6/24/48h: 34562; gap abstentions: 24613. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
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

**Writer:** 45807207737 · **Generation:** 1852 · **Legacy run:** 45807207737
**Main quote time:** 2026-11-26T11:05:59.754118+00:00 · **Legacy report time:** 2026-11-26T11:07:05.899857+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SEI/USD ⭐ | 0.03617 | 83.44 | +1.04% | 1.63x | STRONG 92/100 | HIGH 66/100 | Consider small entry |
| 2 | ADA/USD ⭐ | 0.148034 | 77.98 | +0.14% | 2.35x | STRONG 94/100 | HIGH 55/100 | Watch |
| 3 | XRP/USD ⭐ | 0.94918 | 71.63 | +0.11% | 1.69x | STRONG 81/100 | HIGH 55/100 | Watch |
| 4 | SKY/USD | 0.04439 | 69.98 | +0.32% | 0.60x | MODERATE 65/100 | VERY_HIGH 75/100 | Watch |
| 5 | SYRUP/USD | 0.07162 | 69.21 | +1.37% | 0.20x | MODERATE 60/100 | VERY_HIGH 81/100 | Watch |
| 6 | CC/USD | 0.07955 | 66.97 | -0.11% | 5.05x | MODERATE 63/100 | HIGH 66/100 | Watch |
| 7 | XDG/USD | 0.0565276 | 66.95 | -0.03% | 1.95x | MODERATE 53/100 | HIGH 61/100 | Watch |
| 8 | LTC/USD | 43.41 | 65.04 | +0.14% | 0.90x | MODERATE 53/100 | HIGH 62/100 | Watch |
| 9 | BAT/USD | 0.08072 | 64.76 | +0.54% | 3.48x | STRONG 87/100 | HIGH 60/100 | Watch |
| 10 | LINK/USD | 9.19805 | 63.37 | +0.08% | 0.82x | MODERATE 52/100 | HIGH 62/100 | Watch |
| 11 | INJ/USD | 6.167 | 58.87 | +0.08% | 0.31x | MODERATE 49/100 | VERY_HIGH 70/100 | Watch |
| 12 | DOT/USD | 0.67 | 44.43 | +0.22% | 0.92x | MODERATE 52/100 | HIGH 67/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SEI/USD ⭐ | 0.03618 | 76.21 | +1.04% | 1.63x | 2531 | STRONG 93/100 | HIGH 60/100 | Consider small entry |
| 2 | ADA/USD ⭐ | 0.148091 | 72.88 | +0.14% | 2.35x | 12489 | STRONG 91/100 | HIGH 55/100 | Watch |
| 3 | XRP/USD ⭐ | 0.94903 | 70.84 | +0.11% | 1.69x | 39244 | STRONG 80/100 | HIGH 55/100 | Watch |

**Same-run overlap:** SEI/USD, ADA/USD, XRP/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
