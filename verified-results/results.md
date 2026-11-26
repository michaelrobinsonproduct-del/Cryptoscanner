# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T11:26:54.714202+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45810320318
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 0483db8324623f10ee3232d099a05d6138347964 (atomic ledger/results publication)
**Ledger generation:** 1854 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 586; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | ADA/USD | 0.148141 | 81.914 | 65.305 | +1.63% | +0.32% | 3.85x | 2.2 | 2026-11-26T11:26:47.111755+00:00 | Not calibrated | STRONG 96/100 | HIGH 55/100 | Consider small entry | WATCH |
| 2 | SKY/USD | 0.04452 | 79.828 | 75.775 | +6.30% | +0.23% | 1.29x | 4.5 | 2026-11-26T11:26:47.111755+00:00 | Not calibrated | STRONG 75/100 | HIGH 60/100 | Watch | WATCH |
| 3 | SEI/USD | 0.03665 | 78.531 | 73.507 | +10.03% | +0.36% | 1.32x | 8.2 | 2026-11-26T11:26:47.111755+00:00 | Not calibrated | STRONG 84/100 | HIGH 60/100 | Watch | WATCH |
| 4 | LTC/USD | 43.56 | 71.582 | 67.783 | +1.99% | +0.30% | 1.23x | 2.3 | 2026-11-26T11:26:47.111755+00:00 | Not calibrated | STRONG 71/100 | HIGH 62/100 | Watch | WATCH |
| 5 | SYRUP/USD | 0.07178 | 69.687 | 71.046 | +8.31% | +0.17% | 0.78x | 12.5 | 2026-11-26T11:26:47.111755+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 6 | LINK/USD | 9.22454 | 67.159 | 67.897 | +1.99% | +0.43% | 0.71x | 2.1 | 2026-11-26T11:26:47.111755+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 7 | XRP/USD | 0.95143 | 65.096 | 66.061 | +1.59% | +0.37% | 0.72x | 0.1 | 2026-11-26T11:26:47.111755+00:00 | Not calibrated | MODERATE 63/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 8 | WIF/USD | 0.1341 | 64.761 | 64.841 | +5.34% | +0.90% | 0.54x | 7.5 | 2026-11-26T11:26:47.111755+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 9 | DOT/USD | 0.6734 | 64.118 | 48.447 | +2.29% | +0.39% | 2.37x | 1.5 | 2026-11-26T11:26:47.111755+00:00 | Not calibrated | STRONG 87/100 | HIGH 60/100 | Watch | WATCH |
| 10 | INJ/USD | 6.199 | 63.742 | 70.014 | +4.11% | +0.13% | 0.31x | 4.8 | 2026-11-26T11:26:47.111755+00:00 | Not calibrated | MODERATE 52/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | QNT/USD | 148.39 | 60.129 | 65.359 | +2.48% | +0.26% | 0.35x | 4.0 | 2026-11-26T11:26:47.111755+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | XDG/USD | 0.0567193 | 59.256 | 60.124 | +1.36% | +0.33% | 0.75x | 0.0 | 2026-11-26T11:26:47.111755+00:00 | Not calibrated | MODERATE 60/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 75.775 | 0.04452 | +0.23% | 1.29x |
| 2 | SEI/USD | 73.507 | 0.03665 | +0.36% | 1.32x |
| 3 | SYRUP/USD | 71.046 | 0.07178 | +0.17% | 0.78x |
| 4 | INJ/USD | 70.014 | 6.199 | +0.13% | 0.31x |
| 5 | LINK/USD | 67.897 | 9.22454 | +0.43% | 0.71x |
| 6 | LTC/USD | 67.783 | 43.56 | +0.30% | 1.23x |
| 7 | XRP/USD | 66.061 | 0.95143 | +0.37% | 0.72x |
| 8 | QNT/USD | 65.359 | 148.39 | +0.26% | 0.35x |
| 9 | ADA/USD | 65.305 | 0.148141 | +0.32% | 3.85x |
| 10 | WIF/USD | 64.841 | 0.1341 | +0.90% | 0.54x |
| 11 | XDG/USD | 60.124 | 0.0567193 | +0.33% | 0.75x |
| 12 | DOT/USD | 48.447 | 0.6734 | +0.39% | 2.37x |

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

- Persisted scans: 1854; predictions: 15983; observations: 1123836.
- Matured sampled outcomes across 1/6/24/48h: 34610; gap abstentions: 24641. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 146 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 3; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 45810320318 · **Generation:** 1854 · **Legacy run:** 45810320318
**Main quote time:** 2026-11-26T11:26:54.714202+00:00 · **Legacy report time:** 2026-11-26T11:28:13.479376+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | ADA/USD | 0.148141 | 81.91 | +0.32% | 3.85x | STRONG 96/100 | HIGH 55/100 | Consider small entry |
| 2 | SKY/USD ⭐ | 0.04452 | 79.83 | +0.23% | 1.29x | STRONG 85/100 | HIGH 60/100 | Watch |
| 3 | SEI/USD ⭐ | 0.03665 | 78.53 | +0.36% | 1.32x | STRONG 94/100 | HIGH 60/100 | Watch |
| 4 | LTC/USD ⭐ | 43.56 | 71.58 | +0.30% | 1.23x | STRONG 81/100 | HIGH 62/100 | Watch |
| 5 | SYRUP/USD | 0.07178 | 69.69 | +0.17% | 0.78x | MODERATE 50/100 | VERY_HIGH 73/100 | Watch |
| 6 | LINK/USD | 9.22454 | 67.16 | +0.43% | 0.71x | MODERATE 64/100 | VERY_HIGH 70/100 | Watch |
| 7 | XRP/USD | 0.95143 | 65.10 | +0.37% | 0.72x | MODERATE 63/100 | VERY_HIGH 70/100 | Watch |
| 8 | WIF/USD | 0.1341 | 64.76 | +0.90% | 0.54x | MODERATE 62/100 | VERY_HIGH 82/100 | Watch |
| 9 | DOT/USD | 0.6734 | 64.12 | +0.39% | 2.37x | STRONG 87/100 | HIGH 60/100 | Watch |
| 10 | INJ/USD | 6.199 | 63.74 | +0.13% | 0.31x | MODERATE 52/100 | VERY_HIGH 70/100 | Watch |
| 11 | QNT/USD | 148.39 | 60.13 | +0.26% | 0.35x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |
| 12 | XDG/USD | 0.0567193 | 59.26 | +0.33% | 0.75x | MODERATE 60/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | FET/USD | 0.1149 | 78.41 | +0.88% | 2.60x | 2313 | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 2 | SKY/USD ⭐ | 0.04451 | 75.70 | +0.23% | 1.29x | 4271 | STRONG 83/100 | HIGH 60/100 | Watch |
| 3 | SEI/USD ⭐ | 0.03657 | 73.93 | +0.36% | 1.32x | 2682 | STRONG 92/100 | HIGH 60/100 | Watch |
| 4 | LTC/USD ⭐ | 43.54 | 72.55 | +0.30% | 1.23x | 15555 | STRONG 81/100 | HIGH 62/100 | Watch |

**Same-run overlap:** SKY/USD, SEI/USD, LTC/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
