# Kraken paper scanner — verified results

**Scan:** SUCCESS — PAPER ONLY, no trades or approved BUY orders

**UTC as-of:** 2026-11-19T04:25:20.713251+00:00
**GitHub trigger:** manual dispatch (verified event=workflow_dispatch; no scheduled slot; actual start punctuality NOT verified)
**GitHub run:** https://github.com/michaelrobinsonproduct-del/Cryptoscanner/actions/runs/44458117390
**Source SHA:** b271b90a2cae9e5307600070ce7d0e510fe68996
**Previous ledger commit:** edc72d57557487f1415463dacd5a4368f7ec39a1 (atomic ledger/results publication)
**Ledger generation:** 754 (remote push/readback verified)

**Freshness:** Kraken public ticker client-observed, max quote age 8s (limit 600s). Ticker exchange-event freshness is NOT independently proven.
**Kraken online /USD pairs:** 627; stablecoin-base exclusions: 18; other suffix exclusions: 0; eligible pairs: 609; valid market observations: 609; OHLC screened: 24.

## Challenger-ranked WATCH candidates — paper only

| # | Symbol | Price USD | Challenger score | Baseline score | Since UTC open | 15m move | Volume accel | Spread bps | Quote UTC | 30% / 48h odds | Signal confidence | Risk | Guidance | Status |
|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | NEAR/USD | 3.4175 | 92.205 | 78.447 | +3.64% | -0.25% | 4.04x | 4.1 | 2026-11-19T04:25:13.130201+00:00 | Not calibrated | STRONG 76/100 | HIGH 61/100 | Watch | WATCH |
| 2 | ETH/USD | 1796.61 | 78.318 | 63.590 | +1.23% | -0.05% | 2.83x | 0.1 | 2026-11-19T04:25:13.130201+00:00 | Not calibrated | MODERATE 69/100 | HIGH 61/100 | Watch | WATCH |
| 3 | HYPE/USD | 67.67 | 78.004 | 61.791 | +1.18% | +0.37% | 2.44x | 3.0 | 2026-11-19T04:25:13.130201+00:00 | Not calibrated | STRONG 94/100 | HIGH 55/100 | Consider small entry | WATCH |
| 4 | XRP/USD | 0.97192 | 74.144 | 58.969 | +0.57% | +0.04% | 2.62x | 0.1 | 2026-11-19T04:25:13.130201+00:00 | Not calibrated | STRONG 82/100 | HIGH 55/100 | Watch | WATCH |
| 5 | SOL/USD | 74.43 | 72.509 | 62.800 | +1.21% | +0.16% | 1.89x | 1.3 | 2026-11-19T04:25:13.130201+00:00 | Not calibrated | STRONG 71/100 | HIGH 55/100 | Watch | WATCH |
| 6 | LUNA/USD | 4.847e-05 | 71.636 | 69.980 | +11.32% | -0.41% | 1.37x | 16.5 | 2026-11-19T04:25:13.130201+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 72/100 | Watch | WATCH |
| 7 | TAO/USD | 194.9298 | 69.517 | 62.884 | +1.55% | -0.15% | 1.74x | 5.9 | 2026-11-19T04:25:13.130201+00:00 | Not calibrated | MODERATE 55/100 | HIGH 61/100 | Watch | WATCH |
| 8 | VVV/USD | 22.496 | 68.449 | 73.721 | +3.81% | +0.10% | 0.42x | 9.3 | 2026-11-19T04:25:13.130201+00:00 | Not calibrated | MODERATE 54/100 | VERY_HIGH 70/100 | Watch | WATCH |
| 9 | XBT/USD | 63331.1 | 68.076 | 58.844 | +0.55% | +0.02% | 1.91x | 0.0 | 2026-11-19T04:25:13.130201+00:00 | Not calibrated | MODERATE 69/100 | HIGH 55/100 | Watch | WATCH |
| 10 | XDG/USD | 0.0591179 | 67.965 | 54.372 | +0.70% | +0.10% | 2.31x | 0.0 | 2026-11-19T04:25:13.130201+00:00 | Not calibrated | STRONG 79/100 | HIGH 55/100 | Watch | WATCH |
| 11 | PYTH/USD | 0.05573 | 67.672 | 64.072 | +5.63% | +0.38% | 1.17x | 14.4 | 2026-11-19T04:25:13.130201+00:00 | Not calibrated | MODERATE 64/100 | VERY_HIGH 73/100 | Watch | WATCH |
| 12 | ZEC/USD | 928.14 | 62.266 | 65.758 | +1.78% | +0.16% | 0.57x | 3.3 | 2026-11-19T04:25:13.130201+00:00 | Not calibrated | MODERATE 51/100 | VERY_HIGH 70/100 | Watch | WATCH |

## Baseline ranking (same verified WATCH pool)

| # | Symbol | Baseline score | Price USD | 15m move | Volume accel |
|---:|---|---:|---:|---:|---:|
| 1 | NEAR/USD | 78.447 | 3.4175 | -0.25% | 4.04x |
| 2 | VVV/USD | 73.721 | 22.496 | +0.10% | 0.42x |
| 3 | LUNA/USD | 69.980 | 4.847e-05 | -0.41% | 1.37x |
| 4 | ZEC/USD | 65.758 | 928.14 | +0.16% | 0.57x |
| 5 | PYTH/USD | 64.072 | 0.05573 | +0.38% | 1.17x |
| 6 | ETH/USD | 63.590 | 1796.61 | -0.05% | 2.83x |
| 7 | TAO/USD | 62.884 | 194.9298 | -0.15% | 1.74x |
| 8 | SOL/USD | 62.800 | 74.43 | +0.16% | 1.89x |
| 9 | HYPE/USD | 61.791 | 67.67 | +0.37% | 2.44x |
| 10 | XRP/USD | 58.969 | 0.97192 | +0.04% | 2.62x |
| 11 | XBT/USD | 58.844 | 63331.1 | +0.02% | 1.91x |
| 12 | XDG/USD | 54.372 | 0.0591179 | +0.10% | 2.31x |

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

