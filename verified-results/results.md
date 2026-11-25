# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-25T21:56:07.109362+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/45708585882
**Source SHA:** 858c8bc8ec5d7641ddb39cacd8aca91719f855b1
**Previous ledger commit:** 764e3bd7e108e1c00fc9ba8a9b0df0ccebd204e5 (atomic ledger/results publication)
**Ledger generation:** 1772 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 9s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 628; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 610; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.0258 | 96.607 | 87.969 | +4.90% | +0.17% | 1.78x | 2.6 | 2026-11-25T21:55:58.113736+00:00 | Not calibrated | STRONG 83/100 | HIGH 55/100 | Watch | WATCH |
| 2 | ZEC/USD | 762.09 | 82.145 | 76.388 | +3.14% | -0.13% | 1.64x | 1.2 | 2026-11-25T21:55:58.113736+00:00 | Not calibrated | MODERATE 61/100 | HIGH 61/100 | Watch | WATCH |
| 3 | HYPE/USD | 61.78 | 78.091 | 76.522 | +3.19% | -0.21% | 1.26x | 1.6 | 2026-11-25T21:55:58.113736+00:00 | Not calibrated | MODERATE 49/100 | HIGH 61/100 | Watch | WATCH |
| 4 | SUI/USD | 0.6634 | 77.251 | 70.682 | +2.46% | -0.03% | 1.67x | 3.0 | 2026-11-25T21:55:58.113736+00:00 | Not calibrated | MODERATE 59/100 | HIGH 61/100 | Watch | WATCH |
| 5 | LTC/USD | 42.51 | 76.833 | 82.269 | +4.06% | +0.00% | 0.46x | 2.4 | 2026-11-25T21:55:58.113736+00:00 | Not calibrated | MODERATE 58/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 6 | XMR/USD | 522.8 | 73.460 | 72.654 | +2.59% | +0.03% | 1.07x | 1.0 | 2026-11-25T21:55:58.113736+00:00 | Not calibrated | MODERATE 62/100 | HIGH 62/100 | Watch | WATCH |
| 7 | XRP/USD | 0.94038 | 65.639 | 67.657 | +1.82% | -0.20% | 0.90x | 0.1 | 2026-11-25T21:55:58.113736+00:00 | Not calibrated | WEAK 38/100 | HIGH 68/100 | Watch | WATCH |
| 8 | PUMP/USD | 0.002534 | 63.711 | 68.028 | +3.90% | -0.63% | 0.88x | 3.9 | 2026-11-25T21:55:58.113736+00:00 | Not calibrated | WEAK 37/100 | HIGH 68/100 | Watch | WATCH |
| 9 | ETH/USD | 1685.78 | 63.129 | 58.337 | +0.48% | -0.13% | 1.54x | 0.1 | 2026-11-25T21:55:58.113736+00:00 | Not calibrated | MODERATE 52/100 | HIGH 61/100 | Watch | WATCH |
| 10 | XAUT/USD | 3574.3 | 61.806 | 46.106 | +1.04% | +0.14% | 3.13x | 0.3 | 2026-11-25T21:55:58.113736+00:00 | Not calibrated | STRONG 76/100 | HIGH 55/100 | Watch | WATCH |
| 11 | SOL/USD | 70.63 | 60.327 | 64.651 | +1.48% | -0.24% | 0.69x | 1.4 | 2026-11-25T21:55:58.113736+00:00 | Not calibrated | WEAK 35/100 | VERY_HIGH 76/100 | Watch | WATCH |
| 12 | ADA/USD | 0.146465 | 57.910 | 65.203 | +1.46% | -0.18% | 0.36x | 0.1 | 2026-11-25T21:55:58.113736+00:00 | Not calibrated | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 87.969 | 3.0258 | +0.17% | 1.78x |
| 2 | LTC/USD | 82.269 | 42.51 | +0.00% | 0.46x |
| 3 | HYPE/USD | 76.522 | 61.78 | -0.21% | 1.26x |
| 4 | ZEC/USD | 76.388 | 762.09 | -0.13% | 1.64x |
| 5 | XMR/USD | 72.654 | 522.8 | +0.03% | 1.07x |
| 6 | SUI/USD | 70.682 | 0.6634 | -0.03% | 1.67x |
| 7 | PUMP/USD | 68.028 | 0.002534 | -0.63% | 0.88x |
| 8 | XRP/USD | 67.657 | 0.94038 | -0.20% | 0.90x |
| 9 | ADA/USD | 65.203 | 0.146465 | -0.18% | 0.36x |
| 10 | SOL/USD | 64.651 | 70.63 | -0.24% | 0.69x |
| 11 | ETH/USD | 58.337 | 1685.78 | -0.13% | 1.54x |
| 12 | XAUT/USD | 46.106 | 3574.3 | +0.14% | 3.13x |

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

- Persisted scans: 1772; predictions: 15008; observations: 1074192.
- Matured sampled outcomes across 1/6/24/48h: 32762; gap abstentions: 23185. Per-horizon counts require independent audit; do not infer held-out lift.
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

**Writer:** 45708585882 · **Generation:** 1772 · **Legacy run:** 45708585882
**Main quote time:** 2026-11-25T21:56:07.109362+00:00 · **Legacy report time:** 2026-11-25T21:57:14.251148+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.0258 | 96.61 | +0.17% | 1.78x | STRONG 93/100 | HIGH 55/100 | Watch |
| 2 | ZEC/USD | 762.09 | 82.15 | -0.13% | 1.64x | MODERATE 61/100 | HIGH 61/100 | Watch |
| 3 | HYPE/USD | 61.78 | 78.09 | -0.21% | 1.26x | MODERATE 49/100 | HIGH 61/100 | Watch |
| 4 | SUI/USD | 0.6634 | 77.25 | -0.03% | 1.67x | MODERATE 59/100 | HIGH 61/100 | Watch |
| 5 | LTC/USD | 42.51 | 76.83 | +0.00% | 0.46x | MODERATE 58/100 | VERY_HIGH 70/100 | Watch |
| 6 | XMR/USD | 522.8 | 73.46 | +0.03% | 1.07x | MODERATE 62/100 | HIGH 62/100 | Watch |
| 7 | XRP/USD | 0.94038 | 65.64 | -0.20% | 0.90x | WEAK 38/100 | HIGH 68/100 | Watch |
| 8 | PUMP/USD | 0.002534 | 63.71 | -0.63% | 0.88x | WEAK 37/100 | HIGH 68/100 | Watch |
| 9 | ETH/USD | 1685.78 | 63.13 | -0.13% | 1.54x | MODERATE 52/100 | HIGH 61/100 | Watch |
| 10 | XAUT/USD | 3574.3 | 61.81 | +0.14% | 3.13x | STRONG 76/100 | HIGH 55/100 | Watch |
| 11 | SOL/USD | 70.63 | 60.33 | -0.24% | 0.69x | WEAK 35/100 | VERY_HIGH 76/100 | Watch |
| 12 | ADA/USD | 0.146465 | 57.91 | -0.18% | 0.36x | WEAK 34/100 | VERY_HIGH 76/100 | Do nothing |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD ⭐ | 3.0315 | 97.01 | +0.17% | 1.78x | 16844 | STRONG 94/100 | HIGH 55/100 | Watch |

**Same-run overlap:** NEAR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
