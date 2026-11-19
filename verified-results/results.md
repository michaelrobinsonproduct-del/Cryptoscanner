# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T00:45:15.908753+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44431443719
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** 1f16a0afbed8da40cbb9289ea3ebe9b23735c666 (atomic ledger/results publication)
**Ledger generation:** 710 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 6s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | SUI/USD | 0.721 | 67.376 | 56.351 | +0.29% | +0.47% | 1.87x | 1.4 | 2026-11-19T00:45:09.425706+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 2 | PAXG/USD | 3745.35 | 61.420 | 45.175 | +0.38% | +0.25% | 5.02x | 0.0 | 2026-11-19T00:45:09.425706+00:00 | Not calibrated | STRONG 86/100 | HIGH 55/100 | Watch | WATCH |
| 3 | NEAR/USD | 3.3305 | 58.559 | 59.775 | +1.00% | +0.93% | 0.41x | 4.5 | 2026-11-19T00:45:09.425706+00:00 | Not calibrated | MODERATE 59/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 4 | ETH/USD | 1781.29 | 58.317 | 57.547 | +0.37% | +0.31% | 0.92x | 0.1 | 2026-11-19T00:45:09.425706+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 5 | HYPE/USD | 67.05 | 57.835 | 56.034 | +0.25% | +0.46% | 0.95x | 1.5 | 2026-11-19T00:45:09.425706+00:00 | Not calibrated | MODERATE 59/100 | HIGH 62/100 | Watch | WATCH |
| 6 | TRX/USD | 0.310472 | 57.700 | 41.742 | +0.39% | +0.19% | 3.62x | 0.0 | 2026-11-19T00:45:09.425706+00:00 | Not calibrated | STRONG 74/100 | HIGH 55/100 | Watch | WATCH |
| 7 | ADA/USD | 0.151704 | 56.794 | 55.632 | +0.30% | +0.33% | 0.95x | 2.9 | 2026-11-19T00:45:09.425706+00:00 | Not calibrated | MODERATE 58/100 | HIGH 62/100 | Watch | WATCH |
| 8 | XMR/USD | 506.18 | 56.659 | 54.345 | +0.29% | +0.43% | 1.02x | 5.3 | 2026-11-19T00:45:09.425706+00:00 | Not calibrated | MODERATE 63/100 | HIGH 62/100 | Watch | WATCH |
| 9 | LINK/USD | 9.10716 | 54.390 | 55.527 | +0.38% | +0.68% | 0.55x | 4.3 | 2026-11-19T00:45:09.425706+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 10 | TAO/USD | 192.6861 | 53.331 | 54.648 | +0.38% | +0.49% | 0.62x | 6.0 | 2026-11-19T00:45:09.425706+00:00 | Not calibrated | MODERATE 57/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 11 | ZEC/USD | 917.75 | 52.913 | 58.962 | +0.64% | +0.56% | 0.11x | 1.0 | 2026-11-19T00:45:09.425706+00:00 | Not calibrated | MODERATE 56/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 12 | VVV/USD | 22.038 | 50.576 | 53.033 | +1.69% | +1.22% | 0.14x | 14.1 | 2026-11-19T00:45:09.425706+00:00 | Not calibrated | MODERATE 50/100 | VERY_HIGH 76/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 59.775 | 3.3305 | +0.93% | 0.41x |
| 2 | ZEC/USD | 58.962 | 917.75 | +0.56% | 0.11x |
| 3 | ETH/USD | 57.547 | 1781.29 | +0.31% | 0.92x |
| 4 | SUI/USD | 56.351 | 0.721 | +0.47% | 1.87x |
| 5 | HYPE/USD | 56.034 | 67.05 | +0.46% | 0.95x |
| 6 | ADA/USD | 55.632 | 0.151704 | +0.33% | 0.95x |
| 7 | LINK/USD | 55.527 | 9.10716 | +0.68% | 0.55x |
| 8 | TAO/USD | 54.648 | 192.6861 | +0.49% | 0.62x |
| 9 | XMR/USD | 54.345 | 506.18 | +0.43% | 1.02x |
| 10 | VVV/USD | 53.033 | 22.038 | +1.22% | 0.14x |
| 11 | PAXG/USD | 45.175 | 3745.35 | +0.25% | 5.02x |
| 12 | TRX/USD | 41.742 | 0.310472 | +0.19% | 3.62x |

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

- Persisted scans: 710; predictions: 5745; observations: 429397.
- Matured sampled outcomes across 1/6/24/48h: 5639; gap abstentions: 13410. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 5; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44431443719 · **Generation:** 710 · **Legacy run:** 44431443719
**Main quote time:** 2026-11-19T00:45:15.908753+00:00 · **Legacy report time:** 2026-11-19T00:45:50.203310+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | SUI/USD | 0.721 | 67.38 | +0.47% | 1.87x | STRONG 79/100 | HIGH 55/100 | Watch |
| 2 | PAXG/USD | 3745.35 | 61.42 | +0.25% | 5.02x | STRONG 86/100 | HIGH 55/100 | Watch |
| 3 | NEAR/USD | 3.3305 | 58.56 | +0.93% | 0.41x | MODERATE 59/100 | VERY_HIGH 70/100 | Watch |
| 4 | ETH/USD | 1781.29 | 58.32 | +0.31% | 0.92x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 5 | HYPE/USD | 67.05 | 57.84 | +0.46% | 0.95x | MODERATE 59/100 | HIGH 62/100 | Watch |
| 6 | TRX/USD | 0.310472 | 57.70 | +0.19% | 3.62x | STRONG 74/100 | HIGH 55/100 | Watch |
| 7 | ADA/USD | 0.151704 | 56.79 | +0.33% | 0.95x | MODERATE 58/100 | HIGH 62/100 | Watch |
| 8 | XMR/USD ⭐ | 506.18 | 56.66 | +0.43% | 1.02x | STRONG 73/100 | HIGH 62/100 | Watch |
| 9 | LINK/USD | 9.10716 | 54.39 | +0.68% | 0.55x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 10 | TAO/USD | 192.6861 | 53.33 | +0.49% | 0.62x | MODERATE 57/100 | VERY_HIGH 70/100 | Watch |
| 11 | ZEC/USD | 917.75 | 52.91 | +0.56% | 0.11x | MODERATE 56/100 | VERY_HIGH 70/100 | Watch |
| 12 | VVV/USD | 22.038 | 50.58 | +1.22% | 0.14x | MODERATE 50/100 | VERY_HIGH 76/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SENT/USD | 0.021156 | 58.56 | +0.51% | 1.33x | 7029 | STRONG 74/100 | HIGH 67/100 | Watch |
| 2 | XMR/USD ⭐ | 506.45 | 57.05 | +0.43% | 1.02x | 11913 | STRONG 74/100 | HIGH 62/100 | Watch |
| 3 | XRP/USD | 0.96887 | 55.42 | +0.37% | 1.26x | 33914 | MODERATE 63/100 | HIGH 55/100 | Watch |
| 4 | XLM/USD | 0.137399 | 52.00 | +0.20% | 1.30x | 9186 | STRONG 71/100 | HIGH 55/100 | Watch |

**Same-run overlap:** XMR/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