- Persisted scans: 754; predictions: 6192; observations: 456192.
- Matured sampled outcomes across 1/6/24/48h: 6166; gap abstentions: 13649. Per-horizon counts require independent audit; do not infer held-out lift.
- Observed +30% hits: 10 (sampled only; not a success-rate estimate).
- False positives / missed movers: NOT VERIFIED without eligible continuous outcome coverage.
- Baseline vs challenger: recorded as-of; unbiased held-out lift NOT MEASURED.
- Online Kraken /USD stablecoin-base pairs excluded: 18 (counted from this scan's online AssetPairs metadata, not inferred from price).
- Stablecoin base exclusions: BRL1, BUSD, DAI, EUR, EURC, EUROP, EURQ, EURR, EURT, FDUSD, FRAX, GUSD, PYUSD, QCAD, RLUSD, TGBP, TUSD, USD, USD1, USDC, USDD, USDE, USDG, USDQ, USDR, USDS, USDT, ZUSD.
- DEX: NOT USED; no DEX freshness gate.
- OHLC screening abstentions: 10; details in immutable scan JSON artifact.
- Storage: ledger and results published in one non-force Git commit and read back. Independent artifact recovery is NOT VERIFIED by this scan alone.
- Errors: none in successful committed scan; a failed workflow must not publish a SUCCESS report.

# Cryptoscanner — challenger and independent legacy-inspired WATCH

Paper only · risk is high or higher · 30%+ in 48h probability NOT CALIBRATED
Signal confidence 0–100 means setup strength only, NOT a win probability. Actions are research guidance; no trade authorization.

**Writer:** 44458117390 · **Generation:** 754 · **Legacy run:** 44458117390
**Main quote time:** 2026-11-19T04:25:20.713251+00:00 · **Legacy report time:** 2026-11-19T04:25:53.997732+00:00

## Challenger-scored WATCH (original canonical scanner)
| # | Symbol | USD | Challenger score | 15m move | Volume x | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---|---|---|
| 1 | NEAR/USD | 3.4175 | 92.21 | -0.25% | 4.04x | STRONG 76/100 | HIGH 61/100 | Watch |
| 2 | ETH/USD | 1796.61 | 78.32 | -0.05% | 2.83x | MODERATE 69/100 | HIGH 61/100 | Watch |
| 3 | HYPE/USD ⭐ | 67.67 | 78.00 | +0.37% | 2.44x | STRONG 100/100 | HIGH 55/100 | Consider small entry |
| 4 | XRP/USD | 0.97192 | 74.14 | +0.04% | 2.62x | STRONG 82/100 | HIGH 55/100 | Watch |
| 5 | SOL/USD ⭐ | 74.43 | 72.51 | +0.16% | 1.89x | STRONG 81/100 | HIGH 55/100 | Watch |
| 6 | LUNA/USD | 4.847e-05 | 71.64 | -0.41% | 1.37x | MODERATE 51/100 | VERY_HIGH 72/100 | Watch |
| 7 | TAO/USD | 194.9298 | 69.52 | -0.15% | 1.74x | MODERATE 55/100 | HIGH 61/100 | Watch |
| 8 | VVV/USD | 22.496 | 68.45 | +0.10% | 0.42x | MODERATE 54/100 | VERY_HIGH 70/100 | Watch |
| 9 | XBT/USD | 63331.1 | 68.08 | +0.02% | 1.91x | MODERATE 69/100 | HIGH 55/100 | Watch |
| 10 | XDG/USD | 0.0591179 | 67.97 | +0.10% | 2.31x | STRONG 79/100 | HIGH 55/100 | Watch |
| 11 | PYTH/USD ⭐ | 0.05573 | 67.67 | +0.38% | 1.17x | STRONG 74/100 | VERY_HIGH 73/100 | Watch |
| 12 | ZEC/USD | 928.14 | 62.27 | +0.16% | 0.57x | MODERATE 51/100 | VERY_HIGH 70/100 | Watch |

## Independent legacy-inspired WATCH (separate Kraken sampling)
| # | Symbol | USD | Legacy score | 15m move | Volume x | Trades 24h | Confidence | Risk | Action |
|---:|---|---:|---:|---:|---:|---:|---|---|---|
| 1 | SOL/USD ⭐ | 74.44 | 68.04 | +0.16% | 1.89x | 34996 | STRONG 79/100 | HIGH 55/100 | Watch |
| 2 | PYTH/USD ⭐ | 0.05573 | 67.88 | +0.38% | 1.17x | 2034 | STRONG 74/100 | VERY_HIGH 73/100 | Watch |
| 3 | HYPE/USD ⭐ | 67.69 | 67.48 | +0.37% | 2.44x | 14528 | STRONG 99/100 | HIGH 55/100 | Consider small entry |

**Same-run overlap:** HYPE/USD, SOL/USD, PYTH/USD
A ⭐ means both independently executed scanners identified the exact same /USD market.
Legacy is rebuild-v2-inspired, not the original scanner. Rankings are uncalibrated.
More substantial entry requires independently qualified, calibrated 48h held-out outcome evidence.
Risk drivers and 30% target caveat are in each candidate guidance object.
Freshness must be checked using each candidate's quote_observed_at at delivery.
Read-only learning is separate; no production-scoring promotion or trading.
