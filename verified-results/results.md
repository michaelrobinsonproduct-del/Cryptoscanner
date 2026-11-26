# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-26T17:11:36.123403+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45865288256
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 94f79b10da23c3bc04af5ae2334a6b19dab8aa6b (atomic ledger/results publication)
**Ledger generation:** 1889 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 595; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | WIF/USD | 0.1359 | 85.580 | 72.781 | +6.76% | +0.66% | 1.95x | 7.4 | 2026-11-26T17:11:28.462689+00:00 | Not calibrated | STRONG 88/100 | HIGH 67/100 | Consider small entry | WATCH |
| 2 | LINK/USD | 9.1767 | 79.284 | 63.355 | +1.46% | +0.19% | 10.95x | 3.8 | 2026-11-26T17:11:28.462689+00:00 | Not calibrated | STRONG 85/100 | HIGH 55/100 | Watch | WATCH |
| 3 | QNT/USD | 149.81 | 79.112 | 66.015 | +3.46% | +0.29% | 2.16x | 4.7 | 2026-11-26T17:11:28.462689+00:00 | Not calibrated | STRONG 95/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | SKY/USD | 0.04576 | 78.934 | 76.385 | +9.26% | +0.26% | 1.12x | 6.6 | 2026-11-26T17:11:28.462689+00:00 | Not calibrated | STRONG 74/100 | HIGH 67/100 | Watch | WATCH |
| 5 | LTC/USD | 43.43 | 72.331 | 65.649 | +1.69% | +0.00% | 1.67x | 2.3 | 2026-11-26T17:11:28.462689+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 6 | STBL/USD | 0.020283 | 66.143 | 74.256 | +7.40% | +0.04% | 0.17x | 3.5 | 2026-11-26T17:11:28.462689+00:00 | Not calibrated | MODERATE 53/100 | VERY_HIGH 82/100 | Watch | WATCH |
| 7 | XRP/USD | 0.95001 | 65.650 | 65.000 | +1.44% | +0.26% | 0.94x | 0.1 | 2026-11-26T17:11:28.462689+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 8 | SOL/USD | 71.04 | 64.524 | 60.760 | +0.92% | +0.34% | 1.21x | 1.4 | 2026-11-26T17:11:28.462689+00:00 | Not calibrated | MODERATE 67/100 | HIGH 62/100 | Watch | WATCH |
| 9 | ADA/USD | 0.14883 | 63.536 | 68.115 | +2.10% | +0.34% | 0.37x | 3.2 | 2026-11-26T17:11:28.462689+00:00 | Not calibrated | MODERATE 62/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | ONDO/USD | 0.28622 | 58.380 | 42.733 | +1.32% | +0.13% | 2.65x | 0.4 | 2026-11-26T17:11:28.462689+00:00 | Not calibrated | STRONG 74/100 | HIGH 60/100 | Watch | WATCH |
| 11 | NEAR/USD | 3.0672 | 52.051 | 57.174 | +0.57% | +0.41% | 0.28x | 3.6 | 2026-11-26T17:11:28.462689+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | HBAR/USD | 0.05372 | 51.214 | 56.748 | +3.11% | +0.24% | 0.33x | 1.9 | 2026-11-26T17:11:28.462689+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 75/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | SKY/USD | 76.385 | 0.04576 | +0.26% | 1.12x |
| 2 | STBL/USD | 74.256 | 0.020283 | +0.04% | 0.17x |
| 3 | WIF/USD | 72.781 | 0.1359 | +0.66% | 1.95x |
| 4 | ADA/USD | 68.115 | 0.14883 | +0.34% | 0.37x |
| 5 | QNT/USD | 66.015 | 149.81 | +0.29% | 2.16x |
| 6 | LTC/USD | 65.649 | 43.43 | +0.00% | 1.67x |
| 7 | XRP/USD | 65.000 | 0.95001 | +0.26% | 0.94x |
| 8 | LINK/USD | 63.355 | 9.1767 | +0.19% | 10.95x |
| 9 | SOL/USD | 60.760 | 71.04 | +0.34% | 1.21x |
| 10 | NEAR/USD | 57.174 | 3.0672 | +0.41% | 0.28x |
| 11 | HBAR/USD | 56.748 | 0.05372 | +0.24% | 0.33x |
| 12 | ONDO/USD | 42.733 | 0.28622 | +0.13% | 2.65x |

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

- Persisted scans: 1889; predictions: 16403; observations: 1144487.
- Matured sampled outcomes across 1/6/24/48h: 35450; gap abstentions: 25088. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45865288256 · **Generation:** 1889 · **Legacy run:** 45865288256
**Main quote time:** 2026-11-26T17:11:36.123403+00:00 · **Legacy report time:** 2026-11-26T17:12:26.864222+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | WIF/USD | 0.1359 | 85.58 | +0.66% | 1.95x | STRONG 88/100 | HIGH 67/100 | Consider small entry |
| 2 | LINK/USD | 9.1767 | 79.28 | +0.19% | 10.95x | STRONG 85/100 | HIGH 55/100 | Watch |
| 3 | QNT/USD ⭐ | 149.81 | 79.11 | +0.29% | 2.16x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | SKY/USD ⭐ | 0.04576 | 78.93 | +0.26% | 1.12x | STRONG 84/100 | HIGH 67/100 | Watch |
| 5 | LTC/USD | 43.43 | 72.33 | +0.00% | 1.67x | STRONG 71/100 | HIGH 55/100 | Watch |
| 6 | STBL/USD | 0.020283 | 66.14 | +0.04% | 0.17x | MODERATE 53/100 | VERY_HIGH 82/100 | Watch |
| 7 | XRP/USD | 0.95001 | 65.65 | +0.26% | 0.94x | MODERATE 63/100 | HIGH 62/100 | Watch |
| 8 | SOL/USD | 71.04 | 64.52 | +0.34% | 1.21x | MODERATE 67/100 | HIGH 62/100 | Watch |
| 9 | ADA/USD | 0.14883 | 63.54 | +0.34% | 0.37x | MODERATE 62/100 | VERY_HIGH 70/100 | Watch |
| 10 | ONDO/USD | 0.28622 | 58.38 | +0.13% | 2.65x | STRONG 74/100 | HIGH 60/100 | Watch |
| 11 | NEAR/USD | 3.0672 | 52.05 | +0.41% | 0.28x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 12 | HBAR/USD | 0.05372 | 51.21 | +0.24% | 0.33x | MODERATE 56/100 | VERY_HIGH 75/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | QNT/USD ⭐ | 149.77 | 86.85 | +0.29% | 2.16x | 7443 | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 2 | PIEVERSE/USD | 4.0198 | 82.68 | +0.60% | 2.14x | 3403 | STRONG 91/100 | HIGH 61/100 | Consider small entry |
| 3 | AKT/USD | 0.4995 | 81.34 | +0.93% | 2.69x | 2784 | STRONG 91/100 | HIGH 66/100 | Consider small entry |
| 4 | APT/USD | 0.3858 | 78.19 | +0.39% | 29.42x | 2422 | STRONG 94/100 | HIGH 60/100 | Consider small entry |
| 5 | SKY/USD ⭐ | 0.04586 | 76.00 | +0.26% | 1.12x | 6360 | STRONG 83/100 | HIGH 67/100 | Watch |

**Same-run overlap:** QNT/USD, SKY/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
